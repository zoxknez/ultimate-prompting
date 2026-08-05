# Revizija 09 - Next.js / React / TypeScript Production Audit Prompt

Datum revizije: 5. avgust 2026.

## Rezime

Postojeci Next.js par bio je uskladjen izmedju engleske i srpske verzije, ali je predstavljao prosirenu checklist-u, a ne potpun production audit ugovor.

Glavni problemi pre revizije:

- prompt je imao samo 233 linije i 27 Markdown naslova po jeziku;
- nije postojao YAML frontmatter sa identitetom, verzijom i evidence modelom;
- nije postojao formalni E0-E5 model nivoa dokaza;
- source commit, lockfile, build output, deployment i runtime nisu bili povezani u jedan dokazni lanac;
- Server Components i Client Components nisu imali dovoljno precizan trust, bundle i serialization audit;
- RSC payload, React Server Functions i bezbednosni advisory-ji nisu imali obaveznu patch i regression proceduru;
- Cache Components, `use cache`, private/remote cache, CDN, browser cache i service worker nisu bili objedinjeni u jednu privacy i invalidation matricu;
- Server Actions nisu imali dovoljno detaljan idempotency, transaction, encryption-key i multi-instance ugovor;
- Proxy/Middleware nije bio dovoljno jasno odvojen od stvarne autorizacije na data i mutation granici;
- Vercel, Node self-hosting, container-i, Edge runtime i third-party adapter-i nisu bili tretirani kao razliciti runtime proizvodi;
- version skew izmedju starog browser taba, novih asset-a, starih server instance-i, Server Actions i service worker-a nije bio sistematski obradjen;
- nisu postojale standardizovane evidence matrice, failure scenariji, recovery dokazi i strogo finalno decision pravilo.

## Stanje pre revizije

| Metrika | EN | SR |
| --- | ---: | ---: |
| Linije | 233 | 233 |
| Markdown naslovi | 27 | 27 |
| Verzija | bez 2.0 frontmatter ugovora | bez 2.0 frontmatter ugovora |
| Heading paritet | prosao | prosao |

## Stanje posle revizije

| Metrika | EN | SR |
| --- | ---: | ---: |
| Linije | 985 | 985 |
| Markdown H1-H3 naslovi van code fence blokova | 131 | 131 |
| Verzija | 2.0.0 | 2.0.0 |
| Heading paritet | prosao | prosao |
| Line-shape paritet | 0 odstupanja | 0 odstupanja |

## Formalni evidence model

Uvedeni su nivoi:

- E0 - tvrdnja, ticket, roadmap ili pretpostavka;
- E1 - staticki source, konfiguracija, schema ili dependency deklaracija;
- E2 - resolved graph, generisani izlaz, route manifest, build artefakt, digest ili SBOM;
- E3 - izvrseni lokalni, integration, production-build ili browser dokaz;
- E4 - staging ili production-like load, failure, rollout ili rollback dokaz;
- E5 - produkcijsko posmatranje, izolovani restore ili incident drill.

READY vise nije moguc samo na osnovu source pregleda, zelenog CI-ja, `next build`, unit testova, Lighthouse rezultata ili zelenog platform dashboard-a.

## Source-to-runtime identitet

Novi prompt zahteva korelaciju:

1. repozitorijuma, branch-a, commit-a i dirty state-a;
2. Node.js binary-ja, arhitekture, libc-a, native ABI-ja i package manager-a;
3. lockfile digest-a, resolved dependency graph-a, patch-eva, lifecycle skripti i generated output-a;
4. Next.js build output-a, route manifest-a, function bundle-ova, static asset-a i source map-a;
5. artefakta ili image digest-a, deployment revizije i deployment ID-ja;
6. efektivne konfiguracije, feature flag-ova, regiona, runtime-a, schema verzije i cache namespace-a;
7. pokrenutog procesa, logova, trace-ova, error report-a i browser-visible release identiteta.

Mutable tag ili rebuild izmedju okruzenja vise nisu prihvatljivi kao dokaz da se promovise isti release.

## Build, TypeScript i supply-chain audit

Dodato je:

