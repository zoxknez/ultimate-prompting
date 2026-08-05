## Advanced Production Audit Contract 2.0
Audit the application as a distributed product whose JavaScript, native binaries, generated projects, backend contracts, app-store state, OTA state, device state, and local data can evolve independently. A green Metro session, Expo Go session, simulator build, or EAS job is not production proof.

### Evidence Levels
| Level | Meaning | Maximum permitted claim |
| --- | --- | --- |
| E0 | Assumption, memory, or undocumented statement | Do not present as fact |
| E1 | Source or configuration inspection | The declared intent is known |
| E2 | Resolved dependency, generated project, build graph, or static artifact evidence | The effective build inputs are known |
| E3 | Targeted automated test or controlled reproduction | The tested behavior is known under stated conditions |
| E4 | Signed release artifact installed and exercised on a representative physical device | The release behavior is known for that matrix cell |
| E5 | Production telemetry, controlled rollout, rollback, restore, or incident exercise | Operational behavior and recovery are evidenced |

### Required Finding Record
| Field | Required content |
| --- | --- |
| Identifier | Stable ID such as RN-P0-001 |
| Status | CONFIRMED, PARTIALLY_CONFIRMED, UNVERIFIED, NOT_APPLICABLE, or REJECTED |
| Evidence | File, symbol, command, artifact, device, log, trace, screenshot, or measurement |
| Root cause | Mechanism, not only symptom |
| Impact | User, data, security, availability, store, cost, or compliance impact |
| Scope | Workflow, platform, architecture, build profile, channel, version, tenant, and device class |
| Fix | Smallest safe reversible change |
| Verification | Regression, negative, concurrency, migration, release, and recovery checks |
| Rollback | Executable rollback or forward-fix path |
| Residual risk | Owner, expiry, compensating control, and next review date |

