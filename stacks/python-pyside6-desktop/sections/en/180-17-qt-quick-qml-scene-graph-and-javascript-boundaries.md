## 17. Qt Quick, QML, Scene Graph, And JavaScript Boundaries

### 17.1 Audit Scope

1. Inventory QML modules, engines, contexts, singletons, registered Python types, image providers, JavaScript, shaders, animations, loaders, and remote/local resource origins.
2. Review QML ownership modes, context-property lifetime, binding loops, signal handlers, dynamic object creation, loader destruction, and engine teardown.
3. Assess Python objects exposed to QML, invokable methods, properties, signals, input validation, authorization, thread affinity, and exception propagation.
4. Inspect scene-graph render-thread interactions, custom QQuickItem code, graphics resources, image decoding, shaders, and platform backend differences.
5. Review JavaScript `eval`, dynamic import, network-loaded QML, local file access, URL handling, and untrusted data reaching executable expressions.
6. Measure binding churn, overdraw, texture memory, animation cost, frame pacing, startup compilation, and QML cache behavior.

### 17.2 Required Verification

1. Run QML warnings as test failures for critical flows and inspect packaged import paths, plugins, cache, and missing-module behavior.
2. Test engine recreation, logout, theme/locale changes, dynamic page loading, object destruction, graphics-device reset, and application shutdown.
3. Fuzz or validate every Python-QML boundary with malformed, oversized, stale, unauthorized, and cross-tenant data where applicable.
4. Profile render and GUI threads on each supported graphics backend and realistic low-end hardware.
5. Ensure remote or user-controlled content cannot load QML, JavaScript, plugins, shaders, or local resources outside an explicit trust policy.

