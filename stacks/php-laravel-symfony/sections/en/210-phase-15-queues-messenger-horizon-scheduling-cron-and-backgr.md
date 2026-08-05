## Phase 15 - Queues, Messenger, Horizon, Scheduling, Cron, and Background Work

### Objective

Prove delivery, retry, ordering, deduplication, resource, deployment, and recovery behavior for all asynchronous work.

### Audit Requirements

- Inventory every queue, transport, topic, subscription, failed transport, Horizon supervisor, Messenger worker, scheduler, cron, batch, and external trigger.
- Verify message schema, serialization, versioning, tenant and actor context, authorization, idempotency key, correlation, trace, and sensitive-data policy.
- Audit acknowledgement timing, visibility timeout, retry schedule, max attempts, backoff, jitter, dead-letter handling, poison-message quarantine, and replay approval.
- Test worker crash before and after side effects, broker redelivery, reordered events, duplicates, delayed messages, stale messages, and schema mismatch.
- Review scheduler overlap, lock TTL, leader election, clock skew, missed runs, catch-up, DST, long tasks, and multi-replica execution.
- Verify bounded concurrency, prefetch, memory, database pool pressure, backpressure, graceful drain, worker replacement, and deployment compatibility.

### Required Evidence

- Async topology and message-contract matrix with owner, retry, DLQ, and recovery path.
- Crash, duplicate, reorder, poison, replay, shutdown, and mixed-version worker test evidence.
- Worker and scheduler rollout evidence tied to artifact revision and queue depth.

### Acceptance Criteria

- At-least-once delivery and retries do not violate business invariants or leak tenant context.
- Workers can be drained, replaced, replayed, and recovered without silent loss or uncontrolled duplication.

