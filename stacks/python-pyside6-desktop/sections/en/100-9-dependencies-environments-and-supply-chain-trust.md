## 9. Dependencies, Environments, And Supply-Chain Trust

### 9.1 Audit Scope

1. Inventory `pyproject.toml`, requirements files, lock files, constraints, editable installs, VCS/path dependencies, private indexes, wheelhouses, and vendored code.
2. Determine the authoritative resolver and environment workflow: pip, uv, Poetry, PDM, pip-tools, Conda, Hatch, Rye legacy, system packages, or custom tooling.
3. Review build backends, PEP 517 isolation, dynamic metadata, setup hooks, package-data rules, namespace packages, entry points, and executable scripts.
4. Identify source distributions, compiled wheels, post-install steps, binary downloads, code generators, and packages that execute code during build or import.
5. Check dependency confusion, typosquatting, index precedence, mutable VCS references, compromised maintainers, abandoned packages, license obligations, and security advisories.
6. Separate runtime dependencies, packaging-only dependencies, development tools, test tools, optional extras, platform markers, and plugin ecosystems.

### 9.2 Required Verification

1. Resolve from a clean environment using the committed lock/constraints and compare hashes, versions, markers, wheel tags, and transitive graphs across CI and release.
2. Prefer verified wheels or reproducibly built artifacts; document every source build, native toolchain, external download, and trusted key.
3. Generate and review SBOM, license inventory, vulnerability report, provenance, and package signature/hash evidence for the release graph.
4. Test offline or controlled-index installation where required and prove that an unexpected public package cannot override a private name.
5. Fail the release for unresolved critical advisories, unreviewed executable hooks, unsupported binary wheels, or non-reproducible dependency resolution.

