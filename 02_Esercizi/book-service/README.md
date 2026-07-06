# Book Service — Microservizi Containerizzati

Piattaforma REST di gestione libreria composta da **7 microservizi + PostgreSQL**, orchestrati con **Docker Compose** e containerizzati singolarmente.

```
┌─────────────────────────────────────────────────────────────────────┐
│                        api-gateway (nginx:80)                       │
│  /health  /books/*  /users/*  /loans/*  /reviews/*  /inventory/*   │
└────┬─────────┬──────────┬──────────┬────────────┬─────────────┬────┘
     │         │          │          │            │             │
  ┌──▼──┐  ┌──▼──┐  ┌───▼───┐  ┌──▼───┐  ┌───▼──────┐  ┌───▼─────┐
  │book │  │user │  │ loan  │  │review│  │inventory │  │notificat│
  │serv.│  │serv.│  │serv.  │  │serv. │  │ serv.    │  │ion serv.│
  │:8000│  │:8000│  │:8000  │  │:8000 │  │ :8000    │  │ :8000   │
  └──┬──┘  └─────┘  └───────┘  └──────┘  └──────────┘  └─────────┘
     │      (in-mem)  (in-mem)  (in-mem)   (in-mem)      (in-mem)
  ┌──▼──┐
  │Postg│
  │reSQL│
  │:5432│
  └─────┘
```

**8 container**, 1 rete Docker condivisa (`microservice-network`), 1 volume (`pg-data`).

---

## Architettura

### 1. API Gateway — nginx

Nginx instrada le richieste al servizio corretto in base al path URL. È l'unico container esposto sulla porta `80` dell'host.

| Path | Upstream | Servizio |
|------|----------|----------|
| `/health` | `books` | book-service |
| `/books` | `books` | book-service |
| `/users` | `users` | user-service |
| `/loans` | `loans` | loan-service |
| `/reviews` | `reviews` | review-service |
| `/inventory` | `inventory` | inventory-service |
| `/notifications` | `notifications` | notification-service |

### 2. book-service — FastAPI + PostgreSQL

CRUD completo per la risorsa **libri** con persistenza PostgreSQL.

| Metodo | Endpoint | Codice | Descrizione |
|--------|----------|--------|-------------|
| `GET` | `/health` | 200 | Health check |
| `GET` | `/ready` | 200 / 503 | Readiness con verifica DB |
| `GET` | `/books` | 200 | Lista libri (`?genere=&disponibile=`) |
| `GET` | `/books/{id}` | 200 / 404 | Dettaglio libro |
| `POST` | `/books` | 201 / 409 | Crea libro |
| `PUT` | `/books/{id}` | 200 / 404 / 409 | Aggiorna libro |
| `DELETE` | `/books/{id}` | 204 / 404 | Elimina libro |

**Stack**: FastAPI, SQLAlchemy 2.0, PostgreSQL 16, Pydantic v2, psycopg2-binary

**4 livelli**: Routes → Services → Repository → Database (SQLAlchemy ORM)

**Dual-database**: PostgreSQL in produzione, SQLite in-memory per test.

### 3. user-service — FastAPI (in-memory)

CRUD per la risorsa **utenti** con storage in-memory (dict list).

| Metodo | Endpoint | Codice | Descrizione |
|--------|----------|--------|-------------|
| `GET` | `/users` | 200 | Lista utenti |
| `GET` | `/users/{id}` | 200 / 404 | Dettaglio utente |
| `POST` | `/users` | 201 | Crea utente (name, email) |
| `DELETE` | `/users/{id}` | 204 / 404 | Elimina utente |

### 4. loan-service — FastAPI (in-memory)

Gestione **prestiti libri** con storage in-memory.

| Metodo | Endpoint | Codice | Descrizione |
|--------|----------|--------|-------------|
| `GET` | `/loans` | 200 | Lista prestiti |
| `GET` | `/loans/{id}` | 200 / 404 | Dettaglio prestito |
| `POST` | `/loans` | 201 | Crea prestito (user_id, book_id) |
| `PUT` | `/loans/{id}/return` | 200 / 404 | Restituzione libro |

