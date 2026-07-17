# Fase 2: Comunicazione Inter-Servizio — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Collegare i servizi tra loro via chiamate HTTP sincrone (httpx) per coordinare operazioni (verifica disponibilita libri, decremento stock, notifiche).

**Architecture:** Ogni servizio che ha dipendenze verso altri servizi acquisisce un client HTTP (httpx.AsyncClient) e chiama gli endpoint degli altri servizi via DNS di Docker Compose (nome-servizio:8000). Le URL dei servizi dipendenti vengono configurate via variabili d'ambiente.

**Tech Stack:** FastAPI, httpx, SQLAlchemy 2.0, PostgreSQL 16, Pydantic v2, Docker Compose, nginx

## Global Constraints

- Nessuna rottura API pubblica — gli endpoint esistenti via gateway restano invariati
- Timeout configurabile (default 5s) per chiamate HTTP
- Error handling: servizio non disponibile → 503, 404 → propagato
- Variabili d'ambiente per URL dei servizi dipendenti
- Solo HTTP sincrono (nessun message broker, nessun evento)

---

## Task 0: Preparazione ambiente

- [ ] **Step 1: Aggiungere httpx a tutti i servizi che faranno chiamate HTTP**

Aggiungere `httpx>=0.27.0` a `requirements.txt` di loan-service e review-service.

- [ ] **Step 2: Aggiungere URL dei servizi dipendenti alle config**

In `loan-service/app/config/__init__.py`, aggiungere:
```python
BOOK_SERVICE_URL: str = os.getenv("BOOK_SERVICE_URL", "http://book-service:8000")
INVENTORY_SERVICE_URL: str = os.getenv("INVENTORY_SERVICE_URL", "http://inventory-service:8000")
NOTIFICATION_SERVICE_URL: str = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8000")
```

In `review-service/app/config/__init__.py`, aggiungere:
```python
BOOK_SERVICE_URL: str = os.getenv("BOOK_SERVICE_URL", "http://book-service:8000")
```

---

## Task 1: loan-service → book-service (verifica disponibilita + aggiornamento)

**Files:**
- Modify: `loan-service/app/services/service.py`
- Add: `loan-service/app/services/client.py` (HTTP client)

- [ ] **Step 1: Creare HTTP client per loan-service**

Creare `loan-service/app/services/client.py`:
```python
"""HTTP client per comunicazione inter-servizio."""
import httpx
from app.config import settings

BOOK_SERVICE_URL = settings.BOOK_SERVICE_URL
INVENTORY_SERVICE_URL = settings.INVENTORY_SERVICE_URL
NOTIFICATION_SERVICE_URL = settings.NOTIFICATION_SERVICE_URL


async def check_book_exists(book_id: int) -> bool:
    """Verifica che un libro esista in book-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{BOOK_SERVICE_URL}/books/{book_id}")
            if resp.status_code == 200:
                data = resp.json()
                return data.get("disponibile", False)
            return False
        except httpx.RequestError:
            return False


async def set_book_availability(book_id: int, disponibile: bool) -> bool:
    """Aggiorna la disponibilita di un libro in book-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.put(
                f"{BOOK_SERVICE_URL}/books/{book_id}",
                json={"disponibile": disponibile},
            )
            return resp.status_code == 200
        except httpx.RequestError:
            return False


async def check_inventory(book_id: int, quantity: int = 1) -> bool:
    """Verifica che ci sia stock sufficiente in inventory-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{INVENTORY_SERVICE_URL}/inventory/{book_id}")
            if resp.status_code == 200:
                data = resp.json()
                return data.get("quantity", 0) >= quantity
            return True  # Se inventory non ha il book_id, permetti comunque
        except httpx.RequestError:
            return True  # Se inventory non risponde, permetti comunque


async def send_notification(user_id: int, channel: str, message: str) -> None:
    """Invia una notifica a notification-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            await client.post(
                f"{NOTIFICATION_SERVICE_URL}/notifications",
                json={"user_id": user_id, "channel": channel, "message": message},
            )
        except httpx.RequestError:
            pass  # Non bloccare il flusso principale se notifica fallisce
```

- [ ] **Step 2: Aggiornare loan-service/service.py**

Modificare `create_loan` per verificare disponibilita e stock, e aggiornare disponibilita dopo creazione:
```python
import asyncio
from app.services.client import (
    check_book_exists,
    check_inventory,
    set_book_availability,
    send_notification,
)


async def create_loan_async(db: Session, loan_in: LoanCreate) -> Loan:
    """Crea un prestito dopo aver verificato disponibilita e stock."""
    # 1. Verifica che il libro esista e sia disponibile
    available = await check_book_exists(loan_in.book_id)
    if not available:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Libro non disponibile per il prestito",
        )

    # 2. Verifica stock
    has_stock = await check_inventory(loan_in.book_id)
    if not has_stock:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Scorte insufficienti per il prestito",
        )

    # 3. Crea prestito
    loan = repository.create(db, loan_in)

    # 4. Aggiorna disponibilita libro (fire-and-forget)
    await set_book_availability(loan_in.book_id, False)

    # 5. Invia notifica (fire-and-forget)
    await send_notification(
        user_id=loan_in.user_id,
        channel="email",
        message=f"Prestito effettuato per libro ID {loan_in.book_id}",
    )

    return loan
```

