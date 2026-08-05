## 26. Pouzdanost, failure mode-ovi i chaos validacija

**Cilj:** Potvrdi otpornost kroz kontrolisane failure eksperimente zasnovane na hipotezama.

### 26.1 Obavezne provere

1. Napravi failure-mode and effects analizu za zavisnosti, zone, regione, nodove, control plane, DNS, identity, KMS, registre, storage, redove, baze, observability i third-party sisteme.
2. Za svaki eksperiment definisi hipotezu, steady-state indikatore, opseg, vlasnika, odobrenja, safety kontrole, blast radius, stop uslove, recovery korake i dokaze.
3. Zajedno testiraj timeout, retry, backoff, jitter, circuit breaker, bulkhead, queue, rate-limit, load-shed, cache, fallback i idempotency ponasanje.
4. Ubacuj realnu latenciju, greske, partial response, gubitak mreze, zastarele podatke, clock skew, nedostupnost zavisnosti, process death, gubitak noda i zone u odobrenom okruzenju.
5. Proveri da retry ne amplifikuje load, ne duplira side effect-e, ne krsi redosled, ne iscrpljuje pool-ove i ne skriva trajni otkaz.
6. Proveri da graceful degradation stiti kriticne tokove i integritet podataka umesto da samo vraca healthy status.
7. Ponovi korigovane eksperimente i sacuvaj before-and-after dokaze.

### 26.2 Minimalni dokazi

- Matrica failure mode-ova sa ocekivanim i uocenim ishodima.
- Odobrene definicije eksperimenata i zabelezena telemetrija.
- Dokaz oporavka i ponovljenog testa nakon popravki.

### 26.3 Kriterijumi izlaza

1. Kriticne pretpostavke otkaza su eksperimentalno potvrđene unutar bezbednih granica.
2. Retry, fallback i degradation cuvaju podatke i izbegavaju kaskadni otkaz.
3. Runbook-ovi i alarmi odrazavaju uoceno ponasanje otkaza.

