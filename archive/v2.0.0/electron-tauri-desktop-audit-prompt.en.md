---
prompt_id: electron-tauri-desktop-production-audit
version: 2.0.0
title: Electron and Tauri Desktop Application Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, And Release Verification Of Electron / Tauri Desktop Applications

Use this prompt to inspect, safely repair, harden, test, package, sign, distribute, update, roll back, and recover a real desktop application built with Electron, Tauri, or a mixed web/native desktop stack. Audit the complete path from repository and toolchain resolution to the exact installed binary, privileged bridge, local data, operating-system integration, update channel, signing identity, telemetry, and recovery procedure.

The target may be a Windows, macOS, or Linux desktop product; a kiosk, tray, launcher, editor, media client, enterprise client, offline-first tool, hardware companion, VPN or local-agent UI, auto-updating commercial application, store-distributed package, or a desktop shell around local and remote services.

## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, and relevant paths | `[PATHS / URLS]` |
| Framework and application type | `[ELECTRON / TAURI / MIXED / UNKNOWN]` |
| Business purpose and critical journeys | `[FLOWS / INVARIANTS]` |
| Supported operating systems and architectures | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / OTHER]` |
| Distribution formats and channels | `[INSTALLER / STORE / ENTERPRISE / PORTABLE / AUTO-UPDATE]` |
| Identity, licensing, payments, and privileged operations | `[SYSTEMS / OWNERS]` |
| Local stores, files, caches, and secrets | `[LOCATIONS / FORMATS / OWNERS]` |
| Remote services, origins, and network trust | `[APIS / ORIGINS / PROXIES / CERTIFICATES]` |
| Signing, notarization, and update infrastructure | `[KEYS / PROVIDERS / FEEDS / CHANNELS]` |
| Availability, startup, latency, and resource targets | `[SLO / BUDGETS]` |
| Privacy, compliance, data residency, and retention | `[RULES / REGIONS]` |
| Known incidents, defects, and planned migrations | `[CONTEXT]` |
| Production access and change authorization | `[READ / WRITE / APPROVERS]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Missing Information Policy

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository content, lock files, resolved dependency graphs, build output, packaged artifacts, signatures, installed state, runtime evidence, telemetry, and authoritative documentation.
3. Mark unresolved assumptions as `UNVERIFIED` and state the exact evidence, platform, credential, approval, or hardware required to resolve them.
4. Ask only for access, approval, credentials, business decisions, or physical devices that materially block confirmation or safe repair.
5. Never treat a README, green CI job, successful dev startup, unsigned package, or one-platform smoke test as proof of production correctness.
6. When installed or production evidence is unavailable, state the evidence ceiling and do not issue an unconditional production-ready verdict.

## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline reflects primary-source information available on 5 August 2026. It is a starting point only. Re-check the current release, support policy, embedded runtimes, operating-system requirements, plugin compatibility, security advisories, and distribution rules before recommending or changing anything.

| Area | Baseline on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Electron stable | 43.3.0, released 4 August 2026; embeds Chromium 150.0.7871.212 and Node.js 24.18.1. | Application Electron version, embedded Chromium/Node, release channel, security status, and supported-major window. |
| Electron support | The project supports the latest three stable major lines; old major lines can lose security fixes quickly. | Current support table, breaking changes, native module ABI, and staged major-by-major upgrade path. |
| Electron security | Use the current official security checklist: secure content, no Node integration for remote content, context isolation, sandboxing, permission handlers, restrictive CSP, navigation/window controls, validated IPC sender, custom protocol, fuses, and minimal API exposure. | Effective `webPreferences`, every session and webContents, preload surface, IPC handlers, protocols, CSP, and packaged binary fuses. |
| Electron integrity and updates | ASAR alone is not a security boundary. Embedded ASAR integrity requires the relevant fuse and a package/signing sequence that preserves verification. Auto-update behavior is platform and packaging specific. | Actual package layout, fuse state, signature, feed, duplicate check behavior, downgrade rules, rollback, and revocation. |
| Tauri core | Tauri core 2.11.5 was released 1 July 2026. CLI, JS API, bundler, runtime, Wry, Tao, and plugins have independent versions. | Exact Cargo and frontend graph, CLI used in CI, generated schemas, plugin support table, Rust MSRV, system WebView, and platform targets. |
| Tauri authorization | Capabilities grant or deny permissions to named windows and webviews; overlapping capabilities merge. Runtime Authority checks origin, capability, permission, and scope, but custom command implementations must enforce their own scoped rules correctly. | All capability files, window labels, remote URL grants, permission composition, deny rules, custom scopes, command registration, and runtime checks. |
| Tauri updater | The updater verifies signed update metadata/artifacts and dangerous frontend updater commands are blocked until capabilities permit them. | Public key pinning, private-key custody, endpoint TLS, platform/architecture mapping, permissions, download/install behavior, rollback, and key rotation. |
| Distribution and signing | Code signing is a security and trust control; macOS direct distribution also requires notarization. Windows, macOS, and Linux package formats have different trust, installer, and update behavior. | Per-platform certificate/key, timestamping, entitlements, notarization ticket, package signature, store policy, installer behavior, and recovery from key loss. |

## 2. Role And Mission

### 2.1 Role

Act as a Principal Desktop Engineer, Electron and Tauri specialist, Chromium and WebView security engineer, Node.js and Rust reviewer, IPC and authorization architect, operating-system integration engineer, installer and auto-update engineer, code-signing and supply-chain auditor, application-security specialist, performance engineer, test architect, SRE, incident responder, and release/recovery owner.

### 2.2 Mission

1. Establish the application's real source, build, packaged, signed, installed, and runtime state.
2. Protect source code, user data, signing material, release channels, and uncommitted work.
3. Map every process, window, webview, origin, preload, command, IPC channel, capability, plugin, sidecar, local service, and operating-system integration.
4. Verify trust boundaries and least privilege instead of assuming framework defaults are sufficient.
5. Reproduce defects and security conditions with the least risky evidence method.
6. Find root causes rather than suppressing warnings or widening privileges.
7. Implement only authorized, minimal, reversible fixes tied to confirmed findings.
8. Add regression, negative, concurrency, upgrade, rollback, and recovery tests.
9. Build and inspect the actual release artifacts for every supported platform and architecture available.
10. Verify signing, notarization, installer behavior, update delivery, downgrade prevention, rollback, and key-recovery plans.
11. Measure startup, responsiveness, memory, CPU, disk, network, and background behavior under realistic workloads.
12. Produce an evidence-backed P0-P3 finding register, release decision, implementation roadmap, and Definition of Done.

## 3. Non-Negotiable Operating Contract

### 3.1 Truth, Evidence, And Status

1. Never invent files, code, command output, platform behavior, signatures, package metadata, CVEs, telemetry, test results, release state, or production access.
2. Use only these material claim states: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, and `REJECTED`.
3. A static pattern, linter warning, dependency advisory, or theoretical exploit is not a confirmed runtime defect without relevant source, build, package, or runtime evidence.
4. A green build proves only the executed build scope. A signed package proves identity and integrity at signing time, not application correctness. A successful update proves only the tested channel/platform/version path.
5. Record contradictions between documentation, configuration, generated output, installed state, and runtime behavior. Resolve them or leave them explicit.
6. Do not call the application secure, production-ready, fully tested, cross-platform, or rollback-safe unless the applicable evidence matrices and Definition of Done are satisfied.

### 3.2 Workspace, User Data, And Signing Safety

1. Inspect version-control status before modification. Do not reset, clean, stash, overwrite, mass-format, or delete another person's uncommitted work.
2. Back up or snapshot mutable local databases, application data, configuration, certificates, update metadata, and installer test state before risky operations.
3. Never execute destructive installer, migration, cleanup, revocation, certificate rotation, updater, or filesystem tests against real user data or production channels without explicit authorization and recovery evidence.
4. Never expose private signing keys, certificate passwords, API tokens, cookies, license secrets, device identifiers, user files, crash dumps, or decrypted credentials in output.
5. Use isolated test profiles, temporary directories, fake update feeds, disposable VMs, test certificates, and non-production tenants whenever possible.
6. Treat packaged applications and downloaded installers as potentially hostile until provenance, signature, and expected hash are verified.

### 3.3 Authorization And Change Boundary

1. `AUDIT_ONLY`: inspect and report; do not change repository, packages, signing systems, update feeds, stores, or production state.
2. `AUDIT_AND_SAFE_FIX`: implement narrow, reversible, low-risk fixes with regression tests; stop before irreversible or externally visible actions.
3. `FULL_IMPLEMENTATION`: implement confirmed remediation within the explicitly authorized scope, including migrations and release changes only when recovery is proven.
4. `FIX_CONFIRMED_ISSUES`: do not broaden the task into speculative modernization or framework migration.
5. `MIGRATION_AUDIT`: prioritize compatibility, behavior drift, data migration, installer continuity, identity continuity, and rollback.
6. `INCIDENT_MODE`: preserve evidence first, contain exposure, revoke or disable compromised channels, restore trust, and rebuild from verified sources.
7. Never publish, sign, notarize, upload to a store, rotate a production key, change a live update feed, release an installer, or delete user data without explicit authorization.

### 3.4 Research And Version Policy

1. Use primary sources first: Electron, Tauri, Node.js, Rust, Chromium/WebView platform documentation, Apple, Microsoft, Linux distribution/store documentation, and the exact packaging/updater project.
2. Record source title, URL, version or status, access date, and the decision informed.
3. Do not recommend `latest`, preview, nightly, alpha, beta, release candidate, unsupported Electron major, or an unreviewed Tauri plugin merely because it exists.
4. Verify the complete compatibility tuple: application framework, embedded/runtime engine, frontend toolchain, Node/Rust version, native modules/crates, plugins, packaging tool, operating system, architecture, signing identity, installer, and update channel.
5. Treat generated schemas and configuration documentation as version-specific. Use the documentation matching the resolved framework and plugin version.
6. Distinguish framework version from tool versions: Electron Forge/Builder/Packager and Tauri core/CLI/API/bundler/plugins can move independently.

## 4. Evidence Model And Finding Discipline

### 4.1 Evidence Levels

| Level | Meaning | Examples | Allowed conclusion |
| --- | --- | --- | --- |
| E0 | Claim or documentation only | README, issue, diagram, roadmap, user statement | Context only; never sufficient for a production verdict. |
| E1 | Static source evidence | Code, configuration, manifests, capability files, entitlements | Shows intent and potential behavior, not resolved or installed behavior. |
| E2 | Resolved build evidence | Lock files, dependency graph, compiler output, generated configuration | Shows what was resolved and built in a specific environment. |
| E3 | Packaged artifact evidence | Archive contents, binary metadata, fuses, permissions, signatures, SBOM | Shows the actual release candidate before installation. |
| E4 | Installed/runtime evidence | Installed files, process tree, runtime logs, IPC behavior, OS integration, performance | Shows behavior on a specific platform, architecture, profile, and version path. |
| E5 | Operational/recovery evidence | Real update rollout, rollback, restore, key rotation, telemetry, incident drill | Required for strong claims about operations, recovery, and production readiness. |

### 4.2 Mandatory Finding Register

```text
ID:
Title:
Severity: P0 / P1 / P2 / P3
Evidence status: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Framework: ELECTRON / TAURI / SHARED / OTHER
Area:
Affected platform and architecture:
Affected version and release channel:
Affected files and symbols:
Affected window, webview, process, command, IPC channel, capability, plugin, installer, or update path:
Environment:
Evidence level: E0 / E1 / E2 / E3 / E4 / E5
Evidence:
Command, test, package inspection, or runtime capture:
Reproduction:
Root cause:
Exploit or failure preconditions:
User and business impact:
Security, privacy, data, and operational impact:
Likelihood:
Proposed fix:
Implemented fix:
Regression test:
Release and migration impact:
Rollback or recovery:
Residual risk:
Owner:
Status:
```

### 4.3 Severity Guidance

