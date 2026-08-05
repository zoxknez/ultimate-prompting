## Production Readiness Checklist

1. [ ] Supported and patched Next.js, React, TypeScript, Node.js, package manager, ORM, auth, and platform lines are verified.
2. [ ] Frozen install and authoritative production build/start succeed from a clean checkout.
3. [ ] Source-to-runtime identity and immutable artifact promotion are proven.
4. [ ] Routes, runtimes, rendering, caches, auth, tenants, owners, and SLOs are inventoried.
5. [ ] Server/client and RSC boundaries expose no secrets or private data.
6. [ ] Hydration, state, effects, optimistic updates, and concurrency are deterministic and tested.
7. [ ] Every cache has complete keys, correct privacy scope, bounded staleness, invalidation, and outage behavior.
8. [ ] Actions and APIs enforce server authn, authz, validation, idempotency, transaction, limits, and audit.
9. [ ] Identity, session, revocation, tenant, admin, and impersonation lifecycles are proven.
10. [ ] Browser, application, file, webhook, SSRF, CSP, CSRF, XSS, and abuse protections are verified.
11. [ ] Database invariants, concurrency, migrations, durable side effects, reconciliation, and restore are proven.
12. [ ] Runtime/platform limits, multi-instance behavior, version skew, draining, and asset retention are tested.
13. [ ] Field/lab performance, capacity, headroom, load shedding, and cost guardrails exist.
14. [ ] Accessibility, i18n, SEO, error states, offline, multiple tabs, and service worker meet acceptance.
15. [ ] Observability proves user impact, release identity, causal path, saturation, and recovery without leaks.
16. [ ] Tests cover critical journeys, negative authz, cache privacy, concurrency, migration, platform, rollout, rollback, and restore.
17. [ ] CI/CD isolates untrusted code and promotes trusted immutable artifacts with evidence.
18. [ ] Canary, abort, rollback, repair, kill switches, restore, RPO, RTO, and incident runbooks are exercised.
19. [ ] All P0/P1 are fixed or contained with owner, deadline, monitoring, and approved residual risk.
20. [ ] Every READY claim has required evidence and no critical matrix cell is silently missing.

