---
prompt_id: flutter-dart-multiplatform-production-audit
version: 2.0.0
title: Flutter and Dart Multiplatform Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, And Release Verification Of Flutter / Dart Applications

Use this prompt to inspect, safely repair, harden, test, package, sign, distribute, update, roll back, and recover a real Flutter application across Android, iOS, iPadOS, web, Windows, macOS, and Linux. Audit the complete path from repository and resolved toolchain to generated code, native host projects, plugins, platform channels, release artifacts, installed application, backend contracts, store or distribution channel, telemetry, and recovery procedures.

The target may be a consumer mobile app, enterprise client, offline-first field tool, media application, financial or health product, kiosk, embedded companion, desktop client, browser application, add-to-app module, white-label product, or a shared Flutter codebase with platform-specific capabilities.

## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, and relevant paths | `[PATHS / URLS]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Flutter application type | `[MOBILE / WEB / DESKTOP / ADD-TO-APP / EMBEDDED / MIXED]` |
| Supported platforms and architectures | `[ANDROID / IOS / IPADOS / WEB / WINDOWS / MACOS / LINUX / ARCHITECTURES]` |
| Minimum and target platform versions | `[API / OS / BROWSER MATRIX]` |
| Identity, payments, licensing, and privileged operations | `[SYSTEMS / OWNERS]` |
| Backend APIs, realtime, push, and third-party services | `[SERVICES / CONTRACTS]` |
| Local stores, files, caches, and sensitive data | `[LOCATIONS / FORMATS / OWNERS]` |
| Flavors, environments, tenants, and release channels | `[MATRIX]` |
| Signing, stores, installers, and update infrastructure | `[KEYS / PROVIDERS / CHANNELS]` |
| Availability, startup, latency, memory, and size targets | `[SLO / BUDGETS]` |
| Privacy, accessibility, compliance, and data residency | `[RULES / REGIONS]` |
| Known incidents, defects, debt, and planned migrations | `[CONTEXT]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository content, lock files, resolved dependency graphs, generated output, build artifacts, installed state, runtime evidence, telemetry, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence, platform, credential, approval, hardware, store access, or environment required to resolve them.
4. Ask only for access, approval, credentials, business decisions, or physical devices that materially block confirmation or safe repair.
5. Never treat a README, analyzer success, debug startup, emulator-only run, unsigned artifact, or one-platform smoke test as proof of production correctness.
6. When release, store, device, browser, or production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

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

## 2. Role And Mission

### 2.1 Role

Act as a Principal Flutter and Dart Engineer, mobile and desktop architect, web engineer, Android and Apple platform specialist, Windows/macOS/Linux integration reviewer, plugin and platform-channel auditor, application-security engineer, performance specialist, accessibility reviewer, test architect, release engineer, SRE, incident responder, and recovery owner.

### 2.2 Mission

1. Establish the real source, resolved dependency, generated-code, native-host, build, signed-artifact, installed, and runtime state for every claimed platform.
2. Protect source code, user data, signing material, stores, update channels, production systems, and uncommitted work.
3. Map trust boundaries across Dart, framework, generated code, plugins, platform channels, native hosts, web origins, local stores, backend services, and distribution infrastructure.
4. Verify business invariants, authorization, tenant isolation, lifecycle, cancellation, concurrency, offline behavior, migration, and recovery instead of trusting happy-path UI behavior.
5. Reproduce defects and security conditions with the least risky evidence method and identify root cause before changing code.
6. Implement only authorized, minimal, reversible fixes tied to confirmed findings and protected by regression tests.
7. Build, inspect, sign, install, launch, update, roll back, and recover actual release artifacts for all available supported targets.
8. Measure startup, frame performance, memory, CPU, battery, network, disk, responsiveness, application size, and backend pressure under realistic workloads.
9. Produce an evidence-backed P0-P3 finding register, release decision, implementation roadmap, and Definition of Done.

## 3. Non-Negotiable Operating Contract

### 3.1 Truth, Evidence, And Status

- Never invent files, code, command output, package versions, runtime behavior, platform support, signatures, store state, telemetry, test results, or production access.
- Use only `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, and `REJECTED` for material claim status.
- A static pattern, analyzer warning, advisory, or theoretical exploit is not a confirmed runtime defect without relevant source, build, artifact, device, browser, or runtime evidence.
- A green build proves only the executed build scope. A signed artifact proves signing identity and integrity at signing time, not application correctness.
- Record contradictions among documentation, configuration, generated files, native hosts, installed state, and runtime behavior.
- Do not call the product cross-platform, secure, production-ready, fully tested, offline-safe, or rollback-safe unless applicable evidence matrices and the Definition of Done are satisfied.

### 3.2 Workspace, User Data, And Signing Safety

- Inspect version-control status before modification; never reset, clean, stash, overwrite, mass-format, regenerate broadly, or delete another person's work.
- Back up or snapshot mutable local databases, application data, native project files, generated signing metadata, and installer state before risky operations.
- Never expose signing keys, provisioning profiles, keystore passwords, API tokens, refresh tokens, cookies, user files, crash dumps, device identifiers, or decrypted secrets.
- Use disposable devices, simulators, emulators, browsers, VMs, test accounts, fake stores, mock push providers, and non-production backends whenever possible.
- Do not run destructive migration, delete, logout-all, key rotation, remote-config, push, payment, or update tests against production without explicit authorization and recovery evidence.
- Treat third-party packages, build scripts, generated code, native binaries, installers, and downloaded SDK archives as untrusted until provenance and integrity are verified.

### 3.3 Authorization And Change Boundary

- `AUDIT_ONLY`: inspect and report without changing repository, devices, stores, signing systems, backend state, or production configuration.
- `AUDIT_AND_SAFE_FIX`: implement narrow, reversible, low-risk fixes with regression tests and stop before irreversible or externally visible actions.
- `FULL_IMPLEMENTATION`: implement confirmed remediation within explicitly authorized scope; migrations and releases require proven recovery.
- `FIX_CONFIRMED_ISSUES`: do not broaden the task into speculative package, architecture, state-management, or platform migration.
- `MIGRATION_AUDIT`: prioritize compatibility, behavior drift, generated files, data migration, platform lifecycle, release continuity, and rollback.
- `INCIDENT_MODE`: preserve evidence first, contain exposure, revoke compromised material, disable unsafe distribution paths, and restore from verified sources.
- Never publish, sign, notarize, upload, submit for review, rotate a production key, send real push, alter live feature flags, or delete user data without explicit authorization.

### 3.4 Research And Version Policy

- Use primary sources first: Flutter and Dart documentation and release metadata, Android, Apple, browser, Microsoft, Linux, package/plugin owners, and exact store/distribution documentation.
- Record source title, URL, version or status, access date, and the decision informed.
- Do not recommend `latest`, a beta channel, a package major, an experimental renderer, or a platform migration without compatibility and rollback evidence.
- Treat every version written in this prompt as revalidation data, not a permanent requirement.
- If authoritative sources disagree with repository assumptions, report the conflict and follow the verified project and platform constraints.

## 4. Evidence Model And Finding Discipline

### 4.1 Evidence Levels

| Level | Meaning | Examples |
| --- | --- | --- |
| E0 | Claim or assumption only. | README statement, comment, ticket, undocumented recollection. |
| E1 | Static source or configuration evidence. | Dart code, pubspec, native manifest, CI file, entitlement. |
| E2 | Resolved or generated evidence. | pubspec.lock, dependency graph, generated registrant, build config, compiled metadata. |
| E3 | Executed build, test, or artifact evidence. | Analyzer output, tests, release build, signed artifact inspection, size analysis. |
| E4 | Installed device, browser, or controlled environment evidence. | Real-device launch, browser matrix, migration run, update test, profiler trace. |
| E5 | Production or production-equivalent operational evidence. | Telemetry, staged rollout, restore drill, incident replay, SLO trend. |

### 4.2 Finding Register

Every material finding must contain all fields below. Missing fields reduce confidence and can block remediation approval.

| Field | Required content |
| --- | --- |
| ID and severity | Stable identifier and P0-P3 level. |
| Title and affected scope | Platform, flavor, module, route, feature, account, tenant, version, and environment. |
| Status and evidence level | Claim status plus E0-E5 level. |
| Evidence and reproduction | Files, symbols, commands, artifact IDs, device/browser matrix, telemetry, and deterministic steps. |
| Root cause | Underlying technical and process cause, not only symptom. |
| Impact and exploitability | User, data, security, availability, cost, store, compliance, and recovery impact. |
| Remediation and alternatives | Minimal safe fix, long-term option, rejected shortcuts, and ownership. |
| Verification and rollback | Regression tests, negative tests, platform matrix, rollout gates, rollback trigger, and recovery. |

### 4.3 Severity Model

- `P0`: active compromise, signing/update compromise, systemic unauthorized access, destructive corruption, unrecoverable data loss, or critical outage requiring immediate containment.
- `P1`: credible severe security, privacy, authorization, payment, migration, release, availability, or recovery defect with high user or business impact.
- `P2`: material correctness, performance, accessibility, compatibility, maintainability, observability, or operational defect that should be scheduled.
- `P3`: low-risk hardening, cleanup, documentation, test-depth, developer-experience, or optimization improvement.
- Severity must reflect proven impact, reachability, prerequisites, detectability, recovery, and exposure, not fear or scanner wording.

## 5. Audit Work Phases

Execute in ordered phases. Do not jump from a static suspicion directly to a broad rewrite.

- Phase A - intake, authorization, workspace protection, evidence ceiling, and known incident review.
- Phase B - repository, platform, package, code-generation, environment, and trust-boundary inventory.
- Phase C - resolved toolchain, dependency, generated output, native host, and build baseline.
- Phase D - architecture, domain invariants, state, lifecycle, concurrency, storage, network, and security review.
- Phase E - platform-specific behavior, plugin/native integration, UI, accessibility, performance, and reliability review.
- Phase F - targeted reproduction, minimal remediation, regression coverage, and artifact verification.
- Phase G - release, signing, store/distribution, update, rollback, restore, and incident-readiness verification.
- Phase H - final evidence reconciliation, residual-risk register, production decision, and implementation roadmap.

