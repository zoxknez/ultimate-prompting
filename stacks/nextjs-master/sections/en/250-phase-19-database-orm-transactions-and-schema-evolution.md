## Phase 19 - Database, ORM, Transactions, And Schema Evolution

Prove business invariants at the authoritative data layer and safe evolution across concurrency and mixed versions.

### Audit Requirements

- Inventory clients, ORM instances, pools, replica routing, transaction APIs, raw SQL, migrations, seeds, and admin scripts.
- Express uniqueness, ownership, referential integrity, state transitions, balances, quotas, and idempotency with constraints.
- Review isolation, retry, lock order, optimistic versioning, lost update, write skew, deadlock, timeout, and ambiguous commit.
- Detect N+1, Cartesian joins, scans, missing indexes, stale stats, overfetch, per-request clients, and pool exhaustion.
- Separate expand, backfill, code rollout, constraint validation, and contract cleanup.
- Coordinate database commit with payment, email, storage, search, queue, and webhook effects using durable patterns.

### Required Evidence

- Invariant-to-constraint and transaction matrix.
- Production-like query plans, cardinality, pool sizing, and latency evidence.
- Migration graph with expand, backfill, switch, validate, contract, and repair.
- Outbox/inbox or equivalent atomicity and reconciliation evidence.

### Mandatory Failure And Acceptance Tests

- Perform concurrent writes against every critical invariant.
- Crash before commit, during ambiguity, after commit before response, and before external acknowledgement.
- Run old and new app versions through every migration phase.
- Exhaust connection capacity and verify admission, timeout, recovery, and database protection.

