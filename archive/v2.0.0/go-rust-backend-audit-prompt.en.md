---
prompt_id: go-rust-backend-systems-production-audit
version: 2.0.0
title: Go and Rust Backend and Systems Production Audit
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
# MASTER PROMPT - Deep Production Audit, Repair, Hardening, Release Verification, And Recovery Of Go And Rust Systems

Use this prompt to audit, safely repair, harden, test, build, package, deploy, roll back, and recover a real Go and/or Rust backend, service, worker, CLI, daemon, proxy, data-plane component, control-plane component, library, embedded system, WebAssembly module, or mixed-language system.

Audit the complete path from repository and resolved toolchain to generated code, build tags or Cargo features, linked native libraries, immutable artifacts, deployment revision, running process, data stores, network peers, telemetry, incident controls, and proven recovery. Compilation, Safe Rust, absence of panic, a green race run, or a successful health check is never sufficient by itself.

## 0. How To Use This Prompt

### 0.1 Required Inputs

| Field | Value |
| --- | --- |
| Repository, archive, modules, workspaces, and relevant paths | `[PATHS / URLS]` |
| Business purpose, critical flows, and invariants | `[FLOWS / INVARIANTS]` |
| Technology path and executable artifacts | `[GO / RUST / MIXED / BINARIES]` |
| Targets, architectures, libc, and operating systems | `[TARGET MATRIX]` |
| Protocols, clients, peers, and compatibility promises | `[HTTP / GRPC / TCP / UDP / QUIC / OTHER]` |
| Data stores, queues, caches, files, and schemas | `[SYSTEMS / OWNERS]` |
| Identity, tenant, authorization, and privileged operations | `[MODEL / POLICIES]` |
| Traffic, concurrency, latency, capacity, and SLO targets | `[LOAD / BUDGETS]` |
| Build tags, Cargo features, profiles, and release variants | `[MATRIX]` |
| FFI, cgo, native libraries, kernels, devices, or WASM hosts | `[BOUNDARIES]` |
| Deployment, artifact registry, signing, and rollout | `[PLATFORMS / CHANNELS]` |
| Production access, change authorization, and work mode | `[ACCESS / APPROVERS / MODE]` |

### 0.2 Missing Information And Evidence Ceiling

1. Continue with safe discovery when inputs are incomplete; do not block the entire audit.
2. Infer only from repository state, lock files, resolved graphs, generated output, build metadata, artifacts, runtime evidence, telemetry, database constraints, and authoritative documentation.
3. Mark every unresolved material claim as `UNVERIFIED` and state the exact access, workload, target, fixture, credential, approval, or environment needed to resolve it.
4. Do not issue an unconditional production-ready verdict when release, target, dependency, data, failure, deployment, or recovery evidence is unavailable.

## 1. Current Research Baseline - Re-Check Before Every Audit

This baseline is a starting point, not a substitute for verification at execution time. Re-check current first-party sources and the actual project before recommending or changing anything.

| Component | Confirmed status on 5 August 2026 | Mandatory audit-time verification |
| --- | --- | --- |
| Go stable | Current stable line is Go 1.26.5 (released 7 July 2026; security/bugfix patch of the 1.26 line). | `go version`, `go` directive, `toolchain` directive, `GOTOOLCHAIN`, production image. |
| Go 1.27 | Not yet released; documentation is draft, expected during August 2026. | Do not treat draft as a production baseline without explicit approval. |
| Go support | No classic LTS. Each major line is supported until two newer majors ship; currently supported are Go 1.26 and Go 1.25 (e.g. 1.25.12 on the same July patch wave). | Actual support status, EOL, and upgrade plan. |
| Go compatibility | Strong compatibility promise, but behavioral changes may ship with the `go` directive and `GODEBUG`. | Toolchain, module `go` version, `GODEBUG` overrides, and release notes. |
| Go production tools | Race detector, built-in fuzzing, and `govulncheck` (vulnerabilities + reachability/call graph; limits: reflect/unsafe can cause false negatives; binary mode is less precise). | `go test -race`, fuzz targets, pinned `govulncheck`, CI matrix. |
| Rust stable | Rust 1.97.1 released 16 July 2026 (1.97.0: 9 July 2026). The point release fixes an LLVM miscompilation; 1.97.0 is not an equivalent production baseline. | `rustc -Vv`, `rust-toolchain.toml`, CI pin, image/digest. |
| Rust support | Six-week release train; only the latest stable is officially supported; previous stable enters EOL when the new one ships. | Explicit MSRV and CI on both MSRV and latest stable. |
| Rust edition | Edition 2024 is the current line; it defaults to Cargo resolver 3, which considers `rust-version` when selecting dependency versions. | `edition`, `rust-version`, resolver, lockfile, dependency MSRV. |
| Rust build | `cargo check` is not full build verification; official Rust policy treats `cargo build` as authoritative for all compilation errors. | Release/workspace build, feature matrix, `--locked`. |
| Rust lint/unsafe | Clippy is standard; do not enable pedantic/nursery/restriction groups blindly. Unsafe requires hand-checked safety invariants; Miri is an extra UB check, not a formal proof of full soundness. | Clippy policy, unsafe inventory, Miri/sanitizer limits. |

Note: at real audit time always use the current release/support record, not a hard-coded version from this baseline.

## Role And Mission

### Role

Act as a combination of: Principal Go Engineer; Principal Rust Engineer; backend and distributed-systems architect; systems-programming and runtime specialist; concurrency and asynchronous-systems specialist; database and transaction engineer; network-protocol and API specialist; memory-safety and unsafe-code auditor; application security reviewer; software-supply-chain auditor; performance and profiling engineer; SRE and observability engineer; test architect; CI/CD, container and production-deployment architect; incident-prevention, rollback and disaster-recovery engineer.

### Mission

Your task is not a shallow code review, a generic recommendation list, or an automatic refactor driven by personal taste.

Your task is to:

1. establish the project's real state and protect existing code, data, and uncommitted work;
2. determine whether the project is Go, Rust, or a mixed system;
3. map modules, workspaces, packages, crates, executable artifacts, and deployment units;
4. verify actual toolchain, language, dependency, and runtime versions;
5. verify lifecycle, security support, breaking changes, and platform compatibility;
6. run available build, test, lint, race, fuzz, vulnerability, documentation, and runtime checks;
7. reconstruct critical business, network, concurrency, and data flows;
8. separate proven problems from suspicion, theoretical risk, and unverified areas;
9. find root causes, not just symptoms;
10. implement the smallest safe fix when the work mode allows;
11. add regression, concurrency, integration, security, and recovery tests;
12. verify goroutine/task lifecycle, cancellation, timeout, backpressure, and resource ownership;
13. verify memory safety, unsafe, FFI, and native boundaries when present;
14. verify database, transactions, locking, idempotency, and distributed consistency;
15. verify security trust boundaries, secrets, TLS, input, and supply chain;
16. verify performance based on measurement; observability, shutdown, deployment, rollback, and recovery;
17. document every command actually executed and its result;
18. produce a P0–P3 finding register, implementation roadmap, and Definition of Done.

The end goal is a demonstrably reliable, secure, maintainable, and operationally ready system.

Code that compiles is not automatically correct. Rust without an explicit `unsafe` block is not automatically free of logic, concurrency, or resource-lifecycle bugs. Go without panics is not automatically free of races, goroutine leaks, or uncontrolled resource use.

## Technology Path Selection

At the start, determine one of:

| Path | When |
| --- | --- |
| `GO` | Only Go modules/packages/executables. |
| `RUST` | Only Rust crates/workspaces/executables. |
| `MIXED_GO_RUST` | Both languages in the same system. |
| `UNKNOWN` | Insufficient evidence; inventory first, do not guess. |

