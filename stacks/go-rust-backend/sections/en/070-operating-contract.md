## Operating Contract

1. Start with inventory and baseline. Do not broad-refactor before recording actual failures, constraints, and support status.
2. Every finding must include flow/endpoint/job, file/symbol, input or scenario, root cause, impact, evidence/reproduction, repair, and verification.
3. State a falsifiable local hypothesis, make the smallest defensible change, and run the narrowest check that could disprove it.
4. Never claim that build, test, race, Miri, fuzz, migration, authorization, timeout, rollback, health, or shutdown succeeds unless actually executed.
5. Retain public contracts, protocols, and compatibility unless a documented security or data-integrity repair requires a breaking change.
6. Never weaken authentication, authorization, TLS, validation, database constraints, secret handling, rate limits, tests, or auditability merely to pass a check. Never disclose secrets, tokens, private keys, connection strings, credentials, or sensitive payloads.
7. Consult current first-party documentation whenever language/runtime lifecycle or behavior affects a decision. Record title, URL, version/status, access date, and decision informed.
8. Evidence status: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED`.
9. For every command record: exact command, directory, toolchain, target, feature/tag, environment when material, exit code, real result, material warnings, and check limits. If not run: `UNVERIFIED - command not run because [reason]`.
10. Do not invent common problems (goroutine leak, data race, unsound unsafe, N+1, SQL injection, memory leak, etc.) until you find relevant evidence. Risk: `RISK FOR FURTHER CHECK - not confirmed`.
11. Inspect Git status before modifying anything; do not reset, stash, or overwrite another person's uncommitted changes. Do not run tests against production databases or execute destructive migrations.
12. Do not change the toolchain before recording the initial state.

