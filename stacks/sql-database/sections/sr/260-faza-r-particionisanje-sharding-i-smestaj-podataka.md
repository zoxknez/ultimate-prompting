## Faza R - Particionisanje, sharding i smestaj podataka

Koristi partitioning ili sharding samo za dokazane scale, lifecycle ili isolation potrebe.

- Proveri da partition key odgovara pruning-u, retention-u, uniqueness-u i cestim access pattern-ima.
- Testiraj nedostajuce, buduce, default i prazne particije, kao i granicne timestamp-e i timezone-e.
- Pregledaj globalnu naspram lokalne uniqueness, foreign key-eve, sequence allocation i cross-partition update-e.
- Proveri automatizaciju kreiranja, detach-a, arhiviranja i brisanja particija pod failure i replay uslovima.
- Za sharding definisi routing autoritet, resharding, cross-shard transakciju i reconciliation ponasanje.
- Testiraj hot-shard, unavailable-shard i stale-routing scenarije.

