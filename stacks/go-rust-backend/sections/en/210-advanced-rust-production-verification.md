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

