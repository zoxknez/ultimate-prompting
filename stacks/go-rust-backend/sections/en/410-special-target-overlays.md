## Special Target Overlays

### CLI, Daemon, And System Service

- Verify stdin/stdout/stderr contracts, exit codes, signal handling, terminal detection, non-interactive mode, config precedence, atomic file writes, lock files, privilege dropping, service-manager readiness, restart policy, and log ownership.
- Ensure scripts and automation can distinguish validation, partial success, retryable failure, permanent failure, and interrupted execution.

### WebAssembly, Plugin, And Embedded Targets

- Verify host imports, capability model, linear-memory limits, allocator and panic behavior, serialization boundary, browser or WASI support, deterministic assumptions, sandbox escape surface, and version negotiation.
- For plugins, verify ABI/API stability, loading path, signatures, version compatibility, isolation, resource ownership, panic/crash containment, hot reload, and revocation.
- For embedded or constrained targets, verify allocator availability, interrupt and concurrency model, no-std assumptions, watchdog, power failure, flash wear, persistent-state atomicity, firmware signing, update recovery, and hardware-in-the-loop tests.

