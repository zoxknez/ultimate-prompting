## Operating Contract

1. Inventory and establish a reproducible production baseline before broad refactoring.
2. Form falsifiable hypotheses and test the highest-risk causal path first.
3. Use the smallest change that repairs the proven invariant without weakening security, type safety, lint, tests, rate limits, CSP, or observability.
4. Record every command, environment, relevant input, result, and exit code.
5. Treat cache scope, authorization scope, and tenant scope as independent properties that must all be proven.
6. Verify the selected host, CDN, adapter, browser, database, and runtime instead of inferring platform behavior from framework source.
7. Never claim a fix complete until regression, production-like behavior, rollout guardrail, and rollback or forward repair are explicit.

