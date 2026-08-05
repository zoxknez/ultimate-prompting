# Revizija 10 - Node.js / Express / Fastify API Production Audit Prompt 2.0.0

## Rezime

Postojeci EN/SR par je imao dobar osnovni redosled i potpuni strukturni paritet, ali je sa 272 linije i 27 naslova bio pre svega prosirena checklist-a. Nije dovoljno strogo dokazivao sta je izgradjeno, sta je deploy-ovano, koji Node runtime i native ABI stvarno rade, kako se sistem ponasa pod parcijalnim kvarom i da li su rollback, restore i incident procedure zaista izvrsive.

Novi par je rekonstruisan kao samostalni source-to-runtime production audit ugovor za Node.js, TypeScript, JavaScript, Express, Fastify, HTTP API-je, worker-e, queue-ove, scheduler-e, webhook-e, SSE i WebSocket sisteme.

## Rezultat

| Metrika | Pre | Posle |
| --- | ---: | ---: |
| Linije EN | 272 | 1052 |
| Linije SR | 272 | 1052 |
| H1-H3 naslovi EN | 27 | 152 |
| H1-H3 naslovi SR | 27 | 152 |
| Verzija prompta | bez formalnog 2.0 ugovora | 2.0.0 |
| Evidence model | osnovni statusi | E0-E5 |
| Severity model | P0-P3 | P0-P3 sa obaveznom akcijom |
| Evidence matrice | nema formalnog kompleta | 12 |
| Adversarial i failure scenariji | nekoliko implicitnih | 20 obaveznih |
| Line-shape odstupanja | 0 | 0 |

## Glavne slabosti prethodne verzije

1. Baseline je sadrzao previse patch primera i nije dovoljno jasno odvajao Node Current od podrazumevanog production LTS izbora.
2. Express je bio glavni framework, dok Fastify nije imao zaseban lifecycle, encapsulation, plugin i schema-compiler audit.
3. Nije postojao formalni dokazni lanac od commit-a i lockfile-a do artifact digest-a, deployment revizije i pokrenutog procesa.
4. Nisu dovoljno razdvojeni local, editor, CI, build, worker, migrator, container, serverless i production runtime-i.
5. TypeScript je tretiran pre svega kao static typing sloj bez potpune compiler, transpiler, ESM/CJS i generated-code matrice.
6. HTTP audit nije dovoljno detaljno pokrivao neslaganje proxy i application parser-a, request smuggling, slowloris, malformed header-e i timeout lanac kroz sve hop-ove.
7. Auth i autorizacija nisu imali potpunu route-resource-tenant matricu, admin, support, impersonation i break-glass ugovor.
8. Transakcije i idempotency nisu imali formalne crash point-eve, request fingerprint, stored outcome i reconciliation zahteve.
9. Queue, scheduler i webhook tokovi nisu dovoljno strogo dokazivali ack tacku, redelivery, poison message, DLQ replay, duplicate execution i shutdown.
10. Event loop, worker pool, memorija, handle-ovi, stream-ovi i AsyncLocalStorage nisu bili deo jedinstvenog ownership i capacity modela.
11. CI/CD, provenance, immutable promotion, canary, rollback, forward repair, izolovani restore, RPO, RTO i incident response nisu bili dovoljno razradjeni.

## Nova arhitektura prompta

Prompt sada ima sledece glavne slojeve:

- datirani research baseline i politika primarnih izvora;
- principal-level uloga, misija i non-negotiable outcome;
- required inputs, radni rezimi i safety stop;
- formalni E0-E5 evidence model;
- obavezan finding record;
- operativni ugovor;
- 30 detaljnih audit faza;
- migration i upgrade overlay-i;
- 12 evidence matrica;
- 20 adversarial i failure scenarija;
- P0-P3 severity model;
- repair i verification workflow;
- production readiness checklist;
- Definition of Done;
- Forbidden Shortcuts;
- obavezan finalni izvestaj i odluke READY, READY_WITH_CONDITIONS, NOT_READY i INCIDENT.

## Source-to-runtime dokaz

Novi prompt zahteva korelaciju:

`repository -> commit -> Node binary -> package manager -> lock graph -> compiler/transpiler -> generated code -> native ABI -> built artifact -> digest -> deployment revision -> config revision -> schema -> running process -> telemetry`

