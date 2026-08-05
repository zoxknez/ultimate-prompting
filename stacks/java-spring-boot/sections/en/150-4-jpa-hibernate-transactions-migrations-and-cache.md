## 4. JPA/Hibernate, Transactions, Migrations, And Cache

Inspect entity mappings, fetch plans, lazy loading boundaries, serialization of entities, N+1/cartesian explosion, query/index usage, broad selects, pagination, locking/version fields, unique/foreign-key/check constraints, defaults/nullability, timestamps/time zones, currency precision, connection-pool settings, statement timeout, raw/native SQL, transaction isolation, audit/soft delete, and backup/restore assumptions. Critical invariants belong in the database where possible; binary floating point is not a money source of truth.

Audit `@Transactional` semantics, transaction-manager selection, propagation/isolation/read-only/timeout/rollback rules, checked-exception behavior, async/reactive boundaries, and proxy limitations. In default proxy mode, self-invocation and initialization calls do not pass through transactional advice; do not assume an annotation guarantees a transaction without testing the actual call path. A database transaction does not atomically include external HTTP, message broker, file, or email side effects; use a transactional outbox or deliberate compensation where needed.

Review Flyway/Liquibase migrations as source-controlled production changes. Require migration owner, review of generated SQL, backup/restore verification, lock/duration estimate, rolling-deployment compatibility, data backfill strategy, forward repair path, and tested rollback or compensating migration. Do not let every replica auto-apply production migrations unless a serialized deployment design proves safety.

For every critical write document reads, validation, state changes, invariant, concurrency behavior, atomic boundary, dependent failure behavior, rollback/compensation, and audit record. Test lost updates, write skew, duplicate payment/order/job, negative inventory, duplicate reservation, partial operations, and cache inconsistency. A JVM-local lock cannot protect horizontally scaled instances.

For retryable or externally triggered writes verify idempotency for duplicate submissions, timeouts, webhook replay, broker redelivery, and crash after side effect before acknowledgement. Use appropriate tenant/user-scoped idempotency keys, request fingerprint, unique constraints, stored outcome/state, expiration, defined conflict response, and atomic boundary with the business write/outbox.

Map local, distributed, HTTP/CDN, database, and computed cache. Verify key design, tenant/user/permission scope, TTL, size, invalidation, serialization/versioning, stampede/outage behavior, and stale strategy. Private data must not use shared/public cache keys, and cache is not the source of truth for critical invariants.

