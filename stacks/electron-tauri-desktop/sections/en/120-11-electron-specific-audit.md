## 11. Electron-Specific Audit

### 11.1 Framework, Embedded Runtimes, And Upgrade State

1. Resolve the exact Electron version from the lockfile and packaged binary, not only `package.json`. Record embedded Chromium, Node.js, V8, and relevant ABI.
2. Determine whether the major is within the current supported-major window and whether a newer stable patch fixes security or correctness issues.
3. Review Electron breaking changes major by major. Do not jump multiple majors without intermediate compatibility evidence and native-module verification.
4. Inventory Electron Forge, Electron Builder, Packager, Rebuild, Fuses, notarization, signing, and updater package versions independently.
5. Verify native modules against the actual Electron ABI and every supported OS/architecture. Rebuild, prebuild, fallback compilation, and runtime loading must be tested.
6. Detect unsupported or private Electron APIs, command-line switches, Chromium flags, monkey patches, remote module replacements, and assumptions about process internals.
7. Verify minimum OS support and embedded runtime behavior against the product's declared support matrix.
8. Document the patch and major upgrade cadence, security response owner, testing window, and emergency release path.

### 11.2 Application Lifecycle And Single-Instance Behavior

1. Map execution before and after `app.whenReady()`, single-instance lock acquisition, second-instance arguments, open-file/open-url events, activate, window-all-closed, before-quit, will-quit, quit, and crash/relaunch paths.
2. Validate command-line arguments and deep-link payloads received by the first instance. Do not trust the second process merely because it is the same application.
3. Test startup with corrupted preferences, locked profile, read-only data directory, missing resources, unavailable network, slow keychain, failed migrations, and incomplete update.
4. Define behavior when all windows close on each platform, when the tray remains active, and when the OS requests logout or shutdown.
5. Prevent duplicate background jobs, updater checks, local servers, migrations, device sessions, or file processing across multiple instances.
6. Verify orderly teardown of sessions, sockets, file handles, workers, utility processes, child processes, crash reporters, and telemetry.
7. Test app relaunch, update restart, crash restart, safe mode, recovery mode, and no-window background mode.
8. Ensure fatal startup failures produce actionable diagnostics without leaking secrets and without entering an infinite restart loop.

### 11.3 BrowserWindow, WebContentsView, And WebPreferences

1. Inventory every `BrowserWindow`, `BaseWindow`, `WebContentsView`, offscreen renderer, hidden window, print window, auth window, splash screen, and temporary webContents.
2. Record effective `webPreferences` for each: `nodeIntegration`, `nodeIntegrationInWorker`, `nodeIntegrationInSubFrames`, `contextIsolation`, `sandbox`, `preload`, `webSecurity`, `allowRunningInsecureContent`, `experimentalFeatures`, `enableBlinkFeatures`, `webviewTag`, `partition`, `spellcheck`, and devtools policy.
3. Require `nodeIntegration: false`, `contextIsolation: true`, and sandboxing for untrusted or remote content unless a narrowly proven exception exists.
4. Treat any `sandbox: false`, `contextIsolation: false`, `webSecurity: false`, insecure content, unrestricted webview, or remote Node integration as high-priority evidence requiring reachability analysis.
5. Verify the preload path resolves to the intended packaged file and cannot be replaced through writable directories, environment manipulation, or untrusted navigation.
6. Separate sessions and storage partitions for content with different trust, account, privacy, or lifecycle requirements. Determine whether partitions are persistent.
7. Audit hidden windows and background webContents because they can retain privileges, cookies, microphones, cameras, timers, or IPC listeners after visible UI closes.
8. Ensure window options, content origin, preload, and privilege are bound together in one reviewed creation path rather than mutable across scattered code.

### 11.4 Preload And ContextBridge Surface

1. Inventory every preload file and every property exposed through `contextBridge`. Produce a typed bridge contract.
2. Expose narrow functions and immutable values, not raw `ipcRenderer`, EventEmitter, Electron modules, Node primitives, filesystem handles, shell execution, unrestricted URLs, callbacks with hidden authority, or generic `invoke(channel, payload)`.
3. Validate arguments on both renderer and privileged sides. Renderer validation improves UX but is not a security boundary.
4. Freeze or safely wrap exposed objects. Avoid leaking mutable privileged references, prototypes, Buffer instances, native handles, or objects with unexpected methods.
5. Define error contracts that do not expose stack traces, file paths, tokens, SQL, environment variables, or implementation details to untrusted content.
6. Remove stale listeners and subscriptions on navigation, reload, account switch, window close, and hot update. Bound listener count and message rate.
7. Verify preload behavior in sandboxed contexts and across subframes. Do not assume the main frame is the only caller.
8. Add contract tests that run malicious renderer code against every exposed method and verify denial, validation, authorization, and bounded failure.

### 11.5 IPC Authentication, Authorization, Validation, And Backpressure

