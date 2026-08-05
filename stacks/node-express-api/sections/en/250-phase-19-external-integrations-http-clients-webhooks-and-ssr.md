## Phase 19 - External Integrations, HTTP Clients, Webhooks, And SSRF

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Inventory every external hostname, protocol, credential, timeout, retry, circuit breaker, rate limit, and data classification.
- Set connect, DNS, TLS, pool acquisition, request, read, write, total, and idle deadlines appropriate to each client.
- Propagate AbortSignal and deadlines through request, database, queue, file, and provider calls where supported.
- Use bounded retries with backoff, jitter, retry budget, idempotency awareness, and nested-retry prevention.
- For user-controlled URLs, enforce scheme, resolved IP, private and metadata ranges, redirects, DNS rebinding, size, and timeout controls.
- For webhooks, verify raw-body signature, timestamp, replay window, key rotation, ordering, acknowledgement, and idempotency.

### Required Evidence

- Produce and preserve the integration, timeout, and retry matrix.
- Produce and preserve the SSRF resolution and redirect evidence.
- Produce and preserve the webhook signature, replay, and reconciliation results.

### Mandatory Failure And Acceptance Tests

- Prove that private and metadata addresses remain unreachable.
- Prove that a non-idempotent write is not blindly retried.
- Prove that webhook replay returns the stored outcome without duplicate effects.

