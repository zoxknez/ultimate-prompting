## Phase 16 - Authorization, Tenant Isolation, Admin, And Impersonation

Prove object, action, tenant, and administrative authorization at every data and mutation boundary.

### Audit Requirements

- Build an authz matrix for every route, action, handler, query, file, cache, message, export, search, and admin operation.
- Derive actor and tenant from trusted session or server context, never client IDs alone.
- Enforce ownership in authoritative queries and constraints, not fetch-then-check patterns.
- Verify role, permission, plan, feature, region, data class, and state-transition constraints independently.
- Audit support, admin, impersonation, delegated access, break-glass, approval, marking, audit, expiry, and review.
- Prevent tenant leakage through globals, module caches, singletons, jobs, retries, telemetry, errors, and links.

### Required Evidence

- Route/action/resource authorization matrix with negative cases.
- Authoritative query and constraint evidence for ownership.
- Admin/impersonation approval, audit, expiry, and revocation evidence.
- Cross-tenant cache, queue, file, export, and search isolation evidence.

### Mandatory Failure And Acceptance Tests

- Change resource ID, tenant, role, plan, state, and ownership from a lower privilege.
- Attempt direct route, action, API, file, export, search, and cache access across tenants.
- Revoke privilege during an active session and in-flight mutation.
- Run impersonation across deployment and multiple tabs and verify marking, expiry, restrictions, and audit.

