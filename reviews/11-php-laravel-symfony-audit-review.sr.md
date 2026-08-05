# Revizija 11 - PHP / Laravel / Symfony Production Audit Prompt 2.0.0

## Rezime

Postojeci EN/SR par je imao dobar osnovni smer i gotovo isti obim, ali je sa 237 EN i 238 SR linija i 32 naslova bio pre svega prosirena checklist-a. Nije dovoljno strogo dokazivao koji PHP binary, SAPI, INI, ekstenzije i artifact stvarno rade u svakom procesu, kako se Laravel i Symfony konfiguracija efektivno kompajlira, kako se dugovecni worker-i resetuju, niti kako sistem reaguje na partial failure, mixed-version deployment, stale OPcache, queue replay, migration kvar, compromise ili restore.

Novi par je rekonstruisan kao samostalni source-to-runtime production audit ugovor za PHP, Composer, Laravel, Symfony, PHP-FPM, Octane, RoadRunner, Swoole, Messenger, Horizon, queue-ove, scheduler-e, baze, cache, storage i spoljne provider-e.

## Rezultat

| Metrika | Pre | Posle |
| --- | ---: | ---: |
| Linije EN | 237 | 1070 |
| Linije SR | 238 | 1070 |
| H1-H3 naslovi EN | 32 | 176 |
| H1-H3 naslovi SR | 32 | 176 |
| Verzija prompta | bez formalnog 2.0 ugovora | 2.0.0 |
| Evidence model | osnovni statusi | E0-E5 |
| Severity model | osnovni P0-P3 | P0-P3 sa release akcijom |
| Evidence matrice | nema formalnog kompleta | 12 |
| Adversarial i failure scenariji | nekoliko implicitnih | 20 obaveznih |
| Line-shape odstupanja | postojala je razlika u broju linija | 0 |

## Glavne slabosti prethodne verzije

1. Nije postojao potpuni dokazni lanac od source commit-a, Composer graph-a i PHP toolchain-a do artifact digest-a, deployment revision-a i stvarnog procesa.
2. CLI, FPM, queue worker, scheduler, migrator i dugovecni runtime nisu bili dovoljno jasno razdvojeni.
3. Composer skripte, plugin-i, private repository-ji, platform zahtevi, source install i supply-chain poverenje nisu imali pun audit.
4. Laravel i Symfony su imali zajednicke provere, ali ne i zasebne efektivne lifecycle, container, policy, voter, queue i cache putanje.
5. Laravel Octane, Horizon i Symfony Messenger nisu dovoljno strogo dokazivali reset request stanja, mixed-version poruke, retry, DLQ i graceful drain.
6. Eloquent, Doctrine, DBAL i raw SQL nisu imali jedinstvenu matricu constraint-a, lock-ova, isolation-a, pool-a i production-like query planova.
7. Idempotency, outbox, inbox, reconciliation i crash tacke izmedju database i spoljnih side effect-a nisu bili formalizovani.
8. PHP-FPM, OPcache, JIT, process pool, queue concurrency i dependency pool nisu bili deo jedinstvenog capacity modela.
9. File upload, archive, media i document parser putanje nisu imale kompletan malicious-input i lifecycle ugovor.
10. Rollout nije dovoljno razmatrao stare FPM child procese, stale OPcache, stare worker-e, cache warmup, schema overlap i worker reload.
11. Incident postupak nije jasno razdvajao obicnu gresku od webshell-a, credential compromise-a, korupcije i potrebe za trusted rebuild-om.

## Nova arhitektura prompta

Prompt sada sadrzi:

- datirani baseline zasnovan na primarnim izvorima;
- principal-level ulogu, misiju i non-negotiable rezultate;
- required inputs, radne rezime i safety stop pravila;
- formalni E0-E5 evidence model;
- obavezan finding record;
- 30 detaljnih audit faza;
- zaseban Laravel application path;
- zaseban Symfony application path;
- auth, authorization, tenancy i break-glass matrice;
- persistence, transaction, queue, cache, long-lived runtime i external-provider audit;
- FPM, OPcache, JIT, capacity i resource-exhaustion audit;
- CI/CD, immutable artifact, migration, rollout, rollback, restore i incident ugovor;
- 12 evidence matrica;
- 20 adversarial i failure scenarija;
- Production Readiness checklist;
- Definition of Done;
- Forbidden Shortcuts;
- obavezan finalni izvestaj i odluke READY, READY_WITH_CONDITIONS, NOT_READY i INCIDENT.

## Source-to-runtime dokaz

Novi prompt zahteva korelaciju:

`repository -> commit -> PHP binary -> SAPI -> INI -> extensions -> Composer -> lock graph -> generated code -> framework caches -> artifact digest -> deployment revision -> schema -> running process -> telemetry -> recovery`