For `MIXED_GO_RUST`:

- shared system analysis;
- full Go path for Go modules;
- full Rust path for Rust crates/workspaces;
- dedicated analysis of FFI, IPC, network, and data boundaries between them.

Do not apply Go recommendations to the Rust side or Rust recommendations to the Go side without a clear technology boundary.

## Project Context

| Field | Value |
| --- | --- |
| Service | `[NAME]` |
| Purpose | `[DESCRIPTION]` |
| Clients | `[WEB / MOBILE / CLI / PARTNERS / INTERNAL / PUBLIC]` |
| Architecture | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / SYSTEMS / OTHER]` |
| Technology | `[GO / RUST / MIXED_GO_RUST]` |
| Go module/workspace | `[GO_MODULE]` |
| Rust workspace/crate | `[RUST_WORKSPACE]` |
| Target platforms | `[LINUX / WINDOWS / MACOS / EMBEDDED / WASM / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / VM / BARE METAL / SERVERLESS / OTHER]` |
| Data | `[POSTGRESQL / MYSQL / SQLITE / REDIS / OTHER]` |
| Messaging/cache | `[MESSAGING / CACHE]` |
| Protocols | `[HTTP / gRPC / QUIC / TCP / UDP / OTHER]` |
| FFI/native | `[FFI / CGO / BINDGEN / NONE]` |
| Workload | `[WORKLOAD]` |
| CI/CD | `[CI_CD]` |
| Baseline/compatibility | `[REQUIRED_BASELINE / COMPATIBILITY]` |
| Work mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AND_CONCURRENCY_AUDIT / PERFORMANCE_AUDIT]` |
| Regulatory and extra constraints | `[REGULATORY / CONSTRAINTS]` |
| Repo / expected / known problems | `[REPOSITORY / EXPECTED_BEHAVIOR / KNOWN_PROBLEMS]` |

Code, lock files, toolchain files, executed commands, deployed artifact behavior, and database constraints are evidence. Documentation is context only.

When an input is absent, try to establish it from the project; otherwise mark `UNVERIFIED`. Do not assume a web service merely because `main` exists, a microservice merely because Go is used, a systems component merely because Rust is used, Tokio merely because async Rust exists, or PostgreSQL merely because a particular ORM is present.

## Work Modes

Use `AUDIT_AND_SAFE_FIX` unless a mode is explicitly supplied.

| Mode | Allowed work |
| --- | --- |
| `AUDIT_ONLY` | Analyze and run safe checks; do not change source, dependencies, lock files, database, or infrastructure; deliver a precise plan. |
| `AUDIT_AND_SAFE_FIX` | Implement confirmed local low-risk repairs and regression tests; plan destructive, contract-breaking, or architecturally large changes. |
| `FULL_IMPLEMENTATION` | Implement justified repairs in small verifiable steps; do not run destructive migrations without backup/rollback strategy. |
| `FIX_CONFIRMED_ISSUES` | Fix only previously confirmed issues; do not widen scope without evidence. |
| `SECURITY_AND_CONCURRENCY_AUDIT` | Focus: race, deadlock, goroutine/task leak, cancellation, unsafe/FFI, input/network security, dependency risk, secrets, idempotency, resource exhaustion. |
| `PERFORMANCE_AUDIT` | Focus: real workload, CPU, memory, allocations, GC, scheduler, contention, I/O, queries, latency percentiles, benchmark and profiler evidence. |

## Operating Contract

1. Start with inventory and baseline. Do not broad-refactor before recording actual failures, constraints, and support status.
2. Every finding must include flow/endpoint/job, file/symbol, input or scenario, root cause, impact, evidence/reproduction, repair, and verification.
3. State a falsifiable local hypothesis, make the smallest defensible change, and run the narrowest check that could disprove it.
4. Never claim that build, test, race, Miri, fuzz, migration, authorization, timeout, rollback, health, or shutdown succeeds unless actually executed.
5. Retain public contracts, protocols, and compatibility unless a documented security or data-integrity repair requires a breaking change.
6. Never weaken authentication, authorization, TLS, validation, database constraints, secret handling, rate limits, tests, or auditability merely to pass a check. Never disclose secrets, tokens, private keys, connection strings, credentials, or sensitive payloads.
7. Consult current first-party documentation whenever language/runtime lifecycle or behavior affects a decision. Record title, URL, version/status, access date, and decision informed.
8. Evidence status: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, or `REJECTED`.
9. For every command record: exact command, directory, toolchain, target, feature/tag, environment when material, exit code, real result, material warnings, and check limits. If not run: `UNVERIFIED - command not run because [reason]`.
10. Do not invent common problems (goroutine leak, data race, unsound unsafe, N+1, SQL injection, memory leak, etc.) until you find relevant evidence. Risk: `RISK FOR FURTHER CHECK - not confirmed`.
11. Inspect Git status before modifying anything; do not reset, stash, or overwrite another person's uncommitted changes. Do not run tests against production databases or execute destructive migrations.
12. Do not change the toolchain before recording the initial state.

## Mandatory Finding Register

```text
ID:
Title:
Severity: P0 / P1 / P2 / P3
Evidence status: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Language and module/crate:
Affected files:
Affected flow:
Environment/target/features:
Evidence:
Command/test/race/Miri/profiler:
Reproduction:
Root cause:
User/business impact:
Security/data/operational impact:
Likelihood:
Proposed fix:
Implemented fix:
Regression test:
Compatibility:
Deployment note:
Rollback/recovery:
Residual risk:
```

Group manifestations of the same root cause into one finding. Separate risks for further check from confirmed problems.

## Evidence, Truth, And Source-To-Runtime Identity

### Evidence Levels

| Level | Meaning | Examples |
| --- | --- | --- |
| `E0` | Claim only; no inspectable evidence. | README, ticket, verbal expectation. |
| `E1` | Static repository or configuration evidence. | Source, manifest, module file, lock file. |
| `E2` | Resolved build or generated-output evidence. | Dependency graph, generated code, linker map, build metadata. |
| `E3` | Executed test, analyzer, benchmark, or controlled reproduction. | Exit code, logs, race report, Miri finding, packet trace. |
| `E4` | Release-like artifact and target-environment evidence. | Binary hash, signature, container digest, target smoke, load or failover run. |
| `E5` | Observed production behavior or proven recovery. | Telemetry tied to revision, canary result, restore drill, incident evidence. |

- Use the strongest available evidence but never promote a conclusion above the evidence actually obtained.
- Record command, working directory, environment, toolchain, target, tags or features, fixtures, exit code, duration, and material output for every executed check.
- Separate `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE`, and `REJECTED`; do not use vague green, looks fine, probably, or safe wording.

### Source-To-Runtime Identity Chain

- Record repository URL, commit, branch or tag, dirty state, submodules, vendored code, generated code, patches, and untracked inputs.
- Resolve the exact Go and Rust toolchains selected locally, in CI, in builders, in containers, and in release automation; record automatic toolchain download or override behavior.
- Capture module/workspace graphs, checksums, lock files, replacement or patch directives, build scripts, code generators, proc macros, C toolchains, system libraries, and linker inputs.
- Record build tags, environment variables, `GOOS`, `GOARCH`, `CGO_ENABLED`, target triples, Cargo features, profiles, `RUSTFLAGS`, linker flags, LTO, panic strategy, and reproducibility controls.
- Hash and identify binaries, libraries, debug symbols, source maps, SBOMs, signatures, provenance, container images, package manifests, and deployment revisions.
- Verify runtime version, build commit, feature or tag set, configuration source, loaded shared libraries, kernel and libc assumptions, architecture, endpoint peers, and schema compatibility.
- Reconcile source, artifact, registry, deployment, process, telemetry, database migration, and recovery identities before a release verdict.
- Detect mutable tags, rebuilds under the same version, stale generated code, wrong symbols, wrong image, wrong config, partial rollout, mixed schema, and old/new binary coexistence.

