## 21. Observability, Crash Reporting, Privacy, And Forensics

1. Define structured logs, metrics, traces, crash reports, update events, installer events, security events, and user-visible diagnostic export.
2. Include version, channel, commit/artifact identity, platform, architecture, OS version, WebView/Chromium/Node/Rust relevant version, process type, window label, correlation ID, and operation state where safe.
3. Redact secrets, tokens, cookies, authorization headers, file contents, personal paths, usernames, document names, database records, clipboard data, and sensitive URLs.
4. Use sampling and rate limits to prevent telemetry storms, privacy overcollection, disk exhaustion, and recursive crash-reporting failures.
5. Upload symbols and source maps tied to exact artifact hashes. Restrict access and retention.
6. Distinguish renderer/webview, main/Rust core, GPU, utility, sidecar, installer, updater, and native crash sources.
7. Track startup success, crash-free sessions, update adoption/failure, rollback, migration failure, permission denial, IPC/command denial, queue saturation, and resource budgets.
8. Provide a privacy-preserving local diagnostic bundle with explicit user review and consent where appropriate.
9. Preserve chain of custody for incident artifacts and avoid altering compromised systems before evidence capture.
10. Every production alert must have owner, threshold rationale, dashboard/context, runbook, and user-impact interpretation.

