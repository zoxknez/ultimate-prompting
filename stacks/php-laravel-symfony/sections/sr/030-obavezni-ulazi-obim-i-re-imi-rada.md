## Obavezni ulazi, obim i režimi rada

### Obavezni ulazi

| Polje | Obavezna vrednost |
| --- | --- |
| Repozitorijum i revizija | [PUTANJA/URL, branch, commit, dirty state] |
| Poslovna svrha i kritične invarijante | [AKTERI, NOVAC, INVENTAR, PRAVA, TENANTI, SAGLASNOST] |
| Ulazne tačke | [HTTP, CLI, QUEUE, SCHEDULER, MIGRATOR, REALTIME, WEBHOOK] |
| Framework i runtime | [PLAIN PHP, LARAVEL, SYMFONY, FPM, OCTANE, FRANKENPHP, ROADRUNNER, SWOOLE] |
| Identitet i tenancy | [SESSION, JWT, OIDC, API KEY, SERVICE IDENTITY, ULOGE, TENANTI] |
| Podaci i side effect-i | [DATABASE, ORM, CACHE, QUEUE, FILES, PAYMENT, EMAIL, SEARCH] |
| Deployment i topologija | [VM, CONTAINER, KUBERNETES, SERVERLESS, MULTI-REGION] |
| Operativni ciljevi | [SLO, RPO, RTO, PRIVATNOST, USKLAĐENOST, TROŠAK, KAPACITET] |

### Režimi rada

| Režim | Dozvoljeni obim |
| --- | --- |
| AUDIT_ONLY | Pregledaj i izvrši bezbedne provere bez menjanja source-a, lockfile-a, šeme, infrastrukture ili produkcionog stanja. |
| AUDIT_AND_SAFE_FIX | Primeni male reverzibilne popravke sa fokusiranim regresionim testovima i bez produkcionih side effect-a. |
| FULL_IMPLEMENTATION | Implementiraj opravdane promene sa planovima migracije, rollout-a, rollback-a i monitoringa. |
| FIX_CONFIRMED_ISSUES | Menjaj samo izabrane potvrđene nalaze i sačuvaj nepovezano ponašanje. |
| SECURITY_AND_CONCURRENCY_AUDIT | Daj prioritet auth-u, autorizaciji, tenancy-ju, injection-u, race-u, idempotency-ju, worker-ima, resursima i supply chain-u. |
| PERFORMANCE_AND_RELIABILITY_AUDIT | Daj prioritet latency-ju, memoriji, FPM saturaciji, queue lag-u, dugovečnom stanju, overload-u, shutdown-u, failover-u i oporavku. |
| INCIDENT_AND_RECOVERY | Obuzdaj kompromitovanje, sačuvaj dokaze, rotiraj tajne, proveri integritet, vrati stanje, uskladi podatke i ojačaj sistem. |

### Bezbednosno zaustavljanje

- Podrazumevaj AUDIT_AND_SAFE_FIX osim ako je drugi režim eksplicitno izabran.
- Zaustavi se pre destruktivnih promena šeme, produkcionih upisa, rotacije tajni, promena saobraćaja, čišćenja reda, cache flush-a, restart-a worker-a ili izdanja osim ako su eksplicitno odobreni.
- Nikada ne briši necommitovan rad, ne prepisuj istoriju, ne koristi force-push i ne koristi produkcione kredencijale u lokalnim ili CI testovima.
- Preferiraj disposable okruženja, fixtures, read-only replike, lažne provajdere, izolovane queue namespace-ove i izolovane restore ciljeve.
- Ne prikazuj vrednosti tajni, raw tokene, cookie-je, privatne ključeve, APP_KEY, Symfony secrets, session payload-e ili osetljive lične podatke.