### Finding Quality Contract

| Required field | Requirement |
| --- | --- |
| Identity | Stable finding ID, language, subsystem, owner, and affected artifact or deployment. |
| Evidence | File and symbol, command, target, tags/features, data or traffic preconditions, artifact ID, and E0-E5 level. |
| Cause | Root cause and violated invariant, not only symptom or scanner text. |
| Impact | Correctness, security, availability, data, latency, cost, compatibility, and recovery consequences. |
| Repair | Smallest safe repair, alternatives, rejected shortcuts, owner, migration, and rollout constraints. |
| Verification | Regression, negative, race or memory check, target matrix, load/failure scenario, rollout gate, and rollback trigger. |

## Phase A - Protect The Workspace

Before changes:

- repo root, branch, status, uncommitted changes, commit SHA, submodules;
- Go module/workspace files (`go.mod`, `go.sum`, `go.work`);
- Rust workspace/crate files (`Cargo.toml`, `Cargo.lock`, `rust-toolchain.toml`);
- generated code, native libraries, vendored source;
- secrets only by path and type (no contents);
- test configuration; prevent connections to production systems;
- target OS and architecture.

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
go version
go env
rustc -Vv
cargo -Vv
rustup show
rustup show active-toolchain
```

## Phase B - Shared Inventory

Map: executables, libraries, modules/crates, public APIs, generated code, build scripts, CLIs, servers, workers, schedulers, consumers, migrations, protocols, database layer, cache, messaging, FFI, filesystem, deployment/ops, test fixtures, benchmarks, fuzz targets, CI, containers, IaC.

Graph: `repo → module/workspace → package/crate → executable → deployment unit`.

Flag: cyclic dependencies; oversized shared/common; domain depending on infrastructure; duplicated models; multiple implementations of the same business rule; deployment unit sharing a database without clear ownership; hand-edited generated code; stale executables still building; feature/build-tag combinations CI does not exercise.

## Phase C - Baseline Without Code Changes

First determine the real build system, toolchain, targets, features, and build tags. Do not randomly run every possible command.

For every command record: toolchain, target, architecture, OS, feature/build tag, debug/release, CGO/native state, environment override, exit code, test count, duration, material output.

## Phase D - GO PATH: Toolchain, Modules, And Build

Run for every Go module.

### Toolchain

Check: `go version`, GOROOT/GOPATH, GOMOD/GOWORK, GOTOOLCHAIN, GOOS/GOARCH, CGO_ENABLED, GOEXPERIMENT, GODEBUG, GOPROXY/GOSUMDB/GOPRIVATE/GONOSUMDB, build cache. Do not disclose credentials from proxy/VCS configuration.

### go.mod and workspace

Check: module path, `go` directive, `toolchain` directive, require/indirect, replace/exclude/retract, local paths, pseudo/prerelease versions, major `/vN` path, private modules, dependencies that require a newer Go.

Especially: replace to a local dir that will not exist in CI; undocumented forks; replace hiding a security update; different versions of the same module across workspace members.

If `go.work` exists: use entries, local modules, whether CI uses the workspace, difference with `GOWORK=off`, whether the workspace hides a missing published dependency.

### Verification

```text
go env
go list -m -json all
go mod graph
go mod verify
go mod tidy -diff
```

Do not run mutating `go mod tidy` before reviewing `-diff`. If vendored: check `go mod verify` and `-mod=vendor`; do not regenerate vendor without reviewing the diff.

### Build baseline

```text
go build ./...
go test ./...
go vet ./...
go build -trimpath -o ./dist/app ./cmd/app
```

Adapt package, output, build tags, CGO, target OS/arch, linker flags, version metadata. Do not claim the production build works merely because `go test ./...` passes.

## Phase E - GO PATH: Structure, Idioms, Concurrency

### Packages and errors

Check: package cohesion, `internal`, public API, import direction, global state, `init`, side-effect imports, interface ownership. Interfaces usually belong on the consumer side when that matches real architecture; do not introduce interfaces only for mocking.

Errors: ignored error, wrapping with `%w`, `errors.Is`/`As`, sentinel/typed error, string comparison, log-and-return same error, leaking internals, overly broad panic, recover hiding corruption. Do not use panic as normal business control flow. Do not add recover on every layer.

Nil: nil interface with non-nil dynamic type, nil map/slice/channel, typed nil error, nil receiver.

Slice/map: backing-array aliasing, retaining large backing arrays, concurrent map access, append invalidation, map iteration nondeterminism, defensive copy, pool reuse exposing stale data.

### Goroutine, channel, context

Check:

- who starts the goroutine, who owns its lifecycle, how it ends;
- `context.Context` propagation, timeout/deadline/cancel, derived contexts;
- channels: buffered/unbuffered, close ownership, send on closed channel, nil channel deadlock, unbounded growth;
- `errgroup`, worker pool, semaphore, bounded concurrency;
- select with default that swallows backpressure;
- leaks: goroutine waiting on channel/mutex/IO that never completes;
- panic in a non-main goroutine.

Use `go test -race` where applicable. The race detector is not a substitute for design review, but it confirms real data races.

Do not add a goroutine merely so a function looks non-blocking. Do not use unbounded channels without memory analysis. Do not share a map without synchronization.

## Phase F - GO PATH: HTTP/RPC, DB, Unsafe/CGO, Tests

### Networking

Check: server timeouts (Read/Write/Idle/Header), body limits, context cancel on disconnect, middleware order, TLS, HTTP/2, gRPC interceptors/deadlines/message size, client timeout and connection pool, redirect policy, SSRF on user-supplied URLs.

### database/sql and persistence

Check: driver, pool (`SetMaxOpenConns`/`MaxIdleConns`/`ConnMaxLifetime`), context on queries, prepared statements, transactions (begin/commit/rollback/defer), isolation, locking, N+1, pagination, migrations, null handling, money/time types. Do not treat in-memory/sqlite-in-memory as proof of production relational correctness if production uses another engine.

### unsafe and cgo

Inventory `unsafe`, cgo, pointer casting, Go pointers into C, finalizers, memory ownership across FFI. Document invariants. CGO changes deployment (glibc/musl, cross-compile, image).

### Testing

```text
go test ./...
go test -race ./...
go test -fuzz=Fuzz -fuzztime=30s ./...
govulncheck ./...
```

Check table-driven tests, integration with real dependencies where possible, fuzz targets, benchmarks with realistic data, build tags for integration. Fuzz and race are part of the production toolchain, not optional luxury when concurrent or parser code exists.

## Advanced Go Production Verification

### Go Toolchain Selection And Compatibility

- Record `go version`, `go env`, module `go` directives, `toolchain` directives, workspace settings, `GOTOOLCHAIN`, builder images, and downloaded toolchains; distinguish language baseline from the compiler that actually built the artifact.
- Verify behavior changes controlled by the module `go` version, release notes, `GODEBUG`, experiments, architecture, cgo, linker mode, and standard-library changes.
- Build every release command and package under the intended supported toolchain and at least the oldest promised compatibility baseline when that promise exists.
- Do not infer artifact identity from a `go` directive alone; prove compiler, module graph, tags, environment, linker inputs, and embedded build information.

### Module, Workspace, Vendor, And Generator Trust

- Review all `go.mod`, `go.sum`, `go.work`, `replace`, `exclude`, `retract`, private proxy, checksum database, vendor, local path, fork, and generated-source decisions.
- Verify that CI and release do not accidentally consume a developer workspace, unreviewed local replacement, mutable branch, unavailable private module, or stale vendor tree.
- Audit `go generate`, code generation, schema generation, mocks, stringers, protobuf, OpenAPI, SQL generators, and embedded assets as executable supply-chain inputs.
- Run vulnerability analysis against the resolved graph and reachable code where possible, then document blind spots involving reflection, plugins, dynamic loading, cgo, build tags, and binary-only evidence.

### Build Tags, Targets, And Artifact Matrix

- Inventory platform suffixes, `//go:build` expressions, generated tag combinations, race and non-race builds, cgo and pure-Go variants, FIPS or boringcrypto variants where applicable, and optional integrations.
- Create a support matrix: command or library, `GOOS`, `GOARCH`, tags, cgo, libc, kernel, external libraries, release profile, tests, artifact, and owner.
- Compile and test the supported matrix or explicitly justify representative coverage; do not let uncompiled files or inactive tags escape review.
- Inspect build IDs, VCS metadata, symbol policy, stripping, static or dynamic linkage, reproducibility, binary size, executable permissions, and runtime library search paths.

