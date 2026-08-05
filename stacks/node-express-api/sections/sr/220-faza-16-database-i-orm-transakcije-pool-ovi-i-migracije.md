## Faza 16 - Database-i, ORM, Transakcije, Pool-ovi I Migracije

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Proveri stvarni database, driver, ORM ili query builder, verzije, topologiju, replike, proxy-je i consistency model.
- Audituj schema constraint-e, indexe, foreign key-eve, uniqueness, check-ove, default-e, precision, time zone i collation.
- Pregledaj stvarni generisani SQL, parameterization, planove, cardinality, lock-ove i production-like distribuciju podataka.
- Mapiraj transaction granice, isolation, timeout, retry, deadlock obradu i side effect-e van transakcije.
- Dimenzionisi connection pool-ove prema replikama, serverless concurrency-ju, worker-ima, database limitima i failover ponasanju.
- Koristi expand-and-contract migracije sa kompatibilnim overlap-om, bounded backfill-om, verifikacijom, cutover-om i forward repair-om.

### Obavezni Dokazi

- Proizvedi i sacuvaj schema, query, transaction i pool matricu.
- Proizvedi i sacuvaj migration compatibility i ownership plan.
- Proizvedi i sacuvaj restore, PITR i data-integrity dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da konkurentni write-ovi cuvaju database constraint-e.
- Dokazi da pool exhaustion otkazuje sa ogranicenom latency.
- Dokazi da old i new binary-ji bezbedno koegzistiraju tokom migracije.

