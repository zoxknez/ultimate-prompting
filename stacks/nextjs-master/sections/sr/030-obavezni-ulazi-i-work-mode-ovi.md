## Obavezni ulazi i work mode-ovi

### Obavezni ulazi

| Polje | Obavezna vrednost |
| --- | --- |
| Repozitorijum i branch | [URL/PATH, branch, commit, dirty state] |
| Kriticni tokovi | [PUBLIC, AUTH, CHECKOUT, ACCOUNT, ADMIN, API, OTHER] |
| Router i rendering | [APP ROUTER / PAGES / MIXED / STATIC EXPORT] |
| Hosting | [VERCEL / NODE / CONTAINER / EDGE / ADAPTER / HYBRID] |
| Identitet i tenancy | [AUTH, SESSION, ROLES, TENANTS, ADMIN, IMPERSONATION] |
| Podaci i side effect-i | [DATABASE, ORM, CACHE, QUEUE, FILES, PAYMENT, EMAIL, SEARCH] |
| Operativni ciljevi | [SLO, RPO, RTO, PRIVACY, ACCESSIBILITY, COMPLIANCE] |
| Poznata ogranicenja | [INCIDENTS, DEADLINES, CHANGE FREEZE, DATA SAFETY] |

### Work mode-ovi

| Mode | Dozvoljeni scope |
| --- | --- |
| AUDIT_ONLY | Citaj, pregledaj, izvrsi bezbedne provere i izvesti bez izmene source-a, lockfile-a, scheme ili okruzenja. |
| AUDIT_AND_SAFE_FIX | Primeni male reverzibilne popravke sa ciljanim regresionim testovima i bez produkcionih side effect-a. |
| FULL_IMPLEMENTATION | Implementiraj opravdane promene u kontrolisanim koracima sa migration, rollout, rollback i observability planovima. |
| FIX_CONFIRMED_ISSUES | Menjaj samo izabrane potvrdjene nalaze i sacuvaj nepovezano ponasanje. |

### Safety stop

- Podrazumevano koristi AUDIT_AND_SAFE_FIX osim kada je drugi mode eksplicitno izabran.
- Zaustavi se pre destruktivnih schema promena, produkcionih write operacija, rotacije tajni, nepovratnog purge-a, DNS promene ili release-a osim ako su eksplicitno odobreni.
- Nikada ne brisi necommit-ovan rad, ne prepisuj istoriju, ne koristi force-push i ne koristi produkcione kredencijale u lokalnim testovima.
- Daj prednost disposable okruzenjima, fixture-ima, read-only replikama, mock provider-ima i izolovanim restore ciljevima.

