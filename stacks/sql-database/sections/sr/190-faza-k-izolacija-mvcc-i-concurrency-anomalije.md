## Faza K - Izolacija, MVCC i concurrency anomalije

Dokazi ponasanje na konfigurisanom isolation nivou za stvarni engine.

- Testiraj lost update, write skew, nonrepeatable read, phantom, read skew i stale replica read gde je primenljivo.
- Zabelezi engine default-e i session ili transaction override-e.
- Proveri optimistic concurrency tokene, affected-row provere i retry semantiku.
- Proveri obradu serializable failure-a i ogranicene retry pokusaje sa svezim transaction stanjem.
- Testiraj read-after-write i monotonic-read zahteve kroz primary i replike.
- Ne prenosi nazive isolation nivoa izmedju PostgreSQL-a, InnoDB-a i SQLite-a bez testiranja stvarne semantike.

