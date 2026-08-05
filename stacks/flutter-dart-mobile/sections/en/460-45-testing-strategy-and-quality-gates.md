## 45. Testing Strategy And Quality Gates

Use layered tests tied to risks, contracts, platforms, and release artifacts.

- Unit-test domain invariants, parsing, serialization, error mapping, state transitions, conflict policy, retry policy, authorization decisions, and migrations.
- Widget-test semantics, layout constraints, forms, validation, loading/error/empty states, focus, keyboard, text scale, RTL, restoration, and interaction races.
- Golden-test stable visual contracts with controlled fonts, locales, device sizes, pixel ratios, themes, and justified tolerances; do not hide real regressions with broad thresholds.
- Integration-test critical journeys on real or production-equivalent platform targets with realistic backend, lifecycle, permission, network, storage, and update conditions.
- Contract-test backend APIs, platform channels, Pigeon APIs, plugins, generated clients, database schemas, deep links, notifications, and old/new version overlap.
- Property/fuzz-test parsers, serializers, URL/path handling, file formats, archive handling, native boundaries, state machines, and conflict resolution where valuable.
- Performance-test startup, frame pacing, memory, CPU, battery, network, disk, size, background work, realtime, large data, burst, and soak scenarios.
- Security-test auth, BOLA/IDOR, tenant isolation, storage leakage, WebView bridges, deep links, notifications, file parsing, network failures, update integrity, and signing continuity.
- Artifact-test final release packages: identity, version, signatures, permissions, entitlements, native libraries, assets, symbols, source maps, install, launch, update, and uninstall.
- Quarantine only proven flaky tests with owner, reason, expiry, telemetry, and replacement plan; never normalize silent retries or permanently skipped platform tests.

