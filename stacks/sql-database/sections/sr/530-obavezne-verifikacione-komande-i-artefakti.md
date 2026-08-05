## Obavezne verifikacione komande i artefakti

Koristi samo komande primerene stvarnom engine-u i dozvolama. Bezbedno zabelezi izlaz i rediguj tajne. Primeri su sabloni, a ne dozvola da se pokrenu u produkciji.

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
Artefakt: redigovan dijagram topologije
Artefakt: izvestaj schema i migration drift-a
Artefakt: matrica kriticnih transakcija i invarijanti
Artefakt: before/after planovi upita i load dokaz
Artefakt: izvestaj migration rehearsal-a i abort-a
Artefakt: izvestaj izolovanog restore-a i PITR-a
Artefakt: izvestaj failover/failback-a i reconciliation-a
Artefakt: zavrsni P0-P3 readiness izvestaj
```

