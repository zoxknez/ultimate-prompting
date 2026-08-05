## Faza 11 - Error Handling, Process Failure, Crash Politika I Shutdown

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Definisi error kategorije za validaciju, autentikaciju, autorizaciju, conflict, rate limit, dependency, timeout, cancellation, invariant i interni kvar.
- Mapiraj svaku kategoriju na stabilan status, code, bezbednu poruku, retry smernicu, request ID i telemetry severity.
- Spreci curenje stack-a, SQL-a, filesystem putanje, token-a, internog host-a, header-a i detalja zavisnosti.
- Eksplicitno obradi rejected promise-e, callback greske, stream greske, emitter greske i background task kvarove.
- Definisi uncaughtException, unhandledRejection, fatal error, OOM i native crash politiku; nikada ne nastavljaj u nepoznatom stanju.
- Na SIGTERM ili shutdown povuci readiness, zaustavi intake, drain-uj request-e i job-ove, zatvori pool-ove, flush-uj telemetry i izadji u roku.

### Obavezni Dokazi

- Proizvedi i sacuvaj error taxonomy i response contract.
- Proizvedi i sacuvaj fatal-process, restart i crash-loop politiku.
- Proizvedi i sacuvaj shutdown ownership i timing dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da rejected promise ispravno zavrsava request jednom.
- Dokazi da fatalna process greska vodi kontrolisanoj zameni.
- Dokazi da shutdown tokom dugih request-a i job-ova prati dokumentovanu recovery putanju.