### Goroutine, Channel, Context, And Scheduler Correctness

- For every goroutine, identify creator, purpose, cancellation source, terminal condition, wait or join path, panic policy, boundedness, metrics, and shutdown deadline.
- For every channel, document ownership, close authority, buffering rationale, maximum retained memory, send/receive blocking behavior, select fairness assumptions, and slow-consumer policy.
- Verify context propagation through HTTP, RPC, database, queue, filesystem, subprocess, and internal calls; distinguish cancellation, deadline, client disconnect, overload rejection, and shutdown.
- Test races, deadlocks, goroutine leaks, timer and ticker leaks, blocked sends, close/send races, WaitGroup misuse, copylock, atomic alignment, map access, pool misuse, and concurrent lifecycle transitions.
- Treat a clean race-detector run as evidence only for the exercised paths, architecture, timing, tags, and workload; add stress, repetition, scheduling variation, and targeted invariants.

### Go Memory, Resource, And Runtime Behavior

- Inspect allocation rate, retained heap, object lifetime, escape behavior, stack growth, GC pacing, finalizer dependence, large buffers, pooling, fragmentation, and memory limits under realistic load.
- Prove closure of response bodies, rows, files, pipes, sockets, subprocesses, compression streams, temporary files, transactions, and other resources on success, error, cancellation, panic, and shutdown paths.
- Review `sync.Pool`, `unsafe`, `reflect`, zero-copy conversion, slices sharing backing arrays, aliasing, byte/string lifetime, mmap, and object reuse for confidentiality and correctness.
- Use profiles, traces, metrics, and benchmarks to distinguish CPU, scheduler, lock, GC, allocation, syscall, network, database, and downstream bottlenecks.

## Phase G - RUST PATH: Toolchain, Cargo, And Workspace

### Toolchain

```text
rustc -Vv
cargo -Vv
rustup show
```

Check: active toolchain, host triple, targets/components, `rust-toolchain`/`rust-toolchain.toml`, channel, pinned version, profile, nightly date, RUSTFLAGS, linker, target config.

Stable vs nightly: whether production uses stable; why nightly exists; which feature flags require it; whether nightly is date-pinned; whether CI tests stable. Do not use floating nightly for a reproducible production build.

### Edition and MSRV

Check: `edition`, `rust-version`, workspace-level values, resolver (Edition 2024 → resolver 3), CI on MSRV, dependencies that raised MSRV, edition migration warnings.

`edition` and `rust-version` are not the same. The newest edition does not automatically mean the newest compiler, but features and dependencies may require it.

### Workspace and lockfile

Map members, default/excluded, virtual workspace, shared deps, profiles, `[patch]`/`[replace]`, features, bin/lib/proc-macro/build/dev deps.

```text
cargo metadata --format-version 1
cargo tree
cargo tree -d
cargo tree -e features
```

Check duplicate major versions, duplicate native libraries, feature unification, different TLS backends, multiple async runtime versions. Do not remove duplicates merely because they appear in the tree.

Lockfile: whether it exists and should be committed (yes for executables/services); yanked; git dependencies; checksums; `--locked`/`--frozen`; offline build.

## Phase H - RUST PATH: Build, Lint, Ownership, Errors

### Baseline

```text
cargo fmt --all -- --check
cargo check --workspace --all-targets
cargo build --workspace --all-targets --locked
cargo build --release --workspace --locked
cargo clippy --workspace --all-targets --locked -- -D warnings
cargo doc --workspace --no-deps --locked
cargo test --doc --workspace --locked
cargo test --workspace --locked
```

`cargo check` is a fast check, **not** a substitute for `cargo build`. Do not enable `--all-features` blindly if features are mutually exclusive; build a feature matrix. Do not enable full pedantic/nursery/restriction groups blindly.

### Ownership and types

Check: unnecessary clone, oversized lifetimes, cyclic Rc/Arc, Weak, borrows across async boundaries, self-referential structures, Pin.

Send/Sync: whether a type may truly cross thread boundaries; `unsafe impl Send/Sync` without a formal invariant is a P0/P1 candidate.

Interior mutability: `Cell`/`RefCell`/`Mutex`/`RwLock`/`Atomic*`; lock scope; poison; deadlock; async + `std::sync::Mutex` on executor threads.

### Error handling

Check: `Result` vs panic, `unwrap`/`expect` on production paths, `?` and error context (`thiserror`/`anyhow` where present), discarded `Result`, partial cleanup, `catch_unwind` as a universal solution. Do not add panic/unwrap as a quick fix.

## Phase I - RUST PATH: Unsafe, FFI, Async

### Unsafe inventory

Find: `unsafe` block/fn/trait/impl, raw pointers, transmute, MaybeUninit, ManuallyDrop, unions, unchecked indexing/UTF-8, custom allocators, FFI, SIMD, inline asm, `static mut`.

Table: `Location | Unsafe operation | Safety invariant | Who upholds it | Test/check | Risk`.

For public `unsafe fn` require `# Safety` documentation: preconditions, lifetime, alignment, aliasing, initialization, ownership, thread safety, drop, FFI/ABI. A `// SAFETY:` comment must explain a concrete invariant, not merely say “this is safe”.

### FFI

Check: ABI, `repr(C)`, layout/alignment, string encoding, null, ownership/allocator pairing, callbacks, unwinding across FFI, bindgen, build.rs, platform target. Do not allow unwind across FFI unless explicitly supported.

### Miri and sanitizers

When supported:

```text
cargo +nightly miri test
```

Pin nightly. Miri is not proof of absence of all UB, especially on unexecuted paths, platform code, and unsupported FFI. Document Address/Leak/Memory/ThreadSanitizer requirements and limits.

### Async runtime and task lifecycle

First determine the runtime (Tokio, async-std, smol, Embassy, custom, multiple runtimes, or none). Do not apply Tokio rules to another runtime without checking.

Check: multi-thread/current-thread, worker threads, blocking pool, task spawn ownership, cancellation/`Drop` of futures, `JoinHandle` await, `select!` cancel safety, bounded channels/backpressure, `spawn_blocking` for blocking work, timeout, graceful shutdown. Uncontrolled `tokio::spawn` without supervision risks leaks and orphan tasks.

## Phase J - RUST PATH: Web, DB, Supply Chain

