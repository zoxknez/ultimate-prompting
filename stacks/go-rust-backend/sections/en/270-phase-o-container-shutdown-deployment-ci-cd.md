## Phase O - Container, Shutdown, Deployment, CI/CD

Artifact: reproducible build, pinned base image/digest, non-root, minimal OS, CA/certs, timezone, signal handling, no secrets in layers, SBOM, scan.

Graceful shutdown: stop accepting work, drain, cancel tasks/goroutines with context, flush logs/telemetry, close pools/conns, finish within platform deadline. Test during long requests, jobs, and migrations.

Deployment: immutable artifact, migration order, rolling/canary, abort criteria, application vs database rollback (explicit), recovery, post-deploy verification.

CI/CD: pinned toolchain (Go/Rust), matrix (OS/arch/features/MSRV), race/fuzz/audit where relevant, locked build, no `go install @latest` / floating nightly, artifact promotion, secret hygiene.