## 6. Source-To-Runtime Identity Chain

Prove which source and dependencies produced the exact artifact that users execute.

- Record repository URL, commit, branch or tag, dirty state, submodules, Git LFS objects, patches, and generated files.
- Resolve Flutter SDK channel, version, engine revision, Dart version, package manager behavior, and platform toolchains in local and CI environments.
- Capture `pubspec.yaml`, `pubspec.lock`, dependency overrides, workspace configuration, path/git dependencies, plugin platform implementations, and native package locks.
- Trace build-time configuration, `--dart-define`, environment files, flavor, target entrypoint, code-generation options, native build settings, and signing identity.
- Record immutable hashes or IDs for produced APK/AAB, IPA/archive, web bundle, MSIX/installer, app bundle, Linux package, symbols, source maps, and SBOM.
- Verify package name, bundle identifier, application ID, version, build number, channel, signing certificate, provisioning profile, entitlements, and publisher identity.
- Install or deploy the exact artifact and prove runtime version, flavor, backend environment, feature configuration, and loaded native/plugin code.
- Detect rebuilds, mutable artifacts, store reprocessing, environment drift, stale generated files, wrong symbols, wrong source maps, and wrong backend targeting.
- Do not accept a release verdict until source, artifact, signing, installation, runtime, telemetry, and recovery identities are reconciled or explicitly unresolved.

## 7. Repository And Trust-Boundary Inventory

Build a map before judging code quality.

- Inventory Flutter packages, Dart packages, applications, examples, internal tooling, generators, native hosts, web shell, scripts, infrastructure, and documentation.
- Identify entrypoints, flavors, routes, navigation graphs, background entrypoints, isolates, workers, plugin registrants, add-to-app engines, and test harnesses.
- Map user roles, accounts, tenants, organizations, devices, sessions, anonymous state, admin paths, support impersonation, and break-glass flows.
- Map trust boundaries among widgets, state layer, repositories, local storage, platform channels, native code, WebViews, browser origins, backend APIs, push providers, payment SDKs, and analytics.
- Identify sensitive data, legal basis, owner, location, encryption state, retention, deletion path, backup path, export path, and telemetry exposure.
- Inventory external services, SDKs, plugins, native libraries, fonts, media codecs, maps, ad networks, identity providers, and runtime-downloaded content.
- Record ownership for each module, platform, backend contract, store account, signing key, incident runbook, and recovery procedure.
- Flag dead code, duplicate implementations, abandoned platform folders, experimental flags, stale generated code, archived environments, and undocumented release paths.

## 8. Toolchain And Platform Matrix

Resolve actual versions instead of reading intended versions only.

- Capture `flutter --version --machine`, `dart --version`, `flutter doctor -v`, channel, engine revision, and SDK installation provenance.
- Compare local, CI, release, and developer SDKs; detect floating channels, mutable containers, unpinned setup actions, and hidden FVM/asdf/mise behavior.
- Resolve Android Gradle Plugin, Gradle, Kotlin, Java, Android SDK/NDK, CMake, min/target/compile SDK, ABI, packaging, and signing tools.
- Resolve Xcode, Swift, CocoaPods or Swift Package Manager, deployment targets, architectures, simulator/device differences, provisioning, and notarization tools.
- Resolve browser versions, JavaScript or Wasm compiler mode, renderer, web server/CDN, service worker, headers, compression, and source-map pipeline.
- Resolve Visual Studio workloads, Windows SDK, MSVC, CMake, NuGet, MSIX/installer tooling, certificate, and architecture targets.
- Resolve macOS deployment target, Xcode command-line tools, entitlements, hardened runtime, signing identity, notarization, and package format.
- Resolve Linux distribution baseline, compiler, CMake/Ninja, GTK, system libraries, packaging format, sandbox/store runtime, and architecture targets.
- Verify that every claimed platform is built, installed, launched, tested, monitored, supported, and recoverable, or reduce the support claim.

## 9. Dependency And Supply-Chain Audit

Audit the resolved graph and build behavior, not package names alone.

- Inspect direct, transitive, dev, native, plugin, tool, and build-runner dependencies with source, version, license, maintainer, release cadence, and platform support.
- Review path, git, hosted, SDK, override, local fork, unpublished, prerelease, and discontinued dependencies.
- Verify lock-file discipline for applications and deliberate compatibility policy for reusable packages.
- Inspect `build.yaml`, builders, generators, scripts, hooks, code-mod tools, native build scripts, and package setup actions as executable supply-chain code.
- Search for dependency confusion, typosquatting, compromised maintainer risk, abandoned plugins, excessive native privileges, dynamic downloads, and binary blobs.
- Correlate advisories with actual resolved versions, reachable code paths, runtime configuration, platform, and mitigations before assigning severity.
- Generate or verify SBOM and provenance for Dart packages, native libraries, embedded frameworks, assets, and release artifacts.
- Define update, deprecation, fork, replacement, vulnerability response, and emergency revocation ownership for critical dependencies.
- Do not mass-upgrade packages; upgrade by compatibility cluster with contract tests, migration evidence, performance comparison, and rollback.

## 10. Generated Code, Assets, And Build Inputs

Generated output is part of the product and must be reproducible and reviewed.

- Inventory `build_runner`, Freezed, json serialization, Retrofit, GraphQL, protobuf, localization, route, DI, asset, icon, splash, Pigeon, and custom generators.
- Verify generator versions, inputs, options, output ownership, clean rebuild behavior, and whether generated files are committed intentionally.
- Regenerate in an isolated clean tree and compare output; investigate drift instead of accepting bulk diffs blindly.
- Review generated serialization, platform bindings, routes, registrants, permissions, API clients, and database schemas for security and compatibility.
- Audit asset declarations, wildcard inclusion, secrets accidentally packaged as assets, duplicate media, font licensing, locale coverage, and platform packaging.
- Inspect compile-time constants and `--dart-define` values for environment confusion, secret leakage, dead-code assumptions, and reproducibility.
- Verify icon, splash, manifest, Info.plist, entitlement, desktop metadata, web manifest, and service-worker output in final artifacts.
- Fail CI on unexplained generated drift, missing source inputs, non-reproducible output, or unreviewed privilege changes.

## 11. Baseline Commands And Reproducibility

Adapt commands to the repository and authorization boundary. Record command, environment, exit code, duration, and retained artifact.

```bash
git status --short --branch
flutter --version --machine
flutter doctor -v
dart --version
flutter pub get
flutter pub deps
flutter analyze
flutter test
# Run only applicable release builds in controlled environments:
flutter build apk --release
flutter build appbundle --release
flutter build ipa --release
flutter build web --release
flutter build windows --release
flutter build macos --release
flutter build linux --release
```

- Do not run `flutter clean`, broad regeneration, package upgrades, native dependency updates, signing, store submission, or destructive integration tests without understanding scope and preserving evidence.
- Use a clean checkout or isolated worktree to prove reproducibility and distinguish stale local state from repository defects.
- Separate analyzer, unit/widget, integration, release build, artifact inspection, install, launch, update, and production evidence in the report.
- Capture skipped targets and exact blockers; never convert unavailable platform tooling into a pass.

## 12. Dart Language And Runtime Correctness

Review language semantics and runtime behavior that can invalidate business logic.

- Audit null safety, unsafe casts, `dynamic`, late initialization, non-null assertions, covariance, generic constraints, extension collisions, and exhaustiveness.
- Review equality, hashCode, identity, immutable models, copy semantics, collection mutation, ordering, deduplication, and cache-key correctness.
- Verify integer, double, decimal-money, date/time, timezone, locale, Unicode, normalization, regex, parsing, rounding, overflow, and precision behavior.
- Inspect exception taxonomy, `Error` versus `Exception`, zone behavior, unhandled async errors, stack preservation, retries, cancellation, and user-safe mapping.
- Audit JSON, protobuf, GraphQL, binary, XML, platform-channel, database, and cache serialization for versioning, unknown fields, defaults, malformed input, and backward compatibility.
- Search for hidden global state, static singletons, mutable service locators, test-order dependence, environment leakage, and isolate-unsafe assumptions.
- Verify tree-shaking and release-mode differences for assertions, reflection-like code generation, runtime type names, stack traces, and conditional imports.
- Require tests at boundaries, invalid inputs, minimum/maximum values, malformed payloads, clock changes, locale changes, and old persisted data.

## 13. Architecture, Domain Invariants, And Ownership

Judge architecture by preserved behavior, not by folder names or state-management branding.

- Map presentation, application, domain, data, platform, infrastructure, and integration responsibilities and actual dependency direction.
- Write explicit invariants for identity, authorization, money, inventory, quotas, ordering, status transitions, offline actions, synchronization, deletion, and recovery.
- Trace each critical journey from user input through state, repository, local cache, platform service, backend, persistence, telemetry, and displayed result.
- Verify ownership of mutable state, lifecycle, cancellation, retries, subscriptions, streams, controllers, caches, database handles, and platform resources.
- Detect business logic duplicated across widgets, view models, providers, blocs, repositories, backend clients, native code, and push handlers.
- Verify dependency inversion where it improves testability and platform isolation; reject ceremonial abstraction that hides behavior or error semantics.
- Identify god objects, circular dependencies, service-locator coupling, feature leakage, shared mutable models, implicit singletons, and cross-feature side effects.
- Verify platform-specific code is isolated behind explicit contracts with fallback, unsupported-state handling, tests, and observability.
- Do not refactor architecture broadly unless a confirmed risk, measurable outcome, compatibility plan, migration sequence, and rollback justify it.

## 14. State Management And Reactive Consistency

Audit the actual state machine whether the project uses Provider, Riverpod, Bloc, Cubit, Redux, MobX, Signals, GetX, ValueNotifier, custom controllers, or mixed approaches.

