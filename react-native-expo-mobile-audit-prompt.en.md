# MASTER PROMPT - Deep Production Audit, Repair, And Improvement Of A React Native / Expo Application

## Research Baseline - 4 August 2026

This baseline is a starting point. Re-check reactnative.dev, docs.expo.dev, EAS docs and real lock/native configuration before recommendations.

| Component | Confirmed status on 4 August 2026 | Mandatory audit check |
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

## Severity

| P | Definition |
| --- | --- |
| P0 | Auth/token leak, RCE via native/WebView, malicious/unsigned OTA, data loss, signing key leak, store-blocking crash. |
| P1 | OTA/runtimeVersion mismatch crash, insecure token storage, deep-link hijack, New Arch native crash, broken offline integrity, 16 KB reject. |
| P2 | Measured jank/startup, a11y, weak symbols, capacity. |
| P3 | Docs, style, DX. |

## Production Checklist

1. RN/Expo/Node alignment. 2. Frozen lock + audit. 3. expo-doctor clean or triaged. 4. New Arch + Hermes confirmed in release. 5. Typecheck/lint/test. 6. Release Android+iOS builds. 7. Secure tokens. 8. No server secrets in bundle. 9. Native modules stable. 10. runtimeVersion policy. 11. OTA signed + staging. 12. 16 KB where needed. 13. Symbol maps. 14. Signing isolated. 15. Rollout/rollback documented.

## Definition Of Done

Model/platforms; versions/matrix; New Arch/Hermes; deps; baseline doctor/tsc/test/build; architecture/state; nav/lifecycle; async/background/push; native/Expo Modules/JSI; auth/security; local data; permissions/links/WebView; Android+iOS; perf measured or UNVERIFIED; EAS/OTA trust; crash/symbols; P0/P1; regression tests; production binary; rollout/abort/rollback; command log; unverified listed; no false ready claims.

If not: **The React Native application is not yet fully production-ready.**

## Forbidden

Invent output/CVEs; hide platform failures; delete lock; broad upgrades; manual Expo packages off-matrix; prebuild --clean without protection; New Arch permanently off; `any` as a mask; ignore hooks without analysis; leak listeners; JS timer as background scheduler; refresh tokens in AsyncStorage without a threat model; server secrets in JS; UI = authz; disable TLS; generic WebView/native bridges; deep links/notifications without validation; delete user DB; irreversible migration without recovery; native break + OTA only; same runtimeVersion for incompatible native; unsigned OTA; OTA private key in repo; signing/OTA creds on PRs; Expo Go = prod; emulator = device; optimize without release measurement; declare perfect.

## Final Report

1. Summary + verdict. 2. Workflow/platforms. 3. Version matrix. 4. New Arch/Hermes/Codegen. 5. Architecture/state. 6. Nav/lifecycle/async/background. 7. Native/Expo Modules/JSI. 8. Auth/security. 9. Local data/offline. 10. Permissions/links/WebView. 11. Android/iOS. 12. Perf/a11y. 13. EAS/OTA/signing. 14. Crash/symbols. 15. Findings P0–P3. 16. Changes+tests. 17. Command log. 18. Rollout/rollback (binary vs OTA). 19. Blockers. 20. Sources (URL, date).

## Work Order

protect (+creds) → bare/Expo/brownfield paths → toolchain baseline → deps → doctor/tsc/lint/test/build → architecture → New Arch/Hermes/Metro/Codegen → nav/lifecycle → async/background/push → native modules → auth/security → storage/offline → permissions/links/WebView → Android → iOS → perf → EAS/OTA → observability → findings → fixes → platform tests → production build/signing → staged rollout/abort/rollback → report.

Priorities: users/data; auth/tokens; native+OTA trust; functional/platform correctness; local-data; background/push; New Arch stability; store/signing; measured perf; a11y/maintainability.
