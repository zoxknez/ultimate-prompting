## Phase 14 - Route Handlers, APIs, Webhooks, Files, And Streaming

Audit every externally reachable protocol as an explicit contract with bounded resources and safe failure.

### Audit Requirements

- Inventory methods, content types, schemas, authn, authz, CORS, CSRF, rate, body limits, timeouts, cache, and response contracts.
- Prevent BOLA, mass assignment, injection, traversal, open redirect, SSRF, smuggling, unbounded pagination, and stack leakage.
- For webhooks verify raw-body signature, algorithm, rotation, timestamp, replay, ordering, acknowledgement, retry, and idempotency.
- For uploads verify streaming limits, magic bytes, archive expansion, malware workflow, temp storage, ownership, and signed URL expiry.
- For downloads and exports reauthorize, bind owner/tenant, sanitize names, and prevent active-content injection.
- For SSE/streaming define cancellation, heartbeat, reconnect, buffering, slow consumer, backpressure, timeout, and cleanup.

### Required Evidence

- Endpoint and protocol matrix with trust, resource, and failure limits.
- Observed status, headers, body, cache, and error contract.
- Webhook signature and replay evidence.
- Upload/download parser, storage, authorization, and cleanup evidence.

### Mandatory Failure And Acceptance Tests

- Fuzz malformed paths, headers, content types, encodings, bodies, multipart, archives, and ranges safely.
- Replay webhooks around retry, acknowledgement loss, crash, and key rotation.
- Upload oversized, polyglot, archive-bomb, traversal, duplicate-name, and interrupted files.
- Disconnect slow streaming clients and prove bounded memory and cleanup.