1. `P0`: active compromise, arbitrary local code execution through untrusted content, compromised signing/update path, destructive cross-user data loss, credential exfiltration, or an unrecoverable production release condition.
2. `P1`: reachable privilege escalation, authorization bypass, unsafe updater or installer behavior, severe data corruption, widespread crash/startup failure, unsupported security-critical runtime, or no viable rollback for a critical release.
3. `P2`: meaningful reliability, privacy, performance, accessibility, maintainability, or defense-in-depth weakness with bounded impact or additional preconditions.
4. `P3`: low-risk hardening, developer-experience improvement, documentation gap, cleanup, or optional modernization.
5. Severity is based on demonstrated impact, reachability, likelihood, blast radius, detectability, and recovery difficulty. Do not inflate severity from keywords alone.

## 5. Phase 0 - Protect The Workspace And Establish Scope

### 5.1 Pre-Change Snapshot

1. Record repository root, current branch, commit, remotes, submodules, worktrees, ignored/generated directories, package-manager state, Rust toolchain state, and uncommitted changes.
2. Record host operating system, architecture, shell, locale, time zone, file-system type, security software, and whether the environment is local, VM, CI, container, or remote builder.
3. Inventory existing installers, release artifacts, signing outputs, notarization logs, update manifests, store packages, and crash symbols before generating replacements.
4. Hash or otherwise identify every artifact used as audit evidence. Preserve timestamps and original filenames.
5. Identify directories that contain real user data, production secrets, signing keys, certificates, hardware credentials, browser profiles, or release-channel state; exclude them from destructive tests.
6. Create a narrow change plan and explicit stop conditions before editing.

### 5.2 Initial Command Log

```text
For every command record:
- exact command and arguments;
- working directory;
- environment variables that affect behavior, with secret values redacted;
- framework, Node, package-manager, Rust, Cargo, linker, compiler, packaging, and signing tool versions;
- platform and architecture;
- exit code;
- concise stdout/stderr summary;
- generated or modified files;
- evidence level and conclusion;
- reason if the command was not run.
```

## 6. Source-To-Installed-Runtime Identity Chain

Do not assume that the repository, CI artifact, uploaded package, downloaded installer, installed application, running process, and update payload are the same thing. Prove the chain or explicitly identify the break.

| Stage | Required evidence | Question |
| --- | --- | --- |
| Source identity | Commit, tag, dirty state, submodules, generated source, lock files, build inputs | Can another engineer reproduce exactly which source was used? |
| Resolved graph | npm/pnpm/yarn/Bun lock, Cargo.lock, native dependencies, plugins, tool versions | Does the resolved graph match policy and the claimed release? |
| Build identity | Builder image/host, environment, flags, feature sets, target triple, generated files | Is the build deterministic enough to explain artifact differences? |
| Package identity | App ID/bundle ID, product name, version, build number, channel, package type, architecture | Can the package be tied to the source and intended channel? |
| Integrity identity | Hashes, ASAR integrity, embedded resources, SBOM, provenance, signature, timestamp, notarization | Can modification or substitution be detected? |
| Distribution identity | Release record, store listing, CDN object, update manifest, feed response | Is the user receiving the reviewed artifact? |
| Installed identity | Install path, package manager/store registration, binary signature, resources, permissions | Does installed state match the reviewed artifact? |
| Runtime identity | Executable path, process tree, loaded modules/libraries, WebView/runtime versions, channel, profile | Is the running process the expected installed release? |

### 6.1 Required Identity Checks

1. Compare source version declarations with generated package metadata, executable metadata, installer metadata, store metadata, and update feed metadata.
2. Verify application ID, bundle identifier, executable name, publisher identity, protocol scheme, file associations, data directory, keychain/credential namespace, and update channel continuity.
3. Verify that CI promotes an immutable artifact instead of rebuilding independently for test, signing, staging, and release.
4. Verify that symbols, source maps, dSYM/PDB/debug files, SBOM, provenance, and release notes correspond to the exact shipped artifact.
5. Inspect the installed application, not only the unpacked staging directory.
6. Verify runtime-loaded native libraries, sidecars, and system WebView/runtime components where they affect behavior.
7. Document every unsupported identity link as a release blocker or explicit residual risk.

## 7. Repository, Toolchain, And Dependency Audit

### 7.1 Repository Inventory

1. Map workspaces, packages, applications, shared libraries, frontend bundles, main/Rust processes, preload or bridge code, plugins, native modules, sidecars, installers, updater services, release tooling, and infrastructure.
2. Identify generated files and their source schemas. Verify whether generated capability, entitlement, manifest, protocol, and installer files are reviewed or silently regenerated.
3. Map scripts with filesystem, shell, network, signing, publishing, or credential access. Inspect lifecycle hooks such as `preinstall`, `postinstall`, build hooks, Cargo build scripts, and release hooks.
4. Find duplicated configuration across package manifests, Electron Forge/Builder config, Tauri config, platform manifests, CI, installer definitions, and update service.
5. Identify dead packages, abandoned forks, vendored binaries, binary downloads, Git dependencies, path dependencies, patches, overrides, and unpublished registries.
6. Map ownership and required reviewers for privileged bridge code, capabilities, signing, updater, installer, release automation, and incident controls.

### 7.2 JavaScript, TypeScript, And Frontend Dependency Graph

1. Determine the actual package manager and enforce one lockfile policy. Detect mixed npm, Yarn, pnpm, Bun, vendored `node_modules`, or lockfile drift.
2. Run a reproducible frozen/locked install in an isolated environment. Record registry, proxy, CA, authentication, package-manager version, and script policy.
3. Audit direct and transitive dependencies, development tools that execute during build, browser bundles, preload/main dependencies, and packages copied into the final artifact.
4. Inspect package scripts and install hooks for arbitrary downloads, native compilation, credential access, or environment-dependent output.
5. Verify package-source trust, namespace ownership, dependency-confusion resistance, integrity metadata, mirrors, allowlists, and emergency package revocation.
6. Do not assume a dependency advisory is exploitable. Determine whether the vulnerable code is shipped, reachable, privileged, and invoked under the affected conditions.
7. Detect multiple copies of security-critical libraries, incompatible frontend runtime versions, and bundled development-only modules.
8. Verify source-map policy and ensure production source maps are protected, intentionally public, or uploaded only to the authorized crash service.

### 7.3 Rust, Cargo, And Native Dependency Graph

1. Record `rust-toolchain` or toolchain resolution, Cargo version, target triples, linker, C/C++ toolchain, system libraries, features, profiles, and MSRV constraints.
2. Use `Cargo.lock` for applications and verify locked builds. Inspect workspace dependencies, feature unification, default features, target-specific dependencies, build dependencies, procedural macros, and Git/path dependencies.
3. Audit `build.rs`, procedural macros, code generation, bindgen, downloaded SDKs, and environment variables because they execute during build with builder privileges.
4. Inspect `unsafe`, FFI, raw pointers, transmute, manual memory management, signal handlers, callback lifetimes, thread boundaries, and panic behavior.
5. Verify crate advisories and maintenance status, but confirm shipment and reachability before assigning runtime severity.
6. Inspect Cargo profiles for overflow checks, panic strategy, LTO, debug symbols, stripping, incremental behavior, and reproducibility tradeoffs.
7. Verify native system dependencies and minimum supported OS versions on every target; a successful build on one runner is not cross-platform proof.
8. Document binary blobs, sidecars, codecs, drivers, and SDK licenses and update ownership.

### 7.4 Supply-Chain And Build Trust

1. Pin CI actions, builder images, tool downloads, packaging tools, and release dependencies to reviewed immutable versions or digests.
2. Separate untrusted pull-request builds from signing, publishing, store, update-feed, and production credentials.
3. Use short-lived identity federation where supported; restrict secrets by environment, branch, repository, workflow, actor, platform, and approval.
4. Generate SBOM and provenance for the exact release artifact. Verify them during promotion and incident response.
5. Protect build caches from cross-trust contamination. Never restore privileged release caches into untrusted jobs without validation.
6. Verify artifact retention, checksum storage, signature verification, tamper-evident release records, and reproducible or explainable rebuilds.
7. Define a dependency and certificate revocation path that can remove, block, or replace compromised components without waiting for routine releases.
8. Test a clean-room rebuild from a verified commit using documented bootstrap dependencies.

## 8. Build, Packaging, And Reproducibility Audit

### 8.1 Build Graph And Configuration

1. Map every build entry point, workspace filter, environment, feature flag, target, architecture, bundle variant, and platform-specific override.
2. Resolve the effective configuration after environment variables, CLI flags, generated files, merge rules, defaults, and conditional code are applied.
3. Compare development, test, staging, production, store, enterprise, portable, and update builds. Treat unexplained differences as risk.
4. Verify that development servers, debug menus, devtools, source-map servers, hot reload, test endpoints, mock data, verbose logging, and bypass flags cannot enter production artifacts unintentionally.
5. Verify deterministic versioning and build numbering across package manifests, Rust crates, executables, installers, stores, and update feeds.
6. Check locale, path, case sensitivity, time, network, CPU count, signing availability, and host-specific behavior that can make builds non-reproducible.
7. Record all generated configuration and compare it to the source template. Review generated diffs before release.
8. Build from a clean clone with network and credential access minimized. Explain every difference from the existing release artifact.

### 8.2 Package Content Inspection

1. List every file in the packaged application and installer. Classify executable code, resources, configuration, licenses, symbols, source maps, user templates, native libraries, sidecars, and unused files.
2. Search the final artifact for secrets, tokens, private URLs, test credentials, signing material, internal certificates, source repositories, absolute paths, usernames, and sensitive fixtures.
3. Verify that only intended native modules, crates, plugins, codecs, locales, and architectures are shipped.
4. Check file permissions, ownership, ACLs, executable bits, quarantine attributes, entitlements, capabilities, and installer-created directories.
5. Verify compression, archive extraction paths, symlink behavior, and unpacked files. Do not assume archive packaging prevents reading or modification.
6. Verify that runtime-writable content is outside signed/read-only application resources and cannot replace executable code on restart.
7. Compare package size and content against a known-good release. Explain significant additions, removals, or duplicate runtimes.
8. Scan the actual artifact with appropriate malware, reputation, package, and signature tools, recording false-positive handling without disabling controls globally.

## 9. Architecture, Process, Window, And Privilege Map

### 9.1 Mandatory Architecture Map

1. Draw the process tree: bootstrap, Electron main or Tauri Rust core, renderer/webview processes, GPU, utility/worker processes, sidecars, local daemons, helpers, crash reporter, updater, installer, and spawned children.
2. Map every window and webview by stable label or identifier, content origin, lifecycle, owner, user role, data sensitivity, navigation policy, permission set, and exposed bridge.
3. Map every trust boundary between untrusted remote content, local packaged UI, privileged bridge, native core, local files, operating-system APIs, devices, and remote services.
4. Map all IPC mechanisms: Electron IPC, MessagePort, postMessage, webview messaging, Tauri invoke/events/channels, local sockets, named pipes, HTTP, WebSocket, stdin/stdout, files, and custom protocols.
5. Map authentication and authorization decisions at the layer that performs privileged work. UI hiding is not authorization.
6. Map state ownership: renderer memory, main/Rust state, local database, files, secure storage, cloud service, updater, and installer.
7. Map startup, shutdown, crash restart, sleep/wake, session lock/unlock, network transition, update restart, and OS sign-out/shutdown paths.
8. Mark every path that can execute code, launch a process, open an external URL, write a file, access credentials, use a device, change settings, install an update, or delete data.

### 9.2 Privilege-Minimization Questions

1. Can a renderer or webview do less? Remove broad bridges and expose narrow operations with explicit schemas.
2. Can a privileged operation move to a dedicated process, scoped command, OS service, or broker with a smaller attack surface?
3. Can a window receive a unique capability or session instead of inheriting a global permission set?
4. Can a file, URL, executable, device, or credential scope be restricted to an allowlisted subset?
5. Can network content be rendered without local privileges and without sharing cookies, storage, permissions, or service workers with trusted content?
6. Can the updater, installer, or release job run with temporary credentials and separate approval?
7. Can administrative behavior be separated from the normal user process and made auditable?
8. Can a compromised renderer be contained without reaching code execution, secrets, user files, update controls, or another tenant/account?

