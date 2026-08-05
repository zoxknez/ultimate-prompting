## Phase 2 - Source-To-Runtime Identity And Provenance

Prove the identity of code, dependencies, generated output, artifact, deployment, runtime configuration, schema, and browser-visible release.

### Audit Requirements

- Correlate repository, commit, dirty state, lockfile digest, toolchain, environment class, and build invocation.
- Record resolved packages, patches, overrides, native modules, lifecycle scripts, generated assets, and build-time network access.
- Identify build output, route manifest, function bundles, static assets, image digest, source maps, and deployment identifier.
- Bind deployment revision to logs, traces, errors, safe diagnostics, and browser-visible build metadata.
- Record effective config, flags, region, runtime, schema version, cache namespace, and deployment ID.
- Reject mutable tags, rebuild-per-environment promotion, or claims not tied to immutable identifiers.

### Required Evidence

- Commit-lockfile-artifact-deployment-runtime correlation table.
- Build manifest with toolchain, dependency graph, generated inputs, and output digests.
- Runtime release metadata in logs, traces, errors, and safe responses.
- Evidence that the same immutable artifact is promoted across environments.

### Mandatory Failure And Acceptance Tests

- Detect an intentionally mismatched deployment identifier before traffic reaches it.
- Keep an old tab open through deployment and verify asset/server compatibility.
- Reproduce the release from a clean environment and compare authoritative digests.
- Trace a runtime error to exact commit, artifact, config, schema, and flag state.

