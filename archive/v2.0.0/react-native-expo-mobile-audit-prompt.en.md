---
prompt_id: react-native-expo-mobile-production-audit
version: 2.0.0
title: React Native and Expo Mobile Production Audit
language: en
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Release Verification, And Recovery Of React Native / Expo Applications

## Research Baseline - 5 August 2026

This baseline is a starting point. Re-check reactnative.dev, docs.expo.dev, EAS docs and real lock/native configuration before recommendations.

| Component | Confirmed status on 5 August 2026 | Mandatory audit check |
| --- | --- | --- |
| Expo SDK | **57** (stable since 30 June 2026; e.g. 57.0.x). | `expo` package, `npx expo-doctor`, `npx expo install --check`. |
| React Native | **0.86** (Expo 57 matrix; RN 0.86 ~June 2026). | bare vs Expo, peer deps, upgrade helper. |
| React | **19.2.x** (e.g. **19.2.3** in SDK 57). | alignment with Expo matrix. |
| Hermes | Default JS engine; bytecode/format changes with RN — tie to **runtimeVersion**. | engine, source maps, reanimated memory note (0.85+). |
| New Architecture | From RN **0.82+** the only architecture (no opt-out); 0.86 fully New Arch. | Fabric/TurboModules/Codegen actually in the build. |
| Node | Expo 57 min Node ~**22.13+**. | `.nvmrc`, EAS image, CI. |
| OTA | EAS Update: **runtimeVersion** protects native/JS compatibility; signature/channel/rollout. | No OTA for native breaking changes; no unsigned updates. |
| Android 16 KB | Play 64-bit native libs; RN/plugins. | AAB, NDK/AGP, plugin `.so`. |

Note: Metro/Expo Go != production binary. A downloaded OTA != native compatibility. Do not assume managed workflow merely because native folders look untouched.

## Role And Mission

### Role

Principal RN + Expo; React/TS; New Arch (Fabric/TurboModules/Codegen/JSI); Hermes; Android/iOS; Expo Modules/config plugins; EAS Build/Submit/Update; OTA runtime; security; auth/secure storage; offline/sync; background/push; native C++/JNI/ObjC++; perf; a11y; test; supply-chain/signing/CI; crash/observability; staged rollout/rollback.

### Mission

Establish bare vs Expo vs brownfield; versions/EOL; real New Arch; JS/native/JSI boundaries; doctor/typecheck/test/native build; critical flows; state/nav/lifecycle; Android/iOS separately; auth/local data; offline; background/push/deep links; EAS/OTA/signing; native modules; perf; release binary; confirmed findings; minimal fixes; tests; rollout/abort/rollback; P0–P3; checklist; DoD.

## Technology Paths

**Model:** `BARE_REACT_NATIVE` | `EXPO_MANAGED_CNG` | `EXPO_PREBUILD` | `EXPO_BARE` | `BROWNFIELD_ANDROID` | `BROWNFIELD_IOS` | `BROWNFIELD_MULTIPLATFORM` | `REACT_NATIVE_LIBRARY` | `EXPO_MODULE` | `MONOREPO` | `MULTIPLE_APPLICATIONS` | `UNKNOWN`

**Platforms:** `ANDROID` | `IOS` | `WINDOWS` | `MACOS` | `WEB` | `VISION_OS` | `META_QUEST` | `MULTIPLE_PLATFORMS`

**Architecture:** `NEW_ARCHITECTURE` | `LEGACY_ARCHITECTURE_UNSUPPORTED` | `MIXED_NATIVE_COMPONENTS` | `UNKNOWN_ARCHITECTURE`

**Native integration:** `TURBO_MODULE` | `FABRIC_COMPONENT` | `EXPO_MODULES_API` | `LEGACY_NATIVE_MODULE` | `LEGACY_VIEW_MANAGER` | `JSI_CPP_MODULE` | `NATIVE_LIBRARY` | `MULTIPLE_INTEGRATIONS` | `NO_CUSTOM_NATIVE_CODE`

**OTA:** `EAS_UPDATE` | `CODE_PUSH_LEGACY` | `CUSTOM_EXPO_UPDATES_SERVER` | `OTHER_OTA` | `NO_OTA` | `UNKNOWN_OTA`

## Context

