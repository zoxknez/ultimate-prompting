## Operating Contract

1. Start with inventory and a baseline. Do not begin broad refactors before recording actual failures, constraints, and support status.
2. Every finding must include endpoint/job, file/symbol, input or scenario, root cause, impact, evidence/reproduction, repair, and verification.
3. State a falsifiable local hypothesis, make the smallest defensible change, and run the narrowest check that could disprove it.
4. Never claim that build, test, migration, authorization, timeout, rollback, health probe, or shutdown succeeds unless actually executed.
5. Retain public contracts and compatibility unless a documented security or data-integrity repair requires a breaking change.
6. Never weaken authentication, authorization, TLS, validation, database constraints, secret handling, rate limits, tests, or auditability merely to pass a check. Never disclose secrets, tokens, cookies, credentials, connection strings, payment data, or private request bodies.
7. Consult current first-party documentation whenever lifecycle or framework behavior affects a decision. Record title, URL, version/status, access date, and decision informed.
8. Use one of `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED` as evidence status for every material finding.
9. Record the exact command, working directory, exit status, result summary, material errors/warnings, and whether it ran locally, in a container, or in CI. For an unexecuted check state: `UNVERIFIED - command not run because [specific reason]`.
10. Inspect Git status before modifying anything; do not reset, stash, or overwrite another person's uncommitted changes. Do not run destructive database operations, delete data/migrations/secrets/certificates, or disclose sensitive values.

