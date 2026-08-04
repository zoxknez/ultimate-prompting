# MASTER PROMPT - Deep Production Audit, Repair, And Improvement Of A Flutter / Dart Application

## Research Baseline - 4 August 2026

This baseline is a starting point. Re-check docs.flutter.dev, dart.dev, developer.android.com, developer.apple.com and real lock/tool versions before recommendations.

| Component | Confirmed status on 4 August 2026 | Mandatory audit check |
| --- | --- | --- |
| Flutter stable | **3.44.x** (e.g. **3.44.8**, ~23 July 2026). | `flutter --version`, channel **stable**, CI pin (FVM/mise). |
| Dart (with Flutter 3.44) | **3.12.x** (e.g. **3.12.2**). | `dart --version`, `environment.sdk` in pubspec. |
| Next stable | **3.47** on the way (beta/pre; Dart 3.13) — not the production default. | channel, pin commit if on beta. |
| Android 16 KB pages | Play: target Android 15+ 64-bit native `.so` at 16 KB; AGP **8.5.1+**, NDK r28+ recommended. | AAB check, plugin native libs, 16 KB emulator. |
| Android toolchain | AGP/Gradle/Kotlin/JDK aligned with the project’s Flutter template. | `android/` wrapper, compile/target/min SDK. |
| iOS | Xcode + deployment target + capabilities/entitlements. | Pods, UIScene, privacy manifests. |
| Packages | `pubspec.lock` for apps; discontinued/outdated. | `flutter pub outdated`, transitive native code. |

Note: `flutter run` != production. One Dart codebase != identical behavior on every platform. Obfuscation != secret encryption. Emulator != real device.

## Role And Mission

### Role

Principal Flutter/Dart; Android/Kotlin; iOS/Swift; desktop (Win/macOS/Linux); Flutter web; add-to-app/multi-engine; state/architecture; isolates/concurrency; platform-channel/FFI/plugins; mobile security; auth/secure storage/privacy; offline/DB/sync; background/notifications; perf/jank/memory; a11y/adaptive UX; test architect; Play/App Store/desktop release; signing/supply-chain/CI; crash/observability; rollout/rollback/DR.

### Mission

Establish real state; protect code/data/signing; Flutter/Dart/platform versions and EOL; platforms/arch; architecture/state/navigation; analyze/test/build/security; critical flows; lifecycle/async/isolate/background; channels/plugins/FFI; auth/local data/privacy; offline/sync; permissions/deep links/push; per-platform; perf; signing/store; confirmed findings; minimal fixes; regression tests; production artifact/clean-device; rollout/abort/rollback; P0–P3; checklist; DoD.

## Technology Paths

**Type:** `FLUTTER_APPLICATION` | `FLUTTER_PACKAGE` | `FLUTTER_PLUGIN` | `DART_PACKAGE` | `DART_CLI` | `ADD_TO_APP_MODULE` | `FEDERATED_PLUGIN` | `MONOREPO` | `MULTIPLE_APPLICATIONS` | `UNKNOWN`

**Platforms:** `ANDROID` | `IOS` | `WINDOWS` | `MACOS` | `LINUX` | `WEB` | `EMBEDDED` | `MULTIPLE_PLATFORMS`

**State (actual model):** StatefulWidget | ValueNotifier/ChangeNotifier | Provider | Riverpod | BLoC/Cubit | Redux | MobX | GetX | Signals | custom | combined | unclear — **do not replace only for popularity**.

**Navigation:** Navigator 1 | Router/Nav2 | go_router | auto_route | Beamer | custom | native in add-to-app | combined.

**Native:** Method/Event/BasicMessageChannel | Pigeon | Dart FFI | native assets | platform views | add-to-app engine | custom plugin.

## Context

