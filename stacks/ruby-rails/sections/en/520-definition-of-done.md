## Definition Of Done

- [ ] All active runtime, server, job, database and deployment paths are identified.
- [ ] Version and support decisions are based on current official sources and actual lock/runtime evidence.
- [ ] Every P0 and P1 is fixed, mitigated with explicit acceptance, or blocks release.
- [ ] Critical business invariants have application, database, concurrency and reconciliation evidence.
- [ ] Authorization and tenant isolation have negative tests across HTTP, jobs, cache, files and realtime.
- [ ] Release artifacts, migrations, jobs and process shutdown are verified in production-like conditions.
- [ ] Performance and capacity claims are measured or explicitly marked unverified.
- [ ] Rollback or forward repair and isolated restore are executable, not only documented.
- [ ] Command logs, evidence links, changed files, tests, deployment impact and residual risk are included.
- [ ] The final verdict is `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`, or `INCIDENT`, with blockers and owners.

If any required item is missing, state: **The Ruby on Rails system is not fully production-ready within the audited scope.**

