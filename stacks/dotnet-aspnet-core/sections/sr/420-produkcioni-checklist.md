## Produkcioni Checklist

Pre finalne presude popuni dokazima (DA / NE / DELIMICNO / NEPROVERENO / NIJE_PRIMENJIVO):

1. Podrzan .NET runtime/SDK, stabilan C# baseline, `global.json`, bez neodobrenih preview komponenti.
2. Reproducibilan restore (lock/locked-mode gde primenljivo), package audit, Release build, publish artefakt testiran.
3. Jasne arhitektonske granice, dependency smer, data ownership, deployment vlasnistvo.
4. Nema kriticnog sync-over-async; cancellation/timeout; ispravni DI lifetime-ovi; background scope.
5. Validacija, HTTP semantika, Problem Details, pagination, idempotency, rate limiting, OpenAPI, compatibility.
6. Database constraints, transakcije, concurrency, idempotency, migration review/test, backup/restore, tenant isolation.
7. Default deny authz, resource authorization, token/cookie validation, CSRF odluka, CORS, Data Protection, tajne, TLS, injection/SSRF/upload, supply chain, audit.
8. Timeout/retry/jitter/circuit/concurrency limits; nema retry storma; messaging recovery.
9. Liveness/readiness/degraded; structured log; metrics; tracing; dashboard; alert; runbook.
10. Izmeren ili eksplicitno ogranicen capacity/performance rizik.
11. Container/hosting/publish model proveren (non-root, SBOM gde primenljivo).
12. Graceful shutdown, rollout, abort kriterijum, rollback aplikacije i recovery podataka.

