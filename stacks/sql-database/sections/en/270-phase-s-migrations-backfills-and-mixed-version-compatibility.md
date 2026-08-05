## Phase S - Migrations, Backfills, And Mixed-Version Compatibility

Treat every schema and data change as a distributed release.

- Inspect exact DDL semantics, lock strength, table rewrite, log volume, replication effect and cancellation behavior.
- Use expand-and-contract for incompatible changes and prove old and new application coexistence.
- Make backfills chunked, checkpointed, restartable, idempotent, rate-limited and observable.
- Define correctness query, progress metric, pause, resume, abort and cleanup.
- Test migration from a production-like snapshot with realistic data skew and concurrent traffic.
- Separate application rollback, schema rollback, data rollback and forward repair; prove which are actually safe.

