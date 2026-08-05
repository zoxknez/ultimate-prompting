## 22. Testing And Verification Strategy

### 22.1 Test Pyramid And Contract Coverage
- Map domain unit tests, state tests, hook tests, component tests, navigation tests, integration tests, native tests, end-to-end tests, release tests, and recovery tests.
- Use Jest or the project runner for deterministic logic, React Native Testing Library for user-observable behavior, and native test frameworks for native code.
- Use Maestro, Detox, Appium, XCUITest, Espresso, or equivalent according to actual support and reliability; do not claim end-to-end coverage from mocks.
- Add contract tests for API schema, deep links, notifications, native modules, Codegen, storage migrations, update manifests, and background payloads.
- Test negative authorization, malformed inputs, duplicate actions, reordered events, partial failures, timeouts, process death, upgrade, rollback, and restore.
- Track skipped, flaky, quarantined, platform-excluded, and unrepresentative tests as explicit risk, not silent success.

### 22.2 Required Device And Release Matrix
- Include minimum, current, and latest supported OS versions where available, plus representative vendor, architecture, memory, screen, and performance classes.
- Include physical Android and Apple devices for native lifecycle, notifications, biometrics, background work, media, performance, signing, and update verification.
- Test debug, development, internal release, store release, embedded bundle, latest OTA, rollback OTA, offline, upgrade, and fresh-install paths.
- Include slow and unstable networks, captive portal, low storage, low memory, low battery, thermal pressure, denied permissions, and interrupted operations.
- Record exact device model, OS build, architecture, app version, runtimeVersion, update ID, channel, artifact digest, and test data.
- Do not generalize one matrix cell to all supported devices or channels without a documented rationale.

