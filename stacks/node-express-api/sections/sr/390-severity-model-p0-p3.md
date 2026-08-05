## Severity Model P0-P3

| Severity | Definicija | Ocekivana akcija |
| --- | --- | --- |
| P0 | Aktivno kompromitovanje, cross-tenant disclosure, RCE, kritican authorization bypass, nepovratna korupcija, izlaganje produkcione tajne ili destruktivno izdanje. | Odmah uradi containment, sacuvaj dokaz, opozovi ili izoluj, restore-uj ili reconcile-uj i pokreni incident command. |
| P1 | Visoko verovatan auth, integrity, race, idempotency, event-loop, exhaustion, migration, supply-chain ili recovery kvar. | Blokiraj izdanje ili kritican traffic dok se ne popravi ili eksplicitno contain-uje sa owner-om i rokom. |
| P2 | Materijalan ali lokalizovan correctness, performance, observability, compatibility ili maintainability rizik. | Planiraj i proveri popravku u ogranicenom izdanju sa regression zastitom. |
| P3 | Low-risk cleanup, dokumentacija, konzistentnost, naming ili malo unapredjenje. | Resi oportunisticki bez skretanja paznje sa rada veceg rizika. |

