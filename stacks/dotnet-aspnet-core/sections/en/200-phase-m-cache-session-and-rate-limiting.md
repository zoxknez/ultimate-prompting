## Phase M - Cache, Session, And Rate Limiting

Map in-memory, distributed, HTTP/CDN, database, and computed cache. Check key design, tenant/user/permission scope, TTL, size, invalidation, serialization/versioning, stampede, outage, stale strategy. Private data must never use a shared/public key. Cache is not the source of truth for critical invariants.

Session: whether it is truly needed; distributed store; sticky-session dependency; size; PII; races on parallel requests; rolling deployment.

