## Required Verification Commands And Artifacts

Use only commands appropriate to the actual engine and permissions. Record output securely and redact secrets. The examples are templates, not permission to run them in production.

```sql
-- PostgreSQL identity templates
SELECT version(), current_database(), current_user;
SHOW server_version;
SELECT extname, extversion FROM pg_extension ORDER BY 1;

-- MySQL identity templates
SELECT VERSION(), CURRENT_USER(), DATABASE();
SHOW VARIABLES WHERE Variable_name IN ('version','version_comment','sql_mode');

-- SQLite identity templates
SELECT sqlite_version(), sqlite_source_id();
PRAGMA compile_options;
```

```text
Artifact: sanitized topology diagram
Artifact: schema and migration drift report
Artifact: critical transaction and invariant matrix
Artifact: before/after query plans and load evidence
Artifact: migration rehearsal and abort report
Artifact: isolated restore and PITR report
Artifact: failover/failback and reconciliation report
Artifact: final P0-P3 readiness report
```

