## Phase 1 - Repository, Workspace, Executable, And Ownership Map

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Map monorepo workspaces, packages, apps, internal libraries, shared schemas, infrastructure, migrations, and operational tools.
- Identify every API, worker, cron, CLI, migration runner, webhook receiver, realtime gateway, and one-off script.
- Assign owners for authentication, authorization, tenant isolation, data, cache, queue, release, rollback, restore, and incident response.
- Detect circular dependencies, cross-layer imports, duplicated schemas, shadow config, dead scripts, and abandoned deployment paths.
- Map trust boundaries from client through CDN and proxy to service, database, broker, storage, providers, and admin tooling.
- Distinguish authoritative business logic from adapters, generated code, framework glue, and test-only implementations.

### Required Evidence

- Produce and preserve the workspace and executable graph.
- Produce and preserve route-to-owner and side-effect-to-owner matrices.
- Produce and preserve the trust-boundary and authoritative-source map.

### Mandatory Failure And Acceptance Tests

- Prove that every production executable is discoverable.
- Prove that a critical route has an identified owner.
- Prove that undocumented admin and maintenance paths are surfaced.

