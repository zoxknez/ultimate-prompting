## 33. CI/CD, Artifact Promotion, Release Governance, And Supply Chain

### 33.1 Audit Scope

1. Map repository, branch protection, review, CI runners, reusable workflows, caches, artifacts, package indexes, signing services, notarization, stores, update feeds, and deployment approvals.
2. Distinguish trusted and untrusted code paths, especially forks, pull requests, dependency update bots, self-hosted runners, and generated artifacts.
3. Review workflow injection, command quoting, secrets exposure, mutable action references, cache poisoning, artifact substitution, environment approvals, and OIDC scope.
4. Require locked and verified dependencies, pinned toolchains, controlled external downloads, SBOM, provenance, signature, and vulnerability/license gates.
5. Build once per target and promote the same immutable bytes through test, signing, staging, and production where platform rules allow.
6. Define release ownership, segregation of duties, emergency path, key compromise, package-index compromise, runner compromise, and trusted rebuild.

### 33.2 Required Verification

1. Reproduce release builds from clean runners and compare dependency, resource, native-library, package, and installer manifests and hashes.
2. Prove that untrusted code cannot read signing keys, publish packages, mutate release artifacts, poison trusted caches, or approve production.
3. Verify signatures, provenance, SBOM, release notes, version metadata, and update metadata all refer to the same reviewed bytes.
4. Exercise credential expiry, signing-service outage, notarization failure, store rejection, compromised dependency, revoked key, and emergency rebuild.
5. Keep an auditable record of approver, source commit, toolchains, dependencies, artifact hashes, signatures, channels, cohort, rollout, abort, and rollback.