- Inventory source of truth, derived state, ephemeral UI state, persisted state, server state, cache state, navigation state, and platform state.
- Verify event ordering, stale-result suppression, duplicate request coalescing, optimistic update rollback, pagination, refresh, retry, and account switching.
- Test simultaneous user actions, repeated taps, route changes during requests, background/foreground transitions, reconnect, logout, and tenant switch.
- Verify provider/bloc/controller scope, disposal, auto-dispose, keep-alive, restoration, nested overrides, test overrides, and cross-route ownership.
- Detect inconsistent loading/error/empty/success models, hidden stale data, partial failures, infinite refresh loops, duplicate listeners, and notification storms.
- Ensure sensitive state is cleared on logout, account removal, tenant change, app reset, device compromise response, and retention expiry.
- Measure rebuild granularity and selector behavior; optimize only after profiling confirms avoidable work.
- Require deterministic state-transition tests for critical flows, including invalid, interrupted, duplicated, reordered, and replayed events.

## 15. Navigation, Routing, Deep Links, And Multi-Window State

Treat navigation as a security, lifecycle, and state-consistency boundary.

- Inventory Navigator APIs, Router, declarative routing packages, nested navigators, shell routes, modal routes, restoration IDs, and custom transitions.
- Verify path, query, fragment, route extras, serialized state, and platform deep-link inputs are parsed, normalized, bounded, and authorized.
- Test cold start, warm start, background resume, killed process, logged-out state, expired session, wrong tenant, missing resource, and duplicate deep link delivery.
- Prevent authorization bypass by direct route entry; UI hiding is not authorization.
- Verify browser back/forward, URL synchronization, refresh, history restoration, canonical URLs, and unsupported route behavior on web.
- Verify multiple windows, scenes, desktop instances, secondary displays, notification taps, and add-to-app engines do not share or overwrite the wrong navigation state.
- Audit redirect loops, async guards, stale guards, race conditions between session restoration and routing, and error-page information disclosure.
- Require route contract tests and platform deep-link tests for all privileged and business-critical destinations.

## 16. Widget Tree, Layout, Input, And Rendering Correctness

Review UI behavior across constraints, devices, input modes, text scales, and lifecycle changes.

- Audit widget identity, keys, list reuse, reorder behavior, focus retention, form state, scroll position, hero tags, overlays, and portal-like content.
- Check constraints, unbounded layouts, overflow, intrinsic measurement, nested scrolling, slivers, large lists, grids, tables, dialogs, sheets, and keyboard insets.
- Verify touch, mouse, trackpad, stylus, keyboard, gamepad, remote control, hover, drag/drop, context menus, text selection, and IME behavior where applicable.
- Test minimum and extreme sizes, orientation, split-screen, fold/posture changes, desktop resize, multiple displays, safe areas, system bars, and display cutouts.
- Inspect animation controllers, ticker ownership, reduced-motion behavior, route transitions, loading indicators, skeletons, and interruption handling.
- Verify image decode, caching, placeholders, error states, large images, animated formats, vector assets, color profiles, and memory pressure.
- Detect unnecessary rebuilds, layout thrashing, saveLayer use, opacity/clipping cost, shader compilation issues, raster cache misuse, and platform-view composition cost.
- Require visual, golden, semantic, focus, and interaction tests where regressions have meaningful user impact.

## 17. Lifecycle, Restoration, Process Death, And Resource Ownership

Assume the operating system can suspend, detach, kill, recreate, resize, or restore the application at inconvenient points.

- Map application, view, route, widget, engine, scene/window, isolate, service, and plugin lifecycles for every supported platform.
- Verify initialization ordering, dependency readiness, splash removal, session restoration, database opening, migrations, remote config, and first-frame behavior.
- Test backgrounding, foregrounding, inactive/hidden/detached states, memory pressure, device lock, interruption, permission changes, and process termination.
- Verify restoration of navigation, forms, drafts, playback, downloads, uploads, pagination, unsent actions, and conflict state without exposing another account or tenant.
- Dispose controllers, focus nodes, animation controllers, stream subscriptions, timers, ports, database watchers, plugin listeners, textures, cameras, players, and native handles exactly once.
- Handle hot restart and development-only behavior separately from production lifecycle claims.
- Test interrupted migration, interrupted write, interrupted payment, interrupted file transfer, interrupted update, and restoration after low-memory termination.
- Require state restoration and process-death tests on real or production-equivalent devices for critical flows.

## 18. Futures, Cancellation, Concurrency, And Race Conditions

Dart is single-threaded per isolate, but applications still have asynchronous races, native concurrency, multiple isolates, and distributed conflicts.

- Trace every critical Future chain, callback, completer, timer, microtask, post-frame callback, retry, debounce, throttle, and cancellation boundary.
- Detect use-after-dispose, setState after dispose, stale response overwrite, duplicate submission, overlapping refresh, lost update, double navigation, and repeated side effects.
- Verify cancellation or stale-result suppression when route, query, account, tenant, device, locale, filter, or session changes.
- Audit mutex, lock, semaphore, queue, single-flight, lease, idempotency-key, optimistic concurrency, version, and compare-and-set strategies where needed.
- Verify UI-level deduplication does not replace server-side idempotency and authorization for payments, orders, mutations, uploads, and destructive actions.
- Test rapid repeated input, slow network, timeout, reconnect, retry, app pause, clock change, token refresh, duplicate push, and old/new version overlap.
- Preserve correlation IDs and operation state across retries so telemetry distinguishes one logical operation from duplicate executions.
- Require deterministic concurrency tests with controllable clocks, fake transports, barriers, and fault injection for material races.

## 19. Streams, Subscriptions, Backpressure, And Realtime

Review streams as long-lived resource and ordering contracts.

- Inventory single-subscription and broadcast streams, controllers, subjects, database watchers, sockets, SSE, platform event channels, and push-derived streams.
- Verify subscription ownership, pause/resume, cancellation, close, error handling, done semantics, replay, buffering, and lifecycle binding.
- Audit event ordering, duplicates, gaps, reconnection, resume cursor, snapshots plus deltas, clock skew, stale cache, and version conflict handling.
- Define backpressure, bounded queues, dropping/coalescing policy, slow-consumer behavior, and memory limits for high-volume streams.
- Prevent duplicate listeners after rebuild, navigation, reconnect, hot reload, account switching, and background/foreground transitions.
- Verify sensitive events are filtered by current identity, tenant, resource ownership, and revocation state before state mutation or display.
- Test disconnect storms, duplicate frames, malformed messages, server restart, resume-token expiry, and long offline periods.
- Measure event lag, queue depth, dropped/coalesced events, reconnect rate, memory growth, and server pressure.

## 20. Isolates, Workers, And Heavy Computation

Use isolation deliberately and verify message, memory, and lifecycle costs.

- Inventory `Isolate.spawn`, `Isolate.run`, `compute`, background plugin entrypoints, native worker threads, and web workers.
- Verify entrypoint reachability, tree-shaking annotations where required, initialization, plugin registration, dependency availability, and platform restrictions.
- Audit message serialization, TransferableTypedData, copying cost, object ownership, protocol versioning, malformed messages, and shutdown.
- Prevent isolates from using unsupported UI bindings, stale credentials, wrong tenant context, uninitialized storage, or non-isolate-safe native resources.
- Define cancellation, timeout, progress, crash propagation, restart, queue limits, and cleanup for long-running work.
- Profile whether isolation improves responsiveness after startup, copy, scheduling, and memory overhead.
- On web, verify worker availability, CSP, asset paths, browser support, fallback, and cross-origin isolation requirements.
- Require load, cancellation, termination, malformed-message, and repeated-start/stop tests.

## 21. Background Execution And Scheduling

Background work is platform-controlled and cannot be guaranteed by a Dart timer.

- Inventory WorkManager, foreground services, background fetch, BGTaskScheduler, silent push, isolates, desktop services, scheduled tasks, and browser background capabilities.
- Document platform eligibility, execution window, quotas, battery/network constraints, user-visible requirements, permission, and termination behavior.
- Make tasks idempotent, resumable, bounded, observable, and safe after duplicate scheduling, delayed execution, process death, reboot, upgrade, logout, or account switch.
- Verify background entrypoint initialization, plugin registration, storage access, authentication refresh, tenant context, and conflict handling.
- Prevent background jobs from leaking data after logout, continuing revoked uploads, reviving deleted state, or sending stale notifications.
- Test restricted battery modes, no network, metered network, low storage, reboot, force stop, OS upgrade, app upgrade, and missed schedule recovery.
- Measure success, delay, retries, duplicate execution, duration, resource use, queue age, and backend load.
- Provide a degraded-mode product behavior when the platform cannot or will not run work on the desired schedule.

## 22. Platform Channels, Pigeon, And Native Boundary

Treat every Dart/native bridge as an IPC and authorization boundary.

- Inventory MethodChannel, EventChannel, BasicMessageChannel, Pigeon APIs, FFI, callbacks, codecs, channel names, handlers, and platform implementations.
- Verify schema, type, nullability, range, enum, path, URI, origin, resource ownership, and business authorization on both sides of every call.
- Audit call ordering, reentrancy, concurrent calls, duplicate callbacks, timeout, cancellation, process recreation, engine detach, and late result delivery.
- Do not expose generic file, shell, URL, reflection, database, keychain, clipboard, intent, process, or device operations without narrow allowlists and resource checks.
- Verify errors preserve enough diagnostics without leaking secrets, paths, tokens, native stack data, or internal identifiers to users.
- Version channel contracts and test old/new Dart and native combinations during rolling application or add-to-app upgrades.
- Review thread requirements, main-thread blocking, dispatch queues, coroutine/task ownership, memory ownership, and callback lifetime in native code.
- Require negative, malformed-input, authorization, concurrency, detach/reattach, process-death, and platform-version tests.

## 23. FFI, Native Assets, And Memory Safety

Native code can bypass Dart safety and must be audited as a separate security and reliability domain.

