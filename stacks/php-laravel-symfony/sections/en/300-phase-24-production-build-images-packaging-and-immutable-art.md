## Phase 24 - Production Build, Images, Packaging, and Immutable Artifacts

### Objective

Prove that the reviewed source produces one reproducible, minimal, immutable, identifiable, and runnable production artifact.

### Audit Requirements

- Build from a clean checkout with pinned PHP, Composer, extensions, operating system packages, frontend toolchain, and generation steps.
- Install production dependencies with lockfile enforcement, controlled scripts and plugins, optimized autoloading, and no hidden development packages.
- Generate and verify caches, compiled containers, optimized routes, assets, translations, proxies, metadata, and frontend bundles in a controlled stage.
- Audit container base image, FPM and web server config, non-root execution, filesystem permissions, writable paths, capabilities, health, and signal handling.
- Embed or expose release identity, dependency inventory, build metadata, schema compatibility, and artifact digest without leaking secrets.
- Scan, sign, attest, and store the exact artifact; deploy the same digest across environments without rebuilding.

### Required Evidence

- Clean build transcript, lockfile verification, artifact digest, SBOM, signature, and provenance.
- Artifact inventory proving expected code, dependencies, extensions, config, caches, and absence of development tools or secrets.
- Smoke and critical-flow results from the packaged artifact, not a source checkout.

### Acceptance Criteria

- One immutable digest is traceable to source, toolchain, dependencies, tests, deployment, telemetry, and rollback.
- Production does not depend on mutable source mounts, runtime dependency installation, or manual cache generation.

