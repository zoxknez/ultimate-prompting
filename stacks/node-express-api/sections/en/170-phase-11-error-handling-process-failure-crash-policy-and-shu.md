## Phase 11 - Error Handling, Process Failure, Crash Policy, And Shutdown

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Define error categories for validation, authentication, authorization, conflict, rate limit, dependency, timeout, cancellation, invariant, and internal failure.
- Map each category to stable status, code, safe message, retry guidance, request ID, and telemetry severity.
- Prevent stack, SQL, filesystem path, token, internal host, header, and dependency-detail leakage.
- Handle rejected promises, callback errors, stream errors, emitter errors, and background task failures explicitly.
- Define uncaughtException, unhandledRejection, fatal error, OOM, and native crash policy; never continue in an unknown state.
- On SIGTERM or shutdown, withdraw readiness, stop intake, drain requests and jobs, close pools, flush telemetry, and exit within a deadline.

### Required Evidence

- Produce and preserve the error taxonomy and response contract.
- Produce and preserve the fatal-process, restart, and crash-loop policy.
- Produce and preserve shutdown ownership and timing evidence.

### Mandatory Failure And Acceptance Tests

- Prove that a rejected promise terminates the request correctly once.
- Prove that a fatal process error leads to controlled replacement.
- Prove that shutdown during long requests and jobs follows the documented recovery path.

