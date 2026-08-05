## SQLite putanja

### Ucitana biblioteka, compile opcije i fajl sistem

- Proveri `sqlite_version()`, `sqlite_source_id()` i `PRAGMA compile_options` iz stvarnog aplikativnog procesa.
- Identifikuj system biblioteku, bundled amalgamation, static link, dynamic link, language binding i extension loading.
- Proveri page size, reserved bytes, encoding, auto-vacuum, maksimalne limite i kompatibilnost sa postojecim fajlovima.
- Pregledaj garancije lock-ovanja lokalnog fajl sistema; ne postavljaj writable SQLite bazu na nepodrzan network ili sync storage.
- Zastiti database, `-wal`, `-shm`, journal, backup i temporary fajlove ispravnim ownership-om i dozvolama.

### Transakcije, WAL, lock-ovanje i konkurentnost

- Proveri journal mode, synchronous nivo, locking mode, busy timeout i connection-per-thread ponasanje.
- Testiraj deferred, immediate i exclusive transaction ponasanje pod paralelnim reader-ima i writer-ima.
- Izmeri WAL rast, checkpoint ponasanje, duge reader-e, write starvation i crash recovery.
- Koristi ograniceni retry za `SQLITE_BUSY` ili `SQLITE_LOCKED`; nikada ne skrivaj neogranicenu contention.
- Testiraj pad procesa, nestanak napajanja, pun disk, read-only storage i ponasanje dve instance aplikacije.

### SQLite schema, integritet, migracija i backup

- Proveri `foreign_keys` na svakoj konekciji, `trusted_schema`, defensive podesavanja i upotrebu STRICT tabela gde je primereno.
- Pregledaj affinity, dynamic typing, numeric konverziju, collation i ponasanje generated kolona.
- Koristi `PRAGMA integrity_check` ili `quick_check` uz razumevanje troska i ogranicenja; dodaj aplikativne invarijante.
- Testiraj table-rebuild migracije sa trigger-ima, indeksima, foreign key-evima, kolicinom podataka, crash-em i rollback-om.
- Koristi online Backup API, `VACUUM INTO` ili drugu podrzanu koordinisanu metodu; ne kopiraj slepo samo glavni fajl u WAL rezimu.
- Restore-uj u izolaciju, proveri source ID i compile opcije, pokreni integrity provere i aplikativne smoke testove.