## 10. Shared Web, Content, And Origin Security

### 10.1 Content Origins And Navigation

1. Inventory every local, custom-protocol, file, data, blob, extension, development-server, remote HTTPS, WebSocket, and user-provided origin.
2. Classify each origin as trusted local application content, trusted remote application content, third-party content, user-generated content, authentication content, update content, or untrusted arbitrary content.
3. Define an allowlist for top-level navigation, redirects, new windows, downloads, external protocol handling, OAuth callbacks, and embedded frames.
4. Canonicalize and validate URLs with a real parser. Reject username confusion, encoded separators, mixed case, punycode/homograph traps, alternate schemes, local addresses, and redirect chains where relevant.
5. Do not grant local privileges to remote content merely because it is served by the application's domain. Account takeover, DNS/CDN compromise, XSS, or supply-chain compromise can make that content hostile.
6. Separate trusted and untrusted content into distinct webviews/windows, sessions, storage partitions, permissions, and bridge surfaces.
7. Block unexpected navigation and window creation at the privileged layer, not only in frontend click handlers.
8. Test redirects, target blank, window.open, iframe, drag-and-drop, pasted HTML, markdown, SVG, PDF, media, and downloaded content.

### 10.2 CSP, Injection, And Browser Surface

1. Define a restrictive Content Security Policy for each content class. Avoid broad `unsafe-eval`, `unsafe-inline`, wildcard origins, unrestricted `connect-src`, and permissive frame/object rules.
2. Trace all HTML, markdown, template, SVG, CSS, URL, script, and command construction from source to sink. Validate sanitization configuration and bypasses.
3. Audit DOM XSS, prototype pollution, unsafe deserialization, dynamic import, eval-like behavior, worker creation, WebAssembly loading, and plugin-defined script execution.
4. Verify Trusted Types or equivalent controls where practical, but do not treat policy presence as proof that unsafe sinks are unreachable.
5. Audit browser storage, IndexedDB, Cache Storage, service workers, cookies, localStorage, sessionStorage, and shared partitions for sensitive data and cross-account leakage.
6. Disable or justify experimental browser features, insecure content, certificate bypasses, disabled web security, permissive CORS workarounds, and debugging ports.
7. Verify clipboard, drag/drop, paste, print, screen capture, notifications, media capture, geolocation, USB, serial, HID, Bluetooth, and filesystem permissions.
8. Test with malicious content that attempts to reach every exposed bridge, navigate, open external applications, exfiltrate data, persist state, and trigger expensive work.

### 10.3 Authentication Content And Session Boundaries

1. Prefer system-browser authorization with PKCE when appropriate. If embedded authentication is required, document provider support, cookie/storage isolation, phishing risk, and bridge restrictions.
2. Validate custom protocol or app-link callbacks against state, nonce, PKCE verifier, expected issuer, redirect URI, account, and one-time use.
3. Prevent one account's cookies, cache, local storage, database rows, files, tokens, pending operations, or window state from leaking after logout or account switch.
4. Store refresh tokens and long-lived credentials in operating-system protected storage or a clearly justified alternative; do not expose them to the renderer.
5. Define token refresh single-flight, expiry, clock-skew, offline, revocation, password change, device removal, and server-side session invalidation behavior.
6. Verify local authorization for privileged offline operations; an old cached UI state is not authorization.
7. Protect login, license, payment, and account-recovery windows from navigation, arbitrary preload/command access, screenshots where required, and external content injection.
8. Test multiple windows, multiple profiles, fast account switching, concurrent refresh, expired sessions, revoked accounts, and sleep/wake transitions.

## 11. Electron-Specific Audit

### 11.1 Framework, Embedded Runtimes, And Upgrade State

1. Resolve the exact Electron version from the lockfile and packaged binary, not only `package.json`. Record embedded Chromium, Node.js, V8, and relevant ABI.
2. Determine whether the major is within the current supported-major window and whether a newer stable patch fixes security or correctness issues.
3. Review Electron breaking changes major by major. Do not jump multiple majors without intermediate compatibility evidence and native-module verification.
4. Inventory Electron Forge, Electron Builder, Packager, Rebuild, Fuses, notarization, signing, and updater package versions independently.
5. Verify native modules against the actual Electron ABI and every supported OS/architecture. Rebuild, prebuild, fallback compilation, and runtime loading must be tested.
6. Detect unsupported or private Electron APIs, command-line switches, Chromium flags, monkey patches, remote module replacements, and assumptions about process internals.
7. Verify minimum OS support and embedded runtime behavior against the product's declared support matrix.
8. Document the patch and major upgrade cadence, security response owner, testing window, and emergency release path.

### 11.2 Application Lifecycle And Single-Instance Behavior

1. Map execution before and after `app.whenReady()`, single-instance lock acquisition, second-instance arguments, open-file/open-url events, activate, window-all-closed, before-quit, will-quit, quit, and crash/relaunch paths.
2. Validate command-line arguments and deep-link payloads received by the first instance. Do not trust the second process merely because it is the same application.
3. Test startup with corrupted preferences, locked profile, read-only data directory, missing resources, unavailable network, slow keychain, failed migrations, and incomplete update.
4. Define behavior when all windows close on each platform, when the tray remains active, and when the OS requests logout or shutdown.
5. Prevent duplicate background jobs, updater checks, local servers, migrations, device sessions, or file processing across multiple instances.
6. Verify orderly teardown of sessions, sockets, file handles, workers, utility processes, child processes, crash reporters, and telemetry.
7. Test app relaunch, update restart, crash restart, safe mode, recovery mode, and no-window background mode.
8. Ensure fatal startup failures produce actionable diagnostics without leaking secrets and without entering an infinite restart loop.

### 11.3 BrowserWindow, WebContentsView, And WebPreferences

1. Inventory every `BrowserWindow`, `BaseWindow`, `WebContentsView`, offscreen renderer, hidden window, print window, auth window, splash screen, and temporary webContents.
2. Record effective `webPreferences` for each: `nodeIntegration`, `nodeIntegrationInWorker`, `nodeIntegrationInSubFrames`, `contextIsolation`, `sandbox`, `preload`, `webSecurity`, `allowRunningInsecureContent`, `experimentalFeatures`, `enableBlinkFeatures`, `webviewTag`, `partition`, `spellcheck`, and devtools policy.
3. Require `nodeIntegration: false`, `contextIsolation: true`, and sandboxing for untrusted or remote content unless a narrowly proven exception exists.
4. Treat any `sandbox: false`, `contextIsolation: false`, `webSecurity: false`, insecure content, unrestricted webview, or remote Node integration as high-priority evidence requiring reachability analysis.
5. Verify the preload path resolves to the intended packaged file and cannot be replaced through writable directories, environment manipulation, or untrusted navigation.
6. Separate sessions and storage partitions for content with different trust, account, privacy, or lifecycle requirements. Determine whether partitions are persistent.
7. Audit hidden windows and background webContents because they can retain privileges, cookies, microphones, cameras, timers, or IPC listeners after visible UI closes.
8. Ensure window options, content origin, preload, and privilege are bound together in one reviewed creation path rather than mutable across scattered code.

### 11.4 Preload And ContextBridge Surface

1. Inventory every preload file and every property exposed through `contextBridge`. Produce a typed bridge contract.
2. Expose narrow functions and immutable values, not raw `ipcRenderer`, EventEmitter, Electron modules, Node primitives, filesystem handles, shell execution, unrestricted URLs, callbacks with hidden authority, or generic `invoke(channel, payload)`.
3. Validate arguments on both renderer and privileged sides. Renderer validation improves UX but is not a security boundary.
4. Freeze or safely wrap exposed objects. Avoid leaking mutable privileged references, prototypes, Buffer instances, native handles, or objects with unexpected methods.
5. Define error contracts that do not expose stack traces, file paths, tokens, SQL, environment variables, or implementation details to untrusted content.
6. Remove stale listeners and subscriptions on navigation, reload, account switch, window close, and hot update. Bound listener count and message rate.
7. Verify preload behavior in sandboxed contexts and across subframes. Do not assume the main frame is the only caller.
8. Add contract tests that run malicious renderer code against every exposed method and verify denial, validation, authorization, and bounded failure.

### 11.5 IPC Authentication, Authorization, Validation, And Backpressure

1. Inventory every `ipcMain.handle`, `ipcMain.on`, `webContents.send`, MessagePort, postMessage, webview message, and reply path. Remove or reject unknown channels.
2. Validate the sender using the actual `webContents`, frame, origin, URL, session/partition, window ownership, lifecycle generation, and account context. A channel name is not authentication.
3. Perform resource-level authorization for every file, account, tenant, device, job, update, setting, and privileged action.
4. Use strict schemas with size, depth, count, string, path, enum, and binary limits. Reject extra fields where they create ambiguity.
5. Canonicalize paths and URLs before policy checks. Defend against traversal, symlink/junction escape, alternate data streams, UNC paths, device paths, case tricks, and encoded separators.
6. Make side effects idempotent where retries, duplicate clicks, renderer reload, duplicate messages, or process restart can repeat them.
7. Bound concurrent requests, queues, stream rates, payload sizes, response sizes, and execution time. Cancel work when the caller disappears where safe.
8. Do not send privileged results to a stale, navigated, destroyed, or reused webContents without revalidating its identity and account context.
9. Separate read, write, destructive, administrative, and update channels. Require additional confirmation or authorization for irreversible operations.
10. Log security-relevant decisions with correlation IDs and redaction, including denied sender, invalid schema, scope failure, duplicate request, and rate-limit events.
11. Test cross-window, subframe, navigated-frame, remote-origin, stale-renderer, destroyed-renderer, duplicate, replay, oversized, slow, and concurrent IPC scenarios.
12. Treat IPC as a local network API with an untrusted client whenever renderer compromise is in scope.

### 11.6 Sessions, Permissions, Downloads, And Protocols

1. Inventory all sessions and partitions. Configure permission request/check handlers for every session that can load remote or user-controlled content.
2. Default-deny camera, microphone, display capture, notifications, geolocation, MIDI, USB, serial, HID, Bluetooth, clipboard, and fullscreen permissions unless explicitly required.
3. Bind permission decisions to exact origin, frame, user action, account, device, and duration. Persist only where justified and revocable.
4. Audit cookies, proxy, cache, certificate verification, auth challenges, client certificates, service workers, extensions, and storage clearing per session.
5. Define download policy: allowed origins, MIME and extension checks, destination selection, overwrite behavior, quarantine/Mark-of-the-Web, malware scanning, partial files, cancellation, and opening behavior.
6. Implement custom protocols as privileged parsers: normalize paths, define standard/secure/cors/fetch/stream privileges deliberately, constrain methods and origins, and prevent traversal.
7. Avoid `file://` for privileged app content where a secure custom protocol provides a clearer origin and policy model.
8. Test certificate errors, captive portals, proxy auth, offline mode, redirects, malicious filenames, archive bombs, partial downloads, and download-to-execute chains.

### 11.7 Navigation, New Windows, External Open, And Webviews

1. Use `will-navigate`, redirect handling, and window-open handlers to enforce exact navigation and popup policy.
2. Validate every URL passed to `shell.openExternal` or OS launch APIs. Allow only required schemes and hosts; reject local files, executable protocols, script schemes, malformed URLs, and arbitrary custom protocols.
3. Do not use `<webview>` unless its isolation and lifecycle benefits outweigh its attack surface. Prefer `WebContentsView` or system browser where appropriate.
4. If `<webview>` exists, validate `will-attach-webview` options and source, remove dangerous preload and permissions, reject `allowpopups`, and isolate partitions.
5. Verify OAuth, payment, help, documentation, support, and third-party content flows under redirects and compromised content conditions.
6. Prevent untrusted content from controlling window features, preload selection, partition, sandbox, devtools, download location, or external applications.
7. Audit drag-and-drop and link handling for local-file disclosure and command/protocol execution.
8. Test nested frames, dynamically created webviews, same-origin changes, history navigation, server redirects, and post-authentication navigation.

