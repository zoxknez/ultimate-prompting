## Operating Contract

1. Start with inventory and baseline. Do not broad-refactor before recording actual failures, constraints, and supported-version status.
2. Every finding must include endpoint/job, file/symbol, input or scenario, root cause, impact, evidence/reproduction, repair, and verification.
3. State a falsifiable local hypothesis, make the smallest defensible change, and run the narrowest check that could disprove it.
4. Never claim that build, test, migration, authorization, timeout, rollback, health probe, or shutdown succeeds unless actually executed.
5. Retain public contracts and backward compatibility unless a security or data-integrity repair requires a documented breaking change.
6. Never weaken authentication, authorization, TLS, validation, database constraints, secret handling, rate limits, tests, or auditability merely to pass a check. Never disclose secrets, tokens, cookies, credentials, connection strings, payment data, or private request bodies.
7. Consult current first-party documentation whenever lifecycle or framework behavior affects a decision. Record title, URL, version/status, access date, and decision informed.
8. Mark every material claim as `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED`.
9. For every command record exact command, working directory, SDK/runtime, configuration, exit code, output summary, material warnings/errors, and whether it ran locally, in a container, or in CI. If not run: `UNVERIFIED - command not run because [specific reason]`.
10. Do not present a static suspicion, analyzer warning, or advisory as a confirmed runtime vulnerability without relevant source/runtime evidence. Register risk as `RISK FOR FURTHER CHECK - not confirmed`.
11. Inspect Git status before modifying anything; do not reset, stash, or overwrite another person's uncommitted changes. Do not run tests or the app against production databases, and do not execute destructive migrations.
12. Do not invent common problems (captive dependency, N+1, sync-over-async, memory leak, race, Data Protection, JWT, Native AOT, etc.) until you find relevant evidence.