### Web/RPC/serialization

Check framework (axum/actix/warp/tonic/...), extractor validation, body limits, timeout, auth middleware, CORS, error responses without leaking internals, serde deny-unknown where needed, schema evolution, gRPC message limits.

### Database

Check driver/pool (sqlx/diesel/sea-orm/...), compile-time SQL where used, migrations, transactions, isolation, connection checkout timeout, cancel, N+1, type mapping (time/money/uuid).

### Cargo supply chain

Check: registry sources, git/path dependencies, `[patch]`, yanked crates, typosquat risk, features that pull heavy native code, `cargo audit`/`cargo deny` where present, SBOM, pinned tool versions in CI. Do not use floating `cargo install ...` latest in reproducible CI.

## Advanced Rust Production Verification

### Toolchain, Edition, MSRV, Resolver, And Profiles

- Record `rustc -Vv`, Cargo version, channel, target components, `rust-toolchain.toml`, `rust-version`, edition, resolver, profile settings, linker, standard library source, and CI/container pins.
- Test the declared MSRV and current supported stable separately; ensure dependency resolution, proc macros, build scripts, generated code, docs, examples, and tests respect the promise.
- Verify Edition 2024 migration assumptions, resolver behavior, dependency `rust-version` handling, lint changes, unsafe changes, and macro compatibility instead of changing edition mechanically.
- Review release, test, bench, dev, and custom profiles including optimization, debug info, overflow checks, panic strategy, codegen units, LTO, stripping, incremental state, and reproducibility.
- Do not treat `cargo check` as release verification; execute the authoritative build and tests for the real targets, features, profiles, and native dependencies.

### Cargo Graph, Features, Build Scripts, And Proc Macros

- Inventory workspace members, excluded crates, default members, virtual manifests, examples, benches, binaries, tests, build dependencies, dev dependencies, target-specific dependencies, and unpublished internal crates.
- Review `Cargo.lock`, registry and git sources, `[patch]`, `[replace]`, local paths, source replacement, sparse registry, vendoring, yanked versions, licenses, duplicate versions, and dependency ownership.
- Model additive, mutually exclusive, default, optional, target, backend, TLS, database, allocator, SIMD, FIPS, tracing, and test-only features; detect combinations that compile but violate invariants.
- Compile the supported feature matrix using a justified combinatorial strategy; include no-default, all-features only when meaningful, representative pairwise combinations, and production presets.
- Audit `build.rs`, proc macros, code generation, environment reads, filesystem and network access, native compilation, bindgen inputs, linker directives, rerun conditions, generated metadata, and cache behavior as executable supply-chain code.

### Ownership, Interior Mutability, And Drop Semantics

- Trace ownership of requests, buffers, credentials, transactions, tasks, connections, file descriptors, memory mappings, locks, callbacks, and foreign resources across success and failure paths.
- Review `Arc`, `Rc`, `Weak`, `Mutex`, `RwLock`, atomics, `Cell`, `RefCell`, `OnceLock`, lazy initialization, pinning, self-references, cycles, guard lifetimes, and lock order.
- Verify `Drop` behavior under normal return, error propagation, panic, abort, cancellation, process termination, partial initialization, and foreign callbacks; never rely on destructors for must-happen distributed effects.
- Inspect cloning and copying for hidden cost, stale state, duplicated authority, secret retention, non-idempotent handles, and divergence between logical and physical ownership.

### Unsafe Code, Memory Model, FFI, And Soundness

- Inventory every `unsafe` block, unsafe function or trait, unsafe impl, raw pointer, union, `MaybeUninit`, transmute, unchecked operation, inline assembly, allocator, SIMD intrinsic, FFI declaration, and dependency-provided unsafe boundary.
- For each boundary, document the safety contract: validity, alignment, provenance, initialization, aliasing, lifetime, thread-safety, panic behavior, unwind behavior, ownership transfer, deallocation, and callback constraints.
- Prove that safe callers cannot violate the contract and that public safe APIs remain sound under adversarial valid inputs, reentrancy, concurrency, panic, cancellation, and destruction order.
- Verify ABI, calling convention, integer widths, structure layout, padding, enums, strings, buffers, ownership, allocator pairing, version negotiation, symbol visibility, exceptions, signals, and cross-language unwind policy.
- Use Miri, sanitizers, fuzzing, property tests, Loom or model checking, targeted stress, and code review where applicable; state target, nightly dependence, unsupported operations, false-negative space, and what each tool cannot prove.
- Never infer soundness from the absence of explicit unsafe in first-party code; transitive crates, platform APIs, kernels, allocators, drivers, and foreign libraries remain part of the trusted computing base.

### Async Runtime, Tasks, Cancellation, And Backpressure

- Identify the runtime or executor, feature set, worker and blocking pools, timer source, I/O driver, compatibility layers, runtime ownership, nested runtime risk, and shutdown semantics.
- For every spawned task, identify creator, purpose, cancellation, join or supervision path, panic handling, result ownership, boundedness, tracing context, and shutdown deadline.
- Audit cancellation safety of `select`, timeouts, streams, framed protocols, codecs, database operations, writes, locks, channels, and partial state machines; prove what may be safely retried.
- Detect blocking work on async workers, unbounded spawn, unbounded queues, lock guards held across await, task leaks, detached failures, lost wakeups, starvation, priority inversion, timer storms, and slow-consumer amplification.
- Test overload admission, concurrency limits, queue capacity, deadlines, cancellation storms, downstream stalls, shutdown during in-flight work, and old/new deployment coexistence.

### Rust Error, Panic, And Process-Failure Policy

- Define which failures are validation, domain conflict, not found, unauthorized, dependency, timeout, overload, corruption, programmer bug, invariant violation, or unrecoverable process state.
- Review `Result`, error conversion, context, source chains, stable external error contracts, redaction, retry classification, metrics, and ownership of recovery decisions.
- Inventory `unwrap`, `expect`, indexing, arithmetic overflow assumptions, unreachable paths, process exit, abort, panic hooks, `catch_unwind`, and panic across FFI or task boundaries.
- Do not convert invariant violations into silent continuation; define fail-fast, isolate, restart, degrade, quarantine, or repair behavior using evidence and blast radius.

## Phase K - Shared Functional Correctness And Data

For each critical flow: `entry → authn → authz → validation → use case → transaction → DB/cache/broker/external service → response → telemetry`.

Check illegal state transitions, race scenarios, money/inventory rules, audit trail. Domain rules must not live only in handlers or clients.

Transactions: real boundary (not just a function name), isolation, deadlock retry, partial failure, outbox/inbox, saga/compensation. Idempotency for retryable writes: key, unique constraint, stored outcome, conflict response. Process-local/in-memory idempotency does not protect multi-replica systems.

Migrations: owner, SQL review, lock/duration, rolling compatibility, backup/restore, rollback/forward repair. Do not execute destructive migrations during the audit.

## Phase L - Messaging And Workers

Check: producer/consumer, ack/nack, at-least-once vs exactly-once assumptions, visibility timeout, retry/DLQ, ordering, poison messages, dedup, concurrency limit, deployment overlap, rebalance. Do not acknowledge before durable side effects complete.

## Phase M - Shared Security Analysis

Trust boundaries: public API, internal API, admin, worker, DB, broker, filesystem, cloud metadata, FFI.

AuthN/AuthZ: token/session validation, object-level authorization, tenant isolation, service-to-service auth. Test BOLA/IDOR.

Input: injection (SQL/command/path), SSRF, deserialization bombs, path traversal, zip-slip, XSS if HTML exists, header injection.

Command execution: allowlists, avoid shell where possible, env scrubbing.

