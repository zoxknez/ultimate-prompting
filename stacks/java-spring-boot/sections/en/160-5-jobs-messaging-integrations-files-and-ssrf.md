## 5. Jobs, Messaging, Integrations, Files, And SSRF

For `@Async`, executors, scheduled tasks, Spring Batch, queues, Kafka/JMS/Rabbit consumers, and retry mechanisms assess bounded pools/queues, context propagation, cancellation, startup/shutdown, acknowledgement, visibility/lease timeout, retry/backoff/jitter, dead-letter/poison handling, deduplication, idempotency, concurrency, ordering, timeout, deployment overlap, and observability. At-least-once delivery requires idempotent consumers; do not acknowledge before durable side effects complete.

For each external dependency assess deadline, connect/read/overall timeout, bounded retry with jitter, rate limits, circuit breaking when justified, credentials, webhook signature/replay protection, schema/version changes, fallback, sandbox/production separation, and telemetry. Do not blindly retry validation, authorization, cancellation, or non-idempotent writes. Reuse managed HTTP clients and pools; do not create clients per request.

For uploads/downloads verify count/size limits, MIME plus magic bytes, names, traversal, temporary storage, quotas, streaming, scanning policy, private storage, signed URL expiry, tenant isolation, retention/cleanup, and authorization for each download. Do not load large files into memory or trust client MIME/name.

If the service fetches a user-provided URL, validate scheme, hostname, resolved IPv4/IPv6 address, loopback/private/link-local/cloud-metadata ranges, ports, DNS rebinding, redirects, embedded credentials, response size/content type, timeout, and decompression. String-only URL validation is insufficient.

