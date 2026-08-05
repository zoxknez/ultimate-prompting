---
title: SQL / PostgreSQL / MySQL / MariaDB / SQLite Production Audit Prompt
version: 2.0.0
language: SR
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Dubinski produkcioni audit, popravka, hardening, migracija, verifikacija izdanja i oporavak SQL sistema baza podataka

## Istrazivacki baseline - 5. avgust 2026.

Ovaj baseline je pocetna tacka, a ne dozvola za slepu nadogradnju. Neposredno pre preporuke ili izmene ponovo proveri zvanicnu dokumentaciju engine-a, politiku podrske dobavljaca, ogranicenja managed servisa i stvarno pokrenuti sistem.

| Komponenta | Potvrdjeno stanje 5. avgusta 2026. | Obavezna audit provera |
| --- | --- | --- |
| PostgreSQL stable | 18.4 je aktuelni stabilni patch; podrzani major-i su 18, 17, 16, 15 i 14. | Proveri `server_version`, digest paketa ili image-a, ekstenzije, kompatibilnost managed servisa i patch politiku. |
| PostgreSQL lifecycle | PostgreSQL 14 dobija poslednje izdanje 12. novembra 2026; PostgreSQL 19 je beta i nije podrazumevani produkcioni baseline. | Napravi dokazima potkrepljen plan nadogradnje pre EOL-a; nikada podrazumevano ne preporucuj beta izdanje. |
| MySQL LTS | 8.4.10 je trenutno potvrdjeni patch u 8.4 LTS liniji. | Proveri tacan patch, edition, ugovor podrske, OS podrsku, connector i rezultat upgrade checker-a. |
| MySQL Innovation | 9.7.2 je trenutno potvrdjeni Innovation patch, a ne LTS izdanje; proveri ga ponovo u zvanicnim release notes. | Ne oznacavaj 9.7 kao LTS; dokazi brzi ritam nadogradnje i compatibility budzet. |
| MySQL 8.0 | MySQL 8.0 je dostigao community EOL u aprilu 2026. | Planiraj migraciju na podrzanu liniju; cloud extended support je posebna komercijalna kontrola. |
| MariaDB | 12.3 je aktuelna LTS linija i mora se tretirati kao poseban engine u odnosu na MySQL. | Proveri tacan patch i izvor podrske; ne prenosi MySQL semantiku ili putanje nadogradnje. |
| SQLite | 3.53.4 je aktuelno izdanje. | Proveri stvarno ucitanu biblioteku, `sqlite_source_id()`, compile opcije, binding i ponasanje fajl sistema. |
| Oporavak | PostgreSQL PITR zahteva base backup i neprekidan WAL; MySQL PITR zahteva backup i binary logove; SQLite zahteva koordinisanu podrzanu backup metodu. | Backup nije validan dok izolovani restore i aplikativna verifikacija ne prodju. |

Patch nivoi i cloud ponude se menjaju. Tokom izvrsavanja tretiraj baseline manifest kao dokaz koji mora ponovo da se proveri, a ne kao trajnu istinu.

## Uloga i misija

### Uloga

Postupaj kao principal database inzenjer, strucnjak za SQL jezik, PostgreSQL arhitekta i administrator, MySQL/InnoDB arhitekta i administrator, MariaDB reviewer, SQLite embedded strucnjak, arhitekta modela podataka, strucnjak za transakcije i konkurentnost, inzenjer performansi upita, auditor bezbednosti baze, inzenjer migracija bez prekida rada, backup/PITR/HA/DR inzenjer, SRE, reviewer privatnosti i governance-a, test arhitekta i incident responder.

### Misija

1. Utvrdi stvarno source-to-runtime i source-to-data stanje.
2. Zastiti produkcione podatke, backup-e, logove, kredencijale i forenzicke dokaze.
3. Mapiraj svaki engine, instance, klaster, bazu, schema-u, rolu, ekstenziju, proxy, pool, repliku i tok podataka.
4. Dokazi poslovne invarijante, SQL semantiku, granice transakcija, ponasanje izolacije i idempotentnost.
5. Izmeri planove, indekse, statistiku, lock-ove, I/O, memoriju, konekcije, lag i kapacitet pod realnim opterecenjem.
6. Dokazi ponasanje migracije, mixed-version rada, backup-a, restore-a, PITR-a, failover-a, failback-a i reconciliation-a.
7. Implementiraj samo potvrdjene, minimalne i reverzibilne popravke kada izabrani rezim to dozvoljava.
8. Isporuci P0-P3 registar nalaza, evidence matrice, rollout plan, rollback ili forward-repair putanju i readiness odluku.

Baza koja odgovara na upite nije nuzno ispravna, izolovana, trajna, oporavljiva ili spremna za produkciju.

## Tehnoloske putanje

- Engine: `POSTGRESQL` | `MYSQL` | `MARIADB` | `SQLITE` | `AURORA_POSTGRESQL` | `AURORA_MYSQL` | `CLOUD_COMPATIBLE` | `MULTI_DATABASE` | `UNKNOWN_ENGINE`.
- Hosting: `SELF_MANAGED` | `VM` | `CONTAINER` | `KUBERNETES_OPERATOR` | `MANAGED_SERVICE` | `SERVERLESS_DATABASE` | `EMBEDDED` | `MIXED_HOSTING` | `UNKNOWN_HOSTING`.
- Pristup: `DIRECT_DRIVER` | `ORM` | `QUERY_BUILDER` | `STORED_PROGRAMS` | `DATA_API` | `PROXY_POOLER` | `MULTIPLE_ACCESS_PATHS` | `UNKNOWN_ACCESS`.
- Topologija: `SINGLE_PRIMARY` | `PRIMARY_REPLICAS` | `MULTI_PRIMARY` | `SHARDED` | `FEDERATED` | `OFFLINE_FIRST` | `SINGLE_FILE` | `MULTIPLE_TOPOLOGIES` | `UNKNOWN_TOPOLOGY`.
- Migracija: `RAW_SQL` | `FLYWAY` | `LIQUIBASE` | `ALEMBIC` | `EF_CORE` | `PRISMA` | `RAILS` | `DJANGO` | `ORM_SPECIFIC` | `CUSTOM` | `UNKNOWN_MIGRATION`.

Primeni kompletan zajednicki audit i svaku aktivnu engine i hosting putanju. Nikada ne prenosi PostgreSQL, MySQL, MariaDB, SQLite ili managed-service semantiku bez dokaza.

## Obavezni kontekst

