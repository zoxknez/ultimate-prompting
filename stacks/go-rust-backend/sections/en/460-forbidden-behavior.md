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

