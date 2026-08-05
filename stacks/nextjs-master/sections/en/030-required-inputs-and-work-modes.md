## Required Inputs And Work Modes

### Required Inputs

| Field | Required value |
| --- | --- |
| Repository and branch | [URL/PATH, branch, commit, dirty state] |
| Critical journeys | [PUBLIC, AUTH, CHECKOUT, ACCOUNT, ADMIN, API, OTHER] |
| Router and rendering | [APP ROUTER / PAGES / MIXED / STATIC EXPORT] |
| Hosting | [VERCEL / NODE / CONTAINER / EDGE / ADAPTER / HYBRID] |
| Identity and tenancy | [AUTH, SESSION, ROLES, TENANTS, ADMIN, IMPERSONATION] |
| Data and side effects | [DATABASE, ORM, CACHE, QUEUE, FILES, PAYMENT, EMAIL, SEARCH] |
| Operational targets | [SLO, RPO, RTO, PRIVACY, ACCESSIBILITY, COMPLIANCE] |
| Known constraints | [INCIDENTS, DEADLINES, CHANGE FREEZE, DATA SAFETY] |

### Work Modes

| Mode | Allowed scope |
| --- | --- |
| AUDIT_ONLY | Read, inspect, execute safe checks, and report without source, lockfile, schema, or environment mutation. |
| AUDIT_AND_SAFE_FIX | Apply small reversible fixes with targeted regression tests and no production side effects. |
| FULL_IMPLEMENTATION | Implement justified changes in controlled increments with migration, rollout, rollback, and observability plans. |
| FIX_CONFIRMED_ISSUES | Change only selected confirmed findings and preserve unrelated behavior. |

### Safety Stop

- Default to AUDIT_AND_SAFE_FIX unless another mode is explicitly selected.
- Stop before destructive schema changes, production writes, secret rotation, irreversible purge, DNS change, or release unless explicitly authorized.
- Never delete uncommitted work, rewrite history, force-push, or use production credentials in local tests.
- Prefer disposable environments, fixtures, read-only replicas, mock providers, and isolated restore targets.

