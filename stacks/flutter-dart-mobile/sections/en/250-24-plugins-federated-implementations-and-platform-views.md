## 24. Plugins, Federated Implementations, And Platform Views

A plugin is a distributed contract across Dart API, platform interface, platform implementation, native dependencies, permissions, and lifecycle.

- Map each plugin to supported platforms, selected implementation, transitive native dependencies, permissions, manifests, entitlements, and runtime behavior.
- Verify federated plugin registration, default implementation, endorsed packages, manual overrides, missing implementations, web registration, and desktop registration.
- Review plugin API contracts for nullability, errors, cancellation, threading, lifecycle, multiple engines, multiple windows, background execution, and hot restart assumptions.
- Audit platform views for composition mode, z-order, clipping, transforms, accessibility, focus, input, screenshots, secure content, performance, and lifecycle.
- Test permission denial, limited permission, revoked permission, unsupported device, missing service, old OS, no hardware, and plugin initialization failure.
- Inspect maintained status, issue backlog, security advisories, release cadence, platform implementation quality, test depth, and replacement options.
- Fork only with explicit ownership, patch tracking, upstream strategy, security response, release automation, and eventual exit criteria.
- Require contract tests for every platform implementation and shared behavior that the application depends on.

