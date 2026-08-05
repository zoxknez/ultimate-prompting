## Phase 3 - Package Manager, Dependencies, And Supply Chain

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Use one authoritative lockfile per workspace boundary and document intentional exceptions.
- Verify frozen installation, peer resolution, hoisting, overrides, patches, optional dependencies, and platform conditions.
- Audit lifecycle scripts, install-time binary downloads, git and path dependencies, private registries, proxies, and auth scope.
- Distinguish vulnerable presence from reachable and exploitable use, but never ignore unpatched runtime dependencies without evidence.
- Review dependency confusion, typosquatting, compromised maintainer, abandoned package, malicious update, and transitive native-code risks.
- Verify SBOM completeness, provenance, signatures or attestations, and the policy that consumes them.

### Required Evidence

- Produce and preserve the resolved dependency graph and lock digest.
- Produce and preserve the script, registry, and advisory trust map.
- Produce and preserve SBOM, provenance, and enforcement evidence.

### Mandatory Failure And Acceptance Tests

- Prove that clean installation is deterministic.
- Prove that untrusted pull requests cannot access release credentials.
- Prove that a revoked package or tool is blocked and replaceable.

