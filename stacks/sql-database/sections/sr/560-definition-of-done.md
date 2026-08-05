## Definition of Done

1. Nijedan nerazresen P0 ili P1 nalaz ne ostaje u release scope-u.
2. Svaki P2 ili prihvaceni P3 ima vlasnika, rok, kompenzujucu kontrolu i preostali rizik.
3. Sve tvrdnje o verzijama i podrsci su ponovo proverene iz zvanicnih primarnih izvora.
4. Kriticno schema, transaction, tenant i recovery ponasanje ima E4 ili E5 dokaz.
5. Migracija i backfill su ponovljivi, observable, pausable, abortable i reconciled.
6. Backup i izabrani PITR target se uspesno restore-uju u izolaciji.
7. Aplikativni smoke testovi i provere poslovnih invarijanti prolaze na restore-ovanim podacima.
8. Failover i rollback ili forward repair ispunjavaju deklarisani SLO, RPO i RTO.
9. Zavrsni izvestaj identifikuje potvrdjene cinjenice, neproverene praznine, preostale rizike i sledece vlasnike.
10. Readiness odluka je `READY`, `READY_WITH_CONDITIONS`, `NOT_READY` ili `INCIDENT`, sa dokazima.

