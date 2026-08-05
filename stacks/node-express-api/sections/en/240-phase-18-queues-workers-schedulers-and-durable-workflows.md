## Phase 18 - Queues, Workers, Schedulers, And Durable Workflows

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory producers, consumers, topics, queues, routing keys, payload schemas, headers, DLQs, schedules, and operators.
- Define delivery semantics, acknowledgement point, visibility or lease timeout, concurrency, ordering, partitioning, and retry budget.
- Make consumers idempotent under redelivery, retry, rebalance, crash, timeout, and operator replay.
- Use transactional outbox, inbox, CDC, saga, or reconciliation where database and broker cannot commit atomically.
- Bound prefetch, concurrency, payload size, retries, retained failure data, and poison-message impact.
- For schedulers, prevent duplicate ownership, overlap, missed run, catch-up storm, timezone, DST, and clock-skew errors.

### Required Evidence

- Produce and preserve the producer-consumer contract matrix.
- Produce and preserve the retry, DLQ, replay, and poison-message policy.
- Produce and preserve schedule ownership, overlap, and shutdown evidence.

### Mandatory Failure And Acceptance Tests

- Prove that consumer crash before and after commit is safe.
- Prove that a poison message cannot block processing indefinitely.
- Prove that duplicate scheduled execution preserves the invariant.