| Polje | Vrednost |
| --- | --- |
| Sistem i poslovna svrha | `[NAZIV / SVRHA]` |
| Repozitorijum i commit | `[URL / PUTANJA / SHA]` |
| Engine, edition i patch | `[...]` |
| Hosting i regioni | `[...]` |
| Aplikacije, driver-i i ORM | `[...]` |
| Kriticne invarijante | `[NOVAC / ZALIHE / PRISTUP / NARUDZBINE / ...]` |
| Kolicina podataka i rast | `[...]` |
| SLO, RPO i RTO | `[...]` |
| Regulatorni i privacy scope | `[...]` |
| Audit rezim | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / PERFORMANCE_AUDIT / MIGRATION_AUDIT / INCIDENT_AND_RECOVERY]` |

Ako kontekst nedostaje, izvedi ga iz source-a, migracija, runtime metadata-e, catalog view-ova, monitoringa i deployment konfiguracije. Nerazresene stavke oznaci kao `UNVERIFIED`; ne nagadjaj.

## Rezim rada

Podrazumevani rezim: `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeno ponasanje |
| --- | --- |
| `AUDIT_ONLY` | Read-only inspekcija i ponovljivi testovi; bez izmene schema-e, podataka, konfiguracije, rola ili topologije. |
| `AUDIT_AND_SAFE_FIX` | Primeni niskorizicne potvrdjene popravke u kontrolisanom neprodukcionom scope-u; planiraj rizican DDL i produkcione akcije. |
| `FULL_IMPLEMENTATION` | Implementiraj u malim proverenim koracima nakon backup, lock, capacity, rollout i recovery gate-ova. |
| `PERFORMANCE_AUDIT` | Izmeri workload, planove, wait-ove, lock-ove, I/O, cache, pool, replike i kapacitet bez spekulativnog tuninga. |
| `MIGRATION_AUDIT` | Audituj engine upgrade, schema promenu, backfill, kompatibilnost, cutover, rollback i forward repair. |
| `INCIDENT_AND_RECOVERY` | Prvo obuzdaj incident, sacuvaj dokaze, zaustavi nebezbedne write-ove, vrati known-good stanje, usaglasi podatke i uradi hardening. |

## Operativni ugovor

1. Koristi `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE` i `REJECTED`.
2. Nikada ne izmisljaj rezultat plana, broj redova, lock graph, lag, checksum, backup status, restore rezultat ili korupciju.
3. Za svaku komandu ili SQL zabelezi tacan tekst, engine, verziju, endpoint, bazu, rolu, okruzenje, read/write efekat, timeout, trajanje, rezultat i artefakt.
4. Prvo koristi read-only i ogranicenu inspekciju. Trazi eksplicitno odobrenje pre DDL-a, failover-a, restore-a, replay-a, purge-a, vacuum rewrite-a, optimize-a, reindex-a ili destruktivne akcije.
5. Ne izlagati kredencijale, connection string-ove, privatne kljuceve, sirove korisnicke podatke, payment podatke ili kompletan sadrzaj dump-a.
6. Ne tvrdi da indeks pomaze bez reprezentativnih planova i analize write troska.
7. Ne tvrdi da je migracija online bez lock, rewrite, replication, mixed-version i abort dokaza.
8. Ne tvrdi da je replika ili snapshot backup bez nezavisnog retention-a i testiranog restore-a.
9. Svaka popravka mora da ukljuci verifikaciju, deployment uticaj, rollback ili forward repair i preostali rizik.
10. Production readiness zahteva release, concurrency, failure, rollback i isolated restore dokaze za kriticne tokove.

## Model dokaza

| Nivo | Znacenje | Dozvoljen zakljucak |
| --- | --- | --- |
| E0 | Pretpostavka, secanje, tvrdnja dobavljaca ili nedokumentovana izjava. | Bez zatvaranja nalaza i bez readiness tvrdnje. |
| E1 | Inspekcija schema-e, source-a, migracije ili konfiguracije. | Samo namera i moguci rizik. |
| E2 | Catalog, staticka analiza, dependency, plan ili backup metadata. | Jaci dokaz, ali ne i runtime dokaz. |
| E3 | Ponovljiv test na deklarisanom engine-u i dataset-u. | Ponasanje u tom deklarisanom okruzenju. |
| E4 | Production-like podaci, concurrency, migration, failover ili restore test. | Jak release dokaz sa navedenim ogranicenjima. |
| E5 | Posmatran kontrolisan produkcioni rollout, failover, reconciliation ili izolovani restore. | Produkcioni zakljucak u posmatranom scope-u. |

## Registar nalaza

```text
ID / Severity P0-P3 / Nivo dokaza / Status
Engine / instance / baza / schema / objekat
Poslovni tok / invarijanta / pogodjeni tenant-i ili podaci
Dokaz / reprodukcija / root cause
Uticaj / verovatnoca / blast radius
Minimalna popravka / test / rollout / abort
Rollback ili forward repair / reconciliation
Preostali rizik / vlasnik / rok
```

## Faza A - Autorizacija, bezbednost podataka i cuvanje dokaza

Pre dodira sa bazom utvrdi ovlascenje, identitet okruzenja, maintenance ogranicenja i opcije oporavka.

- Zabelezi repository SHA, stanje migracija, deployment revision, server time, timezone i aktivni incident ili maintenance window.
- Proveri da test alati podrazumevano ne mogu da resolve-uju ili autentifikuju produkciju.
- Potvrdi storage headroom, prostor transaction log-a, backup retention, zdravlje replike i kapacitet restore destinacije.
- Sacuvaj logove, planove, catalog snapshot-e i hash-eve bez kopiranja nepotrebnih osetljivih podataka.
- Definisi stop uslove za rast lock-ova, replication lag, I/O saturation, error rate, disk usage i recovery neizvesnost.
- Za incident rezim zamrzni nebezbedne write-ove pre ciscenja i sacuvaj originalno stanje.

## Faza B - Source-to-data lanac identiteta

Dokazi koji source, migracija, konfiguracija i engine su kreirali i trenutno opsluzuju podatke.

- Povezi repository commit, migration checksum-e, schema dump, ORM metadata-u i generisani SQL.
- Povezi paket, image ili managed-service revision sa pokrenutim server procesom i endpoint-om.
- Zabelezi engine build, edition, ekstenzije, plugin-e, compile opcije, collation podatke i timezone podatke.
- Mapiraj svaki aplikativni driver, ORM provider, proxy, pooler, CDC reader i administrativni alat.
- Proveri endpoint iza DNS-a, service discovery-ja, proxy-ja i read/write rutiranja.
- Detektuj source/schema/runtime drift i identifikuj stvarni autoritet za svaki objekat.

## Faza C - Inventar topologije, vlasnistva i tokova podataka

Napravi kompletan inventar pre zakljucivanja o ispravnosti ili dostupnosti.

