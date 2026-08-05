## Severity Model P0-P3

| Severity | Definition | Expected action |
| --- | --- | --- |
| P0 | Active compromise, cross-tenant disclosure, RCE, critical authorization bypass, unrecoverable corruption, production-secret exposure, or destructive release. | Contain immediately, preserve evidence, revoke or isolate, restore or reconcile, and run incident command. |
| P1 | High-probability auth, integrity, race, idempotency, event-loop, exhaustion, migration, supply-chain, or recovery failure. | Block release or critical traffic until fixed or explicitly contained with owner and deadline. |
| P2 | Material but localized correctness, performance, observability, compatibility, or maintainability risk. | Plan and verify repair in a bounded release with regression protection. |
| P3 | Low-risk cleanup, documentation, consistency, naming, or small improvement. | Address opportunistically without distracting from higher-risk work. |

