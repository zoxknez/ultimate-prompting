## Production Checklist

Before the final verdict fill with evidence (YES / NO / PARTIAL / UNVERIFIED / NOT_APPLICABLE):

1. Supported .NET runtime/SDK, stable C# baseline, `global.json`, no unapproved preview components.
2. Reproducible restore (lock/locked-mode where applicable), package audit, Release build, publish artifact tested.
3. Clear architectural boundaries, dependency direction, data ownership, deployment ownership.
4. No critical sync-over-async; cancellation/timeout; correct DI lifetimes; background scope.
5. Validation, HTTP semantics, Problem Details, pagination, idempotency, rate limiting, OpenAPI, compatibility.
6. Database constraints, transactions, concurrency, idempotency, migration review/test, backup/restore, tenant isolation.
7. Default-deny authz, resource authorization, token/cookie validation, CSRF decision, CORS, Data Protection, secrets, TLS, injection/SSRF/upload, supply chain, audit.
8. Timeout/retry/jitter/circuit/concurrency limits; no retry storms; messaging recovery.
9. Liveness/readiness/degraded; structured log; metrics; tracing; dashboard; alert; runbook.
10. Measured or explicitly bounded capacity/performance risk.
11. Container/hosting/publish model verified (non-root, SBOM where applicable).
12. Graceful shutdown, rollout, abort criteria, application rollback, and data recovery.