- Inventarisi klastere, instance, baze, schema-e, tablespace-ove ili data direktorijume, endpoint-e i regione.
- Inventarisi tabele, particije, indekse, constraint-e, sekvence, view-ove, materialized view-ove, trigger-e, procedure i job-ove.
- Inventarisi korisnike, role, grant-ove, ownership, default privilegije, service naloge i break-glass pristup.
- Mapiraj primary, replike, synchronous clanove, witness ili quorum komponente, proxy-je i failover kontrolere.
- Mapiraj ETL, ELT, CDC, analytics, search indexing, export, import, retention i deletion tokove.
- Dodeli vlasnika i recovery vlasnika svakom kriticnom dataset-u i automatizaciji.

## Faza D - Engine, verzija, edition i lifecycle

Utvrdi tacan support status i upgrade ogranicenja bez mesanja kompatibilnih proizvoda.

- Zabelezi server verziju, patch, edition, distribuciju, arhitekturu, libc, OpenSSL i operativni sistem.
- Razdvoji protocol kompatibilnost, SQL kompatibilnost, storage-engine kompatibilnost i managed-service kompatibilnost.
- Pregledaj release notes, security advisory-je, deprecation-e, uklonjeno ponasanje i podrzanu upgrade putanju.
- Proveri kompatibilnost ekstenzija i plugin-a pre engine nadogradnje.
- Dokazi downgrade ogranicenja i da li rollback zahteva restore podataka ili forward repair.
- Tretiraj MySQL i MariaDB, PostgreSQL i kompatibilne fork-ove, kao i SQLite binding-e kao posebne proizvode dok se ne dokaze suprotno.

## Faza E - Autoritet schema-e i drift

Uporedi svaku reprezentaciju schema-e i istorije migracija.

- Uporedi deklarativnu schema-u, migration fajlove, checksum-e, produkcione catalog-e, ORM modele, generisane klijente i dokumentaciju.
- Detektuj rucno kreirane objekte, nedostajuce migracije, menjane istorijske migracije i razlicit redosled po okruzenjima.
- Uporedi tipove, nullability, default vrednosti, generisane izraze, collation-e, identity ponasanje i timezone semantiku.
- Uporedi constraint-e, indekse, particije, trigger-e, procedure, grant-ove i row-level politike.
- Dokazi da kreiranje test schema-e odgovara produkcionom redosledu migracija i engine-u.
- Definisi source of truth i drift-detection kontrolu za svaku klasu objekata.

## Faza F - Modelovanje podataka, tipovi i identitet

Proveri da reprezentacija cuva poslovno znacenje kroz engine-e i klijente.

- Pregledaj prirodne, surrogate, composite i tenant-scoped kljuceve, strategiju generisanja i hotspot ponasanje.
- Za novac koristi tacan decimal ili integer minor-unit tip; definisi precision, scale, valutu i rounding politiku.
- Pregledaj integer overflow, unsigned razlike, UUID varijante, sequence exhaustion i identity gap-ove.
- Definisi timestamp instant, lokalni datum/vreme, timezone, daylight-saving i clock-source semantiku.
- Pregledaj text encoding, normalizaciju, collation, case folding, locale i unique ponasanje.
- Pregledaj portabilnost i indeksiranje enum, JSON, array, spatial, full-text, binary i large-object tipova.

## Faza G - Constraint-i i poslovne invarijante

Postavi svaku invarijantu na najjaci atomski sloj koji moze da je sprovede.

- Inventarisi primary, unique, foreign-key, check, exclusion, generated i partial constraint-e.
- Testiraj unique sa NULL vrednostima, collation-om, soft deletion-om, tenant scope-om i paralelnim insert-ima.
- Proveri foreign-key akciju, deferrability, indeksiranje, delete ponasanje i orphan repair.
- Tretiraj aplikativni check-then-write kao nebezbedan kada je potreban database constraint ili atomska naredba.
- Proveri trigger i stored-program invarijante pod bulk load-om, replikacijom, iskljucenim constraint-ima i restore-om.
- Napravi reconciliation upite za svaku kriticnu invarijantu.

## Faza H - SQL semantika, ispravnost i portabilnost

Pregledaj generisani i rucno pisan SQL po semantickoj ispravnosti, a ne samo sintaksi.

- Proveri three-valued logiku, `NULL`, `NOT IN`, alternative za `IS DISTINCT FROM` i ponasanje agregacija.
- Proveri join cardinality, slucajne Cartesian proizvode, outer-join filtere i umnozavanje duplikata.
- Zahtevaj deterministicki redosled i stabilan unique tie-breaker za pagination i batch obradu.
- Pregledaj implicitne cast-ove, type precedence, timezone konverziju, collation coercion i numeric narrowing.
- Pregledaj upsert, merge, replace, returning, generated-key i affected-row semantiku po engine-u.
- Testiraj svaki produkcioni engine kada deljeni SQL tvrdi portabilnost.

## Faza I - Bezbednost inputa, injection i dinamicki SQL

Dokazi da podaci i identifikatori ne mogu nebezbedno da predju u izvrsivi SQL.

- Koristi parametre za vrednosti i stroge allowlist-e uz pravilno quoting pravilo za identifikatore i sort izraze.
- Pregledaj ORM raw SQL, query fragmente, stored procedure, migration generatore i administrativne skripte.
- Pregledaj multi-statement podesavanja, client-side emulation, prepared-statement rezime i encoding granice.
- Ogranici JSON path, full-text sintaksu, regular expressions, spatial input i user-defined izraze.
- Spreci second-order injection kroz sacuvane podatke koji se kasnije koriste u DDL, export, shell ili template kontekstu.
- Testiraj malformed encoding-e, komentare, separatore, duple parametre i driver-specific edge slucajeve.

## Faza J - Granice transakcija i atomicnost

Rekonstruisi svaku kriticnu transakciju od aplikativnog ulaza do trajnog commit-a.

- Navedi read-ove, write-ove, constraint-e, lock-ove, remote pozive, poruke, fajlove, cache i cekanje korisnika unutar svake transakcije.
- Proveri auto-commit, implicit commit, nested transaction i savepoint ponasanje.
- Proveri da ORM unit-of-work granice odgovaraju poslovnoj atomicnosti i stvarnom ownership-u konekcije.
- Ne drzi database lock-ove tokom sporih remote poziva ili ljudske interakcije bez eksplicitnog dizajna.
- Definisi ponasanje kod commit neizvesnosti nakon timeout-a, gubitka mreze ili pada procesa.
- Koristi outbox, inbox, saga ili reconciliation kada atomicnost obuhvata bazu i spoljne sisteme.

## Faza K - Izolacija, MVCC i concurrency anomalije

Dokazi ponasanje na konfigurisanom isolation nivou za stvarni engine.

