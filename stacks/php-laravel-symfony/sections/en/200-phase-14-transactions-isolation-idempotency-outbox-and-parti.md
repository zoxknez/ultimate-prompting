## Phase 14 - Transactions, Isolation, Idempotency, Outbox, and Partial Failure

### Objective

Prove atomicity, replay safety, consistency, and recovery across database and external side-effect boundaries.

### Audit Requirements

- Map every critical mutation to transaction manager, connection, isolation level, timeout, retry policy, lock order, and commit boundary.
- Verify framework transaction helpers, nested transactions, savepoints, multiple connections, callback timing, exception conversion, and rollback semantics.
- Test lost update, write skew, phantom, uniqueness race, duplicate request, deadlock, timeout, process crash, and client disconnect.
- Design idempotency with authenticated scope, request fingerprint, atomic ownership, in-progress state, durable result, expiry, retry, and conflict behavior.
- Use transactional outbox, inbox, CDC, or an equivalent proven design when database state and messages or external effects must agree.
- Define reconciliation and compensating actions for payments, email, object storage, search indexing, webhooks, and other non-transactional effects.

### Required Evidence

- Critical-flow transaction and side-effect matrix with every crash point identified.
- Concurrent and replay test evidence around pre-commit, commit, and post-commit boundaries.
- Outbox, inbox, reconciliation, and manual recovery evidence for partial failures.

### Acceptance Criteria

- A retry, duplicate delivery, timeout, or process crash cannot silently duplicate or lose a critical business effect.
- Every non-atomic cross-system flow has detectable divergence and a tested recovery procedure.

