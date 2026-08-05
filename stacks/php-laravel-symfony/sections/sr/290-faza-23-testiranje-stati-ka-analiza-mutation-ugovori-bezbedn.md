## Faza 23 - Testiranje, statička analiza, mutation, ugovori, bezbednost, load i recovery

### Cilj

Izgradi risk-driven verification matricu koja dokazuje ponašanje kroz runtime režime, framework putanje, kvarove i release-e.

### Zahtevi audita

- Inventariši PHPUnit, Pest, Codeception, Behat, Panther, browser, API, integration, database, queue, contract, property, fuzz i end-to-end testove.
- Pokreni PHPStan ili Psalm, framework extension-e, coding standard-e, deprecation provere, architecture pravila, dependency provere i secret scanning na opravdanoj strogoći.
- Koristi mutation testing na kritičnoj business, authorization, validation, idempotency, transaction i recovery logici gde dodaje signal.
- Proveri testove kroz podržane PHP verzije, framework linije, database engine-e, cache i queue backend-e, FPM i dugovečne runtime-e i deployment režime.
- Uključi malformed, hostile, concurrent, timeout, duplicate, replay, stale-state, crash, shutdown, mixed-version, restore i rollback scenarije.
- Prati flaky testove, quarantine ownership, retry policy, coverage gap-ove, production incident regresije i obrazloženje acceptance pragova.

### Obavezni dokazi

- Risk-to-test matrica povezana sa kritičnim tokovima i nalazima.
- Matrica testiranja podržanih runtime-a i zavisnosti sa tačnim verzijama i backend-ima.
- Sirovi rezultati statičkih, unit, integration, contract, security, load, migration, restore i rollback provera.

### Kriterijumi prihvatanja

- Svaka P0 i P1 kontrola ima deterministički automatizovan test ili dokumentovan snažniji metod verifikacije.
- Zeleni suite se ne prihvata kada relevantni runtime, backend, failure mode ili release tranzicija nije izvršena.

