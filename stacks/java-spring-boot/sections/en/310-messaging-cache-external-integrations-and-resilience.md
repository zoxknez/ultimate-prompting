## Messaging, Cache, External Integrations, And Resilience

### Broker And Consumer Semantics

- Inventory Kafka, RabbitMQ, JMS, Pulsar, SQS, Pub/Sub, streams, exchanges, topics, queues, partitions, consumer groups, listeners, serializers, and retry infrastructure.
- Define delivery semantics, ordering key, partitioning, acknowledgement point, visibility timeout, retry ownership, dead-letter policy, poison-message handling, retention, and replay procedure.
- Test crash before and after local commit, acknowledgement loss, duplicate delivery, rebalance, partition loss, broker failover, schema mismatch, slow consumer, and retry storm.
- Bound concurrency, prefetch, in-flight records, batch size, memory, retry rate, and downstream calls; preserve backpressure through every adapter.
- Protect tenant identity, authorization, sensitive data, trace context, and schema compatibility across production, replay, dead-letter, and repair paths.

### Caching And Distributed Coordination

- Inventory local, distributed, HTTP, query, Hibernate, method, result, session, token, metadata, and negative caches with authoritative sources and ownership.
- Define key construction, tenant and authorization dimensions, value schema, TTL, refresh, invalidation, versioning, consistency expectation, and behavior during cache outage.
- Test stampede, hot keys, eviction, stale reads, partial invalidation, deployment schema change, serialization change, clock skew, failover, and cache poisoning.
- For distributed locks and leases, require owner identity, TTL, renewal, fencing token where stale owners can cause damage, failure detection, and cleanup.
- Never use cache presence, a lock without fencing, or best-effort invalidation as the sole protection for money, inventory, quota, uniqueness, or authorization invariants.

### Outbound Clients And Resilience Policies

- Inventory HTTP, gRPC, database, broker, DNS, SMTP, object storage, payment, identity, search, and custom clients with destination allow lists and ownership.
- Define connect, handshake, request, read, write, idle, total, and pool-acquisition timeouts plus deadline propagation and maximum response sizes.
- Apply retries only to classified transient failures and replay-safe operations; include attempt limits, elapsed-time budget, jitter, `Retry-After`, and nested-retry prevention.
- Review circuit breakers, bulkheads, rate limiters, concurrency limiters, hedging, fallback, and degraded modes for state correctness and observability.
- Test DNS changes, stale pooled connections, certificate and credential rotation, partial responses, malformed responses, redirect abuse, SSRF, dependency brownout, and total outage.

### Search, Object Storage, Email, And Payments

- Treat search indexes, object stores, mail systems, payment providers, and third-party APIs as separate consistency, identity, authorization, and recovery domains.
- Define source of truth, synchronization, idempotency, ordering, reconciliation, deletion, retention, and behavior when callbacks or acknowledgements are delayed or duplicated.
- For object storage, verify bucket/container policies, path and tenant binding, signed URL scope and expiry, content validation, encryption, versioning, lifecycle, and delete semantics.
- For email and notifications, prevent header/template injection, recipient confusion, sensitive-data leakage, duplicate sends, and unbounded fan-out.
- For payments and other irreversible operations, prove provider idempotency, webhook verification, amount/currency precision, ledger reconciliation, refund/chargeback handling, and manual recovery.