Mutable image tag, environment rebuild, zeleni dashboard ili package.json engines polje vise nisu dovoljni kao dokaz identiteta produkcionog procesa.

## Node.js runtime i lifecycle

Dodato je:

- razdvajanje Node 26 Current, Node 24 LTS i Node 22 LTS;
- obavezna provera tacnog patch-a i support perioda;
- dokaz stvarnog binary-ja, arhitekture, libc-a, OpenSSL-a, ICU-a, V8-a i native ABI-ja;
- provera razlika izmedju local, CI, build, test, worker, migrator, image, serverless i production runtime-a;
- audit native addon-a, prebuilt binary-ja, WASM-a i install-time alata;
- planiranje promenjenog Node release modela od v27;
- Node Permission Model kao defense-in-depth, a ne kao potpuni sandbox;
- controlled crash, restart, diagnostic report i crash-loop politika.

## Express audit

Express deo sada posebno proverava:

- tacan major i patch;
- Express 5 rejected-promise forwarding;
- async handler i error middleware semantiku;
- path-to-regexp i wildcard promene;
- body, query, static MIME i uklonjene API-je;
- Express 4 custom async wrapper-e i migration blocker-e;
- app, Router, sub-app, mount i settings inheritance;
- double next, double send i headers-already-sent putanje;
- stvarnu trust proxy hop topologiju;
- regression dokaz posle codemod-a ili migracije.

## Fastify audit

Fastify je sada ravnopravan audit path, sa proverama za:

- core i plugin LTS i Node compatibility;
- plugin DAG i registration order;
- encapsulation context, decorator-e, hook-ove, prefix-e i shared schema ID-jeve;
- slucajno globalno izlaganje i scope-dependent ponasanje;
- JSON Schema kao executable application input;
- zabranu kompilacije user-provided schema;
- Ajv opcije, formate, keyword-e i serializer behavior;
- zabranu database i external poziva u pocetnoj validaciji;
- response schema i alternate serializer data leakage;
- content-type parser, body limit i lifecycle od onRequest do onResponse.

## HTTP, proxy i request lifecycle

Dodat je potpuni hop-by-hop audit za:

- client, CDN, WAF, load balancer, ingress, service mesh, reverse proxy i Node server;
- request, headers, keep-alive, idle, upstream, body i shutdown timeout-e;
- HTTP/1.1, HTTP/2, TLS termination, ALPN i connection reuse;
- request smuggling, duplicate content-length i transfer-encoding konflikt;
- host, origin, absolute-form URL i encoded path ponasanje;
- compression, range, cache, slowloris i half-open konekcije;
- client abort i propagation cancellation-a;
- kompletan middleware ili hook order;
- raw-body webhook putanju bez gubitka size i auth kontrole.

## Runtime validacija i API ugovor

TypeScript tip vise nije prihvacen kao runtime dokaz. Prompt zahteva:

- validation za path, query, header, cookie, body, multipart, fajl i upstream odgovor;
- body, depth, array, string, number, file, decompression i total limite;
- semantic, cross-field, ownership-aware i state-aware proveru;
- mass assignment i field allowlist;
- prototype pollution i unsafe merge zastitu;
- money, decimal, date, duration, timezone, Unicode i regex proveru;
- response schema i private-field leakage testove;
- OpenAPI, generated client, SDK, example i runtime route drift;
- bounded pagination, search, include, expansion i batch complexity;
- old/new client i server compatibility.

## Authentication, authorization i tenancy

Dodato je:

- kompletan registration, login, MFA, passkey, reset, recovery, logout i closure audit;
- session fixation, rotation, store, expiry i revocation;
- JWT/OIDC issuer, audience, algorithm, signature, nonce, state, PKCE i key rotation;
- refresh token family i reuse detection;
- API key i service identity scope, hashing, display-once, rotation i attribution;
- route-resource authorization matrica;
- odvojeni identity, role, permission, ownership, tenant, state i relationship slojevi;
- BOLA, BFLA, batch, nested i indirect-reference testovi;
- admin, support, delegated access, impersonation i break-glass ugovor;
- tenant izolacija kroz cache, queue, storage, telemetry, logove, error-e i background job-ove.

