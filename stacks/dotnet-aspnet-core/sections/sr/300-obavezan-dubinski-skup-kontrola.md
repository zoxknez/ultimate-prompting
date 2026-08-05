## Obavezan Dubinski Skup Kontrola

Sledece kontrole su obavezni dodatak svakoj primenljivoj fazi. Ne zamenjuj dokaz popunjavanjem checklist-e.

### 1. Hijerarhija Dokaza I Granica Zakljucka

Prednost dokaza je ovim redom: posmatrano production ponasanje i nepromenljivi runtime metadata; production-like izvrsavanje nad izolovanim zavisnostima; pregled publish artefakta; razreseni build i test output; source i konfiguracija; generisana dokumentacija; projektovana namera.

Eksplicitno razresi neslaganja. Source popravka nije dokaz deployment-a, deployovan binary nije dokaz da ga koriste sve replike, a uspesan zahtev nije dokaz ispravne autorizacije, transakcije ili oporavka.

Zavrsni zakljucak ne moze biti jaci od najslabijeg neproverenog kriticnog sloja. Nedostatak production pristupa, restore dokaza, identity-provider konfiguracije, ogranicenja baze ili deployment vlasnistva mora da smanji pouzdanost i bude blocker kada je materijalan.

### 2. Identitet Od Source-a Do Runtime-a

Dokazi lanac `commit -> SDK -> restore graph -> compiler/analyzers/generators -> publish settings -> artifact digest -> image/package -> deployment revision -> running process`.

Zabelezi informational version, assembly/file version, commit SHA, build ID, artifact digest, runtime verziju, OS/runtime identifier, identitet startup konfiguracije i deployment revision gde postoje.

Pronadji rebuild pod istim tagom, promenljive package ili image reference, lokalni DLL drift, generated source drift, zastarele publish foldere i production runtime patch koji se razlikuje od nameravanog baseline-a.

### 3. Kompatibilnost SDK-a, TFM-a, Jezika I Alata

Razresi `global.json` roll-forward, instalirane SDK-ove, target framework-e, runtime framework-e, C# `LangVersion`, kompatibilnost Visual Studio-a ili build agenta, source generator-e, analyzer-e, workload-e i `dotnet-ef`.

Ne preporucuj `latest`, preview ili language version van TFM podrske bez provere. Testiraj multi-targeted biblioteke pod svakim podrzanim TFM-om i proveri da conditional compilation ne stvara razlicitu bezbednost ili ponasanje.

Za .NET Framework workload-e proveri OS lifecycle, .NET Framework lifecycle, binding redirect-e, GAC ili COM zavisnosti, IIS mod i realan plan migracije ili ogranicavanja rizika.

### 4. MSBuild Evaluacija I Deterministicki Build

Pregledaj evaluirane property-je i import-e, ne samo vidljivi project fajl. Proveri `Directory.Build.*`, `Directory.Packages.props`, custom target-e, environment uslove, generated fajlove, signing, deterministic/continuous-integration build podesavanja, path mapping i reproduktivno verzionisanje.

Pregledaj svaki `Exec`, shell interpolaciju, preuzeti alat, code-generation korak i copy target zbog injection-a, curenja tajni, nehermetickih ulaza, mrezne zavisnosti i menjanja source-a.

Build izvrsi iz cistog checkout-a ili ekvivalentnog izolovanog workspace-a. Uporedi artefakte ili dokumentovana nedeterministicka polja kada je reproduktivnost zahtev.

### 5. NuGet Trust, Provenance I Restore Pravila

Proveri package source mapping, vlasnistvo feed-a, scope autentikacije, HTTPS i certificate ponasanje, package potpise gde su zahtevani, lock fajlove, locked restore, audit izvore, suppression-e, transitive zavisnosti i pravila na nivou repozitorijuma.

Promenu vlasnistva package ID-ja, napustene pakete, typosquatting, dependency confusion, lokalne feedove, source-generator pakete, analyzer-e i build-time pakete tretiraj kao odluke o poverenju za izvrsavanje koda.

