## Release, Rollback, Restore, And Incident Contract

- Promote one immutable artifact through environments; do not silently rebuild production from the same source version.
- Define pre-deploy gates, canary population, SLI comparison, error-budget impact, abort signals, human ownership, maximum observation window, and automatic versus manual rollback.
- Verify graceful shutdown against real orchestration timing, connection draining, readiness removal, in-flight deadlines, queue lease behavior, background workers, and final telemetry flush.
- Document rollback limitations after schema, message, cache, key, file-format, side-effect, or external-contract changes; use forward repair when reversal is unsafe.
- Prove isolated restore, application compatibility, migration replay, key access, external dependency restoration, event reconciliation, RPO, RTO, and integrity checks.
- In incident mode preserve volatile and durable evidence, stop destructive cleanup, bound access, rotate or revoke affected trust, contain blast radius, produce trusted rebuilds, verify eradication, and record recovery decisions.