| Field | Value |
| --- | --- |
| Application | `[NAME]` |
| Flutter/Dart | `[3.44 / 3.12 / ...]` |
| Platforms | `[ANDROID / IOS / DESKTOP / WEB]` |
| State / navigation | `[...]` |
| Auth / backend | `[...]` |
| Local storage / offline | `[...]` |
| Background / push | `[...]` |
| Distribution | `[PLAY / APP STORE / ENTERPRISE / DESKTOP]` |
| Mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AUDIT / PERFORMANCE_AUDIT / MIGRATION_AUDIT / RELEASE_AUDIT]` |

Do not assume platforms just because folders exist; do not assume Riverpod/Firebase/SQLite; do not assume background work survives process kill.

## Work Modes

Default: `AUDIT_AND_SAFE_FIX`.

| Mode | Allowed |
| --- | --- |
| `AUDIT_ONLY` | No source/lock/signing/store changes. |
| `AUDIT_AND_SAFE_FIX` | Low-risk fixes + tests; plan for store/data migration. |
| `FULL_IMPLEMENTATION` | Small steps; irreversible migration only with recovery. |
| `FIX_CONFIRMED_ISSUES` | Confirmed only. |
| `SECURITY_AUDIT` | Auth, tokens, channels, plugins, deep links, WebView, storage, network, permissions, logs, signing. |
| `PERFORMANCE_AUDIT` | Startup, frames, jank, shaders, rebuild, images, GC, isolate, DB, battery; **release** profiling. |
| `MIGRATION_AUDIT` | Flutter/Dart, AGP/Kotlin, iOS/Xcode, plugins, state, router, channels→Pigeon/FFI, DB. |
| `RELEASE_AUDIT` | Flavors, signing, symbols, obfuscation, AAB/IPA, store, staged rollout, crash, hotfix. |

## Operating Contract

1. Status: `CONFIRMED` / `PARTIALLY_CONFIRMED` / `UNVERIFIED` / `NOT_APPLICABLE` / `REJECTED`.
2. Do not invent rebuild/jank/leak/race/BuildContext/insecure storage/channel injection without evidence.
3. For each command: Flutter/Dart version, channel, platform, device, mode, flavor, exit, artifact.
4. Do not invent doctor/analyze/test/frame timing/signing/store/device output.
5. Do not delete `pubspec.lock`; no major `pub upgrade` without a plan; no `flutter clean` as the first step; do not wipe native edits; do not change applicationId/Bundle ID without continuity; do not delete the user DB as a fix.
6. Do not display keystore, Apple keys, API secrets, tokens. Clients cannot reliably hold server secrets; anything in the binary is potentially exposed.
7. Prefer the stable channel for production unless a documented exception exists.

## Finding Register

```text
ID / P0-P3 / Evidence status
Platform / Flutter-Dart / module / flow
Evidence / Reproduction / Root cause / Impact / Likelihood
Fix / Test / Platform impact / Release-rollback
```

## Phase A - Protect The Workspace

```text
git status --short --branch
git rev-parse HEAD
flutter --version
dart --version
flutter channel
flutter doctor -v
flutter devices
```

Find: pubspec/lock, Melos, generated code, Android signing (paths only), iOS entitlements/provisioning, flavors, DB/migrations, native plugin forks, CI/store. Test env != production backend. **Do not `flutter clean` first.**

## Phase B - Versions And Pinning

Table: Flutter, Dart, channel, AGP, Gradle, Kotlin, JDK, min/compile/target SDK, NDK, Xcode, Swift, CocoaPods, iOS/macOS deployment, Win/Linux toolchain, web renderer, direct packages, plugins, generators, test/lint, CI.

Pin: FVM/Puro/mise/`.fvmrc`/CI image. `environment.sdk` / `environment.flutter`.

Platform minimum = product decision (store + user base + plugins).

## Phase C - Pub Dependency Baseline

```text
flutter pub get
flutter pub outdated
dart pub deps
# audit where tools exist; discontinued packages
```

Check: dependency_overrides, path/git deps, floating versions, unused, federated plugins, native code in plugins, licenses. Lock committed for apps.

## Phase D - Format / Analyze / Test / Build Baseline

```text
dart format --output=none --set-exit-if-changed .
flutter analyze
flutter test
flutter test integration_test   # where present
flutter build apk --release     # and/or appbundle / ipa / windows / macos / linux / web
```

Record analyzer, test failures, signing blockers, plugin compile errors. Use release mode for performance conclusions.

## Phase E - Dart Correctness

Null safety; avoid `dynamic`/`!`/`late` as masks; immutability; equality/hash; exceptions; DateTime/timezone; money (not double); sealed/pattern where relevant.

## Phase F - Architecture And Source Of Truth

Layers: UI / state / domain / data. Who is source of truth (server, local DB, memory). Repository boundaries. Feature modules. Dependency direction. Global singletons. God objects.

Flow: `OS/deep link/notification/UI → navigation → state/use case → repository → local/remote → plugin/native → result → UI/telemetry`.

## Phase G - State, Navigation, Lifecycle

State ownership, rebuild scope, side effects outside `build`, dispose controllers/subscriptions, `mounted` after await, typed route args, deep-link restore, process death, configuration change, app pause/resume/detach.

## Phase H - Async, Streams, Isolates, Background

Future race/cancel; StreamSubscription dispose; timers; compute/isolate spawn cost; **isolate != automatic race fix**; send/receive ports; background plugins (workmanager, BGTask, FCM); constraints (battery, network); duplicate delivery; **Dart Timer != reliable OS scheduler**.

## Phase I - Platform Channels, Plugins, FFI

Channel names; codec; threading (UI vs background); error codes; large payloads; Pigeon contracts; FFI safety/memory; platform-view lifecycle; add-to-app engine attach/detach; plugin Android/iOS version skew; breaking native APIs.

## Phase J - Auth, Security, Privacy

Token storage (Keychain/Keystore vs SharedPreferences); biometric; optional cert pinning; TLS; WebView (JS bridge, origin); deep-link authz; screenshot FLAG_SECURE; clipboard; PII in logs; root/jailbreak policy; **no server secrets in the client**.

AuthZ: do not treat UI hiding as authorization; object ownership.

## Phase K - Local Storage, Offline, Sync

sqflite/drift/hive/isar/objectbox; migrations; schema version; corruption recovery; encryption keys; sync conflicts; offline queue; idempotency; multi-isolate DB access; backup/export; right-to-delete.

## Phase L - Permissions, Deep Links, Notifications

Permission rationale and denial paths; Android 13+ notifications; iOS ATT/privacy; app links / universal links verification; notification handlers cold/warm/killed; duplicate opens; action-button auth.

## Phase M - Android Platform

Gradle/AGP/Kotlin; flavors; ProGuard/R8 keeps for plugins; 16 KB page size; Play App Signing; AAB; permission manifest merge; background limits; exact alarms; foreground services; deep-link intent filters; Play Console policy.

## Phase N - iOS Platform

Deployment target; UIScene; Info.plist usage strings; capabilities; ATS; background modes; push entitlements; privacy manifest; archive/export; App Store Connect.

## Phase O - Desktop / Web / Add-to-App

Desktop window lifecycle; secure storage differences; path_provider; web renderer (canvaskit/html/skwasm); CORS; add-to-app: engine lifecycle, platform views, memory, multiple engines.

## Phase P - Performance, Memory, Battery, A11y

Profile/release: startup, frame build/raster, jank, shader warm-up, image cache, list virtualization, rebuilds, GC, isolates for CPU. Battery: GPS, wake locks, polling. A11y: Semantics, screen readers, contrast, text scale, RTL, large screens.

## Phase Q - Observability And Crash

Crashlytics/Sentry; **Dart + native symbols**; breadcrumbs without secrets; ANR/watchdog; release mapping upload in CI; feature flags.

## Phase R - Release, Signing, Store, Rollout

Flavors (dev/stage/prod); isolated keystore/provisioning; obfuscation + split-debug-info; store metadata/privacy; staged rollout; abort criteria; hotfix; custom OTA security if any; do not lose symbols.

## Severity

| P | Definition |
| --- | --- |
| P0 | Auth/token leak, data loss/corruption, RCE via plugin/WebView, store-blocking crash, signing key compromise. |
| P1 | Broken lifecycle/async side effects, insecure token storage, deep-link hijack, failed offline integrity, 16 KB reject, background data loss. |
| P2 | Measured jank/startup, a11y, weak crash symbols, tech debt. |
| P3 | Docs, naming, style. |

## Production Checklist

1. Stable Flutter pin. 2. pub get+analyze+test. 3. Release build per target platform. 4. 16 KB Android where required. 5. Secure auth tokens. 6. No server secrets in client. 7. Channels/plugins validated. 8. DB migration/recovery. 9. Permissions/deep links/push. 10. Symbols uploaded. 11. Signing isolated. 12. Clean-device smoke. 13. Crash monitoring. 14. Rollback plan.

## Definition Of Done

Type/platforms/paths; SDK/channel/pin; Pub graph; format/analyze/test/build baseline; architecture/state; lifecycle/async; channels/FFI; auth/security; local data/sync; permissions/links/push; Android+iOS (+desktop/web); perf measured or UNVERIFIED; crash/symbols; release artifacts; P0/P1; regression tests; rollout/rollback; command log; unverified platforms listed; no false production-ready claims.

If not: **The Flutter application is not yet fully production-ready.**

## Forbidden

Invent output/CVEs/screens; delete lock; broad upgrades; change state library without evidence; `dynamic`/`!`/`late` as masks; async in `build`; BuildContext after await without analysis; leak subscriptions/timers/isolates; Timer as background scheduler; WebView bridge without origin protection; tokens in plain prefs without a threat model; server secrets in the app; disable TLS; over-broad permissions; UI = authz; delete user DB; irreversible migration without recovery; obfuscation = encryption; lose symbols; signing on PRs; emulator = device; Android = iOS; optimize without profile/release; declare perfect.

## Final Report

1. Summary + verdict. 2. Type/platforms/paths. 3. Version matrix. 4. Architecture/state map. 5. Async/lifecycle/background. 6. Channels/plugins/native. 7. Auth/security/privacy. 8. Local data/offline. 9. Permissions/links/push. 10. Per-platform results. 11. Perf/a11y. 12. Crash/symbols. 13. Findings P0–P3. 14. Changes+tests. 15. Command log. 16. Release/signing/store. 17. Rollout/rollback. 18. Blockers. 19. Sources (URL, date).

## Work Order

protect (+signing) → type/platforms/paths → SDK baseline → Pub → format/analyze/test/build → architecture/state → navigation/lifecycle → async/isolate/background → channels/FFI → auth/security → storage/offline → permissions/links/push → Android → iOS → desktop/web/add-to-app → perf/a11y → observability → findings → fixes → platform tests → release/signing/store → rollout/rollback → report.

Priorities: users/data; auth/tokens; functional/platform correctness; lifecycle/async/background; local-data integrity; native/plugin boundaries; store/signing; measured perf; a11y/UX; maintainability.
