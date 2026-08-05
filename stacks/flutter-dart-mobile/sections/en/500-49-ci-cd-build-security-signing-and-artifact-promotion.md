## 49. CI/CD, Build Security, Signing, And Artifact Promotion

The release pipeline is part of the application security boundary.

- Map repository permissions, branch protection, code review, CI triggers, fork behavior, environments, approvals, runner trust, caches, artifacts, secrets, and deployment identities.
- Pin actions, images, SDK archives, package indexes, native dependencies, and tools by immutable version or digest where feasible; verify provenance.
- Prevent untrusted pull requests, build scripts, tests, generators, dependency hooks, or artifact uploads from accessing signing keys, store credentials, production tokens, or privileged runners.
- Prefer short-lived workload identity and protected signing services; define custody, access, quorum, audit, backup, rotation, expiry, revocation, and disaster recovery for keys.
- Build once from an identified commit, retain immutable artifacts, scan and sign the exact bytes, promote the same artifact, and prevent environment-specific rebuilds.
- Generate checksums, SBOM, provenance, dependency inventory, symbols, source maps, release notes, effective configuration, test evidence, and approval record per artifact.
- Verify final signatures, entitlements, permissions, manifests, identities, versions, native libraries, assets, symbols, and store/install metadata after all transformations.
- Protect artifact retention and rollback candidates from deletion or mutation until release and incident policy permits cleanup.
- Test key expiry, revoked credential, unavailable store, failed signing, partial upload, wrong artifact, duplicate version, canceled release, and emergency release path.

