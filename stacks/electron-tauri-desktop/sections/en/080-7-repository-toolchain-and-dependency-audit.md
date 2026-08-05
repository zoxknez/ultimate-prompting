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

