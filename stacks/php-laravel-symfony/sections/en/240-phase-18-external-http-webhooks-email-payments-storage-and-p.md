## Phase 18 - External HTTP, Webhooks, Email, Payments, Storage, and Provider Resilience

### Objective

Audit outbound trust, timeout, retry, identity, reconciliation, and degraded behavior for every external dependency.

### Audit Requirements

- Inventory every HTTP client, SDK, payment provider, mail service, object store, identity provider, search service, analytics sink, and custom integration.
- Verify connect, TLS, pool, request, response, total, and queue timeout budgets plus cancellation and deadline propagation.
- Audit retry eligibility, backoff, jitter, maximum attempts, retry budget, nested retries, circuit breaking, bulkheads, rate limits, and load shedding.
- Validate TLS trust, hostname, certificate rotation, mTLS identity, DNS, redirect policy, proxy use, credential scope, and SSRF resistance.
- For inbound webhooks, verify raw-body signatures, canonicalization, timestamp, replay window, key rotation, event identity, ordering, and idempotency.
- For payments and other irreversible effects, prove state-machine transitions, duplicate handling, asynchronous confirmation, refunds, disputes, and reconciliation.

### Required Evidence

- Dependency contract matrix with owner, timeout, retry, credential, data, SLO, and degraded mode.
- Slow, unavailable, malformed, replayed, rotated-key, rate-limited, and partial-success test evidence.
- Provider reconciliation and manual recovery evidence for irreversible effects.

### Acceptance Criteria

- A slow or failing provider cannot exhaust the service or create uncontrolled duplicate side effects.
- Every externally confirmed business state can be reconciled against an authoritative provider record.

