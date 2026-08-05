## Faza 15 - Autentikacija, sesije, OAuth/OIDC i account lifecycle

Dokazi kompletan identity lifecycle kroz browser, server, provider-e, sesije, uredjaje, role, revocation i recovery.

### Zahtevi audita

- Inventarisi login, registraciju, invitation, linking, reset, magic link, MFA, passkey, reauth, logout i recovery.
- Proveri issuer, audience, nonce, state, PKCE, redirect URI, token algoritam, clock skew, key rollover i provider mix-up otpornost.
- Pregledaj session storage, cookie flag-ove, domain/path, rotaciju, fixation, expiry, concurrency, revocation i rights propagation.
- Razdvoji autentikaciju od autorizacije i postavi guard na mestu koriscenja podataka.
- Spreci enumeration, stuffing, reset replay, email-change takeover, unsafe linking i stale privilegovane sesije.
- Osiguraj da logout, disable, uklanjanje role/tenant-a, promena lozinke i key rotation invalidiraju nameravane sesije i cache-eve.

### Obavezni dokazi

- Identity flow i session-state dijagrami.
- Provider konfiguracija i token-validation dokaz.
- Cookie i session posmatranja iz stvarnih response-a i storage-a.
- Revocation i rights-change propagation merenja.

### Obavezni failure i acceptance testovi

- Pokusaj login CSRF, state/nonce replay, redirect substitution, audience mismatch i provider mix-up.
- Koristi sesiju posle logout-a, promene lozinke, uklanjanja role, tenant-a, disable-a i key rollover-a.
- Povezi identitete sa konfliktnim ownership-om i spreci takeover.
- Izvrsi paralelni refresh ili session rotaciju iz vise tab-ova i uredjaja.