`composer.json`, lokalni CLI, zeleni CI, `php -v` iz pogresnog container-a ili mutable image tag vise nisu prihvaceni kao dokaz stvarnog produkcionog stanja.

## PHP runtime, SAPI i konfiguracija

Dodato je:

- odvojeno dokazivanje CLI, FPM, Apache module, CGI, RoadRunner, Swoole, OpenSwoole, FrankenPHP i custom daemon procesa;
- tacan PHP patch, vendor build, arhitektura, libc i build opcije;
- `php.ini`, scan dir, additional INI fajlovi, environment promenljive i runtime override-i;
- kompletan spisak ekstenzija sa verzijama i konfiguracijom;
- `disable_functions`, `open_basedir`, upload, post, memory, execution i input limite kao defense-in-depth;
- error display, error log, timezone, locale, ICU, OpenSSL i database client razlike;
- startup i shutdown procedure za svaki SAPI;
- dokaz da CLI i produkcioni proces zaista koriste nameravani runtime.

## Composer i supply chain

Prompt sada zahteva:

- verifikovan Composer binary i installer;
- lockfile enforcement;
- `config.platform` u odnosu na stvarni runtime;
- `allow-plugins`, scripts i lifecycle hook audit;
- Packagist, private Composer repository, VCS, path i artifact source poverenje;
- source i dist install razlike;
- abandoned package, fork, replacement i namespace takeover rizike;
- audit runtime i development zavisnosti;
- clean-checkout i offline reproducibility;
- SBOM, provenance, potpis i immutable promotion.

## Laravel audit

Laravel deo sada posebno proverava:

- tacan framework i first-party package patch;
- bootstrap konfiguraciju, service provider-e, package discovery i middleware;
- route model binding, Form Request, DTO, policy, gate i authorization redosled;
- Eloquent fillable ili guarded, cast-ove, global scope-ove, soft delete, observer-e i model event-e;
- Sanctum, Passport, Fortify, Socialite i custom guard putanje;
- queue, Horizon, batch, chain, unique job, failed job i scheduler lock ponašanje;
- config, route, event i view cache generation;
- Telescope, Horizon, Pulse, Ignition i debug-tool pristup;
- Octane scoped binding-e, singleton state, timer-e, task worker-e, concurrency i reset.

## Symfony audit

Symfony deo sada zasebno proverava:

- tacan patch, Flex recipes, bundle-ove, Runtime komponentu i kernel okruzenje;
- kompajlirani service container, autowiring, decorator-e, compiler pass-ove i resettable service-e;
- route loading, argument resolver-e, request mapping, validator-e i serializer-e;
- firewall-e, authenticator-e, access control, voter-e i exception listener-e;
- Doctrine ORM/DBAL, entity listener-e, filtere, migracije i proxy generation;
- Messenger transport-e, stamp-ove, middleware, retry, failure transport i worker reset;
- Scheduler, Lock, Cache, RateLimiter, Workflow, HttpClient, Mailer i secrets vault;
- cache warmup i deployment replacement svih procesa.

## Auth, authorization i tenancy

Dodato je:

- password hashing i rehash;
- session fixation, expiry, revocation i concurrent session kontrola;
- JWT, OAuth i OIDC issuer, audience, algoritam, nonce, state, PKCE i key rotation;
- MFA enrollment, recovery, downgrade i support override;
- registration, invitation, suspension, deletion, anonymization i ownership transfer;
- route, command, queue, export, file, webhook, admin i support authorization matrica;
- BOLA i IDOR testovi;
- tenant scope kroz ORM, raw SQL, cache, session, queue, notification, search, file, log i analytics;
- impersonation, delegated access i break-glass sa odobrenjem, expiry-jem i revizijom.

## Persistence, transakcije i partial failure

Prompt sada zahteva:

- Eloquent, Doctrine, DBAL, query builder i raw SQL inventar;
- model/entity identity, value object, cast, nullability i serialization audit;
- relation ownership, cascade, orphan removal, eager/lazy loading i N+1;
- database constraint-e za uniqueness, tenant granice, money precision i state tranzicije;
- production-like query plan i index dokaz;
- optimistic i pessimistic locking;
- transaction manager, isolation, timeout, retry i lock order;
- idempotency scope, fingerprint, atomic ownership, durable result i conflict ponašanje;
- crash tacke pre, tokom i posle commit-a;
- transactional outbox, inbox i CDC;
- payment, email, object storage, search i webhook reconciliation.

## Queue, scheduler i long-lived runtime

Dodato je:

- transport, acknowledgement, visibility, retry, DLQ i poison-message matrica;
- duplicate, reorder, delay, stale message i schema mismatch testovi;
- scheduler overlap, lock TTL, leader election, clock skew, missed run i DST;
- bounded concurrency, prefetch i database pool pressure;
- graceful drain i worker replacement;
- FPM, Octane, RoadRunner, Swoole, FrankenPHP, ReactPHP, Amp i custom daemon lifecycle;
- static, global, singleton, locale, auth, tenant i tracing state po lifetime-u;
- reset hook-ovi, transaction cleanup, connection health i temporary resource cleanup;
- Fiber i coroutine cancellation, suspension i shared-state rizici;
- cross-user i cross-tenant reuse istog worker-a.

## Bezbednost i file processing

Novi prompt detaljno pokriva:

- SQL, shell, template, HTML, URL, header, log, path, regex, LDAP, XML, YAML, CSV i mail injection;
- contextual encoding, CSP i trusted HTML;
- CSRF, CORS, origin i SameSite granice;
- SSRF, redirect, DNS rebinding, alternativnu IP sintaksu i metadata service;
- PHP object injection, PHAR metadata, YAML tagove, XML entity-je i gadget chain-ove;
- expensive regex, duboke strukture, decompression i export abuse;
- upload auth, tenant namespace, MIME, magic bytes, parser limite i quarantine;
- traversal, symlink, race, overwrite, executable placement i public exposure;
- zip slip, archive bomb, malformed media, PDF, office i CSV rizike;
- export authorization i snapshot konzistentnost.

## FPM, OPcache, JIT i capacity

Dodato je:

- FPM process manager, child, spare, max request, timeout i slow-log audit;
- OPcache memory, interned strings, preload, validation, stale-code rizik i emergency reset;
- JIT kao merena workload-specific odluka;
- memory, fragmentation, worker recycle i queue growth;
- zajednicki model FPM, queue, database, Redis, HTTP i provider pool-a;
- cold, burst, sustained, soak, failover, dependency slowdown i malicious-input testovi;
- load shedding i predvidljivo otkazivanje pre kolapsa hosta ili zavisnosti.

## Release, migracije i recovery

Prompt sada zahteva:

- clean production build;
- generisanje i proveru framework cache-eva i compiled container-a;
- non-root image i minimalne writable putanje;
- build-once/promote-same-digest;
- expand-and-contract migracije;
- resumable i idempotent backfill;
- old/new application i worker compatibility;
- kontrolisan redosled artifact-a, config-a, tajni, cache-a, OPcache-a, traffic-a, worker-a i schema-e;
- canary cohort, guardrail i abort kriterijume;
- odvojeni application, config, traffic, worker i schema rollback;
- forward repair i data reconciliation;
- izolovani restore, point-in-time recovery, RPO i RTO.

## Incident mode

Dodat je poseban INCIDENT workflow za:

- aktivni exploit;
- webshell ili nepoznat executable kod;
- kradju kredencijala;
- signing compromise;
- korupciju podataka;
- destruktivnu migraciju;
- neizvestan integritet produkcije.

Prompt zabranjuje in-place ciscenje kompromitovanog hosta kao dokaz oporavka. Zahteva ocuvanje dokaza, containment, opoziv identiteta, analizu persistence-a i lateral movement-a, trusted rebuild i verifikaciju podataka, queue-ova, storage-a, cache-a, sesija i provider-a pre vracanja normalnog servisa.

## Aktuelni baseline

Baseline je uskladjen sa stanjem na 5. avgust 2026:

- PHP 8.5 je aktivna glavna linija;
- zvanicni changelog navodi PHP 8.5.9 od 30. jula 2026;
- Laravel 13 je stabilna glavna linija i podrzava PHP 8.3 do 8.5;
- Symfony 8.1 je aktuelna stabilna linija;
- Symfony 7.4 je aktuelna LTS linija;
- Composer 2.10.2 je aktuelno stabilno izdanje.

Svaka verzija se ipak mora ponovo proveriti u trenutku konkretnog audita, a upgrade se bira prema support periodu, aplikativnoj kompatibilnosti, provider-u, ekstenzijama, testovima i rollback-u.

## Rezultati validacije

- EN linije: 1070;
- SR linije: 1070;
- EN H1-H3 naslovi: 176;
- SR H1-H3 naslovi: 176;
- heading paritet: prosao;
- line-shape odstupanja: 0;
- YAML frontmatter: validan;
- JSON baseline manifest: validan;
- Markdown fence blokovi: balansirani;
- baseline hardcode scan: prosao;
- en dash u SR promptu: 0;
- em dash u SR promptu: 0;
- non-breaking hyphen u SR promptu: 0.

Repository-level parity checker sada potvrdjuje i PHP / Laravel / Symfony paket. Jedini preostali poznati strukturni problem je jos neobradjeni Python/PySide6 par.