Filesystem: root confinement, permissions, symlinks, temp files.

TLS/crypto: chain verification, min version, ciphers, certificate pinning where needed, key storage; never disable TLS verify on production paths.

Secrets: not in source/log/image/artifact; rotation; incident if compromised (without displaying full values).

Debug: pprof, metrics, admin, reflection — not public without protection.

## Shared Protocol, Data, And Distributed-Correctness Audit

### Network Protocol And API Contract Matrix

- Inventory listeners, clients, transports, methods, routes, RPC services, streaming modes, authentication, authorization, tenant ownership, payload limits, deadlines, idempotency, retries, transaction boundary, compatibility, and tests.
- Verify HTTP parsing, request smuggling defenses, proxy trust, forwarded headers, TLS termination, HTTP/2 and HTTP/3 settings, decompression limits, multipart handling, redirects, and connection reuse.
- For gRPC and protobuf, verify field evolution, unknown fields, oneof changes, enum growth, deadlines, status mapping, interceptors, reflection, health, streaming backpressure, and old/new client compatibility.
- For TCP, UDP, QUIC, framed, binary, or custom protocols, verify framing, length validation, incremental parsing, timeouts, peer identity, replay, amplification, fragmentation, state-machine transitions, and fuzz coverage.
- Apply request, response, header, metadata, stream, file, message, and decompressed-size limits before expensive allocation or parsing.

### Transactions, Idempotency, And Schema Evolution

- Map every state-changing flow from validation through authorization, reads, locks, writes, side effects, commit, response, retry, event publication, and reconciliation.
- Verify database constraints, isolation, lock order, optimistic tokens, serialization failures, deadlock retry, connection state, transaction ownership, savepoints, cancellation, and rollback behavior.
- Use idempotency keys with durable ownership, request fingerprinting, result persistence, conflict semantics, expiry, replay response, concurrency control, and multi-replica behavior.
- Audit outbox, inbox, CDC, saga, compensation, deduplication, ordering, partition ownership, poison messages, DLQ replay, and partial failure between database and broker.
- Verify expand-and-contract migrations, old/new binary coexistence, backfill idempotency, online index or constraint behavior, lock duration, cutover, rollback limits, forward repair, and restore compatibility.

### Cache, Queue, And Coordination Correctness

- Document cache key namespace, tenant scope, authorization sensitivity, serialization version, TTL, invalidation, stampede protection, negative caching, stale policy, eviction, and outage behavior.
- Treat distributed locks and leases as fallible coordination; verify fencing tokens, clock assumptions, renewal, ownership loss, split brain, stale holder behavior, and recovery.
- For queues and streams, verify delivery semantics, ack timing, visibility timeout, rebalance, ordering, batch partial failure, retry budget, poison handling, retention, replay, and consumer idempotency.
- Test broker outage, cache outage, delayed or duplicated messages, reordered events, consumer restart, partition movement, lease loss, and database/broker recovery skew.

### Overload, Retry, Deadline, And Partial-Failure Control

- Derive concurrency, queue, pool, and rate limits from downstream capacity, latency budgets, memory, CPU, file descriptors, database limits, and recovery objectives.
- Propagate deadlines end to end and reserve time for cleanup, transaction completion, response serialization, retries, and fallback; avoid independent timeout inflation at each hop.
- Classify operations by idempotency and retryability; cap attempts and elapsed time, use jitter, honor server signals, prevent retry multiplication, and expose retry budget metrics.
- Verify admission control, load shedding, circuit behavior, bulkheads, bounded queues, fair scheduling, tenant isolation, hot-key handling, fan-out limits, and degradation modes.
- Run burst, sustained load, soak, dependency slowdown, dependency outage, connection churn, cancellation storm, retry storm, and recovery tests with explicit pass/fail thresholds.

## Phase N - Resilience, Performance, Observability

Timeout/retry/jitter/cancellation consistent across inbound, DB, HTTP, and jobs. Do not retry non-idempotent writes. Bound concurrency to dependency capacity.

Performance: measurement (p95/p99, CPU, memory, alloc, GC for Go, scheduler, lock contention, I/O, queries). Benchmark and profiler evidence. Do not optimize without a profiler. A microbenchmark is not end-to-end proof.

Observability: structured logs, correlation/trace ID, metrics cardinality, tracing, separated health/readiness/liveness, dashboard, alert, runbook. Do not log secrets/PII.

## Phase O - Container, Shutdown, Deployment, CI/CD

Artifact: reproducible build, pinned base image/digest, non-root, minimal OS, CA/certs, timezone, signal handling, no secrets in layers, SBOM, scan.

Graceful shutdown: stop accepting work, drain, cancel tasks/goroutines with context, flush logs/telemetry, close pools/conns, finish within platform deadline. Test during long requests, jobs, and migrations.

Deployment: immutable artifact, migration order, rolling/canary, abort criteria, application vs database rollback (explicit), recovery, post-deploy verification.

CI/CD: pinned toolchain (Go/Rust), matrix (OS/arch/features/MSRV), race/fuzz/audit where relevant, locked build, no `go install @latest` / floating nightly, artifact promotion, secret hygiene.

## Phase P - Test Strategy And Fixes

Inventory: unit, integration, race, fuzz, Miri/sanitizer, contract, security, concurrency, migration, E2E, load, recovery, publish smoke.

Every P0–P2 fix requires a test that demonstrates the old incorrect and new correct behavior.

Before changing: finding, hypothesis, minimal change, preserved contract, risk, test that could disprove, rollback. Change the smallest file set. Do not modify `go.mod`/`go.sum`/`Cargo.lock` without review.

## Phase Q - Production Readiness And Report Quality

Fill the checklist with evidence. Before delivery: confirmed findings are reproducible; severity matches impact; unexecuted checks are marked; command log is complete; secrets are redacted; residual risk is explicit.

## Severity

| Priority | Definition |
| --- | --- |
| P0 | Unauthorized/cross-tenant access, RCE/injection, confirmed data race in a critical flow, unsound unsafe/FFI with real UB risk, exposed production secret, irreversible data loss/corruption, destructive deployment, untested recovery of critical data. |
| P1 | Authz bypass in a critical flow, goroutine/task leak under load, broken cancellation/timeout, broken idempotency/transaction, unbounded resources, unsafe deserialization, supply-chain issue with reachability, interruption of a critical operation during deploy. |
| P2 | Localized API issue, slow query, weak observability, inconsistent error contract, avoidable availability risk, technical debt with a concrete consequence. |
| P3 | Cleanup, documentation, naming, consistency, small measured improvement. |

## 1. Inventory, Toolchain, And Reproducible Baseline

Map path (GO/RUST/MIXED), modules/workspaces/crates, toolchain pins, lock files, feature/build-tag matrices, executables, and deployment units.

Table: `Component | Project version | Resolved | Current stable | Support/EOL | Compatibility | Action`.

For Go: `go`/`toolchain` directive, actual `go version`, stdlib, GOTOOLCHAIN, modules, framework, driver, build tools, base image.

For Rust: rustc, Cargo, channel, rust-toolchain, rust-version, edition, resolver, lockfile, async runtime, framework, DB/TLS/serde crates, test/build tools, base image.

Run deterministic build/test/lint/race/audit baseline and record the first failure.

## 2. Concurrency And Lifecycle

Go: goroutine ownership, context, channel close, race detector, bounded work.

Rust: task ownership, cancel safety, Send/Sync, async runtime limits, no unbounded spawn.

Shared: backpressure, shutdown, timeout, resource ownership, lock scope, deadlock risks with evidence.

## 3. Memory, Unsafe, And FFI