Svaki suppression mora imati advisory, analizu primenljivosti, vlasnika, rok, compensating control i putanju upgrade-a ili uklanjanja. Cist audit rezultat nije dokaz da se paket odrzava ili da je ispravno konfigurisan.

### 6. Generisan Kod, Reflection I Dinamicko Ucitavanje

Popisi source generator-e, T4, OpenAPI ili protobuf generisanje, Razor compilation, serializer-e, expression tree-jeve, runtime proxy-je, plugin loading, reflection, `AssemblyLoadContext` i dinamicki ucitane assembly-je.

Proveri poreklo generated outputa, ponovljivost, mogucnost pregleda, nullable anotacije, security pretpostavke i da li se generated fajlovi kompajliraju iz pouzdanog ulaza.

Za plugin-e i extension assembly-je definisi trust, proveru potpisa ili digest-a, izolaciju, dependency resolution, unload ponasanje, capability boundary i putanju opoziva tokom incidenta.

### 7. Poslovne Invarijante I State Machine

Za svaku kriticnu operaciju definisi aktera, preduslove, dozvoljenu promenu stanja, invarijante, side effect-e, granicu transakcije, idempotency key, concurrency pravilo, audit dogadjaj, kompenzaciju i rezultat vidljiv korisniku.

Testiraj duplo, zakasnelo, promenjenog redosleda, konkurentno, ponovljeno, delimicno neuspesno, otkazano i replay izvrsavanje. Ne prihvataj controller happy-path test kao dokaz poslovne invarijante.

Za novac, zalihe, kvote, licence, entitlement-e, rezervacije i vlasnistvo naloga identifikuj autoritativni store i sprovedi invarijante ogranicenjima baze ili jednako jakim trajnim kontrolama.

### 8. Serialization, Binding I Evolucija Ugovora

Pregledaj `System.Text.Json`, Newtonsoft.Json, XML, protobuf, MessagePack, custom converter-e, polimorfizam, reference handling, casing, number handling, enum reprezentaciju, required clanove, nepoznata polja i maksimalnu dubinu ili velicinu payload-a.

Pronadji over-posting, mass assignment, dvosmislene default vrednosti, tiho skracivanje, culture-dependent parsing, nebezbedan type metadata, nekompatibilan date/time rad i promene ugovora skrivene u serializer opcijama.

Javne ugovore verzionisi namerno. Proveri stare i nove klijente, forward/backward kompatibilnost, tolerant reader-e, deprecation pravilo, schema registry ili contract testove i kompatibilnost rollback-a.

### 9. Globalizacija, Vreme, Brojevi I Tekst

Proveri culture, ICU dostupnost, invariant globalization, collation, normalization, case folding, regex timeout-e, Unicode confusable karaktere gde su security relevantni i lokalizovano parsiranje ili formatiranje.

Koristi eksplicitne time-zone i clock apstrakcije za testabilno poslovno vreme. Testiraj daylight-saving praznine i preklapanja, granice prestupnog dana, granice isteka, clock skew i dugotrajne job-ove koji prelaze promenu datuma.

Definisi decimal precision, scale, rounding mode, currency, jedinice, overflow, checked context i mapiranje u bazu. Nikada ne zakljucuj monetarnu ispravnost iz prikaza vrednosti.

### 10. Unsafe Kod, Native Interop I Vlasnistvo Memorije

Popisi `unsafe`, P/Invoke, COM, native biblioteke, memory-mapped fajlove, span-ove, pool-ove, pinned memory, custom marshalling i unmanaged callback-ove.

Proveri ABI, calling convention, arhitekturu, library search path, lifetime, vlasnistvo, granice, integer konverziju, prevod greske, thread affinity, cancellation i cleanup tokom exception-a.

Native zavisnosti zahtevaju vlasnika patchovanja, vidljivost u SBOM-u, platformsku podrsku, container kompatibilnost i stvarne publish/runtime testove za svaki deployovani RID.

### 11. Async Scheduling, Channel-i I Backpressure

