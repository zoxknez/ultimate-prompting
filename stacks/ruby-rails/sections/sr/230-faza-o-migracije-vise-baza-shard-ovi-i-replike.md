## Faza O - Migracije, Vise Baza, Shard-ovi I Replike

- Popisi primary, replica, shard, queue, cache i cable baze i identifikuj vlasnistvo migracija za svaku.
- Koristi expand-and-contract za destruktivne izmene i dokazi da stare i nove verzije aplikacije mogu koegzistirati.
- Odvoji schema migraciju, data backfill, verifikaciju, cutover i cleanup u posmatrane restartabilne korake.
- Proveri trajanje lock-a, statement timeout, metod kreiranja indeksa, rizik table rewrite-a i replication lag.
- Testiraj read-after-write ponasanje, role switching, replica lag, shard routing, tenant move i failover.
- Ne pokreci migracije automatski sa svake web replike. Uspostavi jednog kontrolisanog vlasnika migracije.

