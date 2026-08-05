## Repair And Verification Workflow

1. Register the finding with evidence and an explicit invariant.
2. Reproduce the smallest failing path and preserve the command, input, and result.
3. Identify the authoritative layer that must enforce the invariant.
4. Design the smallest reversible repair and list rejected alternatives with reasons.
5. Add a targeted regression test before or with the repair where feasible.
6. Run narrow tests, then affected integration, contract, security, concurrency, load, and production-build checks.
7. Inspect the final diff, lockfile, generated output, artifacts, migrations, and configuration for unintended changes.
8. Define rollout guardrails, abort criteria, rollback or forward repair, monitoring, and residual risk.
9. Do not close the finding until evidence and acceptance criteria are met.

