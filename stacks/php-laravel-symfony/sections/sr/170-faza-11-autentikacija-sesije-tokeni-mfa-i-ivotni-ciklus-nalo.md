## Faza 11 - Autentikacija, sesije, tokeni, MFA i životni ciklus naloga

### Cilj

Dokaži identity, session, credential, token, recovery i account lifecycle kontrole kroz svaku application površinu.

### Zahtevi audita

- Inventariši svaki guard, firewall, authenticator, provider, session store, API token, OAuth ili OIDC klijent, passwordless tok, MFA metod i machine identity.
- Proveri password hashing politiku, rehash ponašanje, rate limite, odbranu od credential stuffing-a, breached-password postupanje i bezbedne recovery tokove.
- Audituj session fixation, regeneraciju, idle i apsolutni expiry, paralelne sesije, opoziv uređaja, cookie atribute, storage i logout invalidaciju.
- Validiraj JWT, OAuth i OIDC issuer, audience, algoritam, nonce, state, PKCE, key rotation, clock skew, refresh rotaciju i replay postupanje.
- Audituj MFA enrollment, challenge, recovery kodove, trusted device, downgrade, zamenu faktora, step-up autentikaciju i support override.
- Pregledaj registraciju, email ili phone verifikaciju, invitation, suspenziju, brisanje, anonimizaciju, export, reaktivaciju i prenos vlasništva.

### Obavezni dokazi

- Matrica autentikacije i account stanja za browser, API, console, worker, webhook i machine klijente.
- Negativni testovi za fixation, replay, opozvane sesije, rotirane ključeve, zastarele recovery linkove i MFA downgrade.
- Dokaz rotacije kredencijala i signing ključeva bez prinudnog nebezbednog downtime-a.

### Kriterijumi prihvatanja

- Opozvani, istekli, replay-ovani, downgraded ili cross-account kredencijali ne mogu da autentikuju niti zadrže privilegiju.
- Recovery i support workflow-i su najmanje jednako snažno zaštićeni i auditovani kao normalan sign-in.

