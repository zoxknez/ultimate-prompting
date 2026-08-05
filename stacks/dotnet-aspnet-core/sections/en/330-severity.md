## Severity

| Priority | Definition |
| --- | --- |
| P0 | Unauthorized or cross-tenant access, RCE/injection, exposed production secret, irreversible data loss/corruption, double payment, destructive deployment, or untested recovery for critical data. |
| P1 | Authorization bypass in a critical flow, race/transaction failure, broken idempotency, missing critical timeout, unbounded resources, unsafe deserialization, duplicated worker, or deployment interruption of a critical operation. |
| P2 | Localized API/UI issue, slow query, weak observability, inconsistent error contract, avoidable availability risk, or technical debt with a concrete consequence. |
| P3 | Cleanup, documentation, naming, consistency, or a small measured improvement. |

Base severity on impact and likelihood, not aesthetic preference.

