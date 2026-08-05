## 4. Evidence Model And Finding Discipline

### 4.1 Evidence Levels

| Level | Meaning | Examples |
| --- | --- | --- |
| E0 | Claim or assumption only. | README statement, comment, ticket, undocumented recollection. |
| E1 | Static source or configuration evidence. | Dart code, pubspec, native manifest, CI file, entitlement. |
| E2 | Resolved or generated evidence. | pubspec.lock, dependency graph, generated registrant, build config, compiled metadata. |
| E3 | Executed build, test, or artifact evidence. | Analyzer output, tests, release build, signed artifact inspection, size analysis. |
| E4 | Installed device, browser, or controlled environment evidence. | Real-device launch, browser matrix, migration run, update test, profiler trace. |
| E5 | Production or production-equivalent operational evidence. | Telemetry, staged rollout, restore drill, incident replay, SLO trend. |

### 4.2 Finding Register

Every material finding must contain all fields below. Missing fields reduce confidence and can block remediation approval.

| Field | Required content |
| --- | --- |
| ID and severity | Stable identifier and P0-P3 level. |
| Title and affected scope | Platform, flavor, module, route, feature, account, tenant, version, and environment. |
| Status and evidence level | Claim status plus E0-E5 level. |
| Evidence and reproduction | Files, symbols, commands, artifact IDs, device/browser matrix, telemetry, and deterministic steps. |
| Root cause | Underlying technical and process cause, not only symptom. |
| Impact and exploitability | User, data, security, availability, cost, store, compliance, and recovery impact. |
| Remediation and alternatives | Minimal safe fix, long-term option, rejected shortcuts, and ownership. |
| Verification and rollback | Regression tests, negative tests, platform matrix, rollout gates, rollback trigger, and recovery. |

### 4.3 Severity Model

- `P0`: active compromise, signing/update compromise, systemic unauthorized access, destructive corruption, unrecoverable data loss, or critical outage requiring immediate containment.
- `P1`: credible severe security, privacy, authorization, payment, migration, release, availability, or recovery defect with high user or business impact.
- `P2`: material correctness, performance, accessibility, compatibility, maintainability, observability, or operational defect that should be scheduled.
- `P3`: low-risk hardening, cleanup, documentation, test-depth, developer-experience, or optimization improvement.
- Severity must reflect proven impact, reachability, prerequisites, detectability, recovery, and exposure, not fear or scanner wording.

