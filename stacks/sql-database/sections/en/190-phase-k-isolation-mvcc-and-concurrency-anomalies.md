## Phase K - Isolation, MVCC, And Concurrency Anomalies

Prove behavior at the configured isolation level for the actual engine.

- Test lost update, write skew, nonrepeatable read, phantom, read skew and stale replica reads as applicable.
- Record engine defaults and session or transaction overrides.
- Verify optimistic concurrency tokens, affected-row checks and retry semantics.
- Verify serializable failure handling and bounded retries with fresh transaction state.
- Test read-after-write and monotonic-read requirements across primary and replicas.
- Do not transfer isolation names between PostgreSQL, InnoDB and SQLite without testing actual semantics.

