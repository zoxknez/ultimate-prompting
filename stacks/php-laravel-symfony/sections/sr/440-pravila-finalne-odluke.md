## Pravila finalne odluke

| Odluka | Obavezan uslov |
| --- | --- |
| READY | Nema nerešenog P0 ili P1, sve kritične putanje su dokazane, sve obavezne kontrole prolaze i rollback i restore su testirani. |
| READY_WITH_CONDITIONS | Nema P0, nema neprihvaćenog P1, preostali ograničeni rizici imaju owner-e, rokove, monitoring, compensating kontrole i expiry. |
| NOT_READY | Ostaje release blocker, nepoznata kritična putanja, nepodržana kritična komponenta, neuspešan recovery dokaz ili materijalni rizik bez owner-a. |
| INCIDENT | Aktivni compromise, nebezbedna integrity neizvesnost, destruktivni kvar ili je potreban immediate containment i trusted rebuild. |

