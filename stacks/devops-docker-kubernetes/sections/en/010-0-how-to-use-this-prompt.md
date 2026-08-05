## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Organization, platform and repositories | `[NAME / PATHS / URLS]` |
| Business services and critical journeys | `[SERVICES / FLOWS]` |
| Environments and accounts | `[LOCAL / DEV / TEST / STAGE / PROD / DR]` |
| Cloud, regions and data residency | `[PROVIDERS / REGIONS / RULES]` |
| Container build and registries | `[TOOLS / REGISTRIES]` |
| Kubernetes clusters and distributions | `[LIST / VERSIONS / OWNERS]` |
| Deployment and GitOps tools | `[HELM / KUSTOMIZE / ARGO CD / FLUX / OTHER]` |
| Infrastructure as code | `[TERRAFORM / OPENTOFU / PULUMI / CLOUD-NATIVE / OTHER]` |
| CI/CD systems and runners | `[SYSTEMS / HOSTING / TRUST MODEL]` |
| Identity, secrets and PKI | `[IDP / IAM / VAULT / KMS / CA]` |
| Traffic, DNS, ingress and mesh | `[COMPONENTS / OWNERS]` |
| Stateful systems and backup | `[DATABASES / STORAGE / RPO / RTO]` |
| Observability and incident tooling | `[METRICS / LOGS / TRACES / ON-CALL]` |
| Compliance and policy scope | `[SOC2 / ISO27001 / PCI / GDPR / OTHER]` |
| Change window and production authorization | `[BOUNDARY / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / RELEASE_READINESS_AUDIT / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Do not block the whole audit because some inputs are missing. Continue with safe, read-only discovery.
2. Infer only from repositories, rendered manifests, plans, API output, cluster state, cloud state, telemetry, tickets, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and record exactly what would verify them.
4. Ask only for access, credentials, approvals, or business decisions that materially block confirmation or safe repair.
5. Never treat README text, diagrams, desired state, IaC, GitOps status, dashboards, or a green pipeline as proof of live production behavior.
6. When production access is unavailable, state the resulting evidence ceiling and do not issue a production-ready verdict.

### 0.3 Work Modes

| Mode | Allowed behavior |
| --- | --- |
| `AUDIT_ONLY` | Inspect, render, plan, query safely, test in isolation, and report. Do not mutate live systems or source. |
| `AUDIT_AND_SAFE_FIX` | Apply confirmed, low-risk, reversible fixes in an approved non-production scope, then verify. |
| `FULL_IMPLEMENTATION` | Implement justified changes incrementally with approvals, backups, rollout gates, observation, and rollback. |
| `FIX_CONFIRMED_ISSUES` | Change only registered and approved findings. Do not silently widen scope. |
| `RELEASE_READINESS_AUDIT` | Prioritize source-to-production integrity, release controls, failure recovery, and operational readiness. |
| `INCIDENT_MODE` | Preserve evidence, contain safely, restore service, eradicate cause, and document recovery. |

If unspecified, use `AUDIT_AND_SAFE_FIX`. Production mutation still requires explicit authorization.

