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

