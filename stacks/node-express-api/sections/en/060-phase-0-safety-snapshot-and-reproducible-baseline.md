## Phase 0 - Safety Snapshot And Reproducible Baseline

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Capture branch, commit, dirty state, submodules, worktrees, tags, and generated files before changes.
- Resolve the authoritative lockfile and package manager; reject installs that mutate it unexpectedly.
- Run the repository lint, typecheck, unit, integration, build, production start, smoke, and audit commands that actually exist.
- Start built output without production side effects and exercise critical health and request paths.
- Capture the first failure, environment, versions, warnings, and exact exit code instead of masking failures.
- Establish an initial P0/P1 containment decision before low-priority cleanup.

### Required Evidence

- Produce and preserve the command log and environment manifest.
- Produce and preserve clean install, build, and startup artifacts.
- Produce and preserve the initial service and dependency map.

### Mandatory Failure And Acceptance Tests

- Prove that dirty checkout content is not overwritten.
- Prove that frozen installation detects lock drift.
- Prove that the baseline can be reproduced from a clean checkout.