- Inventory `dart:ffi`, native assets, C/C++/Rust libraries, dynamic libraries, symbols, build scripts, download steps, licenses, and architecture variants.
- Verify provenance, hashes, signatures, reproducibility, compiler flags, hardening, ABI, minimum OS, symbol stripping, and debug-symbol retention.
- Audit pointer ownership, allocation/free symmetry, finalizers, lifetimes, callbacks, struct layout, alignment, encoding, integer width, nullability, and error propagation.
- Detect use-after-free, double free, leaks, buffer overflow, out-of-bounds access, race conditions, callback after unload, and blocking native calls.
- Validate all lengths, paths, file formats, network data, and handles before crossing the native boundary.
- Use sanitizers, fuzzing, static analysis, crash-symbolication, and architecture-specific tests where the toolchain allows.
- Verify graceful fallback or explicit unsupported behavior when a native library, symbol, architecture, entitlement, or device capability is unavailable.
- Include native library revocation, emergency replacement, backward compatibility, and rollback in the release plan.

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

## 25. Add-To-App, Multiple Engines, And Native Host Integration

Mixed Flutter/native products need explicit ownership and compatibility contracts.

- Inventory native host applications, Flutter modules, engine groups, cached engines, routes, entrypoints, plugin registration, and lifecycle ownership.
- Verify native and Flutter navigation, authentication, account/tenant state, analytics, accessibility, theme, locale, and error semantics remain consistent.
- Audit engine creation/destruction, retained engines, memory, plugin singleton assumptions, channel collisions, multiple view controllers/activities, and background callbacks.
- Version the boundary between host and module, including routes, arguments, results, events, shared storage, tokens, and rollout compatibility.
- Verify build, packaging, symbols, signing, crash reporting, and release ownership for the combined artifact.
- Test old host/new module and new host/old module combinations where independent rollout or caching can occur.
- Ensure native screens cannot bypass Flutter-side authorization and Flutter screens cannot assume native UI checks are authoritative.
- Document rollback and emergency disable behavior if the Flutter module or native host becomes incompatible.

## 26. Authentication, Session, And Device Trust

Authentication must survive hostile input, lifecycle interruption, token rotation, multi-device use, and account switching.

- Map sign-in, registration, verification, MFA, passkey, biometric unlock, recovery, refresh, logout, logout-all, device enrollment, and account deletion.
- Verify OAuth/OIDC authorization code with PKCE, redirect URI ownership, state, nonce, issuer, audience, signature, clock skew, token type, and key rotation.
- Store only necessary secrets using platform-appropriate protected storage; verify lock state, backup/restore, device migration, rooted/jailbroken behavior, and uninstall semantics.
- Audit refresh single-flight, token rotation, revocation, replay, concurrent 401 handling, stale request retry, background refresh, and session-expiry UX.
- Separate local biometric convenience from server authentication and authorization; define fallback, lockout, re-enrollment, and compromised-device response.
- Ensure logout and account switch clear memory, caches, databases, files, notifications, background work, realtime subscriptions, WebViews, and screenshots as required.
- Test duplicate callbacks, canceled browser login, wrong redirect, deep-link hijack, offline login, expired keys, changed password, revoked device, and old/new app versions.
- Do not log credentials, tokens, authorization codes, biometric results, recovery data, or sensitive identity claims.

## 27. Authorization, Object Ownership, And Tenant Isolation

The client can improve UX but cannot be the authoritative security boundary.

- Map every privileged action, object lookup, mutation, export, share, upload, download, admin flow, support flow, and tenant-scoped query.
- Verify server-side authentication, permission, role, resource ownership, tenant membership, status, quota, and business-invariant checks.
- Treat route guards, hidden buttons, local roles, cached entitlements, feature flags, and disabled controls as presentation only.
- Prevent BOLA/IDOR by testing changed identifiers, stale links, another user, another tenant, deleted membership, downgraded role, and revoked share.
- Verify local cache keys, database partitions, file paths, search indexes, notification payloads, analytics, and background tasks include correct account and tenant identity.
- Test account switch and tenant switch during in-flight reads, writes, uploads, downloads, realtime events, migration, and restoration.
- Audit impersonation and delegated access with explicit actor, subject, purpose, duration, scope, logging, user visibility, and revocation.
- Require negative authorization tests at API, repository, state, route, storage, notification, and UI integration layers.

## 28. Secrets, Cryptography, Privacy, And Data Lifecycle

Minimize data and secrets before choosing storage or encryption.

- Inventory API keys, client secrets, certificates, private keys, tokens, database keys, analytics identifiers, device IDs, personal data, and regulated data.
- Assume values shipped in Dart code, assets, JavaScript, native resources, manifests, Info.plist, desktop resources, or `--dart-define` can be extracted.
- Use backend-held secrets and scoped short-lived credentials for privileged services; restrict public client keys by origin, application ID, certificate, quota, and backend authorization where supported.
- Verify cryptographic algorithm, mode, nonce/IV uniqueness, randomness, key derivation, authentication tag, key custody, rotation, revocation, backup, restore, and versioning.
- Do not invent custom cryptography or treat obfuscation, split strings, base64, application private storage, or certificate pinning as encryption.
- Map collection, purpose, consent, legal basis, minimization, retention, deletion, export, correction, backup, support access, and third-party transfer.
- Audit screenshots, clipboard, notifications, logs, crash reports, analytics, recordings, files, caches, browser storage, backups, and recent-app previews for leakage.
- Verify deletion and account closure propagate to local data, queued work, files, notifications, analytics identifiers, backend systems, exports, and backups according to policy.

## 29. Network, API Contracts, TLS, And Resilience

Audit the complete client-to-service behavior under normal, degraded, hostile, and evolving conditions.

- Inventory HTTP clients, interceptors, adapters, WebSocket/SSE clients, GraphQL, gRPC, upload/download stacks, DNS behavior, proxies, and platform network configuration.
- Verify base URL and environment selection, scheme, host allowlists, redirects, cleartext policy, ATS/network security config, proxy behavior, local network access, and certificate validation.
- Use explicit connect, send, receive, idle, and total deadlines where supported; propagate cancellation and operation deadlines.
- Retry only safe or idempotent operations with bounded attempts, backoff, jitter, server hints, budget, and overload protection.
- Verify API schema, content type, compression, pagination, partial response, unknown fields, error envelope, Problem Details, localization, and backward compatibility.
- Audit token-refresh interaction, request replay, duplicate body streams, upload resume, download integrity, redirect authorization stripping, and cancellation.
- Treat TLS pinning as an operationally expensive optional control requiring backup pins, rotation, expiry monitoring, proxy policy, emergency disable, and tested recovery.
- Test offline, captive portal, DNS failure, IPv4/IPv6, TLS failure, expired certificate, slow body, truncated body, malformed payload, 429, 5xx, timeout, reconnect, and clock skew.
- Measure latency distribution, failure rate, retries, bytes, cache hits, queue time, cancellation, backend amplification, and user-visible recovery.

## 30. WebView, Embedded Browser, And Untrusted Content

A WebView combines remote content with application privileges and requires strict isolation.

- Inventory every WebView/browser view, origin, navigation source, JavaScript setting, bridge, cookie jar, storage, file access, media permission, download path, and popup behavior.
- Allowlist schemes, hosts, paths, redirects, and external-open destinations; reject lookalike hosts, mixed content, unsafe schemes, userinfo, malformed URLs, and open redirects.
- Expose the smallest possible message bridge with schema validation, origin/frame validation, authorization, rate limits, correlation, timeout, and lifecycle binding.
- Do not expose tokens, raw filesystem, shell, arbitrary URL launch, clipboard, contacts, camera, database, or device APIs to untrusted content.
- Verify cookie flags, SameSite behavior, SSO logout, cache clearing, account switch, storage partitioning, certificate errors, safe browsing, and download validation.
- Test XSS in remote content, malicious redirects, nested frames, bridge spoofing, replay, navigation during a privileged request, process recreation, and offline cached pages.
- Keep browser and platform WebView versions in the compatibility matrix and define unsupported-version behavior.
- Require security review for every new origin, bridge method, file permission, download type, or authentication flow.

## 31. Local Storage, Databases, Migrations, And Cache

Local persistence is a versioned data system, not an implementation detail.

- Inventory SQLite/Drift/sqflite, Isar, Hive, ObjectBox, Realm, SharedPreferences, secure storage, files, browser storage, desktop preferences, caches, and indexes.
- Classify authoritative data, replicated data, cache, derived data, secret material, draft state, queue state, telemetry state, and disposable data.
- Verify schema versioning, forward migration, rollback policy, interrupted migration, low disk, corruption, old application version, restored backup, and partial write behavior.
- Use transactions for multi-step invariants; inspect isolation, concurrent readers/writers, nested transactions, WAL/journal behavior, and native-thread access.
- Partition data by account and tenant; verify logout, account switch, tenant switch, deletion, backup, restore, and cache invalidation.
- Audit encryption claims, key lifecycle, searchable metadata, temporary files, backups, screenshots, browser DevTools exposure, and desktop filesystem permissions.
- Define cache key, freshness, stale-while-revalidate, invalidation, size, eviction, corruption, stampede protection, and offline semantics.
- Require migration fixtures from every supported historical version and test upgrade, interrupted upgrade, recovery, downgrade rejection, and data export.

## 32. Offline-First, Synchronization, And Conflict Resolution

Offline behavior must define authority, ordering, identity, and conflict semantics.

- Document which reads and writes are allowed offline, their user promise, durability, expiration, cancellation, and server acceptance conditions.
- Assign stable operation IDs and idempotency keys; persist queue state transactionally with payload version, actor, tenant, dependency, retry count, and status.
- Define ordering, dependency, compaction, deduplication, retry, backoff, expiry, poison operation, cancellation, and manual intervention.
- Choose conflict policy per entity and field: server authority, client authority, version check, merge, append-only, CRDT, or explicit user resolution.
- Prevent stale offline operations from acting after logout, role change, tenant change, deletion, quota change, price change, or business-rule change.
- Test long offline periods, clock skew, reordered operations, duplicated operations, partial synchronization, server reset, schema change, token expiry, and multiple devices.
- Provide truthful UI for pending, synced, conflicted, failed, canceled, expired, and rejected operations.
- Measure queue age, conflict rate, retry count, poison rate, duplicate suppression, reconciliation lag, and user-visible data loss.

