## Phase 8 - HTTP Server, Reverse Proxy, CDN, And Transport Semantics

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Map client, CDN, WAF, load balancer, ingress, service mesh, reverse proxy, Node server, and downstream hops.
- Verify request, headers, keep-alive, idle, body, upstream, and shutdown timeouts across all hops.
- Audit HTTP/1.1, HTTP/2, TLS termination, ALPN, connection reuse, proxy protocol, and forwarded headers.
- Test request smuggling, duplicate content-length, transfer-encoding ambiguity, malformed headers, and hop disagreement.
- Validate host, origin, absolute-form URL, path normalization, encoded separators, and method override handling.
- Verify overload, slowloris, half-open connection, compression, range, cache, and client-abort cleanup behavior.

### Required Evidence

- Produce and preserve the hop-by-hop timeout and header matrix.
- Produce and preserve the trusted proxy, TLS, and parser configuration map.
- Produce and preserve smuggling and malformed-request results.

### Mandatory Failure And Acceptance Tests

- Prove that spoofed host and forwarded headers are rejected or normalized.
- Prove that a slow client cannot retain unbounded resources.
- Prove that the proxy and application agree on request framing.

