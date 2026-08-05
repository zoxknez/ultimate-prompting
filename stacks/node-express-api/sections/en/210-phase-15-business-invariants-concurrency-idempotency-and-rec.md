## Phase 15 - Business Invariants, Concurrency, Idempotency, And Reconciliation

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- List authoritative invariants for money, inventory, entitlement, quota, uniqueness, state transitions, and external side effects.
- Map every read-modify-write flow, race window, lock, version check, database constraint, transaction, and retry boundary.
- Define idempotency key source, actor and operation scope, request fingerprint, storage, atomic claim, expiry, and stored outcome.
- Do not rely on process memory, module globals, or one replica for durable idempotency or locking.
- Distinguish transport retry, application retry, queue replay, user double-submit, provider replay, and operator re-run.
- Define reconciliation where database and external systems cannot commit atomically and test crash points around all side effects.

### Required Evidence

- Produce and preserve the critical-invariant and concurrency register.
- Produce and preserve the idempotency and crash-point matrix.
- Produce and preserve the reconciliation procedure and ownership record.

### Mandatory Failure And Acceptance Tests

- Prove that parallel mutations preserve the invariant.
- Prove that the same idempotency key with a different payload is rejected.
- Prove that a timeout after commit reconstructs the stored outcome without duplicate side effects.

