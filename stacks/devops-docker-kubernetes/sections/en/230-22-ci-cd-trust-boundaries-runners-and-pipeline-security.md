## 22. CI/CD Trust Boundaries, Runners And Pipeline Security

**Objective:** Prevent untrusted changes from gaining build, secret, artifact, deployment, or cloud authority.

### 22.1 Required Checks

1. Map events, repositories, branches, tags, pull requests, forks, actors, environments, approvals, reusable workflows, external triggers, and deployment targets.
2. Audit default token permissions, job-level permissions, OIDC claims, cloud trust policies, environment protection, branch rules, required reviews, and separation of build from deploy.
3. Pin third-party actions, images, plugins, orbs, templates, and includes to immutable reviewed references. Verify maintainer, provenance, permissions, and update process.
4. Separate trusted and untrusted jobs. Prevent fork or pull-request code from accessing production secrets, caches, artifacts, signing, registries, self-hosted networks, or deployment credentials.
5. Audit self-hosted runners for tenancy, persistence, cleanup, patching, network reachability, container escape, host credentials, workspace reuse, autoscaling, and compromise response.
6. Prevent command, path, expression, matrix, artifact, cache, environment-file, log, and shell injection from untrusted metadata.
7. Verify artifact upload and download identity, checksum, attestation, retention, access, overwrite behavior, and cross-workflow substitution resistance.
8. Test cancellation, retry, duplicate trigger, stale approval, partial publish, unavailable registry, compromised dependency, runner loss, and rollback pipeline.

### 22.2 Minimum Evidence

- Pipeline trust-boundary and permission map.
- Fork, OIDC, runner, artifact, cache, and injection test evidence.
- Representative build-to-deploy audit trail with approvals and immutable references.

### 22.3 Exit Criteria

1. Untrusted code cannot access trusted credentials, networks, artifacts, caches, or deployment authority.
2. Production deployment requires attributable, protected, least-privileged identities and reviewed evidence.
3. Runner compromise, artifact substitution, and duplicate execution have tested containment paths.

