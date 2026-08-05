## Faza Q - Storage, bloat, maintenance i kapacitet

Dokazi da rutinski maintenance odrzava strukture podataka zdravim bez krsenja SLO-a.

- Odvojeno meri rast podataka, indeksa, logova, privremenog prostora, undo-a, WAL-a ili binlog-a i backup-a.
- Pregledaj autovacuum ili purge ponasanje, checkpoint-e, flushing, compaction i fragmentaciju gde je primenljivo.
- Modeluj disk headroom za peak write, migration rewrite, index build, backup, restore i failover.
- Pregledaj limite temporary fajlova i spill-a, memoriju po operaciji i aggregate concurrency.
- Proveri da su maintenance job-ovi ograniceni, nadgledani, restartabilni i bezbedni tokom promena topologije.
- Napravi capacity pragove i lead-time alarme pre iscrpljenja resursa.

