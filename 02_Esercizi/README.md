# Microservizi Libreria

Sistema di 7 microservizi per la gestione libreria, orchestrati con Docker Compose.

## Architettura

```
api-gateway (nginx:80)
├── book-service → PostgreSQL  (libri, CRUD + disponibilità)
├── user-service → PostgreSQL  (utenti, CRUD)
├── loan-service → PostgreSQL  (prestiti, orchestrazione inter-servizio)
├── review-service → PostgreSQL (recensioni, validazione)
├── inventory-service → PostgreSQL (scorte)
└── notification-service → PostgreSQL (notifiche)
```

## Comunicazione Inter-Servizio

| Chiamante | Servizio | Scopo |
|-----------|----------|-------|
| **loan-service** → | **book-service** | Verifica disponibilità; aggiorna `disponibile` su prestito/return |
| **loan-service** → | **inventory-service** | Controlla scorte prima del prestito |
| **loan-service** → | **notification-service** | Invia notifica prestito/restituzione |
| **review-service** → | **book-service** | Verifica esistenza libro prima della recensione |

## Avvio

```bash
docker compose up -d --build
```

Gateway su `http://localhost`.

## Endpoint principali

| Endpoint | Servizio |
|----------|----------|
| `GET /health` | Health check |
| `GET/POST /books` | Book service |
| `GET/POST /users` | User service |
| `GET/POST /loans`, `PUT /loans/{id}/return` | Loan service |
| `GET/POST /reviews` | Review service |
| `GET/POST /inventory` | Inventory service |
| `GET/POST /notifications` | Notification service |

## Stack

FastAPI + SQLAlchemy 2.0 + PostgreSQL 16 Alpine + nginx + Docker Compose
Python 3.14, Pydantic v2, httpx per comunicazione inter-servizio

## Fasi implementate

- [x] Fase 1: Database PostgreSQL + SQLAlchemy per tutti i servizi
- [x] Fase 2: Comunicazione inter-servizio (httpx)
- [ ] Fase 3: Test automatici