## 33. Files, Media, Downloads, Uploads, And Archives

Treat every external file as untrusted and every local path as platform-specific.

- Inventory document pickers, camera/gallery, drag/drop, share intents, clipboard, imports, exports, archives, media decode, thumbnails, downloads, uploads, and temporary files.
- Validate type from content where possible, size, dimensions, duration, count, encoding, filename, extension, path, archive structure, and parser limits.
- Prevent path traversal, symlink/reparse abuse, zip slip, decompression bombs, overwrite, executable content, malicious metadata, parser crashes, and unsafe external opening.
- Use scoped or user-selected storage appropriately; verify platform bookmarks/permissions, revocation, sandbox paths, removable media, cloud files, and file-provider semantics.
- Define upload and download resume, integrity hash, content length, partial file, cancellation, retry, quota, duplicate, overwrite, cleanup, and low-disk behavior.
- Do not expose private local paths, signed URLs, tokens, tenant identifiers, EXIF/GPS data, or user content in logs and analytics.
- Test malformed, truncated, huge, encrypted, nested, renamed, zero-byte, duplicate, unsupported, and slow-stream files.
- Verify cleanup after success, failure, cancellation, process death, logout, account deletion, app update, and uninstall according to policy.

## 34. Permissions, Sensors, Hardware, And External Applications

Request the minimum capability at the moment of need and survive denial or revocation.

- Inventory camera, microphone, photos, media, contacts, calendar, location, Bluetooth, nearby devices, notifications, local network, USB, serial, NFC, biometrics, health, sensors, and screen capture.
- Map runtime requests to manifest/Info.plist/entitlement/desktop declarations, purpose text, store disclosures, privacy manifests, and actual code paths.
- Handle not determined, denied, permanently denied, restricted, limited, approximate, one-time, while-in-use, background, and revoked states accurately.
- Do not repeatedly nag, bypass platform UI, open settings without context, or claim capability that the OS has not granted.
- Verify hardware absence, busy device, interruption, route change, lifecycle transition, multi-window use, permission change, and plugin error cleanup.
- Validate external application intents, URLs, file handoff, return values, spoofed callbacks, missing handlers, and sensitive-data exposure.
- Test physical devices and relevant OS versions; emulator/simulator support is not enough for camera, Bluetooth, background location, NFC, biometrics, media, and USB.
- Measure battery, thermal, radio, CPU, memory, and privacy impact of continuous sensing or scanning.

## 35. Notifications, Push, Universal Links, And App Links

Push delivery is untrusted, duplicated, delayed, and platform-dependent.

- Inventory FCM/APNs/web push providers, tokens, topics, channels/categories, background handlers, notification service extensions, actions, badges, and local notifications.
- Verify token registration, rotation, deletion, environment separation, account/tenant binding, logout cleanup, device replacement, and server-side authorization.
- Treat payload fields as untrusted; validate type, size, route, object identifier, actor, tenant, freshness, signature where used, and current authorization.
- Test foreground, background, terminated, force-stopped, offline, duplicate, delayed, reordered, revoked-session, wrong-account, and app-upgrade delivery.
- Avoid sensitive notification content on locked screens unless policy and user choice permit it; handle preview settings and platform redaction.
- Verify app links, universal links, custom schemes, asset association files, domain ownership, fallback pages, multiple apps, and hijack resistance.
- Make notification actions idempotent and server-authorized; prevent repeated taps from duplicating payments, orders, messages, or destructive changes.
- Measure delivery, open rate, duplicate rate, invalid token rate, action failure, deep-link failure, and notification-to-backend amplification.

## 36. Android-Specific Audit

Verify the Flutter layer together with the actual Android host and final AAB/APK.

- Audit Gradle settings, AGP/Kotlin/JDK/SDK/NDK compatibility, repositories, variants, flavors, manifests, resource merging, desugaring, ABI splits, and dependency graph.
- Inspect application/activity classes, FlutterActivity/Fragment/Engine integration, launch mode, task behavior, process, exported components, intent filters, providers, receivers, and services.
- Verify permissions, scoped storage, media/photo picker, package visibility, PendingIntent mutability, FileProvider, network security config, backup rules, and data extraction rules.
- Audit lifecycle, configuration change, predictive back, edge-to-edge, system bars, picture-in-picture, multi-window, foldables, large screens, Android TV, and ChromeOS where claimed.
- Verify background restrictions, WorkManager, foreground service types, notification permission/channels, exact alarms, boot behavior, battery optimization, and force-stop semantics.
- Inspect app signing, upload/app-signing keys, certificate continuity, Play Integrity or equivalent use, Play Console tracks, target API, Data safety, and staged rollout.
- Build and inspect release AAB/APK, manifest, resources, native libraries, symbols, R8 output, mapping, ABI, 16 KB page compatibility where applicable, and install behavior.
- Test real devices across supported API, vendor, architecture, memory, display, background restriction, upgrade, restore, and low-storage conditions.

## 37. iOS And iPadOS-Specific Audit

Verify Flutter, Runner/native hosts, extensions, entitlements, signing, and App Store behavior together.

- Audit Xcode project/workspace, build settings, configurations, schemes, deployment targets, Swift/Objective-C code, pods/packages, scripts, architectures, and generated settings.
- Inspect AppDelegate, SceneDelegate/UIScene configuration, FlutterEngine integration, multiple scenes/windows, restoration, deep links, universal links, and add-to-app lifecycle.
- Verify Info.plist purpose strings, entitlements, capabilities, privacy manifests, required-reason APIs, ATS, associated domains, keychain groups, app groups, and extensions.
- Audit background modes, BGTaskScheduler, silent push, notification extensions, audio/location/Bluetooth behavior, process suspension, termination, and user force-quit semantics.
- Verify data protection class, keychain accessibility, backup/restore, iCloud behavior, files, pasteboard, screenshots, screen recording, and protected-data availability.
- Inspect signing certificates, provisioning profiles, team/bundle IDs, App Store Connect roles, TestFlight groups, export options, archive, dSYM, symbol upload, and certificate expiry.
- Test iPhone and iPad device classes, orientations, multitasking, external keyboard, pointer, Stage Manager, memory pressure, accessibility, upgrade, restore, and old/new OS versions.
- Review App Store privacy, tracking, subscription/payment, account deletion, review, export compliance, encryption declarations, and phased release requirements.

## 38. Web-Specific Audit

Flutter web is a browser application with origin, cache, deployment, accessibility, and compatibility constraints.

- Record JavaScript or Wasm mode, renderer, optimization, base href, asset URL strategy, compile-time defines, browser matrix, mobile/desktop browser support, and fallback.
- Verify CSP including nonce/hash strategy, Trusted Types where used, COOP/COEP/CORP for cross-origin isolation, CORS, permissions policy, frame policy, referrer policy, and HTTPS.
- Audit service worker, cache versioning, stale shell, asset hashing, CDN caching, HTML cache policy, update prompt, rollback, offline behavior, and partial deployment.
- Verify origin separation, cookies, browser storage, session restoration, logout, multi-tab behavior, BroadcastChannel or worker use, private mode, quota, and storage eviction.
- Audit URL handling, history, refresh, server rewrites, deep routes, canonical metadata, SEO limitations where relevant, and error fallback.
- Test accessibility with browser semantics, screen readers, keyboard-only navigation, focus, zoom, text scaling, high contrast, reduced motion, and copy/paste.
- Measure initial download, compression, caching, first paint, Flutter first frame, interaction readiness, frame performance, memory, worker cost, and low-end-device behavior.
- Inspect JavaScript interop and DOM access for schema validation, origin checks, XSS, unsafe HTML, prototype behavior, callback lifetime, and release minification differences.
- Test supported browsers, versions, devices, zoom levels, network states, cache states, old/new deployments, and extension/privacy interference.

## 39. Windows-Specific Audit

Verify the Win32 host, package, signing identity, installation, protocol handling, and update path.

- Audit CMake, Visual Studio workload, MSVC/runtime, Windows SDK, architecture, runner code, plugins, generated registrant, native DLLs, and build configuration.
- Verify application identity, package family, publisher, AppUserModelID, MSIX or installer metadata, install scope, elevation, per-user/per-machine behavior, and repair/uninstall.
- Audit Authenticode certificate, timestamp, nested binaries, DLL search, side-loading, SmartScreen reputation, certificate renewal, revocation, and key custody.
- Verify protocol/file associations, command-line arguments, single-instance behavior, multiple windows, toast activation, startup tasks, drag/drop, clipboard, and external processes.
- Test DPI scaling, multiple monitors, remote desktop, high contrast, screen readers, keyboard, IME, touch, tablet mode, sleep/resume, lock/unlock, and fast user switching.
- Audit local files, registry, credential storage, ACLs, temporary paths, symlinks/reparse points, roaming data, backup, and enterprise policy.
- Inspect update atomicity, running-file replacement, reboot requirement, downgrade, channel switch, rollback, old shortcut cleanup, and user-data preservation.
- Test Windows versions, architectures, clean install, upgrade, repair, uninstall, restricted user, offline install, antivirus interaction, and low disk.

## 40. macOS-Specific Audit

Verify the macOS host, sandbox, entitlements, signing, notarization, package, and update behavior.

