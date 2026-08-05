## 10. Hermes, Metro, Bundles, And Source Maps

### 10.1 Hermes Runtime
- Confirm the Hermes version bundled with the actual React Native release and artifact; do not manage it as an unrelated version by assumption.
- Compare debug, development, profile, and release behavior for bytecode, optimization, debugger, exception handling, startup, memory, and native integration.
- Inspect synchronous native calls, large object graphs, serialization, repeated global retention, and long JS tasks.
- Verify crash and error symbolication with matching JavaScript bundle, Hermes source map, native symbols, update ID, and release identity.
- Test cold launch, warm launch, reload, OTA launch, offline launch, low-memory state, and repeated navigation in release mode.
- Treat engine migration or bytecode-affecting change as a native runtime compatibility event.

### 10.2 Metro And Bundle Boundaries
- Audit resolver configuration, monorepo watch folders, symlink handling, platform extensions, package exports, aliases, transformers, and serializer hooks.
- Detect duplicate React, React Native, native-module wrapper, state-library, or singleton copies caused by workspaces or resolver drift.
- Inspect bundle content for secrets, private endpoints, internal feature flags, debug code, source paths, test fixtures, credentials, and unnecessary assets.
- Measure bundle size, module count, lazy loading, route splitting where supported, startup imports, and asset duplication.
- Prove minification, dead-code elimination, environment replacement, source-map retention, and release-only code paths.
- Retain a manifest that maps release and update identities to exact bundles, source maps, assets, and native binaries.

