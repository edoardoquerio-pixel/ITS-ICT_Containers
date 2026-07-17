# Microservizi Libreria --- Ottimizzazioni e Migliorie

**Data:** 2026-07-17
**Progetto:** 17_Container_Docker_Kubernetes/02_Esercizi
**Autore:** Edoardo Querio Gianetto

---

## 1. Contesto

Sistema di gestione libreria composto da 7 microservizi containerizzati (6 FastAPI + 1 nginx API Gateway), orchestrati con Docker Compose. Ogni servizio ha il proprio database PostgreSQL, ma attualmente solo `book-service` utilizza SQLAlchemy + PostgreSQL; gli altri 5 servizi (user, loan, review, inventory, notification) usano storage in-memory nonostante abbiano gia la struttura SQLAlchemy completa.

Gli unici test automatizzati sono per `book-service` (42 test pytest). Solo `book-service` ha manifest Kubernetes.

Il progetto e sia un esercizio didattico per il corso ITS Cloud Specialist sia una potenziale base per un deploy reale.

---

## 2. Priorita --- Percorso consigliato

| Priorita | Area | Sforzo | Impatto |
|----------|------|--------|---------|
| 1 | B --- PostgreSQL per tutti i servizi | ~2-3h | Alto |
| 2 | E --- Comunicazione inter-servizio | ~3-4h | Alto |
| 3 | A --- Testing automatizzato per tutti | ~2h | Alto |
| 4 | Kubernetes completo | ~4-6h | Medio |
| 5 | CI/CD (GitHub Actions) | ~2-3h | Medio |
| 6 | Healthcheck + Readiness robusti | ~1h | Medio |
| 7 | Migliorie Docker/Dockerfile | ~1h | Basso |
| 8 | Sicurezza (env, secrets, rate limiting) | ~2h | Medio |
| 9 | Monitoring & Logging | ~3-4h | Medio |
| 10 | Performance & Scalabilita (async, Redis) | ~3h | Basso |
| 11 | Costi Cloud | ~1h | Basso |
| 12 | Documentazione per servizio | ~2h | Basso |

---

## 3. Fase 1 --- B: PostgreSQL per tutti i servizi

### Obiettivo
Convertire user-service, loan-service, review-service, inventory-service e notification-service da storage in-memory a PostgreSQL con SQLAlchemy, seguendo esattamente il pattern gia implementato in book-service.

### Stato attuale
Ogni servizio ha gia la struttura a 4 layer pronta:
- `app/models/models.py` --- modelli ORM SQLAlchemy
- `app/schemas/schemas.py` --- schemi Pydantic
- `app/repositories/repository.py` --- CRUD SQLAlchemy
- `app/services/service.py` --- logica di business
- `app/database/database.py` --- engine, sessione, init
- `app/config/__init__.py` --- Settings con dual-database (sqlite/postgres)
- `app/api/routes.py` --- endpoint FastAPI

### Cosa manca
I services/repository attuali usano liste Python in-memory invece di SQLAlchemy. I database PostgreSQL sono gia definiti in `docker-compose.yml` con reti isolate (`internal: true`).

### Azioni
1. Sostituire repository in-memory con repository SQLAlchemy (stesso pattern di book-service)
2. Aggiornare i services per usare i repository SQLAlchemy con Dependency Injection
3. Collegare le route ai services via Depends(get_db)
4. Verificare che docker-compose punti ai DB corretti
5. Testare con curl tramite API gateway

### Schema reti
Ogni servizio ha gia:
- Una rete `microservice-network` condivisa (per API gateway)
- Una rete DB `internal: true` isolata

---

## 4. Fase 2 --- E: Comunicazione inter-servizio

### Obiettivo
Collegare i servizi tra loro per operazioni che richiedono coordinamento. Approccio iniziale: chiamate HTTP sincrone via `httpx.AsyncClient`.

### Flussi da implementare

