## 25. Packaging, Bundling, Installers, Signing, Updates, And Rollback

### 25.1 Audit Scope

1. Identify packaging tools, versions, spec/config files, hooks, hidden imports, exclusions, data files, Qt modules, plugin collection, native libraries, and runtime options.
2. Compare one-file, one-folder, app bundle, portable, installer, store, system-package, and enterprise deployment behavior where applicable.
3. Review bootloader/runtime trust, extraction directories, temporary execution, DLL/library search, resource integrity, antivirus interaction, and writable code paths.
4. Map code-signing identities, certificates, timestamp services, notarization, entitlements, package signing, key custody, approval, rotation, revocation, and loss recovery.
5. Document update metadata, transport, signature verification, channel, cohort, architecture/platform mapping, version ordering, downgrade policy, delta/full packages, install timing, and restart.
6. Define fresh install, upgrade, repair, interrupted install, interrupted update, rollback, forward repair, uninstall, data retention, and side-by-side channel behavior.

### 25.2 Required Verification

1. Build from a clean environment, inspect package manifests and binaries, and compare delivered files against an allowlisted bill of materials.
2. Install on clean machines as standard users and administrators; verify first run, permissions, shortcuts, associations, services, prerequisites, and uninstall.
3. Verify signatures and notarization after final packaging; prove that post-sign mutation or tampered update content is rejected.
4. Test update from every supported version/channel/architecture, offline interruption, disk full, process lock, antivirus delay, power loss, signature failure, and server rollback.
5. Prove recovery when an update starts but cannot complete, data schema advances, old binaries restart, signing keys are revoked, or the update service is compromised.