Prati cancellation i deadline od ingress-a kroz bazu, HTTP, queue, fajl i streaming operacije. Razlikuj caller cancellation, timeout, host shutdown i internu gresku.

Audituj `Task.WhenAll`, parallel loop-ove, Channel-e, TPL Dataflow, timer-e, semaphore, lock-ove, concurrent kolekcije, thread-affine context i execution-context flow. Ogranici concurrency i duzinu reda.

Definisi ponasanje pod preopterecenjem: odbijanje, load shedding, queue, degradacija ili skaliranje. Neograniceni redovi, neograniceni fan-out ili retry bez zajednickog deadline-a su availability defekti i kada normal-load test prolazi.

### 12. DI Vlasnistvo I Dispose

Mapiraj svaki singleton, scoped, transient, keyed servis, factory, pooled objekat, hosted servis i eksterno vlasnistvo disposable resursa.

Pronadji captive dependency, dupli singleton graph, rucne root container-e, service locator, prerani dispose, neoslobodjene stream/response/scope resurse i async-disposable resurse koriscene sinhrono.

Proveri kreiranje scope-a i obradu greske u worker-ima, SignalR hub-ovima, gRPC servisima, middleware-u, filterima, background callback-ovima i paralelnim operacijama.

### 13. Configuration Reload, Feature Flag I Kill Switch

Klasifikuj konfiguraciju kao startup-only, reloadable, tajnu, per-tenant, per-environment ili deployment-owned. Validiraj kriticne opcije pri startup-u i odbij nevalidne kombinacije.

Za reloadable podesavanja proveri atomicnost, parcijalni update, cache invalidation, thread safety, telemetriju, audit trag i da li promena zahteva ponovno kreiranje konekcije ili klijenta.

Feature flag mora imati vlasnika, default, targeting, rok, testove oba stanja, bezbedan fallback, redosled zavisnosti i emergency kill-switch ponasanje. Flag ne sme zaobici autorizaciju ili schema kompatibilnost.

### 14. Granica Reverse Proxy-ja, Kestrel-a, IIS-a I YARP-a

Mapiraj klijenta, CDN/WAF, load balancer, reverse proxy, IIS ili ingress, Kestrel, YARP i application trust. Proveri poznate proxy-je i mreze pre prihvatanja forwarded header-a.

Pregledaj request limit-e, header limit-e, body rate, timeout-e, keep-alive, HTTP/2 i HTTP/3 ponasanje, TLS termination, prosledjivanje sertifikata, path base, host filtering, WebSocket upgrade i proxy buffering.

Testiraj direktan backend pristup, spoofed forwarding header-e, neispravan host, prevelike ili spore zahteve, client disconnect, proxy retry i deployment drain ponasanje.

### 15. Middleware, Filter I Endpoint Metadata

Napravi tacan redosled middleware-a i endpoint-a iz runtime registracije. Proveri exception handling, status-code pages, HSTS/HTTPS, static files, routing, CORS, authentication, authorization, antiforgery, rate limiting, output cache, session, localization i fallback.

Pregledaj MVC filtere, endpoint filtere, authorization handler-e, model binder-e, convention-e, metadata i route group-e zbog order-dependent bypass-a ili neujednacenog ponasanja.

Fallback policy, group-level zahtev ili convention nisu dovoljni dok negativni testovi ne dokazu da svaki zasticeni endpoint nasledjuje nameravanu kontrolu.

### 16. HTTP Semantika, Greske I OpenAPI

Za svaku rutu proveri method safety/idempotency, content negotiation, media type, status kodove, conditional request-e, cache header-e, pagination, range handling, request limit-e, cancellation i stabilnu semantiku greske.

Koristi Problem Details ili jednako stabilan error ugovor bez stack trace-a, SQL-a, putanje fajla, tajni ili topologije. Sacuvaj correlation identifier bez nebezbednog reflektovanja neproverenih vrednosti.

Uporedi kod, generisani OpenAPI, gateway dokumentaciju, client SDK-ove i posmatrano ponasanje. Contract drift je nalaz i kada server prihvata zahtev.

