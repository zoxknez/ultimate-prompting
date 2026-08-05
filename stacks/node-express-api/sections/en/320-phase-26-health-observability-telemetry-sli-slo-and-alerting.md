## Phase 26 - Health, Observability, Telemetry, SLI, SLO, And Alerting

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Separate startup, liveness, readiness, degraded, dependency, and deep diagnostic signals.
- Readiness must reflect ability to accept safe traffic, not merely that the event loop is alive.
- Instrument request rate, errors, latency, saturation, event-loop delay, memory, handles, pools, queues, retries, timeouts, and dependencies.
- Initialize OpenTelemetry before instrumented modules where required and verify context propagation through clients, queues, and workers.
- Define sampling, cardinality limits, baggage policy, redaction, retention, exporter failure, and telemetry backpressure.
- Define user-centered SLI and SLO, error budget, burn-rate alerts, owner, runbook, escalation, and recovery confirmation.

### Required Evidence

- Produce and preserve the health-state and readiness decision table.
- Produce and preserve the telemetry-coverage and redaction matrix.
- Produce and preserve the SLI, SLO, alert, owner, and runbook register.

### Mandatory Failure And Acceptance Tests

- Prove that readiness withdraws before unsafe dependency state.
- Prove that telemetry exporter failure cannot crash or saturate the service.
- Prove that alerts fire and resolve on tested failure and recovery paths.

