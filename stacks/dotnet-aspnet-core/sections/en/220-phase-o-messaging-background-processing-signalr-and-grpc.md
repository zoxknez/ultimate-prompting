## Phase O - Messaging, Background Processing, SignalR, And gRPC

For `IHostedService`/`BackgroundService`, queue consumers, and schedulers: scope per operation, cancellation, bounded concurrency, ack/visibility timeout, retry/backoff/jitter, DLQ/poison, deduplication, idempotency, ordering, timeout, heartbeat, shutdown, deployment overlap, observability. At-least-once requires idempotent consumers; do not acknowledge before durable side effects complete.

For SignalR/SSE/gRPC streaming: connection and per-message authorization, origin/tenant, reconnect, heartbeat, idle timeout, message/connection limits, backpressure, cleanup, replay/sequence, slow consumer, deployment. Authorizing only the initial connection is insufficient.

