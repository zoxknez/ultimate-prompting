## Phase 17 - Cache, Sessions, Distributed Locks, And Consistency

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory local, shared, response, object, session, authorization, and CDN caches.
- Define keys with tenant, user, role, locale, permission, version, and feature dimensions where required.
- Classify data as public, tenant-shared, user-private, request-private, or forbidden to cache.
- Document TTL, stale tolerance, invalidation order, outage behavior, and stampede protection.
- For distributed locks, define owner, lease, renewal, expiry, fencing token, clock assumptions, and side-effect guard.
- Verify session and authorization invalidation after logout, tenant change, rights change, and credential revocation.

### Required Evidence

- Produce and preserve the cache-classification and key matrix.
- Produce and preserve the invalidation, outage, and stampede table.
- Produce and preserve the lock, lease, and fencing protocol.

### Mandatory Failure And Acceptance Tests

- Prove that cross-tenant cache reads are impossible.
- Prove that stale rights cannot preserve revoked access.
- Prove that an expired lock holder cannot commit the protected side effect.