- Audit Xcode project, deployment target, architectures, Swift/Objective-C runner, pods/packages, plugins, generated registrant, frameworks, rpaths, and native libraries.
- Verify bundle identifier, version, hardened runtime, App Sandbox, entitlements, privacy purpose strings, keychain access groups, app groups, bookmarks, and file access.
- Audit Developer ID or Mac App Store signing, nested code, timestamps, notarization, stapling, Gatekeeper assessment, certificate expiry, revocation, and key custody.
- Verify multiple windows, menu bar, dock, activation policy, open-file/open-URL events, app relaunch, login items, notifications, services, and single-instance expectations.
- Test Retina/scaling, multiple displays, Spaces, full screen, Stage Manager, keyboard, trackpad, VoiceOver, reduced motion, high contrast, sleep/wake, and fast user switching.
- Audit container paths, Application Support, Caches, temporary files, iCloud behavior, backups, quarantine attributes, symlinks, and user-selected file access.
- Inspect DMG/PKG/App Store packaging, update framework/feed, signature verification, atomic install, downgrade, rollback, channel, and user-data continuity.
- Test Intel and Apple Silicon where supported, clean install, migration, old OS, new OS, restricted account, offline launch, update, rollback, and restore.

## 41. Linux-Specific Audit

Define and prove the supported distribution, desktop, packaging, sandbox, and library matrix.

- Audit compiler, CMake/Ninja, GTK, glibc and system libraries, plugins, generated registrant, dynamic linkage, rpaths, architecture, and reproducible build environment.
- Declare tested distributions, versions, desktop environments, display servers, architectures, package formats, sandbox/store runtimes, and support policy.
- Verify desktop file, MIME/protocol handlers, icons, AppStream metadata, single-instance behavior, DBus, portals, notifications, keyring, and file chooser.
- Audit package signature, repository trust, update path, dependency resolution, bundled versus system libraries, permissions, sandbox interfaces, and rollback.
- Test X11 and Wayland where claimed, HiDPI, multiple monitors, keyboard layouts, IME, accessibility stack, screen readers, clipboard, drag/drop, suspend/resume, and session restart.
- Audit filesystem permissions, XDG paths, temporary files, symlinks, removable media, keyring unavailability, headless/remote sessions, and enterprise restrictions.
- Verify crash symbols, core dump privacy, logs, package metadata, license notices, uninstall cleanup, and user-data preservation.
- Test clean/minimal environments, supported old/new distributions, offline launch, missing optional library, restricted user, low disk, update, rollback, and restore.

## 42. Adaptive Design, Accessibility, Localization, And Inclusive UX

Accessibility and adaptation are correctness requirements, not final polish.

- Define supported window classes, breakpoints, orientation, posture, input modes, navigation patterns, information density, and feature parity by platform.
- Test text scaling beyond common defaults, bold text, display zoom, high contrast, color filters, dark mode, reduced motion, reduced transparency, and system font changes.
- Verify semantic labels, roles, values, states, actions, traversal order, live regions, headings, grouping, error association, and hidden decorative content.
- Test TalkBack, VoiceOver, browser screen readers, Narrator, VoiceOver on macOS, and supported Linux accessibility tools with critical journeys.
- Verify keyboard-only and switch access, visible focus, focus trapping, restoration, shortcuts, escape/back semantics, touch target size, gesture alternatives, and timeout extensions.
- Audit contrast, non-color cues, flashing, animation, autoplay, captions, transcripts, audio descriptions, haptics, and error recovery.
- Verify locale resolution, fallback, plural/gender rules, RTL, bidirectional text, date/time, timezone, numbers, currency, names, addresses, sorting, search, and Unicode normalization.
- Detect hard-coded user text, concatenated translations, clipped strings, missing keys, stale generated localizations, untranslated native UI, and unsafe server text.
- Require automated semantics checks plus manual assistive-technology and locale matrix testing for critical flows.

## 43. Performance, Capacity, Battery, And Resource Audit

Profile release/profile builds on representative hardware before optimizing.

- Define budgets for cold/warm startup, first frame, time to interactive, route transition, input latency, frame build/raster time, memory, CPU, battery, network, disk, and artifact size.
- Capture DevTools timelines, frame charts, CPU profiles, allocation profiles, heap snapshots, network traces, shader/raster behavior, platform traces, and backend metrics.
- Measure low-end devices, old supported devices, large datasets, slow storage, constrained memory, thermal pressure, battery saver, poor network, and long sessions.
- Audit startup dependency chain, synchronous I/O, plugin initialization, database migration, remote config, authentication restoration, font/image decode, and first-route work.
- Detect rebuild and relayout hotspots, expensive paint, platform-view cost, large object churn, image/cache leaks, stream/listener leaks, isolate overhead, and background wakeups.
- Test burst, soak, pagination, huge list, rapid navigation, repeated login/logout, account switch, offline queue, reconnect, upload/download, media, and notification storms.
- Correlate client behavior with API rate, retry amplification, websocket connections, push registration, storage growth, cache hit rate, and cloud cost.
- Require before/after measurements, statistical context, device matrix, workload definition, visual correctness, and rollback for performance changes.

## 44. Application Size, Symbols, Obfuscation, And Reverse Engineering

Reduce size and information exposure without sacrificing diagnosability or pretending the client can keep secrets.

- Measure per-platform release size, download size, installed size, split size, web transfer size, native libraries, fonts, assets, localization, and duplicate resources.
- Use size analysis and diffs per release; assign ownership and budget for significant growth.
- Verify tree shaking, deferred loading where appropriate, asset variants, image formats, font subsetting, native stripping, debug artifact exclusion, and package-level contributors.
- If Dart obfuscation is used, preserve exact symbol maps per artifact and verify crash deobfuscation and retention.
- Preserve Android mapping/native symbols, Apple dSYM, Windows PDB, macOS/Linux symbols, web source maps, and native plugin symbols with access controls.
- Do not claim obfuscation protects API secrets, authorization logic, encryption keys, business rules, or personal data.
- Review runtime strings, logs, error messages, manifest metadata, endpoints, feature flags, test credentials, certificates, and assets for unintended disclosure.
- Test symbol upload, crash decoding, source-map privacy, retention, access, incident availability, and artifact-to-symbol identity.

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

## 46. Upgrade, Migration, And Compatibility Audit

Treat SDK, package, platform, architecture, data, and distribution upgrades as behavior migrations.

- Inventory current and target Flutter/Dart, package majors, native toolchains, platform SDKs, minimum OS/browser versions, renderers, storage schemas, and distribution formats.
- Read official breaking changes, migration guides, release notes, deprecations, store deadlines, plugin compatibility, and platform lifecycle changes.
- Build a compatibility matrix for old data, old cache, old server, new server, old client, new client, background jobs, deep links, notifications, and independently deployed components.
- Upgrade in bounded stages with clean build, generated diff review, contract tests, platform builds, artifact inspection, device/browser tests, performance comparison, and rollback after each stage.
- Use expand-and-contract for storage and API schema changes; avoid one-way destructive migration before old/new coexistence and recovery are proven.
- Verify signing identity, bundle/package ID, keychain/secure-storage accessibility, file paths, database location, store listing, update eligibility, and user-data continuity.
- Test interrupted upgrade, low disk, revoked permission, offline launch, restored old backup, downgrade attempt, rollback, and support handoff.
- Do not remove compatibility paths, legacy data, old API support, symbols, or rollback artifacts until telemetry and policy prove the deprecation window is complete.

## 47. Observability, Telemetry, Crash Reporting, And Diagnostics

Telemetry must identify user impact without becoming a privacy or stability risk.

- Define events, metrics, traces, logs, crash reports, breadcrumbs, network diagnostics, performance spans, release markers, and business outcome signals.
- Attach application version, build, platform, OS/browser, device class, flavor, environment, feature flag state, operation ID, and privacy-safe account/tenant correlation.
- Redact tokens, credentials, authorization headers, cookies, personal data, file content, sensitive paths, notification payloads, form fields, and raw database values.
- Verify Flutter framework errors, platform errors, uncaught async errors, isolate errors, native crashes, ANR/hang, web errors, and update/install failures are captured without loops.
- Upload and retain exact Dart symbol maps, Android mapping/native symbols, Apple dSYM, Windows/macOS/Linux symbols, and web source maps per artifact.
- Define sampling, consent, opt-out, retention, data residency, access controls, deletion, vendor outage behavior, SDK failure isolation, and cost limits.
- Create dashboards and alerts for crash-free users/sessions, startup, jank, memory, network errors, auth failures, migration failures, sync conflicts, update failures, and critical journeys.
- Verify each actionable alert has owner, threshold, deduplication, runbook, escalation, safe diagnostic queries, and closure evidence.
- Test telemetry while offline, during startup failure, after logout, under crash loops, with blocked vendors, and across staged release/rollback.

## 48. Flavors, Environments, Feature Flags, And Configuration

Environment isolation must be enforced across code, artifacts, services, signing, stores, and data.

- Inventory Dart entrypoints, flavors/schemes/configurations, application IDs, bundle IDs, web origins, desktop identities, signing, icons, names, backends, analytics, push, payments, and stores.
- Verify no production artifact can accidentally target staging identity, database, analytics, push, payment, storage, feature flags, or update channel, and vice versa.
- Treat `--dart-define`, environment files, remote config, build settings, manifests, plist values, web configuration, and desktop resources as one effective configuration.
- Detect missing, duplicate, stale, conflicting, insecure-default, and silently falling-back configuration.
- Feature flags must define owner, purpose, targeting, prerequisite, default, offline behavior, telemetry, expiry, cleanup, security boundary, and emergency behavior.
- Do not use client flags to grant server authorization or protect secrets; validate risky flag combinations and old-client behavior.
- Test fresh install, upgrade, restored backup, offline startup, missing remote config, stale cache, wrong clock, revoked flag, and rollout/rollback.
- Include an effective-configuration snapshot in release evidence without exposing secrets.

## 49. CI/CD, Build Security, Signing, And Artifact Promotion

The release pipeline is part of the application security boundary.

