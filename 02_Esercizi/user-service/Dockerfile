FROM python:3.14-slim AS builder

LABEL maintainer="Edoardo Querio Gianetto"

WORKDIR /app

# Copia solo requirements prima per sfruttare la cache Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    find /usr/local -name '__pycache__' -type d -exec rm -rf {} + 2>/dev/null || true


FROM python:3.14-slim

WORKDIR /app

# Crea directory per SQLite locale (usato solo in sviluppo/test) e utente non-root
RUN mkdir -p /data && \
    addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --gid 1001 --no-create-home appuser && \
    chown appuser:appgroup /data

# Copia dipendenze dallo stage builder
COPY --from=builder /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copia il codice dell'applicazione con proprietà non-root
COPY --chown=appuser:appgroup app/ ./app/

# Espone la porta del servizio
EXPOSE 8000

USER appuser

# Healthcheck per Kubernetes / Docker Compose
HEALTHCHECK --interval=10s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# CMD con uvicorn (reload=False in produzione)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