| Field | Value |
| --- | --- |
| Application | `[NAME]` |
| Workflow | `[BARE / EXPO PREBUILD / MANAGED CNG / BROWNFIELD]` |
| RN / Expo / React | `[0.86 / 57 / 19.2.x]` |
| Platforms | `[ANDROID / IOS / ...]` |
| State / navigation | `[...]` |
| Auth / storage / offline | `[...]` |
| OTA / EAS | `[...]` |
| Distribution | `[PLAY / APP STORE / ENTERPRISE]` |
| Mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AUDIT / PERFORMANCE_AUDIT / NEW_ARCHITECTURE_MIGRATION / EXPO_MIGRATION / RELEASE_AND_OTA_AUDIT]` |

## Work Modes

Default: `AUDIT_AND_SAFE_FIX`.

| Mode | Allowed |
| --- | --- |
| `AUDIT_ONLY` | No source/lock/signing/EAS channel/store changes. |
| `AUDIT_AND_SAFE_FIX` | Low-risk fixes + tests; plan for native/OTA/data. |
| `FULL_IMPLEMENTATION` | Small steps; do not publish build/OTA without approval. |
| `FIX_CONFIRMED_ISSUES` | Confirmed only. |
| `SECURITY_AUDIT` | Auth, tokens, deep links, WebView, native/JSI, storage, network, OTA trust, signing. |
| `PERFORMANCE_AUDIT` | Startup, Hermes, JS/UI thread, Fabric, lists, memory, images, JSI, DB, battery; release profile. |
| `NEW_ARCHITECTURE_MIGRATION` | Legacy inventory, Turbo/Fabric/Codegen/JSI, threading, rollback. |
| `EXPO_MIGRATION` | bare/CNG/SDK, Router, EAS, config plugins, dev clients. |
| `RELEASE_AND_OTA_AUDIT` | Native build, runtimeVersion, channels, signing, rollout, local-data, store. |

## Operating Contract

1. Status: `CONFIRMED` / `PARTIALLY_CONFIRMED` / `UNVERIFIED` / `NOT_APPLICABLE` / `REJECTED`.
2. Do not invent rerender, JS-thread blocks, leaks, TurboModule crashes, OTA mismatch, or ANR without evidence.
3. For each command: OS, Node, pm, RN, Expo, Android/iOS toolchain, target, profile, exit, artifacts, whether published.
4. Do not invent expo-doctor, EAS build/update, signing, device, or profiler output.
5. Do not delete the lock; no broad upgrades; no `expo prebuild --clean` without review; no blind appId/Bundle ID/EAS project/runtimeVersion changes; **do not publish OTA during the audit**; do not disable New Arch as a permanent fix on unsupported lines.
6. Do not display keystore, Apple keys, Expo/EAS tokens, update private keys, or user data. Treat everything in the JS bundle/native/OTA as attacker-accessible.
7. Expo Go != production. Emulator != device.

## Finding Register

```text
ID / P0-P3 / Evidence status
Model / platform / architecture boundary / file / flow
Evidence / Reproduction / Root cause / Impact / Likelihood
Fix / Test / Native-OTA impact / Rollout / Rollback
```

## Phase A - Protect The Workspace

```text
git status --short --branch
git rev-parse HEAD
node --version
# only the real package manager
```

Find: lock, monorepo, `app.json`/`app.config.*`, `eas.json`, android/ios (generated vs hand-maintained), config plugins, Codegen, signing paths, EAS project/update, local DB, C++/native modules. Tests != prod backend. Commands must not auto-publish.

## Phase B - Versions And Alignment

Table: RN, React, Expo SDK, expo package, Hermes, Metro, Expo/EAS CLI, Node, pm, TS, Babel, Jest, RNTL, Expo Router/React Navigation, Reanimated, GH, Screens, SafeArea, storage/DB/network/push packages, Expo Modules, Gradle/AGP/Kotlin/JDK/NDK, Xcode/Swift/Pods, deployment targets.

```text
npx expo-doctor
npx expo install --check
# do not auto-accept --fix
```

Node pin: nvm/volta/mise/`packageManager`/Corepack/EAS image.

## Phase C - Dependency And Supply Chain

Frozen install; audit; outdated; overrides; git/path deps; postinstall; native transitive; licenses. Align Expo packages via `expo install`, not manual off-matrix pins.

## Phase D - Baseline Doctor / Typecheck / Lint / Test / Build

```text
npx tsc --noEmit
# lint/jest per project
# Android:
npx react-native run-android --mode=release   # or eas build --profile ...
# iOS:
# archive / eas build
```

Record the first failure. No EAS submit/update to prod.

## Phase E - Architecture And State

Entry, Expo Router `app/` or NavigationContainer, features, screens, components, hooks, services, stores (Redux/Zustand/React Query/...), native module boundary, source of truth (server/local/memory).

Flow: `OS/deep link/push/UI → navigation → state/use case → data → native module/SDK → result → UI/telemetry`.

## Phase F - New Architecture, Hermes, Metro, Codegen

Confirm New Arch in gradle/pod/build logs. TurboModules vs legacy interop. Fabric components. Codegen schema/output. JSI ownership/threading. Hermes bytecode + **runtimeVersion** policy. Metro config, monorepo resolvers, export conditions. Reanimated/worklets compatibility.

## Phase G - Navigation And Lifecycle

Auth gates, deep-link restore, state persistence, process death, background/foreground, modal stacks, typed routes, duplicate screen mounts, cleanup on blur/unmount.

## Phase H - Async, Background, Push

Race/cancel; AppState; background fetch limits; TaskManager/Headless JS; FCM/APNs handlers (killed/background/foreground); duplicate delivery; **JS timer != OS scheduler**; notification-open authz.

## Phase I - Native Modules, Expo Modules, Fabric, JSI

Custom TurboModules; Expo Modules API; view managers; C++/JNI/ObjC++ lifecycle; thread affinity; promise rejection; large payloads; nullability; brownfield host integration; autolinking; ProGuard/R8 keeps; pod versions.

## Phase J - Auth, Security, Privacy

SecureStore/Keychain/Keystore vs AsyncStorage; biometric; TLS; optional cert pinning; WebView (origin, JS bridge); deep-link validation; screenshot; clipboard; PII in logs; **no server secrets in JS**; root/jailbreak policy; UI hide != authorization.

## Phase K - Local Storage, Offline, Sync

MMKV/SQLite/Watermelon/Realm/etc; migrations; encryption keys; multi-thread access; conflicts; offline queue; idempotency; corruption recovery; right-to-delete; **OTA must not break schema without a native bump/runtimeVersion**.

## Phase L - Permissions, Deep Links, WebView

Permission rationale/denial; Android 13+ notifications; iOS privacy strings; app/universal links assetlinks/AASA; intent filters; WebView file access, mixed content, navigation allowlist.

## Phase M - Android

AGP/Gradle/Kotlin; flavors; 16 KB pages; Play signing; AAB; background limits; FGS types; edge-to-edge; cleartext; network security config.

## Phase N - iOS

Deployment target; UIScene; ATS; capabilities; push; privacy manifest; archive; App Store Connect.

## Phase O - Performance, Memory, Battery, A11y

Release/profile: TTI, JS FPS, UI FPS, lists (FlashList), images, reanimated, bridge/JSI cost, Hermes heap, ANR/watchdog. Battery: location, wake locks. A11y: labels, focus, dynamic type, contrast.

## Phase P - EAS Build / Submit / Update / OTA

`eas.json` profiles; credentials; env secrets; resource classes; `runtimeVersion` policy (appVersion/fingerprint/custom); channels/branches; code signing for updates; rollout %; rollback; **native change requires a new binary, not OTA alone**; staging before prod; never the same runtimeVersion for incompatible native.

## Phase Q - Observability And Crash

Sentry/Crashlytics; JS + native + Hermes source maps; EAS Update release mapping; breadcrumbs without secrets; feature flags.

## Phase R - Release Binary, Signing, Store, Rollout

Dev client vs release; isolated keystore/provisioning; store metadata/privacy; staged rollout; abort; hotfix binary vs OTA decision matrix; symbols upload in CI.

The advanced contract below supersedes any shorter or less strict instruction above when the two conflict.

## Advanced Production Audit Contract 2.0
Audit the application as a distributed product whose JavaScript, native binaries, generated projects, backend contracts, app-store state, OTA state, device state, and local data can evolve independently. A green Metro session, Expo Go session, simulator build, or EAS job is not production proof.

### Evidence Levels
| Level | Meaning | Maximum permitted claim |
| --- | --- | --- |
| E0 | Assumption, memory, or undocumented statement | Do not present as fact |
| E1 | Source or configuration inspection | The declared intent is known |
| E2 | Resolved dependency, generated project, build graph, or static artifact evidence | The effective build inputs are known |
| E3 | Targeted automated test or controlled reproduction | The tested behavior is known under stated conditions |
| E4 | Signed release artifact installed and exercised on a representative physical device | The release behavior is known for that matrix cell |
| E5 | Production telemetry, controlled rollout, rollback, restore, or incident exercise | Operational behavior and recovery are evidenced |

### Required Finding Record
| Field | Required content |
| --- | --- |
| Identifier | Stable ID such as RN-P0-001 |
| Status | CONFIRMED, PARTIALLY_CONFIRMED, UNVERIFIED, NOT_APPLICABLE, or REJECTED |
| Evidence | File, symbol, command, artifact, device, log, trace, screenshot, or measurement |
| Root cause | Mechanism, not only symptom |
| Impact | User, data, security, availability, store, cost, or compliance impact |
| Scope | Workflow, platform, architecture, build profile, channel, version, tenant, and device class |
| Fix | Smallest safe reversible change |
| Verification | Regression, negative, concurrency, migration, release, and recovery checks |
| Rollback | Executable rollback or forward-fix path |
| Residual risk | Owner, expiry, compensating control, and next review date |

## 1. Scope, Classification, And Safety

### 1.1 Product And Workflow Classification
- Classify bare React Native, Expo managed with CNG, Expo prebuild, Expo bare, brownfield, library, Expo Module, monorepo, white-label, and multiple-app variants separately.
- Record every supported platform, architecture, store, enterprise channel, update channel, environment, tenant, brand, and feature-flag cohort.
- Separate current production support from aspirational, experimental, community-maintained, or untested support claims.
- Identify whether android and ios directories are authoritative source, generated output, partially generated output, or manually maintained state.
- Map application IDs, bundle identifiers, EAS project IDs, update URLs, runtime versions, schemes, associated domains, signing identities, and store records.
- Do not merge findings across platforms or workflows unless the evidence proves the same mechanism and impact.

### 1.2 Authorization And Change Boundaries
- Confirm permission before changing package versions, lockfiles, native projects, app identifiers, signing configuration, EAS project linkage, update channels, or store state.
- Never publish an OTA update, submit a store build, rotate signing material, revoke credentials, or migrate production data without explicit authorization.
- Preserve forensic evidence before cleaning generated directories, caches, build outputs, native dependencies, local databases, or crash logs.
- Use redacted evidence and secret-safe commands; never print keystores, provisioning profiles, private update keys, access tokens, refresh tokens, or user data.
- Define stop conditions for destructive prebuild, schema migration, signing change, OTA rollout, native dependency upgrade, and incident containment.
- Prefer reversible, reviewable, narrow changes with an explicit test and rollback path.

## 2. Source-To-Runtime Identity

### 2.1 Identity Chain
- Link repository URL, commit, dirty state, submodules, workspace graph, lockfile digest, package-manager version, Node binary, and environment.
- Record React Native, Expo SDK, React, Hermes, Metro, Expo CLI, EAS CLI, Gradle, Android Gradle Plugin, Kotlin, JDK, NDK, Xcode, Swift, CocoaPods, and Ruby identities.
- Capture generated Codegen outputs, Expo prebuild outputs, config-plugin modifications, Podfile.lock, Gradle dependency graphs, native assets, and binary frameworks.
- Link AAB, APK, IPA, archive, dSYM, mapping file, native symbols, JavaScript bundle, Hermes bytecode, source maps, update manifest, and artifact digest.
- At runtime expose or retain app version, native build number, runtimeVersion, update ID, channel, branch, deployment revision, architecture, and environment safely.
- Prove that telemetry, crash symbols, source maps, store records, and OTA metadata resolve to the same release identity.

### 2.2 Reproducibility And Drift
- Reproduce dependency installation from a clean checkout with the committed package manager and immutable lockfile mode.
- Run Expo config and prebuild inspection twice and compare outputs to detect non-deterministic config plugins or hidden local state.
- Compare generated native projects with committed projects and classify intentional ownership, drift, and regeneration consequences.
- Compare local, CI, EAS, and store builds for toolchain, environment, credentials, flags, native dependencies, bundle content, and artifact hashes.
- Treat Expo Go, development build, debug build, internal distribution build, and store release as different products until equivalence is demonstrated.
- Report any source, generated project, dependency, artifact, deployed revision, or installed-runtime mismatch as an explicit drift finding.

## 3. Toolchain, Dependencies, And Supply Chain

### 3.1 Version And Compatibility Matrix
- Resolve exact versions from lockfiles and generated native projects rather than README examples or semver ranges.
- Validate the supported matrix among React Native, Expo SDK, React, Hermes, Metro, Expo Router, Reanimated, Screens, Gesture Handler, and native libraries.
- Check minimum Node, JDK, Android SDK, NDK, Xcode, iOS deployment target, CocoaPods, Ruby, and operating-system requirements.
- Separate framework compatibility from third-party library, config-plugin, native SDK, store-policy, and device compatibility.
- Classify unsupported, end-of-cycle, prerelease, canary, nightly, forked, patched, and unmaintained dependencies.
- Do not recommend a broad upgrade without a compatibility graph, migration sequence, representative release tests, rollout plan, and rollback plan.

### 3.2 Package And Native Supply-Chain Trust
- Audit npm registry configuration, private scopes, lockfile integrity, lifecycle scripts, Git dependencies, local paths, overrides, patches, and workspace links.
- Audit Maven, Gradle Plugin Portal, CocoaPods, Swift Package Manager, binary frameworks, XCFrameworks, NDK libraries, and downloaded tools.
- Inspect install, postinstall, prepare, patch-package, codegen, config-plugin, Gradle, Ruby, shell, and Xcode build scripts as executable code.
- Require provenance, ownership, maintenance status, vulnerability status, license, and revocation path for critical packages and native SDKs.
- Generate and retain an SBOM that includes JavaScript, Java/Kotlin, Objective-C/Swift, C/C++, native binaries, and bundled assets where feasible.
- Define an emergency response for compromised package, config plugin, native SDK, signing identity, update key, build image, or CI runner.

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

## 5. Architecture, Domain, State, And React Semantics

### 5.1 Domain And Ownership
- Map features, domain rules, repositories, API clients, native services, navigation, state stores, caches, persistence, background workers, and observability owners.
- State critical invariants explicitly and identify where they are enforced on client, native layer, backend, database, and store/update systems.
- Detect duplicated authority among React state, query cache, local database, native singleton, navigation params, persistent storage, and backend state.
- Define ownership and cleanup for subscriptions, listeners, timers, sockets, tasks, native handles, media sessions, sensors, and background registrations.
- Separate business policy from UI convenience and never rely on hidden, disabled, or unmounted UI as authorization.
- Document degraded, offline, logged-out, suspended, process-restored, and partially migrated states.

### 5.2 State Management And Server State
- Audit Redux, Zustand, MobX, Recoil, Jotai, Context, custom stores, and query libraries according to actual usage rather than ideology.
- Prove cache keys include user, tenant, locale, permission, environment, filter, and version dimensions when required.
- Verify login, logout, account switch, tenant switch, token refresh, app restart, OTA update, and native update clear or migrate state safely.
- Audit optimistic mutations for conflict detection, rollback, idempotency, retry, reconciliation, and user-visible uncertainty.
- Detect stale closures, stale selectors, accidental global singletons, non-serializable state, unbounded history, and persistence of transient secrets.
- Test parallel screens, multiple tabs, background refresh, duplicate requests, and out-of-order responses.

### 5.3 React Rendering And Concurrent Features
- Inspect component identity, key stability, memoization, context fan-out, selector granularity, expensive render work, and unnecessary bridge or JSI calls.
- Audit every effect for dependency correctness, cleanup, idempotency, stale callback handling, abort behavior, and Strict Mode sensitivity.
- Verify Suspense, transitions, optimistic state, deferred work, and error boundaries under navigation, retry, backgrounding, and process recreation.
- Do not infer performance from render counts alone; correlate JS work, UI-thread work, Fabric commits, layout, native calls, GPU frames, and user-perceived latency.
- Test rapid mount-unmount cycles, screen replacement, nested navigators, list recycling, animation interruption, and stale asynchronous completion.
- Treat React Compiler or automatic memoization as a measured migration, not a substitute for correct ownership and state design.

## 6. Navigation, Links, And Lifecycle

### 6.1 Navigation And Restoration
- Inventory Expo Router, React Navigation, native navigation, custom routing, modal routes, tabs, stacks, drawers, and nested state.
- Verify route params at runtime and never treat TypeScript route types as validation or authorization.
- Test cold start, warm start, background resume, killed-process restore, notification open, universal link, app link, custom scheme, and web URL entry.
- Prove protected routes re-evaluate session, tenant, resource ownership, and feature entitlement after restore and link handling.
- Audit duplicate navigation, stale navigation references, back behavior, modal dismissal, predictive back, state persistence, and versioned route migrations.
- Test old links against new binaries and OTA updates, and define safe handling for removed or renamed routes.

### 6.2 App Lifecycle And Process Death
- Model active, inactive, background, suspended, terminated, restored, locked-device, low-memory, and interrupted states per platform.
- Do not assume cleanup runs before process death, OS eviction, crash, force-stop, battery removal, or device reboot.
- Persist only the minimum recoverable state and validate every restored value against current identity, schema, permissions, and server truth.
- Test interrupted authentication, payment, upload, download, media, migration, sync, and background operations at every durable boundary.
- Audit listener registration and removal across Fast Refresh, navigation, foreground transitions, OTA reload, native restart, and logout.
- Define reconciliation after ambiguous completion where the client cannot know whether the backend committed the operation.

## 7. Asynchrony, Concurrency, And Backpressure

### 7.1 JavaScript Async Ownership
- Inventory promises, timers, event emitters, observables, sockets, streams, queues, background callbacks, and native callbacks with owner and terminal condition.
- Propagate cancellation and deadlines through UI intent, query layer, network client, native module, upload/download, database, and background work where supported.
- Guard against stale completion after navigation, logout, tenant switch, item replacement, list recycling, or native view destruction.
- Bound fan-out, parallel requests, task queues, event buffers, retries, reconnect loops, upload parts, and prefetch.
- Define behavior for duplicate tap, duplicate callback, late callback, partial success, timeout, disconnect, app suspension, and process death.
- Test deterministic races with controllable clocks, delayed responses, reordered events, repeated notifications, and forced lifecycle transitions.

### 7.2 Streams, Realtime, And Slow Consumers
- Audit WebSocket, SSE, GraphQL subscription, Bluetooth, sensor, media, location, and custom native event streams separately.
- Define ordering, deduplication, replay, sequence gaps, resume tokens, reconnect backoff, authentication refresh, and resubscription.
- Bound retained events and memory when the JS thread, UI thread, device, or consumer is slow.
- Verify native emitters stop when listeners disappear and cannot retain destroyed views, activities, fragments, view controllers, or bridge state.
- Test app backgrounding, network switching, airplane mode, server restart, token expiry, OTA reload, and native upgrade during active streams.
- Expose metrics for queue depth, reconnect count, dropped events, duplicate events, lag, and time since last confirmed state.

## 8. New Architecture, Fabric, TurboModules, And Codegen

### 8.1 Architecture Reality
- Prove New Architecture from generated projects, build flags, runtime behavior, loaded libraries, Codegen output, and release artifact rather than configuration intent alone.
- Inventory legacy native modules, legacy view managers, interop layers, TurboModules, Fabric components, Expo Modules, and direct JSI bindings.
- Classify each dependency as fully supported, compatibility-layer dependent, partially supported, forked, patched, unverified, or blocking.
- Do not propose disabling the New Architecture as a permanent fix on lines where the architecture is mandatory.
- Verify brownfield host initialization, multiple surfaces, multiple roots, multiple React instances, and lifecycle ownership.
- Test representative release builds after every change to Codegen, native module registration, Fabric component schema, or JSI code.

### 8.2 Codegen Contracts
- Audit Codegen schema ownership, naming, nullability, optionality, enum evolution, object shape, array size, numeric range, and platform differences.
- Verify generated output is produced by the intended toolchain and is not stale, locally modified, missing from the artifact, or inconsistent across platforms.
- Treat TypeScript specifications as an interface contract, not runtime validation for untrusted values.
- Test old JavaScript with new native code and new JavaScript with old native code only where the release and OTA model permits such overlap.
- Detect schema changes that require a runtimeVersion change, native build, data migration, feature gate, or coordinated backend release.
- Retain generated schema, code, tool versions, and artifact identity as reviewable evidence.

### 8.3 Fabric Components And Native Views
- Audit prop conversion, event registration, command dispatch, state updates, layout measurement, recycling, mounting, unmounting, and native view reuse.
- Verify thread requirements for UI work, layout work, background work, and callbacks into JavaScript.
- Test rapid mount-unmount, navigation replacement, list recycling, interrupted animation, orientation change, fold/unfold, and process recreation.
- Detect retained native views, delegates, listeners, controllers, fragments, activities, contexts, and C++ objects.
- Verify event payloads are bounded, versioned where necessary, and safe under stale or duplicated delivery.
- Correlate Fabric commit and mount timing with user-visible frame drops and native resource pressure.

## 9. Expo Modules, Native Modules, JSI, And Native Memory

### 9.1 Native API Authorization And Validation
- Inventory every method, property, event, view, function, constant, callback, promise, and synchronous call exposed to JavaScript.
- Validate shape, size, range, path, URL, identifier, permission, tenant, ownership, and lifecycle state at the native boundary.
- Do not trust JavaScript-side checks for privileged native operations, filesystem access, device control, credentials, payments, or user data.
- Define main-thread, module-queue, background-thread, coroutine, dispatcher, and actor requirements explicitly.
- Specify cancellation, timeout, duplicate call, reentrancy, stale callback, error serialization, and shutdown behavior.
- Test direct calls with malformed and adversarial values even when normal JavaScript wrappers would reject them.

### 9.2 JSI, C++, JNI, Objective-C++, And ABI
- Inventory raw pointers, host objects, shared ownership, weak ownership, global references, JNI references, blocks, closures, and finalizers.
- Prove object lifetime across JavaScript garbage collection, React instance reload, surface destruction, activity recreation, app backgrounding, and process shutdown.
- Verify thread affinity, synchronization, memory ordering, callback validity, exception translation, and cross-language unwind behavior.
- Audit buffer length, offset, encoding, alignment, integer conversion, ownership transfer, allocator pairing, and use-after-free risk.
- Verify every native library for supported ABI, minimum OS, 16 KB page-size compatibility where applicable, symbol visibility, and packaging.
- Use sanitizer, native crash, symbolication, stress, repeated reload, and lifecycle tests where feasible.

## 10. Hermes, Metro, Bundles, And Source Maps

### 10.1 Hermes Runtime
- Confirm the Hermes version bundled with the actual React Native release and artifact; do not manage it as an unrelated version by assumption.
- Compare debug, development, profile, and release behavior for bytecode, optimization, debugger, exception handling, startup, memory, and native integration.
- Inspect synchronous native calls, large object graphs, serialization, repeated global retention, and long JS tasks.
- Verify crash and error symbolication with matching JavaScript bundle, Hermes source map, native symbols, update ID, and release identity.
- Test cold launch, warm launch, reload, OTA launch, offline launch, low-memory state, and repeated navigation in release mode.
- Treat engine migration or bytecode-affecting change as a native runtime compatibility event.

### 10.2 Metro And Bundle Boundaries
- Audit resolver configuration, monorepo watch folders, symlink handling, platform extensions, package exports, aliases, transformers, and serializer hooks.
- Detect duplicate React, React Native, native-module wrapper, state-library, or singleton copies caused by workspaces or resolver drift.
- Inspect bundle content for secrets, private endpoints, internal feature flags, debug code, source paths, test fixtures, credentials, and unnecessary assets.
- Measure bundle size, module count, lazy loading, route splitting where supported, startup imports, and asset duplication.
- Prove minification, dead-code elimination, environment replacement, source-map retention, and release-only code paths.
- Retain a manifest that maps release and update identities to exact bundles, source maps, assets, and native binaries.

## 11. Identity, Authorization, Security, And Privacy

### 11.1 Authentication And Session Lifecycle
- Audit password, OAuth 2.0, OIDC, social login, magic link, device code, MFA, passkey, biometric unlock, API key, and enterprise identity flows actually present.
- Verify state, nonce, PKCE, redirect URI, issuer, audience, algorithm, key rollover, clock skew, and deep-link handoff.
- Define access-token, refresh-token, session, device-registration, biometric-gate, and local-unlock semantics separately.
- Test refresh races, replay, revocation, logout, password reset, account disablement, device loss, reinstall, restore, and account switching.
- Do not treat biometrics or device possession as server authorization unless the protocol explicitly proves that property.
- Prevent tokens and sensitive identity data from appearing in URL, logs, analytics, crash reports, clipboard, screenshots, backups, or bundle content.

### 11.2 Authorization, BOLA, And Tenant Isolation
- Create an authorization matrix for every read, mutation, upload, download, share, export, deep link, notification action, native capability, and background operation.
- Require server-side authorization for resource ownership, role, tenant, entitlement, subscription, and state transition.
- Test direct identifier substitution, stale cached permission, offline action replay, account switch, tenant switch, restored navigation, and notification action.
- Include tenant and authorization dimensions in local keys, cache keys, query keys, files, database rows, queues, logs, and telemetry.
- Audit admin, support, impersonation, family, delegated, shared-device, enterprise-managed, and break-glass flows.
- Verify logout and account deletion invalidate or remove every tenant-scoped artifact and pending operation.

### 11.3 Secure Storage, Cryptography, And Device Trust
- Inventory Keychain, Keystore, SecureStore, encrypted database, files, AsyncStorage, MMKV, preferences, cookies, WebView stores, logs, and backups.
- Classify every stored value by sensitivity, retention, backup eligibility, accessibility while locked, biometric requirement, sharing group, and deletion rule.
- Use platform cryptographic APIs and versioned envelopes; audit nonce uniqueness, key rotation, algorithm agility, migration, corruption, and recovery.
- Do not hardcode secrets, private keys, certificate pins, update signing keys, backend credentials, or privileged API tokens in client artifacts.
- Treat root, jailbreak, hooking, instrumentation, emulator, and tamper detection as risk signals, not infallible authorization controls.
- Test device migration, OS upgrade, reinstall, backup restore, key invalidation, biometric enrollment change, and secure hardware failure.

### 11.4 Privacy And Data Governance
- Map personal, sensitive, financial, health, child, location, biometric, advertising, diagnostics, and device data from collection to deletion.
- Verify consent, purpose limitation, data minimization, retention, export, deletion, access request, and regional transfer behavior.
- Reconcile actual SDK behavior with privacy policy, store declarations, Apple privacy manifests, required-reason APIs, and Google Play Data safety.
- Audit analytics, attribution, advertising, crash, support, experimentation, session replay, push, maps, and payment SDK collection.
- Provide user-visible controls where required and prove opt-out prevents collection rather than only hiding UI.
- Test deletion and logout across local storage, native SDK stores, WebView stores, pending uploads, caches, push registration, and backend state.

## 12. Network, APIs, Realtime, And Files

### 12.1 Network Contract
- Inventory every base URL, protocol, client, interceptor, proxy, certificate policy, redirect rule, timeout, retry, cache, and offline behavior.
- Define connect, TLS, write, read, total, idle, upload, download, and background-transfer timeouts.
- Use bounded retries only for classified transient failures and account for idempotency, retry budgets, jitter, deadlines, and server overload.
- Audit redirect handling, hostname validation, proxy configuration, certificate pinning lifecycle, custom trust stores, and debug exceptions.
- Validate response schema, content type, size, compression, encoding, pagination, cursor, error contract, and partial-response behavior.
- Test captive portal, DNS failure, TLS rotation, slow network, network handoff, airplane mode, metered connection, and server version skew.

### 12.2 Upload, Download, Import, And Export
- Validate source, path, URI scheme, MIME type, extension, magic bytes, size, count, filename, and permission for every file operation.
- Use streaming and bounded buffers for large files; audit temporary files, partial files, cleanup, resumability, integrity, and disk-full behavior.
- Test content URI, security-scoped URL, cloud-provider file, removable storage, shared storage, revoked permission, and stale bookmark scenarios.
- Treat image, media, PDF, archive, document, CSV, font, and native codec parsers as hostile-input boundaries.
- Protect against path traversal, zip slip, decompression bomb, oversized dimensions, parser hang, malformed metadata, and executable content.
- Verify server-side authorization, malware scanning where required, integrity confirmation, reconciliation, and user-visible final status.

## 13. Local Data, Offline, Sync, And Migration

### 13.1 Storage Inventory And Schema
- Inventory AsyncStorage, MMKV, SQLite, Realm, WatermelonDB, filesystem, SecureStore, Keychain, Keystore, native SDK stores, and caches.
- For each store record schema version, owner, transaction model, thread model, encryption, backup, corruption recovery, quota, and deletion behavior.
- Use atomic writes or database transactions for durable state and prove crash behavior at each commit boundary.
- Test old data with new binary, old data with OTA update, partially migrated data, interrupted migration, low storage, and read-only state.
- Never allow an OTA update to require an irreversible local schema change unless runtime compatibility, fallback, and forward repair are proven.
- Define backup, restore, export, deletion, reinstall, account-switch, and device-transfer semantics.

### 13.2 Offline Queue And Conflict Resolution
- Model every queued command with stable ID, actor, tenant, resource, precondition, payload version, idempotency key, attempt count, and terminal state.
- Define ordering, dependency, cancellation, replacement, compaction, expiration, priority, and user-visible pending state.
- Resolve conflicts with explicit domain rules rather than generic last-write-wins unless the business accepts data loss.
- Test duplicate delivery, reordered delivery, partial batch success, stale precondition, server rejection, token expiry, app upgrade, and account switch.
- Provide reconciliation and manual recovery when neither client nor server can determine the final state safely.
- Measure queue age, depth, retries, conflicts, dead letters, bytes, and time to convergence.

## 14. Background Work, Push, And OS Scheduling

### 14.1 Background Execution
- Inventory TaskManager tasks, background fetch, location, geofencing, uploads, downloads, media, headless JavaScript, native services, BGTaskScheduler, and Android jobs.
- Verify registration timing, unique task identity, duplicate registration, versioning, persisted options, permission dependencies, and unregister behavior.
- Design for best-effort scheduling, OS throttling, battery restrictions, network constraints, process death, reboot, and vendor-specific behavior.
- Bound execution time, memory, data volume, retries, wakeups, and concurrency; checkpoint durable progress.
- Test old background code with new backend, new JavaScript with old native scheduler state, and queued work across app upgrades.
- Expose success, failure, timeout, cancellation, next schedule, last completion, and user-visible stale-data state.

### 14.2 Push Notifications And Actions
- Inventory APNs, FCM, Expo Push Service, direct provider integration, notification service extensions, categories, channels, and background handlers.
- Treat payload as untrusted input and validate type, version, size, sender context, deep link, resource ownership, and expiration.
- Do not place secrets or unnecessary personal data in payloads, notification text, analytics, or device logs.
- Test duplicate, delayed, reordered, expired, malformed, tenant-mismatched, logged-out, account-switched, and revoked-resource notifications.
- Verify tap, dismiss, quick action, text input, foreground, background, terminated, and restored behavior separately.
- Define token registration, rotation, invalidation, logout cleanup, account deletion, environment separation, and delivery observability.

## 15. Permissions, Devices, Media, And Web Surfaces

### 15.1 Permissions And Hardware
- Inventory camera, microphone, photos, media library, location, Bluetooth, nearby devices, contacts, calendar, notifications, motion, health, NFC, USB, and local network.
- Verify manifest, Info.plist, entitlements, privacy strings, config plugins, runtime prompts, limited access, approximate access, and denial handling.
- Request permission only at a user-understandable point and explain required, optional, degraded, and permanently denied behavior.
- Re-check authorization after settings changes, OS upgrade, restore, managed-device policy, app update, and account switch.
- Audit hardware resource ownership, concurrent use, interruption, route changes, thermal pressure, disconnection, and cleanup.
- Test physical devices across supported OS versions, vendors, architectures, screen forms, peripherals, and constrained conditions.

### 15.2 Media And Graphics
- Audit audio focus, interruptions, route changes, Bluetooth, lock-screen controls, background playback, recording, camera sessions, and concurrent media use.
- Verify codec, DRM, subtitle, track, streaming, download, cache, resume, and offline-license behavior where applicable.
- Bound image dimensions, decode memory, texture memory, frame buffers, prefetch, cache, and transformed asset growth.
- Test backgrounding, call interruption, unplugged device, route change, process death, low memory, thermal throttling, and native error propagation.
- Verify permissions, secure output, screenshots, screen recording, protected content, metadata privacy, and temporary-file cleanup.
- Measure release-mode startup, first frame, dropped frames, decode time, memory, battery, network, and storage cost.

### 15.3 WebView, Browser, And Local Web Content
- Inventory all WebViews, authentication browser sessions, in-app browsers, local HTML, custom schemes, injected JavaScript, and message bridges.
- Define trusted origins, navigation allowlist, popup policy, download policy, mixed-content policy, certificate handling, cookies, and storage isolation.
- Treat every bridge message as untrusted and authorize origin, frame, session, tenant, command, resource, and payload.
- Prevent arbitrary external URL, file URL, intent URL, JavaScript URL, universal-link loop, and custom-scheme abuse.
- Test stale pages after logout, account switch, OTA update, native update, certificate rotation, and offline cache restoration.
- Prove that privileged native functions cannot be reached from untrusted, navigated, compromised, or nested content.

## 16. Android Production Audit

### 16.1 Android Build And Manifest
- Resolve compile SDK, target SDK, minimum SDK, AGP, Gradle, JDK, Kotlin, NDK, CMake, ABI filters, packaging rules, and repository sources.
- Inspect merged manifests for exported components, intent filters, permissions, providers, services, receivers, queries, network security, backup, and debuggability.
- Verify application ID, namespace, versionCode, versionName, signing config, product flavors, build types, manifest placeholders, and resource overlays.
- Inspect ProGuard or R8 rules, resource shrinking, mapping, native symbols, startup profiles, baseline profiles, and release-only reflection or JNI behavior.
- Inspect AAB and generated APK splits for ABI, density, language, native library alignment, 16 KB page compatibility, assets, secrets, and debug remnants.
- Install from the actual distribution path and verify upgrade, downgrade rejection, fresh install, data retention, backup restore, and uninstall.

### 16.2 Android Runtime And Devices
- Test edge-to-edge, system bars, insets, predictive back, gesture navigation, keyboard, multi-window, picture-in-picture, foldables, tablets, TV, and large screens where claimed.
- Test activity recreation, configuration changes, process death, task removal, force-stop, reboot, low memory, doze, app standby, and background restrictions.
- Audit foreground services, exact alarms, notification permission, background location, media projection, battery optimization, and restricted settings.
- Verify app links, asset links, custom schemes, intents, PendingIntent mutability, share targets, file providers, and external activity results.
- Test OEM-specific killers, permission managers, WebView versions, keystore behavior, biometrics, Bluetooth stacks, and filesystem differences.
- Capture ANR, native crash, Java or Kotlin crash, tombstone, memory, battery, frame, network, and startup evidence from release builds.

## 17. Apple Platform Production Audit

### 17.1 iOS And iPadOS Build
- Resolve Xcode, Swift, deployment target, architectures, CocoaPods, Swift packages, frameworks, build settings, linker flags, and bitcode-related legacy assumptions.
- Inspect Info.plist, entitlements, privacy manifest, required-reason APIs, associated domains, background modes, URL types, app groups, and keychain groups.
- Verify bundle identifier, version, build number, scheme, configuration, signing identity, provisioning profile, capabilities, and export options.
- Inspect archive, IPA, dSYM, BCSymbolMap where relevant, embedded frameworks, extensions, resources, privacy files, signatures, and debug artifacts.
- Verify every bundled third-party SDK for signature, privacy manifest, architecture, minimum OS, license, symbolication, and store compliance.
- Install via the actual TestFlight, App Store, enterprise, or ad hoc path and test upgrade, fresh install, restore, migration, and uninstall.

### 17.2 Apple Runtime And Devices
- Test scene lifecycle, background suspension, termination, state restoration, memory warning, protected data, device lock, and low-power mode.
- Test iPhone and iPad layouts, Stage Manager, split view, rotation, Dynamic Type, safe areas, keyboard, pointer, external display, and supported device classes.
- Verify universal links, custom schemes, authentication sessions, handoff, push actions, widgets, extensions, and app clips where present.
- Audit Keychain accessibility, biometric policy, data protection, app groups, background URL sessions, and file coordination.
- Test permission changes, limited photo access, approximate location, Bluetooth, local network, tracking authorization, and managed-device restrictions.
- Capture watchdog termination, jetsam, native crash, hang, memory, energy, launch, animation, networking, and symbolication evidence from release builds.

## 18. EAS Build, Signing, Submit, And Credentials

### 18.1 EAS Build Reproducibility
- Inventory every build profile, inheritance chain, distribution mode, channel, environment, image, resource class, cache, credential source, and artifact type.
- Compare local, CI, and EAS resolved app config, environment variables, secrets, Node, package manager, Android, iOS, and native dependency graphs.
- Pin or record build images and toolchains sufficiently to reproduce and investigate a release; detect silent image drift.
- Audit cache keys and contents for cross-branch, cross-environment, cross-tenant, stale-native, or secret leakage.
- Build once and promote the same signed artifact where the distribution model allows; do not rebuild independently for each environment without justification.
- Retain build URL, job identity, commit, resolved config, native fingerprint, artifact digest, signature, symbols, source maps, and SBOM.

### 18.2 Credentials And Store Submission
- Inventory Android upload key, app-signing key ownership, keystore backups, certificate fingerprints, Apple distribution certificates, profiles, API keys, and roles.
- Use least privilege, short-lived credentials where possible, separation of duties, protected environments, audit logs, and emergency revocation.
- Verify package name, bundle ID, store application, signing lineage, version code, build number, track, phased release, and metadata before submission.
- Do not expose credentials in logs, artifacts, environment dumps, support bundles, pull requests, shell history, or generated configuration.
- Test replacement, expiration, revocation, team transfer, lost credential, and compromised credential procedures.
- Require explicit approval before submission, track promotion, phased rollout change, store listing change, or production release.

## 19. EAS Update And OTA Compatibility

### 19.1 Runtime Compatibility Contract
- Treat the native binary and JavaScript update as independently deployed artifacts joined only by an explicit runtime compatibility contract.
- Inventory runtimeVersion policy, native fingerprint inputs, update URL, request headers, channel, branch, platform, architecture, environment, and embedded update.
- Change runtime compatibility whenever native code, native configuration, Hermes compatibility, Codegen schema, native dependency, local schema, or privileged capability requires it.
- Test new update on every compatible native binary still in the field and prove incompatible binaries cannot receive it.
- Test old embedded update, latest update, rollback update, offline launch, failed download, corrupted asset, low storage, and repeated crash recovery.
- Do not use an OTA update for native breaking changes, signing changes, entitlement changes, permission declarations, store-policy changes, or irreversible data migration.

### 19.2 OTA Trust, Rollout, And Recovery
- Verify update manifest and asset authenticity, code-signing certificate configuration, private-key custody, key ID, rotation, revocation, and offline verification.
- Map channels to branches and environments explicitly; prevent preview, staging, test, tenant, or white-label updates from reaching production binaries.
- Use staged rollout with cohort size, guardrails, crash thresholds, launch thresholds, business metrics, pause, abort, and rollback authority.
- Retain update ID, group, channel, branch, runtimeVersion, commit, message, signer, manifest, assets, source maps, publication actor, and rollout history.
- Define automatic recovery from crash loops and prove fallback cannot reopen a data format that the failed update changed incompatibly.
- Exercise rollback, republish, channel remap, update disablement, emergency native release, and forward-fix procedures.

## 20. Performance, Memory, Battery, And Capacity

### 20.1 Measurement Contract
- Define budgets for cold start, warm start, time to interactive, navigation, input response, list scroll, animation, memory, bundle, binary, network, battery, and storage.
- Measure release builds on representative low, medium, and high capability physical devices with realistic data and network conditions.
- Separate JavaScript thread, UI thread, native module, render, GPU, I/O, network, database, image decode, and backend latency.
- Capture p50, p95, p99, maximum, variance, regression threshold, sample size, warmup, and environmental noise.
- Compare before and after every performance change and reject improvements that trade correctness, accessibility, memory, battery, or crash safety.
- Do not close a performance finding from simulator, debug, remote debugger, or microbenchmark evidence alone.

### 20.2 Startup, Lists, Animations, And Images
- Profile module initialization, native SDK startup, synchronous storage, font loading, asset loading, authentication bootstrap, navigation readiness, and first useful content.
- Audit FlatList, SectionList, VirtualizedList, FlashList, custom recyclers, item keys, estimated sizes, windows, clipping, pagination, and nested scrolling.
- Audit Reanimated, Gesture Handler, LayoutAnimation, native animations, shared values, worklets, UI-thread work, cancellation, and stale callbacks.
- Bound image dimensions, cache, prefetch, decode, transformations, animated images, thumbnails, placeholders, and full-resolution retention.
- Test rapid navigation, long lists, repeated media, orientation changes, fold/unfold, low memory, background-resume, and OTA reload.
- Use platform profilers and React Native DevTools together and retain traces linked to release identity.

### 20.3 Memory, Battery, Thermal, And Network Cost
- Measure JavaScript heap, native heap, graphics memory, image memory, database cache, socket buffers, and retained object graphs.
- Detect leaks from listeners, timers, closures, navigation, native modules, Fabric views, media, sensors, WebViews, SDKs, tasks, and caches.
- Audit wakeups, polling, reconnect loops, background location, push processing, animation, media, sync, and network batching for battery impact.
- Test low-memory warnings, memory pressure, thermal throttling, low-power mode, data saver, metered network, and constrained background execution.
- Set capacity and abuse limits for pagination, search, uploads, downloads, offline queues, notifications, media, maps, and realtime events.
- Tie technical resource use to user journey, device class, SLO, infrastructure cost, and store-quality metrics.

## 21. Accessibility, Adaptive UI, And Localization

### 21.1 Accessibility
- Test screen readers, focus order, labels, roles, states, hints, live regions, grouping, headings, modals, errors, and custom gestures.
- Test keyboard, switch control, external input, D-pad, pointer, TV focus, and hardware-key navigation where supported.
- Verify large text, font scaling, Dynamic Type, bold text, display zoom, contrast, color independence, reduced motion, transparency, and animation settings.
- Test loading, empty, offline, permission-denied, validation, partial failure, destructive confirmation, and success states.
- Ensure custom Fabric views, native views, charts, maps, media controls, and WebViews expose usable accessibility semantics.
- Use automated checks as a supplement to manual assistive-technology testing on both platforms.

### 21.2 Adaptive Layout And Localization
- Test supported phones, tablets, foldables, resizable windows, split screen, orientation, safe areas, keyboard, cutouts, and external displays.
- Use measured adaptive breakpoints and content priorities instead of device-name assumptions.
- Test LTR and RTL layout, bidirectional text, locale switching, long translations, plural rules, grammatical variants, and fallback locale.
- Audit date, time, calendar, timezone, number, currency, decimal precision, rounding, units, phone number, address, and sorting behavior.
- Verify persisted values are locale-independent and migrations do not reinterpret formatted display strings as canonical data.
- Test locale and timezone changes while the application is installed, backgrounded, offline, or running a long operation.

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

## 23. Observability, Crash, And Operational Readiness

### 23.1 Telemetry And Symbolication
- Correlate logs, traces, metrics, crash reports, ANRs, hangs, native crashes, JavaScript errors, network events, background work, and updates with one release identity.
- Upload and retain matching JavaScript source maps, Hermes maps, Android mapping, native symbols, dSYM, and build metadata securely.
- Redact tokens, credentials, personal data, message content, file paths, precise location, and sensitive identifiers before telemetry leaves the device.
- Define SLI and SLO for crash-free users, crash-free sessions, ANR or hang rate, startup, update success, critical journey success, sync freshness, and notification handling.
- Create alerts with threshold, window, cohort, severity, owner, runbook, suppression, and release or update correlation.
- Verify telemetry still works during partial backend outage, update failure, authentication failure, offline state, and crash-loop recovery without causing additional failure.

### 23.2 Runbooks And Supportability
- Provide runbooks for crash spike, ANR spike, update mismatch, signing failure, store rejection, push failure, auth outage, sync corruption, and compromised dependency.
- Define safe support diagnostics with user consent, redaction, bounded retention, version identity, and no secret exposure.
- Document how to identify installed native build, current update, channel, environment, account scope, device class, storage schema, and pending work.
- Provide kill switches for risky client features, background jobs, providers, native capabilities, and backend interactions where appropriate.
- Define customer communication, store review constraints, staged mitigation, data reconciliation, and evidence preservation.
- Exercise the runbooks and record gaps, owners, deadlines, and follow-up verification.

## 24. CI/CD, Provenance, Rollout, And Recovery

### 24.1 CI/CD Trust Boundaries
- Map repository permissions, branch protection, pull-request trust, fork behavior, workflow permissions, runners, caches, artifacts, OIDC, secrets, and deployment approvals.
- Prevent untrusted pull-request code from accessing signing credentials, update keys, production tokens, store APIs, private packages, or protected caches.
- Pin or verify actions, build images, package managers, toolchains, downloaded binaries, native dependencies, and remote scripts.
- Require clean checkout, immutable dependencies, tests, release builds, artifact inspection, SBOM, provenance, signatures, and approval gates.
- Separate build, signing, submission, OTA publication, channel mapping, and production rollout permissions.
- Retain immutable evidence linking actor, workflow, source, environment, artifact, signature, store submission, update publication, and rollout decision.

### 24.2 Rollout, Abort, Rollback, And Forward Fix
- Define rollout cohort, platform, device, OS, app version, native runtime, update channel, tenant, geography, feature flag, and monitoring window.
- Set quantitative guardrails for crash, ANR, startup, update success, critical journey, auth, sync, battery, backend errors, and support volume.
- Assign authority to pause, abort, roll back OTA, halt store rollout, disable feature, stop background work, revoke credential, and initiate incident mode.
- Separate JavaScript rollback, native binary rollback, configuration rollback, backend rollback, data rollback, reconciliation, and forward repair.
- Prove old and new binaries, old and new updates, old and new backend contracts, and old and new local schemas can coexist for the required window.
- Never label rollback ready until it has been exercised with representative data, installed versions, channels, and failure states.

### 24.3 Backup, Restore, And Incident Recovery
- Inventory recoverable server data, client data, update metadata, symbols, source maps, signing records, store records, configuration, and audit evidence.
- Define RPO and RTO per critical journey and verify them with isolated restore and reconciliation exercises.
- Test recovery from corrupted local data, bad OTA, bad native release, lost signing credential, revoked certificate, backend restore, and incompatible schema.
- Preserve forensic evidence before deleting caches, uninstalling, republishing, rotating keys, rebuilding, or restoring.
- For supply-chain compromise rebuild from trusted source, clean runners, verified dependencies, newly issued credentials, and reviewed artifacts.
- Document containment, eradication, recovery, user impact, notification obligations, residual risk, and recurrence prevention.

## 25. Migration Overlays

### 25.1 React Native And Expo Upgrade
- Upgrade supported framework and Expo SDK versions incrementally unless evidence justifies a different sequence.
- Before each step freeze baseline behavior, critical journey tests, release artifacts, symbols, source maps, store state, update state, and rollback path.
- Compare native templates, config plugins, generated projects, build tools, permission declarations, lifecycle, Hermes, Metro, Codegen, and third-party support.
- Test release binaries and OTA compatibility at every step; do not rely on Expo Doctor or successful compilation alone.
- Track deprecated APIs, removed behavior, support windows, store requirements, minimum OS changes, and native library replacements.
- Roll out each step independently with telemetry, guardrails, abort, rollback, and retained evidence.

### 25.2 New Architecture And Expo Adoption
- Inventory unsupported libraries, custom native modules, view managers, JSI code, brownfield surfaces, build scripts, and native patches before migration.
- Migrate one boundary at a time with schema, threading, lifecycle, memory, error, and compatibility tests.
- When adopting Expo or CNG define native project ownership, config-plugin coverage, regeneration rules, development-build strategy, EAS linkage, and escape path.
- Do not erase working native behavior with prebuild cleanup until every manual change has an authoritative config-plugin or documented ownership strategy.
- Validate library maintainers, fork plans, patch ownership, future framework support, and rollback from partially migrated state.
- Retire compatibility code only after production evidence proves the replacement across supported platforms and versions.

## 26. Mandatory Evidence Matrices
Complete every applicable matrix. A blank cell is not a pass; mark it NOT_APPLICABLE with rationale or UNVERIFIED with the exact blocker.
1. M1 - Source, toolchain, generated project, artifact, installed runtime, and telemetry identity.
2. M2 - Workflow, application, brand, tenant, environment, channel, branch, platform, architecture, and store mapping.
3. M3 - React Native, Expo SDK, React, Hermes, Metro, Router, Node, package manager, Android, Apple, and native dependency compatibility.
4. M4 - Expo config, config plugins, prebuild ownership, generated files, manual native changes, and regeneration safety.
5. M5 - New Architecture, Codegen, TurboModules, Fabric, Expo Modules, legacy interop, JSI, thread, memory, and ABI boundaries.
6. M6 - Critical journeys, invariants, state ownership, authorization, tenant isolation, idempotency, offline behavior, and reconciliation.
7. M7 - Storage, schema, migration, encryption, backup, restore, account switch, reinstall, and deletion behavior.
8. M8 - Network, realtime, push, background tasks, permissions, devices, files, media, and WebView contracts.
9. M9 - Android version, device, ABI, signing, manifest, release artifact, install, upgrade, performance, accessibility, and recovery.
10. M10 - Apple version, device, signing, entitlement, privacy, archive, install, upgrade, performance, accessibility, and recovery.
11. M11 - EAS build profile, credential, native fingerprint, runtimeVersion, update channel, signer, rollout, rollback, and source-map linkage.
12. M12 - CI/CD trust, SBOM, provenance, artifact promotion, store submission, SLO, incident, restore, RPO, RTO, and trusted rebuild.

## 27. Mandatory Adversarial And Failure Scenarios
1. S1 - Two rapid user actions initiate the same privileged or financial mutation.
2. S2 - A response completes after navigation, logout, tenant switch, item replacement, or view destruction.
3. S3 - The app dies before request send, during transfer, after server commit, and before local acknowledgement.
4. S4 - Old binary receives new JavaScript, new binary starts with old embedded JavaScript, and rollback follows local migration.
5. S5 - OTA download is interrupted, corrupted, out of storage, signature-invalid, channel-mismatched, or crash-looping.
6. S6 - Account or tenant switches while cached data, offline commands, streams, notifications, and background work remain active.
7. S7 - Deep link or notification targets a removed, unauthorized, stale, cross-tenant, or malformed resource.
8. S8 - Token refresh, logout, revocation, key rollover, network retry, and multiple parallel requests race.
9. S9 - Native callback arrives after React instance reload, activity recreation, view-controller replacement, or Fabric view recycling.
10. S10 - JSI or native code receives malformed, oversized, misaligned, stale, duplicated, or concurrently accessed data.
11. S11 - Background task, push action, media event, or location event executes with old code, expired credentials, or changed schema.
12. S12 - Network is slow, captive, metered, switching, offline, TLS-rotated, partially failing, or returning incompatible data.
13. S13 - Local database migration is interrupted, storage is full, data is corrupted, backup is restored, or two app versions access the state.
14. S14 - Permission changes in settings, is limited, becomes permanently denied, or is revoked while a resource is active.
15. S15 - App is backgrounded, suspended, killed, restored, upgraded, or rebooted during each critical operation.
16. S16 - Low memory, thermal pressure, low battery, low storage, slow device, long list, large image, and repeated navigation coincide.
17. S17 - Malicious file, archive, image, media, PDF, URL, WebView page, bridge message, or native intent is processed.
18. S18 - Signing credential, update key, CI runner, dependency, config plugin, native SDK, or build image is compromised.
19. S19 - Store rollout, OTA rollout, backend rollout, local migration, and feature flag overlap in incompatible order.
20. S20 - Production rollback and isolated restore are executed after real data, queue, update, and schema changes.

## 28. Severity And Production Decision
| Level | Definition | Release effect |
| --- | --- | --- |
| P0 | Active compromise, severe data integrity loss, unsafe signing or update path, mass cross-tenant exposure, unrecoverable critical failure, or immediate user safety risk. | Stop release or enter incident mode immediately. |
| P1 | Likely critical security, privacy, financial, availability, store, migration, or rollback failure with material impact. | Block release until fixed or formally contained with approved evidence. |
| P2 | Material defect, unsupported configuration, performance, accessibility, observability, or operational weakness. | Fix before broad rollout or accept with owner, deadline, compensating control, and monitoring. |
| P3 | Limited improvement, maintainability issue, optimization, documentation gap, or optional modernization. | Prioritize by value and risk; does not alone block release. |

Final decision must be exactly one of: READY, READY_WITH_CONDITIONS, NOT_READY, or INCIDENT.

## 29. Safe Repair And Verification Workflow
1. Protect workspace, credentials, signing material, update keys, stores, production state, local data, and forensic evidence.
2. Confirm scope, workflow, platforms, identities, environments, critical journeys, support claims, authorization, and evidence ceiling.
3. Inventory source, dependencies, generated projects, native code, services, stores, update paths, signing, distribution, telemetry, and recovery.
4. Reproduce a clean baseline and build the source-to-runtime identity chain before broad changes.
5. Create finding and evidence matrices before modification; distinguish confirmed defects from hypotheses.
6. Reproduce each critical finding with the smallest targeted test and retain pre-fix evidence.
7. Implement the smallest authorized reversible fix without unrelated cleanup or broad upgrade.
8. Add regression, negative, concurrency, lifecycle, migration, release, update, rollback, and recovery coverage appropriate to the mechanism.
9. Run clean analysis, tests, generated-project checks, native builds, artifact inspection, install, physical-device matrix, and operational checks.
10. Verify symbols, source maps, telemetry, rollout, abort, rollback, restore, and incident procedures before the final decision.
11. Reconcile every claim with evidence and downgrade unsupported certainty to UNVERIFIED.
12. Issue the final report with blockers, conditions, residual risk, owners, deadlines, and exact next verification steps.

## 30. Production Readiness Checklist
- [ ] Authorization, scope, support claims, and evidence ceiling are recorded.
- [ ] Source-to-runtime identity is complete for every production artifact and OTA update.
- [ ] Toolchains, dependency graphs, generated projects, and native projects are reproducible and reviewed.
- [ ] New Architecture, Codegen, native modules, Fabric, JSI, ABI, and memory boundaries are verified.
- [ ] Critical journeys, invariants, authorization, tenant isolation, idempotency, and reconciliation pass.
- [ ] Storage, offline, migration, backup, restore, account switch, and deletion behavior pass.
- [ ] Network, realtime, background, push, permissions, device, file, media, and WebView contracts pass.
- [ ] Android release build, artifact inspection, signing, installation, upgrade, device, performance, accessibility, and recovery pass.
- [ ] Apple archive, signing, privacy, installation, upgrade, device, performance, accessibility, and recovery pass.
- [ ] EAS build profiles, credentials, environment, update runtime, code signing, channels, and rollout are verified.
- [ ] Crash, ANR, hang, source-map, native-symbol, SLI, alert, dashboard, and runbook readiness pass.
- [ ] CI/CD trust, SBOM, provenance, immutable artifact promotion, store submission, and approval gates pass.
- [ ] Staged rollout, quantitative abort criteria, OTA rollback, native rollback, forward fix, and kill switches are exercised.
- [ ] Isolated restore, RPO, RTO, data reconciliation, incident containment, credential revocation, and trusted rebuild are exercised.
- [ ] All P0 and P1 findings are closed or the decision is NOT_READY or INCIDENT.
- [ ] Every accepted P2 or P3 risk has owner, deadline, compensating control, monitoring, and next verification date.

## 31. Definition Of Done
- [ ] The audited repository, commit, environment, workflow, application IDs, native fingerprints, artifacts, update IDs, devices, and evidence locations are identified.
- [ ] Every relevant claim is supported at the stated E0-E5 evidence level.
- [ ] The EN and SR prompt structure is aligned and no platform or workflow is silently omitted.
- [ ] Confirmed root causes are separated from symptoms, hypotheses, and unrelated cleanup.
- [ ] Implemented changes are minimal, authorized, reviewable, reversible, and linked to findings.
- [ ] Regression, negative, concurrency, lifecycle, migration, release, OTA, rollback, and restore tests cover the changed mechanism.
- [ ] Release artifacts are inspected, signed, installed, launched, exercised, symbolicated, and linked to telemetry.
- [ ] Production rollout, abort, rollback or forward-fix, restore, and incident procedures are executable by named owners.
- [ ] Skipped checks and inaccessible systems are reported as UNVERIFIED with impact and blocker.
- [ ] Residual risks, accepted exceptions, compensating controls, expiry, owners, dependencies, and next verification dates are explicit.
- [ ] The final decision follows the severity model and is not contradicted by unresolved evidence.
- [ ] The final report contains enough commands, hashes, matrices, and evidence references for an independent reviewer to reproduce the conclusion.

## 32. Forbidden Shortcuts
- Do not claim production readiness from Expo Go, Metro, simulator, emulator, debug build, typecheck, lint, Expo Doctor, or a green cloud build alone.
- Do not delete lockfiles, native projects, generated files, caches, local data, signing records, symbols, or forensic evidence to make the build pass.
- Do not run broad dependency upgrades, automated fix commands, clean prebuild, pod update, Gradle version change, or framework migration without review and rollback.
- Do not publish OTA, submit to stores, promote tracks, change channels, rotate keys, revoke credentials, or modify production data without explicit approval.
- Do not suppress crashes, ANRs, warnings, permission errors, migration failures, update failures, or failing tests instead of fixing root cause.
- Do not treat client-side validation, hidden UI, biometrics, root detection, certificate pinning, or TypeScript types as complete authorization.
- Do not use mutable tags, undocumented local patches, unreviewed config plugins, unsigned updates, or unverifiable artifacts for production.
- Do not declare rollback ready when data, native runtime, backend contract, local schema, or update compatibility prevents it.
- Do not generalize Android evidence to Apple, Apple evidence to Android, one device to all devices, or one workflow to all workflows.
- Do not invent command output, device behavior, store state, telemetry, signatures, credentials, rollout status, restore result, or certainty.

## 33. Final Report Format
1. Executive summary and final decision: READY, READY_WITH_CONDITIONS, NOT_READY, or INCIDENT.
2. Audit scope, authorization, exclusions, evidence ceiling, inaccessible systems, and exact date.
3. Product map: workflows, apps, platforms, environments, tenants, identities, critical journeys, stores, services, and owners.
4. Source-to-runtime identity, reproducibility, generated-project ownership, artifact, signing, store, update, and telemetry results.
5. P0-P3 finding register ordered by severity and dependency with evidence, root cause, impact, scope, fix, verification, rollback, and residual risk.
6. Implemented changes with file and symbol scope, reason, risk, artifact impact, tests, and rollback.
7. Evidence matrix and adversarial-scenario results including skipped cells and exact blockers.
8. Per-platform release, install, signing, permissions, performance, accessibility, update, store, and recovery status.
9. Observability, SLO, rollout, abort, rollback or forward-fix, restore, incident, credential revocation, and trusted-rebuild readiness.
10. Residual risks, accepted exceptions, compensating controls, owners, deadlines, dependencies, monitoring, and next verification dates.
11. Prioritized roadmap: immediate containment, release blockers, short-term remediation, medium-term hardening, and optional modernization.
12. Appendix with commands, environment, sources, hashes, signatures, manifests, symbols, source maps, matrices, measurements, logs, and evidence locations.

## 34. Authoritative Baseline Sources
- React Native releases, support policy, upgrade guidance, architecture, Hermes, Metro, performance, security, accessibility, and platform documentation.
- Expo SDK reference, upgrade guide, development builds, CNG, prebuild, config plugins, Expo Modules, EAS Build, Submit, Update, runtime versions, fingerprints, and code signing.
- Android Developers and Google Play documentation for SDK levels, app bundles, signing, permissions, background work, privacy, quality, 16 KB pages, and store policy.
- Apple Developer and App Store documentation for Xcode, signing, entitlements, privacy manifests, required-reason APIs, background execution, accessibility, TestFlight, and review.
- React, TypeScript, package-manager, native dependency, security advisory, OWASP MASVS, and backend contract documentation applicable to the project.
- Re-check current official sources on the audit date and record exact versions, publication dates, support status, and retrieved references.

## 35. Mandatory Work Order
1. Protect workspace, credentials, signing, update keys, data, stores, and evidence.
2. Confirm scope, workflow, platforms, critical journeys, authorization, support claims, and evidence ceiling.
3. Inventory source, dependencies, generated native projects, architecture, services, stores, devices, distribution, update paths, and owners.
4. Resolve toolchains and reproduce the clean baseline without destructive cleanup.
5. Build the source-to-runtime identity chain and identify drift before modification.
6. Audit domain, state, lifecycle, concurrency, New Architecture, native boundaries, security, storage, network, background work, and platform behavior.
7. Create findings and evidence matrices, reproduce confirmed defects, and retain pre-fix evidence.
8. Implement the smallest authorized reversible fixes with focused regression and adversarial coverage.
9. Run clean tests, native release builds, artifact inspection, physical-device matrices, install, upgrade, OTA, performance, accessibility, rollback, and restore checks.
10. Verify signing, provenance, symbols, source maps, telemetry, rollout gates, runbooks, credentials, store state, and incident recovery.
11. Reconcile all claims with evidence, state residual risk honestly, and issue the final production decision.

## 36. Final Instruction
Do not merely review JavaScript or make the application compile. Prove the real React Native and Expo product across source, generated native projects, New Architecture, native modules, JSI and ABI boundaries, backend contracts, local data, signed release artifacts, physical devices, stores, OTA channels, telemetry, rollout, rollback, restore, and incident recovery. Work evidence-first, preserve safety, make only authorized reversible changes, and never claim more certainty than the available evidence supports.
