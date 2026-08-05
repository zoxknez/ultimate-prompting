## 28. Severity i production odluka
| Nivo | Definicija | Uticaj na izdanje |
| --- | --- | --- |
| P0 | Aktivna kompromitacija, ozbiljan gubitak integriteta podataka, nebezbedan signing ili update put, masovno cross-tenant izlaganje, nepopravljiv kritican kvar ili neposredan rizik po korisnika. | Odmah zaustavi izdanje ili udji u incident rezim. |
| P1 | Verovatan kritican bezbednosni, privacy, finansijski, availability, store, migration ili rollback kvar sa materijalnim uticajem. | Blokiraj izdanje do popravke ili formalnog containment-a sa odobrenim dokazom. |
| P2 | Materijalan defekt, nepodrzana konfiguracija, performance, accessibility, observability ili operativna slabost. | Popravi pre sirokog rollout-a ili prihvati sa vlasnikom, rokom, kompenzacionom kontrolom i monitoring-om. |
| P3 | Ograniceno poboljsanje, maintainability problem, optimizacija, dokumentacioni propust ili opciona modernizacija. | Prioritizuj prema vrednosti i riziku; samostalno ne blokira izdanje. |

Konacna odluka mora biti tacno jedna od: READY, READY_WITH_CONDITIONS, NOT_READY ili INCIDENT.

