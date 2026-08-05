## 9. Dependency And Supply-Chain Audit

Audit the resolved graph and build behavior, not package names alone.

- Inspect direct, transitive, dev, native, plugin, tool, and build-runner dependencies with source, version, license, maintainer, release cadence, and platform support.
- Review path, git, hosted, SDK, override, local fork, unpublished, prerelease, and discontinued dependencies.
- Verify lock-file discipline for applications and deliberate compatibility policy for reusable packages.
- Inspect `build.yaml`, builders, generators, scripts, hooks, code-mod tools, native build scripts, and package setup actions as executable supply-chain code.
- Search for dependency confusion, typosquatting, compromised maintainer risk, abandoned plugins, excessive native privileges, dynamic downloads, and binary blobs.
- Correlate advisories with actual resolved versions, reachable code paths, runtime configuration, platform, and mitigations before assigning severity.
- Generate or verify SBOM and provenance for Dart packages, native libraries, embedded frameworks, assets, and release artifacts.
- Define update, deprecation, fork, replacement, vulnerability response, and emergency revocation ownership for critical dependencies.
- Do not mass-upgrade packages; upgrade by compatibility cluster with contract tests, migration evidence, performance comparison, and rollback.

