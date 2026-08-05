## Definition Of Done

1. The repository, dependency graph, generated code, artifact, deployment, process, schema, and telemetry are correlated.
2. All baseline commands and meaningful warnings have real results and exit codes.
3. Every finding contains evidence, root cause, impact, repair, regression, rollout, rollback, and residual risk.
4. P0 findings are contained and recovered; P1 findings do not remain as undocumented release risk.
5. Critical authorization, tenant, transaction, idempotency, replay, timeout, abort, and shutdown paths are tested.
6. Effective Express or Fastify behavior is verified in the target runtime, not inferred from source alone.
7. Event-loop, memory, pool, queue, provider, and overload behavior meet explicit thresholds.
8. The same immutable artifact is promoted and identifiable in the running process.
9. Rollout, abort, rollback or forward repair, reconciliation, and monitoring are executable and owned.
10. An isolated restore proves data, keys, schema, tenant isolation, critical journeys, RPO, and RTO.
11. The final report states READY, READY_WITH_CONDITIONS, NOT_READY, or INCIDENT and names every blocker.
12. No result, source, command output, test success, version, or production behavior is invented.

If any mandatory item is missing, state: **The system is not yet fully production-ready.**