### 17. Identity, Token, Cookie I Rotacija Kljuca

Mapiraj izdavanje kredencijala, validaciju, cuvanje, refresh, opoziv, logout, account recovery, MFA, device/session management, service identity i emergency disablement.

Proveri OIDC/OAuth state, nonce, PKCE, redirect URI, issuer, audience, signing algoritam, metadata refresh, key rollover, clock skew, token type, scope i sender constraint gde je primenljivo.

Za cookie proveri Secure, HttpOnly, SameSite, path/domain, expiration, sliding renewal, session fixation, kontinuitet key ring-a, consent, antiforgery i ponasanje tokom promene deployment slot-a ili regiona.

### 18. Autorizacija, Tenant Izolacija I Stanje Resursa

Napravi authorization matricu po akteru, ruti ili operaciji, tenant-u, vlasnistvu resursa, stanju resursa i potrebnoj policy. Testiraj dozvoljene i odbijene slucajeve.

Odbij client-controlled tenant, role, owner, price, status ili entitlement polja osim kada se validiraju prema autoritativnom stanju. Scope-uj svaki query, cache key, event, file path i background job na odgovarajuci tenant i principal.

Pregledaj admin, support, impersonation, delegirani pristup, break-glass, batch operacije, export, search i indirect object reference zbog horizontalnog i vertikalnog privilege escalation-a.

### 19. Blazor, Razor I Browser Bezbednost

Kada postoje, razlikuj Blazor Server, WebAssembly, Auto, static SSR, enhanced navigation, Razor Pages, MVC view i API granice. Client-side provere nisu server autorizacija.

Pregledaj component circuit lifetime, reconnect, prerendering, persisted state, JS interop, DOM sink-ove, antiforgery, CSP, XSS encoding, open redirect, file download, refresh authentication stanja i osetljive podatke u browser storage-u.

Testiraj vise tabova, zastarele circuit-e, reconnect posle promene role ili tenant-a, deployment tokom aktivnih circuit-a i propagaciju logout-a ili opoziva.

### 20. Kriptografija, Data Protection I Osetljivi Podaci

Koristi platform primitives i pregledane biblioteke. Popisi encryption, hashing, password hashing, signature, random vrednosti, key derivation, sertifikate, key store i custom kriptografiju.

Proveri algoritam, mod, key size, nonce jedinstvenost, associated data, rotaciju, opoziv, backup, restore, access control, FIPS zahtev gde je primenljiv i migraciju sa starih kljuceva ili algoritama.

Klasifikuj osetljiva polja i sprovedi minimizaciju, retention, deletion, export, masking, log redaction, rad u nizim okruzenjima i zastitu backup-a. Encryption ne zamenjuje autorizaciju.

### 21. Deserialization, Template, Komande I Injection

Pregledaj SQL, LINQ raw fragmente, shell/process izvrsavanje, PowerShell, template-e, regex, XPath, LDAP, putanje fajla, expression parsing, dynamic compilation, reflection activation i archive extraction.

Preferiraj parameterization i allowlist-e. Proveri argumente odvojeno od command stringa, canonical path nakon razresavanja, archive traversal i expansion limit-e i pretpostavke template sandbox-a.

Unsafe deserialization, type-name handling, neproverene plugin-e, Roslyn compilation i expression evaluator-e tretiraj kao code-execution granice koje zahtevaju eksplicitan trust i izolaciju.

### 22. Outbound HTTP, DNS I Resilience Pipeline

Popisi svaku spoljnu zavisnost, client registraciju, base address, DNS ponasanje, handler lifetime, connection pool, proxy, certificate policy, timeout, retry, hedging, circuit breaker, rate limiter i telemetriju.

Koristi jedan end-to-end deadline i izbegni umnozavanje retry-a kroz proxy, client, biblioteku, queue i caller. Ponavljaj samo operacije ciji side effect ne postoji, idempotentan je ili zasticen.