### 11.8 Fuses, ASAR Integrity, And Executable Hardening

1. Inspect fuses in the actual packaged executable. Do not rely only on Forge or build configuration.
2. Evaluate fuses such as disabling `RunAsNode`, disabling `NODE_OPTIONS` and `NODE_EXTRA_CA_CERTS` influence where appropriate, disabling inspection arguments, enforcing ASAR app loading, and enabling embedded ASAR integrity validation.
3. Flip fuses after packaging and before code signing, then verify the final signed binary. Record the exact fuse tool version and options.
4. Understand the compatibility impact before disabling behavior; test CLI integrations, child processes, debugging, enterprise certificates, and native modules.
5. Enable ASAR integrity only with the complete required fuse combination and packaging flow. Verify that modified archives fail as expected.
6. Keep executable code out of writable unpacked resources. Justify every `asarUnpack` path and protect its load path.
7. Verify signature and ASAR integrity behavior after installer installation, delta update, full update, repair, and rollback.
8. Treat fuses and ASAR as defense in depth, not a replacement for secure renderer isolation, IPC authorization, signing, and update trust.

### 11.9 Utility Processes, Workers, Extensions, And Native Modules

1. Prefer utility processes over ad hoc Node child processes when Electron lifecycle, sandboxing, and MessagePort integration provide a safer fit; justify exceptions.
2. Inventory Node child processes, forked workers, worker threads, renderer workers, service workers, GPU tasks, extension processes, and native helper processes.
3. Validate child executable and argument construction; avoid shell interpretation; use explicit environment allowlists and working directories.
4. Bound process count, CPU, memory, file descriptors, output buffers, restart frequency, and queue depth. Prevent crash loops and fork bombs.
5. Authenticate local IPC to helpers and prevent another local process from impersonating the app or connecting to privileged sockets/pipes.
6. Verify native module loading paths, signatures where available, ABI compatibility, DLL search order, rpath, library search paths, and writable-directory hijacking.
7. Disable or strictly control Chrome extensions, devtools extensions, remote debugging, inspect ports, and automation interfaces in production.
8. Test helper crash, hang, malformed output, oversized output, partial protocol messages, version mismatch, update overlap, and application shutdown.

## 12. Tauri-Specific Audit

### 12.1 Core, CLI, API, Runtime, WebView, And Plugin Matrix

1. Resolve the exact versions of `tauri`, `tauri-build`, `tauri-cli`, `@tauri-apps/cli`, `@tauri-apps/api`, runtime, Wry, Tao, bundler, macros, and every official or third-party plugin.
2. Do not force artificial version equality across independently released components. Instead verify their documented compatibility and the actual generated/runtime behavior.
3. Record Rust toolchain and MSRV, Cargo features, frontend package manager, generated schemas, target triples, mobile overlays if present, and platform-specific plugin support.
4. Identify the system WebView implementation and minimum supported version on each target: WebView2, WKWebView/WebKit, WebKitGTK, or mobile WebView. Test behavior on the oldest supported environment.
5. Verify whether WebView2 is evergreen, fixed, embedded, offline-installed, store-provided, or assumed present. Include installer and enterprise-offline behavior.
6. Review Tauri release notes, breaking changes, plugin changelogs, generated ACL schemas, and platform limitations for the resolved versions.
7. Inventory third-party plugins and forks. Review their Rust core, guest JavaScript, permissions, scopes, build scripts, native code, release process, and maintenance state.
8. Define an upgrade cadence that covers core, CLI, JS API, plugins, Rust, system WebView requirements, installer tooling, and OS support.

### 12.2 Capabilities, Permissions, Scopes, And Runtime Authority

1. Inventory every capability file, inline capability, permission definition, scope, deny rule, target platform, remote URL pattern, window label, and webview label.
2. Build an effective permission matrix after all capabilities are merged. Windows or webviews referenced by multiple capabilities receive the union of their permissions.
3. Use stable, unique window/webview labels and verify that dynamic creation cannot accidentally match or inherit a broader capability.
4. Default-deny privileged commands. Grant only the exact commands and scopes required for a specific window, webview, origin, role, and platform.
5. Review `remote` capability grants with extreme caution. A remote origin receiving local-system access must be justified against XSS, account compromise, DNS/CDN compromise, and content takeover.
6. Use deny permissions where they provide defense in depth, but understand the final merge and precedence behavior for the resolved version.
7. Verify custom scopes are actually enforced by the command or plugin implementation. Configuration alone does not enforce an application-defined scope.
8. Review generated permission schemas and plugin permission files for the exact dependency version. Do not copy identifiers from unrelated versions.
9. Verify command registration and generated app manifests. Commands registered through broad invoke handlers must still be constrained by capabilities and in-command authorization.
10. Test each privileged command from allowed and denied windows, allowed and denied origins, subframes, dynamically created webviews, stale windows, and renamed labels.
11. Document every capability without a clear owner, purpose, test, and removal condition.
12. Treat Runtime Authority as one layer in the authorization chain, not a substitute for business authorization, path validation, account ownership, or destructive-action confirmation.

### 12.3 Commands, Invoke, Events, Channels, And Managed State

1. Inventory every Tauri command, invoke handler, plugin command, event, channel, global listener, window listener, menu/tray action, and Rust-to-frontend message.
2. Define strict request and response types. Reject ambiguous untagged enums, unbounded collections, deeply nested data, oversized strings/binaries, unknown fields where dangerous, and lossy numeric conversions.
3. Authorize inside the command using caller window/webview/origin, account, role, resource ownership, current application state, and operation intent.
4. Validate and canonicalize all paths, URLs, command names, device identifiers, database keys, and external-service identifiers before use.
5. Do not expose generic filesystem, shell, process, SQL, HTTP, plugin, or command dispatchers to the frontend unless they have a narrowly scoped, formally reviewed policy.
6. Bound command concurrency, duration, memory, output, channel rate, event fan-out, listener count, and queue depth. Support cancellation where safe.
7. Use managed state with explicit synchronization and ownership. Audit mutex/RwLock selection, lock ordering, blocking in async contexts, poisoning, reentrancy, and shutdown behavior.
8. Do not hold locks across await, IPC callbacks, filesystem/network operations, or frontend events without a proven design.
9. Make destructive and externally visible commands idempotent or protected against duplicate invoke, double click, event replay, renderer reload, and process restart.
10. Define stable error codes and redacted messages. Convert panics and library errors into controlled failures at the boundary.
11. Remove listeners and close channels when windows are destroyed, navigated, logged out, or replaced. Prevent stale messages from reaching a new account context.
12. Test malformed serialization, unknown commands, denied capability, invalid scope, stale caller, duplicate call, concurrent call, cancellation, panic, and shutdown.

### 12.4 Official And Third-Party Plugins

1. Create a plugin matrix: purpose, version, frontend API, Rust crate, supported platforms, permissions, scopes, native dependencies, storage, network access, update owner, and tests.
2. Review default permission sets before using them. A convenient `plugin:default` grant may include more commands than the window requires.
3. Prefer individual allow permissions and narrow scopes for filesystem, shell, process, opener, HTTP, SQL, store, clipboard, notification, dialog, deep link, single instance, global shortcut, autostart, and updater functionality.
4. Review plugin-generated permissions and application-added extensions. Ensure custom scope types are parsed and enforced consistently.
5. Audit plugin initialization order, managed state, background threads, event listeners, migration behavior, cleanup, and error handling.
6. Verify path variables and scope expansion against platform-specific directories, symlinks, junctions, Unicode, case sensitivity, removable media, and network shares.
7. Check whether a plugin exposes dangerous frontend commands by default or only after capability grants. Test the actual resolved version.
8. Treat unofficial plugins and forks as application code: inspect source, release provenance, maintainers, advisories, build scripts, native code, and incident response.
9. Remove unused plugins and Cargo features from the final binary and capabilities.
10. Test plugin behavior on unsupported or partially supported platforms and ensure the UI does not offer nonfunctional or unsafe operations.

### 12.5 Filesystem, Shell, Opener, Process, And Sidecars

1. Restrict filesystem access by command and canonical scope. Distinguish user-selected files from application-controlled paths and broad directory grants.
2. Prevent traversal and escape through symlinks, junctions, aliases, hard links, UNC/device paths, case changes, Unicode normalization, alternate data streams, and race conditions between check and use.
3. Use secure create/write/replace patterns, temporary-file permissions, atomic rename where supported, fsync requirements, conflict handling, and recovery from partial writes.
4. Never expose arbitrary shell strings. Use allowlisted programs or bundled sidecars, structured arguments, no shell interpretation, explicit environment, explicit working directory, and bounded output.
5. Verify sidecar path resolution, bundled target-triple naming, executable permissions, signature/hash, version handshake, update coupling, and writable-path hijacking.
6. Authenticate local communication with sidecars or services. Use protected sockets/pipes, random secrets or OS credentials, peer verification, and narrow access control.
7. Validate URLs and schemes passed to opener APIs. Separate opening HTTPS documentation from invoking arbitrary application protocols.
8. Define child-process timeout, cancellation, graceful stop, forced termination, descendant cleanup, output backpressure, crash retry, and quarantine behavior.
9. Audit elevation and administrator/root helpers. Use platform-approved privilege separation and authenticate requests; never run the entire UI privileged for convenience.
10. Test malicious filenames, executable substitution, argument injection, environment injection, local impersonation, sidecar version mismatch, partial output, hang, crash, and application shutdown.

### 12.6 Asset Protocol, CSP, Isolation, And Remote Content

1. Inventory asset/custom protocol configuration, allowed paths, scope, CSP, dev URL, frontend distribution directory, remote URLs, and any asset conversion helpers.
2. Verify the production build cannot load a development server or untrusted URL because of environment drift or fallback behavior.
3. Use restrictive CSP and isolation settings supported by the resolved Tauri/WebView version. Test on each system WebView because enforcement and feature support can differ.
4. Treat `convertFileSrc` and asset protocol access as privileged file disclosure. Restrict which files and directories can be converted and rendered.
5. Do not grant remote URLs capabilities unless the complete compromise scenario is accepted and mitigated. Prefer a privilege-free remote webview or system browser.
6. Verify navigation, popup, download, external-open, clipboard, media, permission, and devtools behavior in every webview.
7. Audit frontend dependencies and XSS sinks with the same rigor as Electron; a smaller native core does not make compromised web content harmless when commands are exposed.
8. Test malformed asset URLs, encoded traversal, local-file probing, remote redirects, compromised frontend bundle, CSP bypass attempts, and stale capability assignment.

### 12.7 Unsafe Rust, FFI, Mobile Overlay, And Platform Code

1. Review every `unsafe` block with documented invariants, ownership, lifetime, thread, alignment, aliasing, initialization, and error assumptions.
2. Audit FFI boundaries for ABI, struct layout, string encoding, buffer length, callback lifetime, exception/panic crossing, cancellation, and library version mismatch.
3. Verify platform modules and conditional compilation produce equivalent security decisions; absent code on one target must not silently broaden behavior.
4. Inspect Objective-C/Swift, C/C++, Java/Kotlin, PowerShell, shell, and installer custom actions with the same finding discipline as Rust and TypeScript.
5. If mobile targets exist, audit generated Android/iOS projects, permissions, intents/URL schemes, WebView settings, signing, stores, background behavior, and plugin hooks separately.
6. Test native-library absence, wrong architecture, signature failure, denied permission, OS API deprecation, callback after shutdown, and malformed native data.
7. Use sanitizers, Miri, fuzzing, clippy, compiler warnings, and platform diagnostics where applicable, but correlate findings with shipped code and runtime reachability.
8. Do not rewrite safe working code into `unsafe` or custom FFI merely for performance without measurement and a maintained test strategy.

## 13. Local Data, Databases, Files, And Recovery

### 13.1 Data Inventory And Classification

