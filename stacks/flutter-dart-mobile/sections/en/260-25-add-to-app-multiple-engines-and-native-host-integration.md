## 25. Add-To-App, Multiple Engines, And Native Host Integration

Mixed Flutter/native products need explicit ownership and compatibility contracts.

- Inventory native host applications, Flutter modules, engine groups, cached engines, routes, entrypoints, plugin registration, and lifecycle ownership.
- Verify native and Flutter navigation, authentication, account/tenant state, analytics, accessibility, theme, locale, and error semantics remain consistent.
- Audit engine creation/destruction, retained engines, memory, plugin singleton assumptions, channel collisions, multiple view controllers/activities, and background callbacks.
- Version the boundary between host and module, including routes, arguments, results, events, shared storage, tokens, and rollout compatibility.
- Verify build, packaging, symbols, signing, crash reporting, and release ownership for the combined artifact.
- Test old host/new module and new host/old module combinations where independent rollout or caching can occur.
- Ensure native screens cannot bypass Flutter-side authorization and Flutter screens cannot assume native UI checks are authoritative.
- Document rollback and emergency disable behavior if the Flutter module or native host becomes incompatible.

