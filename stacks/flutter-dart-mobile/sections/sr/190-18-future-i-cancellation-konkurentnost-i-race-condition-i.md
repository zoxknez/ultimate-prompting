## 18. Future-i, cancellation, konkurentnost i race condition-i

Dart je single-threaded po isolate-u, ali aplikacije i dalje imaju asinhrone race condition-e, native konkurentnost, više isolate-a i distribuirane konflikte.

- Prati svaki kritični Future lanac, callback, completer, timer, microtask, post-frame callback, retry, debounce, throttle i cancellation granicu.
- Otkrij use-after-dispose, setState posle dispose-a, prepisivanje zastarelim odgovorom, duplu predaju, preklopljeni refresh, izgubljen update, duplu navigaciju i ponovljene side effect-e.
- Proveri cancellation ili potiskivanje zastarelog rezultata kada se promeni ruta, query, nalog, tenant, uređaj, locale, filter ili sesija.
- Audituj mutex, lock, semaphore, queue, single-flight, lease, idempotency-key, optimistic concurrency, version i compare-and-set strategije gde su potrebne.
- Proveri da UI deduplikacija ne zamenjuje serversku idempotentnost i autorizaciju za plaćanja, porudžbine, mutacije, upload-e i destruktivne akcije.
- Testiraj brzo ponovljen input, sporu mrežu, timeout, reconnect, retry, pauziranje aplikacije, promenu sata, token refresh, dupli push i preklapanje stare/nove verzije.
- Sačuvaj correlation ID-jeve i stanje operacije kroz retry-je da telemetrija razlikuje jednu logičku operaciju od duplih izvršenja.
- Zahtevaj determinističke concurrency testove sa kontrolisanim satovima, fake transportima, barijerama i fault injection-om za materijalne race-ove.

