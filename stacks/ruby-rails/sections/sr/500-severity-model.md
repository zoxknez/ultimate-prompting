## Severity Model

| Prioritet | Definicija | Primeri |
| --- | --- | --- |
| P0 | Aktivna eksploatacija, cross-tenant pristup, RCE, kompromitacija credential-a, gubitak podataka ili neoporavljivo production stanje. | Authorization bypass, zlonamerna deserializacija, procureli master key, destruktivna migracija bez oporavka. |
| P1 | Verovatan outage, krsenje kriticne invarijante, dupli nepovratni efekat, nebezbedan rollout ili velika security slabost. | Dupli payment job, pool exhaustion, stale authorization cache, nebezbedna Active Storage obrada. |
| P2 | Materijalna reliability, performance, observability, maintainability ili recovery slabost sa ogranicenim uticajem. | Izmeren N+1, rast memorije, slabe queue metrike, netestiran failover. |
| P3 | Niskorizicna higijena, dokumentacija, stil ili developer-experience problem. | Manja upozorenja, naming, nedostajuca nekriticna dokumentacija. |

