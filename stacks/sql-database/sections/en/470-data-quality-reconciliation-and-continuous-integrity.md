## Data Quality, Reconciliation, And Continuous Integrity

Correct schema and successful queries do not prove historical data correctness.

- Define data-quality rules for ranges, references, uniqueness, chronology, totals and state transitions.
- Create bounded reconciliation queries that can run safely in production or on replicas.
- Track discrepancies with lineage, first-seen time, affected scope, owner and repair status.
- Use repair scripts that are reviewed, idempotent, checkpointed, auditable and reversible where possible.
- Validate totals and invariants after migration, failover, restore, queue replay and incident recovery.
- Alert on trend changes, not only absolute invalid-row counts.

