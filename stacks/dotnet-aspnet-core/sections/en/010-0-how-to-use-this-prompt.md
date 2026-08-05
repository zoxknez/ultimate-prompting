## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, solution, and relevant paths | `[PATHS / URLS]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Environments and deployment units | `[LOCAL / TEST / STAGE / PROD / DR]` |
| Hosting and operating systems | `[IIS / KESTREL / CONTAINER / KUBERNETES / AZURE / OTHER]` |
| Data stores, brokers, caches, and object storage | `[SYSTEMS / OWNERS]` |
| Identity providers and trust boundaries | `[OIDC / COOKIE / JWT / MTLS / API KEY / OTHER]` |
| Public and internal contracts | `[HTTP / GRPC / SIGNALR / EVENTS / FILES]` |
| Availability, latency, RPO, and RTO targets | `[SLO / RPO / RTO]` |
| Compliance, privacy, and data residency | `[RULES / REGIONS]` |
| Known incidents, defects, and planned migrations | `[CONTEXT]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repositories, project files, resolved builds, runtime state, deployment artifacts, telemetry, database metadata, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence or access required to resolve them.
4. Ask only for access, approval, credentials, or business decisions that materially block confirmation or safe repair.
5. Never treat a README, architecture diagram, green pipeline, successful health response, or generated OpenAPI document as proof of complete production correctness.
6. When production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