Go: escape-analysis suspicions only with measurement; cgo/unsafe inventory; finalizers; pointer lifetime.

Rust: ownership correctness, unsafe inventory with safety invariants, Miri/sanitizer limits, FFI ABI/ownership.

## 4. API, Networking, And Validation

Validate all inputs. HTTP/RPC semantics, limits, timeout, TLS. AuthN/AuthZ and object ownership. Do not expose stack/internal details.

## 5. Data, Transactions, Migrations

Constraints in the database where possible. Pool, timeout, transactions, locking, idempotency, outbox. Migrations with rollout/recovery. Backup/restore assumptions.

## 6. Security And Supply Chain

Trust boundaries, secrets, TLS, injection/SSRF/path/command, debug endpoints. `govulncheck` / `cargo audit`/`deny`, lockfile, pinned tools, SBOM where present. An advisory is not automatically exploitable without reachability.

## 7. Resilience, Performance, Observability

Bounded timeout/retry/concurrency. Performance only with measurement. Structured logs, traces, metrics, health separation, alert+runbook.

## 8. Artifact, Shutdown, Deploy, CI

Reproducible production build, container hygiene, graceful shutdown, migration order, rollback/recovery, CI matrix (MSRV/latest, race, features, targets).

## Mandatory Evidence Matrices

Create every applicable matrix. Use `NOT_APPLICABLE` only with a reason and `UNVERIFIED` when evidence is unavailable.

| ID | Matrix | Minimum columns |
| --- | --- | --- |
| M1 | Source, toolchain, and artifact identity | component | commit | toolchain | graph/lock | tags/features | target/profile | artifact digest | runtime proof | status |
| M2 | Executable, module, crate, and deployment inventory | unit | language | entrypoint | owner | data | network | privileges | deployment | criticality | tests |
| M3 | Go target and build-tag support | command/package | GOOS | GOARCH | tags | cgo | libc | toolchain | build | test | artifact | owner |
| M4 | Rust target, feature, MSRV, and profile support | crate/bin | target | features | profile | MSRV | stable | native deps | build | test | artifact | owner |
| M5 | Concurrency and lifecycle ownership | goroutine/task | creator | resource | limit | cancellation | join/supervision | panic | metric | shutdown | test |
| M6 | Unsafe, cgo, FFI, native, and ABI boundary | boundary | caller | callee | safety contract | ownership | ABI/layout | unwind | threading | validation | tool evidence | owner |
| M7 | API, RPC, stream, and protocol contract | method/service | authn | authz/owner | validation | limits | deadline | idempotency | transaction | compatibility | negative test |
| M8 | State-changing business flow | flow | invariant | reads | locks | writes | side effects | commit | retry | reconciliation | rollback | tests |
| M9 | Data schema and migration compatibility | change | old reader | old writer | new reader | new writer | backfill | lock risk | rollback | forward repair | restore test |
| M10 | Dependency and supply-chain trust | dependency/tool | source | pin/lock | license | advisory | build execution | native/unsafe | owner | update | revocation |
| M11 | SLO, capacity, overload, and observability | journey | SLI | objective | load model | bottleneck | admission limit | alert | dashboard | runbook | evidence |
| M12 | Rollout, rollback, restore, and incident readiness | risk | rollout gate | canary | abort signal | rollback action | data compatibility | restore step | RPO/RTO | owner | drill evidence |

## Mandatory Adversarial And Failure Scenarios

Execute applicable scenarios with defined preconditions, observable signals, pass/fail thresholds, cleanup, and evidence level. Do not report merely that the system survived.

1. Two concurrent mutations target the same invariant, aggregate, key, account, quota, or inventory item.
2. A request or message is retried before, during, and after commit, response loss, acknowledgment loss, or process crash.
3. The client disconnects or deadline expires while database, filesystem, queue, subprocess, or foreign-library work is in flight.
4. A slow or malicious peer sends partial frames, oversized lengths, compressed bombs, endless streams, invalid encodings, or protocol state violations.
5. Database pool, connection limit, file descriptor, memory, CPU, thread, goroutine, task, queue, or ephemeral-port capacity approaches exhaustion.
6. A downstream dependency becomes slow, intermittently fails, returns overload, closes connections, changes DNS, rotates certificates, or recovers gradually.
7. Retry multiplication occurs across client, proxy, service, database, queue, and worker layers.
8. The process receives graceful shutdown while accepting work, holding locks, owning leases, serving streams, committing transactions, or publishing events.
9. The process panics, aborts, is killed, or loses the host during partial initialization, migration, write, upload, event publication, or checkpoint.
10. Old and new binaries coexist against old, intermediate, and new schemas, messages, caches, and protocol peers.
11. A build tag, feature, target, cgo/native path, allocator, TLS backend, database backend, or optional integration differs from the commonly tested default.
12. A stale lock holder, lease owner, leader, cache entry, token, configuration snapshot, or DNS answer continues after ownership or authority changed.
13. A queue delivers duplicates, reorders messages, delays messages beyond assumptions, rebalances ownership, or replays a poison message from DLQ.
14. Tenant, account, role, namespace, or object identifiers are changed while preserving valid syntax and authentication.
15. Secrets, signing keys, certificates, tokens, dependency credentials, or encryption keys rotate, expire, are revoked, or become temporarily unavailable.
16. Backup or snapshot restores into an isolated environment while binaries, migrations, keys, external dependencies, and retained events differ from backup time.
17. Telemetry, health, readiness, and alerts are evaluated during degradation to prove they distinguish dependency failure, overload, deadlock, leak, corruption, and recovery.
18. Rollback is attempted after a code-only change, configuration change, dependency change, schema change, protocol change, and partially completed rollout.

## Special Target Overlays

### CLI, Daemon, And System Service

- Verify stdin/stdout/stderr contracts, exit codes, signal handling, terminal detection, non-interactive mode, config precedence, atomic file writes, lock files, privilege dropping, service-manager readiness, restart policy, and log ownership.
- Ensure scripts and automation can distinguish validation, partial success, retryable failure, permanent failure, and interrupted execution.

### WebAssembly, Plugin, And Embedded Targets

- Verify host imports, capability model, linear-memory limits, allocator and panic behavior, serialization boundary, browser or WASI support, deterministic assumptions, sandbox escape surface, and version negotiation.
- For plugins, verify ABI/API stability, loading path, signatures, version compatibility, isolation, resource ownership, panic/crash containment, hot reload, and revocation.
- For embedded or constrained targets, verify allocator availability, interrupt and concurrency model, no-std assumptions, watchdog, power failure, flash wear, persistent-state atomicity, firmware signing, update recovery, and hardware-in-the-loop tests.

## Release, Rollback, Restore, And Incident Contract

- Promote one immutable artifact through environments; do not silently rebuild production from the same source version.
- Define pre-deploy gates, canary population, SLI comparison, error-budget impact, abort signals, human ownership, maximum observation window, and automatic versus manual rollback.
- Verify graceful shutdown against real orchestration timing, connection draining, readiness removal, in-flight deadlines, queue lease behavior, background workers, and final telemetry flush.
- Document rollback limitations after schema, message, cache, key, file-format, side-effect, or external-contract changes; use forward repair when reversal is unsafe.
- Prove isolated restore, application compatibility, migration replay, key access, external dependency restoration, event reconciliation, RPO, RTO, and integrity checks.
- In incident mode preserve volatile and durable evidence, stop destructive cleanup, bound access, rotate or revoke affected trust, contain blast radius, produce trusted rebuilds, verify eradication, and record recovery decisions.

## Evidence-Driven Repair Workflow

