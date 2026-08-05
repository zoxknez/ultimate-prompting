## Faza O - Messaging, Background Processing, SignalR I gRPC

Za `IHostedService`/`BackgroundService`, queue consumere i schedulere: scope po operaciji, cancellation, bounded concurrency, ack/visibility timeout, retry/backoff/jitter, DLQ/poison, deduplikacija, idempotency, ordering, timeout, heartbeat, shutdown, deployment overlap, observability. At-least-once zahteva idempotentne consumere; ne potvrdjuj pre trajnog side effecta.

Za SignalR/SSE/gRPC streaming: connection i per-message authorization, origin/tenant, reconnect, heartbeat, idle timeout, message/connection limite, backpressure, cleanup, replay/sequence, slow consumer, deployment. Autorizacija samo pocetne konekcije nije dovoljna.

