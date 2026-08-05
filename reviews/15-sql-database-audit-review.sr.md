# Revizija 15 - SQL / PostgreSQL / MySQL / MariaDB / SQLite production audit prompt

## Status

Paket je potpuno unapredjen i sinhronizovan na verziju 2.0.0.

- EN linije: 803
- SR linije: 803
- EN H1-H3 naslovi: 74
- SR H1-H3 naslovi: 74
- heading depth odstupanja: 0
- line-shape odstupanja: 0
- YAML frontmatter: validan
- Markdown fence blokovi: balansirani
- baseline JSON: validan
- nedozvoljeni Unicode tipovi crte u SR promptu: 0

## Kriticna ispravka baseline-a

Stari prompt je pogresno oznacavao MySQL 9.7 kao LTS liniju.

Zvanicni MySQL release model jasno razdvaja:

- MySQL 8.4 - LTS linija
- MySQL 9.7 - Innovation linija

Aktuelno potvrdjeni patch nivoi na dan 5. avgusta 2026. su:

- MySQL 8.4.10 LTS
- MySQL 9.7.2 Innovation

MySQL 8.0 je dostigao community EOL u aprilu 2026. Prompt sada zahteva poseban upgrade plan i ne tretira cloud extended support kao automatsku zamenu za internu security i lifecycle politiku.

## PostgreSQL baseline

Potvrdjeno je:

- PostgreSQL 18.4 je aktuelni stabilni patch
- podrzani major-i su 18, 17, 16, 15 i 14
- PostgreSQL 14 dobija poslednje izdanje 12. novembra 2026.
- PostgreSQL 19 Beta 2 nije podrazumevani production baseline

Prompt sada zahteva proveru stvarnog server procesa, package ili image identiteta, managed-service kompatibilnosti, extension verzija i kompletnog base-backup plus WAL recovery lanca.

## SQLite baseline

Potvrdjeno je SQLite 3.53.4 izdanje od 24. jula 2026.

Prompt vise ne prihvata verziju iz package manifesta ili jezickog binding-a kao dovoljan dokaz. Zahteva:

- `sqlite_version()`
- `sqlite_source_id()`
- `PRAGMA compile_options`
- stvarno ucitanu native biblioteku
- journal i WAL mode
- filesystem locking ponasanje
- podrzanu koordinisanu backup metodu

## MariaDB razdvajanje

MariaDB 12.3 je aktuelna LTS linija, ali prompt je tretira kao zaseban engine.

Zabranjeno je automatsko prenosenje:

- MySQL release modela
- MySQL upgrade checker zakljucaka
- Group Replication i Router semantike
- optimizer i SQL-mode pretpostavki
- GTID i replication pravila
- backup i restore procedure

## Glavna unapredjenja

### Formalni audit ugovor

Dodati su:

- E0-E5 evidence model
- P0-P3 severity model
- finding register
- precizni work mode-ovi
- read-only-first pravilo
- stop uslovi
- mandatory recovery dokaz
- readiness decision model

### Source-to-data identitet

Novi prompt povezuje:

`repository -> commit -> migration checksum -> schema -> engine build -> package/image -> endpoint -> topology -> process -> data -> backup/log chain -> restore`

Time se uklanja opasna pretpostavka da su migration fajlovi, ORM model ili schema dump sami po sebi stvarna produkciona istina.

### Schema i poslovne invarijante

Detaljno su dodati:

- schema drift
- tipovi i collation
- novac, vreme i timezone
- natural, surrogate, composite i tenant kljucevi
- PK, UK, FK, CHECK, exclusion i partial constraint-i
- soft-delete uniqueness
- NULL semantika
- concurrent insert i update testovi
- reconciliation upiti

### SQL semantika i injection

Obradjeni su:

- three-valued logic
- `NOT IN` i NULL
- join cardinality
- outer-join filteri
- deterministicki pagination
- implicit cast
- collation coercion
- engine-specific upsert i merge
- value parameterization
- identifier allowlist
- second-order injection
- JSON, regex, full-text i spatial input