### 5. review-service — FastAPI (in-memory)

Gestione **recensioni libri** con storage in-memory.

| Metodo | Endpoint | Codice | Descrizione |
|--------|----------|--------|-------------|
| `GET` | `/reviews` | 200 | Lista recensioni |
| `GET` | `/reviews/{id}` | 200 / 404 | Dettaglio recensione |
| `GET` | `/reviews/by-book/{book_id}` | 200 | Recensioni per libro |
| `POST` | `/reviews` | 201 / 422 | Crea recensione (book_id, user_id, rating 1-5, comment) |

### 6. inventory-service — FastAPI (in-memory)

Gestione **scorte/libri** con dizionario book_id → quantità.

| Metodo | Endpoint | Codice | Descrizione |
|--------|----------|--------|-------------|
| `GET` | `/inventory` | 200 | Lista scorte |
| `GET` | `/inventory/{book_id}` | 200 / 404 | Scorta per libro |
| `POST` | `/inventory` | 201 | Imposta scorta (book_id, quantity) |

### 7. notification-service — FastAPI (in-memory)

Invio simulato di **notifiche** (email/sms/push) con log in-memory.

| Metodo | Endpoint | Codice | Descrizione |
|--------|----------|--------|-------------|
| `GET` | `/notifications` | 200 | Lista notifiche inviate |
| `POST` | `/notifications` | 201 | Invia notifica (user_id, channel, message) |

---

## Tecnologie

| Componente | Tecnologia |
|-----------|-----------|
| Linguaggio | Python 3.14 |
| Framework API | FastAPI ≥ 0.100 |
| Validazione | Pydantic ≥ 2.0 |
| ORM (solo book) | SQLAlchemy 2.0 |
| Database (book) | PostgreSQL 16 |
| Driver DB | psycopg2-binary |
| Server ASGI | Uvicorn ≥ 0.20 |
| Reverse proxy | nginx 1.31 (alpine) |
| Container | Docker |
| Orchestrazione | Docker Compose |

---

## Struttura del progetto

```
02_Esercizi/
├── docker-compose.yml              # Orchestrazione 8 container
├── api-gateway/
│   ├── Dockerfile                  # nginx:alpine + nginx.conf
│   └── nginx.conf                  # upstream + proxy_pass per ogni servizio
├── book-service/
│   ├── app/                        # FastAPI con SQLAlchemy + PostgreSQL
│   ├── tests/                      # pytest (42 test)
│   ├── Dockerfile                  # multi-stage, utente non-root
│   ├── docker-compose.yml          # standalone (legacy)
│   ├── Makefile
│   ├── requirements.txt
│   └── README.md
├── user-service/
│   ├── app/main.py                 # CRUD utenti (in-memory)
│   ├── Dockerfile
│   └── requirements.txt
├── loan-service/
│   ├── app/main.py                 # Prestiti libri (in-memory)
│   ├── Dockerfile
│   └── requirements.txt
├── review-service/
│   ├── app/main.py                 # Recensioni (in-memory)
│   ├── Dockerfile
│   └── requirements.txt
├── inventory-service/
│   ├── app/main.py                 # Scorte (in-memory)
│   ├── Dockerfile
│   └── requirements.txt
└── notification-service/
    ├── app/main.py                 # Notifiche simulate (in-memory)
    ├── Dockerfile
    └── requirements.txt
```

---

## Prerequisiti

- **Docker** + **Docker Compose** ≥ 3.8
- **curl** o **httpie** per testare le API

---

## Avvio rapido

```bash
# Dalla directory 02_Esercizi/

# Build e avvio di tutti i servizi
docker compose up -d --build

# Verifica lo stato
docker compose ps

# Log in tempo reale
docker compose logs -f

# Log di un singolo servizio
docker compose logs -f book-service

# Arresto (dati persistiti)
docker compose down

# Arresto + pulizia volume DB
docker compose down -v
```

Tutti i servizi sono raggiungibili tramite **api-gateway** su `http://localhost` (porta 80).

### Endpoint di verifica

