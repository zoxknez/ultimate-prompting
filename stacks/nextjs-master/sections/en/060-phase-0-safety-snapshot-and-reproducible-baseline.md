## Phase 0 - Safety Snapshot And Reproducible Baseline

### Mandatory Commands

```bash
git status --short --branch
git rev-parse HEAD
git submodule status --recursive || true
node --version
corepack --version || true
# use the package manager selected by the lockfile
# npm ci | pnpm install --frozen-lockfile | yarn install --immutable
# run repository lint, typecheck, unit, integration, production build, production start, and smoke scripts
```

### Baseline Rules

- Run from a clean checkout or record every local modification that affects the result.
- Use frozen or immutable installation and fail on lockfile drift.
- Do not use dev-mode success as a substitute for production build and production start.
- Capture route manifests, build output, warnings, static/dynamic decisions, bundle analysis, and runtime logs.
- Repeat the authoritative build in the release platform image, architecture, environment class, and package-manager mode.
- Start the built artifact without production side effects and smoke-test critical journeys.

### Baseline Outputs

- Command log with exit codes and relevant warnings.
- Version and lifecycle table for framework, runtime, package manager, ORM, auth, and platform.
- Initial route, runtime, cache, identity, data, and deployment inventory.
- Initial P0/P1 containment decision before lower-priority work.

