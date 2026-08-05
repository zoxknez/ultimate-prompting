## 46. Upgrade, Migration, And Compatibility Audit

Treat SDK, package, platform, architecture, data, and distribution upgrades as behavior migrations.

- Inventory current and target Flutter/Dart, package majors, native toolchains, platform SDKs, minimum OS/browser versions, renderers, storage schemas, and distribution formats.
- Read official breaking changes, migration guides, release notes, deprecations, store deadlines, plugin compatibility, and platform lifecycle changes.
- Build a compatibility matrix for old data, old cache, old server, new server, old client, new client, background jobs, deep links, notifications, and independently deployed components.
- Upgrade in bounded stages with clean build, generated diff review, contract tests, platform builds, artifact inspection, device/browser tests, performance comparison, and rollback after each stage.
- Use expand-and-contract for storage and API schema changes; avoid one-way destructive migration before old/new coexistence and recovery are proven.
- Verify signing identity, bundle/package ID, keychain/secure-storage accessibility, file paths, database location, store listing, update eligibility, and user-data continuity.
- Test interrupted upgrade, low disk, revoked permission, offline launch, restored old backup, downgrade attempt, rollback, and support handoff.
- Do not remove compatibility paths, legacy data, old API support, symbols, or rollback artifacts until telemetry and policy prove the deprecation window is complete.