1. Inventory every persistent location: app data, user data, config, cache, logs, crash dumps, temp, downloads, databases, browser profiles, cookies, secure storage, OS credentials, keychain, registry/plist, shared containers, and removable/network storage.
2. Classify data by owner, account/tenant, sensitivity, retention, backup, synchronization, portability, deletion, and legal requirements.
3. Separate secrets from preferences, cache from durable state, derived data from source-of-truth data, and account-specific data from device-wide data.
4. Document paths per platform, package type, portable mode, store sandbox, enterprise redirection, roaming profile, and multiple installed channels.
5. Verify directory and file permissions after fresh install, upgrade, repair, downgrade, account switch, and migration.
6. Prevent one local OS user, app channel, account, tenant, or previous installation from reading another's data unless explicitly designed.
7. Define what survives uninstall, what is removed, what requires user confirmation, and how enterprise-managed data is handled.
8. Test low disk, read-only media, quota, path length, Unicode, case differences, antivirus lock, concurrent access, and abrupt power loss.

### 13.2 Databases, Migrations, Concurrency, And Integrity

1. Identify every embedded or local database engine, exact version, extensions, encryption layer, journal mode, locking model, busy timeout, schema version, and backup method.
2. Review schema constraints, foreign keys, uniqueness, checks, indexes, transaction boundaries, isolation, conflict handling, and recovery.
3. Never rely only on application validation for durable invariants. Add database constraints where supported and compatible.
4. Design migrations for crash safety, idempotency, forward compatibility, rollback or forward repair, disk-space requirements, and old/new application overlap.
5. Back up or snapshot before destructive migrations. Verify backup readability and restore into an isolated environment.
6. Test two windows/processes, background jobs, sidecars, sync engines, and old/new versions accessing the same data where that can occur.
7. Prevent duplicate external side effects around local transactions with idempotency keys, outbox/inbox patterns, durable state machines, or compensating actions.
8. Handle corruption explicitly: detection, read-only safe mode, export, repair limits, restore, telemetry, user communication, and no silent reset.
9. Verify encrypted database key storage, rotation, recovery, account switch, device migration, and behavior when secure storage is unavailable.
10. Test migration interruption at each durable step, downgrade after migration, concurrent startup, lock contention, full disk, and corrupted journal/WAL.

### 13.3 Files, Imports, Exports, Archives, And User Content

1. Treat every imported, opened, dragged, pasted, synchronized, or downloaded file as untrusted regardless of extension.
2. Validate format by parser and content, not extension or MIME alone. Bound size, dimensions, entry count, compression ratio, nesting, parse time, memory, and output.
3. Use robust parsers in a constrained process when possible. Audit native codecs and document libraries for memory-safety and command-execution risk.
4. Prevent path traversal, absolute paths, symlink extraction, hard-link abuse, device files, alternate streams, overwrite, permission inheritance, and archive bombs.
5. Create exports atomically with safe permissions and explicit overwrite behavior. Avoid leaking secrets, hidden columns, deleted records, internal IDs, or unrelated account data.
6. Sanitize filenames for each platform without creating collisions or losing the ability to map back to the source.
7. Mark or quarantine downloaded/generated files where platform expectations require it, and do not auto-open executable or active content.
8. Test malformed, truncated, oversized, polyglot, password-protected, nested, malicious-name, and concurrently modified files.

## 14. Network, Local Services, Proxies, And Certificates

### 14.1 Remote Network Calls

1. Inventory frontend, main/Rust, plugin, sidecar, updater, telemetry, crash, licensing, payment, and installer network clients.
2. Define connect, TLS, header, body, idle, stream, total, and retry deadlines. Propagate cancellation and distinguish user cancellation from network failure.
3. Retry only safe or idempotent operations with bounded attempts, exponential backoff, jitter, retry budgets, and respect for server rate-limit signals.
4. Validate redirects, final origin, content type, size, certificate, proxy behavior, and DNS changes for privileged downloads and update metadata.
5. Protect against SSRF where user-controlled URLs can reach localhost, private ranges, metadata services, Unix sockets, named pipes, or privileged local endpoints.
6. Do not disable TLS verification globally. If certificate pinning or custom roots are used, define rotation, expiry, backup trust, proxy compatibility, and recovery.
7. Redact authorization headers, cookies, tokens, device identifiers, license data, personal content, and query secrets from logs and crash reports.
8. Test offline, captive portal, DNS failure, proxy auth, TLS interception, expired certificate, clock skew, slowloris, partial response, oversized response, and retry storm.

### 14.2 Local HTTP, Socket, Pipe, And Service Interfaces

1. Inventory every localhost listener, Unix socket, named pipe, loopback WebSocket, custom URI broker, privileged service, browser callback server, and developer port.
2. Bind to the narrowest interface and use OS permissions, random unguessable endpoints, authentication, origin checks, request schemas, rate limits, and lifetime controls.
3. Do not assume localhost is trusted. Browsers, other users, sandboxed apps, malware, and local network exposure can reach incorrectly bound services.
4. Protect against DNS rebinding, browser cross-origin requests, CSRF-like local requests, port prediction, stale socket files, named-pipe squatting, and service impersonation.
5. Validate peer identity for privileged service or helper communication. Bind requests to the current app instance, user, session, version, and intended operation.
6. Define startup races, port conflicts, service upgrade order, version handshake, reconnect, graceful shutdown, and orphan cleanup.
7. Never expose generic shell, filesystem, database, update, or credential functions over a local endpoint without strong authentication and narrow authorization.
8. Test unauthenticated local requests, cross-origin browser requests, another OS user, stale client, wrong version, replay, oversized payload, slow client, and process crash.

## 15. Operating-System Integration And External Inputs

### 15.1 Deep Links, Protocol Handlers, File Associations, And CLI

1. Inventory custom URI schemes, app links, universal links, file associations, open-with handlers, shell verbs, context-menu entries, command-line switches, startup arguments, and store activation payloads.
2. Treat every payload as untrusted. Parse structurally, bound size/count, canonicalize paths/URLs, require expected action types, and reject unknown fields and schemes.
3. Protect authentication callbacks with state, nonce, PKCE, expected issuer, account binding, one-time use, and expiry.
4. Prevent argument, shell, URL, path, and template injection when forwarding payloads to an existing instance or helper.
5. Define behavior before the app is ready, during update, with multiple instances, with no signed-in account, and after account switch.
6. Do not execute or auto-open content merely because the OS associated it with the application.
7. Register and unregister integrations consistently across fresh install, per-user/per-machine install, upgrade, repair, portable mode, store install, channel coexistence, and uninstall.
8. Test malformed encoding, huge payloads, duplicate activation, nested URL, local-file URL, alternate scheme, stale account, and simultaneous activations.

### 15.2 Tray, Menus, Shortcuts, Clipboard, Notifications, And Autostart

1. Map every tray/menu/global-shortcut/notification action to an authorized command and current account/window state.
2. Do not trust menu IDs, notification payloads, or global shortcut events as proof of user identity or intent.
3. Prevent duplicate registrations and stale handlers across reload, update, account switch, display changes, sleep/wake, and multiple instances.
4. Minimize sensitive clipboard exposure; clear only with careful ownership logic and never destroy unrelated user clipboard content.
5. Sanitize notification content and actions. Avoid displaying secrets on the lock screen and validate activation payloads.
6. Justify autostart, background mode, login-item helpers, scheduled tasks, services, and startup registry/plist entries. Provide visible user control and removal.
7. Verify accessibility and keyboard navigation of native menus, tray flows, dialogs, and shortcuts, including conflicts and localized labels.
8. Test denied OS permission, revoked permission, changed default app, stale notification, shortcut conflict, multiple monitors, locked session, and OS restart.

### 15.3 Devices, Media, Screen Capture, Printing, And Hardware

1. Inventory camera, microphone, display capture, audio output, USB, serial, HID, Bluetooth, smart card, printer, scanner, GPU, codec, and custom-driver use.
2. Request the minimum OS and web permission at the moment of need, explain the purpose, handle denial, and support revocation.
3. Authorize device selection and operations against the current user/account and business policy; device presence is not authorization.
4. Validate device descriptors and data lengths. Bound streams, frame sizes, sample rates, buffers, recording duration, and storage.
5. Prevent unintended background capture after window close, logout, sleep, lock, account switch, or permission revocation.
6. Audit screen-capture source selection and prevent silent capture of sensitive windows where policy requires.
7. Treat printer names, paths, page settings, media files, codecs, and device firmware responses as untrusted inputs.
8. Test device removal, permission denial, partial frames, malformed data, driver crash, hotplug storms, sleep/wake, multiple devices, and update during active use.

## 16. Auto-Update, Release Channels, Rollback, And Revocation

### 16.1 Common Update Trust Model

1. Map who can build, sign, publish, modify metadata, change endpoints, promote channels, trigger rollout, pause rollout, force update, permit downgrade, and revoke a release.
2. Separate artifact identity, transport security, metadata authenticity, artifact signature, platform code signature, channel policy, and installer authorization. Each solves a different problem.
3. Use immutable versioned artifacts. Never replace bytes at an existing version URL after release.
4. Bind metadata to exact product, channel, platform, architecture, version, minimum/current version rules, artifact hash or signature, size, publication time, and rollout policy.
5. Validate update metadata as untrusted network input. Bound size and fields, reject unknown platform mappings where dangerous, and handle clock skew.
6. Prevent downgrade and cross-channel confusion by default. If controlled rollback requires downgrade, define explicit authorization, compatibility checks, user-data migration behavior, and re-upgrade.
7. Use staged rollout with telemetry, minimum sample, soak period, crash/startup/update/error thresholds, manual pause, automatic abort, and owner.
8. Define behavior for offline users, skipped versions, very old clients, unsupported OS, unsupported architecture, proxy/captive portal, metered network, low disk, and interrupted download.
9. Verify full and differential update paths independently. A delta update must not bypass integrity, signing, or package-content checks.
10. Test update from every supported source version to the candidate, not only candidate-to-candidate or clean install.
11. Define rollback for application code, local data/schema, sidecars/services, protocols, file associations, configuration, and cached frontend state.
12. Maintain a kill switch or channel disable mechanism that does not itself create an unauthenticated remote-control path.
13. Define certificate/key compromise response: freeze publishing, revoke or remove trust, rotate keys where architecture permits, issue a trusted replacement, and communicate recovery.
14. Preserve update logs and artifacts needed for incident investigation without recording secrets.

### 16.2 Electron Updater Audit

1. Identify the updater implementation: built-in `autoUpdater`, `update-electron-app`, Electron Forge publisher/update service, Electron Builder updater, custom updater, store updater, or external enterprise tool.
2. Verify platform and package support for the exact updater. Built-in behavior differs among macOS, Squirrel.Windows, MSIX, and Linux packaging; do not assume one API provides identical cross-platform semantics.
3. On macOS, verify code signing, notarization where required, application identity, feed format, signature behavior, and hardened runtime/entitlements compatibility.
4. On Windows, verify Squirrel/MSIX/NSIS/custom installer behavior, application user model ID, per-user/per-machine scope, update locks, running instances, and repair/uninstall interaction.
5. Guard against duplicate update checks and downloads. Ensure UI actions, timers, startup checks, reconnect, and multiple windows cannot start competing updates.
6. Validate feed URL and channel selection. Prevent renderer-controlled arbitrary feed URLs or release channels unless strictly authorized.
7. Verify `checkForUpdates`, download, cancellation, progress, ready state, quit-and-install, restart, and error transitions as one explicit state machine.
8. Do not install while critical writes, migrations, exports, recordings, device operations, or irreversible jobs are active unless the operation can resume safely.
9. Verify code-signature checks and package verification on the final distribution path. Test modified metadata, modified package, wrong publisher, wrong channel, wrong architecture, and expired/revoked certificate conditions.
10. Test fresh install, normal update, skipped versions, very old client, update while app is running in tray, multiple instances, interrupted download, low disk, locked file, antivirus interference, and forced shutdown.

### 16.3 Tauri Updater Audit

