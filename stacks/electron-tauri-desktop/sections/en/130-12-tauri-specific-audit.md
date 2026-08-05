## 12. Tauri-Specific Audit

### 12.1 Core, CLI, API, Runtime, WebView, And Plugin Matrix

1. Resolve the exact versions of `tauri`, `tauri-build`, `tauri-cli`, `@tauri-apps/cli`, `@tauri-apps/api`, runtime, Wry, Tao, bundler, macros, and every official or third-party plugin.
2. Do not force artificial version equality across independently released components. Instead verify their documented compatibility and the actual generated/runtime behavior.
3. Record Rust toolchain and MSRV, Cargo features, frontend package manager, generated schemas, target triples, mobile overlays if present, and platform-specific plugin support.
4. Identify the system WebView implementation and minimum supported version on each target: WebView2, WKWebView/WebKit, WebKitGTK, or mobile WebView. Test behavior on the oldest supported environment.
5. Verify whether WebView2 is evergreen, fixed, embedded, offline-installed, store-provided, or assumed present. Include installer and enterprise-offline behavior.
6. Review Tauri release notes, breaking changes, plugin changelogs, generated ACL schemas, and platform limitations for the resolved versions.
7. Inventory third-party plugins and forks. Review their Rust core, guest JavaScript, permissions, scopes, build scripts, native code, release process, and maintenance state.
8. Define an upgrade cadence that covers core, CLI, JS API, plugins, Rust, system WebView requirements, installer tooling, and OS support.

### 12.2 Capabilities, Permissions, Scopes, And Runtime Authority

1. Inventory every capability file, inline capability, permission definition, scope, deny rule, target platform, remote URL pattern, window label, and webview label.
2. Build an effective permission matrix after all capabilities are merged. Windows or webviews referenced by multiple capabilities receive the union of their permissions.
3. Use stable, unique window/webview labels and verify that dynamic creation cannot accidentally match or inherit a broader capability.
4. Default-deny privileged commands. Grant only the exact commands and scopes required for a specific window, webview, origin, role, and platform.
5. Review `remote` capability grants with extreme caution. A remote origin receiving local-system access must be justified against XSS, account compromise, DNS/CDN compromise, and content takeover.
6. Use deny permissions where they provide defense in depth, but understand the final merge and precedence behavior for the resolved version.
7. Verify custom scopes are actually enforced by the command or plugin implementation. Configuration alone does not enforce an application-defined scope.
8. Review generated permission schemas and plugin permission files for the exact dependency version. Do not copy identifiers from unrelated versions.
9. Verify command registration and generated app manifests. Commands registered through broad invoke handlers must still be constrained by capabilities and in-command authorization.
10. Test each privileged command from allowed and denied windows, allowed and denied origins, subframes, dynamically created webviews, stale windows, and renamed labels.
11. Document every capability without a clear owner, purpose, test, and removal condition.
12. Treat Runtime Authority as one layer in the authorization chain, not a substitute for business authorization, path validation, account ownership, or destructive-action confirmation.

### 12.3 Commands, Invoke, Events, Channels, And Managed State

1. Inventory every Tauri command, invoke handler, plugin command, event, channel, global listener, window listener, menu/tray action, and Rust-to-frontend message.
2. Define strict request and response types. Reject ambiguous untagged enums, unbounded collections, deeply nested data, oversized strings/binaries, unknown fields where dangerous, and lossy numeric conversions.
3. Authorize inside the command using caller window/webview/origin, account, role, resource ownership, current application state, and operation intent.
4. Validate and canonicalize all paths, URLs, command names, device identifiers, database keys, and external-service identifiers before use.
5. Do not expose generic filesystem, shell, process, SQL, HTTP, plugin, or command dispatchers to the frontend unless they have a narrowly scoped, formally reviewed policy.
6. Bound command concurrency, duration, memory, output, channel rate, event fan-out, listener count, and queue depth. Support cancellation where safe.
7. Use managed state with explicit synchronization and ownership. Audit mutex/RwLock selection, lock ordering, blocking in async contexts, poisoning, reentrancy, and shutdown behavior.
8. Do not hold locks across await, IPC callbacks, filesystem/network operations, or frontend events without a proven design.
9. Make destructive and externally visible commands idempotent or protected against duplicate invoke, double click, event replay, renderer reload, and process restart.
10. Define stable error codes and redacted messages. Convert panics and library errors into controlled failures at the boundary.
11. Remove listeners and close channels when windows are destroyed, navigated, logged out, or replaced. Prevent stale messages from reaching a new account context.
12. Test malformed serialization, unknown commands, denied capability, invalid scope, stale caller, duplicate call, concurrent call, cancellation, panic, and shutdown.

### 12.4 Official And Third-Party Plugins

