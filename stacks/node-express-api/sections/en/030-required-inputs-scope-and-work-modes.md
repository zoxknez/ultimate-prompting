## Required Inputs, Scope, And Work Modes

### Required Inputs

| Field | Required value |
| --- | --- |
| Repository and revision | [PATH/URL, branch, commit, dirty state] |
| Business purpose and critical invariants | [FLOWS, ACTORS, MONEY, INVENTORY, RIGHTS, TENANTS] |
| Executables and entrypoints | [API, WORKER, CRON, CLI, MIGRATOR, REALTIME, WEBHOOK] |
| Framework and protocol surface | [EXPRESS, FASTIFY, OTHER, HTTP1, HTTP2, SSE, WS, GRPC] |
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
| SECURITY_AND_CONCURRENCY_AUDIT | Prioritize auth, authorization, tenancy, injection, race, idempotency, event-loop, resources, and supply chain. |
| PERFORMANCE_AND_RELIABILITY_AUDIT | Prioritize latency, event-loop delay, memory, saturation, overload, shutdown, failover, and recovery. |

### Safety Stop

- Default to AUDIT_AND_SAFE_FIX unless another mode is explicitly selected.
- Stop before destructive schema changes, production writes, secret rotation, traffic changes, queue purge, or release unless explicitly authorized.
- Never delete uncommitted work, rewrite history, force-push, or use production credentials in local or CI tests.
- Prefer disposable environments, fixtures, emulators, read-only replicas, mock providers, and isolated restore targets.
- Do not print secret values, raw tokens, cookies, private keys, or sensitive personal data.