```bash
# Health check globale
curl http://localhost/health

# --- Books (porta 80 via gateway) ---
curl http://localhost/books

# Crea un libro
curl -X POST http://localhost/books \
  -H "Content-Type: application/json" \
  -d '{"titolo":"Il nome della rosa","autore":"Umberto Eco","isbn":"9788845293689","anno_pubblicazione":1980,"genere":"Giallo storico"}'

# --- Users ---
curl http://localhost/users
curl -X POST http://localhost/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Mario Rossi","email":"mario@example.com"}'

# --- Loans ---
curl http://localhost/loans
curl -X POST http://localhost/loans \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"book_id":1}'
curl -X PUT http://localhost/loans/1/return

# --- Reviews ---
curl http://localhost/reviews
curl http://localhost/reviews/by-book/1
curl -X POST http://localhost/reviews \
  -H "Content-Type: application/json" \
  -d '{"book_id":1,"user_id":1,"rating":5,"comment":"Ottimo libro!"}'

# --- Inventory ---
curl http://localhost/inventory
curl http://localhost/inventory/1
curl -X POST http://localhost/inventory \
  -H "Content-Type: application/json" \
  -d '{"book_id":1,"quantity":10}'

# --- Notifications ---
curl http://localhost/notifications
curl -X POST http://localhost/notifications \
  -H "Content-Type: application/json" \
  -d '{"user_id":1,"channel":"email","message":"Benvenuto!"}'
```

---

## Sviluppo

### Hot-reload per book-service

Il file `book-service/docker-compose.override.yml` monta `./app` come volume e abilita `--reload` di uvicorn. Per gli altri servizi, modificare il `main.py` e ricostruire:

```bash
docker compose up -d --build <service-name>
```

### Aggiungere un nuovo servizio

1. Crea directory `<service-name>/` con `app/main.py`, `Dockerfile`, `requirements.txt`
2. Esponi `/health` e `/ready` su porta `8000`
3. Aggiungi `upstream` in `api-gateway/nginx.conf`
4. Aggiungi `location /<name>` in `nginx.conf`
5. Aggiungi il servizio in `docker-compose.yml`

---

## Test

```bash
# Test solo book-service (42 test)
cd book-service && python -m pytest tests/ -v

# Test con coverage
cd book-service && python -m pytest tests/ --cov=app -v
```

Per i nuovi servizi (in-memory), eseguire test manuali tramite curl come sopra.

---

## Kubernetes

Il solo book-service ha manifest K8s in `book-service/k8s/`. Per deploy completo su cluster:

1. Convertire ogni servizio in deployment + service K8s
2. Aggiungere nginx Ingress Controller per il routing
3. Sostituire PostgreSQL con managed DB (es. Cloud SQL)

---

## Decisioni tecniche

| Scelta | Motivazione |
|--------|------------|
| **API Gateway (nginx)** | Singolo punto di ingresso, routing trasparente, nessuna modifica ai servizi |
| **In-memory per 5 servizi** | Demo pronta senza configurazione DB esterna; facilmente sostituibile con SQLite/PostgreSQL |
| **Servizi indipendenti** | Ogni servizio ha il proprio storage, build, healthcheck; scalabile individualmente |
| **redirect_slashes=False** | Previene redirect 307 su `/users` vs `/users/`, comportamento coerente via gateway |
| **Python:3.14-slim** | Base image minimale per servizi Python semplici |
| **Healthcheck HTTP** | Docker Compose e orchestrazione rilevano servizi pronti |
| **Volume pg-data** | Dati DB persistenti tra riavvii container |

---

## Possibili estensioni

- **Persistenza reale** per user/loan/review/inventory/notification (SQLite → PostgreSQL)
- **Comunicazione inter-servizio** (es. loan-service chiama inventory per decrementare stock)
- **Autenticazione JWT** su API gateway
- **Rate limiting** nginx per endpoint pubblici
- **CI/CD** con GitHub Actions: test → build → push registry → deploy
- **Metriche** (Prometheus + Grafana) per ogni servizio
- **Tracing distribuito** (OpenTelemetry)
- **K8s manifests** per tutti i servizi con Ingress Controller
