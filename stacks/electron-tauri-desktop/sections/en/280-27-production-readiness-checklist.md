## 27. Production Readiness Checklist

1. Supported framework/runtime/toolchain versions are verified from source, lock files, packaged artifact, and runtime. No unapproved preview or unsupported major remains.
2. Repository, generated configuration, dependency graph, build scripts, native code, plugins, and supply-chain trust are inventoried and owned.
3. Source-to-installed-runtime identity chain is proven or every break is an explicit blocker/residual risk.
4. Every window/webview has documented origin, lifecycle, session, privilege, bridge/capability, navigation policy, data owner, and negative tests.
5. Electron webPreferences/preload/IPC or Tauri capabilities/permissions/scopes/commands enforce least privilege in the actual packaged app.
6. Remote and user-controlled content cannot reach local code, secrets, files, devices, updater, installer, or other accounts without explicit authorization.
7. Path, URL, deep-link, external-open, file import/export, archive, and local-service boundaries are canonicalized, scoped, authenticated, and tested.
8. Local data has ownership, permissions, schema/migration, backup/restore, corruption recovery, account isolation, retention, and uninstall policy.
9. Critical writes and external side effects have constraints, transactions or durable state transitions, concurrency control, idempotency, and crash recovery.
10. Network clients and local listeners have TLS/peer trust, authentication, timeouts, bounded retry, cancellation, backpressure, redaction, and failure tests.
11. Native modules, FFI, sidecars, codecs, system dependencies, and WebView runtimes are verified on every supported platform/architecture.
12. Package contents contain no unintended secrets, debug surfaces, writable executable code, unsupported binaries, or unexplained additions.
13. Every distributed artifact is tied to source, inspected, hashed, signed as required, timestamped/notarized where applicable, and verified after installation.
14. Install, repair, upgrade from every supported source, skipped-version update, interrupted update, rollback/recovery, and uninstall are tested with representative data.
15. Update metadata, signatures, key custody, channel policy, staged rollout, abort, downgrade, rollback, revocation, and compromised-key response are proven.
16. Startup, responsiveness, memory, CPU, GPU, disk, network, idle, long-run, and failure-containment budgets are measured on representative systems.
17. Accessibility, localization, high DPI, multiple displays, keyboard, screen reader, IME, permissions, and native dialogs are verified in packaged builds.
18. Logs, metrics, traces, crashes, symbols/source maps, alerts, privacy redaction, diagnostic export, and runbooks support incident diagnosis.
19. CI/CD separates untrusted and privileged work, promotes immutable artifacts, protects signing/publishing, retains evidence, and exercises emergency release.
20. All P0/P1 findings are fixed or contain explicit containment and recovery; P2/P3 have owners, acceptance criteria, and priorities.
21. Commands, environments, outputs, skipped checks, evidence ceiling, changed files, tests, artifact hashes, and external sources are recorded.
22. Final verdict is `ready`, `ready-with-conditions`, or `not-ready`, with exact blockers and residual risk.

