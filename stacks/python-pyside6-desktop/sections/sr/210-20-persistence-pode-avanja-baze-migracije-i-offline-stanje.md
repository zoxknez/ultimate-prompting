## 20. Persistence, podešavanja, baze, migracije i offline stanje

### 20.1 Obim audita

1. Inventariši QSettings, JSON/YAML/TOML/XML fajlove, SQLite, SQLAlchemy, ORM store-ove, cache-eve, key-value baze, object store-ove, istorije, queue-eve i privremene fajlove.
2. Zabeleži verzije schema-e i formata, vlasništvo, dozvole, enkripciju, journaling, atomic-write strategiju, locking, backup, retention i brisanje.
3. Pregledaj vlasništvo database konekcije po thread-u/procesu, transaction granice, isolation, constraint-e, busy timeout-e, WAL, checkpoint-e, corruption handling i redosled zatvaranja.
4. Proceni konkurentne instance aplikacije, crash tokom write-a, pun disk, read-only medij, antivirus locking, network home direktorijume i prekinut upgrade.
5. Mapiraj offline command queue-eve, sync cursor-e, conflict resolution, deduplikaciju, tombstone-e, pretpostavke sata i reconciliation sa serverskim autoritetom.
6. Razlikuj korisničke preference od security politike, credential-a, authorization stanja, poslovnih zapisa, izvedenog cache-a i obnovljivih download-a.

### 20.2 Obavezna verifikacija

1. Pokreni migration matrice sa svake podržane istorijske verzije koristeći reprezentativne, velike, malformed, delimično migrirane i korumpirane skupove podataka.
2. Injektuj crash pre, tokom i posle atomic write-a, commit-a, schema izmene, zamene cache-a i sync acknowledgement-a.
3. Testiraj dve instance aplikacije, stale lock-ove, konkurentne update-e, promenu naloga, rollback na stariji binary i forward repair.
4. Izvrši izolovan restore backup-a i, gde je primenljivo, point-in-time recovery; izmeri i zabeleži postignuti RPO i RTO.
5. Dokaži da logout, brisanje korisnika, retention expiry, uninstall i kreiranje support bundle-a obrađuju svaku klasu podataka prema politici.

