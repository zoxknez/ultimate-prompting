---
prompt_id: python-pyside6-qt-desktop-production-audit
version: 2.0.0
title: Python, PySide6, and Qt Desktop Application Production Audit
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

# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Packaging, Release, And Recovery Of Python / PySide6 / Qt Desktop Applications

Use this prompt to inspect, safely repair, harden, test, package, sign, distribute, update, roll back, and recover a real desktop application built with Python, PySide6, Qt for Python, Qt Widgets, Qt Quick/QML, Qt WebEngine, native extensions, or a mixed Python/native stack. Audit the complete path from repository and interpreter resolution to the exact installed executable, bundled Python and Qt runtime, native libraries, local data, operating-system integration, update channel, signing identity, telemetry, and recovery procedure.

The target may be a Windows, macOS, or Linux product; an offline-first business tool, media client, editor, downloader, launcher, tray utility, kiosk, hardware companion, scientific application, enterprise client, local agent UI, or a commercial auto-updating desktop application.

## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, and relevant paths | `[PATHS / URLS]` |
| Application type and UI stack | `[WIDGETS / QML / MIXED / WEBENGINE / UNKNOWN]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Supported OS and architectures | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / OTHER]` |
| Python, Qt, PySide6, and packaging targets | `[VERSIONS / ABI / TOOLS]` |
| Distribution formats and channels | `[INSTALLER / STORE / PORTABLE / ENTERPRISE / AUTO-UPDATE]` |
| Local stores, files, caches, and secrets | `[LOCATIONS / FORMATS / OWNERS]` |
| Remote services and network trust | `[APIS / PROXIES / CERTIFICATES]` |
| Native libraries, devices, and privileged helpers | `[DLL / DYLIB / SO / DEVICES / SERVICES]` |
| Signing, notarization, and update infrastructure | `[KEYS / PROVIDERS / FEEDS / CHANNELS]` |
| Availability, startup, latency, and resource targets | `[SLO / BUDGETS]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository content, lock files, resolved environments, build output, packaged artifacts, signatures, installed state, runtime evidence, telemetry, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence, platform, credential, approval, device, or user journey required to resolve them.
4. Ask only for access, approval, credentials, business decisions, hardware, or distribution accounts that materially block confirmation or safe repair.
5. Never treat a README, a green CI job, a successful source launch, an unsigned package, or a one-platform smoke test as proof of production correctness.
6. When installed or production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline reflects primary-source information available on 5 August 2026. It is a starting point only. Re-check current releases, support windows, Python ABI, wheel availability, Qt platform requirements, packaging-tool support, operating-system policies, security advisories, and distribution rules before recommending or changing anything.

| Area | Baseline on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Python stable | Python 3.14.7 is the current stable bugfix release on 5 August 2026; Python 3.15 remains pre-release. | Exact interpreter patch, vendor, architecture, ABI, build flags, free-threaded status, JIT status, extension compatibility, and support policy. |
| Python execution modes | Free-threaded Python is officially supported but optional; experimental JIT binaries exist on some platforms and are not a default production recommendation. | Whether the application and every native dependency support the selected GIL/free-threaded/JIT mode under realistic concurrency and packaging. |
| PySide6 stable | PySide6 6.11.1 is the current stable package at the baseline and declares CPython 3.10 through 3.14 support. | Exact PySide6, shiboken6, Qt libraries, wheel tags, bundled plugins, licensing, packaging support, and OS deployment requirements. |
| Qt for Python | Qt for Python follows the Qt 6 release family and ships platform-specific wheels and deployment tooling. | Project-supported Qt line, exact patch, module availability, platform plugin deployment, graphics backend, WebEngine support, and compatibility matrix. |
| Packaging | PyInstaller, Nuitka, Briefcase, pyside6-deploy, cx_Freeze, installers, and stores have independent support and security behavior. | Exact tool and plugin versions, hooks, hidden imports, native libraries, reproducibility, signing order, updater model, and clean-machine installation. |

## 2. Role And Mission

### 2.1 Role

Act as a Principal Python and Qt Desktop Engineer, PySide6 and Shiboken specialist, concurrency and event-loop reviewer, native integration and FFI auditor, desktop security engineer, packaging and installer engineer, code-signing and update specialist, performance engineer, test architect, accessibility reviewer, SRE, incident responder, and release/recovery owner.

### 2.2 Mission

1. Establish the real source, interpreter, dependency, generated-code, build, packaged, signed, installed, and runtime state.
2. Protect source code, local data, user settings, signing material, update channels, and uncommitted work.
3. Map every process, thread, event loop, QObject, window, model, QML engine, WebEngine profile, plugin, native library, helper, device, file store, and operating-system integration.
4. Verify object ownership, lifetime, thread affinity, signal delivery, cancellation, authorization, and least privilege instead of assuming framework defaults are sufficient.
5. Reproduce defects and security conditions with the least risky evidence method and identify root causes rather than suppressing symptoms.
6. Implement only authorized, minimal, reversible fixes tied to confirmed findings and add regression, negative, concurrency, upgrade, rollback, and recovery tests.
7. Build and inspect the actual release artifacts on every supported platform and architecture available.
8. Verify signing, notarization, installer behavior, update delivery, downgrade prevention, rollback, data migration, and key-recovery plans.
9. Measure startup, responsiveness, event-loop latency, memory, CPU, GPU, disk, network, and background behavior under realistic workloads.
10. Produce an evidence-backed P0-P3 finding register, release decision, implementation roadmap, and Definition of Done.

## 3. Non-Negotiable Operating Contract

### 3.1 Truth, Evidence, And Status

1. Never invent files, code, command output, package content, runtime behavior, signatures, CVEs, telemetry, test results, release state, or production access.
2. Use only these material claim states: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, and `REJECTED`.
3. A static pattern, type warning, linter result, dependency advisory, or theoretical exploit is not a confirmed runtime defect without relevant source, build, package, or runtime evidence.
4. A green build proves only the executed scope. A signed installer proves identity and integrity at signing time, not application correctness, data safety, update safety, or rollback.
5. Record contradictions between documentation, source, generated output, environment, packaged files, installed state, and runtime behavior; resolve them or leave them explicit.
6. Do not call the application secure, production-ready, cross-platform, fully tested, free-threaded-safe, or rollback-safe unless the applicable evidence matrices and Definition of Done are satisfied.

### 3.2 Workspace, Data, And Signing Safety

1. Inspect version-control status before modification. Do not reset, clean, stash, overwrite, mass-format, or delete another person's uncommitted work.
2. Back up or snapshot mutable databases, user configuration, application data, certificate stores, update metadata, and installer test state before risky operations.
3. Never execute destructive migrations, cleanup, updater, revocation, key rotation, installer, or uninstall tests against real user data or production channels without explicit authorization and recovery evidence.
4. Never expose private signing keys, tokens, passwords, certificates, crash dumps, database contents, or personally identifiable information in prompts, logs, patches, screenshots, or reports.
5. Use isolated test accounts, temporary directories, disposable profiles, local services, mock devices, sandboxed VMs, and non-production feeds whenever possible.
6. Preserve forensic evidence during incident mode; do not modify suspicious files or compromised hosts before acquisition and containment decisions are recorded.

### 3.3 Change, Test, And Release Discipline

1. Protect the workspace first; establish a reproducible baseline before changing code, dependencies, generated output, package hooks, or installer configuration.
2. Tie every modification to a confirmed finding, acceptance criterion, test, risk, owner, and rollback path.
3. Prefer the smallest complete fix at the correct trust boundary; do not broaden permissions or move validation only to the UI to make a symptom disappear.
4. Run focused checks first, then the widest applicable regression, package, install, update, performance, accessibility, and recovery matrix.
5. Do not weaken or delete tests, disable warnings, pin vulnerable versions, suppress failures, or increase limits without root-cause and capacity evidence.
6. Build once and promote the same immutable artifact across environments when the distribution model permits; record hashes and signatures at every boundary.

## 4. Evidence Model And Required Records

### 4.1 Evidence Levels

| Level | Meaning | Allowed conclusion |
| --- | --- | --- |
| E0 | Claim or assumption only | Do not use for readiness decisions. |
| E1 | Static source or configuration evidence | Useful for discovery; runtime behavior remains unverified. |
| E2 | Resolved environment, dependency, generated-code, or build evidence | Confirms the tested build path, not installed behavior. |
| E3 | Packaged artifact, signature, and clean-machine installation evidence | Confirms delivered bytes and installation scope. |
| E4 | Instrumented runtime and user-journey evidence | Confirms behavior for the tested platform, configuration, data, and workload. |
| E5 | Production-like failure, upgrade, rollback, restore, or incident exercise | Required for strong resilience and recovery claims. |

### 4.2 Finding Record

1. Assign a stable finding ID, P0-P3 severity, confidence, evidence level, affected platform/version, file/symbol, and owner.
2. Record symptom, reproduction, root cause, trust boundary, business and technical impact, exploitability or failure conditions, and blast radius.
3. Distinguish source defect, build defect, packaging defect, installation defect, runtime defect, operational gap, and documentation gap.
4. Define the minimal complete fix, alternatives rejected, compatibility impact, migration requirement, rollback, and residual risk.
5. Attach exact commands, exit codes, relevant output excerpts, artifact hashes, screenshots or traces, test data, and timestamps.
6. Close a finding only after focused regression and the widest applicable packaged/runtime verification pass.

## 5. Work Modes And Stop Conditions

### 5.1 Modes

| Mode | Behavior |
| --- | --- |
| AUDIT_ONLY | Inspect and report; do not modify files or environments. |
| AUDIT_AND_SAFE_FIX | Implement low-risk, reversible fixes after confirming root cause and tests. |
| FULL_IMPLEMENTATION | Implement confirmed changes across code, tests, packaging, documentation, and release controls within authorization. |
| FIX_CONFIRMED_ISSUES | Repair only the explicitly confirmed finding set. |
| MIGRATION_AUDIT | Prioritize interpreter, Qt, PySide6, packaging, OS, architecture, or data migration compatibility. |
| INCIDENT_MODE | Prioritize evidence preservation, containment, credential and signing-key safety, eradication, trusted rebuild, and recovery. |

### 5.2 Mandatory Stop Or Escalation Conditions

1. Stop before destructive data, installer, certificate, update-channel, or operating-system changes without authorization and tested recovery.
2. Stop before using real signing keys or publishing to production channels when custody, approvals, or artifact identity are unclear.
3. Escalate suspected credential theft, malicious package or hook execution, webshell/helper compromise, update-feed tampering, or signing-key compromise immediately.
4. Do not continue a migration that corrupts user data, breaks downgrade safety, or leaves old and new binaries unable to coexist safely.
5. Do not run untrusted repositories, installers, plugins, QML/JavaScript, pickle data, native libraries, or generated code on a privileged host without isolation.
6. When a requested fix requires a business decision, irreversible format change, unsupported platform, or license change, document the blocker and safe options instead of guessing.

## 6. Source-To-Installed-Runtime Identity

### 6.1 Audit Scope

1. Inventory repository roots, submodules, generated directories, build outputs, vendor folders, installer projects, update metadata, scripts, and ownership.
2. Record commit, dirty state, branch/tag, source archive hash, build host, CI run, environment lock, and every external input that can alter delivered bytes.
3. Distinguish developer interpreter, test interpreter, build interpreter, packaging interpreter, embedded interpreter, helper interpreter, and system Python.
4. Map source modules to generated code, bytecode, extension modules, resources, Qt plugins, executable, installer, update package, and installed files.
5. Record executable, package, installer, manifest, SBOM, signature, timestamp, and update metadata hashes.
6. Connect the installed process, loaded modules, Qt libraries, plugin paths, configuration, schema, feature flags, and telemetry release identity to the intended artifact.

### 6.2 Required Verification

1. Perform a clean environment resolve and build; compare dependency, generated-code, resource, and artifact manifests with CI and release records.
2. Inspect packaged and installed files, import origins, `sys.executable`, `sys.path`, `sys.prefix`, Qt library paths, plugin paths, and loaded native modules.
3. Verify that no writable search path, current directory, user plugin path, or stale file can shadow trusted Python or Qt components.
4. Launch the installed application on a clean machine or VM and record exact binary, command line, environment, working directory, libraries, and release identifiers.
5. Test update and rollback identity so the reported version, code, data schema, resources, and telemetry cannot disagree silently.

## 7. Repository, Architecture, And Ownership

### 7.1 Audit Scope

1. Map packages, application entrypoints, UI layers, domain services, data access, infrastructure adapters, workers, helpers, plugins, tests, packaging, and installer code.
2. Document process, thread, event-loop, QObject, model/view, QML, WebEngine, database, file, network, device, and privileged-helper boundaries.
3. Identify global state, service locators, singleton objects, circular imports, import-time side effects, hidden ownership, and mutable cross-feature dependencies.
4. List critical user journeys and business invariants with their source modules, UI entrypoints, data, side effects, and recovery path.
5. Distinguish UI state, domain state, persisted state, cached state, derived state, and operating-system state.
6. Record owners for code, data formats, signing, installer, update feed, telemetry, privacy, support, and incident response.

### 7.2 Required Verification

1. Produce architecture, ownership, data-flow, privilege, and lifecycle diagrams backed by source and runtime evidence.
2. Trace at least one critical journey end to end through UI, signals, services, persistence, external calls, error handling, telemetry, and recovery.
3. Confirm that dependency direction and ownership prevent UI code, plugin code, or background work from bypassing domain authorization and invariants.
4. Identify abandoned modules, duplicate implementations, unreachable code, stale generated output, and packaging-only code paths.
5. Verify that every critical resource has one explicit lifecycle owner and every cross-boundary call has a contract.

## 8. Python Runtime, ABI, GIL, Free-Threaded Mode, And JIT

### 8.1 Audit Scope

1. Record exact CPython version, vendor, build flags, architecture, debug/release status, ABI tag, `SOABI`, Unicode configuration, OpenSSL, and platform runtime.
2. Identify whether the build uses the traditional GIL, free-threaded mode, experimental JIT, debug allocator, sanitizers, or custom interpreter patches.
3. Map every C/C++/Rust extension, limited-API/abi3 wheel, ctypes/cffi binding, Shiboken wrapper, and native library to supported Python and platform ABIs.
4. Review reference ownership, finalizers, weak references, cyclic GC, shutdown order, exception hooks, import hooks, and signal handling.
5. Assess subinterpreters, embedded Python, isolated mode, virtual environments, zip imports, frozen modules, and user-site behavior if applicable.
6. Distinguish language-level thread safety from extension-level, Qt-level, database-level, file-level, and business-level concurrency safety.

### 8.2 Required Verification

1. Run the packaged application under the exact supported interpreter mode and exercise native extensions, shutdown, exceptions, and concurrency.
2. For free-threaded mode, require explicit compatibility evidence for PySide6, every native dependency, global state, callbacks, reference lifetimes, and third-party libraries.
3. For JIT or non-default builds, compare correctness, startup, memory, diagnostics, packaging, crash behavior, and rollback against the supported baseline.
4. Use debug builds, faulthandler, tracemalloc, sanitizers, or platform debuggers where appropriate to investigate native crashes and lifetime defects.
5. Reject an interpreter upgrade when required wheels, Qt bindings, packaging tools, native libraries, or operating-system targets are unsupported.

## 9. Dependencies, Environments, And Supply-Chain Trust

### 9.1 Audit Scope

1. Inventory `pyproject.toml`, requirements files, lock files, constraints, editable installs, VCS/path dependencies, private indexes, wheelhouses, and vendored code.
2. Determine the authoritative resolver and environment workflow: pip, uv, Poetry, PDM, pip-tools, Conda, Hatch, Rye legacy, system packages, or custom tooling.
3. Review build backends, PEP 517 isolation, dynamic metadata, setup hooks, package-data rules, namespace packages, entry points, and executable scripts.
4. Identify source distributions, compiled wheels, post-install steps, binary downloads, code generators, and packages that execute code during build or import.
5. Check dependency confusion, typosquatting, index precedence, mutable VCS references, compromised maintainers, abandoned packages, license obligations, and security advisories.
6. Separate runtime dependencies, packaging-only dependencies, development tools, test tools, optional extras, platform markers, and plugin ecosystems.

### 9.2 Required Verification

1. Resolve from a clean environment using the committed lock/constraints and compare hashes, versions, markers, wheel tags, and transitive graphs across CI and release.
2. Prefer verified wheels or reproducibly built artifacts; document every source build, native toolchain, external download, and trusted key.
3. Generate and review SBOM, license inventory, vulnerability report, provenance, and package signature/hash evidence for the release graph.
4. Test offline or controlled-index installation where required and prove that an unexpected public package cannot override a private name.
5. Fail the release for unresolved critical advisories, unreviewed executable hooks, unsupported binary wheels, or non-reproducible dependency resolution.

## 10. Generated Code, Resources, Configuration, And Feature Flags

### 10.1 Audit Scope

1. Inventory `.ui`, `.qrc`, QML cache, translation catalogs, protobuf/OpenAPI clients, ORM models, icons, themes, schemas, version files, and generated bindings.
2. Record generator executable, version, inputs, options, environment, output ownership, determinism, and regeneration command.
3. Map configuration precedence across defaults, bundled files, environment, command line, registry/plist, user settings, enterprise policy, remote config, and feature flags.
4. Distinguish public configuration from secrets and identify values copied into packages, logs, crash reports, or support bundles.
5. Review feature-flag ownership, targeting, expiry, offline behavior, fail-open/fail-closed behavior, and rollback dependencies.
6. Detect stale generated output, developer-local resources, missing translations, case-sensitive path differences, and source/package drift.

### 10.2 Required Verification

1. Regenerate from a clean checkout and fail on unexplained diff or missing toolchain.
2. Inspect the package and installed application to confirm the intended resources, translations, certificates, schemas, and configuration are present once and loaded from trusted locations.
3. Test precedence and malformed-value behavior without silently falling back to unsafe defaults.
4. Exercise flag enable, disable, stale cache, network loss, targeting change, emergency kill, and rollback scenarios.
5. Ensure sensitive values are injected at the correct runtime boundary and are absent from source control, package resources, logs, and telemetry.

## 11. Qt Application Lifecycle, QObject Ownership, And Destruction

### 11.1 Audit Scope

1. Map `QApplication` or `QGuiApplication` creation, singleton initialization, startup phases, splash, dependency construction, event-loop entry, shutdown, and restart.
2. For every critical QObject, record creator, parent, Python reference owner, thread affinity, consumers, destruction trigger, `deleteLater` behavior, and shutdown order.
3. Identify ownership mismatches between Python garbage collection and Qt parent-child deletion, dangling wrappers, resurrected references, and use-after-delete risks.
4. Review top-level windows, dialogs, tray icons, timers, network objects, threads, models, delegates, actions, and native resources for deterministic cleanup.
5. Inspect application state changes, session restore, suspend/resume, logout, user switching, and operating-system termination paths.
6. Distinguish normal close, hide-to-tray, forced termination, crash, update restart, installer shutdown, and operating-system logout semantics.

### 11.2 Required Verification

1. Instrument creation, affinity, signal connections, destruction, finalization, and shutdown for representative critical objects.
2. Test repeated open/close, login/logout, workspace switch, window recreation, tray restore, update restart, and application exit for leaks and stale callbacks.
3. Use weak references, `QPointer`, destroyed signals, debug assertions, and platform tools where appropriate to prove lifetime assumptions.
4. Verify that shutdown stops new work, cancels or drains existing work, flushes critical data, releases locks and devices, and exits within a defined deadline.
5. Reject fixes that merely keep objects alive globally or call garbage collection without correcting ownership.

## 12. Signals, Slots, Events, Reentrancy, And UI State

### 12.1 Audit Scope

1. Inventory critical signal-slot connections, connection types, lambdas/closures, queued arguments, event filters, custom events, and direct method calls across boundaries.
2. Identify duplicate connections, connection leaks, stale receivers, captured mutable state, retained objects, silent signature mismatch, and overloaded-signal ambiguity.
3. Review direct, queued, blocking queued, and auto connection behavior with actual sender and receiver thread affinity.
4. Assess nested event loops from modal dialogs, `processEvents`, synchronous waits, drag/drop, menus, native dialogs, and reentrant callbacks.
5. Map UI state transitions, enabled/disabled controls, focus, selection, progress, cancellation, optimistic changes, errors, retries, and rollback.
6. Ensure user-triggered actions cannot start duplicate non-idempotent work through double-click, shortcut, menu, tray, deep link, or restored state.

### 12.2 Required Verification

1. Log and test connection establishment, delivery thread, ordering, duplicate delivery, receiver destruction, disconnect, and shutdown.
2. Force rapid repeated input, modal reentrancy, delayed completion, out-of-order completion, cancellation, window closure, and account switch.
3. Verify that UI updates occur only on the GUI thread and that stale results are rejected using operation identity, generation, or current-context checks.
4. Replace `processEvents` or synchronous GUI waits with explicit asynchronous state machines unless a narrowly justified, tested use remains.
5. Prove that action gating, idempotency, and domain constraints work independently of button disabled state.

## 13. Threads, Tasks, Locks, Cancellation, And Backpressure

### 13.1 Audit Scope

1. Inventory `QThread`, worker-object patterns, `QThreadPool`, `QRunnable`, Python threads, executors, timers, queues, locks, semaphores, conditions, and background services.
2. Record owner, start condition, concurrency limit, input queue, cancellation contract, deadline, result delivery, exception path, join/drain behavior, and shutdown owner.
3. Identify subclassed-QThread misuse, work executing on the wrong thread, QObject moves after parenting, direct cross-thread UI access, and blocking queued deadlocks.
4. Review lock ordering, lock scope, callbacks under locks, signal emission under locks, database connections per thread, and native-library thread safety.
5. Check unbounded task submission, queue growth, large retained payloads, priority inversion, starvation, retry storms, and user-triggered concurrency amplification.
6. Distinguish cancellation request from completed cancellation and define behavior for non-cancellable native, file, database, device, and network work.

### 13.2 Required Verification

1. Run burst, sustained, cancellation, timeout, shutdown, worker-crash, queue-full, and dependency-slowdown scenarios with thread and queue instrumentation.
2. Use deterministic synchronization tests, faulthandler dumps, platform stack capture, and stress repetition to investigate races and deadlocks.
3. Verify bounded queues, admission control, progress coalescing, load shedding, retry budgets, and user-visible degraded states.
4. Prove that every background exception is observed, classified, reported, and either recovered or causes a controlled state transition.
5. Confirm that no worker, thread, timer, lock, device handle, or database connection survives logout, workspace switch, update restart, or shutdown unintentionally.

## 14. Asyncio, QtAsyncio, Qasync, And Multiple Event Loops

### 14.1 Audit Scope

1. Identify asyncio usage, QtAsyncio or qasync integration, loop policy, task groups, executors, async generators, network clients, and library-owned loops.
2. Document which loop owns each coroutine, how Qt and asyncio callbacks interleave, and where thread or process handoff occurs.
3. Review task creation, structured concurrency, cancellation propagation, timeout composition, shielded tasks, exception groups, and task retention.
4. Detect nested `asyncio.run`, loop creation in worker threads, blocking code on the loop, unobserved tasks, cross-loop futures, and shutdown warnings.
5. Assess compatibility of libraries that assume the main thread, a specific event-loop implementation, or Unix-only signal behavior.
6. Define offline, reconnect, retry, backpressure, application-close, logout, and update-restart behavior for asynchronous work.

### 14.2 Required Verification

1. Instrument task creation, completion, cancellation, exceptions, queue depth, loop lag, and shutdown across representative flows.
2. Test delayed and reordered responses, disconnect during await, cancellation during write, window destruction, account switch, and application exit.
3. Ensure cancellation reaches sockets, streams, files, database operations, child processes, and business workflows or is explicitly compensated.
4. Verify one clear integration strategy rather than accidental coexistence of independent GUI and asyncio loops.
5. Fail readiness when critical background tasks can become orphaned, silently fail, update stale UI, or prevent clean shutdown.

## 15. Subprocesses, Multiprocessing, IPC, And Local Services

### 15.1 Audit Scope

1. Inventory subprocesses, `multiprocessing`, helper executables, local agents, services, named pipes, Unix sockets, loopback HTTP, shared memory, and file-based IPC.
2. Record executable resolution, arguments, environment, working directory, privileges, ownership, authentication, framing, versioning, timeout, and shutdown.
3. Review shell usage, quoting, command injection, PATH hijacking, current-directory search, inherited handles, environment leakage, and writable executable locations.
4. Assess multiprocessing start methods, frozen-application bootstrap, recursive spawn, resource tracker behavior, shared-state consistency, and crash recovery.
5. Treat localhost and same-user IPC as attacker-reachable unless authentication, authorization, permissions, and peer identity are proven.
6. Define compatibility for old/new GUI, helper, service, protocol, schema, and update versions.

### 15.2 Required Verification

1. Launch from installed paths and adversarial working directories to prove trusted executable and library resolution.
2. Test malformed, oversized, reordered, replayed, unauthenticated, cross-user, stale-version, and partial IPC messages.
3. Force helper crash, GUI crash, timeout, pipe break, duplicate request, upgrade overlap, and shutdown during critical work.
4. Verify privilege separation, least-privilege service accounts, OS ACLs, peer credentials, request authorization, and signed/versioned helpers.
5. Confirm no orphan process, shared-memory segment, lock file, port listener, temporary secret, or half-applied side effect remains after failure.

## 16. Qt Widgets, Models, Views, Delegates, And Large Data

### 16.1 Audit Scope

1. Inventory windows, dialogs, stacked pages, dock widgets, actions, shortcuts, forms, tables, trees, lists, proxy models, delegates, and custom painting.
2. Review layout ownership, duplicate layout assignment, widget parenting, focus chains, tab order, modality, geometry persistence, and multi-monitor behavior.
3. For every model, verify index validity, parent/child relationships, row and column notifications, persistent indexes, reset semantics, sorting, filtering, and thread ownership.
4. Assess lazy loading, pagination, virtualization, fetch-more behavior, image/icon caching, large text, drag/drop, clipboard, and undo/redo.
5. Review delegate editors, validation, commit/close ordering, stale indexes, selection state, and concurrent model updates.
6. Distinguish presentation formatting from domain values, permissions, validation, persistence, and business invariants.

### 16.2 Required Verification

1. Exercise empty, small, large, malformed, rapidly changing, filtered, sorted, reordered, and concurrently refreshed datasets.
2. Use model testers, assertions, focused unit tests, and UI automation to validate notification order and index safety.
3. Measure scroll, resize, selection, editing, filtering, painting, and memory behavior at realistic maximum data sizes.
4. Test keyboard-only navigation, screen reader names/states, high DPI, text scaling, localization expansion, and right-to-left layouts.
5. Ensure model changes are marshalled to the GUI thread and stale asynchronous results cannot mutate a replaced model or selection.

## 17. Qt Quick, QML, Scene Graph, And JavaScript Boundaries

### 17.1 Audit Scope

1. Inventory QML modules, engines, contexts, singletons, registered Python types, image providers, JavaScript, shaders, animations, loaders, and remote/local resource origins.
2. Review QML ownership modes, context-property lifetime, binding loops, signal handlers, dynamic object creation, loader destruction, and engine teardown.
3. Assess Python objects exposed to QML, invokable methods, properties, signals, input validation, authorization, thread affinity, and exception propagation.
4. Inspect scene-graph render-thread interactions, custom QQuickItem code, graphics resources, image decoding, shaders, and platform backend differences.
5. Review JavaScript `eval`, dynamic import, network-loaded QML, local file access, URL handling, and untrusted data reaching executable expressions.
6. Measure binding churn, overdraw, texture memory, animation cost, frame pacing, startup compilation, and QML cache behavior.

### 17.2 Required Verification

1. Run QML warnings as test failures for critical flows and inspect packaged import paths, plugins, cache, and missing-module behavior.
2. Test engine recreation, logout, theme/locale changes, dynamic page loading, object destruction, graphics-device reset, and application shutdown.
3. Fuzz or validate every Python-QML boundary with malformed, oversized, stale, unauthorized, and cross-tenant data where applicable.
4. Profile render and GUI threads on each supported graphics backend and realistic low-end hardware.
5. Ensure remote or user-controlled content cannot load QML, JavaScript, plugins, shaders, or local resources outside an explicit trust policy.

## 18. Qt WebEngine, WebChannel, Browser Profiles, And Untrusted Content

### 18.1 Audit Scope

1. Inventory every WebEngine view, profile, page, process model, storage partition, cache, cookie store, download handler, permission request, certificate handler, and custom URL scheme.
2. Record all local and remote origins, navigation rules, popup behavior, external-open behavior, CSP, mixed content, service workers, DevTools access, and command-line switches.
3. Map WebChannel objects, exposed methods/properties/signals, origin binding, frame binding, argument validation, authorization, and lifetime.
4. Review JavaScript injection, HTML generation, local file access, `qrc` and custom-scheme privileges, clipboard, camera, microphone, geolocation, notifications, and screen capture.
5. Assess profile isolation between users, tenants, accounts, environments, and privileged/unprivileged content.
6. Treat web content as attacker-controlled unless origin, transport, content integrity, and update ownership are proven.

### 18.2 Required Verification

1. Test navigation to malicious, redirected, downgraded, local-file, custom-scheme, popup, iframe, and compromised-origin content.
2. Attempt WebChannel calls from unauthorized origins, frames, stale pages, restored sessions, and after account or environment changes.
3. Verify explicit allowlists for navigation, external opening, downloads, permissions, certificates, and custom-scheme resources.
4. Inspect packaged Chromium/Qt WebEngine versions and security support; verify sandbox/process behavior on each platform.
5. Confirm browser data, cookies, credentials, cache, downloads, and service workers are removed or isolated correctly on logout and uninstall.

## 19. Networking, TLS, Authentication, Retries, And Streaming

### 19.1 Audit Scope

1. Inventory QNetworkAccessManager instances, Python HTTP clients, WebSocket/SSE/gRPC clients, proxy configuration, DNS, certificate stores, and custom transports.
2. Record connection, TLS, request, read, write, total, idle, and pool-acquisition timeouts plus cancellation and deadline propagation.
3. Review certificate validation, hostname verification, redirects, proxy authentication, client certificates, pinning where justified, and rotation behavior.
4. Assess token acquisition, refresh serialization, expiry, revocation, logout, account switching, MFA/passkey flows, and secure browser handoff.
5. Check retry classification, idempotency, jitter, budget, circuit breaking, offline queueing, reconnect, resume, duplicate delivery, and replay.
6. For streaming and large transfers, review backpressure, partial files, checksums, disk limits, sparse files, cancellation, resume metadata, and cleanup.

### 19.2 Required Verification

1. Test slow DNS, TLS failure, certificate rotation, proxy changes, captive portal, offline transition, packet loss, partial response, malformed response, and server throttling.
2. Run concurrent expiry and refresh scenarios to prove one safe refresh path and correct failure propagation.
3. Verify that retries do not duplicate purchases, writes, uploads, downloads, device commands, or local state transitions.
4. Measure queue growth, memory, disk, UI responsiveness, and recovery during long-running or stalled transfers.
5. Confirm secrets and sensitive payloads are absent from URLs, proxy logs, debug traces, crash reports, telemetry, and support bundles.

## 20. Persistence, Settings, Databases, Migrations, And Offline State

### 20.1 Audit Scope

1. Inventory QSettings, JSON/YAML/TOML/XML files, SQLite, SQLAlchemy, ORM stores, caches, key-value databases, object stores, histories, queues, and temporary files.
2. Record schema and format versions, ownership, permissions, encryption, journaling, atomic-write strategy, locking, backup, retention, and deletion.
3. Review database connection ownership per thread/process, transaction boundaries, isolation, constraints, busy timeouts, WAL, checkpoints, corruption handling, and close order.
4. Assess concurrent application instances, crash during write, disk full, read-only media, antivirus locking, network home directories, and interrupted upgrade.
5. Map offline command queues, sync cursors, conflict resolution, deduplication, tombstones, clock assumptions, and reconciliation with server authority.
6. Distinguish user preferences from security policy, credentials, authorization state, business records, derived caches, and recoverable downloads.

### 20.2 Required Verification

1. Run migration matrices from every supported historical version using representative, large, malformed, partially migrated, and corrupted datasets.
2. Inject crashes before, during, and after atomic writes, commits, schema changes, cache replacement, and sync acknowledgement.
3. Test two application instances, stale locks, concurrent updates, account switching, rollback to an older binary, and forward repair.
4. Perform isolated backup restore and, where applicable, point-in-time recovery; measure and record achieved RPO and RTO.
5. Prove that logout, user deletion, retention expiry, uninstall, and support-bundle creation handle each data class according to policy.

## 21. Authorization, Secrets, Cryptography, Privacy, And Account Isolation

### 21.1 Audit Scope

1. Inventory identities, sessions, roles, permissions, tenants, accounts, workspaces, organizations, licenses, entitlements, and privileged operations.
2. Map every UI action, background action, deep link, plugin call, WebChannel call, IPC request, file operation, device command, and API mutation to server-side or trusted-boundary authorization.
3. Review OS credential stores, keyrings, DPAPI, Keychain, Secret Service, encrypted files, key derivation, random generation, key rotation, recovery, and deletion.
4. Distinguish authentication state, authorization state, cached display data, offline grants, license state, and server authority.
5. Assess local attackers, same-user processes, other OS users, stolen profiles, copied databases, memory inspection, logs, crash dumps, swap, and backups.
6. Record privacy purpose, minimization, consent, retention, export, deletion, telemetry, crash reporting, and regional requirements for each data class.

### 21.2 Required Verification

1. Execute positive and negative authorization tests for direct object access, stale UI, modified local state, deep links, plugins, IPC, offline mode, and account switching.
2. Verify secret storage and retrieval in the installed application, including backup/restore, key rotation, revoked credentials, and unavailable keyring behavior.
3. Confirm that clearing UI fields or deleting a config entry actually revokes sessions and removes sensitive local artifacts according to policy.
4. Inspect logs, telemetry, crash dumps, temporary files, clipboard, screenshots, recent-file lists, and support bundles for sensitive leakage.
5. Fail readiness when client-only checks protect server resources or when tenant/account identifiers are omitted from cache, queue, file, or telemetry isolation.

## 22. Plugins, Scripting, Dynamic Imports, Serialization, And Extension Points

### 22.1 Audit Scope

1. Inventory Python plugin systems, entry points, dynamic imports, user scripts, macros, templates, QML modules, native plugins, codecs, and third-party extensions.
2. Document discovery paths, trust source, signature or hash verification, compatibility contract, permissions, API surface, process isolation, update, disable, and removal.
3. Review `pickle`, `marshal`, `shelve`, unsafe YAML, object hooks, dynamic class loading, `eval`, `exec`, template execution, and expression engines.
4. Assess plugin access to filesystem, network, credentials, UI, clipboard, devices, database, updater, and privileged helpers.
5. Detect import shadowing, writable plugin paths, namespace collisions, dependency conflicts, ABI mismatch, crash propagation, and startup denial of service.
6. Define behavior for incompatible, corrupted, malicious, revoked, slow, crashing, or abandoned plugins.

### 22.2 Required Verification

1. Attempt plugin loading from user-writable, current-directory, removable-media, network-share, and tampered package locations.
2. Feed untrusted serialized objects, templates, expressions, scripts, and configuration; confirm strict formats and safe failure.
3. Test plugin timeout, crash, infinite loop, excessive memory, dependency conflict, API mismatch, update, revocation, and disable/recovery.
4. Use process isolation or a deliberately constrained capability model for untrusted extension code; document residual risk when true sandboxing is unavailable.
5. Reject arbitrary-code extension features presented as safe without explicit trust, distribution, permission, and incident controls.

## 23. Operating-System Integration, Devices, And Privileged Helpers

### 23.1 Audit Scope

1. Inventory file associations, URL schemes, deep links, autostart, tray, notifications, global shortcuts, clipboard, drag/drop, recent files, shell integration, and single-instance behavior.
2. Review camera, microphone, screen capture, location, Bluetooth, USB, serial, HID, smart card, printing, scanners, media keys, and other device permissions.
3. Map services, daemons, scheduled tasks, drivers, kernel extensions, privileged helpers, elevation prompts, and installer custom actions.
4. Validate all OS-delivered inputs: command line, environment, file-open events, URLs, notification actions, clipboard, drag/drop, device data, and registry/plist values.
5. Assess same-user process impersonation, symlink/junction attacks, TOCTOU, insecure temporary files, inherited permissions, and writable service/helper paths.
6. Define disconnect, reconnect, permission denial, device removal, sleep/resume, fast user switching, remote desktop, and OS update behavior.

### 23.2 Required Verification

1. Fuzz deep links, file associations, notification actions, clipboard, drag/drop, command-line arguments, and device payloads with malformed and oversized input.
2. Test least-privilege operation as standard user and verify explicit, narrow elevation only where required.
3. Verify helper identity, signature, version handshake, request authorization, ACLs, installation path, update order, rollback, and compromised-helper response.
4. Exercise permission denied, revoked permission, unavailable device, device replacement, sleep/resume, session lock, user switch, and shutdown.
5. Confirm uninstall removes or intentionally retains services, tasks, drivers, associations, permissions, and data according to documented policy.

## 24. Files, Archives, Media, Documents, Imports, And Exports

### 24.1 Audit Scope

1. Inventory every accepted and produced file format, parser, codec, archive, image, media, PDF, office, CSV, database, project, backup, and export path.
2. Record trust source, maximum size, expansion ratio, recursion depth, path rules, temporary storage, validation, sanitization, and cleanup.
3. Review path traversal, zip slip, symlink/hardlink abuse, alternate streams, special files, device paths, filename normalization, extension confusion, and overwrite behavior.
4. Assess parser memory/CPU limits, decompression bombs, malformed metadata, external references, macros, formulas, embedded content, and native codec vulnerabilities.
5. Validate atomic export, partial output, disk full, cancellation, existing files, permissions, network shares, removable media, and concurrent access.
6. Distinguish preview, validation, import, conversion, execution, external-open, and trusted-project semantics.

### 24.2 Required Verification

1. Use a malicious corpus and fuzz representative parsers in isolated environments; include oversized, recursive, truncated, polyglot, and path-manipulating samples.
2. Test import/export cancellation and crash at every write boundary; verify no misleading successful output or corrupted original remains.
3. Confirm temporary files use safe locations, restrictive permissions, unpredictable names, atomic replacement, and deterministic cleanup.
4. Verify external tools and codecs are resolved from trusted signed locations and receive safely quoted arguments and constrained resources.
5. Ensure user warnings describe actual risk and do not become the only control for executable or active content.

## 25. Packaging, Bundling, Installers, Signing, Updates, And Rollback

### 25.1 Audit Scope

1. Identify packaging tools, versions, spec/config files, hooks, hidden imports, exclusions, data files, Qt modules, plugin collection, native libraries, and runtime options.
2. Compare one-file, one-folder, app bundle, portable, installer, store, system-package, and enterprise deployment behavior where applicable.
3. Review bootloader/runtime trust, extraction directories, temporary execution, DLL/library search, resource integrity, antivirus interaction, and writable code paths.
4. Map code-signing identities, certificates, timestamp services, notarization, entitlements, package signing, key custody, approval, rotation, revocation, and loss recovery.
5. Document update metadata, transport, signature verification, channel, cohort, architecture/platform mapping, version ordering, downgrade policy, delta/full packages, install timing, and restart.
6. Define fresh install, upgrade, repair, interrupted install, interrupted update, rollback, forward repair, uninstall, data retention, and side-by-side channel behavior.

### 25.2 Required Verification

1. Build from a clean environment, inspect package manifests and binaries, and compare delivered files against an allowlisted bill of materials.
2. Install on clean machines as standard users and administrators; verify first run, permissions, shortcuts, associations, services, prerequisites, and uninstall.
3. Verify signatures and notarization after final packaging; prove that post-sign mutation or tampered update content is rejected.
4. Test update from every supported version/channel/architecture, offline interruption, disk full, process lock, antivirus delay, power loss, signature failure, and server rollback.
5. Prove recovery when an update starts but cannot complete, data schema advances, old binaries restart, signing keys are revoked, or the update service is compromised.

## 26. Windows Production Audit

### 26.1 Audit Scope

1. Review supported Windows versions, x64/ARM64, MSVC runtime, Universal CRT, WebView/graphics dependencies, DPI awareness, and code-page assumptions.
2. Inspect PE imports, manifests, Authenticode, timestamp, catalog/signature chain, DLL search order, side-by-side assemblies, and packaged Qt platform plugins.
3. Assess MSI/MSIX/EXE/portable installer behavior, per-user versus per-machine scope, UAC, registry, services, scheduled tasks, firewall, file associations, and repair.
4. Review DPAPI, Credential Manager, ACLs, junctions, reparse points, named pipes, AppData/ProgramData/Program Files locations, and multi-user isolation.
5. Test high DPI, multiple monitors, Remote Desktop, session lock, fast user switching, sleep/resume, dark mode, input methods, and accessibility tools.
6. Define SmartScreen reputation, certificate renewal, enterprise deployment, antivirus/EDR interaction, update, rollback, and uninstall support.

### 26.2 Required Verification

1. Verify the final installed executable and every shipped DLL/plugin with trusted inspection tools and signature-chain validation.
2. Launch from adversarial working directories and with modified PATH to detect DLL or executable hijacking.
3. Test standard-user install/use/update/uninstall, elevation boundaries, another OS user, roaming/non-roaming profiles, and locked files.
4. Exercise display scaling combinations, monitor removal, RDP reconnect, graphics fallback, accessibility, locale, and IME scenarios.
5. Validate update and rollback across certificate renewal, reboot-required files, running helper processes, and enterprise security software.

## 27. macOS Production Audit

### 27.1 Audit Scope

1. Review supported macOS versions, Intel/Apple Silicon, universal binaries, deployment target, SDK/Xcode, hardened runtime, sandbox, and Rosetta assumptions.
2. Inspect app bundle structure, Mach-O architectures, load commands, rpaths, frameworks, dylibs, Qt plugins, resources, Info.plist, entitlements, and helper apps.
3. Assess Developer ID or App Store signing, nested-code signing order, secure timestamp, notarization, stapling, Gatekeeper, quarantine, and designated requirements.
4. Review Keychain access groups, application groups, bookmarks, file access, privacy usage descriptions, TCC permissions, launch agents, and privileged helpers.
5. Test Retina/high DPI, multiple displays, spaces, full screen, sleep/wake, screen lock, locale/input methods, accessibility, and system appearance.
6. Define DMG/PKG/store installation, app translocation, update framework, key/certificate renewal, rollback, and uninstall/data-retention behavior.

### 27.2 Required Verification

1. Verify every nested binary and resource seal after final packaging and confirm notarization acceptance and stapled ticket where applicable.
2. Test clean download with quarantine, first launch, translocation-sensitive paths, standard-user operation, permission denial/revocation, and another macOS user.
3. Exercise Intel, Apple Silicon, and universal paths where supported; detect accidental Rosetta-only helpers or architecture-mismatched plugins.
4. Test TCC prompts, revoked permissions, Keychain locked/unavailable, sleep/wake, display changes, VoiceOver, locale, and IME.
5. Validate update and rollback when the app is running, helpers are active, data schema changes, certificates rotate, or notarization/update services fail.

## 28. Linux Production Audit

### 28.1 Audit Scope

1. Review supported distributions, glibc/musl baseline, x86_64/ARM64, desktop environments, Wayland/X11, graphics drivers, portals, and system library assumptions.
2. Inspect ELF architecture, interpreter, RPATH/RUNPATH, bundled/shared libraries, symbol versions, Qt plugins, platform themes, codecs, and license obligations.
3. Assess AppImage, Flatpak, Snap, deb, rpm, tarball, distribution repository, system package, and portable deployment behavior.
4. Review filesystem permissions, XDG paths, Secret Service/KWallet, D-Bus, Unix sockets, udev rules, systemd units, polkit, sandbox permissions, and multi-user isolation.
5. Test Wayland and X11, multiple desktop environments, fractional scaling, remote sessions, screen lock, sleep/resume, accessibility, input methods, and headless failure.
6. Define repository signing, package updates, delta behavior, rollback, dependency removal, uninstall, and retained data.

### 28.2 Required Verification

1. Run dependency and symbol inspection on the final artifact and launch on the minimum supported clean distribution images.
2. Test missing optional libraries, old drivers, Wayland/X11 switching, portal denial, sandbox restrictions, and read-only or noexec locations.
3. Verify package/repository signatures, update metadata, architecture mapping, downgrade behavior, and cross-package-manager conflicts.
4. Exercise standard-user use, another user, locked secret store, system sleep, display changes, screen readers, locale, and IME.
5. Confirm uninstall removes integrations and helpers without deleting user data outside documented policy.

## 29. Performance, Responsiveness, Memory, CPU, GPU, Disk, And Capacity

### 29.1 Audit Scope

1. Define budgets for cold/warm startup, first interactive state, critical journey latency, GUI-thread stall, frame time, memory, CPU, GPU, disk, network, package size, and update size.
2. Measure import time, module initialization, resource loading, font and icon loading, QML compilation, database startup, network initialization, and first-window rendering.
3. Profile GUI thread, render thread, Python threads, native threads, event-loop lag, lock waits, queue waits, allocation, object retention, native heap, textures, and handles.
4. Assess large datasets, images, media, documents, caches, histories, undo stacks, background transfers, devices, multiple windows, and long sessions.
5. Review batching, coalescing, pagination, lazy loading, caching, prefetch, compression, worker limits, and degraded modes with correctness constraints.
6. Define supported device classes, minimum hardware, headroom, concurrency, maximum project/data size, disk requirements, and failure thresholds.

### 29.2 Required Verification

1. Run cold, warm, burst, sustained, soak, low-memory, disk-pressure, offline, dependency-slowdown, and multi-window workloads on representative hardware.
2. Capture repeatable before/after measurements with exact artifact, data set, environment, sampling, and statistical summary.
3. Use Python and native profilers, Qt tools, operating-system traces, heap snapshots, handle inspection, and graphics diagnostics as appropriate.
4. Test cancellation and cleanup after large operations so memory, temporary files, threads, queues, and handles return to acceptable baselines.
5. Reject optimizations that weaken validation, authorization, durability, accessibility, diagnostics, or recovery without an explicit approved tradeoff.

## 30. Accessibility, Localization, Visual Correctness, And Error UX

### 30.1 Audit Scope

1. Inventory supported languages, scripts, locales, time zones, calendars, numbering, currencies, units, plural rules, input methods, themes, contrast modes, and motion preferences.
2. Review accessible names, roles, states, descriptions, relationships, live updates, focus order, keyboard operation, shortcuts, mnemonics, and screen-reader output.
3. Assess text scaling, high DPI, fractional scaling, long translations, right-to-left layout, bidirectional text, emoji, combining marks, truncation, and font fallback.
4. Review color contrast, non-color indicators, focus visibility, target size, reduced motion, flashing, animation cancellation, and graphics alternatives.
5. Map user-visible error states for validation, permission denial, offline, timeout, partial failure, cancellation, corrupted data, update failure, and recovery.
6. Ensure errors are actionable without exposing secrets, stack traces, internal paths, identifiers, or misleading success states.

### 30.2 Required Verification

1. Test critical journeys with keyboard only, screen readers, high contrast, 200 percent or policy-required text scaling, RTL, long translations, and reduced motion.
2. Run packaged builds on each platform because native accessibility bridges, fonts, menus, dialogs, and shortcuts differ from source tests.
3. Verify focus and announcements during asynchronous progress, validation failure, modal dialogs, notifications, page replacement, and error recovery.
4. Test locale and time-zone changes, ambiguous dates, daylight-saving transitions, Unicode filenames, and mixed-script input.
5. Require screenshots or recordings for visual regressions and accessibility evidence where automation is insufficient.

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

## 32. Observability, Diagnostics, Crash Reporting, And Supportability

### 32.1 Audit Scope

1. Inventory structured logs, audit events, metrics, traces, crash reporting, native dumps, Python exception hooks, Qt messages, performance traces, and support bundles.
2. Record release, artifact hash, channel, platform, architecture, Python, Qt, PySide6, packaging mode, data schema, configuration, account/tenant pseudonym, and feature flags where privacy permits.
3. Review log levels, cardinality, sampling, retention, redaction, local storage, upload consent, offline buffering, exporter failure, and support access.
4. Ensure GUI-thread stalls, worker failures, deadlocks, queue growth, memory pressure, update failure, migration failure, device disconnect, and data corruption are diagnosable.
5. Define health and readiness for local helpers, services, databases, update channels, network dependencies, and critical background workers.
6. Map user-facing incident IDs to privacy-safe technical evidence without exposing secrets or internal implementation details.

### 32.2 Required Verification

1. Force representative failures and verify the installed application emits sufficient, correlated, redacted evidence and actionable user guidance.
2. Confirm crash and support artifacts can identify exact delivered bytes and loaded native components, not only a marketing version.
3. Test offline buffering, disk full, exporter outage, permission denial, crash-loop rate limiting, and user opt-out behavior.
4. Verify support-bundle generation is bounded, cancellable, consented, redacted, reviewable, and safe against symlink/path attacks.
5. Define dashboards, alerts, runbooks, owners, escalation, and release-correlation procedures for material production signals.

## 33. CI/CD, Artifact Promotion, Release Governance, And Supply Chain

### 33.1 Audit Scope

1. Map repository, branch protection, review, CI runners, reusable workflows, caches, artifacts, package indexes, signing services, notarization, stores, update feeds, and deployment approvals.
2. Distinguish trusted and untrusted code paths, especially forks, pull requests, dependency update bots, self-hosted runners, and generated artifacts.
3. Review workflow injection, command quoting, secrets exposure, mutable action references, cache poisoning, artifact substitution, environment approvals, and OIDC scope.
4. Require locked and verified dependencies, pinned toolchains, controlled external downloads, SBOM, provenance, signature, and vulnerability/license gates.
5. Build once per target and promote the same immutable bytes through test, signing, staging, and production where platform rules allow.
6. Define release ownership, segregation of duties, emergency path, key compromise, package-index compromise, runner compromise, and trusted rebuild.

### 33.2 Required Verification

1. Reproduce release builds from clean runners and compare dependency, resource, native-library, package, and installer manifests and hashes.
2. Prove that untrusted code cannot read signing keys, publish packages, mutate release artifacts, poison trusted caches, or approve production.
3. Verify signatures, provenance, SBOM, release notes, version metadata, and update metadata all refer to the same reviewed bytes.
4. Exercise credential expiry, signing-service outage, notarization failure, store rejection, compromised dependency, revoked key, and emergency rebuild.
5. Keep an auditable record of approver, source commit, toolchains, dependencies, artifact hashes, signatures, channels, cohort, rollout, abort, and rollback.

## 34. Install, Upgrade, Migration, Rollback, Restore, And Disaster Recovery

### 34.1 Audit Scope

1. Inventory all supported starting versions, channels, architectures, installation scopes, data schemas, configuration versions, plugins, helpers, and operating-system states.
2. Define fresh install, first run, upgrade, repair, side-by-side install, channel switch, architecture migration, downgrade, uninstall, reinstall, and profile transfer.
3. Map every data and configuration migration with precondition, transaction or atomicity, backup, compatibility window, failure state, retry, forward repair, and rollback limits.
4. Distinguish application rollback, configuration rollback, feature rollback, updater rollback, helper rollback, data rollback, and server-side compatibility.
5. Document backup coverage, encryption, off-device copies, retention, corruption detection, restore tooling, operator procedure, RPO, and RTO.
6. Define behavior when old and new binaries, helpers, plugins, schemas, update metadata, and server APIs overlap.

### 34.2 Required Verification

1. Execute the supported upgrade matrix with representative data, plugins, accounts, settings, interrupted operations, and low-resource conditions.
2. Inject failure before, during, and after package replacement, migration, helper update, service restart, metadata switch, and first launch.
3. Prove that rollback does not silently corrupt newer data and that forward repair or data reconciliation is available when reverse migration is unsafe.
4. Perform isolated restore from real backups on clean machines and measure achieved RPO and RTO, including keyring and certificate dependencies.
5. Document exact manual recovery for boot failure, crash loop, broken updater, corrupted profile, revoked certificate, lost signing key, and unavailable backend.

## 35. Incident Response, Containment, Forensics, And Trusted Rebuild

### 35.1 Audit Scope

1. Define incident classes for malicious package or plugin, dependency compromise, credential theft, signing-key compromise, update-feed tampering, helper/service compromise, data corruption, and privacy breach.
2. Map evidence sources: repository, CI, package indexes, build logs, provenance, signatures, update metadata, installed files, process/module lists, logs, dumps, databases, and network telemetry.
3. Define containment controls: disable feed, revoke key or token, block package/version, pause rollout, disable plugin or feature, isolate host, stop writes, and preserve evidence.
4. Distinguish cleanup from trusted rebuild; a compromised interpreter, package, helper, updater, signing system, or host cannot be trusted merely because suspicious files were deleted.
5. Document credential rotation, certificate revocation, user notification, legal/privacy escalation, clean-room rebuild, restored data validation, and re-enrollment.
6. Define exit criteria, heightened monitoring, retrospective actions, owner, and verification that the original root cause and persistence mechanisms are removed.

### 35.2 Required Verification

1. Run a tabletop or technical exercise for at least the highest-impact applicable incident class.
2. Verify rapid identification of affected commits, dependencies, artifacts, signatures, channels, installed versions, users, data, and credentials.
3. Prove revocation, update disablement, kill switch, safe-mode startup, plugin quarantine, write freeze, and trusted replacement mechanisms.
4. Rebuild from known-good source and trusted toolchains on clean infrastructure; compare hashes, provenance, SBOM, signatures, and behavior.
5. Test recovery communication and operator runbooks without exposing sensitive forensic or personal data.

## 36. Mandatory Evidence Matrices

### 36.1 M1 - Source, interpreter, dependency, generated-code, artifact, signature, installed-runtime, and telemetry identity.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.2 M2 - Supported operating system, architecture, Python, Qt, PySide6, packaging mode, graphics backend, and distribution channel.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.3 M3 - Process, thread, event loop, QObject, model, QML engine, WebEngine profile, helper, device, and shutdown ownership.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.4 M4 - Signal, slot, connection type, sender thread, receiver thread, lifetime, ordering, cancellation, and stale-result protection.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.5 M5 - Identity, role, tenant/account, resource, operation, trusted boundary, authorization rule, negative test, and evidence.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.6 M6 - Local data class, owner, path/store, schema, permissions, encryption, migration, backup, retention, deletion, and restore.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.7 M7 - External input or file format, parser, limits, trust, sandbox/isolation, side effects, malicious tests, and cleanup.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.8 M8 - Dependency/native library, source, version, hash/signature, ABI, license, advisory status, package inclusion, and update owner.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.9 M9 - Package/installer/update artifact, platform, architecture, hash, signature, timestamp, channel, install test, update test, and rollback.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.10 M10 - Critical journey, invariant, concurrency/idempotency rule, failure points, persisted state, external side effects, compensation, and reconciliation.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.11 M11 - SLI/budget, workload, platform/hardware, measurement, threshold, result, headroom, alert, and owner.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

### 36.12 M12 - Release step, approver, artifact, migration, cohort, guardrail, abort, rollback/forward repair, restore, and evidence.

1. Populate every applicable row with owner, status, evidence level, exact artifact or runtime identity, and unresolved gap.
2. Link each material finding, fix, test, release gate, rollback, and residual risk to the relevant rows.
3. Do not mark the matrix complete when a platform, architecture, user type, data version, or failure path is represented only by assumption.

## 37. Mandatory Adversarial And Failure Scenarios

### 37.1 S1 - Rapid repeated UI action starts duplicate non-idempotent work.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.2 S2 - Window, model, or account changes before a delayed worker result returns.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.3 S3 - QObject receiver is destroyed while signals, timers, network replies, or callbacks remain queued.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.4 S4 - GUI thread is blocked, reentered, or updated directly from a worker.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.5 S5 - Worker, asyncio task, subprocess, or helper crashes during a critical operation.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.6 S6 - Application closes, logs out, changes workspace, sleeps, or updates during in-flight work.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.7 S7 - Disk becomes full, read-only, locked, slow, or unavailable during write, migration, download, or update.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.8 S8 - Two application instances or stale locks modify the same local state.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.9 S9 - Network becomes slow, offline, redirected, proxied, certificate-rotated, or partially responsive.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.10 S10 - Authentication expires concurrently and refresh, logout, revocation, or account switching races.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.11 S11 - Unauthorized deep link, IPC, WebChannel, plugin, local file, or modified local state attempts a privileged action.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.12 S12 - Malformed, oversized, recursive, polyglot, or path-traversing file reaches an import or preview path.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.13 S13 - Writable current directory, PATH, plugin path, temp path, or user directory attempts module, DLL, helper, or resource hijacking.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.14 S14 - Queue, thread pool, event loop, memory, handles, disk, or GPU becomes saturated under burst and soak load.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.15 S15 - Native extension, Qt plugin, codec, driver, or graphics backend is missing, incompatible, or crashes.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.16 S16 - Installer or updater is interrupted, tampered, out of disk, blocked by antivirus, or cannot replace running files.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.17 S17 - Old and new binaries, helpers, plugins, schemas, or server APIs overlap during staged rollout and rollback.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.18 S18 - Signing certificate or update key expires, rotates, is revoked, or is suspected compromised.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.19 S19 - Backup restore occurs on a clean machine with missing keyring, changed paths, different user, or newer operating system.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

### 37.20 S20 - Malicious dependency, plugin, helper, package, or build runner requires containment and trusted rebuild.

1. Define setup, trigger, expected invariant, observable evidence, cleanup, and pass/fail criterion.
2. Run on the narrowest safe isolated environment first and expand to packaged production-like conditions.
3. Record whether prevention, detection, containment, recovery, user guidance, and telemetry all behaved as designed.

## 38. Severity And Release Decision

### 38.1 P0-P3 Interpretation

| Severity | Meaning | Default action |
| --- | --- | --- |
| P0 | Active compromise, arbitrary code execution, signing/update compromise, irreversible widespread data loss, or immediate critical safety/business impact. | Stop release or operation; contain, preserve evidence, and recover. |
| P1 | High-likelihood severe security, authorization, data-integrity, crash-loop, update, migration, or rollback failure affecting material users. | Block release until fixed and verified or explicitly risk-accepted by authorized owners. |
| P2 | Material reliability, performance, accessibility, operability, privacy, maintainability, or compatibility defect with bounded impact. | Remediate before release when applicable or schedule with owner, deadline, controls, and acceptance criteria. |
| P3 | Low-risk improvement, cleanup, documentation, test depth, or optional modernization. | Prioritize transparently; do not present as a blocker without evidence. |

### 38.2 Verdicts

1. `READY`: all applicable production evidence and Definition of Done conditions are satisfied with no unresolved blocking risk.
2. `READY_WITH_CONDITIONS`: no unresolved P0/P1 blocker, but explicit bounded conditions, owners, dates, controls, and evidence ceilings remain.
3. `NOT_READY`: one or more blocking security, correctness, data, packaging, platform, update, rollback, restore, or operational conditions remain.
4. `INCIDENT`: active or suspected compromise, unsafe release channel, corrupted state, or untrusted build/runtime requires containment and trusted recovery.
5. Never convert lack of evidence into a positive verdict; state `UNVERIFIED` and the exact missing proof.

## 39. Production Readiness Checklist

1. Source-to-installed-runtime identity is continuous and reproducible for every supported release target.
2. Exact Python, PySide6, Qt, native libraries, packaging tools, and operating-system support are current and verified.
3. Architecture, ownership, process, thread, QObject, model, QML, WebEngine, IPC, data, privilege, and update maps are complete.
4. No unresolved P0 or P1 finding remains without explicit authorized acceptance and containment.
5. GUI thread, event loops, workers, tasks, subprocesses, helpers, cancellation, shutdown, and stale-result protection are verified.
6. QObject ownership, destruction, signals, slots, reentrancy, model/view notifications, and UI state are correct under stress.
7. Authentication, authorization, tenant/account isolation, secret storage, privacy, and privileged actions are verified with negative tests.
8. Local data, migrations, concurrency, offline queues, corruption handling, backup, retention, deletion, and restore are verified.
9. Files, archives, parsers, plugins, scripts, WebEngine content, deep links, IPC, devices, and OS inputs are constrained and tested.
10. Packaging includes only intended files and native components; package, installer, signature, notarization, and installed state are verified.
11. Fresh install, upgrade matrix, interrupted update, rollback/forward repair, uninstall, and clean-machine restore are tested.
12. Performance, responsiveness, memory, CPU, GPU, disk, network, capacity, and low-resource behavior meet measured budgets.
13. Accessibility, localization, high DPI, multiple monitors, screen readers, keyboard operation, RTL, IME, and reduced motion are tested.
14. Observability identifies exact release bytes and diagnoses critical GUI, worker, update, migration, data, and native failures without leaking sensitive data.
15. CI/CD protects trusted release boundaries, verifies dependencies, produces SBOM/provenance, and promotes immutable artifacts.
16. Rollout, abort, emergency release, signing-key compromise, update-feed compromise, incident containment, and trusted rebuild are documented and exercised.
17. Every material fix has focused regression, packaged verification, owner, risk, and rollback.
18. All applicable evidence matrices and adversarial scenarios are complete or explicitly blocked with owner and acceptance plan.
19. Final diff is narrow, reviewable, documented, and free of unrelated changes or weakened tests.
20. Final report contains exact evidence, commands, artifacts, hashes, results, blockers, residual risk, owners, and authoritative sources.

## 40. Definition Of Done

1. The current repository, environment, toolchain, package, installed application, runtime, and production-like state have been distinguished explicitly.
2. All critical journeys and invariants have evidence-backed ownership, failure behavior, recovery, and tests.
3. Every confirmed P0-P2 finding has root cause, minimal complete fix or approved plan, regression proof, release impact, and owner.
4. No critical claim relies only on source inspection when packaged, installed, runtime, upgrade, rollback, or restore evidence is required.
5. All supported platform and architecture combinations have current support evidence or are explicitly removed from claims.
6. Concurrency, QObject lifetime, cancellation, shutdown, account switching, duplicate actions, and stale results are safe.
7. Local data and external side effects remain consistent under duplicate, concurrent, interrupted, and crash conditions.
8. Package contents, signatures, installer, updater, and installed search paths resist tampering and hijacking.
9. Fresh install, upgrade, repair, rollback/forward repair, uninstall, backup, and restore are operationally usable.
10. Performance and accessibility conclusions are measured on packaged builds and representative hardware.
11. Observability and support evidence are sufficient, correlated, bounded, and privacy-safe.
12. CI/CD, signing, promotion, rollout, abort, incident, revocation, and trusted rebuild controls are reviewable and tested where material.
13. All commands, skipped checks, failures, artifacts, hashes, screenshots, traces, and residual risks are recorded truthfully.
14. Unrelated files and user work are preserved; the final change set is minimal and reviewable.
15. The final verdict follows the evidence ceiling and does not overstate security, compatibility, testing, or recovery.

## 41. Forbidden Shortcuts

1. Do not declare success because the application starts from source, a unit suite passes, or one unsigned package launches on the developer machine.
2. Do not call `processEvents`, sleep on the GUI thread, move UI work to arbitrary threads, or keep objects globally alive merely to hide lifecycle defects.
3. Do not update widgets or models directly from workers, ignore thread affinity, or assume the GIL makes Qt and business state thread-safe.
4. Do not enable free-threaded mode, JIT, a new Python major, or a new Qt major without native dependency, packaging, platform, and rollback evidence.
5. Do not silence exceptions, Qt warnings, failed futures, unhandled tasks, type errors, linter results, packaging warnings, signature failures, or migration errors without root-cause analysis.
6. Do not add broad `except`, empty handlers, arbitrary sleeps, forced garbage collection, unchecked casts, global mutable state, or blanket suppressions as universal fixes.
7. Do not deserialize untrusted pickle/YAML/object data, execute user input, load arbitrary plugins, or compile untrusted QML/JavaScript/templates.
8. Do not build shell commands from interpolated input, trust localhost automatically, open arbitrary URLs, or search writable paths for code and helpers.
9. Do not disable TLS validation, accept all certificates, store secrets in plain settings, or log tokens, credentials, personal data, or cryptographic material.
10. Do not broaden file, device, plugin, WebChannel, IPC, helper, service, or installer permissions merely to make a feature work.
11. Do not treat PyInstaller/Nuitka/Qt bundling, obfuscation, code signing, antivirus approval, or OS sandboxing as a complete security boundary.
12. Do not auto-migrate or reset data without backup and failure semantics; do not silently delete corrupted profiles or user files.
13. Do not publish mutable or unsigned artifacts, rebuild different bytes per environment without reason, or let untrusted CI access signing and production channels.
14. Do not raise thread, queue, timeout, retry, memory, disk, parser, or transfer limits without capacity and abuse analysis.
15. Do not claim Windows, macOS, Linux, x64, ARM64, high DPI, accessibility, update, rollback, or restore support without applicable packaged evidence.
16. Do not mass-format, delete unrelated files, weaken tests, hide failed checks, or overwrite another person's work.
17. Do not call the application perfect, fully secure, fully tested, or production-ready without satisfying the applicable evidence and recovery requirements.

## 42. Mandatory Final Report

1. Executive summary and verdict: `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`, or `INCIDENT`, with evidence ceiling.
2. Application and release context: purpose, critical journeys, platforms, architectures, Python/Qt stack, distribution, identities, data, integrations, and constraints.
3. Source-to-installed-runtime identity chain with exact commits, environments, dependency graph, generated code, artifact hashes, signatures, installed paths, and unresolved breaks.
4. Architecture and trust maps: process, thread, event loop, QObject, UI/model, QML/WebEngine, IPC/helper, data, device, privilege, installer, and update.
5. Version/support table: project, resolved, packaged/runtime, current supported line, status, compatibility, action, and primary source.
6. Findings table: `ID | P0-P3 | confidence | evidence | platform | file/symbol | cause | impact | fix | test | rollback | status | owner`.
7. Implemented changes: exact files, dependencies, generated output, configuration, permissions, migrations, package/installer/update changes, and regression risk.
8. Actual commands: command, directory, environment/tool versions, platform, exit code, output summary, artifacts, and conclusion.
9. Test matrix: unit, integration, GUI, package, install, update, adversarial, performance, accessibility, rollback, restore, and blocked checks.
10. Package and distribution verification: contents, native libraries, hashes, signatures, notarization, stores, channels, update metadata, cohort, install, and uninstall.
11. Data and recovery results: migrations, concurrent/duplicate/interrupted operations, corruption, backup, restore, RPO, RTO, rollback, forward repair, and reconciliation.
12. Security and privacy summary: authorization, account isolation, secrets, files, plugins, WebEngine, IPC, devices, local services, telemetry, supply chain, and residual risk.
13. Operational readiness: budgets, telemetry, alerts, runbooks, staged rollout, abort, emergency release, key compromise, incident containment, and owners.
14. Remaining work grouped as `blocks production`, `needed soon`, `planned refactor`, and `optional`, with owner, dependency, acceptance criterion, and target date.
15. External sources consulted: title, URL, version/status, access date, and decision informed.

## 43. Required Work Order

1. Protect workspace, user data, credentials, signing material, update channels, and forensic evidence.
2. Inventory repository, generated files, environments, dependencies, native libraries, toolchains, packaging, installers, and owners.
3. Establish source-to-installed-runtime identity and current support baseline.
4. Run clean resolve, build, static, unit, and focused baselines without destructive changes.
5. Map architecture, processes, threads, event loops, QObjects, UI/model/QML/WebEngine, data, IPC, devices, privileges, and OS integrations.
6. Audit lifecycle, ownership, signals, concurrency, cancellation, shutdown, stale results, and account switching.
7. Audit authorization, secrets, privacy, network, persistence, files, plugins, native code, helpers, and external inputs.
8. Build and inspect real packages; verify signatures, installers, update feeds, installed state, and search paths.
9. Reproduce and classify findings with root cause, evidence, impact, and release relevance.
10. Implement authorized minimal fixes and focused regression tests.
11. Execute packaged platform, adversarial, performance, accessibility, install, update, rollback, restore, and incident verification.
12. Complete evidence matrices, release decision, roadmap, Definition of Done, and final report.

## 44. Primary Source Register

| Source | URL | Use |
| --- | --- | --- |
| Python Downloads | https://www.python.org/downloads/ | Current stable and prerelease status. |
| Python 3.14 Documentation | https://docs.python.org/3.14/ | Runtime, language, free-threaded mode, JIT, packaging, and standard-library behavior. |
| Python Release Status | https://devguide.python.org/versions/ | Support phases and release managers. |
| Python Packaging User Guide | https://packaging.python.org/ | Packaging standards, dependency and environment guidance. |
| PySide6 on PyPI | https://pypi.org/project/PySide6/ | Current package version, Python requirement, wheel platforms, and metadata. |
| Qt for Python Documentation | https://doc.qt.io/qtforpython-6/ | PySide6 modules, deployment, tools, examples, and release notes. |
| Qt 6 Documentation | https://doc.qt.io/qt-6/ | Qt lifecycle, threading, model/view, QML, WebEngine, platform, and deployment behavior. |
| Qt Supported Platforms | https://doc.qt.io/qt-6/supported-platforms.html | Official operating-system, compiler, and architecture support. |
| PyInstaller Documentation | https://pyinstaller.org/en/stable/ | Bootloader, hooks, package modes, platform support, and runtime behavior. |
| Nuitka Documentation | https://nuitka.net/doc/user-manual.html | Compilation, standalone deployment, plugins, and platform behavior. |
| Microsoft Code Signing | https://learn.microsoft.com/windows-hardware/drivers/dashboard/code-signing-reqs | Windows signing and publisher trust context. |
| Apple Notarization | https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution | macOS signing, notarization, and Gatekeeper trust. |
| OWASP Desktop App Security | https://owasp.org/www-project-desktop-app-security-top-10/ | Desktop threat taxonomy used only as a starting point for concrete evidence. |

