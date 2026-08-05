## 22. Test Strategy And Mandatory Negative Scenarios

### 22.1 Test Layers

1. Unit-test pure business logic, parsers, validators, canonicalizers, state machines, authorization decisions, migration steps, and update-version policy.
2. Contract-test every preload bridge, Electron IPC channel, Tauri command, event/channel payload, sidecar protocol, local service, update metadata, and installer exit-code contract.
3. Integration-test with real filesystem semantics, real embedded database engine, secure-storage abstraction, representative proxy/certificate setup, and actual platform WebView/runtime where applicable.
4. Run packaged-application tests, not only browser/dev-server tests. Verify effective privileges, resources, signatures, paths, and OS integrations.
5. Use end-to-end tests for critical user journeys: install, first run, sign in, account switch, file/device workflow, offline/online transition, update, restart, rollback, export, logout, and uninstall.
6. Use security tests for XSS-to-bridge reachability, IPC/command authorization, path/URL validation, local-service authentication, update tampering, signature failure, and data isolation.
7. Use concurrency and durability tests for duplicate actions, multiple windows, multiple instances, background jobs, database locking, update overlap, shutdown, and crash recovery.
8. Use performance tests for startup, critical interactions, large data, burst input, many windows, idle, long-run leaks, low resources, and slow dependencies.
9. Use accessibility tests with automated checks plus keyboard and screen-reader verification in packaged builds.
10. Use installation and update matrices on clean snapshots/VMs with realistic old versions and user data.
11. Every confirmed P0-P2 fix must have a focused regression test that would fail before the fix and pass after it.
12. Record skipped, flaky, quarantined, platform-unavailable, or manually verified tests with owner, reason, risk, and exit criterion.

### 22.2 Mandatory Adversarial And Failure Scenarios

1. Compromised renderer/webview attempts every exposed Electron bridge or Tauri command from the wrong origin, frame, window, label, account, and lifecycle generation.
2. Malicious IPC/command payload uses extra fields, wrong types, deep nesting, huge strings/binaries, traversal, symlinks, UNC/device paths, alternate schemes, and encoded separators.
3. Two windows or instances submit the same destructive or externally visible operation concurrently and after a renderer reload.
4. Caller navigates, logs out, changes account, closes, or is destroyed while privileged work is in progress and before the result is delivered.
5. Remote content redirects, opens a new window, calls an external protocol, downloads active content, and attempts to retain privileges after navigation.
6. Local untrusted process attempts to connect to localhost/socket/pipe/helper interfaces, replay messages, impersonate the application, or squat on the endpoint.
7. Update metadata, package, signature, publisher, channel, architecture, version, and endpoint are independently tampered with.
8. Update is interrupted during download, verification, install, first restart, data migration, sidecar replacement, and cleanup.
9. Fresh install, repair, upgrade from each supported old version, skipped-version upgrade, downgrade attempt, rollback, and uninstall run with realistic user data.
10. Signing certificate or updater key is expired, revoked, missing, wrong, inaccessible, or believed compromised.
11. Disk becomes full or read-only during write, database transaction, migration, export, download, update, logging, and crash reporting.
12. Application is terminated, OS shuts down, user logs out, machine sleeps, or power is lost during critical work.
13. Native module, sidecar, plugin, WebView runtime, codec, driver, or system dependency is missing, wrong architecture, incompatible, slow, hung, or maliciously replaced.
14. Proxy auth, captive portal, DNS failure, TLS interception, certificate error, clock skew, slow server, partial response, oversized response, and retry storm occur.
15. User switches accounts, OS users, channels, or profiles while caches, cookies, windows, background work, notifications, and local data still exist.
16. Many windows, large files, hotplug storms, burst IPC/events, slow consumer, and long-running idle push CPU, memory, GPU, disk, queue, and listener limits.

### 22.3 Platform And Architecture Matrix

| Dimension | Required coverage | Evidence |
| --- | --- | --- |
| Operating system | Each supported Windows, macOS, and Linux baseline plus current representative versions | Clean VM/device, exact build, install/update/runtime results |
| Architecture | x64, ARM64, and any additional shipped target | Native module/sidecar/plugin/package/signature/runtime verification |
| Distribution | Direct, store, enterprise, portable, repository, or package format actually shipped | Channel-specific install, update, rollback, and policy evidence |
| Source version | Fresh install and every supported upgrade source, including a realistically old version | Versioned snapshots with representative user data |
| Environment | Online, offline, proxy, enterprise TLS interception where supported, low disk, low memory | Recorded conditions, logs, user-visible outcome, recovery |
| Display/input | Single/multiple mixed-DPI displays, keyboard, screen reader, IME, touch where supported | Packaged-app accessibility and window-state evidence |

