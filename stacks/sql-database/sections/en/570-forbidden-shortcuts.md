## Forbidden Shortcuts

- Do not add indexes by intuition or remove them only because a counter says unused.
- Do not run `VACUUM FULL`, `OPTIMIZE TABLE`, rebuild, reindex, purge or shrink as a generic fix.
- Do not disable foreign keys, checks, row security, strict mode, durability or TLS to make a migration pass.
- Do not delete migration history, edit applied migrations or force checksums without root-cause analysis.
- Do not treat ORM models, a schema dump, a replica, a snapshot or a dashboard as the sole truth.
- Do not perform production DDL from an interactive shell without reviewed artifact, timeout, monitoring and abort plan.
- Do not claim zero downtime, exactly once, no data loss or recovery readiness without failure evidence.
- Do not copy a live SQLite main file alone in WAL mode and call it a verified backup.

