# Core — Severity Model (P0–P3)

| Priority | Meaning |
| -------- | ------- |
| **P0** | Unauthorized/cross-tenant access, RCE/injection, exposed production secret, irreversible data loss/corruption, destructive unrehearsed deploy, unrecoverable backup gap for critical data |
| **P1** | Authz bypass in a critical flow, race/transaction/idempotency failure, unbounded resources, worker duplication, deployment interruption of critical ops, unsafe migration under load |
| **P2** | Localized functional/UX issue, measured performance problem, weak observability, avoidable availability risk, tech debt with concrete consequence |
| **P3** | Docs, naming, consistency, small measured cleanup |

Severity is impact × likelihood, not aesthetics.
