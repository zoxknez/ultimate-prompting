## 23. Observability, Crash, And Operational Readiness

### 23.1 Telemetry And Symbolication
- Correlate logs, traces, metrics, crash reports, ANRs, hangs, native crashes, JavaScript errors, network events, background work, and updates with one release identity.
- Upload and retain matching JavaScript source maps, Hermes maps, Android mapping, native symbols, dSYM, and build metadata securely.
- Redact tokens, credentials, personal data, message content, file paths, precise location, and sensitive identifiers before telemetry leaves the device.
- Define SLI and SLO for crash-free users, crash-free sessions, ANR or hang rate, startup, update success, critical journey success, sync freshness, and notification handling.
- Create alerts with threshold, window, cohort, severity, owner, runbook, suppression, and release or update correlation.
- Verify telemetry still works during partial backend outage, update failure, authentication failure, offline state, and crash-loop recovery without causing additional failure.

### 23.2 Runbooks And Supportability
- Provide runbooks for crash spike, ANR spike, update mismatch, signing failure, store rejection, push failure, auth outage, sync corruption, and compromised dependency.
- Define safe support diagnostics with user consent, redaction, bounded retention, version identity, and no secret exposure.
- Document how to identify installed native build, current update, channel, environment, account scope, device class, storage schema, and pending work.
- Provide kill switches for risky client features, background jobs, providers, native capabilities, and backend interactions where appropriate.
- Define customer communication, store review constraints, staged mitigation, data reconciliation, and evidence preservation.
- Exercise the runbooks and record gaps, owners, deadlines, and follow-up verification.

