## 19. EAS Update And OTA Compatibility

### 19.1 Runtime Compatibility Contract
- Treat the native binary and JavaScript update as independently deployed artifacts joined only by an explicit runtime compatibility contract.
- Inventory runtimeVersion policy, native fingerprint inputs, update URL, request headers, channel, branch, platform, architecture, environment, and embedded update.
- Change runtime compatibility whenever native code, native configuration, Hermes compatibility, Codegen schema, native dependency, local schema, or privileged capability requires it.
- Test new update on every compatible native binary still in the field and prove incompatible binaries cannot receive it.
- Test old embedded update, latest update, rollback update, offline launch, failed download, corrupted asset, low storage, and repeated crash recovery.
- Do not use an OTA update for native breaking changes, signing changes, entitlement changes, permission declarations, store-policy changes, or irreversible data migration.

### 19.2 OTA Trust, Rollout, And Recovery
- Verify update manifest and asset authenticity, code-signing certificate configuration, private-key custody, key ID, rotation, revocation, and offline verification.
- Map channels to branches and environments explicitly; prevent preview, staging, test, tenant, or white-label updates from reaching production binaries.
- Use staged rollout with cohort size, guardrails, crash thresholds, launch thresholds, business metrics, pause, abort, and rollback authority.
- Retain update ID, group, channel, branch, runtimeVersion, commit, message, signer, manifest, assets, source maps, publication actor, and rollout history.
- Define automatic recovery from crash loops and prove fallback cannot reopen a data format that the failed update changed incompatibly.
- Exercise rollback, republish, channel remap, update disablement, emergency native release, and forward-fix procedures.