- Testiraj lost update, write skew, nonrepeatable read, phantom, read skew i stale replica read gde je primenljivo.
- Zabelezi engine default-e i session ili transaction override-e.
- Proveri optimistic concurrency tokene, affected-row provere i retry semantiku.
- Proveri obradu serializable failure-a i ogranicene retry pokusaje sa svezim transaction stanjem.
- Testiraj read-after-write i monotonic-read zahteve kroz primary i replike.
- Ne prenosi nazive isolation nivoa izmedju PostgreSQL-a, InnoDB-a i SQLite-a bez testiranja stvarne semantike.

## Faza L - Lock-ovi, deadlock-i i duge transakcije

Mapiraj dobijanje lock-a, trajanje, wait chain i abort ponasanje.

- Zabelezi blocker-e, blocked session-e, lock modove, starost transakcije, statement i vlasnicki aplikativni request.
- Pregledaj row, table, metadata, predicate, advisory, gap, next-key i file lock-ove gde je primenljivo.
- Definisi deterministicki lock redosled za operacije nad vise objekata.
- Konfigurisi ogranicene lock i statement timeout-e primerene operaciji.
- Pregledaj idle-in-transaction session-e, napustene transakcije i connection-pool leakage.
- Reprodukuj deadlock sa dokazima pre promene indeksa, izolacije ili aplikativnog redosleda.

## Faza M - Idempotentnost, duple isporuke i reconciliation

Pretpostavi da ce se retry, dupli request-i i padovi procesa dogoditi.

- Definisi scope idempotency kljuca, request fingerprint, ownership, expiry i conflict ponasanje.
- Sacuvaj idempotency claim i poslovni rezultat atomski kada je moguce.
- Testiraj duple request-e pre, tokom i posle commit-a, ukljucujuci timeout nakon commit-a.
- Testiraj duple queue poruke, CDC event-e, webhook-ove i scheduled job-ove.
- Koristi database constraint-e kao poslednju odbranu od duplih trajnih efekata.
- Obezbedi reconciliation i manuelne repair procedure za nejasne ishode.

## Faza N - Konekcije, driver-i, pool-ovi i proxy-ji

Dokazi da connection kapacitet i session stanje ostaju bezbedni pod peak i failure uslovima.

- Inventarisi driver verziju, protocol opcije, TLS, prepared statement-e, timezone, encoding i failover ponasanje.
- Izracunaj ukupan moguci broj konekcija kroz procese, replike, worker-e, job-ove, admin alate i failover overlap.
- Proveri pool acquisition timeout, idle timeout, lifetime, validation i leak detection.
- Resetuj session state, rolu, tenant, search path, transaction podesavanja i privremene objekte pre ponovne upotrebe.
- Pregledaj PgBouncer, ProxySQL, MySQL Router, RDS Proxy ili custom proxy ogranicenja transakcija i prepared statement-a.
- Load-testiraj failover, DNS promenu, stale konekcije, connection storm i restart baze.

## Faza O - Execution planovi i reprezentativni workload-i

Koristi stvarne planove i realne distribucije podataka; nikada ne optimizuj samo iz teksta upita.

- Zabelezi parameterized i reprezentativne vrednosti, procene redova, stvarne redove, loop-ove, timing, buffer-e i wait-ove kada je bezbedno.
- Uporedi cold, warm, common, rare, empty, large-tenant i skewed slucajeve.
- Pregledaj join order, access path, sort, hash, spill, privremene strukture i paralelizam.
- Detektuj parameter sensitivity, nestabilnost plan cache-a i generic/custom plan efekte prepared statement-a.
- Meri aplikativnu end-to-end latenciju, a ne samo vreme izvrsavanja na serveru.
- Sacuvaj before/after planove i odbij regresije u kriticnim klasama upita.

## Faza P - Indeksi, statistika i write trosak

Svaki indeks mora da sluzi izmerenom access path-u ili invarijanti i opravda trosak odrzavanja.

- Pregledaj redosled kljuceva, selectivity, covering kolone, predicate-e, izraze, collation-e i operator klase.
- Detektuj duple, preklapajuce, nekoriscene, invalid, invisible ili redundant indekse.
- Izmeri insert, update, delete, vacuum ili purge, backup i replication trosak.
- Proveri svezinu statistike, kvalitet uzorka, extended statistics i vidljivost skew-a.
- Pregledaj promene plana nakon osvezavanja statistike, engine patch-a i major nadogradnje.
- Deploy-uj promene indeksa sa lock, disk, replication-lag, cancellation i rollback gate-ovima.

## Faza Q - Storage, bloat, maintenance i kapacitet

Dokazi da rutinski maintenance odrzava strukture podataka zdravim bez krsenja SLO-a.

- Odvojeno meri rast podataka, indeksa, logova, privremenog prostora, undo-a, WAL-a ili binlog-a i backup-a.
- Pregledaj autovacuum ili purge ponasanje, checkpoint-e, flushing, compaction i fragmentaciju gde je primenljivo.
- Modeluj disk headroom za peak write, migration rewrite, index build, backup, restore i failover.
- Pregledaj limite temporary fajlova i spill-a, memoriju po operaciji i aggregate concurrency.
- Proveri da su maintenance job-ovi ograniceni, nadgledani, restartabilni i bezbedni tokom promena topologije.
- Napravi capacity pragove i lead-time alarme pre iscrpljenja resursa.

## Faza R - Particionisanje, sharding i smestaj podataka

Koristi partitioning ili sharding samo za dokazane scale, lifecycle ili isolation potrebe.

- Proveri da partition key odgovara pruning-u, retention-u, uniqueness-u i cestim access pattern-ima.
- Testiraj nedostajuce, buduce, default i prazne particije, kao i granicne timestamp-e i timezone-e.
- Pregledaj globalnu naspram lokalne uniqueness, foreign key-eve, sequence allocation i cross-partition update-e.
- Proveri automatizaciju kreiranja, detach-a, arhiviranja i brisanja particija pod failure i replay uslovima.
- Za sharding definisi routing autoritet, resharding, cross-shard transakciju i reconciliation ponasanje.
- Testiraj hot-shard, unavailable-shard i stale-routing scenarije.

## Faza S - Migracije, backfill i mixed-version kompatibilnost

Tretiraj svaku schema i data promenu kao distribuirano izdanje.

- Pregledaj tacnu DDL semantiku, snagu lock-a, table rewrite, log volume, replication efekat i cancellation ponasanje.
- Koristi expand-and-contract za nekompatibilne promene i dokazi koegzistenciju stare i nove aplikacije.
- Ucini backfill chunked, checkpointed, restartabilnim, idempotentnim, rate-limited i observable.
- Definisi correctness upit, progress metriku, pause, resume, abort i cleanup.
- Testiraj migraciju iz production-like snapshot-a sa realnim data skew-om i paralelnim saobracajem.
- Razdvoji application rollback, schema rollback, data rollback i forward repair; dokazi koji su stvarno bezbedni.

