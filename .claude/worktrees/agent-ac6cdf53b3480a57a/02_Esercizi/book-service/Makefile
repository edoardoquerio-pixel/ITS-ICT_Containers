SHELL := /bin/bash
.PHONY: help run test lint docker-build docker-up docker-down docker-test k8s-apply k8s-delete clean

help: ## Mostra questo help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# === Sviluppo locale ===

run: ## Avvia il server in locale con hot-reload
	uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

test: ## Esegue i test
	python -m pytest tests/ -v

test-cov: ## Esegue i test con coverage
	python -m pytest tests/ --cov=app -v

lint: ## Analisi statica con ruff
	ruff check app/ tests/

format: ## Formatta il codice con ruff
	ruff format app/ tests/

# === Docker ===

docker-build: ## Builda l'immagine Docker
	docker compose build

docker-up: ## Avvia i container in background
	docker compose up -d

docker-down: ## Ferma e rimuove i container
	docker compose down

docker-logs: ## Mostra i log del book-service
	docker compose logs -f book-service

docker-test: ## Esegue i test in container
	docker compose -f docker-compose.test.yml up --abort-on-container-exit

# === Kubernetes ===

k8s-apply: ## Applica tutti i manifest Kubernetes
	kubectl apply -f k8s/namespace.yaml
	kubectl apply -f k8s/configmap.yaml
	kubectl apply -f k8s/pvc.yaml
	kubectl apply -f k8s/postgres-statefulset.yaml
	kubectl apply -f k8s/deployment.yaml
	kubectl apply -f k8s/service.yaml

k8s-delete: ## Elimina tutte le risorse Kubernetes
	kubectl delete -f k8s/service.yaml --ignore-not-found
	kubectl delete -f k8s/deployment.yaml --ignore-not-found
	kubectl delete -f k8s/postgres-statefulset.yaml --ignore-not-found
	kubectl delete -f k8s/pvc.yaml --ignore-not-found
	kubectl delete -f k8s/configmap.yaml --ignore-not-found
	kubectl delete -f k8s/namespace.yaml --ignore-not-found

k8s-logs: ## Mostra i log del pod book-service
	kubectl logs -n book-service -l app=book-service --tail=100 -f

k8s-status: ## Mostra lo stato dei pod
	kubectl get all -n book-service

# === Pulizia ===

clean: ## Rimuove cache Python e file temporanei
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name '*.pyc' -delete
	rm -rf .coverage htmlcov/
