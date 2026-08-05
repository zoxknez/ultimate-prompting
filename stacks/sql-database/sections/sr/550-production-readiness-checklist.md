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