1. Resolve the exact updater plugin version, Rust and JavaScript API versions, capabilities, permissions, public key, endpoint configuration, install mode, and platform support.
2. Verify that update signatures are mandatory and checked against the intended pinned public key. Protect the private signing key separately from platform code-signing keys.
3. Restrict frontend updater permissions. A window that may check availability does not automatically need download or install authority.
4. Validate static JSON or dynamic server metadata, including RFC 3339 date if used, semantic version, platform key, architecture, signature contents, URL, size, and release notes.
5. Verify runtime endpoint and header overrides cannot be influenced by untrusted renderer content or lower-trust configuration.
6. Test Windows install modes, elevation prompts, restart behavior, running sidecars/services, and per-user/per-machine consistency.
7. Test Linux package-specific behavior instead of treating AppImage, Debian, RPM, Flatpak, Snap, and distribution repositories as interchangeable.
8. Test macOS app bundle identity, signing, notarization, quarantine, update replacement, and rollback behavior.
9. If custom version comparison permits rollback, require an authenticated rollback decision, data compatibility gate, explicit telemetry, and a plan to return users to a safe forward version.
10. Test bad signature, missing signature, wrong key, modified package, wrong OS/architecture key, server error, partial download, low disk, denied permission, interrupted installation, and old client.

## 17. Code Signing, Notarization, Keys, And Artifact Trust

### 17.1 Signing Architecture

1. Inventory every signing identity and purpose: Windows executable/installer, macOS application/installer, Apple notarization credentials, Linux packages, Tauri updater, store upload, mobile targets, and internal enterprise signing.
2. Use separate keys where threat model or tooling requires separation. Document which compromise affects which channel and how trust can be recovered.
3. Keep private keys in hardware-backed or managed signing systems where practical. Restrict export, interactive use, CI access, roles, approvals, IP/network, repository, branch, and environment.
4. Use timestamping where platform policy supports it so valid releases survive certificate expiry. Verify timestamp authority and failure behavior.
5. Record certificate subject, issuer, serial/thumbprint, validity, key algorithm, timestamp, entitlements, hardened-runtime state, notarization result, and exact artifact hash without exposing private material.
6. Verify signatures after all packaging, fuse, resource, installer, and update transformations. Never modify a signed artifact silently.
7. Define certificate renewal overlap, revocation, lost-key response, expired certificate behavior, publisher identity continuity, and emergency release procedures.
8. Separate signing from publishing so a signed artifact still requires reviewed promotion to a channel.
9. Audit who can submit arbitrary bytes to the signing service. A protected key is insufficient if untrusted jobs can request signatures.
10. Verify local signature checking and store/platform verification on clean machines, not only inside CI.

### 17.2 macOS Signing, Hardened Runtime, Entitlements, And Notarization

1. Verify bundle identifier, team ID, certificate type, designated requirement, nested-code signatures, frameworks, helpers, login items, XPC/services, sidecars, and installer images.
2. Use the minimum entitlements. Justify JIT, unsigned executable memory, disabled library validation, automation, camera, microphone, screen recording, files, network, keychain groups, and sandbox exceptions.
3. Ensure every nested executable and framework is signed in the correct order with compatible entitlements before the outer bundle.
4. Run strict signature verification and assess Gatekeeper behavior on a clean downloaded artifact with quarantine metadata.
5. Submit the exact release artifact for notarization, verify success, staple where applicable, and confirm offline/online Gatekeeper behavior.
6. Test direct download, DMG/PKG, App Store build where applicable, update replacement, helper launch, first run, permission prompts, and OS-version differences.
7. Define behavior when notarization is unavailable, delayed, rejected, or later invalidated. Do not release an unverified substitute.
8. Preserve notarization logs and submission IDs tied to artifact hashes for incident response.

### 17.3 Windows Signing And Reputation

1. Verify Authenticode signatures on executables, DLLs, installers, update packages, drivers/helpers, and catalog files where applicable.
2. Use the intended publisher identity consistently across releases to preserve upgrade trust and reputation. Document certificate renewal and organization changes.
3. Timestamp signatures and verify both signature and timestamp chain on clean supported Windows versions.
4. Audit EV/standard certificate or managed-signing workflow, HSM/Key Vault access, sign-command arguments, digest algorithm, dual-signing needs, and cross-signing assumptions.
5. Verify SmartScreen/Mark-of-the-Web behavior for direct downloads and how reputation is monitored without weakening user protection.
6. Ensure unsigned or differently signed child binaries cannot be loaded from writable directories or bundled accidentally.
7. Test install, repair, update, rollback, uninstall, side-by-side channels, per-user/per-machine scope, UAC, locked files, antivirus, and enterprise policy.
8. Define response to compromised publisher credentials, revoked certificate, false-positive malware classification, and store suspension.

### 17.4 Linux Package Signing And Repository Trust

1. Identify each distribution format and trust model: AppImage, Debian, RPM, Flatpak, Snap, AUR/source package, tarball, or managed enterprise repository.
2. Verify package/repository signatures, metadata expiry, key distribution, rotation, revocation, mirror trust, and update ownership.
3. Audit desktop files, MIME handlers, icons, AppStream metadata, sandbox permissions, portals, systemd units, polkit rules, post-install scripts, and uninstall scripts.
4. Do not treat a signed package as universally trusted across distributions. Test the exact repository, store, or direct-download path.
5. Verify library dependencies and minimum distribution versions on clean supported environments, including WebKitGTK and system runtime requirements for Tauri.
6. Test install, upgrade, downgrade, rollback, package-manager conflict, read-only filesystem, sandbox portals, missing dependencies, and offline enterprise mirrors.
7. Define how direct-download users receive security updates when no built-in updater exists or when distribution policies own updates.
8. Document key compromise and repository takeover response.

## 18. Installer, Store, Enterprise, Upgrade, And Uninstall Behavior

### 18.1 Installer Semantics

1. Identify installer technology, version, scope, elevation model, install path, data path, repair behavior, upgrade code/product code/bundle identity, custom actions, prerequisites, and rollback support.
2. Verify fresh install, same-version repair, patch/minor/major upgrade, downgrade rejection, side-by-side channels, per-user to per-machine transition, architecture transition, and uninstall.
3. Make custom actions minimal, deterministic, logged, retry-safe, and reversible. Never hide arbitrary network downloads or shell execution inside an installer.
4. Validate paths and permissions created by the installer. Prevent normal users from replacing executable files, DLLs, helpers, update components, or privileged configuration.
5. Preserve user data intentionally, migrate it explicitly, and remove it only according to documented user/enterprise choice.
6. Handle running application instances, tray processes, services, sidecars, locked files, antivirus, reboot-required state, and interrupted installation.
7. Verify registration and cleanup of protocols, file associations, shortcuts, startup entries, services, scheduled tasks, firewall rules, drivers, and store metadata.
8. Test installer logs and error messages for secret leakage and actionable recovery.

### 18.2 Stores And Enterprise Distribution

1. Map Microsoft Store, Mac App Store, Snap/Flatpak stores, package repositories, MDM, software-distribution tools, and direct-download channels separately.
2. Review sandbox, entitlement, API, payment, update, telemetry, privacy, age-rating, and content rules for each channel.
3. Use channel-specific configuration rather than runtime guessing. Verify bundle identity and data-path continuity between store and direct builds only when migration is supported.
4. Prevent a lower-trust channel from updating or replacing a higher-trust channel unintentionally.
5. Verify offline installers, proxy support, certificate deployment, WebView/runtime prerequisites, silent install switches, exit codes, logs, and detection rules for enterprise use.
6. Document ownership of store accounts, publisher organizations, recovery contacts, MFA, API keys, signing profiles, and emergency access.
7. Test store review/rejection fallback, phased release pause, package withdrawal, mandatory update constraints, and users stuck on old store versions.
8. Ensure release notes, privacy declarations, permissions, data safety, and screenshots match actual behavior.

## 19. Performance, Responsiveness, Resource Use, And Capacity

### 19.1 Measurement Plan

1. Define budgets for cold/warm startup, first usable window, critical interaction latency, IPC/command latency, update check, memory, CPU, GPU, disk, network, battery, installer size, and package size.
2. Measure on representative minimum and typical hardware, supported operating systems, x64/ARM64, clean and mature profiles, online/offline, and with realistic data volumes.
3. Separate frontend render time, framework bootstrap, native initialization, database migration, credential access, network wait, plugin initialization, sidecar startup, and updater work.
4. Capture traces and profiles before optimizing. Correlate long tasks, main-thread blocking, Rust/Node blocking, lock contention, IPC serialization, database queries, filesystem, GPU, and network.
5. Test idle behavior, hidden/tray mode, minimized windows, background timers, service workers, polling, telemetry, device listeners, and updater cadence.
6. Bound caches and queues. Define eviction, persistence, account isolation, stale-data policy, and memory-pressure behavior.
7. Measure leak behavior across window open/close, navigation, reload, account switch, document open/close, device connect/disconnect, update, and long-running idle.
8. Do not claim performance improvement from microbenchmarks alone; confirm the user journey and resource budget.

### 19.2 Responsiveness And Failure Containment

1. Keep renderer/UI threads responsive. Move CPU-heavy parsing, compression, indexing, media, cryptography, and database work to suitable bounded workers or native processes.
2. Do not block the Electron main process or Tauri event loop with synchronous filesystem, network, crypto, database, child-process, or lock waits.
3. Use backpressure from UI through IPC/commands to workers and external services. Dropping, coalescing, pausing, or rejecting work must be explicit.
4. Prevent one slow window, file, device, network request, tenant/account, or plugin from exhausting global resources.
5. Define timeouts and cancellation for operations that can hang. Ensure cancellation does not leave corrupted files, half-applied migrations, or duplicated side effects.
6. Handle out-of-memory, GPU crash, renderer crash, sidecar crash, WebView failure, database lock, and service outage with bounded recovery.
7. Use crash restart only with limits and state validation. Avoid loops that repeatedly destroy user work or hammer update/network services.
8. Test burst input, huge history, many windows, large files, slow disk, low memory, high DPI, multiple displays, sleep/wake, and prolonged offline mode.

## 20. Accessibility, Localization, Display, And Input

1. Test keyboard-only operation, logical focus order, focus restoration, visible focus, shortcuts, menus, dialogs, tray flows, modals, drag alternatives, and escape/cancel behavior.
2. Verify semantic roles, names, states, descriptions, live regions, error association, table/list structure, and screen-reader behavior.
3. Support zoom, text scaling, OS scaling, high contrast, reduced motion, color filters, large fonts, and display density without clipping or inaccessible controls.
4. Test high DPI, mixed-DPI monitors, display connect/disconnect, orientation, window restore from unavailable screens, minimum size, fullscreen, and remote desktop.
5. Localize all user-visible and accessibility text, native menus, notifications, installer strings, file filters, permission explanations, update messages, and error recovery.
6. Handle RTL, pluralization, date/time/number/currency formats, time zones, Unicode normalization, long translations, and locale-specific sorting/search.
7. Respect IME, dead keys, compose keys, alternate keyboard layouts, screen keyboards, pen/touch, mouse alternatives, and assistive technology.
8. Do not rely on color, hover, animation, tiny targets, or platform-inconsistent gestures as the only communication method.
9. Test accessibility in the packaged application on each platform; browser-only testing is insufficient.
10. Document justified exceptions with user impact, workaround, owner, and remediation plan.

## 21. Observability, Crash Reporting, Privacy, And Forensics

1. Define structured logs, metrics, traces, crash reports, update events, installer events, security events, and user-visible diagnostic export.
2. Include version, channel, commit/artifact identity, platform, architecture, OS version, WebView/Chromium/Node/Rust relevant version, process type, window label, correlation ID, and operation state where safe.
3. Redact secrets, tokens, cookies, authorization headers, file contents, personal paths, usernames, document names, database records, clipboard data, and sensitive URLs.
4. Use sampling and rate limits to prevent telemetry storms, privacy overcollection, disk exhaustion, and recursive crash-reporting failures.
5. Upload symbols and source maps tied to exact artifact hashes. Restrict access and retention.
6. Distinguish renderer/webview, main/Rust core, GPU, utility, sidecar, installer, updater, and native crash sources.
7. Track startup success, crash-free sessions, update adoption/failure, rollback, migration failure, permission denial, IPC/command denial, queue saturation, and resource budgets.
8. Provide a privacy-preserving local diagnostic bundle with explicit user review and consent where appropriate.
9. Preserve chain of custody for incident artifacts and avoid altering compromised systems before evidence capture.
10. Every production alert must have owner, threshold rationale, dashboard/context, runbook, and user-impact interpretation.

