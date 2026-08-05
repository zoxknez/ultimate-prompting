## Faza 27 - Testiranje, Contract-i, Fuzzing, Load I Capacity Dokaz

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Napravi risk-based test piramidu koja pokriva logiku, adapter-e, database-e, broker-e, provider-e, HTTP, klijente i operacije.
- Koristi production-like verzije i semantiku za database-e, queue-ove, cache, proxy-je i filesystem-e kada je ponasanje vazno.
- Dodaj negative authorization, tenant, validation, injection, SSRF, replay, concurrency, timeout, abort i partial-failure testove.
- Koristi property-based ili fuzz testiranje za parser-e, scheme, state machine-e, identifikatore i protocol granice gde je korisno.
- Proveri OpenAPI, generisane klijente, consumer contract-e, migracije, message scheme i old-new kompatibilnost.
- Pokreni cold, warm, burst, sustained, soak, failover, dependency-slow i recovery testove sa eksplicitnim acceptance pragovima.

### Obavezni Dokazi

- Proizvedi i sacuvaj risk-to-test i P0-P2 regression matricu.
- Proizvedi i sacuvaj contract, compatibility, fuzz i failure rezultate.
- Proizvedi i sacuvaj load, soak, capacity i cost dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da parallel i replay scenariji cuvaju invarijante.
- Dokazi da malformed i adversarial input ostaje ogranicen.
- Dokazi da performance i capacity pragovi ostaju ispunjeni pod reprezentativnim load-om.

