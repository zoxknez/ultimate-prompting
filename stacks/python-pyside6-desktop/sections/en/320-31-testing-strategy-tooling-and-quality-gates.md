## 31. Testing Strategy, Tooling, And Quality Gates

### 31.1 Audit Scope

1. Inventory unit, property, contract, integration, model/view, signal/thread, GUI, end-to-end, package, installer, update, performance, accessibility, security, and recovery tests.
2. Review pytest configuration, markers, fixtures, isolation, temporary paths, event-loop integration, Qt bot tooling, timeouts, retries, parallelism, randomness, and flaky-test policy.
3. Map mocks, fakes, emulators, local services, databases, devices, network proxies, clocks, keyrings, update feeds, and platform VMs to production behavior.
4. Identify untested entrypoints, generated code, packaging hooks, frozen-only paths, installer custom actions, update logic, native extensions, and crash recovery.
5. Define supported platform, architecture, Python, Qt, graphics backend, locale, account, data-version, and upgrade matrices.
6. Separate fast presubmit gates from scheduled, release, destructive, hardware, store, and disaster-recovery suites.

### 31.2 Required Verification

1. Run deterministic focused tests for each finding and then the widest applicable clean, packaged, installed, and runtime matrix.
2. Use race/stress repetition, fault injection, network shaping, disk and memory pressure, malicious corpora, and kill/restart testing for critical paths.
3. Capture exact command, environment, versions, platform, exit code, duration, logs, artifacts, and conclusion for every claimed test.
4. Quarantine flaky tests only with owner, evidence, expiry, and replacement plan; do not treat retries as proof of correctness.
5. Block release when critical matrices are skipped without a documented evidence ceiling, owner, and acceptance plan.