### Transakcije i konkurentnost

Novi prompt zahteva dokaz za:

- transaction boundaries
- auto-commit i implicit commit
- savepoint i nested semantics
- isolation anomaly-je
- lost update i write skew
- optimistic i pessimistic locking
- deadlock graph i retry
- commit uncertainty
- idempotency claim i result
- outbox, inbox, saga i reconciliation

### Performanse

Audit vise ne preporucuje indeks po intuiciji.

Zahteva:

- reprezentativne parametre i distribuciju podataka
- before/after planove
- actual rows i estimate kvalitet
- buffers, waits, spills i temporary rad
- cold, warm, common, rare i skewed slucajeve
- index write cost
- plan-cache i parameter-sensitivity analizu
- p50, p95, p99 i end-to-end latenciju

### Storage i maintenance

Dodati su:

- WAL, binlog, undo i temporary rast
- vacuum, purge, checkpoint i compaction
- bloat i fragmentation
- migration rewrite headroom
- backup i restore headroom
- resource governance
- cancellation i timeout-i
- workload izolacija

### Migracije

Novi prompt tretira migration kao distribuirani release.

Obavezni su:

- tacna DDL lock semantika
- table rewrite dokaz
- log i replication uticaj
- old/new application koegzistencija
- expand-and-contract
- chunked i checkpointed backfill
- pause, resume i abort
- rollback ogranicenja
- forward repair

### Backup, PITR, HA i DR

Dodati su odvojeni ugovori za:

- PostgreSQL base backup i WAL
- MySQL backup i binary log
- SQLite Backup API i `VACUUM INTO`
- izolovani restore
- application-level verification
- PITR timezone proveru
- failover i stale-primary fencing
- failback i re-seeding
- RPO i RTO merenje
- disaster-recovery game day

### Security i tenancy

Detaljno su obradjeni:

- odvojene runtime, migration, reporting, backup i admin role
- default privilegije
- superuser i break-glass pristup
- RLS policy kombinacije
- tenant predicate bypass
- TLS i certificate rotation
- encryption at rest i backup encryption
- secrets inventory
- privileged audit
- PII, retention, deletion i legal hold

### Engine-specific putanje

Dodate su kompletne putanje za:

- PostgreSQL
- MySQL i InnoDB
- MariaDB
- SQLite
- managed i cloud baze

### Dodatni specijalizovani slojevi

Dodati su:

- stored procedure, function i trigger audit
- materialized view, search i spatial audit
- sequence i distributed ID allocation
- multi-database konzistentnost
- data-quality i continuous integrity
- ORM i query-builder audit
- CDC, ETL i export audit
- major-upgrade rehearsal
- change governance i privileged production access

## Obavezni dokazi

Prompt sadrzi 12 evidence matrica:

1. identitet
2. topologija
3. schema drift
4. invarijante
5. transakcije
6. upiti i planovi
7. konekcije
8. migracije
9. bezbednost
10. backup i restore
11. HA
12. release readiness

## Adversarial i failure scenariji

Dodato je 20 scenarija, ukljucujuci:

- concurrent unique insert
- concurrent balance ili inventory update
- timeout oko commit-a
- crash posle commit-a
- deadlock i serialization failure
- long transaction
- pool exhaustion
- failover tokom in-flight request-a
- old/new release overlap
- dupli backfill
- WAL/binlog/disk exhaustion
- stale primary return
- stale replica authorization read
- missing log segment
- pogresan PITR timezone
- key rotation
- tenant omission
- malformed input
- SQLite multi-instance i shared-storage problem
- restore uz kasnije spoljne side effect-e

## Zakljucak

Novi paket je uskladjen sa dubinom ostalih 2.0 production audit promptova. On vise nije lista generickih SQL preporuka, vec kompletan ugovor za dokazivanje integriteta, bezbednosti, performansi, migracija, oporavka i operativne spremnosti realnog sistema baza podataka.
