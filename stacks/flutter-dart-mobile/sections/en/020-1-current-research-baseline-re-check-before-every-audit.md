## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline reflects primary-source information available on 5 August 2026. It is a starting point only. Re-check current stable releases, support policies, platform requirements, breaking changes, security advisories, store rules, and the project-resolved toolchain before every recommendation or modification.

| Area | Baseline on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Flutter stable | Flutter 3.44.8 with Dart 3.12.2, released 23 July 2026. | Exact SDK hash and channel in local, CI, build, and release environments; current stable patch and support status. |
| Flutter prerelease | Flutter 3.47 is a beta line and is not the default production baseline. | Whether any beta/dev SDK or experimental feature is used, why it is required, and how rollback is proven. |
| Supported platforms | Flutter publishes separate deployment support matrices for Android, iOS, web, Windows, macOS, and Linux. | Project minimums, target OS/browser versions, architecture matrix, plugin support, store rules, and real device coverage. |
| Architecture | Current Flutter guidance favors explicit UI/data layers, repositories, immutable models, unidirectional data flow, and testable dependency boundaries when appropriate. | Whether the chosen architecture actually preserves domain invariants, ownership, cancellation, testability, and platform independence. |
| Web rendering | Flutter web supports JavaScript and WebAssembly build modes with renderer and browser constraints. Threaded Wasm can require cross-origin isolation headers. | Actual build mode, browser matrix, COOP/COEP, CSP, caching, service worker behavior, source maps, and fallback path. |
| iOS lifecycle | Modern Flutter iOS projects use UIScene-based lifecycle behavior; migration and plugin compatibility must be verified. | Scene configuration, deep links, state restoration, notifications, background modes, add-to-app hosts, and plugin callbacks. |
| Security and supply chain | Framework defaults do not replace application authorization, secret handling, dependency review, platform hardening, or signed release verification. | Resolved packages, advisories, native code, generated code, signing identities, artifact provenance, and runtime permission boundaries. |

