## Phase I - Rack, Routing, Middleware And HTTP Semantics

- Inventory every route, mount, engine, admin UI, health endpoint, metrics endpoint, file route, webhook and websocket upgrade path.
- Record middleware order and verify authentication, sessions, CSRF, CORS, compression, host authorization, rate limiting, logging and exception handling order.
- Test method handling, canonical paths, encoded separators, duplicate headers, host headers, forwarded headers, redirects and proxy trust.
- Verify request, header, URL, body, multipart, decompression and response-size limits at proxy, server and application layers.
- Audit HTTP caching, conditional requests, ETags, range requests, streaming and client disconnect behavior.

