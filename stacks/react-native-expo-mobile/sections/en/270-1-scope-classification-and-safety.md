## 1. Scope, Classification, And Safety

### 1.1 Product And Workflow Classification
- Classify bare React Native, Expo managed with CNG, Expo prebuild, Expo bare, brownfield, library, Expo Module, monorepo, white-label, and multiple-app variants separately.
- Record every supported platform, architecture, store, enterprise channel, update channel, environment, tenant, brand, and feature-flag cohort.
- Separate current production support from aspirational, experimental, community-maintained, or untested support claims.
- Identify whether android and ios directories are authoritative source, generated output, partially generated output, or manually maintained state.
- Map application IDs, bundle identifiers, EAS project IDs, update URLs, runtime versions, schemes, associated domains, signing identities, and store records.
- Do not merge findings across platforms or workflows unless the evidence proves the same mechanism and impact.

### 1.2 Authorization And Change Boundaries
- Confirm permission before changing package versions, lockfiles, native projects, app identifiers, signing configuration, EAS project linkage, update channels, or store state.
- Never publish an OTA update, submit a store build, rotate signing material, revoke credentials, or migrate production data without explicit authorization.
- Preserve forensic evidence before cleaning generated directories, caches, build outputs, native dependencies, local databases, or crash logs.
- Use redacted evidence and secret-safe commands; never print keystores, provisioning profiles, private update keys, access tokens, refresh tokens, or user data.
- Define stop conditions for destructive prebuild, schema migration, signing change, OTA rollout, native dependency upgrade, and incident containment.
- Prefer reversible, reviewable, narrow changes with an explicit test and rollback path.

