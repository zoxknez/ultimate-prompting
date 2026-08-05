## Phase 3 - Node.js, Package Manager, Install, And Supply Chain

Audit the executable dependency and installation path rather than package.json declarations alone.

### Audit Requirements

- Determine actual Node binary, release line, architecture, libc, OpenSSL/FIPS mode, and native ABI in local, CI, preview, and production.
- Verify lockfile owner, package-manager version, Corepack policy, frozen install, workspace resolution, peers, and hoisting.
- Inspect lifecycle scripts, binary downloads, generators, patches, Git/path dependencies, and registry config.
- Detect dependency confusion, typosquatting, compromised maintainers, unmaintained packages, duplicates, and reachable vulnerabilities.
- Verify registry token scope, provenance, cache trust, offline policy, and approved advisory suppressions.
- Treat native addons, WASM, image processors, database drivers, and browser binaries as platform-specific inputs.

### Required Evidence

- Executed Node and package-manager version evidence.
- Resolved dependency graph, advisory report, reachability rationale, and suppressions.
- Lifecycle-script and build-time network inventory.
- Release-tied SBOM or equivalent dependency inventory.

### Mandatory Failure And Acceptance Tests

- Frozen install must fail on package.json and lockfile drift.
- Build without network after dependencies are prepared or document every exception.
- Build supported architectures for native dependencies.
- Prove untrusted pull requests cannot access release tokens, production secrets, or privileged caches.