#### 4.1 loan --> book (verifica disponibilita + aggiornamento)
- **POST /loans/** --> loan-service chiama GET /books/{book_id} su book-service per verificare che il libro esista e sia disponibile=true
  - Se OK: crea prestito, poi chiama PUT /books/{book_id} con disponibile=false
  - Se KO: rifiuta prestito con errore
- **PUT /loans/{id}/return** --> loan-service chiama PUT /books/{book_id} con disponibile=true

#### 4.2 loan --> inventory (decremento stock)
- **POST /loans/** --> loan-service chiama GET /inventory/{book_id} per verificare stock > 0
  - Se OK: chiama POST /inventory/{book_id} per decrementare
  - Se KO: rifiuta prestito
- **PUT /loans/{id}/return** --> reintegra stock

#### 4.3 loan --> notification (notifica evento)
- **POST /loans/** --> loan-service invia notifica "Prestito effettuato" a notification-service
- **PUT /loans/{id}/return** --> notifica "Restituzione avvenuta"

#### 4.4 review --> book (verifica esistenza)
- **POST /reviews/** --> review-service verifica che book_id esista in book-service
  - Se inesistente --> 400 Bad Request

### Architettura di comunicazione

**Approccio scelto: HTTP sincrono con httpx**
- `httpx.AsyncClient` per chiamate asincrone non bloccanti
- Timeout configurabile (default 5s)
- Retry semplice (1-2 tentativi) per tolleranza
- Service discovery via DNS di Docker Compose (nome servizio = hostname)
- Variabili d'ambiente per URL dei servizi dipendenti

**Configurazione:**
```python
BOOK_SERVICE_URL = os.getenv("BOOK_SERVICE_URL", "http://book-service:8000")
INVENTORY_SERVICE_URL = os.getenv("INVENTORY_SERVICE_URL", "http://inventory-service:8000")
NOTIFICATION_SERVICE_URL = os.getenv("NOTIFICATION_SERVICE_URL", "http://notification-service:8000")
```

### Gestione errori
- Timeout / connessione rifiutata --> risposta 503 con messaggio "servizio non disponibile"
- Servizio restituisce 404 --> propagare come 400/404 al client
- Fallimenti parziali --> rollback logico (es. loan creato ma notifica fallita, logga errore, non bloccare)

---

## 5. Fase 3 --- A: Testing automatizzato

### Obiettivo
Aggiungere pytest per tutti i 5 servizi convertiti, seguendo il pattern di book-service:
- SQLite in-memory per test (stessa configurazione gia usata da book-service)
- TestClient FastAPI per test di integrazione
- Fixtures per database e client

### Per ogni servizio
1. `conftest.py` con:
   - Fixture `db_session` (SQLite in-memory, tables create/drop per test)
   - Fixture `client` (TestClient con override dipendenze)
2. `test_routes.py` con:
   - Health check (/health, /ready)
   - CRUD base (create, list, get, update, delete)
   - Edge case (404, 422, duplicati)
   - Pattern identico a book-service

### Coverage target
- Copertura di tutti gli endpoint REST
- Test per flussi inter-servizio (Fase 2) usando mock delle chiamate HTTP

---

## 6. Fase 4+ --- Migliorie future

### 6.1 Kubernetes completo
- Namespace, Deployment, Service, ConfigMap per ogni servizio
- StatefulSet per PostgreSQL di ogni servizio
- Ingress Controller nginx per routing
- readinessProbe + livenessProbe per tutti

### 6.2 CI/CD (GitHub Actions)
- Build immagini Docker
- Esecuzione test (con servizio PostgreSQL come container)
- Push a GHCR (GitHub Container Registry)
- Deploy automatico su cluster K8s (dev)

### 6.3 Security hardening
- `.env` file per secret (password DB) invece di hard-coded
- Docker secrets per produzione
- Rate limiting nginx (limit_req_zone)
- HTTPS/TLS con Let's Encrypt

### 6.4 Monitoring
- Prometheus metrics endpoint per ogni servizio
- Grafana dashboard (richieste/sec, latenza, error rate)
- Logging strutturato uniforme
- OpenTelemetry tracing distribuito

### 6.5 Performance
- Endpoint async (async def) con sessioni SQLAlchemy asincrone
- Redis caching per catalogo libri
- Connection pooling ottimizzato

---

## 7. Struttura del progetto (dopo le modifiche)

```
02_Esercizi/
+-- docker-compose.yml               # Invariato (6 DB gia presenti)
+-- api-gateway/                     # Invariato
+-- book-service/                    # Gia completo
+-- user-service/                    # PostgreSQL + test
+-- loan-service/                    # PostgreSQL + test + HTTP client
+-- review-service/                  # PostgreSQL + test + HTTP client
+-- inventory-service/               # PostgreSQL + test
+-- notification-service/            # PostgreSQL + test
+-- docs/
|   +-- superpowers/
|       +-- specs/
|           +-- 2026-07-17-microservizi-ottimizzazioni-design.md
+-- Makefile                         # Aggiornato con nuovi target
```

---

## 8. Vincoli e principi

- **Nessuna rottura API pubblica** --- gli endpoint esistenti via gateway restano invariati
- **Stesso pattern di book-service** --- coerenza architetturale tra tutti i servizi
- **Nessuna dipendenza aggiuntiva** oltre a httpx per le chiamate HTTP
- **Dual-database** --- SQLite in-memory per test, PostgreSQL per produzione (stessa logica di book-service)
- **YAGNI** --- niente message broker, niente event sourcing, niente saga pattern. HTTP sincrono e sufficiente
