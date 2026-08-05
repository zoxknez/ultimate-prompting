## Phase 13 - Authorization, Ownership, Tenancy, Admin, And Impersonation

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Build an authorization matrix for every route, job, query, file, cache key, message, export, search, and admin action.
- Separate identity, role, permission, ownership, tenant, resource state, relationship, and contextual policy checks.
- Enforce owner and tenant constraints in authoritative queries or commands, not only fetch-then-check logic.
- Test BOLA, BFLA, cross-tenant enumeration, batch endpoints, nested resources, indirect references, and alternate media types.
- Define admin, support, delegated access, impersonation, and break-glass approval, scope, reason, expiry, audit, and review.
- Verify tenant isolation through cache, queue, storage, telemetry, logs, errors, background jobs, and reconciliation.

### Required Evidence

- Produce and preserve the route-resource authorization matrix.
- Produce and preserve the tenant data-flow and negative-test map.
- Produce and preserve the admin, support, and impersonation register.

### Mandatory Failure And Acceptance Tests

- Prove that cross-tenant object identifiers are denied without existence leakage.
- Prove that stale role caches cannot preserve revoked access.
- Prove that background jobs and admin paths preserve tenant scope and audit.

