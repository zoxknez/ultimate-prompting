## 5. Pozadinski Rad, Integracije, Fajlovi I SSRF

Hosted service sa scoped zavisnostima mora kreirati scope po operaciji. At-least-once zahteva idempotentne consumere.

Spoljne zavisnosti: deadline, cancellation, bounded retry+jitter, rate limit, circuit breaker kada opravdan, webhook potpis/replay, telemetry. `IHttpClientFactory` + moderni resilience stack.

Upload/download: size/count, MIME+magic bytes, traversal, streaming, private storage, signed URL expiry, tenant, retention, auth na svaki download.

User-supplied URL fetch: scheme, resolved IP, private/metadata ranges, DNS rebinding, redirects, size, timeout. String-only validacija nije dovoljna.

