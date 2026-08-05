## Severity Model

| Priority | Definition | Examples |
| --- | --- | --- |
| P0 | Active exploitation, cross-tenant access, RCE, credential compromise, data loss or unrecoverable production state. | Authorization bypass, malicious deserialization, leaked master key, destructive migration without recovery. |
| P1 | Likely outage, critical invariant violation, duplicate irreversible effect, unsafe rollout or major security weakness. | Duplicate payment job, pool exhaustion, stale authorization cache, unsafe Active Storage processing. |
| P2 | Material reliability, performance, observability, maintainability or recovery weakness with bounded impact. | Measured N+1, memory growth, weak queue metrics, untested failover. |
| P3 | Low-risk hygiene, documentation, style or developer-experience issue. | Minor warnings, naming, missing non-critical docs. |

