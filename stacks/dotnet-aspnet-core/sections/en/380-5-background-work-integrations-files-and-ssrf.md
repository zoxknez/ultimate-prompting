## 5. Background Work, Integrations, Files, And SSRF

A hosted service with scoped dependencies must create a scope per operation. At-least-once requires idempotent consumers.

External dependencies: deadline, cancellation, bounded retry+jitter, rate limit, circuit breaker when justified, webhook signature/replay, telemetry. `IHttpClientFactory` + modern resilience stack.

Upload/download: size/count, MIME+magic bytes, traversal, streaming, private storage, signed URL expiry, tenant, retention, auth on every download.

User-supplied URL fetch: scheme, resolved IP, private/metadata ranges, DNS rebinding, redirects, size, timeout. String-only validation is insufficient.