## Faza T - Backup, restore, PITR i verifikacija podataka

Backup-i su samo potencijalni recovery materijal dok restore i verifikacija ne prodju.

- Inventarisi full, incremental, logical, physical, snapshot i log-archive backup-e, retention i immutability.
- Proveri enkripciju, key custody, checksum-e, catalog metadata-u, cross-account ili offsite kopije i deletion protection.
- Izvrsi izolovani restore koristeci dokumentovane kredencijale, mrezu, DNS i aplikativne korake verifikacije.
- Proveri PITR na timestamp neposredno pre i posle poznate transakcije i potvrdi tumacenje timezone-a.
- Validiraj schema-u, opsege broja redova, kriticne invarijante, checksum-e gde imaju smisla i aplikativne smoke testove.
- Izmeri stvarni RPO i RTO i ukljuci queue, object storage, search i configuration recovery zavisnosti.

## Faza U - Replikacija, visoka dostupnost, failover i failback

Replikacija stiti dostupnost, a ne automatski istorijsku oporavljivost.

- Mapiraj replication mode, durability, acknowledgement, lag, slot-ove ili logove, topology manager i split-brain kontrole.
- Proveri konzistentnost replica read-a, read-only enforcement, promotion readiness i rizik writable replike.
- Testiraj planirani switchover, neplanirani failover, network partition, quorum loss i fencing stale primary-ja.
- Proveri client reconnect, DNS ili proxy convergence, transaction uncertainty i idempotent retry.
- Izmeri gubitak podataka i aplikativno error ponasanje prema deklarisanom RPO-u i SLO-u.
- Dokumentuj i testiraj failback, re-seeding, divergence detection i reconciliation.

## Faza V - Autentikacija, autorizacija, tenancy i privilegije

Dokazi least privilege na database, schema, object, row i operativnom sloju.

- Inventarisi login metode, TLS client identitet, IAM autentikaciju, lozinke, sertifikate i service naloge.
- Pregledaj role membership, ownership, default privilegije, grant option, superuser ili administrativne role i public pristup.
- Razdvoji migration, runtime, reporting, backup, replication, monitoring i break-glass identitete.
- Dokazi da tenant predicate i ownership provere ne mogu da se izostave kroz alternativne upite, job-ove, export-e ili support alate.
- Za row-level security eksplicitno testiraj owner, bypass, maintenance i policy-combination ponasanje.
- Loguj i pregledaj privilegovani pristup bez belezenja tajni ili osetljivih query vrednosti.

## Faza W - Enkripcija, tajne, audit, privatnost i retention

Zastiti podatke i kljuceve kroz transit, storage, backup-e, logove i administrativne workflow-e.

- Proveri TLS verzije, hostname validaciju, rotaciju sertifikata i fail-closed ponasanje.
- Proveri enkripciju storage-a, logova, temporary fajlova i backup-a, kao i razdvajanje i opoziv kljuceva.
- Inventarisi tajne u connection string-ovima, parameter group-ama, config fajlovima, image-ima, skriptama i shell istoriji.
- Definisi audit event-e, tamper resistance, retention, pristup i alerting za privilegovane ili osetljive operacije.
- Mapiraj PII, finansijska, zdravstvena, autentikaciona i poverljiva polja sa svrhom, retention, deletion i export pravilima.
- Testiraj deletion, legal hold, anonimizaciju, backup retention i propagaciju u replike ili analytics.

## Faza X - Observability, SLO, kapacitet i trosak

Izgradi monitoring oko korisnicki vidljive ispravnosti i saturation-a resursa, a ne samo server uptime-a.

- Definisi SLI-jeve za dostupnost, query latenciju, transaction success, lock wait, lag, connection wait i recovery freshness.
- Korelisi aplikativni request, transakciju, query fingerprint, database session, deployment i tenant bez curenja podataka.
- Nadgledaj CPU, I/O, memoriju, cache, temporary work, logove, storage, connection pool-ove i background maintenance.
- Napravi alarme sa vlasnikom, severity-jem, obrazlozenjem praga, runbook-om, suppression-om i recovery uslovom.
- Pokreni cold, burst, sustained, soak, failover i degraded-dependency testove sa production-like podacima.
- Prikazi unit economics kao sto su trosak po transakciji, tenant-u, sacuvanoj jedinici, backup-u i zadrzanom logu.

## Faza Y - Incidenti, korupcija i pouzdan oporavak

U incident rezimu daj prednost obuzdavanju, dokazima i trusted stanju u odnosu na kozmeticku dostupnost.

- Klasifikuj slucajno brisanje, logicku korupciju, fizicku korupciju, kompromitovane kredencijale, maliciozni DDL, ransomware i supply-chain kompromitaciju.
- Zaustavi nebezbedne write-ove i izoluj pogodjene endpoint-e bez unistavanja forenzickih dokaza.
- Identifikuj poslednji known-good backup, log chain, schema-u, aplikativni revision, kredencijale i signing trust.
- Restore-uj u izolaciju, validiraj integritet, usaglasi spoljne sisteme i tek onda izvrsi cutover.
- Rotiraj kompromitovane kredencijale i kljuceve, invalidiraj session-e i pregledaj istorijski pristup.
- Uradi root-cause analizu i dodaj kontrole koje detektuju ili sprecavaju ponavljanje.

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

## MariaDB putanja

- Tretiraj MariaDB verziju, storage engine-e, optimizer, replikaciju i autentikaciju kao razlicite od Oracle MySQL-a.
- Proveri tacnu LTS ili rolling liniju, patch, maintenance politiku i podrzanu upgrade putanju.
- Pregledaj InnoDB ili XtraDB lineage, Galera, binary-log i GTID razlike, backup alate i system-versioned tabele.
- Testiraj SQL mode-ove, collation-e, JSON ponasanje, sekvence, generated kolone i optimizer razlike.
- Ne koristi MySQL upgrade checker, Router, Group Replication ili support zakljucke kao MariaDB dokaz.
- Napravi posebne migration i rollback planove za MySQL-to-MariaDB ili MariaDB-to-MySQL prelaze.

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

## Managed i cloud database putanja

