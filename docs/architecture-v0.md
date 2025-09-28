# Architecture v0 (MVP)
Mobile app (Expo/React Native) -> REST API -> Postgres
Services (later):
- api/: FastAPI (Python) or Go (Chi/Gin)
- infra/: Docker Compose for local; K8s later
Observability (Later): structured logs, Prometheus metrics, OTEL traces.
