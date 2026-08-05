## MySQL And InnoDB Path

### Release Track, Runtime, And SQL Mode

- Identify LTS or Innovation track, exact patch, edition, distribution and Oracle support status.
- Verify MySQL 8.0 EOL exposure and a supported upgrade path to the selected line.
- Review global, persisted and session variables plus configuration-file precedence.
- Review `sql_mode`, strictness, zero dates, division, group-by, implicit defaults and application assumptions.
- Verify character set, collation, timezone tables, authentication plugins, keyring components and TLS.

### InnoDB Transactions, Locks, And Durability

- Review isolation, consistent reads, locking reads, gap and next-key locks and auto-increment locking.
- Capture deadlock reports, metadata locks, history-list growth, purge lag and long transactions.
- Review redo, undo, doublewrite, flush policy, binary-log sync and crash-recovery assumptions.
- Verify connection and thread concurrency against buffer pool, temporary storage and I/O capacity.
- Test commit uncertainty, deadlock retry and duplicate request handling.

### MySQL Plans, Indexes, And DDL

- Use `EXPLAIN ANALYZE`, optimizer trace or Performance Schema only with bounded representative queries.
- Review composite key order, covering indexes, prefix indexes, functional indexes, invisible indexes and histograms.
- Review clustered primary-key effects, secondary-index amplification and random-key write behavior.
- For DDL, verify `ALGORITHM`, `LOCK`, instant or in-place eligibility, table rebuild and metadata-lock impact.
- Use online-schema tools only after trigger, foreign-key, replica, throttling, cutover and cleanup analysis.

### MySQL Replication, HA, Backup, And PITR

- Review binary-log enablement, format, GTID, retention, encryption, source identity and crash-safe repositories.
- Review asynchronous, semi-synchronous, Group Replication, InnoDB Cluster, Router and managed-service behavior.
- Test replica lag, write-set conflicts, errant transactions, clone or seed, promotion and split-brain prevention.
- Prove backup consistency, binary-log coordinates or GTID and replay to a selected point.
- Test application reconnect, read/write routing, failover, failback and transaction uncertainty.