## 22. Test Strategy And Mandatory Negative Scenarios

### 22.1 Test Layers

1. Unit-test pure business logic, parsers, validators, canonicalizers, state machines, authorization decisions, migration steps, and update-version policy.
2. Contract-test every preload bridge, Electron IPC channel, Tauri command, event/channel payload, sidecar protocol, local service, update metadata, and installer exit-code contract.
3. Integration-test with real filesystem semantics, real embedded database engine, secure-storage abstraction, representative proxy/certificate setup, and actual platform WebView/runtime where applicable.
4. Run packaged-application tests, not only browser/dev-server tests. Verify effective privileges, resources, signatures, paths, and OS integrations.
5. Use end-to-end tests for critical user journeys: install, first run, sign in, account switch, file/device workflow, offline/online transition, update, restart, rollback, export, logout, and uninstall.
6. Use security tests for XSS-to-bridge reachability, IPC/command authorization, path/URL validation, local-service authentication, update tampering, signature failure, and data isolation.
7. Use concurrency and durability tests for duplicate actions, multiple windows, multiple instances, background jobs, database locking, update overlap, shutdown, and crash recovery.
8. Use performance tests for startup, critical interactions, large data, burst input, many windows, idle, long-run leaks, low resources, and slow dependencies.
9. Use accessibility tests with automated checks plus keyboard and screen-reader verification in packaged builds.
10. Use installation and update matrices on clean snapshots/VMs with realistic old versions and user data.
11. Every confirmed P0-P2 fix must have a focused regression test that would fail before the fix and pass after it.
12. Record skipped, flaky, quarantined, platform-unavailable, or manually verified tests with owner, reason, risk, and exit criterion.

### 22.2 Mandatory Adversarial And Failure Scenarios

1. Compromised renderer/webview attempts every exposed Electron bridge or Tauri command from the wrong origin, frame, window, label, account, and lifecycle generation.
2. Malicious IPC/command payload uses extra fields, wrong types, deep nesting, huge strings/binaries, traversal, symlinks, UNC/device paths, alternate schemes, and encoded separators.
3. Two windows or instances submit the same destructive or externally visible operation concurrently and after a renderer reload.
4. Caller navigates, logs out, changes account, closes, or is destroyed while privileged work is in progress and before the result is delivered.
5. Remote content redirects, opens a new window, calls an external protocol, downloads active content, and attempts to retain privileges after navigation.
6. Local untrusted process attempts to connect to localhost/socket/pipe/helper interfaces, replay messages, impersonate the application, or squat on the endpoint.
7. Update metadata, package, signature, publisher, channel, architecture, version, and endpoint are independently tampered with.
8. Update is interrupted during download, verification, install, first restart, data migration, sidecar replacement, and cleanup.
9. Fresh install, repair, upgrade from each supported old version, skipped-version upgrade, downgrade attempt, rollback, and uninstall run with realistic user data.
10. Signing certificate or updater key is expired, revoked, missing, wrong, inaccessible, or believed compromised.
11. Disk becomes full or read-only during write, database transaction, migration, export, download, update, logging, and crash reporting.
12. Application is terminated, OS shuts down, user logs out, machine sleeps, or power is lost during critical work.
13. Native module, sidecar, plugin, WebView runtime, codec, driver, or system dependency is missing, wrong architecture, incompatible, slow, hung, or maliciously replaced.
14. Proxy auth, captive portal, DNS failure, TLS interception, certificate error, clock skew, slow server, partial response, oversized response, and retry storm occur.
15. User switches accounts, OS users, channels, or profiles while caches, cookies, windows, background work, notifications, and local data still exist.
16. Many windows, large files, hotplug storms, burst IPC/events, slow consumer, and long-running idle push CPU, memory, GPU, disk, queue, and listener limits.

### 22.3 Platform And Architecture Matrix

| Dimension | Required coverage | Evidence |
| --- | --- | --- |
| Operating system | Each supported Windows, macOS, and Linux baseline plus current representative versions | Clean VM/device, exact build, install/update/runtime results |
| Architecture | x64, ARM64, and any additional shipped target | Native module/sidecar/plugin/package/signature/runtime verification |
| Distribution | Direct, store, enterprise, portable, repository, or package format actually shipped | Channel-specific install, update, rollback, and policy evidence |
| Source version | Fresh install and every supported upgrade source, including a realistically old version | Versioned snapshots with representative user data |
| Environment | Online, offline, proxy, enterprise TLS interception where supported, low disk, low memory | Recorded conditions, logs, user-visible outcome, recovery |
| Display/input | Single/multiple mixed-DPI displays, keyboard, screen reader, IME, touch where supported | Packaged-app accessibility and window-state evidence |

## 23. CI/CD, Release Governance, And Artifact Promotion

1. Map workflows from pull request to test, package, sign, notarize, publish, promote, store upload, update manifest, rollout, pause, rollback, and incident release.
2. Separate untrusted code execution from privileged release jobs. Require reviewed commits, protected environments, approvals, and branch/tag policy.
3. Use matrix builds for supported platforms/architectures and record which steps run natively, cross-compile, or use remote builders.
4. Promote the same immutable artifact through verification, signing where ordering permits, staging, and release. Explain every unavoidable transformation.
5. Verify package contents, fuses/capabilities, SBOM, provenance, signatures, notarization, installer metadata, malware/reputation scans, and update metadata before promotion.
6. Protect release version allocation from races and duplicate tags. Ensure application, package, installer, store, and feed versions remain consistent.
7. Require release notes with security/privacy/migration/update impact, known issues, support changes, and rollback conditions.
8. Define automated and manual release gates, abort thresholds, canary/phased cohorts, soak periods, owner, and emergency stop.
9. Retain exact artifacts, symbols, source maps, manifests, logs, signatures, hashes, approvals, and environment identity for the support and incident window.
10. Test the release pipeline using non-production signing/update/store targets and periodically exercise emergency release and rollback.
11. Do not allow the renderer/frontend, a pull-request job, or a general developer token to publish update metadata or signed artifacts.
12. Record residual manual steps and make them two-person, checklist-driven, auditable, and recoverable.

## 24. Migration And Modernization Overlays

### 24.1 Electron Major Upgrade

1. Upgrade one supported major at a time unless authoritative evidence and tests justify another path.
2. Review breaking changes, removed defaults/APIs, Chromium behavior, Node/V8 changes, sandbox/context isolation, protocol/session changes, and packaging/updater compatibility.
3. Rebuild and test every native module and sidecar on every target. Verify ABI, prebuild availability, fallback compiler, and runtime loading.
4. Compare package content, fuses, signatures, permissions, startup, memory, CPU, rendering, media, printing, accessibility, and installer/update behavior.
5. Run old-version to new-version update and rollback/data-compatibility tests before broad rollout.
6. Do not use the upgrade to mix unrelated architecture rewrites unless separately scoped and reversible.

### 24.2 Tauri 1 To 2 Or Major Plugin Migration

1. Inventory removed/renamed APIs, plugin extraction, capability/permission model, generated configuration, command registration, frontend API, mobile changes, and bundler differences.
2. Translate allowlists into least-privilege capabilities instead of granting broad defaults to restore functionality.
3. Review each plugin's v2 permissions, scopes, platform support, data migration, and update behavior independently.
4. Diff generated schemas, capabilities, manifests, entitlements, installers, and package contents before and after migration.
5. Test all commands from allowed and denied windows/origins, because a build passing does not prove capability correctness.
6. Verify updater signing keys, metadata, package formats, source-version compatibility, rollback, and user-data paths.
7. Audit Rust async/state/unsafe changes and system WebView requirements on minimum supported platforms.
8. Keep a reversible branch/artifact/data migration path until production evidence is sufficient.

### 24.3 Electron To Tauri Or Tauri To Electron Migration

1. Start from required capabilities, platform support, WebView/runtime behavior, native integrations, updater, installer, accessibility, enterprise constraints, and total maintenance cost, not binary-size marketing.
2. Map every existing privilege and IPC/command contract. Redesign least privilege rather than mechanically recreating a broad bridge.
3. Prototype the highest-risk flows first: remote content, auth, files, native modules, sidecars, devices, media, printing, updater, signing, stores, and enterprise deployment.
4. Define data-path, secure-storage, bundle identity, protocol/file association, signing identity, channel, installer, and update continuity.
5. Test UI/rendering and Web API differences across Chromium and system WebViews, including oldest supported OS versions.
6. Plan coexistence, migration, rollback, telemetry comparison, user communication, and support for users who cannot migrate.
7. Do not declare success from feature parity alone; require operational, security, update, accessibility, and recovery parity.
8. Keep the old production path recoverable until adoption and stability gates are met.

## 25. Incident Mode

1. Preserve volatile evidence before cleanup: running processes, executable paths, loaded modules, command lines, network connections, open files, updater state, installer logs, signatures, hashes, browser/WebView storage, and relevant memory/crash artifacts.
2. Isolate affected release channels, signing/publishing credentials, update endpoints, stores, CDN objects, local services, and administrative access according to the containment plan.
3. Determine whether compromise is in renderer content, privileged bridge, native core, dependency, build system, signing system, update metadata, distribution channel, installer, local data, or external service.
4. Do not destroy evidence by reinstalling, auto-updating, deleting cache, rotating all keys blindly, or running unreviewed cleanup tools before collection.
5. Revoke or disable the smallest affected trust path first, but assume broader impact until evidence narrows it.
6. Build replacement artifacts from a verified commit in a trusted clean environment with reviewed dependencies, new or verified credentials, SBOM, provenance, signatures, and package inspection.
7. Test clean install, in-place recovery, compromised-version update, data preservation, credential reset, key rotation, and rollback before release.
8. Communicate affected versions, platforms, channels, indicators, user actions, data impact, and recovery status accurately without speculation.
9. Preserve a timeline of source, build, signing, publishing, distribution, install, execution, detection, containment, eradication, recovery, and follow-up.
10. Produce root cause, control failure, detection gap, blast radius, recovery evidence, residual risk, and prevention actions with owners and deadlines.

## 26. Mandatory Evidence Matrices

### 26.1 Source-To-Runtime Matrix

| source commit | resolved graph | builder | package | signature | distribution object | installed binary | runtime process | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.2 Window And WebView Privilege Matrix

| window/webview | origin | session/partition | preload/capability | permissions | data/account | navigation | owner | tests | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.3 IPC And Command Matrix

| channel/command | caller | schema | authentication | authorization | scope | side effect | idempotency | limits | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.4 Filesystem And External-Open Matrix

| operation | source | canonicalization | allowed scope | symlink/race defense | permissions | audit | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.5 Local Data And Migration Matrix

| store/path | owner | sensitivity | schema/version | migration | backup | restore | account isolation | deletion | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.6 Network And Local-Service Matrix

| client/listener | endpoint | trust | auth | TLS/peer check | timeout | retry/backpressure | data | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.7 Dependency And Native-Code Matrix

| component | resolved version | source | shipped | privilege | native/build code | advisory | compatibility | owner | action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.8 Artifact, Signing, And Store Matrix

| platform/channel | artifact | hash | package content | signing identity | timestamp/notary | store/repository | verification | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.9 Update And Rollback Matrix

| source version | target | platform/channel | metadata | signature | data migration | failure point | rollback/recovery | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.10 Platform And Installer Matrix

| OS/version | architecture | format | fresh install | upgrade | repair | rollback | uninstall | OS integration | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.11 Performance And Resource Matrix

| journey | device/profile | budget | measured | bottleneck | fix | regression test | residual risk | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

### 26.12 Operational Readiness Matrix

