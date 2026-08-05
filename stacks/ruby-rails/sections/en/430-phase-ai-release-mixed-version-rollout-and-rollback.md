## Phase AI - Release, Mixed-Version Rollout And Rollback

- Define canary cohort, duration, guardrails, error-budget impact, abort thresholds and decision owner.
- Test old web with new schema, new web with old-compatible schema, old jobs with new arguments, new jobs with old queued payloads and old assets with new server.
- Separate application, configuration, traffic, job, cache, data and schema rollback procedures.
- Use forward repair when destructive data or schema changes make binary rollback unsafe.
- Verify queue pause, write freeze, feature kill switch, cache invalidation and session-key behavior during rollback.
- Record exact release and rollback commands and execute a controlled rehearsal before critical launch.

