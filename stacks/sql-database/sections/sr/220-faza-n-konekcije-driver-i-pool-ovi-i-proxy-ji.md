## Faza N - Konekcije, driver-i, pool-ovi i proxy-ji

Dokazi da connection kapacitet i session stanje ostaju bezbedni pod peak i failure uslovima.

- Inventarisi driver verziju, protocol opcije, TLS, prepared statement-e, timezone, encoding i failover ponasanje.
- Izracunaj ukupan moguci broj konekcija kroz procese, replike, worker-e, job-ove, admin alate i failover overlap.
- Proveri pool acquisition timeout, idle timeout, lifetime, validation i leak detection.
- Resetuj session state, rolu, tenant, search path, transaction podesavanja i privremene objekte pre ponovne upotrebe.
- Pregledaj PgBouncer, ProxySQL, MySQL Router, RDS Proxy ili custom proxy ogranicenja transakcija i prepared statement-a.
- Load-testiraj failover, DNS promenu, stale konekcije, connection storm i restart baze.

