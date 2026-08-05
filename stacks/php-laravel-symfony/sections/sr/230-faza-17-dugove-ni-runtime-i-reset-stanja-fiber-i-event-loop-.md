## Faza 17 - Dugovečni runtime-i, reset stanja, fiber-i, event loop-ovi i konkurentnost

### Cilj

Dokaži da reuse worker-a i konkurentno izvršavanje ne cure request stanje, ne iscrpljuju resurse i ne krše lifecycle pretpostavke.

### Zahtevi audita

- Inventariši PHP-FPM, RoadRunner, Swoole, OpenSwoole, FrankenPHP, Laravel Octane, ReactPHP, Amp, Messenger, queue i custom daemon procese.
- Klasifikuj static, global, singleton, service, container, connection, logger, locale, auth, tenant, tracing i temporary-file stanje po lifetime-u.
- Proveri reset hook-ove, scoped service-e, container reset, request cleanup, transaction cleanup, health konekcija, čišćenje privremenih resursa i memory limite.
- Audituj Fiber i coroutine cancellation, suspension, context propagation, exception handling, concurrent mutation, sinhronizaciju i nebezbedne shared object-e.
- Pregledaj event-loop blocking, CPU rad, filesystem i network pozive, DNS, subprocess-e, database klijente, backpressure, bounded queue-ove i starvation.
- Testiraj sekvencijalne cross-user zahteve na jednom worker-u, konkurentne zahteve, cancellation, timeout, worker crash, max-request recycle i deployment drain.

### Obavezni dokazi

- Runtime i state-lifetime matrica za svaki procesni model.
- Dokaz cross-request leakage, concurrency, cancellation, blocking, memory-growth i recycle testova.
- Dokaz drain-a i zamene worker-a za deployment-e i emergency revocation.

### Kriterijumi prihvatanja

- Nijedno request, user, tenant, locale, credential, transaction ili trace stanje ne preživljava svoj autorizovani lifetime.
- Konkurentnost i dugovečno izvršavanje ostaju ograničeni, cancellable, observabilni i bezbedno zamenljivi.

