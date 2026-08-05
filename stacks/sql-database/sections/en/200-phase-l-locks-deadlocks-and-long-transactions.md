## Phase L - Locks, Deadlocks, And Long Transactions

Map lock acquisition, duration, wait chains and abort behavior.

- Capture blockers, blocked sessions, lock modes, transaction age, statement and owning application request.
- Review row, table, metadata, predicate, advisory, gap, next-key and file locks as applicable.
- Define deterministic lock order for multi-object operations.
- Configure bounded lock and statement timeouts appropriate to the operation.
- Review idle-in-transaction sessions, abandoned transactions and connection-pool leakage.
- Reproduce deadlocks with evidence before changing indexes, isolation or application order.

