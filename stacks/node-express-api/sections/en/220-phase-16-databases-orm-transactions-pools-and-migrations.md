## Phase 16 - Databases, ORM, Transactions, Pools, And Migrations

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Verify the actual database, driver, ORM or query builder, versions, topology, replicas, proxies, and consistency model.
- Audit schema constraints, indexes, foreign keys, uniqueness, checks, defaults, precision, time zones, and collation.
- Inspect actual generated SQL, parameterization, plans, cardinality, locks, and production-like data distribution.
- Map transaction boundaries, isolation, timeout, retry, deadlock handling, and side effects outside the transaction.
- Size connection pools against replicas, serverless concurrency, workers, database limits, and failover behavior.
- Use expand-and-contract migrations with compatible overlap, bounded backfill, verification, cutover, and forward repair.

### Required Evidence

- Produce and preserve the schema, query, transaction, and pool matrix.
- Produce and preserve the migration compatibility and ownership plan.
- Produce and preserve restore, PITR, and data-integrity evidence.

### Mandatory Failure And Acceptance Tests

- Prove that concurrent writes preserve database constraints.
- Prove that pool exhaustion fails with bounded latency.
- Prove that old and new binaries coexist safely during migration.