Testiraj DNS promenu, stale konekciju, parcijalni odgovor, throttling, long-tail latenciju, rotaciju sertifikata, proxy kvar, cancellation i oporavak zavisnosti bez retry storm-a.

### 23. Cache, Session, Output Cache I Distribuirana Koordinacija

Za svaki cache definisi vlasnika, key namespace, tenant scope, verziju serialization-a, TTL, invalidation, consistency model, stampede zastitu, maksimalnu velicinu, eviction i ponasanje pri kvaru.

Pregledaj session affinity, distributed session, output caching, authorization-dependent odgovor, user-specific header, velicinu cookie-ja i Data Protection kontinuitet. Nikada ne cache-uj privatni output pod zajednickim kljucem.

Distributed lock i lease zahtevaju fencing ili ekvivalentnu zastitu od zastarelog vlasnika, ogranicenu akviziciju, renewal, cancellation, identitet vlasnika i recovery. Process-local lock nije cluster-wide garancija.

### 24. EF Core Query I Provider Ispravnost

Pregledaj generisani SQL i execution plan za kriticne query-je. Pregledaj translation, client evaluation, parameterization, include, split query, cartesian expansion, projection, tracking, identity resolution, compiled query, pagination i query filter.

Proveri provider-specific ponasanje za SQL Server, PostgreSQL, MySQL, SQLite, Cosmos ili drugi store: isolation, retry, precision, collation, concurrency token, sequence, generated value, JSON, array, timestamp i migracije.

Ne generalizuj EF InMemory ili SQLite rezultat na drugi relational provider. Koristi pravi provider u integration i migration testovima kada ispravnost zavisi od provider ponasanja.

### 25. Transakcije, Konkurentnost, Idempotency I Outbox

Mapiraj granice transakcije kroz EF Core, raw ADO.NET, Dapper, vise DbContext-a, broker, cache i spoljne side effect-e. Izbegni skrivene parcijalne commit-e.

Definisi optimistic ili pessimistic concurrency ponasanje, odgovor na konflikt, retry pravilo, obradu duplog zahteva, lifecycle idempotency zapisa, replay odgovora i zastitu od stale write-a.

Za konzistentnost baze i poruke proceni transactional outbox/inbox ili ekvivalentan trajni dizajn. Testiraj crash tacke pre i posle commit-a, dispatch-a, acknowledgement-a i consumer side effect-a.

### 26. Migracije, Backfill I Zero-Downtime Promena

Pregledaj svaku migraciju i generated SQL zbog lock nivoa, trajanja, table rewrite-a, index build-a, gubitka podataka, default vrednosti, nullability, collation, precision, trigger-a i provider-specific ponasanja.

Koristi expand-and-contract za rolling kompatibilnost. Razdvoji schema promenu, dual-read/write gde je potrebno, backfill, proveru, cutover, cleanup i uklanjanje stare verzije.

Definisi vlasnika migracije, single-run mehanizam, backup/PITR dokaz, canary ili probu, abort kriterijum, forward repair, kompatibilnost application rollback-a i data recovery. Nikada ne pretpostavljaj da rollback aplikacije vraca schema-u ili podatke.

### 27. Messaging, Webhook I Delivery Semantika

Za svakog producer-a i consumer-a dokumentuj message schema/version, partition ili ordering key, delivery garanciju, acknowledgement tacku, retry/backoff, dead-letter pravilo, deduplication, poison handling, replay, retention i observability.

Proveri autorizaciju i tenant scope za objavljene i primljene poruke. Potpisuj i replay-zastiti ulazne webhook-ove; definisi idempotency, retry, secret rotation i delivery dokaz za izlazne webhook-ove.

Testiraj duplikat, promenu redosleda, kasnjenje, parcijalni kvar, broker reconnect, consumer crash, deployment overlap, schema evolution, dead-letter replay i kvar downstream side effect-a.

### 28. Hosted Service, Scheduling I Graciozno Gasenje

Popisi hosted service-e, timer-e, scheduler-e, queue pump-e, cleanup task-ove, cache warmer-e, migration job-ove i leader-elected rad.