- Map repository permissions, branch protection, code review, CI triggers, fork behavior, environments, approvals, runner trust, caches, artifacts, secrets, and deployment identities.
- Pin actions, images, SDK archives, package indexes, native dependencies, and tools by immutable version or digest where feasible; verify provenance.
- Prevent untrusted pull requests, build scripts, tests, generators, dependency hooks, or artifact uploads from accessing signing keys, store credentials, production tokens, or privileged runners.
- Prefer short-lived workload identity and protected signing services; define custody, access, quorum, audit, backup, rotation, expiry, revocation, and disaster recovery for keys.
- Build once from an identified commit, retain immutable artifacts, scan and sign the exact bytes, promote the same artifact, and prevent environment-specific rebuilds.
- Generate checksums, SBOM, provenance, dependency inventory, symbols, source maps, release notes, effective configuration, test evidence, and approval record per artifact.
- Verify final signatures, entitlements, permissions, manifests, identities, versions, native libraries, assets, symbols, and store/install metadata after all transformations.
- Protect artifact retention and rollback candidates from deletion or mutation until release and incident policy permits cleanup.
- Test key expiry, revoked credential, unavailable store, failed signing, partial upload, wrong artifact, duplicate version, canceled release, and emergency release path.

## 50. Distribution, Store Submission, Installation, Update, And Rollback

Release success means users can safely obtain, install, run, update, and recover the intended artifact.

- Inventory Google Play, App Store/TestFlight, web/CDN, Microsoft Store/MSIX, direct Windows installers, Mac App Store/Developer ID, Linux stores/packages, enterprise, and internal channels.
- Verify identity continuity, version/build monotonicity, signing, metadata, screenshots, privacy disclosures, content ratings, export compliance, subscriptions, account deletion, and review requirements.
- Test clean install, upgrade from every supported prior version, skipped-version upgrade, reinstall, restore, channel switch, architecture change, interrupted install, low disk, offline launch, and uninstall.
- Verify user data, secure storage, database, files, permissions, notifications, deep links, background tasks, app links, and associations survive or reset according to policy.
- Define staged rollout cohorts, telemetry gates, acceptance thresholds, abort triggers, freeze authority, rollback owner, support communication, and store-specific rollback limits.
- Web deployments must prevent mixed asset versions, stale HTML/service worker traps, incompatible API changes, missing source maps, and cache-poisoned rollback.
- Mobile store rollback may require a forward-fix build; preserve old/new compatibility, remote disable controls, backend mitigations, and recovery communications.
- Desktop updaters/installers must verify signature, metadata, channel, architecture, atomic replacement, running process, downgrade policy, rollback, and key rotation.
- Do not call rollout successful until operational evidence covers intended cohorts, critical journeys, migrations, crashes, performance, support signals, and rollback readiness.

## 51. Backup, Restore, Disaster Recovery, And Business Continuity

A backup claim is incomplete until restore and application compatibility are demonstrated.

- Inventory server backups, local exports, user-created backups, cloud backup behavior, secure-storage backup behavior, signing material backup, artifact retention, symbols, source maps, and store access recovery.
- Define owner, scope, frequency, encryption, immutability, retention, access, region, legal constraints, dependency order, RPO, RTO, and restore environment.
- Test restore with exact application versions, schema versions, encryption keys, credentials, backend contracts, feature configuration, and symbols required to operate and diagnose.
- Verify restored clients and services do not duplicate queued operations, reuse revoked credentials, resurrect deleted data, cross tenant boundaries, or violate retention.
- Include signing-key loss, store-account loss, push certificate loss, update-feed compromise, backend-region loss, telemetry outage, and critical vendor outage scenarios.
- Test failover and failback where applicable, including DNS, certificate, origin, app-link association, remote config, cache, and old-client behavior.
- Record measured RPO/RTO, missing dependencies, manual steps, data loss, user impact, and remediation from every drill.
- Do not declare recovery-ready based only on successful backup jobs, retained artifacts, or documented procedures.

## 52. Incident Response And Trusted Rebuild

Preserve evidence and restore trust before optimizing normal delivery.

- Define triggers for active compromise, credential leakage, signing-key compromise, malicious dependency, update-channel compromise, data exposure, crash loop, destructive migration, and widespread outage.
- Preserve repository state, CI logs, dependency resolution, generated output, build artifacts, signatures, store metadata, update metadata, telemetry, backend logs, device evidence, and timelines.
- Contain with the narrowest safe controls: revoke credentials, disable flags/routes, stop rollout, remove malicious artifacts, block versions, isolate services, and protect user data.
- Assess client-version reach, store propagation delay, offline devices, old installers, cached web assets, background jobs, tokens, and persisted malicious state.
- Revoke and rotate affected secrets, certificates, keys, tokens, signing identities, update keys, push credentials, and vendor access with dependency-aware sequencing.
- Rebuild from a verified commit in a clean trusted environment with re-resolved dependencies, reviewed generated code, new provenance, new signatures, and artifact comparison.
- Validate eradication, backward compatibility, user remediation, forced update or minimum-version policy, recovery of offline clients, and recurrence detection.
- Document decisions, approvals, communications, legal/privacy obligations, store/vendor coordination, residual risk, and follow-up ownership.
- Do not destroy evidence, clean compromised systems before capture, publish unverifiable fixes, or declare closure without trusted-build and operational proof.

## 53. Mandatory Evidence Matrices

Produce every applicable matrix. A missing platform, artifact, environment, identity, or recovery path must be visible rather than silently excluded.

### 53.1 Platform And Device Matrix

- Platform, OS/browser version, architecture, device/window class, input mode, distribution channel, support status, test depth, owner, and evidence.
- Include minimum, typical, latest, low-resource, accessibility, and representative vendor/device cases.

### 53.2 Toolchain And Dependency Matrix

- Local, CI, release, and production-resolved Flutter, Dart, engine, package graph, native toolchain, platform SDK, and generator versions.
- Mark drift, floating versions, unsupported combinations, prerelease components, native binary provenance, and remediation.

### 53.3 Artifact Identity Matrix

- Commit, dirty state, build job, artifact hash, package/bundle ID, version/build, flavor, signing identity, store/channel, symbols/source maps, SBOM, provenance, and runtime confirmation.
- Cover every promoted, staged, production, rollback, and incident-rebuild artifact.

### 53.4 Critical Journey Matrix

- Journey, role, tenant, starting state, network state, lifecycle state, platform, expected invariant, negative case, telemetry, rollback, and evidence.
- Include authentication, privileged mutations, payments/orders where applicable, offline flows, file/media flows, notification/deep-link entry, and recovery.

### 53.5 Authorization And Tenant Matrix

- Actor, subject, role, tenant, resource, operation, client presentation, server enforcement, local partition, negative test, revocation behavior, and evidence.
- Include direct route entry, changed identifier, stale link, account switch, tenant switch, impersonation, background work, and notifications.

### 53.6 Data And Storage Matrix

- Data class, owner, authority, location, account/tenant partition, encryption, key, backup, retention, deletion, export, migration, corruption recovery, and evidence.
- Include memory, secure storage, database, files, cache, browser storage, notifications, logs, crash reports, analytics, and backups.

### 53.7 Lifecycle And Concurrency Matrix

- Operation, owner, start state, interruption, cancellation, timeout, duplicate, stale-result rule, account/tenant change, process death, resume, cleanup, and evidence.
- Cover network calls, streams, state controllers, background jobs, isolates, platform channels, uploads/downloads, payments, migrations, and updates.

### 53.8 Plugin And Native Boundary Matrix

- Plugin/API, platform implementation, native dependency, permission/entitlement, channel/FFI contract, lifecycle, threading, error model, unsupported behavior, tests, owner, and evidence.
- Include federated implementations, platform views, background entrypoints, multiple engines, native assets, and security-sensitive bridges.

### 53.9 Permission And Hardware Matrix

- Capability, platform declaration, runtime state, purpose, data accessed, fallback, revocation, lifecycle, hardware absence, privacy disclosure, test device, and evidence.
- Include denied, permanently denied, restricted, limited, approximate, one-time, while-in-use, background, and revoked states where applicable.

### 53.10 Release And Rollout Matrix

- Platform/channel, artifact, cohort, prerequisite, store/install step, telemetry gate, acceptance threshold, abort trigger, rollback/forward-fix path, owner, and evidence.
- Include clean install, upgrades from supported versions, restored backup, low disk, offline launch, update interruption, old/new coexistence, and support communication.

### 53.11 Observability And SLO Matrix

- Critical journey or resource, SLI, target, source, dimensions, sampling, privacy, alert, owner, runbook, release gate, retention, and evidence.
- Include crash-free use, startup, jank, memory, network, auth, migration, sync, background work, notifications, update/install, and business outcomes.

### 53.12 Recovery And Incident Matrix

- Scenario, detection, evidence source, containment, revoked material, trusted source, rebuild/restore step, user impact, communication, RPO/RTO, owner, validation, and evidence.
- Include signing-key loss, malicious dependency, update compromise, data exposure, backend loss, store loss, telemetry outage, crash loop, and destructive migration.

## 54. Mandatory Adversarial And Failure Scenarios

