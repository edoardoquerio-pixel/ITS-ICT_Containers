SHELL := /bin/bash
.PHONY: help up down build rebuild ps logs logs-%

help: ## Mostra questo help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# === Docker Compose (7 servizi + PostgreSQL) ===

up: ## Build e avvia tutti i servizi in background
	docker compose up -d --build

down: ## Ferma e rimuove i container (dati persistiti)
	docker compose down

down-v: ## Ferma, rimuove container e volume DB
	docker compose down -v

build: ## Ricostruisce tutte le immagini
	docker compose build

rebuild: ## Ricostruisce e riavvia tutti i servizi
	docker compose up -d --build --force-recreate

restart: ## Riavvia i container senza rebuild
	docker compose restart

ps: ## Mostra lo stato di tutti i container
	docker compose ps

logs: ## Log in tempo reale di tutti i servizi
	docker compose logs -f

logs-%: ## Log di un singolo servizio (es. make logs-book-service)
	docker compose logs -f $(@:logs-%=%)

# === Servizi specifici ===

rebuild-%: ## Ricostruisce e riavvia un singolo servizio (es. make rebuild-user-service)
	docker compose up -d --build --no-deps $(@:rebuild-%=%)

# === Test ===

test: ## Test del book-service
	cd book-service && python -m pytest tests/ -v

test-cov: ## Test book-service con coverage
	cd book-service && python -m pytest tests/ --cov=app -v

# === Health check ===

health: ## Verifica health check via gateway
	@curl -s http://localhost/health | python -m json.tool

check: ## Verifica rapida di tutti i servizi
	@echo "=== Gateway ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/health && echo " /health"
	@echo ""
	@echo "=== Books ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/books && echo " /books"
	@echo ""
	@echo "=== Users ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/users && echo " /users"
	@echo ""
	@echo "=== Loans ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/loans && echo " /loans"
	@echo ""
	@echo "=== Reviews ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/reviews && echo " /reviews"
	@echo ""
	@echo "=== Inventory ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/inventory && echo " /inventory"
	@echo ""
	@echo "=== Notifications ==="
	@curl -s -o /dev/null -w "%{http_code}" http://localhost/notifications && echo " /notifications"

# === Pulizia ===

clean: ## Rimuove cache Python da tutti i servizi
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	rm -rf .coverage htmlcov/
