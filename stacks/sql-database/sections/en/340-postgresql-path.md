## PostgreSQL Path

### Runtime, Extensions, And Configuration

- Verify `SHOW server_version`, `server_version_num`, package or image, extension versions and managed-service engine.
- Review `postgresql.conf`, `postgresql.auto.conf`, role and database settings, startup parameters and pending restart values.
- Review `pg_hba.conf`, SSL, authentication methods, replication access and include ordering.
- Audit extension trust, shared preload libraries, background workers, upgrade scripts and binary compatibility.
- Verify locale, ICU, collation versions and reindex requirements after operating-system or ICU change.

### MVCC, Vacuum, Freeze, And Bloat

- Measure transaction age, dead tuples, autovacuum progress, freeze age and wraparound risk.
- Review table-specific autovacuum thresholds, cost settings, scale factors and workload fit.
- Detect long transactions, replication slots, prepared transactions and idle sessions retaining old snapshots.
- Measure table and index bloat with method limitations; do not prescribe `VACUUM FULL` without rewrite and lock analysis.
- Verify vacuum, analyze and reindex procedures under disk and replication constraints.

### PostgreSQL Plans, Indexes, And Partitioning

- Use `EXPLAIN (ANALYZE, BUFFERS, WAL, SETTINGS, VERBOSE)` only when execution is safe and bounded.
- Review B-tree, hash, GIN, GiST, SP-GiST, BRIN, expression, partial, INCLUDE and unique index semantics.
- Review extended statistics, correlation, visibility map, index-only scan and HOT update behavior.
- Verify partition pruning at plan and execution time, partitionwise operations and default partition growth.
- Audit concurrent index build failure, invalid indexes, attach or detach locks and replication lag.

### PostgreSQL Replication, HA, And Recovery

- Review `wal_level`, archive mode, archive command, retention, WAL gaps, timelines and restore command.
- Review physical and logical replication, slots, publications, subscriptions, replica identity and conflict handling.
- Verify synchronous-commit and synchronous-standby semantics against latency and RPO.
- Test promotion, timeline change, `pg_rewind` prerequisites, stale primary fencing and failback.
- Prove base backup plus uninterrupted WAL archive can restore to a selected point and start the application.

### PostgreSQL Security And Row-Level Policies

- Review ownership, `SECURITY DEFINER`, search path, function volatility and extension privileges.
- Review default privileges, schema create access, public role grants and temporary-object permissions.
- Test row-level security with owner, `BYPASSRLS`, restrictive and permissive policy combinations.
- Review logical backup and replication behavior for roles, policies, large objects and extensions.
- Prevent untrusted input from controlling search path, identifiers, dynamic SQL or server-side file access.

