## Phase L - Authorization, Tenancy And Administrative Access

- Create an endpoint and job authorization matrix covering actor, role, tenant, resource ownership, state, action and negative case.
- Audit Pundit, CanCanCan, Action Policy or custom policy fallback behavior and verify default deny.
- Test BOLA and IDOR by changing IDs, nested resource parents, tenant keys, signed IDs, GlobalID values and background-job arguments.
- Verify tenant isolation in SQL, default scopes, associations, caches, files, search indexes, broadcasts, jobs, mail and analytics.
- Audit admin, support, impersonation and break-glass access with step-up authentication, reason capture, expiry, logging and review.

