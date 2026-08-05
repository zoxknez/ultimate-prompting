## Phase 13 - Eloquent, Doctrine, DBAL, Raw SQL, and Data Integrity

### Objective

Audit persistence mappings, query behavior, constraints, concurrency, performance, and data lifecycle using production-like evidence.

### Audit Requirements

- Inventory every database, connection, replica, ORM, DBAL, query builder, raw SQL path, stored procedure, search index, and analytical sink.
- Review model or entity identity, equality, casts, custom types, value objects, nullability, defaults, timestamps, soft deletes, inheritance, and serialization.
- Audit relation ownership, cascade, orphan removal, pivot data, eager and lazy loading, global filters or scopes, and N+1 or Cartesian growth.
- Verify schema constraints for uniqueness, foreign keys, checks, exclusion, tenant boundaries, money precision, status transitions, and immutable facts.
- Test query plans and indexes with production-like cardinality, skew, selectivity, pagination depth, sort order, lock behavior, and replica lag.
- Audit optimistic and pessimistic locking, stale entities, unit-of-work boundaries, identity maps, detached objects, retries, and deadlock handling.

### Required Evidence

- Schema-to-model mapping and invariant matrix with database constraint evidence.
- Representative query plans and load measurements from production-like data.
- Concurrency tests for lost update, write skew, duplicate insertion, deadlock, and replica lag.

### Acceptance Criteria

- Critical invariants are enforced by durable constraints or equally strong atomic mechanisms, not only application callbacks.
- Query, locking, and pool behavior remains bounded under representative scale and concurrency.