1. Create a plugin matrix: purpose, version, frontend API, Rust crate, supported platforms, permissions, scopes, native dependencies, storage, network access, update owner, and tests.
2. Review default permission sets before using them. A convenient `plugin:default` grant may include more commands than the window requires.
3. Prefer individual allow permissions and narrow scopes for filesystem, shell, process, opener, HTTP, SQL, store, clipboard, notification, dialog, deep link, single instance, global shortcut, autostart, and updater functionality.
4. Review plugin-generated permissions and application-added extensions. Ensure custom scope types are parsed and enforced consistently.
5. Audit plugin initialization order, managed state, background threads, event listeners, migration behavior, cleanup, and error handling.
6. Verify path variables and scope expansion against platform-specific directories, symlinks, junctions, Unicode, case sensitivity, removable media, and network shares.
7. Check whether a plugin exposes dangerous frontend commands by default or only after capability grants. Test the actual resolved version.
8. Treat unofficial plugins and forks as application code: inspect source, release provenance, maintainers, advisories, build scripts, native code, and incident response.
9. Remove unused plugins and Cargo features from the final binary and capabilities.
10. Test plugin behavior on unsupported or partially supported platforms and ensure the UI does not offer nonfunctional or unsafe operations.

### 12.5 Filesystem, Shell, Opener, Process, And Sidecars

1. Restrict filesystem access by command and canonical scope. Distinguish user-selected files from application-controlled paths and broad directory grants.
2. Prevent traversal and escape through symlinks, junctions, aliases, hard links, UNC/device paths, case changes, Unicode normalization, alternate data streams, and race conditions between check and use.
3. Use secure create/write/replace patterns, temporary-file permissions, atomic rename where supported, fsync requirements, conflict handling, and recovery from partial writes.
4. Never expose arbitrary shell strings. Use allowlisted programs or bundled sidecars, structured arguments, no shell interpretation, explicit environment, explicit working directory, and bounded output.
5. Verify sidecar path resolution, bundled target-triple naming, executable permissions, signature/hash, version handshake, update coupling, and writable-path hijacking.
6. Authenticate local communication with sidecars or services. Use protected sockets/pipes, random secrets or OS credentials, peer verification, and narrow access control.
7. Validate URLs and schemes passed to opener APIs. Separate opening HTTPS documentation from invoking arbitrary application protocols.
8. Define child-process timeout, cancellation, graceful stop, forced termination, descendant cleanup, output backpressure, crash retry, and quarantine behavior.
9. Audit elevation and administrator/root helpers. Use platform-approved privilege separation and authenticate requests; never run the entire UI privileged for convenience.
10. Test malicious filenames, executable substitution, argument injection, environment injection, local impersonation, sidecar version mismatch, partial output, hang, crash, and application shutdown.

### 12.6 Asset Protocol, CSP, Isolation, And Remote Content

1. Inventory asset/custom protocol configuration, allowed paths, scope, CSP, dev URL, frontend distribution directory, remote URLs, and any asset conversion helpers.
2. Verify the production build cannot load a development server or untrusted URL because of environment drift or fallback behavior.
3. Use restrictive CSP and isolation settings supported by the resolved Tauri/WebView version. Test on each system WebView because enforcement and feature support can differ.
4. Treat `convertFileSrc` and asset protocol access as privileged file disclosure. Restrict which files and directories can be converted and rendered.
5. Do not grant remote URLs capabilities unless the complete compromise scenario is accepted and mitigated. Prefer a privilege-free remote webview or system browser.
6. Verify navigation, popup, download, external-open, clipboard, media, permission, and devtools behavior in every webview.
7. Audit frontend dependencies and XSS sinks with the same rigor as Electron; a smaller native core does not make compromised web content harmless when commands are exposed.
8. Test malformed asset URLs, encoded traversal, local-file probing, remote redirects, compromised frontend bundle, CSP bypass attempts, and stale capability assignment.

### 12.7 Unsafe Rust, FFI, Mobile Overlay, And Platform Code

1. Review every `unsafe` block with documented invariants, ownership, lifetime, thread, alignment, aliasing, initialization, and error assumptions.
2. Audit FFI boundaries for ABI, struct layout, string encoding, buffer length, callback lifetime, exception/panic crossing, cancellation, and library version mismatch.
3. Verify platform modules and conditional compilation produce equivalent security decisions; absent code on one target must not silently broaden behavior.
4. Inspect Objective-C/Swift, C/C++, Java/Kotlin, PowerShell, shell, and installer custom actions with the same finding discipline as Rust and TypeScript.
5. If mobile targets exist, audit generated Android/iOS projects, permissions, intents/URL schemes, WebView settings, signing, stores, background behavior, and plugin hooks separately.
6. Test native-library absence, wrong architecture, signature failure, denied permission, OS API deprecation, callback after shutdown, and malformed native data.
7. Use sanitizers, Miri, fuzzing, clippy, compiler warnings, and platform diagnostics where applicable, but correlate findings with shipped code and runtime reachability.
8. Do not rewrite safe working code into `unsafe` or custom FFI merely for performance without measurement and a maintained test strategy.

