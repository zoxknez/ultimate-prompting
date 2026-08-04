# MASTER PROMPT - Deep Production Audit, Repair, And Improvement Of A Go And/Or Rust Backend/Systems Project

## Research Baseline - 4 August 2026

This baseline is a starting point, not a substitute for verification at execution time. Re-check current first-party sources and the actual project before recommending or changing anything.

| Component | Confirmed status on 4 August 2026 | Mandatory audit-time verification |
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
