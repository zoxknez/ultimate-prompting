## Obavezni Ulazi, Scope I Rezim Rada

### Obavezni Ulazi

| Polje | Obavezna vrednost |
| --- | --- |
| Repozitorijum i revizija | [PATH/URL, branch, commit, dirty state] |
| Poslovna svrha i kriticne invarijante | [TOKOVI, AKTERI, NOVAC, INVENTAR, PRAVA, TENANTI] |
| Executable-i i entrypoint-i | [API, WORKER, CRON, CLI, MIGRATOR, REALTIME, WEBHOOK] |
| Framework i protocol povrsina | [EXPRESS, FASTIFY, DRUGO, HTTP1, HTTP2, SSE, WS, GRPC] |
| Identitet i tenancy | [SESSION, JWT, OIDC, API KEY, SERVICE IDENTITY, ROLE, TENANTI] |
| Podaci i side effect-i | [DATABASE, ORM, CACHE, QUEUE, FAJLOVI, PAYMENT, EMAIL, SEARCH] |
| Deployment i topologija | [VM, CONTAINER, KUBERNETES, SERVERLESS, MULTI-REGION] |
| Operativni ciljevi | [SLO, RPO, RTO, PRIVACY, COMPLIANCE, COST, CAPACITY] |

### Rezim Rada

| Rezim | Dozvoljeni scope |
| --- | --- |
| AUDIT_ONLY | Pregledaj i izvrsi bezbedne provere bez promene source-a, lockfile-a, scheme, infrastrukture ili produkcionog stanja. |
| AUDIT_AND_SAFE_FIX | Primeni male reverzibilne popravke sa fokusiranim regression testovima i bez production side effect-a. |
| FULL_IMPLEMENTATION | Implementiraj opravdane promene sa migration, rollout, rollback i monitoring planovima. |
| FIX_CONFIRMED_ISSUES | Menjaj samo izabrane potvrdjene nalaze i sacuvaj nepovezano ponasanje. |
| SECURITY_AND_CONCURRENCY_AUDIT | Prioritizuj auth, autorizaciju, tenancy, injection, race, idempotency, event-loop, resurse i supply chain. |
| PERFORMANCE_AND_RELIABILITY_AUDIT | Prioritizuj latency, event-loop delay, memoriju, saturaciju, overload, shutdown, failover i oporavak. |

### Safety Stop

- Koristi AUDIT_AND_SAFE_FIX kao default osim ako je eksplicitno izabran drugi rezim.
- Zaustavi se pre destruktivnih schema promena, produkcionih write operacija, rotacije tajni, traffic promena, queue purge-a ili izdanja osim kada je eksplicitno odobreno.
- Nikada ne brisi necommit-ovan rad, ne prepisuj istoriju, ne radi force-push i ne koristi produkcione kredencijale u lokalnim ili CI testovima.
- Preferiraj disposable okruzenja, fixture-e, emulatore, read-only replike, mock provider-e i izolovane restore ciljeve.
- Ne ispisuj vrednosti tajni, raw token-e, cookie-je, privatne kljuceve ili osetljive licne podatke.

