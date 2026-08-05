## Spring Security, Tenancy I Privilegovani Pristup

### Efektivni Security Filter Chain-ovi

- Popiši svaki `SecurityFilterChain`, matcher, order, authentication provider, filter, entry point, access-denied handler, session policy, CSRF pravilo, CORS pravilo i exception putanju.
- Dokaži koji chain štiti svaki endpoint i management površinu; testiraj overlap, praznine, fallback pravila, dispatcher type-ove, async dispatch, error dispatch i forwarded request-e.
- Uporedi method-security annotation-e i advisor-e sa HTTP security-jem; nijedan sloj ne nadoknađuje neproverenu prazninu u drugom.
- Testiraj direktnu controller/service invokaciju, interno prosleđivanje, scheduled invokaciju, message listener-e, GraphQL resolver-e, WebSocket poruke i ne-HTTP entry point-e.
- Fail closed kada authentication infrastruktura, key discovery, policy podaci, tenant lookup ili authorization zavisnosti nisu dostupne osim ako postoji pregledan degraded mode.

### Authentication, Session, OAuth I OIDC

- Audituj password, MFA, passkey, API key, mTLS, service account, OAuth 2.0, OpenID Connect, SAML, LDAP i custom authentication tokove koji su stvarno uključeni.
- Proveri issuer, audience, algoritam, key use, key rotation, clock skew, nonce, state, PKCE, redirect URI, token type, token binding gde je primenljivo i logout semantiku.
- Za browser session proveri cookie scope, `Secure`, `HttpOnly`, `SameSite`, fixation zaštitu, rotaciju, concurrency limite, idle i absolute expiry, remember-me i serversku invalidaciju.
- Testiraj revoked, expired, not-yet-valid, wrong-issuer, wrong-audience, wrong-tenant, wrong-client, downgraded, duplirane i malformed kredencijale.
- Drži refresh token-e, client secret-e, signing key-eve, session identifikatore i authentication trace podatke van logova, metrika, URL-ova, browser storage-a i support export-a.

### Object Authorization I Tenant Izolacija

- Definiši authorization za akciju, resurs, tenant, owner-a, state, relaciju, polje i svrhu; role provere same nisu dovoljne za object pristup.
- Testiraj BOLA/IDOR zamenom identifikatora, parent resursa, tenant header-a, claim-ova, path variable-a, query parametara, batch stavki, export-a i indirektnih referenci.
- Sprovedi tenant constraint u svakom repository-ju, query-ju, cache key-u, poruci, file putanji, search index-u, event-u, async task-u i administrativnom toku.
- Proveri da tenant context ne može biti dostavljen ili promenjen od nepoverljivog klijenta osim ako je nezavisno vezan za autentifikovani autoritet.
- Testiraj curenje context-a kroz reuse thread-a, Reactor context, scheduled job-ove, deljene cache-eve, pooled klijente, retry, dead letter-e, logove, metrike i trace-ove.

### Administrativne, Impersonation I Break-Glass Putanje

- Inventariši admin endpoint-e, konzole, Actuator operacije, support alate, data export-e, replay alate, migracije, repair skripte, feature override-e i emergency kontrole.
- Zahtevaj jaču autentifikaciju, least privilege, vezivanje za svrhu, odobrenje gde je primenljivo, vremenska ograničenja, odvojenu session i audit zapise otporne na izmenu.
- Za impersonation sačuvaj originalnog aktera, efektivnog aktera, razlog, tenant, scope, početak/kraj, odobrenja i svaku izvršenu akciju; nikada tiho ne zameni identitet.
- Testiraj confused-deputy putanje gde privilegovani servis izvršava akciju koristeći korisnički kontrolisane identifikatore, destinacije, template-e, query-je ili callback-ove.
- Proveri da su break-glass kredencijali recoverable, rotirani posle upotrebe, nadzirani, testirani i nedostupni normalnom application kodu ili CI logovima.

### Browser Bezbednost, CORS, CSRF I Header-i

- Proveri CORS origin-e, metode, header-e, credentials, preflight caching, wildcard ponašanje, proxy rewriting i environment-specifične origin liste.
- Primeni CSRF zaštitu na cookie-authenticated state promene, login, logout, token binding i osetljive browser tokove; dokumentuj opravdane izuzetke.
- Pregledaj CSP, HSTS, frame ancestors, content-type options, referrer policy, permissions policy, cache control, cross-origin policy-je i ponašanje error stranica.
- Testiraj host-header injection, open redirect, origin confusion, DNS rebinding gde postoje lokalni servisi, clickjacking, MIME confusion i mixed-content putanje.
- Ne izlaži token-e, tajne, internu topologiju, stack trace, korisničke podatke ili privilegovane akcije kroz generisanu dokumentaciju, Actuator, GraphiQL, Swagger UI ili debug stranice.


