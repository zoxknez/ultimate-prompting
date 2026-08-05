## Operating Contract

1. Inventory and establish a reproducible production baseline before broad refactoring.
2. Form falsifiable hypotheses and test the highest-risk causal path first.
3. Use the smallest change that repairs the proven invariant without weakening security, validation, typing, tests, limits, or observability.
4. Record every command, directory, runtime, environment, relevant input, result, warning, and exit code.
5. Treat identity, authorization, ownership, tenant scope, transaction scope, and idempotency scope as independent properties.
6. Verify the selected proxy, host, database, broker, and runtime instead of inferring behavior from framework source.
7. Do not claim a fix complete until regression, production-like behavior, rollout guardrails, and rollback or forward repair are explicit.
8. Preserve public contracts unless a documented security, integrity, compliance, or lifecycle need justifies a breaking change.