- razlikovanje lokalnog, CI, preview i produkcionog Node.js runtime-a;
- provera Corepack politike, vlasnika lockfile-a, frozen install-a, peer dependency-ja i hoisting modela;
- audit lifecycle i postinstall skripti, binary download-a, Git/path dependency-ja i registry konfiguracije;
- dependency confusion, typosquatting, compromised maintainer, unmaintained package i reachable vulnerability analiza;
- native addon, WASM, image processor, database driver i browser binary kao platformski supply-chain ulazi;
- kompletan inventar `tsconfig` fajlova, project reference-i, module resolution-a, target-a i strictness override-a;
- detekcija `noCheck`, `skipLibCheck`, transpile-only i build putanja koje zaobilaze puni TypeScript check;
- ESM/CJS, conditional export, server/client entrypoint i test-runner resolution provere;
- deterministic generated contract i schema/type drift provere.

## Next.js routing, rendering i RSC

Novi prompt detaljno obuhvata:

- App Router, Pages Router i mixed-router sisteme;
- route group-e, parallel route-e, intercepting route-e, dynamic i catch-all segmente;
- layout, template, loading, error, not-found, forbidden, unauthorized, default i global-error granice;
- direktan URL, client navigaciju, reload, back/forward, locale i encoded-path ponasanje;
- `proxy.ts` i legacy `middleware.ts`, matcher-e, rewrite-e, redirect-e, header-e i bypass putanje;
- eksplicitno pravilo da Proxy/Middleware nije authorization boundary;
- `use client`, server-only, client-only, barrel export i transitive import granice;
- client bundle scan za tajne, private environment vrednosti i privilegovane module;
- RSC payload velicinu, privatna polja, error leakage, serialization i cross-tenant izolaciju;
- patch i regression dokaz za React, React DOM, Next.js i RSC advisory-je.

## Hydration, state i React Compiler

Dodate su provere za:

- hydration drift zbog vremena, random-a, locale-a, timezone-a, browser API-ja, invalidnog HTML-a i flag drift-a;
- duplicated state, stale closure, effect dependency, subscription, timer, observer, abort i cleanup probleme;
- Suspense, transition, `useActionState`, `useOptimistic` i optimistic rollback;
- double-submit, stale overwrite, out-of-order response i navigation-triggered replay;
- controlled React Compiler rollout sa before/after correctness, performance, memory i debugging dokazima;
- zabranu automatskog uklanjanja manual memoization-a bez merenja.

## Cache i version-skew audit

Najvece prosirenje odnosi se na cache sistem.

Prompt sada zahteva:

- identifikaciju tacnog version-specific cache modela;
- `cacheComponents`, `use cache`, private/remote cache, fetch cache, route cache, request memoization i platform cache inventar;
- kompletan cache key sa tenant, user, role, locale, currency, permission, feature flag i data-version dimenzijama;
- klasifikaciju public, tenant-shared, user-private, request-private i forbidden-to-cache podataka;
- TTL, stale policy, cache life, tag, path invalidation, update ordering i tolerated-staleness ugovor;
- stampede, hot-key, cache penetration, invalidation storm i unbounded cardinality testove;
- CDN, browser cache, service worker i regional purge behavior;
- old HTML/new asset, old client/new server, old action/new deployment i old service-worker scenarije;
- deployment ID, asset retention, compatibility window i safe reload strategiju.

## Server Actions, API i webhook hardening

Dodato je:

- inventarisanje svake `use server` funkcije, bound action-a, form action-a i indirektne reference;
- server-side authentication i authorization unutar same akcije;
- zabrana poverenja u hidden field, bound ID, client state, Proxy check ili UI visibility;
- validation strukture, semantike, ownership-a, state transition-a, velicine i business invarijanti;
- idempotency key, duplicate scope, expiry i behavior kroz retry, timeout, disconnect, redirect i crash;
- database constraint i transaction dokaz za autoritativne invarijante;
- outbox, reconciliation ili compensation za spoljne side effect-e;
- `allowedOrigins`, host/origin, body size, action encryption key, rotation i multi-instance compatibility;
- API, webhook, file upload/download i streaming resource-limit ugovori;
- webhook raw-body signature, replay, key rotation, ordering i acknowledgement scenariji.

## Auth, tenant i admin

Novi prompt uvodi:

