## MySQL i InnoDB putanja

### Release track, runtime i SQL mode

- Identifikuj LTS ili Innovation track, tacan patch, edition, distribuciju i Oracle support status.
- Proveri MySQL 8.0 EOL izlozenost i podrzanu upgrade putanju ka izabranoj liniji.
- Pregledaj globalne, persisted i session promenljive, kao i precedence konfiguracionih fajlova.
- Pregledaj `sql_mode`, strictness, zero date-ove, division, group-by, implicit default-e i aplikativne pretpostavke.
- Proveri character set, collation, timezone tabele, authentication plugin-e, keyring komponente i TLS.

### InnoDB transakcije, lock-ovi i trajnost

- Pregledaj isolation, consistent read, locking read, gap i next-key lock-ove i auto-increment locking.
- Zabelezi deadlock report-e, metadata lock-ove, history-list rast, purge lag i duge transakcije.
- Pregledaj redo, undo, doublewrite, flush politiku, binary-log sync i crash-recovery pretpostavke.
- Proveri connection i thread concurrency prema buffer pool-u, temporary storage-u i I/O kapacitetu.
- Testiraj commit uncertainty, deadlock retry i obradu duplih request-a.

### MySQL planovi, indeksi i DDL

- Koristi `EXPLAIN ANALYZE`, optimizer trace ili Performance Schema samo sa ogranicenim reprezentativnim upitima.
- Pregledaj redosled composite kljuceva, covering indekse, prefix indekse, functional indekse, invisible indekse i histogram-e.
- Pregledaj efekte clustered primary key-a, secondary-index amplification i write ponasanje random kljuceva.
- Za DDL proveri `ALGORITHM`, `LOCK`, instant ili in-place eligibility, table rebuild i uticaj metadata lock-a.
- Koristi online-schema alate samo nakon analize trigger-a, foreign key-a, replike, throttling-a, cutover-a i cleanup-a.

### MySQL replikacija, HA, backup i PITR

- Pregledaj binary-log enablement, format, GTID, retention, enkripciju, source identitet i crash-safe repository-je.
- Pregledaj asynchronous, semi-synchronous, Group Replication, InnoDB Cluster, Router i managed-service ponasanje.
- Testiraj replica lag, write-set konflikte, errant transaction-e, clone ili seed, promotion i split-brain prevenciju.
- Dokazi backup konzistentnost, binary-log koordinate ili GTID i replay do izabrane tacke.
- Testiraj application reconnect, read/write rutiranje, failover, failback i transaction uncertainty.

