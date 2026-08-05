## 29. Network, API Contracts, TLS, And Resilience

Audit the complete client-to-service behavior under normal, degraded, hostile, and evolving conditions.

- Inventory HTTP clients, interceptors, adapters, WebSocket/SSE clients, GraphQL, gRPC, upload/download stacks, DNS behavior, proxies, and platform network configuration.
- Verify base URL and environment selection, scheme, host allowlists, redirects, cleartext policy, ATS/network security config, proxy behavior, local network access, and certificate validation.
- Use explicit connect, send, receive, idle, and total deadlines where supported; propagate cancellation and operation deadlines.
- Retry only safe or idempotent operations with bounded attempts, backoff, jitter, server hints, budget, and overload protection.
- Verify API schema, content type, compression, pagination, partial response, unknown fields, error envelope, Problem Details, localization, and backward compatibility.
- Audit token-refresh interaction, request replay, duplicate body streams, upload resume, download integrity, redirect authorization stripping, and cancellation.
- Treat TLS pinning as an operationally expensive optional control requiring backup pins, rotation, expiry monitoring, proxy policy, emergency disable, and tested recovery.
- Test offline, captive portal, DNS failure, IPv4/IPv6, TLS failure, expired certificate, slow body, truncated body, malformed payload, 429, 5xx, timeout, reconnect, and clock skew.
- Measure latency distribution, failure rate, retries, bytes, cache hits, queue time, cancellation, backend amplification, and user-visible recovery.

