## Severity Model P0-P3

| Severity | Definition | Response |
| --- | --- | --- |
| P0 | Active compromise, auth bypass, cross-tenant disclosure, secret exposure, RCE, destructive data loss, corrupted release, or uncontrolled critical outage | Contain immediately, preserve evidence, revoke/isolate, and enter incident command |
| P1 | Exploitable BOLA, private cache leak, broken mutation authz, serious race/idempotency, unsafe migration, or release blocker | Fix or contain before release with regression, guardrail, and recovery |
| P2 | Material performance, a11y, SEO, observability, resilience, cost, maintainability, or compatibility risk | Schedule with owner, acceptance, evidence plan, and deadline |
| P3 | Minor cleanup, consistency, docs, developer experience, or low-impact optimization | Backlog with clear value, owner, and non-regression scope |