## Podaci, transakcije i idempotency

Prompt sada zahteva:

- registar autoritativnih poslovnih invarijanti;
- mapu svakog read-modify-write i race window-a;
- unique constraint, version, CAS, lock, lease i fencing dokaz;
- idempotency key source, actor, operation, fingerprint, atomic claim, expiry i stored outcome;
- odbijanje istog key-a sa drugim payload-om;
- crash test pre, tokom i posle commit-a;
- razlikovanje transport retry-ja, application retry-ja, queue replay-a i operator re-run-a;
- transaction, isolation, deadlock, pool i generated SQL audit;
- expand-and-contract migracije i old/new binary overlap;
- reconciliation kada database i eksterni provider ne mogu atomicki da commit-uju.

## Queue, worker, scheduler i webhook pouzdanost

Dodato je:

- delivery i acknowledgement semantika;
- visibility ili lease timeout;
- partitioning, ordering, concurrency i retry budget;
- transactional outbox, inbox, CDC, saga i reconciliation;
- poison message, quarantine, DLQ i replay politika;
- duplicate scheduler ownership, overlap, missed run, catch-up storm, DST i clock skew;
- graceful shutdown sa stop intake, drain ili checkpoint ponasanjem;
- webhook raw-body signature, timestamp, replay window, key rotation, ordering i stored outcome.

## Event loop, worker pool i memorija

Novi prompt zahteva merenje:

- event-loop delay i utilization;
- worker-pool pritiska;
- CPU, throughput i tail latency;
- heap, RSS, external i native memory;
- active handle-ova, request-a, socket-a i file descriptor-a;
- retainera, cache growth-a, unbounded queue-a i AsyncLocalStorage context-a;
- stream backpressure, abort, pipeline i cleanup putanja;
- soak testa koji razlikuje warmup, fragmentation i pravi leak;
- OOM, restart, diagnostic capture i crash-loop zastitu.

## CI/CD, release i recovery

Dodato je:

- repository, runner, fork, cache, OIDC, registry, secret i deployment trust mapiranje;
- izolacija untrusted PR izvrsavanja;
- immutable pinning akcija, toolchain-a i image-a;
- build-once/promote-same-artifact pravilo;
- SBOM, provenance, approval i exception expiry;
- canary cohort, guardrail, observation window i abort authority;
- odvojeni traffic, application, configuration i feature rollback;
- schema forward repair i data reconciliation;
- izolovani restore sa podacima, kljucevima, schemom, tenant izolacijom i kriticnim tokovima;
- dokaz RPO i RTO umesto dokumentovane pretpostavke;
- containment za credential compromise, tenant leak, corruption, supply-chain incident i provider outage.

## Aktuelni baseline

Baseline je uskladjen sa stanjem na 5. avgust 2026:

- Node.js 26 je Current linija;
- Node.js 24 Krypton i Node.js 22 Jod su LTS linije;
- Node projekat je najavio jednu major verziju godisnje pocevsi od v27;
- Express 5 je najnoviji stabilni major;
- Express 4 ostaje legacy odrzavana linija;
- Fastify 5.11.x je najnovija dokumentovana LTS linija na datum audita;
- TypeScript 7 je stabilan;
- OWASP API Security Top 10 2023 ostaje aktuelno zvanicno API izdanje;
- OpenTelemetry JavaScript ima Node instrumentaciju i OTLP exporter-e, uz obaveznu proveru stabilnosti konkretnih paketa.

## Rezultati validacije

- EN linije: 1052;
- SR linije: 1052;
- EN H1-H3 naslovi: 152;
- SR H1-H3 naslovi: 152;
- heading depth i count paritet: prosao;
- line-shape odstupanja: 0;
- YAML frontmatter: validan;
- JSON baseline manifest: validan;
- Markdown fence blokovi: balansirani;
- baseline hardcode scan: prosao;
- en dash u SR promptu: 0;
- em dash u SR promptu: 0;
- non-breaking hyphen u SR promptu: 0.

Repository-level parity checker sada potvrdjuje i Node.js / Express / Fastify paket. Jedini preostali poznati strukturni problem je jos neobradjeni Python/PySide6 par.
