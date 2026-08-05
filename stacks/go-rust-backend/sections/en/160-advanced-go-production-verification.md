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

