## 32. Observability, Diagnostics, Crash Reporting, And Supportability

### 32.1 Audit Scope

1. Inventory structured logs, audit events, metrics, traces, crash reporting, native dumps, Python exception hooks, Qt messages, performance traces, and support bundles.
2. Record release, artifact hash, channel, platform, architecture, Python, Qt, PySide6, packaging mode, data schema, configuration, account/tenant pseudonym, and feature flags where privacy permits.
3. Review log levels, cardinality, sampling, retention, redaction, local storage, upload consent, offline buffering, exporter failure, and support access.
4. Ensure GUI-thread stalls, worker failures, deadlocks, queue growth, memory pressure, update failure, migration failure, device disconnect, and data corruption are diagnosable.
5. Define health and readiness for local helpers, services, databases, update channels, network dependencies, and critical background workers.
6. Map user-facing incident IDs to privacy-safe technical evidence without exposing secrets or internal implementation details.

### 32.2 Required Verification

1. Force representative failures and verify the installed application emits sufficient, correlated, redacted evidence and actionable user guidance.
2. Confirm crash and support artifacts can identify exact delivered bytes and loaded native components, not only a marketing version.
3. Test offline buffering, disk full, exporter outage, permission denial, crash-loop rate limiting, and user opt-out behavior.
4. Verify support-bundle generation is bounded, cancellable, consented, redacted, reviewable, and safe against symlink/path attacks.
5. Define dashboards, alerts, runbooks, owners, escalation, and release-correlation procedures for material production signals.