- [ ] **Step 3: Aggiornare routes per usare versione async**

In `loan-service/app/api/routes.py`:
```python
@router.post("", response_model=Loan, status_code=status.HTTP_201_CREATED)
async def create_loan(loan_in: LoanCreate, db: Session = Depends(get_db)):
    return await loan_service.create_loan_async(db, loan_in)
```

- [ ] **Step 4: Stessa logica per return_loan**

In `loan-service/app/services/service.py`, aggiungere:
```python
async def return_loan_async(db: Session, loan_id: int) -> Loan:
    loan = repository.return_loan(db, loan_id)
    if not loan:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Prestito con id {loan_id} non trovato",
        )
    # Riabilita disponibilita libro
    await set_book_availability(loan.book_id, True)
    # Notifica
    await send_notification(
        user_id=loan.user_id,
        channel="email",
        message=f"Restituzione completata per libro ID {loan.book_id}",
    )
    return loan
```

---

## Task 2: review-service → book-service (verifica esistenza)

**Files:**
- Modify: `review-service/app/services/service.py`
- Modify: `review-service/app/services/client.py`
- Modify: `review-service/app/api/routes.py`

- [ ] **Step 1: Creare HTTP client per review-service**

In `review-service/app/services/client.py`:
```python
import httpx
from app.config import settings


async def check_book_exists(book_id: int) -> bool:
    """Verifica che un libro esista in book-service."""
    async with httpx.AsyncClient(timeout=5.0) as client:
        try:
            resp = await client.get(f"{settings.BOOK_SERVICE_URL}/books/{book_id}")
            return resp.status_code == 200
        except httpx.RequestError:
            return False
```

- [ ] **Step 2: Aggiornare review-service/service.py**

```python
async def create_review_async(db: Session, review_in: ReviewCreate) -> Review:
    # Verifica che il libro esista
    from app.services.client import check_book_exists
    exists = await check_book_exists(review_in.book_id)
    if not exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Il libro specificato non esiste",
        )
    return repository.create(db, review_in)
```

- [ ] **Step 3: Aggiornare route**

---

## Task 3: Aggiornare docker-compose per variabili d'ambiente

**Files:**
- Modify: `docker-compose.yml`

Aggiungere a `loan-service`:
```yaml
BOOK_SERVICE_URL: "http://book-service:8000"
INVENTORY_SERVICE_URL: "http://inventory-service:8000"
NOTIFICATION_SERVICE_URL: "http://notification-service:8000"
```

Aggiungere a `review-service`:
```yaml
BOOK_SERVICE_URL: "http://book-service:8000"
```

---

## Task 4: Test del flusso inter-servizio

- [ ] **Step 1: Build e riavvio**

```bash
docker compose up -d --build
```

- [ ] **Step 2: Test flusso completo**

```bash
# 1. Crea un libro disponibile
curl -s -X POST http://localhost/books/ -H "Content-Type: application/json" \
  -d '{"titolo":"Test","autore":"A","isbn":"9780000000001","disponibile":true}'

# 2. Imposta scorte
curl -s -X POST http://localhost/inventory -H "Content-Type: application/json" \
  -d '{"book_id":1,"quantity":5}'

# 3. Crea prestito (dovrebbe funzionare)
curl -s -X POST http://localhost/loans -H "Content-Type: application/json" \
  -d '{"user_id":1,"book_id":1}'

# 4. Verifica che il libro non sia piu disponibile
curl -s http://localhost/books/1 | python -c "import sys,json; print(json.load(sys.stdin)['disponibile'])"

# 5. Restituisci prestito
curl -s -X PUT http://localhost/loans/1/return

# 6. Verifica che il libro sia di nuovo disponibile
curl -s http://localhost/books/1 | python -c "import sys,json; print(json.load(sys.stdin)['disponibile'])"

# 7. Verifica notifiche create
curl -s http://localhost/notifications
```

- [ ] **Step 3: Test recensione su libro inesistente**

```bash
# Recensione su libro inesistente → 400
curl -s -o /dev/null -w "%{http_code}" -X POST http://localhost/reviews \
  -H "Content-Type: application/json" \
  -d '{"book_id":999,"user_id":1,"rating":3,"comment":"Test"}'
```

Expected: 400 (Bad Request)

---

## Task 5: Aggiornamento README e commit

- [ ] **Step 1: Aggiornare README con i nuovi flussi inter-servizio**

- [ ] **Step 2: Commit**

```bash
git add -A
git commit -m "feat: comunicazione inter-servizio via HTTP (httpx)"
```
