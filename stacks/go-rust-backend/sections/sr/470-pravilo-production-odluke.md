## Pravilo production odluke

- Vrati tačno jednu ocenu: `READY`, `READY_WITH_CONDITIONS`, `NOT_READY` ili `INCIDENT_CONTAINMENT_REQUIRED`.
- Ocena `READY` zahteva zatvorene primenljive P0 i P1 nalaze, kompletne obavezne matrice, uspešne kritične scenarije, proveren immutable artefakt, dokazan rollout i rollback i restore dokaz koji ispunjava odobren RPO/RTO.
- Koristi `READY_WITH_CONDITIONS` samo kada svaki uslov ima vlasnika, rok, containment, merljiv acceptance kriterijum i nema skrivenu P0/P1 izloženost.
- Svaki nerešen kritični authorization, data-integrity, memory-safety, concurrency, migration, supply-chain, rollback ili restore rizik blokira bezuslovnu ready ocenu.

