## Required Inputs, Scope, And Work Modes

### Required Inputs

| Field | Required value |
| --- | --- |
| Repository and revision | [PATH/URL, branch, commit, dirty state] |
| Business purpose and critical invariants | [ACTORS, MONEY, INVENTORY, RIGHTS, TENANTS, CONSENT] |
| Entrypoints | [HTTP, CLI, QUEUE, SCHEDULER, MIGRATOR, REALTIME, WEBHOOK] |
| Framework and runtime | [PLAIN PHP, LARAVEL, SYMFONY, FPM, OCTANE, FRANKENPHP, ROADRUNNER, SWOOLE] |
| Identity and tenancy | [SESSION, JWT, OIDC, API KEY, SERVICE IDENTITY, ROLES, TENANTS] |
| Data and side effects | [DATABASE, ORM, CACHE, QUEUE, FILES, PAYMENT, EMAIL, SEARCH] |
| Deployment and topology | [VM, CONTAINER, KUBERNETES, SERVERLESS, MULTI-REGION] |
| Operational targets | [SLO, RPO, RTO, PRIVACY, COMPLIANCE, COST, CAPACITY] |

### Work Modes

| Mode | Allowed scope |
| --- | --- |
| AUDIT_ONLY | Inspect and execute safe checks without changing source, lockfile, schema, infrastructure, or production state. |
| AUDIT_AND_SAFE_FIX | Apply small reversible fixes with focused regression tests and no production side effects. |
| FULL_IMPLEMENTATION | Implement justified changes with migration, rollout, rollback, and monitoring plans. |
| FIX_CONFIRMED_ISSUES | Change only selected confirmed findings and preserve unrelated behavior. |
| SECURITY_AND_CONCURRENCY_AUDIT | Prioritize auth, authorization, tenancy, injection, race, idempotency, workers, resources, and supply chain. |
| PERFORMANCE_AND_RELIABILITY_AUDIT | Prioritize latency, memory, FPM saturation, queue lag, long-lived state, overload, shutdown, failover, and recovery. |
| INCIDENT_AND_RECOVERY | Contain compromise, preserve evidence, rotate secrets, verify integrity, restore, reconcile, and harden. |

### Safety Stop

- Default to AUDIT_AND_SAFE_FIX unless another mode is explicitly selected.
- Stop before destructive schema changes, production writes, secret rotation, traffic changes, queue purge, cache flush, worker restart, or release unless explicitly authorized.
- Never delete uncommitted work, rewrite history, force-push, or use production credentials in local or CI tests.
- Prefer disposable environments, fixtures, read-only replicas, fake providers, isolated queue namespaces, and isolated restore targets.
- Do not print secret values, raw tokens, cookies, private keys, APP_KEY, Symfony secrets, session payloads, or sensitive personal data.

