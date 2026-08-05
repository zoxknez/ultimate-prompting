## PostgreSQL putanja

### Runtime, ekstenzije i konfiguracija

- Proveri `SHOW server_version`, `server_version_num`, paket ili image, verzije ekstenzija i managed-service engine.
- Pregledaj `postgresql.conf`, `postgresql.auto.conf`, role i database podesavanja, startup parametre i pending restart vrednosti.
- Pregledaj `pg_hba.conf`, SSL, authentication metode, replication pristup i redosled include fajlova.
- Audituj poverenje ekstenzija, shared preload libraries, background worker-e, upgrade skripte i binary kompatibilnost.
- Proveri locale, ICU, collation verzije i reindex zahteve nakon promene operativnog sistema ili ICU-a.

### MVCC, vacuum, freeze i bloat

- Izmeri starost transakcija, dead tuple-ove, autovacuum progress, freeze age i wraparound rizik.
- Pregledaj table-specific autovacuum pragove, cost podesavanja, scale factor-e i uklapanje sa workload-om.
- Detektuj duge transakcije, replication slot-ove, prepared transaction-e i idle session-e koji zadrzavaju stare snapshot-e.
- Izmeri table i index bloat uz ogranicenja metode; ne propisuj `VACUUM FULL` bez analize rewrite-a i lock-a.
- Proveri vacuum, analyze i reindex procedure pod disk i replication ogranicenjima.

### PostgreSQL planovi, indeksi i partitioning

- Koristi `EXPLAIN (ANALYZE, BUFFERS, WAL, SETTINGS, VERBOSE)` samo kada je izvrsavanje bezbedno i ograniceno.
- Pregledaj B-tree, hash, GIN, GiST, SP-GiST, BRIN, expression, partial, INCLUDE i unique index semantiku.
- Pregledaj extended statistics, correlation, visibility map, index-only scan i HOT update ponasanje.
- Proveri partition pruning tokom planiranja i izvrsavanja, partitionwise operacije i rast default particije.
- Audituj failure concurrent index build-a, invalid indekse, attach ili detach lock-ove i replication lag.

### PostgreSQL replikacija, HA i oporavak

- Pregledaj `wal_level`, archive mode, archive command, retention, WAL gap-ove, timeline-ove i restore command.
- Pregledaj fizicku i logicku replikaciju, slot-ove, publication-e, subscription-e, replica identity i obradu konflikata.
- Proveri synchronous-commit i synchronous-standby semantiku prema latenciji i RPO-u.
- Testiraj promotion, timeline promenu, `pg_rewind` preduslove, fencing stale primary-ja i failback.
- Dokazi da base backup i neprekinuti WAL archive mogu da vrate izabranu tacku i pokrenu aplikaciju.

### PostgreSQL bezbednost i row-level politike

- Pregledaj ownership, `SECURITY DEFINER`, search path, function volatility i privilegije ekstenzija.
- Pregledaj default privilegije, schema create pristup, public role grant-ove i dozvole za temporary objekte.
- Testiraj row-level security sa owner-om, `BYPASSRLS`, restrictive i permissive kombinacijama politika.
- Pregledaj ponasanje logical backup-a i replikacije za role, politike, large object-e i ekstenzije.
- Spreci da nepoverljiv input kontrolise search path, identifikatore, dinamicki SQL ili server-side pristup fajlovima.

