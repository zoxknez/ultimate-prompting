## Faza 12 - Autentikacija, Session-i, Token-i I Service Identity

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Audituj registration, invitation, login, MFA, passkey, reset, recovery, linking, reauthentication, logout i zatvaranje naloga.
- Proveri parametre password hashing-a, politiku, breached-password strategiju, lockout, throttling i otpornost na enumeraciju.
- Za session-e proveri otpornost na fixation, rotaciju, secure cookie flag-ove, durable store, tenant scope, expiry i revocation.
- Za JWT i OIDC proveri issuer, audience, algorithm allowlist, potpis, key rotation, expiry, nonce, state, PKCE i redirect URI.
- Za refresh token-e proveri rotaciju, family tracking, reuse detection, session binding i odgovor na kompromitovanje.
- Za API key-eve i service identitete proveri scope, hashing, display-once ponasanje, rotaciju, revocation, attribution i rate limit.

### Obavezni Dokazi

- Proizvedi i sacuvaj authentication-flow i credential matricu.
- Proizvedi i sacuvaj session i token lifecycle tabelu.
- Proizvedi i sacuvaj key rotation, revocation i compromise dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da session identifikator se rotira pri promeni privilegija.
- Dokazi da refresh-token reuse se detektuje i contain-uje.
- Dokazi da pogresan issuer, audience, algoritam ili kljuc se odbija.

