## Production Decision Rule

- Return exactly one verdict: `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`, or `INCIDENT_CONTAINMENT_REQUIRED`.
- A `READY` verdict requires applicable P0 and P1 findings closed, mandatory matrices complete, critical scenarios passed, immutable artifact verified, rollout and rollback proven, and restore evidence meeting approved RPO/RTO.
- Use `READY_WITH_CONDITIONS` only when every condition has owner, deadline, containment, measurable acceptance criterion, and no hidden P0/P1 exposure.
- Any unresolved critical authorization, data-integrity, memory-safety, concurrency, migration, supply-chain, rollback, or restore risk blocks an unconditional ready verdict.