- Inventarisi provider-a, service tier, engine kompatibilnost, parameter group-e, ekstenzije, maintenance politiku i regionalne limite.
- Razdvoji vendor control-plane dostupnost od database i aplikativne ispravnosti podataka.
- Proveri retention automatizovanih backup-a, PITR window, cross-region kopije, deletion protection i customer-managed kljuceve.
- Pregledaj forced maintenance, automatske minor nadogradnje, failover ponasanje, DNS TTL, connection proxy i ogranicenja ekstenzija.
- Testiraj quota exhaustion, scaling delay, serverless cold kapacitet, failover i restore u poseban nalog ili projekat.
- Dokumentuj koje kontrole ostaju odgovornost korisnika, ukljucujuci schema-u, role, upite, retention i recovery verifikaciju.

## ORM, query builder i aplikativni data sloj

- Inventarisi svaki ORM, query builder, driver, migration alat i raw SQL escape hatch.
- Proveri generisani SQL, transaction ownership, connection scope, batching, eager ili lazy loading i N+1 dokaze.
- Pregledaj identity map, change tracking, stale entity, optimistic token i bulk-update bypass ponasanje.
- Proveri type mapping-e za decimal, timestamp-e, UUID, JSON, array-e, enum-e, binary i nullable vrednosti.
- Testiraj generisanje migracije na stvarnom engine-u i pregledaj DDL pre izvrsavanja.
- Obezbedi da aplikativna autorizacija i tenant context ne mogu da se zaobidju kroz alternativne repository-je, job-ove, export-e ili admin alate.

## CDC, ETL, analytics i export podataka

- Mapiraj snapshot, log poziciju, schema verziju, ordering, duplicate i delete semantiku za svaki pipeline.
- Testiraj schema evolution, backfill overlap, replay, consumer lag i poison record-e.
- Proveri da se analytics ili search store-ovi ne tretiraju kao autoritativni za write ili autorizaciju.
- Zastiti export-e autorizacijom, tenant scope-om, row limitima, enkripcijom, expiry-jem i auditom.
- Usaglasi source i destination broj redova, agregate, checksum-e gde imaju smisla i kriticne invarijante.
- Definisi cutover i rollback ponasanje kada je pipeline deo migracije.

## Stored procedure, funkcije, trigger-i i server-side kod

Tretiraj server-side kod kao produkcioni aplikativni kod sa privilegijama, lifecycle-om, testovima i deployment rizikom.

- Inventarisi funkcije, procedure, trigger-e, event-e, scheduled rutine, jezike, vlasnike i pozivaoce.
- Pregledaj security-definer ili definer prava, search path ili schema resolution, dinamicki SQL i ownership objekata.
- Proveri da deterministic, volatility i side-effect deklaracije odgovaraju stvarnom ponasanju.
- Testiraj recursion, cascading trigger-e, bulk operacije, replikaciju, restore i putanje sa iskljucenim trigger-ima.
- Version-uj i deploy-uj server-side kod kroz pregledane migracije, a ne kroz ad hoc console izmene.
- Dodaj unit, integration, privilege i rollback testove za kriticne rutine.

## View-ovi, materialized view-ovi, search, spatial i izvedeni podaci

Izvedeni podaci moraju imati eksplicitne freshness, authority, refresh, invalidation i recovery ugovore.

- Inventarisi view-ove, materialized view-ove, indexed view-ove, search indekse, spatial indekse i summary tabele.
- Proveri da ownership i autorizacija nisu oslabljeni definer context-om ili zaobidjenim base-table politikama.
- Definisi freshness SLO, refresh trigger, concurrency mode, failure ponasanje i catch-up proceduru.
- Testiraj schema promene i engine nadogradnje prema sacuvanim definicijama, parser-ima, tokenizer-ima i spatial reference sistemima.
- Usaglasi izvedene agregate i search dokumente sa autoritativnim tabelama.
- Ukljuci vreme rebuild-a izvedenih podataka i storage u RTO i capacity planove.

## Sekvence, identity, generisani kljucevi i distribuirana dodela ID-a

Dokazi uniqueness, exhaustion, ordering i recovery ponasanje svakog generatora identifikatora.

- Inventarisi sekvence, identity kolone, auto-increment, UUID ili ULID generatore, hi-lo allocation i spoljne ID servise.
- Pregledaj cache velicinu, gap-ove, cycling, maksimalnu vrednost, signedness, failover i ponasanje replike.
- Proveri da restore, clone, shard split i kopija okruzenja ne mogu da kreiraju preklapajuce ID opsege.
- Izbegavaj poslovne ordering pretpostavke zasnovane samo na generisanim identifikatorima.
- Testiraj paralelnu dodelu, rollback, retry i bulk import.
- Nadgledaj iscrpljenje i definisi migration plan pre nego sto kapacitet postane kritican.

## Resource governance, timeout-i, cancellation i workload izolacija

Spreci da jedan upit, tenant, izvestaj, migracija ili maintenance zadatak iscrpi deljene resurse.

- Definisi statement, lock, transaction, idle, connection-acquisition i administrativne timeout-e.
- Proveri da client cancellation stize do servera i oslobadja transakcije, lock-ove, memoriju i temporary fajlove.
- Razdvoji OLTP, reporting, migration, backup, CDC i administrativne workload-e gde je potrebno.
- Koristi quota-e, resource group-e, admission control, concurrency cap-ove ili replike uz izmerene tradeoff-e.
- Testiraj maliciozno skupe filtere, sort-ove, join-ove, regex, JSON, full-text i export zahteve.
- Alarmiraj na cancellation failure, runaway session-e, ponovljene timeout-e i workload starvation.

## Major nadogradnje, kompatibilnost i rolling transition

Major engine nadogradnja je aplikativna, data, operativna i recovery migracija, a ne samo promena paketa.

- Inventarisi uklonjeno ponasanje, reserved reci, default-e, collation-e, autentikaciju, ekstenzije, replikaciju i backup kompatibilnost.
- Pokreni vendor checker-e, ali nezavisno testiraj aplikativni SQL, migracije, planove i operativnu automatizaciju.
- Uvezbaj logical, physical, in-place, replica-first ili blue-green putanje sa realnim podacima i merenjem downtime-a.
- Uporedi kriticne planove upita, statistiku, collation rezultate i transaction anomalije pre i posle.
- Dokazi kompatibilnost aplikacije, driver-a, pooler-a, proxy-ja, backup-a i monitoringa.
- Definisi cutover, freeze, abort, rollback ogranicenja, forward repair i post-upgrade validaciju.

## Multi-database i cross-system konzistentnost

Kada poslovni tok obuhvata vise baza ili servisa, dokumentuj odsustvo jedne atomske granice.

