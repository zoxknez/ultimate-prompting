## Definition Of Done

Work is complete only when applicable items are marked with evidence or `NOT_APPLICABLE` with rationale:

1. Repo snapshot and status of others' changes are recorded.
2. Solution and all relevant projects are inventoried; dependency graph mapped.
3. SDK, runtime, C#, ASP.NET Core, EF Core, and NuGet versions verified; lifecycle/EOL from current official sources.
4. Restore, Debug/Release build, test, and publish status recorded with real commands.
5. Critical business flows mapped.
6. All P0/P1 have evidence, cause, impact; fixed or have containment and recovery.
7. Potential risks separated from confirmed findings.
8. AuthN/AuthZ/ownership/tenant verified with positive and negative tests.
9. Data Protection strategy verified.
10. Critical write flows have constraints, concurrency, and idempotency evidence.
11. EF migrations reviewed; transaction boundaries documented.
12. Async propagates cancellation where needed; timeout/retry defined.
13. Message/job ack, dedup, and shutdown verified or marked UNVERIFIED.
14. Secrets, configuration, and supply chain audited; secrets not disclosed.
15. Health/observability enable diagnosis; alert/runbook where present.
16. Performance not declared without measurement.
17. Graceful shutdown tested or clearly UNVERIFIED.
18. Rollout and rollback documented.
19. Implemented changes minimal and tied to findings; P0–P2 have regression tests.
20. Relevant test/build/publish scope executed after changes.
21. Command log complete (command, dir, SDK, config, exit, summary).
22. Final diff free of unrelated changes.
23. Final verdict, blockers, residual risk, recovery, and next owners clear.

If any condition is unmet: **The project is not yet fully production-ready.** List the blocking conditions precisely.

