## 14. Phase I - Networking, APIs And Real-Time Communication

1. Inventory all base URLs, clients, interceptors, authenticators, DNS behavior, proxies, WebSockets, streaming, and download paths per variant.
2. Verify connect, read, write, call, ping, and overall timeouts match operation semantics.
3. Verify retries only for safe or idempotent operations, or use idempotency keys and server support.
4. Verify cancellation closes calls, streams, parsers, files, and progress jobs.
5. Verify authentication refresh is serialized correctly and cannot create refresh storms or token races.
6. Prevent credentials, headers, bodies, media URLs, query parameters, and PII from release logs.
7. Verify TLS defaults, trust managers, hostname verification, network security configuration, cleartext exceptions, and certificate pinning strategy where justified.
8. Never accept all certificates or disable hostname verification.
9. Validate response codes, content type, content length, redirects, compression, charset, schema, and error bodies.
10. Bound downloads, uploads, decompression, image sizes, parser depth, and memory use.
11. Verify resumable transfer, range requests, temporary files, atomic rename, integrity checks, and cleanup.
12. Verify pagination, caching, ETag, stale data, rate limits, backpressure, and offline fallback.
13. Test slow, flaky, captive, metered, roaming, IPv6-only, DNS-failure, proxy, and no-network scenarios where material.
14. Verify real-time reconnect, message ordering, duplicate delivery, missed events, heartbeat, and background restrictions.
15. Verify server errors are mapped to actionable, localized, privacy-safe user states.

