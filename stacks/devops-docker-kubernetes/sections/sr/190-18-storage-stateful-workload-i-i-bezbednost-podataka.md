## 18. Storage, stateful workload-i i bezbednost podataka

**Cilj:** Zastiti perzistenciju, konzistentnost, trajnost i oporavak tokom normalnih i neuspesnih operacija.

### 18.1 Obavezne provere

1. Popisi storage class-e, CSI driver-e, tipove volume-a, access mode-ove, topologiju, encryption, snapshot-e, reclaim policy, expansion, kvote, performance tier-e i vlasnistvo.
2. Proveri StatefulSet identitet, redosled, persistent-volume claim-ove, rescheduling, zone affinity, failover, fencing, sprecavanje split-brain-a i pretpostavke data locality-ja.
3. Audituj baze, redove, cache-eve, object store-ove, search sisteme i operator-e za replikaciju, quorum, konzistentnost, trajnost, compaction, retention, obradu korupcije i podrzane verzije.
4. Razdvoji dostupnost aplikacije od ispravnosti podataka. Proveri duplu isporuku, redosled, idempotency, transakcije, kompatibilnost seme i delimican otkaz.
5. Proveri expand-and-contract strategiju migracije, backward i forward kompatibilnost, lock uticaj, rollback ogranicenja, backup-e i odobrenje vlasnika.
6. Testiraj otkaz attach-a volume-a, pun disk, IOPS ili throughput throttling, izgubljen node, izgubljenu zonu, replica lag, detekciju korupcije i izolovani oporavak.
7. Proveri zastitu od brisanja, finalizer-e, reclaim ponasanje, vlasnistvo snapshot-a, ciscenje orphan resursa i zahteve unistavanja podataka.

### 18.2 Minimalni dokazi

- Mapa topologije, konzistentnosti i vlasnistva stateful sistema.
- Rezultati testova migracije, failover-a, korupcije, kapaciteta i oporavka.
- Dokazi brisanja, retention-a, snapshot-a i unistavanja podataka.

### 18.3 Kriterijumi izlaza

1. Kriticni data sistemi imaju dokazano ponasanje konzistentnosti, kapaciteta, failover-a, backup-a i oporavka.
2. Izmene seme i podataka imaju kompatibilan rollout i eksplicitan rollback ili compensating plan.
3. Nijedna destruktivna reclaim, deletion ili orphan putanja nije nekontrolisana.