1. Inventory every `ipcMain.handle`, `ipcMain.on`, `webContents.send`, MessagePort, postMessage, webview message, and reply path. Remove or reject unknown channels.
2. Validate the sender using the actual `webContents`, frame, origin, URL, session/partition, window ownership, lifecycle generation, and account context. A channel name is not authentication.
3. Perform resource-level authorization for every file, account, tenant, device, job, update, setting, and privileged action.
4. Use strict schemas with size, depth, count, string, path, enum, and binary limits. Reject extra fields where they create ambiguity.
5. Canonicalize paths and URLs before policy checks. Defend against traversal, symlink/junction escape, alternate data streams, UNC paths, device paths, case tricks, and encoded separators.
6. Make side effects idempotent where retries, duplicate clicks, renderer reload, duplicate messages, or process restart can repeat them.
7. Bound concurrent requests, queues, stream rates, payload sizes, response sizes, and execution time. Cancel work when the caller disappears where safe.
8. Do not send privileged results to a stale, navigated, destroyed, or reused webContents without revalidating its identity and account context.
9. Separate read, write, destructive, administrative, and update channels. Require additional confirmation or authorization for irreversible operations.
10. Log security-relevant decisions with correlation IDs and redaction, including denied sender, invalid schema, scope failure, duplicate request, and rate-limit events.
11. Test cross-window, subframe, navigated-frame, remote-origin, stale-renderer, destroyed-renderer, duplicate, replay, oversized, slow, and concurrent IPC scenarios.
12. Treat IPC as a local network API with an untrusted client whenever renderer compromise is in scope.

### 11.6 Sessions, Permissions, Downloads, And Protocols

1. Inventory all sessions and partitions. Configure permission request/check handlers for every session that can load remote or user-controlled content.
2. Default-deny camera, microphone, display capture, notifications, geolocation, MIDI, USB, serial, HID, Bluetooth, clipboard, and fullscreen permissions unless explicitly required.
3. Bind permission decisions to exact origin, frame, user action, account, device, and duration. Persist only where justified and revocable.
4. Audit cookies, proxy, cache, certificate verification, auth challenges, client certificates, service workers, extensions, and storage clearing per session.
5. Define download policy: allowed origins, MIME and extension checks, destination selection, overwrite behavior, quarantine/Mark-of-the-Web, malware scanning, partial files, cancellation, and opening behavior.
6. Implement custom protocols as privileged parsers: normalize paths, define standard/secure/cors/fetch/stream privileges deliberately, constrain methods and origins, and prevent traversal.
7. Avoid `file://` for privileged app content where a secure custom protocol provides a clearer origin and policy model.
8. Test certificate errors, captive portals, proxy auth, offline mode, redirects, malicious filenames, archive bombs, partial downloads, and download-to-execute chains.

### 11.7 Navigation, New Windows, External Open, And Webviews

1. Use `will-navigate`, redirect handling, and window-open handlers to enforce exact navigation and popup policy.
2. Validate every URL passed to `shell.openExternal` or OS launch APIs. Allow only required schemes and hosts; reject local files, executable protocols, script schemes, malformed URLs, and arbitrary custom protocols.
3. Do not use `<webview>` unless its isolation and lifecycle benefits outweigh its attack surface. Prefer `WebContentsView` or system browser where appropriate.
4. If `<webview>` exists, validate `will-attach-webview` options and source, remove dangerous preload and permissions, reject `allowpopups`, and isolate partitions.
5. Verify OAuth, payment, help, documentation, support, and third-party content flows under redirects and compromised content conditions.
6. Prevent untrusted content from controlling window features, preload selection, partition, sandbox, devtools, download location, or external applications.
7. Audit drag-and-drop and link handling for local-file disclosure and command/protocol execution.
8. Test nested frames, dynamically created webviews, same-origin changes, history navigation, server redirects, and post-authentication navigation.

### 11.8 Fuses, ASAR Integrity, And Executable Hardening

1. Inspect fuses in the actual packaged executable. Do not rely only on Forge or build configuration.
2. Evaluate fuses such as disabling `RunAsNode`, disabling `NODE_OPTIONS` and `NODE_EXTRA_CA_CERTS` influence where appropriate, disabling inspection arguments, enforcing ASAR app loading, and enabling embedded ASAR integrity validation.
3. Flip fuses after packaging and before code signing, then verify the final signed binary. Record the exact fuse tool version and options.
4. Understand the compatibility impact before disabling behavior; test CLI integrations, child processes, debugging, enterprise certificates, and native modules.
5. Enable ASAR integrity only with the complete required fuse combination and packaging flow. Verify that modified archives fail as expected.
6. Keep executable code out of writable unpacked resources. Justify every `asarUnpack` path and protect its load path.
7. Verify signature and ASAR integrity behavior after installer installation, delta update, full update, repair, and rollback.
8. Treat fuses and ASAR as defense in depth, not a replacement for secure renderer isolation, IPC authorization, signing, and update trust.

### 11.9 Utility Processes, Workers, Extensions, And Native Modules

1. Prefer utility processes over ad hoc Node child processes when Electron lifecycle, sandboxing, and MessagePort integration provide a safer fit; justify exceptions.
2. Inventory Node child processes, forked workers, worker threads, renderer workers, service workers, GPU tasks, extension processes, and native helper processes.
3. Validate child executable and argument construction; avoid shell interpretation; use explicit environment allowlists and working directories.
4. Bound process count, CPU, memory, file descriptors, output buffers, restart frequency, and queue depth. Prevent crash loops and fork bombs.
5. Authenticate local IPC to helpers and prevent another local process from impersonating the app or connecting to privileged sockets/pipes.
6. Verify native module loading paths, signatures where available, ABI compatibility, DLL search order, rpath, library search paths, and writable-directory hijacking.
7. Disable or strictly control Chrome extensions, devtools extensions, remote debugging, inspect ports, and automation interfaces in production.
8. Test helper crash, hang, malformed output, oversized output, partial protocol messages, version mismatch, update overlap, and application shutdown.