- Mapiraj autoritativni sistem za svako polje, objekat i state transition.
- Pregledaj upotrebu distribuiranih transakcija, two-phase commit, retention prepared transakcija i pad koordinatora.
- Preferiraj eksplicitne saga, outbox, inbox i reconciliation ugovore kada globalna atomicnost nije dostupna.
- Testiraj duple, nedostajuce, promenjenog redosleda i zakasnele cross-system event-e.
- Definisi conflict autoritet i manuelni repair za divergentne sisteme.
- Ukljuci stanje spoljnih sistema u rollback, restore i disaster-recovery planiranje.

## Kvalitet podataka, reconciliation i kontinualni integritet

Ispravna schema i uspesni upiti ne dokazuju istorijsku ispravnost podataka.

- Definisi data-quality pravila za opsege, reference, uniqueness, hronologiju, totale i state transition-e.
- Napravi ogranicene reconciliation upite koji mogu bezbedno da rade u produkciji ili na replikama.
- Prati odstupanja sa lineage-om, first-seen vremenom, pogodjenim scope-om, vlasnikom i repair statusom.
- Koristi repair skripte koje su pregledane, idempotentne, checkpointed, auditable i reverzibilne gde je moguce.
- Validiraj totale i invarijante nakon migracije, failover-a, restore-a, queue replay-a i incident recovery-ja.
- Alarmiraj na promene trenda, a ne samo na apsolutni broj nevalidnih redova.

## Test strategija i piramida database verifikacije

Izgradi testove na sloju koji moze da reprodukuje relevantnu engine semantiku i failure mode.

- Koristi unit testove za cisto mapiranje i generisanje SQL-a, a ne kao dokaz engine ponasanja.
- Koristi integration testove na stvarnom produkcionom engine-u i podrzanoj patch porodici.
- Dodaj schema, migration, rollback, seed, permission i tenant-isolation testove.
- Dodaj concurrent transaction, deadlock, retry, idempotency i commit-uncertainty testove.
- Dodaj reprezentativne plan, load, soak, connection-storm i resource-exhaustion testove.
- Dodaj backup, PITR, restore, failover, failback i reconciliation game-day testove.

## Disaster-recovery game day i operativna vezba

Recovery procedure moraju biti izvrsive od strane on-call tima pod vremenskim pritiskom i sa delimicnim informacijama.

- Izaberi realne scenarije kao sto su gubitak regiona, slucajno brisanje, korumpirana migracija, kompromitovani kredencijali ili povratak stale primary-ja.
- Koristi izolovano okruzenje i odobreno rukovanje podacima uz ocuvanje production-like topologije.
- Izmeri vreme detekcije, odluke, pristupa, restore-a, validacije, cutover-a, reconciliation-a i komunikacije.
- Zabelezi svaku nedostajucu dozvolu, nedokumentovanu zavisnost, zastarelu komandu i nejasan ownership.
- Azuriraj runbook-ove, automatizaciju, monitoring, kontakte i obuku na osnovu dokaza.
- Ponavljaj dok izmereni RPO i RTO ne zadovolje deklarisane ciljeve.

## Change governance, review i produkcioni pristup

Database promene zahtevaju jace kontrole jer efekti mogu biti trajni, globalni i tesko reverzibilni.

- Zahtevaj peer review za DDL, destruktivni DML, promene rola, backup politiku, failover automatizaciju i retention promene.
- Koristi immutable pregledane skripte ili migration artefakte sa checksum-ima i environment guard-ovima.
- Razdvoji request, approval, execution i audit identitete za visokorizicne akcije.
- Koristi just-in-time privilegovani pristup, session recording i automatski expiry gde je podrzano.
- Zabrani deljene administrativne naloge i nedokumentovane produkcione console promene.
- Pregledaj emergency promene nakon incidenta i pretvori ih u managed source-controlled stanje.

## Obavezne evidence matrice

| Matrica | Obavezan sadrzaj |
| --- | --- |
| M1 - Identitet | Commit, migration checksum, engine build, paket ili image, endpoint, baza, schema i proces. |
| M2 - Topologija | Primary, replike, proxy-ji, pool-ovi, regioni, read/write rute, failover autoritet i vlasnici. |
| M3 - Schema drift | Source, migracija, catalog, ORM, test schema, grant-ovi, politike i odstupanja. |
| M4 - Invarijante | Invarijanta, enforcement sloj, concurrency test, reconciliation upit i repair vlasnik. |
| M5 - Transakcije | Tok, isolation, lock-ovi, timeout, idempotentnost, spoljni efekti, retry i uncertainty ponasanje. |
| M6 - Upiti | Fingerprint, parametri, planovi, indeksi, statistika, p50/p95/p99, redovi i regression prag. |
| M7 - Konekcije | Klijenti, pool-ovi, maksimumi, timeout-i, session reset, failover i aggregate kapacitet. |
| M8 - Migracija | DDL, lock-ovi, rewrite, log volume, old/new kompatibilnost, backfill, abort i repair. |
| M9 - Bezbednost | Identitet, grant-ovi, tenant kontrole, enkripcija, tajne, audit i negativni testovi. |
| M10 - Backup | Tip backup-a, retention, enkripcija, log chain, restore rezultat, RPO, RTO i aplikativna verifikacija. |
| M11 - HA | Lag, trajnost, promotion, fencing, reconnect, failback, gubitak i reconciliation. |
| M12 - Release readiness | Artefakt, schema, rollout, observability, kapacitet, rollback, forward repair i vlasnici. |

## Obavezni adversarial i failure scenariji

1. Dva paralelna request-a pokusavaju da kreiraju isti logicki unique resurs.
2. Dve transakcije menjaju isti balans, zalihu ili state transition.
3. Klijent dobija timeout neposredno pre ili posle commit-a i ponavlja zahtev.
4. Proces pada nakon database commit-a, ali pre poruke, fajla, cache-a ili HTTP acknowledgement-a.
5. Deadlock ili serialization failure nastaje pod reprezentativnom konkurentnoscu.
6. Duga transakcija blokira vacuum, purge, DDL ili retention rad.
7. Connection pool je iscrpljen dok je baza spora, ali jos prihvata konekcije.
8. Proxy, DNS target ili primary se menja dok su request-i aktivni.
9. Migracija se izvrsava dok stare i nove verzije aplikacije rade paralelno.
10. Backfill je prekinut, restartovan i slucajno pokrenut dva puta.
11. Disk, WAL, binlog, undo, temporary ili backup storage se priblizava iscrpljenju.
12. Replika je promovisana sa lag-om, a stari primary se kasnije vraca.
13. Stale replika opsluzuje authorization-sensitive ili read-after-write zahtev.
14. Backup restore nailazi na nedostajuci ili korumpiran log segment.
15. PITR target se tumaci u pogresnoj timezone ili prelazi daylight-saving promenu.
16. Kredencijal, sertifikat ili encryption key se rotira dok su pool-ovi i replike aktivni.
17. Tenant identifikator je izostavljen iz cache-a, job-a, export-a ili administrativnog upita.
18. Malformed JSON, text encoding, collation ili numeric input stize do kriticnog upita.
19. SQLite otvaraju dve instance aplikacije ili je postavljen na nepouzdan shared storage.
20. Izolovani restore mora da postane novi produkcioni source dok queue-ovi i spoljni sistemi sadrze kasnije efekte.

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

