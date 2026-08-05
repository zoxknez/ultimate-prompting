## 48. Flavors, Environments, Feature Flags, And Configuration

Environment isolation must be enforced across code, artifacts, services, signing, stores, and data.

- Inventory Dart entrypoints, flavors/schemes/configurations, application IDs, bundle IDs, web origins, desktop identities, signing, icons, names, backends, analytics, push, payments, and stores.
- Verify no production artifact can accidentally target staging identity, database, analytics, push, payment, storage, feature flags, or update channel, and vice versa.
- Treat `--dart-define`, environment files, remote config, build settings, manifests, plist values, web configuration, and desktop resources as one effective configuration.
- Detect missing, duplicate, stale, conflicting, insecure-default, and silently falling-back configuration.
- Feature flags must define owner, purpose, targeting, prerequisite, default, offline behavior, telemetry, expiry, cleanup, security boundary, and emergency behavior.
- Do not use client flags to grant server authorization or protect secrets; validate risky flag combinations and old-client behavior.
- Test fresh install, upgrade, restored backup, offline startup, missing remote config, stale cache, wrong clock, revoked flag, and rollout/rollback.
- Include an effective-configuration snapshot in release evidence without exposing secrets.

