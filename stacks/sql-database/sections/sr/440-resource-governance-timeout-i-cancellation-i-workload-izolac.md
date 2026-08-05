## Resource governance, timeout-i, cancellation i workload izolacija

Spreci da jedan upit, tenant, izvestaj, migracija ili maintenance zadatak iscrpi deljene resurse.

- Definisi statement, lock, transaction, idle, connection-acquisition i administrativne timeout-e.
- Proveri da client cancellation stize do servera i oslobadja transakcije, lock-ove, memoriju i temporary fajlove.
- Razdvoji OLTP, reporting, migration, backup, CDC i administrativne workload-e gde je potrebno.
- Koristi quota-e, resource group-e, admission control, concurrency cap-ove ili replike uz izmerene tradeoff-e.
- Testiraj maliciozno skupe filtere, sort-ove, join-ove, regex, JSON, full-text i export zahteve.
- Alarmiraj na cancellation failure, runaway session-e, ponovljene timeout-e i workload starvation.

