## Rezim Rada

Ako nije eksplicitno zadat, koristi `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeni rad |
| --- | --- |
| `AUDIT_ONLY` | Analiziraj i testiraj bez izmene source-a, konfiguracije, dependency-ja ili infrastrukture; isporuci konkretne izmene i roadmap. |
| `AUDIT_AND_SAFE_FIX` | Implementiraj samo potvrdjene lokalne, bezbedne, niskorizicne popravke. Za destruktivne migracije, velike arhitektonske promene i javne ugovore napravi plan. |
| `FULL_IMPLEMENTATION` | Implementiraj potvrdjene popravke i opravdana unapredjenja, ali ne radi destruktivne operacije bez backup/rollback strategije; razbij velike izmene na proverljive korake. |
| `FIX_CONFIRMED_ISSUES` | Ne siri scope; popravi samo prethodno potvrdjene probleme, dodaj testove i pokreni relevantni regresioni opseg. |

