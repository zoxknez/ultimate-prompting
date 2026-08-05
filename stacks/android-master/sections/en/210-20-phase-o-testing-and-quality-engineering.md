## 20. Phase O - Testing And Quality Engineering

### 20.1 Test Strategy And Determinism

1. Map unit, integration, component, UI, screenshot, instrumented, end-to-end, migration, benchmark, fuzz, security, and device tests.
2. Tie tests to risks and critical journeys, not only code coverage.
3. Verify deterministic time, dispatchers, randomness, network, database, locale, timezone, and device state.
4. Eliminate flaky sleeps and uncontrolled external dependencies.
5. Verify fakes preserve the semantics required by the test and do not hide concurrency or persistence bugs.
6. Separate hermetic tests from environment-dependent tests.
7. Record retries as flakiness evidence, not as proof of stability.
8. Every P0-P2 repair should receive a regression test where technically feasible.

### 20.2 Unit, Coroutine, Flow And Data Tests

1. Test reducers, state holders, ViewModels, use cases, repositories, parsers, validators, serializers, auth, retry, and conflict logic.
2. Test success, empty, boundary, invalid, timeout, cancellation, duplicate, out-of-order, partial, and recovery cases.
3. Use coroutine test APIs and virtual time correctly.
4. Verify hot and cold Flow behavior, replay, sharing, cancellation, completion, and errors.
5. Test Room queries, constraints, transactions, migrations, and concurrency.
6. Test network error mapping, schema drift, malformed payloads, and idempotency.
7. Verify tests fail for the original defect before the fix when practical.

### 20.3 Compose UI, View And Instrumented Tests

1. Test semantics and user-visible behavior, not implementation details alone.
2. Control clocks, idling, animations, background work, network, permissions, and test data.
3. Test navigation, back, restoration, deep links, process recreation, rotation, locale, font scale, and window size.
4. Test View and Compose interoperability and lifecycle boundaries.
5. Verify screenshot tests have stable rendering conditions and reviewed baselines.
6. Run release-like or minified instrumented smoke tests where critical reflection or R8 behavior exists.
7. Test on physical devices when hardware, codecs, DRM, Bluetooth, camera, TV remote, OEM behavior, or thermal state matters.

### 20.4 Macrobenchmark, Baseline Profiles And Device Matrix

1. Create Macrobenchmarks for startup, scroll, navigation, playback, and other critical journeys.
2. Generate app-specific Baseline Profiles and verify they are merged and shipped.
3. Benchmark release or benchmark variants with representative data.
4. Define a device matrix across minimum SDK, target behavior, current stable Android, representative OEMs, low RAM, tablet, foldable, TV, 16 KB, and relevant ABIs.
5. Include offline, slow network, low storage, battery saver, dark theme, locale, font scale, and permission states.
6. Record device-lab configuration and avoid averaging away severe device-specific failures.

