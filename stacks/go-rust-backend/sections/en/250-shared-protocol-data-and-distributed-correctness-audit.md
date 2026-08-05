## Shared Protocol, Data, And Distributed-Correctness Audit

### Network Protocol And API Contract Matrix

- Inventory listeners, clients, transports, methods, routes, RPC services, streaming modes, authentication, authorization, tenant ownership, payload limits, deadlines, idempotency, retries, transaction boundary, compatibility, and tests.
- Verify HTTP parsing, request smuggling defenses, proxy trust, forwarded headers, TLS termination, HTTP/2 and HTTP/3 settings, decompression limits, multipart handling, redirects, and connection reuse.
- For gRPC and protobuf, verify field evolution, unknown fields, oneof changes, enum growth, deadlines, status mapping, interceptors, reflection, health, streaming backpressure, and old/new client compatibility.
- For TCP, UDP, QUIC, framed, binary, or custom protocols, verify framing, length validation, incremental parsing, timeouts, peer identity, replay, amplification, fragmentation, state-machine transitions, and fuzz coverage.
- Apply request, response, header, metadata, stream, file, message, and decompressed-size limits before expensive allocation or parsing.

### Transactions, Idempotency, And Schema Evolution

- Map every state-changing flow from validation through authorization, reads, locks, writes, side effects, commit, response, retry, event publication, and reconciliation.
- Verify database constraints, isolation, lock order, optimistic tokens, serialization failures, deadlock retry, connection state, transaction ownership, savepoints, cancellation, and rollback behavior.
- Use idempotency keys with durable ownership, request fingerprinting, result persistence, conflict semantics, expiry, replay response, concurrency control, and multi-replica behavior.
- Audit outbox, inbox, CDC, saga, compensation, deduplication, ordering, partition ownership, poison messages, DLQ replay, and partial failure between database and broker.
- Verify expand-and-contract migrations, old/new binary coexistence, backfill idempotency, online index or constraint behavior, lock duration, cutover, rollback limits, forward repair, and restore compatibility.

### Cache, Queue, And Coordination Correctness

- Document cache key namespace, tenant scope, authorization sensitivity, serialization version, TTL, invalidation, stampede protection, negative caching, stale policy, eviction, and outage behavior.
- Treat distributed locks and leases as fallible coordination; verify fencing tokens, clock assumptions, renewal, ownership loss, split brain, stale holder behavior, and recovery.
- For queues and streams, verify delivery semantics, ack timing, visibility timeout, rebalance, ordering, batch partial failure, retry budget, poison handling, retention, replay, and consumer idempotency.
- Test broker outage, cache outage, delayed or duplicated messages, reordered events, consumer restart, partition movement, lease loss, and database/broker recovery skew.

### Overload, Retry, Deadline, And Partial-Failure Control

- Derive concurrency, queue, pool, and rate limits from downstream capacity, latency budgets, memory, CPU, file descriptors, database limits, and recovery objectives.
- Propagate deadlines end to end and reserve time for cleanup, transaction completion, response serialization, retries, and fallback; avoid independent timeout inflation at each hop.
- Classify operations by idempotency and retryability; cap attempts and elapsed time, use jitter, honor server signals, prevent retry multiplication, and expose retry budget metrics.
- Verify admission control, load shedding, circuit behavior, bulkheads, bounded queues, fair scheduling, tenant isolation, hot-key handling, fan-out limits, and degradation modes.
- Run burst, sustained load, soak, dependency slowdown, dependency outage, connection churn, cancellation storm, retry storm, and recovery tests with explicit pass/fail thresholds.

