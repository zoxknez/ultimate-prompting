## Phase 21 - PHP-FPM, OPcache, JIT, Capacity, and Resource Exhaustion

### Objective

Measure and bound process, pool, cache, CPU, memory, connection, and downstream capacity under realistic and hostile load.

### Audit Requirements

- Inventory FPM pools, process manager mode, child limits, spare settings, request limits, timeouts, slow logs, termination behavior, and status exposure.
- Verify OPcache memory, interned strings, validation, preload, file cache, huge pages, deployment invalidation, stale code risk, and emergency reset.
- Treat JIT as a measured workload-specific choice; compare correctness, startup, CPU, memory, latency, and observability with and without it.
- Measure application memory, peak request memory, leak-like growth, fragmentation, worker recycling, queue memory, serialization size, and large-response behavior.
- Model FPM, queue, web server, database, Redis, HTTP client, and provider pool sizes together to prevent multiplicative overload.
- Run cold, burst, sustained, soak, failover, dependency-slowdown, large-payload, expensive-query, and malicious-input tests.

### Required Evidence

- Capacity model with arrival rate, concurrency, service time, queue depth, pool limits, memory, and headroom.
- FPM, OPcache, JIT, long-lived worker, and dependency-saturation measurements.
- Load, burst, soak, failover, overload, and recovery test evidence.

### Acceptance Criteria

- Resource limits, queues, timeouts, and load shedding fail predictably before host or dependency collapse.
- Deployment and OPcache transitions cannot serve an untracked mixture of old code, new code, and stale configuration.

