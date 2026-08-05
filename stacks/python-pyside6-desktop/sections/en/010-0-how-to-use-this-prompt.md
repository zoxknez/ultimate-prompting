## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, and relevant paths | `[PATHS / URLS]` |
| Application type and UI stack | `[WIDGETS / QML / MIXED / WEBENGINE / UNKNOWN]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Supported OS and architectures | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / OTHER]` |
| Python, Qt, PySide6, and packaging targets | `[VERSIONS / ABI / TOOLS]` |
| Distribution formats and channels | `[INSTALLER / STORE / PORTABLE / ENTERPRISE / AUTO-UPDATE]` |
| Local stores, files, caches, and secrets | `[LOCATIONS / FORMATS / OWNERS]` |
| Remote services and network trust | `[APIS / PROXIES / CERTIFICATES]` |
| Native libraries, devices, and privileged helpers | `[DLL / DYLIB / SO / DEVICES / SERVICES]` |
| Signing, notarization, and update infrastructure | `[KEYS / PROVIDERS / FEEDS / CHANNELS]` |
| Availability, startup, latency, and resource targets | `[SLO / BUDGETS]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository content, lock files, resolved environments, build output, packaged artifacts, signatures, installed state, runtime evidence, telemetry, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence, platform, credential, approval, device, or user journey required to resolve them.
4. Ask only for access, approval, credentials, business decisions, hardware, or distribution accounts that materially block confirmation or safe repair.
5. Never treat a README, a green CI job, a successful source launch, an unsigned package, or a one-platform smoke test as proof of production correctness.
6. When installed or production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

