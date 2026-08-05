## Severity

| Priority | Definition |
| --- | --- |
| P0 | Unauthorized/cross-tenant access, RCE/injection, confirmed data race in a critical flow, unsound unsafe/FFI with real UB risk, exposed production secret, irreversible data loss/corruption, destructive deployment, untested recovery of critical data. |
| P1 | Authz bypass in a critical flow, goroutine/task leak under load, broken cancellation/timeout, broken idempotency/transaction, unbounded resources, unsafe deserialization, supply-chain issue with reachability, interruption of a critical operation during deploy. |
| P2 | Localized API issue, slow query, weak observability, inconsistent error contract, avoidable availability risk, technical debt with a concrete consequence. |
| P3 | Cleanup, documentation, naming, consistency, small measured improvement. |

