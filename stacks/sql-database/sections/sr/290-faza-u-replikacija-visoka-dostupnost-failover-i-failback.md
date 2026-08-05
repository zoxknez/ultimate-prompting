## Faza U - Replikacija, visoka dostupnost, failover i failback

Replikacija stiti dostupnost, a ne automatski istorijsku oporavljivost.

- Mapiraj replication mode, durability, acknowledgement, lag, slot-ove ili logove, topology manager i split-brain kontrole.
- Proveri konzistentnost replica read-a, read-only enforcement, promotion readiness i rizik writable replike.
- Testiraj planirani switchover, neplanirani failover, network partition, quorum loss i fencing stale primary-ja.
- Proveri client reconnect, DNS ili proxy convergence, transaction uncertainty i idempotent retry.
- Izmeri gubitak podataka i aplikativno error ponasanje prema deklarisanom RPO-u i SLO-u.
- Dokumentuj i testiraj failback, re-seeding, divergence detection i reconciliation.

