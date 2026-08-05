## Phase D - Engine, Version, Edition, And Lifecycle

Establish exact support status and upgrade constraints without confusing compatible products.

- Record server version, patch, edition, distribution, architecture, libc, OpenSSL and operating system.
- Separate protocol compatibility, SQL compatibility, storage-engine compatibility and managed-service compatibility.
- Review release notes, security advisories, deprecations, removed behavior and supported upgrade path.
- Verify extension and plugin compatibility before engine upgrades.
- Prove downgrade limitations and whether rollback requires data restore or forward repair.
- Treat MySQL and MariaDB, PostgreSQL and compatible forks, and SQLite bindings as distinct products until proven otherwise.

