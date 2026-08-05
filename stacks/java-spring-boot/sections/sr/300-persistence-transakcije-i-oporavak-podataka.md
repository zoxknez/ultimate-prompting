## Persistence, Transakcije I Oporavak Podataka

### JPA, Hibernate, JDBC I Ispravnost Mapping-a

- Pregledaj entity identitet, equality, hash code, mutability, ownership, cascade, orphan removal, fetch strategiju, inheritance, converter-e, listener-e, generisane vrednosti i audit polja.
- Detektuj N+1 query-je, Cartesian product-e, neograničene kolekcije, lazy pristup van validnog context-a, duple join-ove, slučajne flush-eve, dirty-checking iznenađenja i serializaciju entity-ja.
- Proveri optimistic i pessimistic locking, lock timeout, deadlock obradu, isolation, write skew, sprečavanje lost update-a i retry scope kroz konkurentne testove.
- Pregledaj stvarni SQL, bind vrednosti uz bezbednu redakciju, query planove, index-e, cardinality procene, broj redova, sortiranje, stabilnost paginacije i production-like distribuciju podataka.
- Tretiraj ORM portabilnost kao nedokazanu dok svaki podržani database dialect, verzija, collation, vremenska zona, isolation i migration putanja nisu testirani.

### Connection Pool I Database Failure

- Zabeleži pool implementaciju, min/max veličinu, acquisition timeout, validation, lifetime, idle timeout, leak detection, initialization SQL, transaction default-e i metrike.
- Dimenzioniši pool prema capacity baze, broju replika, background radu, admin saobraćaju, virtual-thread konkurentnosti, failover ponašanju i drugim aplikacijama.
- Testiraj pool exhaustion, spore query-je, network partition, primary failover, DNS promenu, stale konekcije, rotaciju kredencijala, rotaciju sertifikata i restart baze.
- Proveri da timeout i cancellation stižu do driver-a i servera gde je moguće; napušteni client future ne sme da ostavi neograničen database rad.
- Alertuj na saturation, wait time, timeout, active/idle disbalans, starost transakcije, deadlock, replication lag i klase grešaka povezane sa runbook-ovima.

### Dokaz Transaction Granice

- Za svaku kritičnu operaciju zabeleži transaction manager, propagation, isolation, read-only flag, timeout, rollback pravila, proxy putanju, uključene resurse i side effect-e van transakcije.
- Testiraj checked exception-e, uhvaćene exception-e, wrapped exception-e, async granice, self-invocation, više transaction manager-a, savepoint-e, nested pozive i retry.
- Dokaži da se nijedan remote poziv, objava poruke, cache mutacija, upis fajla, email, plaćanje ili nepovratni side effect ne smatra atomarnim sa database transakcijom osim ako stvarni protokol to pruža.
- Koristi unique constraint, compare-and-set, version kolonu, idempotency zapis ili locking da concurrency invarijante budu sprovodive u autoritativnom store-u.
- Zabeleži tačnu crash tačku pre, tokom i posle commit-a i definiši replay, reconciliation i operator repair za svaki dvosmisleni ishod.

### Outbox, Inbox, Saga I Idempotency

- Za svaku komandu i event definiši stabilan identitet, deduplication scope, retention, canonical request hash, response replay, conflict ponašanje i tenant vezivanje.
- Proveri transactional outbox insert, ordering objave, polling ili CDC ownership, retry, duplu objavu, cleanup, lag monitoring i disaster recovery.
- Proveri da je inbox ili consumer deduplication atomaran sa lokalnom state promenom i da preživljava process crash, rebalance, redelivery i expiry retention-a.
- Za saga-e dokumentuj state machine, compensation preduslove, nepovratne korake, timeout, manuelnu intervenciju i observability zaglavljenih ili parcijalno kompenzovanih instanci.
- Testiraj duple request-e pre commit-a, posle commit-a pre odgovora, posle gubitka odgovora, posle failover-a, posle deploy-a i posle expiry-ja idempotency zapisa.

### Schema Migracija, Backup I Restore

- Inventariši Flyway, Liquibase, Hibernate DDL, custom skripte, online schema alate, seed podatke, reference podatke, search mapping-e, cache schema-e i message schema-e.
- Koristi expand-and-contract za rolling kompatibilnost; testiraj old code/new schema, new code/old schema gde je potrebno, mešane verzije, parcijalni backfill, pause, resume, retry i granice rollback-a.
- Pregledaj lock-ove, rewrite rizik, veličinu transakcije, rast diska, replication lag, statement timeout, strategiju izgradnje index-a, validation query-je i vidljiv napredak.
- Zabrani nekontrolisanu automatsku produkcionu migraciju iz svake application replike osim ako su konkurentnost, ownership, failure i recovery dokazivo bezbedni.
- Izvrši izolovane restore i point-in-time recovery probe koje potvrđuju schema-u, podatke, ključeve, fajlove, queue-eve, search index-e, object storage, startup aplikacije, reconciliation, RPO i RTO.