## Workflow popravke i promene

1. Reprodukuj i klasifikuj problem najmanje invazivnim dokazom.
2. Identifikuj prekrsenu invarijantu ili operativni ugovor i najmanji bezbedan kontrolni sloj.
3. Dizajniraj minimalnu popravku i uticaj na migraciju, kapacitet, lock-ove, replikaciju i bezbednost.
4. Dodaj regression test i reconciliation ili integrity upit.
5. Uvezbaj na production-like podacima i stvarnoj engine verziji.
6. Definisi rollout cohort, guardrail-e, abort pragove i vlasnika.
7. Dokazi rollback ili forward repair, ukljucujuci podatke koje je zapisalo novo izdanje.
8. Deploy-uj isti pregledani artefakt ili migraciju bez ad hoc produkcionog menjanja.
9. Posmatraj ispravnost, lock-ove, lag, kapacitet i korisnicki vidljive SLO-e.
10. Zatvori nalaz tek nakon cuvanja dokaza i dokumentacije.

## Production readiness checklist

- Svi kriticni dataset-i, topologije, vlasnici i trust boundary-ji su inventarisani.
- Stvarni engine, patch, edition, ekstenzije, driver-i i support status su provereni.
- Schema source of truth i drift kontrole su definisani.
- Kriticne invarijante se sprovode atomski i imaju reconciliation upite.
- Transaction, isolation, locking, timeout, idempotency i uncertainty ponasanje su testirani.
- Postoje reprezentativni planovi, indeksi, statistika i capacity dokazi.
- Connection pool-ovi i proxy-ji su ograniceni i bezbedni tokom failover-a.
- Migracije i backfill-i su uvezbani sa mixed verzijama i abort gate-ovima.
- Autentikacija, privilegije, tenancy, enkripcija, tajne i audit kontrole su provereni.
- Backup, PITR, restore, aplikativna verifikacija, RPO i RTO su dokazani.
- Failover, fencing stale primary-ja, reconnect, failback i reconciliation su testirani.
- Observability, SLO-i, alarmi, runbook-ovi, capacity i cost guardrail-i su operativni.
- Rollout, rollback, forward repair i incident trusted-recovery planovi imaju vlasnike i testirani su.

## Definition of Done

1. Nijedan nerazresen P0 ili P1 nalaz ne ostaje u release scope-u.
2. Svaki P2 ili prihvaceni P3 ima vlasnika, rok, kompenzujucu kontrolu i preostali rizik.
3. Sve tvrdnje o verzijama i podrsci su ponovo proverene iz zvanicnih primarnih izvora.
4. Kriticno schema, transaction, tenant i recovery ponasanje ima E4 ili E5 dokaz.
5. Migracija i backfill su ponovljivi, observable, pausable, abortable i reconciled.
6. Backup i izabrani PITR target se uspesno restore-uju u izolaciji.
7. Aplikativni smoke testovi i provere poslovnih invarijanti prolaze na restore-ovanim podacima.
8. Failover i rollback ili forward repair ispunjavaju deklarisani SLO, RPO i RTO.
9. Zavrsni izvestaj identifikuje potvrdjene cinjenice, neproverene praznine, preostale rizike i sledece vlasnike.
10. Readiness odluka je `READY`, `READY_WITH_CONDITIONS`, `NOT_READY` ili `INCIDENT`, sa dokazima.

## Zabranjene precice

- Ne dodaj indekse po intuiciji i ne uklanjaj ih samo zato sto brojac kaze da nisu korisceni.
- Ne pokreci `VACUUM FULL`, `OPTIMIZE TABLE`, rebuild, reindex, purge ili shrink kao genericku popravku.
- Ne iskljucuj foreign key-eve, check-ove, row security, strict mode, trajnost ili TLS da bi migracija prosla.
- Ne brisi istoriju migracija, ne menjaj primenjene migracije i ne forsiraj checksum-e bez root-cause analize.
- Ne tretiraj ORM modele, schema dump, repliku, snapshot ili dashboard kao jedinu istinu.
- Ne izvrsavaj produkcioni DDL iz interaktivnog shell-a bez pregledanog artefakta, timeout-a, monitoringa i abort plana.
- Ne tvrdi zero downtime, exactly once, no data loss ili recovery readiness bez failure dokaza.
- Ne kopiraj samo aktivni SQLite glavni fajl u WAL rezimu i ne nazivaj ga proverenim backup-om.

## Format zavrsnog izvestaja

1. Izvrsni rezime i readiness odluka.
2. Potvrdjen source-to-data identitet i topologija.
3. Lifecycle, support i upgrade nalazi.
4. P0-P3 registar nalaza sa nivoima dokaza.
5. Rezultati schema-e, invarijanti, SQL-a, transakcija i konkurentnosti.
6. Rezultati performansi, kapaciteta, maintenance-a i troska.
7. Rezultati bezbednosti, tenancy-ja, privatnosti i audita.
8. Dokazi migracije, backup-a, restore-a, PITR-a, failover-a i reconciliation-a.
9. Implementirane promene sa testovima i artefaktima.
10. Rollout, abort, rollback, forward-repair i incident planovi.
11. Neproverene praznine, preostali rizici, vlasnici i datumi.
12. Dodatak sa redigovanim komandama, planovima, schema-ma, matricama i restore zapisima.

## Redosled rada

1. Procitaj zajednicke core ugovore i ovaj prompt.
2. Utvrdi scope, ovlascenje, rezim, engine putanje i stop uslove.
3. Zastiti podatke i sacuvaj dokaze.
4. Napravi source-to-data identitet, topologiju i ownership mape.
5. Audituj schema-u, invarijante, SQL, transakcije, lock-ove i idempotentnost.
6. Audituj planove, indekse, statistiku, storage, maintenance i kapacitet.
7. Audituj bezbednost, tenancy, privatnost, backup-e, replikaciju i recovery.
8. Primeni kompletne aktivne PostgreSQL, MySQL, MariaDB, SQLite i cloud putanje.
9. Pokreni obavezne matrice i adversarial scenarije.
10. Implementiraj samo potvrdjene bezbedne promene i sacuvaj dokaze.
11. Uvezbaj rollout, abort, rollback ili forward repair i isolated restore.
12. Isporuci zavrsni izvestaj i readiness odluku potkrepljenu dokazima.

