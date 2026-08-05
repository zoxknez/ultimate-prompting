## 8. Source-To-Production Integrity And Drift

**Objective:** Prove what is running, where it came from, and how it was promoted.

### 8.1 Required Checks

1. Trace a representative production revision from commit and review through build, tests, artifact digest, signature, provenance, registry, deployment revision, and running process.
2. Compare source manifests, generated manifests, Helm or Kustomize output, GitOps desired state, live objects, cloud resources, and runtime configuration.
3. Detect manual hotfixes, mutable tags, floating dependencies, unreviewed console changes, emergency changes, and controller exclusions.
4. Verify environment promotion preserves artifact identity instead of rebuilding different binaries per environment unless explicitly designed and controlled.
5. Verify deployment metadata exposes commit, digest, build, owner, change request, and rollback target without leaking secrets.
6. Reconcile declared and live state without overwriting emergency evidence or legitimate controlled exceptions.

### 8.2 Minimum Evidence

- End-to-end trace for at least one production artifact and one rollback artifact.
- Desired-versus-live drift report across application and infrastructure layers.
- List of mutable, rebuilt, manually changed, or unverifiable artifacts.

### 8.3 Exit Criteria

1. Running critical workloads are attributable to reviewed source and verified artifacts.
2. Material drift has an owner, disposition, and safe reconciliation path.
3. Promotion and rollback preserve identity and auditability.

