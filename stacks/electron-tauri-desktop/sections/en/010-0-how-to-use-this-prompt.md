## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, and relevant paths | `[PATHS / URLS]` |
| Framework and application type | `[ELECTRON / TAURI / MIXED / UNKNOWN]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Supported operating systems and architectures | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / OTHER]` |
| Distribution formats and channels | `[INSTALLER / STORE / ENTERPRISE / PORTABLE / AUTO-UPDATE]` |
| Identity, licensing, payments, and privileged operations | `[SYSTEMS / OWNERS]` |
| Local stores, files, caches, and secrets | `[LOCATIONS / FORMATS / OWNERS]` |
| Remote services, origins, and network trust | `[APIS / ORIGINS / PROXIES / CERTIFICATES]` |
| Signing, notarization, and update infrastructure | `[KEYS / PROVIDERS / FEEDS / CHANNELS]` |
| Availability, startup, latency, and resource targets | `[SLO / BUDGETS]` |
| Privacy, compliance, data residency, and retention | `[RULES / REGIONS]` |
| Known incidents, defects, and planned migrations | `[CONTEXT]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository content, lock files, resolved dependency graphs, build output, packaged artifacts, signatures, installed state, runtime evidence, telemetry, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence, platform, credential, approval, or hardware required to resolve them.
4. Ask only for access, approval, credentials, business decisions, or physical devices that materially block confirmation or safe repair.
5. Never treat a README, green CI job, successful dev startup, unsigned package, or one-platform smoke test as proof of production correctness.
6. When installed or production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

