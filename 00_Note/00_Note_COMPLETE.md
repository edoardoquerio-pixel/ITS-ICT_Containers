# Container Docker Kubernetes — Note Complete

## 1. Docker

**Concetti:**
- **Immagine**: template read-only (layers, UnionFS)
- **Container**: istanza eseguibile da immagine
- **Dockerfile**: istruzioni per build immagine
- **Layer caching**: ogni istruzione Dockerfile crea layer cacheable
- **Registry**: Docker Hub, ACR, ECR, GCR, GHCR

```dockerfile
# Dockerfile example
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s \
    CMD wget -qO- http://localhost/ || exit 1
```

```bash
docker build -t myapp:latest .
docker run -d -p 8080:80 --name myapp myapp:latest
docker compose up -d
docker exec -it myapp sh
```

**Docker Compose:**
```yaml
services:
  app:
    build: .
    ports: ["8080:80"]
    depends_on: [db]
  db:
    image: postgres:16-alpine
    volumes: ["pgdata:/var/lib/postgresql/data"]
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_pass
volumes:
  pgdata:
```

**Best practices:**
- Multi-stage build per immagini piccole
- `.dockerignore` per escludere file non necessari
- Non eseguire come root (`USER appuser`)
- Healthcheck per reliability
- Tag semantici, mai `latest` in produzione

## 2. BuildKit

- Nuovo builder back-end (default da Docker 23+)
- Funzionalità: parallel build, secret mount, SSH mount, cache mount
- `DOCKER_BUILDKIT=1 docker build .`
- `RUN --mount=type=cache,target=/root/.npm npm install`

## 3. Kubernetes

**Architettura:**
```
Control Plane (master):
  - API Server (kube-apiserver) — entry point
  - etcd — key-value store
  - Scheduler (kube-scheduler) — assegnazione nodi
  - Controller Manager (kube-controller-manager) — reconciler loop

Worker Nodes:
  - kubelet — agente nodo
  - kube-proxy — networking
  - Container Runtime (containerd, CRI-O)
```

**Oggetti:**
| Oggetto | Descrizione |
|---------|-------------|
| **Pod** | Unità minima, 1+ container, IP condiviso |
| **Deployment** | ReplicaSet + rolling update + rollback |
| **StatefulSet** | Pod con identità stabile, storage persistente |
| **Service** | IP stabile + load balancing verso Pod |
| **Ingress** | L7 routing (host, path), TLS termination |
| **ConfigMap/Secret** | Config non sensibili/sensibili |
| **PersistentVolumeClaim** | Storage richiesto da Pod |
| **Namespace** | Isolamento logico cluster |

**Comandi essenziali:**
```bash
kubectl apply -f deployment.yaml
kubectl get pods -n default -w
kubectl logs -f deployment/myapp
kubectl exec -it pod-name -- sh
kubectl port-forward svc/myapp 8080:80
kubectl describe pod myapp-xxx
kubectl delete pod myapp-xxx   # Ricreato da Deployment
```

## 4. Helm

- **Chart**: pacchetto K8s templateable
- **Values**: override configurazione (`values.yaml`, `--set`)
- **Release**: istanza chart installata
- Comandi: `helm install`, `helm upgrade`, `helm rollback`, `helm pull`
- Repo: Artifact Hub

## 5. Servizio Mesh

- **Istio**: Envoy sidecar proxy, traffic management, security, observability
- **Linkerd**: mesh leggero, mTLS automatico, prometheus metrics
- **Features**: Circuit breaking, retry, timeout, canary, mirroring, mTLS, tracing

## 6. Strumenti Moderni

| Tool | Funzione |
|------|----------|
| Podman | Docker alternativa (daemonless, rootless) |
| K3s | K8s leggero (edge, IoT, ARM) |
| Kind | K8s in Docker (testing locale) |
| Minikube | K8s locale a nodo singolo |
| Skaffold | Dev loop continuo per K8s |
| Kustomize | Config nativa K8s (base + overlay) |

## 7. CICD per Container

```yaml
# GitHub Actions
jobs:
  build:
    steps:
      - uses: docker/build-push-action@v6
        with:
          tags: myapp:${{ github.sha }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

- **Quando rebuildare**: nuovo tag git, cambio immagine base (Dependabot/Renovate)
- **Scanning**: Trivy, Snyk, Docker Scout
- **Registry**: Docker Hub (pubblico), GHCR, ECR/ACR/GCR (privato)