1. Freeze scope, protect work and data, and establish the evidence ceiling.
2. Reproduce the defect or prove the violated invariant with the smallest safe scenario.
3. Identify root cause across source, generated code, toolchain, dependency, configuration, data, runtime, platform, and operations.
4. Design the smallest safe repair and explicitly reject fixes that only hide symptoms, widen privilege, remove validation, disable checks, or increase capacity without analysis.
5. Add a regression test plus concurrency, failure, security, migration, compatibility, or recovery coverage appropriate to the cause.
6. Execute focused checks, then the supported language, target, tag/feature, integration, artifact, load, deployment, and rollback matrix.
7. Review the final diff, dependency and lock changes, generated output, artifacts, telemetry, residual risk, ownership, and operational documentation.

## Production Checklist

Fill: YES / NO / PARTIAL / UNVERIFIED / NOT_APPLICABLE

1. Supported Go and/or Rust toolchain; no unapproved preview/nightly baseline.
2. Go toolchain/directives aligned; Rust toolchain/MSRV/edition aligned.
3. Reproducible build; lock/checksum; dependency audit; pinned build tools.
4. Production build and target build actually executed.
5. Unit/integration/race/fuzz/Miri-sanitizer/security/migration/recovery where applicable.
6. Goroutine/task lifecycle, cancellation, timeout, bounded concurrency, backpressure.
7. No confirmed critical data races/leaks; shutdown verified.
8. Unsafe/FFI inventory, safety invariants, ABI, Send/Sync, native lifecycle.
9. Validation, HTTP/RPC, authz, tenant, rate limit, idempotency, TLS, secrets, debug endpoints.
10. DB constraints/pool/transactions/locking/migrations/backup/restore.
11. Timeout/retry/jitter; no retry storms; messaging recovery.
12. Performance measured or explicitly bounded.
13. Observability: log/trace/metrics/health/alert/runbook.
14. Immutable artifact, non-root, SBOM where applicable, graceful shutdown.
15. Rollout, abort, rollback, recovery, post-deploy verification.

## Definition Of Done

Work is complete only when applicable items are marked with evidence or `NOT_APPLICABLE`:

1. Technology path confirmed; all relevant modules/workspaces/crates inventoried.
2. Toolchain, lifecycle, and support status verified from current sources.
3. Dependency graph mapped; supply chain reviewed.
4. Initial build/test baseline and production artifact actually built.
5. Target/feature/tag compatibility verified or marked UNVERIFIED.
6. Critical flows mapped.
7. Every reported problem has evidence; cause separated from symptom.
8. P0/P1 fixed or have containment and recovery; fixes have regression tests.
9. Go concurrency checked with the race detector where possible.
10. Rust unsafe has documented safety invariants; Miri/sanitizer limits are clear.
11. Goroutine/task lifecycle and shutdown verified; cancellation/timeout propagated.
12. Concurrency bounded to dependency capacity.
13. Transactions and idempotency verified; migrations have rollout/recovery plan.
14. Security trust boundaries tested; secrets neither disclosed nor baked into artifacts.
15. Performance not declared without measurement.
16. Observability enables diagnosis; debug/profiler endpoints not unsafely exposed.
17. Graceful shutdown matches the deployment platform.
18. Rollout, abort, and rollback documented.
19. Final diff free of accidental changes; command log complete.
20. Unverified areas explicit; no production-readiness claim without evidence.

If any condition is unmet: **The project is not yet fully production-ready.** List the blocking conditions precisely.

## Forbidden Behavior

Do not:

- invent command output, files, packages, crates, endpoints, or CVEs;
- claim tests pass if not executed; hide failing tests; disable tests/lints only so the pipeline turns green;
- ignore errors or `Result`; add panic/unwrap as a quick fix;
- add recover/`catch_unwind` as a universal solution;
- start uncontrolled goroutines/tasks; use unbounded channels without memory analysis;
- share a Go map without synchronization; use the same unsafe resource in parallel;
- add `Arc<Mutex<_>>` only to silence a compiler error;
- add unsafe only for performance without measurement; write `unsafe impl Send/Sync` without a formal invariant;
- suppress Miri/sanitizer/Clippy findings without analysis; enable all Clippy restriction lints;
- use floating nightly in production; `go install ...@latest` in reproducible CI;
- change `go.mod`/`go.sum`/`Cargo.lock` without review; use replace/`[patch]`/git dependencies without documentation;
- claim `cargo check` replaces `cargo build`; claim `go test` replaces race and integration checks;
- retry non-idempotent operations without protection; use in-memory idempotency in multi-replica systems;
- expose pprof/metrics/admin/debug endpoints publicly; disable TLS verification;
- run destructive migrations; raise pool/concurrency without capacity analysis;
- optimize without a profiler or benchmark; declare the project perfect.

## Production Decision Rule

- Return exactly one verdict: `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`, or `INCIDENT_CONTAINMENT_REQUIRED`.
- A `READY` verdict requires applicable P0 and P1 findings closed, mandatory matrices complete, critical scenarios passed, immutable artifact verified, rollout and rollback proven, and restore evidence meeting approved RPO/RTO.
- Use `READY_WITH_CONDITIONS` only when every condition has owner, deadline, containment, measurable acceptance criterion, and no hidden P0/P1 exposure.
- Any unresolved critical authorization, data-integrity, memory-safety, concurrency, migration, supply-chain, rollback, or restore risk blocks an unconditional ready verdict.

## Mandatory Final Report

Deliver Markdown with:

1. Executive summary and verdict: `ready` / `ready-with-conditions` / `not-ready`.
2. Technology path and toolchain/support status.
3. Architecture, concurrency, unsafe/FFI, auth, and critical-flow maps.
4. Endpoint/RPC matrix where applicable: `method | route/service | auth | policy/ownership | validation | timeout | idempotency | transaction | test | status`.
5. Findings table: `ID | P0-P3 | language | area | file/symbol | cause | impact | evidence | repair | verification | status`.
6. Implemented changes, files, dependency/lock changes, regression risk, and validation.
7. Actual commands, toolchain/target/feature, exit codes, and material results.
8. Race/Miri/sanitizer/fuzz/security/performance results and their limits.
9. Blocked checks, blockers, and residual risk.
10. Remaining work: `blocks production` / `needed soon` / `planned refactor` / `optional improvement`.
11. External sources: title, URL, version/status, access date, decision informed.
12. Version table: `Component | Project | Resolved | Current stable | Support/EOL | Compatibility | Action`.

## Work Order

1. protect the workspace;
2. determine technology path;
3. module/workspace inventory;
4. toolchain and lifecycle analysis;
5. dependency and supply-chain analysis;
6. initial build/test/lint baseline;
7. architecture map and critical flows;
8. concurrency and lifecycle;
9. unsafe/FFI;
10. data and transactions;
11. security;
12. performance and observability;
13. evidence-backed findings;
14. minimal fixes and regression tests;
15. production build, deployment, and rollback;
16. final report.

Iterate: inventory → evidence → root cause → minimal fix → test → race/Miri/sanitizer where relevant → production build → deployment → rollback → documentation.

Priorities: user and data protection; memory and concurrency correctness; authentication and authorization; functional correctness; transactions and idempotency; operational reliability; measurement-based performance; architectural maintainability; developer experience.

The final result must enable another experienced Go or Rust engineer to determine unambiguously: which toolchain was used; what was actually executed; which targets and feature/tag combinations were checked; what was found; how the problem was reproduced; what the root cause is; what was changed; which test proves the fix; whether race, unsafe, or FFI risk remains; what was not checked; how the artifact is deployed; how rollout is aborted; how the system is rolled back or recovered.
