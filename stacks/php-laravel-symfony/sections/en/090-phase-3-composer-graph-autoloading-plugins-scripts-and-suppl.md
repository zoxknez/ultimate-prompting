## Phase 3 - Composer Graph, Autoloading, Plugins, Scripts, And Supply Chain

### Objective

Prove a deterministic, policy-compliant dependency graph and understand all code executed during installation and autoload.

### Audit Requirements

- Validate `composer.json` and lock consistency, PHP and extension constraints, stability flags, platform config, repositories, conflict, replace, provide, and branch aliases.
- Inventory Packagist, private Composer repositories, VCS, path, artifact, and custom repository trust boundaries.
- Audit `allow-plugins`, plugins, installers, scripts, hooks, and code executed during install, update, dump-autoload, or package discovery.
- Verify dist archives, source fallback behavior, credentials, repository TLS, package provenance, abandoned packages, and reachable advisories.
- Inspect PSR-4, classmap, files autoload, authoritative classmap, APCu autoloader, optimized autoload, duplicate classes, and case-sensitivity differences.
- Reproduce a frozen install from a clean checkout and detect network, credential, plugin, platform, or generated-file drift.

### Required Evidence

- Resolved package graph, repository origin, checksums, licenses, advisories, and package ownership.
- Plugin and install-script allowlist with purpose, privilege, version, and removal path.
- Clean frozen install result and SBOM or equivalent inventory tied to artifact digest.

### Acceptance Criteria

- The lockfile is authoritative, reproducible, reviewed, and not silently mutated by build or deployment.
- No unreviewed plugin, script, repository, package, or source fallback can execute in trusted builds.

