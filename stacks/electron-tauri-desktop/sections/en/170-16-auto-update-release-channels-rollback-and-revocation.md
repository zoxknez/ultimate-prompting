## 16. Auto-Update, Release Channels, Rollback, And Revocation

### 16.1 Common Update Trust Model

1. Map who can build, sign, publish, modify metadata, change endpoints, promote channels, trigger rollout, pause rollout, force update, permit downgrade, and revoke a release.
2. Separate artifact identity, transport security, metadata authenticity, artifact signature, platform code signature, channel policy, and installer authorization. Each solves a different problem.
3. Use immutable versioned artifacts. Never replace bytes at an existing version URL after release.
4. Bind metadata to exact product, channel, platform, architecture, version, minimum/current version rules, artifact hash or signature, size, publication time, and rollout policy.
5. Validate update metadata as untrusted network input. Bound size and fields, reject unknown platform mappings where dangerous, and handle clock skew.
6. Prevent downgrade and cross-channel confusion by default. If controlled rollback requires downgrade, define explicit authorization, compatibility checks, user-data migration behavior, and re-upgrade.
7. Use staged rollout with telemetry, minimum sample, soak period, crash/startup/update/error thresholds, manual pause, automatic abort, and owner.
8. Define behavior for offline users, skipped versions, very old clients, unsupported OS, unsupported architecture, proxy/captive portal, metered network, low disk, and interrupted download.
9. Verify full and differential update paths independently. A delta update must not bypass integrity, signing, or package-content checks.
10. Test update from every supported source version to the candidate, not only candidate-to-candidate or clean install.
11. Define rollback for application code, local data/schema, sidecars/services, protocols, file associations, configuration, and cached frontend state.
12. Maintain a kill switch or channel disable mechanism that does not itself create an unauthenticated remote-control path.
13. Define certificate/key compromise response: freeze publishing, revoke or remove trust, rotate keys where architecture permits, issue a trusted replacement, and communicate recovery.
14. Preserve update logs and artifacts needed for incident investigation without recording secrets.

### 16.2 Electron Updater Audit

1. Identify the updater implementation: built-in `autoUpdater`, `update-electron-app`, Electron Forge publisher/update service, Electron Builder updater, custom updater, store updater, or external enterprise tool.
2. Verify platform and package support for the exact updater. Built-in behavior differs among macOS, Squirrel.Windows, MSIX, and Linux packaging; do not assume one API provides identical cross-platform semantics.
3. On macOS, verify code signing, notarization where required, application identity, feed format, signature behavior, and hardened runtime/entitlements compatibility.
4. On Windows, verify Squirrel/MSIX/NSIS/custom installer behavior, application user model ID, per-user/per-machine scope, update locks, running instances, and repair/uninstall interaction.
5. Guard against duplicate update checks and downloads. Ensure UI actions, timers, startup checks, reconnect, and multiple windows cannot start competing updates.
6. Validate feed URL and channel selection. Prevent renderer-controlled arbitrary feed URLs or release channels unless strictly authorized.
7. Verify `checkForUpdates`, download, cancellation, progress, ready state, quit-and-install, restart, and error transitions as one explicit state machine.
8. Do not install while critical writes, migrations, exports, recordings, device operations, or irreversible jobs are active unless the operation can resume safely.
9. Verify code-signature checks and package verification on the final distribution path. Test modified metadata, modified package, wrong publisher, wrong channel, wrong architecture, and expired/revoked certificate conditions.
10. Test fresh install, normal update, skipped versions, very old client, update while app is running in tray, multiple instances, interrupted download, low disk, locked file, antivirus interference, and forced shutdown.

### 16.3 Tauri Updater Audit

1. Resolve the exact updater plugin version, Rust and JavaScript API versions, capabilities, permissions, public key, endpoint configuration, install mode, and platform support.
2. Verify that update signatures are mandatory and checked against the intended pinned public key. Protect the private signing key separately from platform code-signing keys.
3. Restrict frontend updater permissions. A window that may check availability does not automatically need download or install authority.
4. Validate static JSON or dynamic server metadata, including RFC 3339 date if used, semantic version, platform key, architecture, signature contents, URL, size, and release notes.
5. Verify runtime endpoint and header overrides cannot be influenced by untrusted renderer content or lower-trust configuration.
6. Test Windows install modes, elevation prompts, restart behavior, running sidecars/services, and per-user/per-machine consistency.
7. Test Linux package-specific behavior instead of treating AppImage, Debian, RPM, Flatpak, Snap, and distribution repositories as interchangeable.
8. Test macOS app bundle identity, signing, notarization, quarantine, update replacement, and rollback behavior.
9. If custom version comparison permits rollback, require an authenticated rollback decision, data compatibility gate, explicit telemetry, and a plan to return users to a safe forward version.
10. Test bad signature, missing signature, wrong key, modified package, wrong OS/architecture key, server error, partial download, low disk, denied permission, interrupted installation, and old client.

