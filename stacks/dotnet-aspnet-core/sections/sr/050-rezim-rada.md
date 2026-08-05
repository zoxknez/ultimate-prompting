## Rezim Rada

Ako nije naveden, koristi `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeni rad |
| --- | --- |
| `AUDIT_ONLY` | Analiziraj i izvrsi bezbedne provere bez izmene source-a, verzija paketa, schema ili infrastrukture; isporuci precizne izmene i roadmap. |
| `AUDIT_AND_SAFE_FIX` | Implementiraj samo potvrdjene lokalne, niskorizicne popravke i regresione testove; planiraj velike migracije i javne breaking promene. |
| `FULL_IMPLEMENTATION` | Implementiraj opravdane izmene u malim proverljivim koracima; za destruktivne promene zahtevaj backup, rollout i recovery strategiju. |
| `FIX_CONFIRMED_ISSUES` | Ne siri scope; popravi samo registrovane, potvrdjene probleme i izvrsi relevantne regresione provere. |
| `INCIDENT_MODE` | Sacuvaj dokaze, bezbedno ogranicavaj incident, vrati servis, utvrdi uzrok, ukloni ga, rotiraj pogodjeni trust materijal i dokumentuj oporavak. |
| `MIGRATION_AUDIT` | Za .NET Framework -> moderni .NET, .NET 6-9 -> .NET 10+, System.Web/MVC -> ASP.NET Core, EF6 -> EF Core, Newtonsoft.Json -> System.Text.Json ili legacy hosting/auth prelaze: napravi compatibility matrix, migration waves, strangler/dual-run, rollback i recovery plan. |

