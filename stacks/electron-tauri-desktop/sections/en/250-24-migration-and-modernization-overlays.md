## 24. Migration And Modernization Overlays

### 24.1 Electron Major Upgrade

1. Upgrade one supported major at a time unless authoritative evidence and tests justify another path.
2. Review breaking changes, removed defaults/APIs, Chromium behavior, Node/V8 changes, sandbox/context isolation, protocol/session changes, and packaging/updater compatibility.
3. Rebuild and test every native module and sidecar on every target. Verify ABI, prebuild availability, fallback compiler, and runtime loading.
4. Compare package content, fuses, signatures, permissions, startup, memory, CPU, rendering, media, printing, accessibility, and installer/update behavior.
5. Run old-version to new-version update and rollback/data-compatibility tests before broad rollout.
6. Do not use the upgrade to mix unrelated architecture rewrites unless separately scoped and reversible.

### 24.2 Tauri 1 To 2 Or Major Plugin Migration

1. Inventory removed/renamed APIs, plugin extraction, capability/permission model, generated configuration, command registration, frontend API, mobile changes, and bundler differences.
2. Translate allowlists into least-privilege capabilities instead of granting broad defaults to restore functionality.
3. Review each plugin's v2 permissions, scopes, platform support, data migration, and update behavior independently.
4. Diff generated schemas, capabilities, manifests, entitlements, installers, and package contents before and after migration.
5. Test all commands from allowed and denied windows/origins, because a build passing does not prove capability correctness.
6. Verify updater signing keys, metadata, package formats, source-version compatibility, rollback, and user-data paths.
7. Audit Rust async/state/unsafe changes and system WebView requirements on minimum supported platforms.
8. Keep a reversible branch/artifact/data migration path until production evidence is sufficient.

### 24.3 Electron To Tauri Or Tauri To Electron Migration

1. Start from required capabilities, platform support, WebView/runtime behavior, native integrations, updater, installer, accessibility, enterprise constraints, and total maintenance cost, not binary-size marketing.
2. Map every existing privilege and IPC/command contract. Redesign least privilege rather than mechanically recreating a broad bridge.
3. Prototype the highest-risk flows first: remote content, auth, files, native modules, sidecars, devices, media, printing, updater, signing, stores, and enterprise deployment.
4. Define data-path, secure-storage, bundle identity, protocol/file association, signing identity, channel, installer, and update continuity.
5. Test UI/rendering and Web API differences across Chromium and system WebViews, including oldest supported OS versions.
6. Plan coexistence, migration, rollback, telemetry comparison, user communication, and support for users who cannot migrate.
7. Do not declare success from feature parity alone; require operational, security, update, accessibility, and recovery parity.
8. Keep the old production path recoverable until adoption and stability gates are met.

