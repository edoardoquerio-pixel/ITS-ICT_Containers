# Fase 1: PostgreSQL per tutti i servizi — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Verificare che tutti e 5 i servizi (user, loan, review, inventory, notification) usino già PostgreSQL con SQLAlchemy, confermare che il docker-compose sia corretto, testare il sistema completo.

**Architecture:** Tutti i servizi hanno già la struttura a 4 layer (models, schemas, services, repository, database) con SQLAlchemy + dual-database. Il docker-compose.yml imposta DATABASE_TYPE=postgres per tutti i servizi. I database PostgreSQL sono già definiti come servizi separati con reti isolate.

**Tech Stack:** FastAPI, SQLAlchemy 2.0, PostgreSQL 16, Pydantic v2, Docker Compose, nginx

## Global Constraints

- Nessuna rottura API pubblica — gli endpoint esistenti via gateway restano invariati
- Tutti i servizi espongono /health e /ready
- Ogni servizio ha la propria rete DB isolata (internal: true)
- Docker Compose per orchestrazione locale

---

## Task 0: Audit — Stato attuale dei servizi

**Files:**
- Audit: tutti i file app/ di user-service, loan-service, review-service, inventory-service, notification-service
- Referenza: book-service (pattern di riferimento)

**Interfaces:**
- Consumes: N/A (audit)
- Produces: Rapporto sullo stato attuale

- [ ] **Step 1: Verificare che user-service usi SQLAlchemy (non in-memory)**

Conferma: `app/repositories/repository.py` usa `db.add()`, `db.commit()`, `db.refresh()`, `select()`, `db.get()` — SQLAlchemy puro.
Conferma: `app/services/service.py` usa `Session` type hint e chiama repository SQLAlchemy.
Conferma: `app/api/routes.py` usa `Depends(get_db)` per Dependency Injection.
Conferma: `app/database/database.py` ha engine SQLAlchemy con dual-database support.
Conferma: `app/main.py` ha `init_database()` nel lifespan e endpoint `/ready` con verifica DB.

- [ ] **Step 2: Stessa verifica per loan-service, review-service, inventory-service, notification-service**

Tutti e 4 hanno identica struttura SQLAlchemy come user-service.

- [ ] **Step 3: Verificare docker-compose.yml**

Conferma: ogni servizio nel docker-compose ha `DATABASE_TYPE: postgres` e `DATABASE_URL` che punta al suo DB PostgreSQL.
Conferma: ogni DB PostgreSQL ha healthcheck, volume persistente, e rete `internal: true` separata.

---

## Task 1: Avvio del sistema con Docker Compose

**Files:**
- Modify: N/A
- Run: docker compose up -d --build

- [ ] **Step 1: Build e avvio di tutti i servizi**

```bash
cd /c/Users/edoardo.querio/OneDrive\ -\ ITS\ ICT\ Piemonte/Desktop/Materie/17_Container_Docker_Kubernetes/02_Esercizi
docker compose up -d --build
```

Expected: Build di 7 immagini (api-gateway + 6 servizi). Avvio di ~13 container (6 servizi + 6 DB + 1 gateway).

- [ ] **Step 2: Verifica stato container**

```bash
docker compose ps
```

Expected: Tutti i container con stato "Up" e "healthy".

- [ ] **Step 3: Test health check via gateway**

```bash
curl -s http://localhost/health
```

Expected: `{"status":"ok"}`

- [ ] **Step 4: Test readiness di ogni servizio**

```bash
curl -s http://localhost/health
```

Expected: Tutti i servizi rispondono 200.

---

## Task 2: Test CRUD su ogni servizio via gateway

**Files:**
- Test via: curl/httpie attraverso api-gateway (localhost:80)

- [ ] **Step 1: Test user-service CRUD**

```bash
# Create user
curl -s -X POST http://localhost/users -H "Content-Type: application/json" -d '{"name":"Mario Rossi","email":"mario@example.com"}'

# List users
curl -s http://localhost/users

# Get user by ID
curl -s http://localhost/users/1

# Update user
curl -s -X PUT http://localhost/users/1 -H "Content-Type: application/json" -d '{"name":"Mario Verdi"}'

# Delete user
curl -s -X DELETE http://localhost/users/1
```

- [ ] **Step 2: Test loan-service CRUD**

```bash
# Create loan
curl -s -X POST http://localhost/loans -H "Content-Type: application/json" -d '{"user_id":1,"book_id":1}'

# List loans
curl -s http://localhost/loans

# Return loan
curl -s -X PUT http://localhost/loans/1/return
```

- [ ] **Step 3: Test review-service CRUD**

```bash
# Create review
curl -s -X POST http://localhost/reviews -H "Content-Type: application/json" -d '{"book_id":1,"user_id":1,"rating":4,"comment":"Bel libro!"}'

# List reviews
curl -s http://localhost/reviews

# Get reviews by book
curl -s http://localhost/reviews/by-book/1
```

- [ ] **Step 4: Test inventory-service CRUD**

```bash
# Set stock
curl -s -X POST http://localhost/inventory -H "Content-Type: application/json" -d '{"book_id":1,"quantity":10}'

# List stock
curl -s http://localhost/inventory

# Get stock by book
curl -s http://localhost/inventory/1
```

- [ ] **Step 5: Test notification-service**

```bash
# Send notification
curl -s -X POST http://localhost/notifications -H "Content-Type: application/json" -d '{"user_id":1,"channel":"email","message":"Ciao!"}'

# List notifications
curl -s http://localhost/notifications
```

---

## Task 3: Verifica persistenza PostgreSQL

- [ ] **Step 1: Inserisci dati, ferma container, riavvia, verifica persistenza**

```bash
# Inserisci un libro
curl -s -X POST http://localhost/books -H "Content-Type: application/json" -d '{"titolo":"Test","autore":"T","isbn":"9788845293689"}'

# Ferma tutto
docker compose down

# Riavvia
docker compose up -d

# Verifica che il libro esista ancora
curl -s http://localhost/books
```

Expected: Il libro creato prima del down è ancora presente dopo il riavvio.

- [ ] **Step 2: Verifica isolamento database**

Conferma: i dati di book-service non compaiono in user-service e viceversa (ogni servizio ha il proprio DB isolato).

---

## Task 4: Aggiornamento documentazione

- [ ] **Step 1: Aggiornare README.md**

Modificare la descrizione dei servizi da "in-memory" a "PostgreSQL con SQLAlchemy".

- [ ] **Step 2: Commit**

```bash
git add docs/ README.md
git commit -m "feat: verifica PostgreSQL per tutti i servizi"
```
