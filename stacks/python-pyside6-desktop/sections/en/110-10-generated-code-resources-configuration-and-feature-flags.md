## 10. Generated Code, Resources, Configuration, And Feature Flags

### 10.1 Audit Scope

1. Inventory `.ui`, `.qrc`, QML cache, translation catalogs, protobuf/OpenAPI clients, ORM models, icons, themes, schemas, version files, and generated bindings.
2. Record generator executable, version, inputs, options, environment, output ownership, determinism, and regeneration command.
3. Map configuration precedence across defaults, bundled files, environment, command line, registry/plist, user settings, enterprise policy, remote config, and feature flags.
4. Distinguish public configuration from secrets and identify values copied into packages, logs, crash reports, or support bundles.
5. Review feature-flag ownership, targeting, expiry, offline behavior, fail-open/fail-closed behavior, and rollback dependencies.
6. Detect stale generated output, developer-local resources, missing translations, case-sensitive path differences, and source/package drift.

### 10.2 Required Verification

1. Regenerate from a clean checkout and fail on unexplained diff or missing toolchain.
2. Inspect the package and installed application to confirm the intended resources, translations, certificates, schemas, and configuration are present once and loaded from trusted locations.
3. Test precedence and malformed-value behavior without silently falling back to unsafe defaults.
4. Exercise flag enable, disable, stale cache, network loss, targeting change, emergency kill, and rollback scenarios.
5. Ensure sensitive values are injected at the correct runtime boundary and are absent from source control, package resources, logs, and telemetry.

