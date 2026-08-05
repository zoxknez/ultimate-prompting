---
prompt_id: devops-docker-kubernetes-production-audit
version: 2.0.0
title: DevOps, Docker, Kubernetes and Cloud Platform Production Audit
language: en
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---

# MASTER PROMPT - Deep Production Audit of DevOps, Docker, Kubernetes and Cloud Platforms

Use this prompt to audit, safely repair, verify, and prepare a real delivery platform for production. Audit the complete path from source change to running workload, user traffic, telemetry, incident response, backup, restore, and rollback.

The target may include Docker, BuildKit, Compose, OCI registries, Kubernetes, managed clusters, Helm, Kustomize, Operators, GitOps, Terraform or OpenTofu, cloud services, service meshes, gateways, CI/CD, self-hosted runners, policy engines, secret managers, observability stacks, databases, queues, object storage, serverless services, edge systems, virtual machines, or hybrid and multi-cloud infrastructure.