- kompletan login, registration, invitation, linking, reset, magic-link, MFA, passkey, reauth, logout i recovery audit;
- OIDC issuer, audience, nonce, state, PKCE, redirect URI, algorithm i key rollover provere;
- session fixation, rotation, idle/absolute expiry, revocation i rights-change propagation;
- resource-level authorization matricu za rute, action-e, API-je, query-je, fajlove, cache, queue, export, search i admin;
- tenant derivaciju iz trusted server context-a;
- owner constraint u autoritativnom query-ju umesto race-prone fetch-then-check obrasca;
- admin, support, impersonation, delegated access i break-glass approval/audit/expiry ugovor;
- cross-tenant testove kroz cache, queue, file, export, search, telemetry i error putanje.

## Platform, performance i operacije

Dodate su zasebne provere za:

- Node runtime, Edge runtime, serverless, Vercel, self-hosted Node, container i adapter deployment;
- API, filesystem, socket, native module, WASM, crypto i database-driver kompatibilnost po runtime-u;
- zabranu oslanjanja na warm instance, module global, local filesystem ili in-memory lock za correctness;
- Vercel project linkage, env scope, domen, alias, protection, region, function i platform access;
- self-hosting standalone output, output tracing, asset retention, shared cache handler, deployment ID i graceful draining;
- field i lab LCP, INP, CLS, TTFB, RSC payload, JavaScript, slike, fontove i third-party rad;
- cold, warm, burst, sustained, soak, failover, cache-cold i dependency-brownout testove;
- capacity, headroom, saturation, load shedding i cost guardrail-e;
- accessibility, i18n, RTL, SEO, structured data, PWA, offline, browser storage, push i multi-tab ponasanje;
- telemetry redaction, release correlation, SLI/SLO, error budget, alert owner i recovery confirmation.

## Rollout, rollback i restore

Prompt sada razlikuje:

- traffic rollback;
- application rollback;
- configuration rollback;
- feature disable;
- cache namespace promenu;
- schema forward repair;
- data reconciliation;
- credential i session revocation.

Eksplicitno je zabranjena pretpostavka da deployment rollback vraca database write operacije, payment, email, queue, file, cache ili service-worker side effect-e.

Restore mora biti izveden u izolovanom okruzenju uz proveru scheme, kljuceva, object storage-a, queue state-a, search index-a, tenant izolacije, kriticnih tokova, RPO i RTO.

## Aktuelni baseline

Revizija je uskladjena sa sledecim stanjem na dan 5. avgusta 2026:

- Next.js 16.3.x je najnovija stabilna feature linija;
- posle July 2026 Security Release, 16.2.11 je Active LTS, a 15.5.21 Maintenance LTS;
- React 19.2 je stabilna linija;
- React Compiler 1.0 je stabilan, ali zahteva kontrolisanu adoption proveru;
- TypeScript 7 je stabilno objavljen 8. jula 2026;
- TypeScript 6 ostaje bitna transition i compatibility linija;
- Node.js 24 i 22 su LTS linije, dok je 26 Current;
- Next.js 16 koristi `proxy.ts` konvenciju umesto starog Middleware naziva;
- RSC security advisory iz decembra 2025. pokazuje da hosting mitigacija ne sme zameniti framework patch.

## Obavezne matrice i scenariji

Dodato je:

- 12 obaveznih evidence matrica M1-M12;
- 20 obaveznih adversarial i failure scenarija S1-S20;
- P0-P3 severity model;
- 20-stavki Production Readiness checklist;
- 12-stavki Definition of Done;
- Forbidden Shortcuts sekcija;
- obavezni final report;
- READY, READY_WITH_CONDITIONS, NOT_READY i INCIDENT decision pravila.

## Rezultati validacije

- EN linije: 985;
- SR linije: 985;
- EN H1-H3 naslovi van code fence blokova: 131;
- SR H1-H3 naslovi van code fence blokova: 131;
- line-shape odstupanja: 0;
- YAML frontmatter: validan;
- JSON baseline manifest: validan;
- Markdown code fence blokovi: balansirani;
- baseline hardcode scan: prosao;
- en dash, em dash i non-breaking hyphen u SR promptu: 0.

Repository-level parity checker sada potvrduje Next.js paket. Jedino preostalo staro strukturno odstupanje nalazi se u Python/PySide6 paru, koji jos nije obradjen.