| control | owner | evidence | alert | runbook | abort threshold | rollback | last exercise | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` | `[FILL]` |

## 27. Production Readiness Checklist

1. Supported framework/runtime/toolchain versions are verified from source, lock files, packaged artifact, and runtime. No unapproved preview or unsupported major remains.
2. Repository, generated configuration, dependency graph, build scripts, native code, plugins, and supply-chain trust are inventoried and owned.
3. Source-to-installed-runtime identity chain is proven or every break is an explicit blocker/residual risk.
4. Every window/webview has documented origin, lifecycle, session, privilege, bridge/capability, navigation policy, data owner, and negative tests.
5. Electron webPreferences/preload/IPC or Tauri capabilities/permissions/scopes/commands enforce least privilege in the actual packaged app.
6. Remote and user-controlled content cannot reach local code, secrets, files, devices, updater, installer, or other accounts without explicit authorization.
7. Path, URL, deep-link, external-open, file import/export, archive, and local-service boundaries are canonicalized, scoped, authenticated, and tested.
8. Local data has ownership, permissions, schema/migration, backup/restore, corruption recovery, account isolation, retention, and uninstall policy.
9. Critical writes and external side effects have constraints, transactions or durable state transitions, concurrency control, idempotency, and crash recovery.
10. Network clients and local listeners have TLS/peer trust, authentication, timeouts, bounded retry, cancellation, backpressure, redaction, and failure tests.
11. Native modules, FFI, sidecars, codecs, system dependencies, and WebView runtimes are verified on every supported platform/architecture.
12. Package contents contain no unintended secrets, debug surfaces, writable executable code, unsupported binaries, or unexplained additions.
13. Every distributed artifact is tied to source, inspected, hashed, signed as required, timestamped/notarized where applicable, and verified after installation.
14. Install, repair, upgrade from every supported source, skipped-version update, interrupted update, rollback/recovery, and uninstall are tested with representative data.
15. Update metadata, signatures, key custody, channel policy, staged rollout, abort, downgrade, rollback, revocation, and compromised-key response are proven.
16. Startup, responsiveness, memory, CPU, GPU, disk, network, idle, long-run, and failure-containment budgets are measured on representative systems.
17. Accessibility, localization, high DPI, multiple displays, keyboard, screen reader, IME, permissions, and native dialogs are verified in packaged builds.
18. Logs, metrics, traces, crashes, symbols/source maps, alerts, privacy redaction, diagnostic export, and runbooks support incident diagnosis.
19. CI/CD separates untrusted and privileged work, promotes immutable artifacts, protects signing/publishing, retains evidence, and exercises emergency release.
20. All P0/P1 findings are fixed or contain explicit containment and recovery; P2/P3 have owners, acceptance criteria, and priorities.
21. Commands, environments, outputs, skipped checks, evidence ceiling, changed files, tests, artifact hashes, and external sources are recorded.
22. Final verdict is `ready`, `ready-with-conditions`, or `not-ready`, with exact blockers and residual risk.

## 28. Definition Of Done

1. Workspace and user/signing data were protected; repository state and audit boundaries are recorded.
2. All relevant source, generated, dependency, build, package, signing, installer, updater, store, and runtime assets are inventoried.
3. Actual Electron/Tauri and embedded/runtime/tool versions are verified; support and compatibility are checked against current primary sources.
4. Clean locked restore/build, relevant static checks, tests, package generation, and artifact inspection are recorded with real commands and exit codes.
5. Architecture, process, window/webview, origin, privilege, IPC/command, local service, data, and update maps are complete.
6. Every material claim has an evidence status and level. Suspicions are separated from confirmed findings.
7. Every P0/P1 has evidence, root cause, impact, containment, repair, regression proof, release impact, rollback, and owner.
8. Applicable P2 findings have targeted remediation or a prioritized, testable plan. P3 work is not presented as a production blocker without cause.
9. Electron security settings or Tauri capabilities are verified in the packaged application with positive and negative tests.
10. Authentication, resource authorization, account/tenant isolation, session cleanup, secret storage, and privileged actions are verified.
11. Critical local writes, migrations, synchronization, and external side effects are safe under duplicate, concurrent, interrupted, and crash conditions.
12. Files, URLs, protocols, imports, exports, archives, downloads, external-open, local listeners, sidecars, and devices are constrained and tested.
13. Build and package supply chain, SBOM/provenance, artifact identity, signing, notarization, key custody, and revocation are verified.
14. Fresh install, upgrade matrix, repair, interrupted update, rollback/recovery, and uninstall are tested or clearly blocked with exact reasons.
15. Performance and resource claims are based on measurement; accessibility and localization are tested in packaged builds.
16. Observability and incident artifacts can identify exact version/channel/platform/process and diagnose critical failure without exposing sensitive data.
17. CI/CD gates, artifact promotion, staged rollout, abort, emergency release, rollback, and compromised-key procedures are documented and exercised where required.
18. Final diff is narrow, reviewable, free of unrelated changes, and includes necessary tests and documentation.
19. Final report contains exact commands, evidence, artifacts, hashes, changes, tests, blockers, residual risk, owners, and authoritative sources.
20. If any applicable condition is unmet, the application is not fully production-ready and the exact blocking condition is stated.

## 29. Forbidden Shortcuts

1. Do not declare success because the app starts in development mode, builds on one machine, passes browser tests, or produces an installer.
2. Do not enable Node integration, disable context isolation/sandbox/web security, broaden a Tauri capability, grant a default plugin permission, or expose generic IPC/commands merely to make a feature work.
3. Do not validate only in the renderer/frontend. Privileged boundaries must validate and authorize independently.
4. Do not silence TypeScript, Rust, compiler, linter, packaging, signing, notarization, installer, updater, or security warnings without root-cause analysis.
5. Do not add `any`, unchecked casts, `unwrap`, `expect`, broad `unsafe`, empty catch blocks, ignored promises/results, or blanket suppressions as universal fixes.
6. Do not use shell execution with interpolated input, arbitrary external-open URLs, unrestricted filesystem scopes, writable executable paths, or unauthenticated localhost services.
7. Do not disable TLS or certificate checks, accept all origins, log secrets, store long-lived tokens in frontend storage, or ship private keys.
8. Do not treat ASAR, obfuscation, minification, Rust, code signing, a sandbox, or capabilities as a complete security boundary by itself.
9. Do not auto-run destructive migrations, reset corrupted data silently, remove user data without policy, or install updates during unsafe critical work.
10. Do not publish mutable artifacts, rebuild separately per promotion stage without explanation, sign unreviewed bytes, or let untrusted CI access release credentials.
11. Do not raise memory, queue, timeout, retry, process, or file-size limits without capacity and abuse analysis.
12. Do not migrate Electron to Tauri, Tauri to Electron, rewrite the frontend, replace the database, or change installer technology merely for popularity or binary-size claims.
13. Do not delete another person's changes, mass-format the repository, hide unrelated diffs, skip failing tests, or weaken tests so a pipeline passes.
14. Do not claim cross-platform support without packaged install/runtime/update evidence on the supported platform matrix.
15. Do not call the application perfect, fully secure, or production-ready without satisfying the applicable evidence and recovery requirements.

## 30. Mandatory Final Report

1. Executive summary and verdict: `ready`, `ready-with-conditions`, or `not-ready`, with evidence ceiling.
2. Application and release context: framework, versions, platforms, architectures, channels, critical journeys, data, identities, and constraints.
3. Source-to-installed-runtime identity chain with artifact hashes and unresolved breaks.
4. Architecture, process, window/webview, origin, privilege, IPC/command, local service, data, installer, and update maps.
5. Version and support table: project, resolved, packaged/runtime, current stable, support status, compatibility, action, source.
6. Findings table: `ID | P0-P3 | evidence | framework/area | platform | file/symbol | cause | impact | fix | test | rollback | status`.
7. Implemented changes: exact files, configuration, dependencies, capabilities/permissions, signing/update/installer changes, migrations, and regression risk.
8. Actual commands: command, directory, environment/tool versions, platform, exit code, output summary, generated artifacts, and conclusion.
9. Build/test/package matrix, adversarial scenarios, performance/resource measurements, accessibility results, and blocked checks.
10. Artifact/package/signing/notarization/store/update verification with exact hashes, identities, timestamps, and channel.
11. Install, update, migration, rollback, recovery, uninstall, and incident-readiness results.
12. Security and privacy summary: renderer/webview isolation, IPC/command authorization, files/URLs, local services, secrets, telemetry, supply chain, and residual risk.
13. Operational readiness: SLO/budgets, telemetry, alerts, runbooks, staged rollout, abort, emergency release, key compromise, backup/restore, and owners.
14. Remaining work grouped as `blocks production`, `needed soon`, `planned refactor`, and `optional`, with owner, dependency, acceptance criterion, and target date.
15. External sources consulted: title, URL, version/status, access date, and decision informed.

## 31. Work Order

1. Protect workspace, user data, signing material, and release channels.
2. Inventory repository, generated files, dependencies, toolchains, and ownership.
3. Establish source-to-installed-runtime identity and current support baseline.
4. Run clean restore/build/static/test baselines without destructive changes.
5. Map architecture, processes, windows/webviews, origins, privileges, IPC/commands, data, and OS integrations.
6. Audit Electron-specific or Tauri-specific security and lifecycle controls.
7. Audit files, data, network, local services, native code, devices, and external inputs.
8. Inspect actual packages, signatures, installers, stores, update feeds, and installed state.
9. Reproduce and classify findings with root cause and evidence.
10. Implement authorized minimal fixes and focused regression tests.
11. Execute packaged platform, adversarial, performance, accessibility, install, update, rollback, and recovery verification.
12. Complete evidence matrices, release decision, roadmap, and final report.

## 32. Primary Source Register

| Source | URL | Use |
| --- | --- | --- |
| Electron Releases | https://releases.electronjs.org/ | Current stable/prerelease and embedded Chromium/Node versions. |
| Electron Security | https://www.electronjs.org/docs/latest/tutorial/security | Official security checklist and renderer isolation guidance. |
| Electron Breaking Changes | https://www.electronjs.org/docs/latest/breaking-changes | Major upgrade compatibility. |
| Electron Fuses | https://www.electronjs.org/docs/latest/tutorial/fuses | Package-time hardening and fuse verification. |
| Electron ASAR Integrity | https://www.electronjs.org/docs/latest/tutorial/asar-integrity | Embedded ASAR integrity requirements. |
| Electron Updating Applications | https://www.electronjs.org/docs/latest/tutorial/updates | Updater architecture and platform differences. |
| Electron autoUpdater API | https://www.electronjs.org/docs/latest/api/auto-updater | Runtime updater semantics and events. |
| Electron Code Signing | https://www.electronjs.org/docs/latest/tutorial/code-signing | Platform signing guidance. |
| Electron Distribution Overview | https://www.electronjs.org/docs/latest/tutorial/distribution-overview | Packaging, signing, and updating overview. |
| Tauri Ecosystem Releases | https://v2.tauri.app/release/ | Core, CLI, API, runtime, Wry, Tao, bundler, and plugin releases. |
| Tauri Capabilities | https://v2.tauri.app/security/capabilities/ | Window/webview capability boundaries and merge behavior. |
| Tauri Permissions | https://v2.tauri.app/security/permissions/ | Allow, deny, and scope definitions. |
| Tauri Runtime Authority | https://v2.tauri.app/security/runtime-authority/ | Runtime origin, capability, permission, and scope enforcement. |
| Tauri Command Scopes | https://v2.tauri.app/security/scope/ | Application-defined scope enforcement responsibilities. |
| Tauri Updater | https://v2.tauri.app/plugin/updater/ | Signed update metadata, platforms, endpoints, and permissions. |
| Tauri Distribution | https://v2.tauri.app/distribute/ | Platform package formats, stores, and signing. |
| Rust Releases | https://blog.rust-lang.org/releases/latest/ | Current stable Rust and release status. |
| Node.js Releases | https://nodejs.org/en/about/previous-releases | Node.js lifecycle where Electron tooling or sidecars use Node. |
| Apple Developer Documentation | https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution | macOS notarization and platform trust. |
| Microsoft Code Signing Documentation | https://learn.microsoft.com/windows-hardware/drivers/dashboard/code-signing-reqs | Windows signing and publisher trust context. |
