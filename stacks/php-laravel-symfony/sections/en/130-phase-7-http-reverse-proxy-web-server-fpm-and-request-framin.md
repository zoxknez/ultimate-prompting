## Phase 7 - HTTP, Reverse Proxy, Web Server, FPM, And Request Framing

### Objective

Verify end-to-end HTTP semantics and prevent mismatches between network hops and application parsing.

### Audit Requirements

- Map client, CDN, WAF, load balancer, ingress, reverse proxy, web server, FastCGI, FPM pool, and application limits and timeouts.
- Audit trusted proxy configuration, forwarded headers, client IP, scheme, host, port, prefix, absolute URLs, and redirect generation.
- Test duplicate `Content-Length`, conflicting `Transfer-Encoding`, malformed headers, encoded paths, null bytes, path normalization, method override, and smuggling defenses.
- Verify body, header, URI, multipart, file, decompression, execution, idle, upstream, keepalive, and shutdown limits across all hops.
- Audit Nginx or Apache FastCGI parameters, script path resolution, document root, static handling, internal redirects, error pages, and source disclosure.
- Verify client disconnect, aborted request, output buffering, streaming, SSE, large response, and partial-response cleanup semantics.

### Required Evidence

- Hop-by-hop timeout and size-limit matrix.
- Trusted proxy and effective URL evidence using the real deployment topology.
- Negative protocol tests at the edge and application boundary.

### Acceptance Criteria

- No untrusted hop can spoof identity, scheme, host, tenant, rate-limit key, or secure-cookie behavior.
- Request framing and timeout policy prevent ambiguous parsing and resource exhaustion.

