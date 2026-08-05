## 8. Faza D - Zivotni Ciklus Podataka, Privatnost I Governance

1. Popisi prikupljene, generisane, retrieved, izvedene, kesirane, logovane, evaluirane, eksportovane i obrisane podatke.
2. Gde je primenjivo utvrdi namenu, pravni osnov ili organizaciono ovlascenje, retention, lokaciju, subprocessore i access kontrole.
3. Proveri provider data-use, training, retention, zero-retention, regional-processing i abuse-monitoring podesavanja prema aktuelnoj provider dokumentaciji i ugovornim uslovima.
4. Spreci ulazak osetljivih podataka u promptove, traces, eval dataset-e, analytics, support ticket-e i debug logove osim kada je eksplicitno potrebno i zasticeno.
5. Proveri redaction, tokenization, enkripciju, key management, delete propagation, legal hold i backup ponasanje.
6. Proveri da user ili data-subject zahtevi mogu obuhvatiti primarna skladista, vector index-e, cache, memoriju, fine-tuning podatke i izvedene artefakte.
7. Testiraj memory poisoning, neautorizovane izmene profila i obradu izvedenih osetljivih atributa.
8. Proveri poreklo dataset-a, licence, pristanak, kvalitet i contamination kontrole.
9. Napravi matricu retention-a i brisanja podataka.

