## Production Readiness Checklist

- [ ] Source, PHP, SAPI, extensions, dependencies, artifact, deployment, schema, and running process are traceably identified.
- [ ] Every supported execution mode uses an approved runtime, INI, extension set, configuration, lifecycle, and test matrix.
- [ ] Composer lockfile, repositories, scripts, plugins, platform requirements, SBOM, signatures, and provenance are verified.
- [ ] Framework routes, containers, middleware, policies, firewalls, queues, schedulers, caches, and debug surfaces are proven from the production artifact.
- [ ] Authentication, account lifecycle, authorization, ownership, tenancy, administration, and break-glass paths pass negative tests.
- [ ] Critical data invariants, transaction boundaries, idempotency, outbox or inbox, and reconciliation are verified under concurrency and crash.
- [ ] Queue, scheduler, cache, session, lock, storage, search, and external-provider failure behavior is bounded and recoverable.
- [ ] Long-lived processes reset request state, bound concurrency, drain safely, and are fully replaced during release.
- [ ] Injection, XSS, CSRF, SSRF, deserialization, file parsing, traversal, and resource-abuse controls pass exploit-oriented tests.
- [ ] Capacity, pool, FPM, OPcache, worker, dependency, timeout, queue, and load-shedding limits are measured and monitored.
- [ ] Logs, traces, metrics, health, alerts, runbooks, and privacy controls explain critical failures without exposing sensitive data.
- [ ] CI isolates untrusted code, uses scoped credentials, builds once, promotes one immutable digest, and supports revocation and trusted rebuild.
- [ ] Migrations and backfills support mixed versions, bounded execution, pause, resume, verification, forward repair, and recovery.
- [ ] Rollout, OPcache transition, worker reload, rollback, forward repair, isolated restore, RPO, and RTO are exercised.
- [ ] No unresolved P0, unaccepted P1, expired waiver, unknown critical path, unsupported component, or untrusted production state remains.

