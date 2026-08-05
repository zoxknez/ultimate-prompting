## Repair and Verification Workflow

1. Reproduce or establish the finding with the strongest available evidence and preserve a minimal failing case.
2. Identify root cause, affected trust boundary, invariant, process type, data, tenant, release, and failure window.
3. Design the smallest complete fix that removes the cause without hiding the symptom or weakening another control.
4. Add deterministic regression, negative, concurrent, failure, migration, or recovery tests appropriate to the risk.
5. Re-run targeted checks, then the relevant framework, integration, security, load, migration, and packaging suites.
6. Build the production artifact from a clean checkout and verify its digest, contents, runtime compatibility, and release metadata.
7. Deploy through the intended path with canary or staged guardrails, complete process replacement, and telemetry correlation.
8. Verify user-visible behavior, invariants, authorization, tenant isolation, side effects, queues, data, health, and rollback conditions.
9. Update the finding record with evidence, residual risk, owner, operational action, expiry, and final status.

