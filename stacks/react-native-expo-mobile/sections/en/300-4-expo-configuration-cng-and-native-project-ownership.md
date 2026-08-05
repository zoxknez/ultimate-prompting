## 4. Expo Configuration, CNG, And Native Project Ownership

### 4.1 Effective Expo Configuration
- Resolve dynamic app configuration with the exact environment used by local, CI, EAS, preview, production, and store builds.
- Inspect public and private configuration boundaries and prove that no secret is embedded in the JavaScript bundle, manifest, resources, native strings, or OTA metadata.
- Compare introspected config, generated Android manifest, Gradle properties, Info.plist, entitlements, Podfile properties, URL schemes, and associated domains.
- Audit config-plugin ordering, idempotency, conflict resolution, dangerous mods, file ownership, conditional branches, and platform-specific behavior.
- Prove that repeated prebuild does not silently remove manual native changes, duplicate entries, reorder critical configuration, or change identifiers.
- Document the authoritative place for every native configuration value and the regeneration procedure.

### 4.2 Development Builds And Expo Go
- Inventory every native capability unavailable or behaviorally different in Expo Go.
- Use development builds for custom native code, config plugins, push credentials, background modes, universal links, app links, and production-like permissions.
- Separate development client menu, debugger, dev server, network security, and bundle loading behavior from release behavior.
- Verify offline launch and embedded bundle behavior without Metro or a reachable development machine.
- Do not close a native, update, signing, performance, memory, or lifecycle finding using Expo Go evidence alone.
- Retain the exact development-build profile and native fingerprint used for each reproduction.

