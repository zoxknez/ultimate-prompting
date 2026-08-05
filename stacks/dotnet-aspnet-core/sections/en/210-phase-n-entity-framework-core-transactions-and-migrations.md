## Phase N - Entity Framework Core, Transactions, And Migrations

DbContext: scoped lifetime, factory, pooling (careful with mutable state/interceptors/tenants), background-service scope per operation, disposal. DbContext is not thread-safe and must not be used in parallel from multiple tasks.

Model: PK/AK, concurrency token/rowversion, FK, cascade/restrict, owned/complex types, value converters, precision, indexes, unique/check constraints, query filters (tenant/soft delete), audit fields.

Do not return EF entities as the public API contract without justification. Check tracking vs `AsNoTracking`, N+1, cartesian explosion, oversized Include, split query, projection, client evaluation, generated SQL, pagination (offset vs keyset), parameterized raw SQL.

Critical invariants belong in the database where possible. For every critical write document: what is read/validated/changed, the invariant, concurrency, atomic boundary, dependent-failure behavior, rollback/compensation, audit. Test lost update, write skew, duplicate payment/order/job, negative inventory, duplicate reservation, partial operation.

Idempotency for retryable/externally triggered writes: tenant/user-scoped key, fingerprint, unique constraint, stored outcome, conflict response, atomic boundary with the business write or transactional outbox.

Migrations are versioned schema changes, not an automatic production side effect. Review generated SQL before applying. Production rollout: owner, backup/restore verification, lock/duration, rolling compatibility, backfill, forward repair, tested rollback or compensating migration. Prefer reviewed SQL scripts or migration bundles. Do not call `Database.Migrate()` from every production replica unless a serialized deployment design proves safety. Do not execute destructive migrations during the audit.

