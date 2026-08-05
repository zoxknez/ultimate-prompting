## Phase 0 - Safety Snapshot And Reproducible Baseline

### Objective

Capture the exact starting state and execute only safe, side-effect-aware baseline checks before diagnosis or repair.

### Audit Requirements

- Capture branch, commit, dirty state, submodules, worktrees, tags, generated files, local patches, and deployment references.
- Identify the authoritative Composer lockfile, monorepo boundaries, path repositories, and environment-specific dependency resolution.
- Inventory existing lint, static analysis, test, build, bootstrap, smoke, migration, queue, and security commands without inventing defaults.
- Assess bootstrap side effects before running `artisan`, `bin/console`, application entrypoints, service providers, bundles, or custom scripts.
- Preserve logs, failed commands, stack traces, configuration fingerprints, and the first reproducible failure.
- Verify local checks cannot connect to production databases, queues, caches, email, payment, storage, search, or identity providers.

### Required Evidence

- Command log with directory, binary, SAPI, INI, environment, exit code, and redacted result.
- Repository snapshot and explicit list of unavailable or unsafe evidence.
- Baseline test and bootstrap results from a disposable environment.

### Acceptance Criteria

- The starting state is recoverable and no unapproved production side effect occurred.
- Every subsequent finding can be traced to a concrete revision and environment.

