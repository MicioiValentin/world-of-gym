# World of Gym

**Project status:** Planning / MVP design.

World of Gym (WOG) is a mobile application that helps users log workouts, earn XP, level up, and maintain consistency through cooldowns and level decay. The project is being developed in a staged, testable way with strong attention to reliability and operations.

---

## Objectives (MVP)

- Manual set logging: exercise, reps, kilograms.
- Server-calculated XP per set with diminishing returns by level.
- Level progression with a daily 120-minute cooldown (no XP after limit).
- Consistency mechanic: decay after skipping two consecutive weekdays (for higher levels).
- Simple leaderboard (local first; global later).

**Out of scope (MVP):** hardware sensors, BLE integration, payments.

---

## Architecture Overview (v0)

**Client:** Expo / React Native (TypeScript)  
**API:** Python (FastAPI) or Go (Chi/Gin) — to be decided  
**Database:** PostgreSQL  
**Local development:** Docker Compose (Kubernetes later)

See: [`docs/architecture-v0.md`](docs/architecture-v0.md)

---

## Tech Stack (planned)

- Mobile: Expo + React Native (TypeScript)
- Backend: FastAPI (Python) or Chi/Gin (Go)
- Database: PostgreSQL
- Observability: structured logs, Prometheus metrics, OpenTelemetry traces (later)
- Infrastructure: Docker Compose locally; Terraform + Kubernetes later

---

## Roadmap (high level)

- Repository and documentation scaffold 
- API contract (OpenAPI) 
- XP/level rules and test plan   
- Choose backend language (Python or Go)  
- CLI for XP math + unit tests  
- API service (Dockerized) and `/v1/sets` endpoint  
- Mobile app: auth + basic logging flows  
- Leaderboard and achievements  
- Observability, SLOs, IaC

Details in **/docs** and **/planning**.

---

## Key Documents

- MVP Spec: [`docs/project-spec.md`](docs/project-spec.md)  
- API Contract (OpenAPI 3.1): [`api/contract/openapi.yaml`](api/contract/openapi.yaml)  
- XP & Leveling Rules: [`docs/xp-rules.md`](docs/xp-rules.md)  
- Test Plan: [`planning/test-plan.md`](planning/test-plan.md)  
- Week Plan: [`planning/week-plan.md`](planning/week-plan.md)

---

## SRE/DevOps Focus

This project is intentionally structured to demonstrate operational excellence:

- **Contract-first development:** OpenAPI-driven API design before implementation.  
- **Containerized local stack:** Reproducible environment with Docker Compose.  
- **Reliability by design:** Health/readiness endpoints, timeouts/retries, and backpressure planned from the outset.  
- **Observability plan:** Structured logging, metrics, and traces with Prometheus/OpenTelemetry; dashboards and alerts aligned to SLOs.  
- **Testing strategy:** Unit tests for XP math; integration and contract tests for API; smoke tests in CI.  
- **Infrastructure as Code:** Terraform for cloud resources; Helm/Kubernetes for deployment (later phases).  
- **Operations documentation:** Runbooks, incident response, postmortem template, and change management practices.  
- **Security and supply chain:** Dependency scanning, image SBOMs/signing, and secret management policy (later phases).

---

## Getting Started (Windows 11)

Prerequisites: Git, Node.js LTS, VS Code (Docker Desktop optional at this stage)
API and mobile code will be added incrementally. For now, review the documents above.