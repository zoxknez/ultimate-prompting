## Mandatory Final Report

Deliver Markdown with:

1. Executive summary and verdict: `ready`, `ready-with-conditions`, or `not-ready`.
2. Runtime/support status and architecture, filter-chain, auth/authz, transaction, and critical-flow maps.
3. Endpoint matrix: `method | route/service | auth | policy/ownership | validation | rate limit | idempotency | transaction | timeout | side effect | test | status`.
4. Critical-write transaction/idempotency and migration rollout matrices.
5. Findings: `ID | P0-P3 | area | file/symbol | cause | impact | evidence | repair | verification | status`.
6. Implemented changes, files, dependency/configuration/migrations, regression risk, and validation.
7. Actual commands, Java/build-tool/framework versions, environments, exit codes, and material results.
8. Security, concurrency, load/performance, startup, health, and graceful-shutdown results.
9. Blocked checks, exact blockers, and residual risk.
10. Remaining work grouped by `blocks production`, `needed soon`, `planned refactor`, and `optional improvement`, with owner, dependency, acceptance criterion, and organization-defined due date.
11. External sources: title, URL, version/status, access date, and decision informed.

Start with project inventory, Java/Spring lifecycle verification, deterministic build, and production-like startup. Do not begin stylistic cleanup before authorization, transactions, database invariants, idempotency, timeouts, probes, and graceful shutdown are proven.