Proveri start redosled, readiness zavisnost, kreiranje scope-a, sprecavanje overlap-a, misfire pravilo, clock/time-zone ponasanje, lease ili leadership, ogranicenu konkurentnost, cancellation, final acknowledgement i restart recovery.

Tokom shutdown-a postani unready, zaustavi prijem, postuj ograniceni drain period, zavrsi ili bezbedno napusti rad, sacuvaj checkpoint, zatvori stream i client, flush-uj telemetriju i izadji pre platform kill deadline-a.

### 29. SignalR, SSE I gRPC

Pregledaj autentikaciju i autorizaciju na nivou konekcije i poruke ili metode, tenant routing, origin, connection limit, payload limit, keepalive, idle timeout, reconnect, replay, ordering, backpressure, cancellation i cleanup.

Za gRPC proveri deadline, status mapping, interceptor, metadata limit, reflection exposure, health, retry, load balancing, streaming flow control i protobuf kompatibilnost.

Za SignalR i SSE testiraj sporog klijenta, disconnected klijenta, zastarele grupe, scale-out backplane, deployment drain, opoziv i izolaciju poruke po korisniku ili tenant-u.

### 30. Fajlovi, Object Storage, Arhive I Mediji

Za upload i import sprovedi ukupne i per-file limite, streaming, temporary storage, kvotu, extension plus magic-byte pravilo, malware scanning gde je opravdan, archive traversal i decompression limit, uklanjanje metadata i cleanup.

Privatni storage koristi po default-u. Autorizuj svaki download i signed URL, scope-uj object key na tenant i vlasnika, koristi bezbedan content disposition, spreci path traversal i definisi expiry, revocation, retention, deletion i backup ponasanje.

Za obradu medija ili dokumenata izoluj parser i converter, ogranici CPU/memory/time, proveri patchovanje native zavisnosti i tretiraj generated preview ili thumbnail kao neproveren output.

### 31. Health, OpenTelemetry I Dijagnostika Incidenta

Razdvoji startup, liveness, readiness, degradaciju zavisnosti i business health. Health endpoint mora imati ograniceno izvrsavanje, kontrolisanu izlozenost, stabilnu semantiku i bez curenja tajni ili topologije.

Korelisi log, metric, trace, exemplar, deployment verziju, tenant-safe identifier, dependency call, retry, queue lag, database pool, GC, thread pool, rate limit i poslovni ishod.

Definisi redaction i sampling tako da telemetrija ostane korisna bez curenja tokena, request body-ja, SQL parametara, zdravstvenih podataka, payment podataka ili licnih podataka. Proveri vlasnika alerta, prag, trajanje, severity, dashboard, runbook i eskalaciju.

### 32. CLR, GC, Thread Pool I Kapacitet

Izmeri startup, warmup, throughput, percentile latencije, allocation rate, LOH, GC pause i heap size, thread-pool queue, lock contention, exception, JIT ili AOT ponasanje, CPU, memory, socket, file handle, pool i kapacitet zavisnosti.

Koristi trace, counter, dump, profile ili benchmark primeren pitanju. Dump i trace artefakte zastiti kao osetljive i zabelezi uticaj prikupljanja.

Testiraj realan steady state, burst, soak, degradaciju, overload, recovery i shutdown. Ne povecavaj thread, connection ili pool limit bez modelovanja downstream kapaciteta i failure ponasanja.

### 33. Publish, Trimming, Single-File I Native AOT

Testiraj tacan deployovani publish profil i RID. Proveri odgovornost za servicing framework-dependent naspram self-contained modela, single-file extraction ponasanje, ReadyToRun, trimming warning, reflection metadata, serializer, plugin, lokalizaciju, dijagnostiku i native biblioteke.

Svaki trimming ili AOT warning tretiraj kao compatibility pitanje, ne kao buku. Ne dodaj siroke suppression-e ili descriptor-e bez testa koji dokazuje da potrebno ponasanje prezivljava publish.

