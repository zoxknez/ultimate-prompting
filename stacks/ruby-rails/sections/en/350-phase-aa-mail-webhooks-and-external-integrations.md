## Phase AA - Mail, Webhooks And External Integrations

- Audit Action Mailer delivery, queueing, retries, template data exposure, header injection and duplicate sends.
- Verify outbound webhook signing, timestamp, key rotation, canonicalization, retry, ordering, idempotency and dead-letter handling.
- For inbound webhooks, validate signature before parsing expensive content and reject replay and cross-account routing.
- Define connect, TLS, request, read, write, total and pool-acquisition timeouts for every external dependency.
- Use bounded retries, jitter, circuit breaking, bulkheads and reconciliation without multiplying retry layers.
- Audit SSRF, redirects, DNS rebinding, proxy settings, credential scope and response-size limits.