1. Change a resource identifier, route parameter, tenant, account, notification payload, or deep-link target and verify server and local isolation.
2. Tap a mutation repeatedly under slow network and verify one logical side effect, truthful UI state, idempotency, and telemetry.
3. Switch route, account, tenant, locale, or filter while requests and streams are active and verify stale work cannot mutate new state.
4. Kill the process during startup, database migration, write, upload, payment, synchronization, and update; verify recovery and invariant preservation.
5. Deliver duplicate, delayed, reordered, malformed, expired, wrong-account, and revoked-session push or realtime events.
6. Deny, restrict, limit, revoke, or change every material permission while the feature and application are active.
7. Run offline for a long period, change clock/timezone, queue conflicting operations from multiple devices, then reconnect and reconcile.
8. Return 401, 403, 409, 412, 429, 5xx, malformed, truncated, huge, slow, redirected, and timed-out network responses during critical journeys.
9. Feed malicious URLs, files, archives, media, JavaScript messages, platform-channel payloads, FFI inputs, paths, and filenames.
10. Exercise minimum, typical, latest, low-memory, low-storage, battery-restricted, accessibility, multi-window, and architecture variants.
11. Install every supported old version, create realistic data, upgrade through skipped versions, interrupt the upgrade, restore an old backup, and attempt downgrade.
12. Serve old web shell with new assets and new shell with old assets; test stale service workers, mixed CDN caches, and rollback.
13. Use old client/new server and new client/old server combinations with schema, feature flag, notification, and background-job overlap.
14. Simulate missing plugin, native library, symbol, hardware, entitlement, system service, keychain/keyring, browser capability, and distribution service.
15. Expire or revoke signing, push, TLS, identity, store, update, and telemetry credentials; verify alerts, containment, rotation, and continuity.
16. Trigger crash loops, memory growth, retry storms, reconnect storms, notification storms, large queues, large lists, and backend overload.
17. Restore from backup or trusted artifacts in an isolated environment and prove identity, data consistency, authorization, observability, and measured RPO/RTO.
18. Rebuild after a simulated compromised dependency or build runner and prove clean provenance, new signatures where required, artifact comparison, and revocation.

## 55. Acceptance Criteria

- Every production-relevant claim has status, evidence level, scope, and explicit uncertainty.
- Source, dependency, generated output, native host, artifact, signing, installation, runtime, telemetry, and rollback identities are reconciled.
- All critical business invariants and server authorization rules have positive, negative, duplicate, concurrent, interrupted, and recovery tests.
- Every claimed platform has an explicit support matrix, release build, artifact inspection, install/launch evidence, critical-journey tests, accessibility coverage, telemetry, and recovery path.
- No secret relies on client confidentiality, no privileged action relies only on UI checks, and no sensitive data crosses account or tenant boundaries.
- Lifecycle, cancellation, stream ownership, isolate/background behavior, process death, restoration, and resource cleanup are proven for critical flows.
- Storage migrations, offline queues, conflict resolution, logout/account switching, backup restore, upgrade, rollback, and incident recovery preserve invariants.
- Performance, size, memory, battery, network, disk, crash, and accessibility budgets are measured on representative targets and gated in delivery.
- Signing, provenance, SBOM, symbols, source maps, store/distribution metadata, staged rollout, abort criteria, and rollback/forward-fix procedures are verified.
- All P0/P1 findings are remediated or formally accepted by an authorized owner with compensating controls, expiry, and monitoring.

## 56. Production Readiness Checklist

- [ ] Scope, owners, authorization, evidence ceiling, critical journeys, and support claims are documented.
- [ ] Workspace, user data, signing material, stores, and production systems were protected throughout the audit.
- [ ] Resolved Flutter/Dart/native toolchains and dependencies are supported, reproducible, and free of unexplained drift.
- [ ] Generated code and assets reproduce cleanly and privilege-impacting diffs are reviewed.
- [ ] Architecture preserves domain invariants, explicit ownership, platform isolation, lifecycle, and testability.
- [ ] Authentication, authorization, tenant isolation, secrets, privacy, and data lifecycle meet documented policy.
- [ ] Async operations, streams, isolates, background jobs, channels, FFI, and plugins have bounded lifecycle and failure behavior.
- [ ] Network, WebView, storage, migration, offline, files, permissions, hardware, notifications, and deep links have adversarial coverage.
- [ ] Android, iOS/iPadOS, web, Windows, macOS, and Linux claims are individually proven or explicitly excluded.
- [ ] Adaptive layout, accessibility, localization, RTL, input modes, and reduced-motion behavior pass critical journeys.
- [ ] Release performance, capacity, memory, battery, size, symbols, and diagnostic budgets meet approved thresholds.
- [ ] Layered tests and quality gates cover source, generated code, native boundaries, artifacts, installation, upgrade, and recovery.
- [ ] Telemetry is privacy-safe, artifact-aware, actionable, resilient, and linked to owners and runbooks.
- [ ] Flavor and environment isolation prevents cross-targeting and feature flags cannot grant authorization.
- [ ] CI/CD uses reviewed trust boundaries, immutable promotion, protected signing, provenance, SBOM, and retained recovery artifacts.
- [ ] Store/distribution, install, update, staged rollout, abort, rollback/forward-fix, and support procedures are tested.
- [ ] Backup restore, signing/store access recovery, trusted rebuild, incident containment, and measured RPO/RTO are demonstrated.
- [ ] Residual risks, accepted exceptions, expiry, owners, compensating controls, and next review are recorded.

## 57. Definition Of Done

1. The authorized scope is fully traced to evidence, findings, changes, tests, artifacts, rollout, and recovery.
2. No material claim relies solely on documentation, debug mode, emulator/simulator behavior, analyzer success, or an unsigned artifact.
3. Every confirmed issue has root cause, minimal remediation, regression coverage, platform scope, owner, and verification evidence.
4. Every unresolved issue states the evidence ceiling, blocker, risk, required owner, and next exact verification step.
5. All applicable release artifacts are reproducible, inspected, signed, installable, diagnosable, and linked to exact source and symbols.
6. Critical journeys pass normal, invalid, unauthorized, offline, duplicate, concurrent, interrupted, upgrade, rollback, restore, and accessibility scenarios.
7. Production telemetry and support signals prove the release meets approved gates or the release remains blocked.
8. P0/P1 findings are closed or formally accepted with expiry; no hidden blocker is converted into a green status.
9. Rollback, forward-fix, backup restore, key/store recovery, and trusted rebuild have named owners and tested procedures.
10. The final report is internally consistent, concise enough to execute, detailed enough to reproduce, and honest about uncertainty.

## 58. Forbidden Shortcuts

- Do not solve analyzer or compiler failures by broad ignores, blanket suppressions, unsafe casts, `dynamic`, removed tests, or deleted code unless the behavior is proven obsolete and removal is authorized.
- Do not mass-upgrade Flutter, Dart, packages, native dependencies, minimum OS versions, renderers, state management, architecture, or platforms to make the audit look modern.
- Do not widen permissions, entitlements, exported components, WebView bridges, platform channels, filesystem access, network exceptions, CORS, CSP, or tenant scope to make a feature pass.
- Do not embed secrets, disable certificate validation, accept every URL, trust notification/deep-link payloads, skip signature checks, or rely on obfuscation.
- Do not call debug, emulator, simulator, one-device, one-browser, unsigned, locally rebuilt, or partially deployed results production proof.
- Do not delete user data, caches, migrations, old schemas, compatibility paths, symbols, source maps, old artifacts, or forensic evidence merely to make tests pass.
- Do not hide flaky tests with retries, loosen golden thresholds broadly, silence platform warnings, or exclude unsupported targets without changing support claims.
- Do not invent measurements, coverage, device results, store status, signatures, RPO/RTO, or incident closure.
- Do not publish, submit, sign, notarize, rotate production material, send real notifications, or alter live services without explicit authorization.
- Do not stop at a checklist. Reproduce, verify, fix within scope, retest, inspect artifacts, and report residual risk.

## 59. Required Final Report

Use this exact order. Keep evidence near each conclusion and separate facts, inferences, risks, and recommendations.

1. Executive summary and production decision: `GO`, `CONDITIONAL_GO`, `NO_GO`, or `INSUFFICIENT_EVIDENCE`.
2. Scope, exclusions, authorization, environments, platforms, artifacts, evidence ceiling, and unresolved access.
3. System map: architecture, critical journeys, identities, tenants, trust boundaries, stores, services, native integrations, and owners.
4. Source-to-runtime identity and reproducibility results.
5. Toolchain, dependency, supply-chain, generated-code, and native-host results.
6. P0-P3 finding register ordered by severity and dependency, with evidence and root cause.
7. Implemented changes with file/symbol scope, reason, risk, tests, artifact impact, and rollback.
8. Test and evidence matrix results, including skipped cases and exact blockers.
9. Per-platform release, install, signing, store/distribution, update, performance, accessibility, and recovery status.
10. Observability, rollout, abort, rollback/forward-fix, backup/restore, incident, and trusted-rebuild readiness.
11. Residual risks, accepted exceptions, compensating controls, expiry, owner, dependency, and next verification date.
12. Prioritized roadmap: immediate containment, release blockers, short-term remediation, medium-term hardening, and optional modernization.
13. Appendix with commands, environment, source references, artifact hashes, signatures, matrices, measurements, logs, and retained evidence locations.

## 60. Mandatory Work Order

1. Protect workspace, data, credentials, signing material, stores, and production state.
2. Confirm authorization, scope, critical journeys, platforms, environments, support claims, and evidence ceiling.
3. Inventory repository, trust boundaries, identities, tenants, dependencies, generators, native hosts, plugins, services, and distribution paths.
4. Resolve toolchains and reproduce baseline from a clean controlled environment.
5. Build the source-to-runtime identity chain and identify drift or missing evidence.
6. Audit domain invariants, state, lifecycle, concurrency, storage, network, security, native boundaries, platform behavior, accessibility, and performance.
7. Create the finding register and evidence matrices before broad modification.
8. Reproduce confirmed defects with targeted tests and capture pre-fix evidence.
9. Implement the smallest authorized reversible fix and add regression, negative, concurrency, migration, and recovery coverage.
10. Run applicable clean analysis, tests, release builds, artifact inspection, install, launch, device/browser matrix, performance, accessibility, upgrade, rollback, and restore checks.
11. Verify signing, provenance, symbols, configuration, store/distribution, rollout gates, alerts, runbooks, and incident recovery.
12. Reconcile all claims with evidence, state residual risk honestly, and issue the final production decision.

## 61. Final Instruction

Do not merely review the Flutter code. Prove the real product across source, dependencies, generated code, native hosts, plugins, platform services, release artifacts, supported devices and browsers, distribution channels, backend contracts, telemetry, update paths, rollback, restore, and incident recovery. Work evidence-first, preserve safety, make only authorized reversible changes, and never claim more certainty than the available evidence supports.