Uporedi build output sa finalnim image/package artefaktom i pokreni publish smoke, startup, endpoint, migration, diagnostics i shutdown provere u stvarnom hosting modelu.

### 34. Container, IIS, Windows Service I systemd

Za container proveri zvanicni podrzani base image, digest pravilo, OS lifecycle, non-root identitet, port, filesystem permission, read-only mogucnost, ICU/globalization, sertifikate, native zavisnosti, signale, probe, resource limit, SBOM i image scan.

Za IIS proveri hosting bundle, in-process ili out-of-process model, app pool identitet, bitness, ANCM podesavanja, web garden/farm ponasanje, Data Protection, stdout log, recycle, overlapped restart, request limit i proxy header.

Za Windows service ili systemd proveri service identity, zavisnosti, working directory, environment, restart policy, watchdog, stop timeout, privilegije, log destinaciju, upgrade proceduru i rollback.

### 35. CI/CD, Promocija Artefakta I Supply Chain

Mapiraj trigger, pull-request trust, fork ponasanje, runner izolaciju, permission, secret access, dependency restore, instalaciju alata, testove, signing, SBOM, provenance, retention artefakta, promociju, environment approval i deployment identity.

Pinuj ili drugacije kontrolisi action, template, container, alat i script. Razdvoji build od deployment-a i promovisi isti nepromenljivi artefakt umesto rebuild-a za svako okruzenje.

Proveri branch protection, required check, review ownership, emergency putanju, segregation of duties gde je zahtevano, audit log, odgovor na kompromitovan runner, rotaciju signing kljuca i opoziv artefakta.

### 36. Deployment, Rollout, Rollback I Disaster Recovery

Definisi preflight, redosled migracije, rollout strategiju, compatibility window, health i business gate, canary metriku, observation period, abort uslov, vracanje saobracaja, application rollback, forward repair i data recovery.

Testiraj deployment sa aktivnim zahtevima, stream-ovima, job-ovima i dugim transakcijama. Proveri da stara i nova verzija mogu koegzistirati tokom planiranog prozora i da rollback ne vraca nekompatibilne reader-e ili writer-e.

Dokazi backup restore i, gde je zahtevano, point-in-time recovery u izolovanom okruzenju. Zabelezi postignuti RPO/RTO, zavisnosti, kredencijale, kontinuitet key ring-a, message replay, DNS ili traffic korake i akcije vlasnika.

### 37. Incident Mode I Forenzicka Spremnost

Sacuvaj timestamp, deployment revision, log, trace, audit zapis, stanje baze i broker-a, pogodjene identitete, artifact digest i volatile dokaz pre cleanup-a kada je bezbedno.

Ogranici incident najmanjim blast radius-om, vodi decision log, rotiraj kompromitovane kredencijale ili kljuceve, opozovi pogodjeni artefakt ili session, vrati servis iz pouzdanih komponenti i proveri eradication.

Dokumentuj detection gap, root cause, impact window, pogodjene podatke i tenant-e, recovery dokaz, residual risk, corrective action, vlasnika, rok i lekciju koja menja test, alert, runbook ili arhitekturu.

### 38. Migration Audit Dodatak

Za .NET Framework ka modernom .NET-u, legacy ASP.NET ka ASP.NET Core-u, EF6 ka EF Core-u, WCF ka podrzanim alternativama, staru autentikaciju ili Newtonsoft.Json ka System.Text.Json napravi feature i behavior compatibility matricu.

Popisi nepodrzane API-je, Windows-only zavisnosti, serialization razlike, threading pretpostavke, konfiguraciju, identity, session, caching, putanje fajla, globalizaciju, ponasanje baze, deployment, observability i operativne alate.

Koristi migration talase, adaptere, strangler ili dual-run gde je opravdano, shadow poredjenje, contract testove, data reconciliation, rollback i kriterijum uklanjanja starog sistema. Ne spajaj framework migraciju, architecture rewrite, redizajn baze i feature rad bez eksplicitne kontrole rizika.

