## 47. Observability, Telemetry, Crash Reporting, And Diagnostics

Telemetry must identify user impact without becoming a privacy or stability risk.

- Define events, metrics, traces, logs, crash reports, breadcrumbs, network diagnostics, performance spans, release markers, and business outcome signals.
- Attach application version, build, platform, OS/browser, device class, flavor, environment, feature flag state, operation ID, and privacy-safe account/tenant correlation.
- Redact tokens, credentials, authorization headers, cookies, personal data, file content, sensitive paths, notification payloads, form fields, and raw database values.
- Verify Flutter framework errors, platform errors, uncaught async errors, isolate errors, native crashes, ANR/hang, web errors, and update/install failures are captured without loops.
- Upload and retain exact Dart symbol maps, Android mapping/native symbols, Apple dSYM, Windows/macOS/Linux symbols, and web source maps per artifact.
- Define sampling, consent, opt-out, retention, data residency, access controls, deletion, vendor outage behavior, SDK failure isolation, and cost limits.
- Create dashboards and alerts for crash-free users/sessions, startup, jank, memory, network errors, auth failures, migration failures, sync conflicts, update failures, and critical journeys.
- Verify each actionable alert has owner, threshold, deduplication, runbook, escalation, safe diagnostic queries, and closure evidence.
- Test telemetry while offline, during startup failure, after logout, under crash loops, with blocked vendors, and across staged release/rollback.

