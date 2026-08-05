---
prompt_id: devops-docker-kubernetes-production-audit
version: 2.0.0
title: Produkcioni audit za DevOps, Docker, Kubernetes i cloud platformu
language: sr-Latn
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---

# MASTER PROMPT - Dubinski produkcioni audit za DevOps, Docker, Kubernetes i cloud platforme

Koristi ovaj prompt za audit, bezbednu popravku, verifikaciju i pripremu stvarne delivery platforme za produkciju. Audit mora obuhvatiti ceo put od izmene izvornog koda do aktivnog workload-a, korisnickog saobracaja, telemetrije, incident response-a, backup-a, restore-a i rollback-a.

Cilj moze ukljucivati Docker, BuildKit, Compose, OCI registre, Kubernetes, managed klastere, Helm, Kustomize, Operator-e, GitOps, Terraform ili OpenTofu, cloud servise, service mesh, gateway-e, CI/CD, self-hosted runner-e, policy engine-e, secret manager-e, observability stack, baze, redove poruka, object storage, serverless servise, edge sisteme, virtuelne masine ili hibridnu i multi-cloud infrastrukturu.

