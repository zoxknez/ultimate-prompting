## Faza J - Authentication, Authorization I Data Protection

Utvrdi auth model: cookie, Identity, JWT bearer, OAuth2/OIDC, API key, mTLS, multiple schemes, fallback/default policy.

Proveri autentikaciju: issuer/audience/signature/algorithm, key rotation, JWKS, exp/nbf/clock skew, refresh-token rotacija/revokacija/reuse detekcija, security stamp, session revocation, MFA, user enumeration. Validan potpis nije dovoljan ako token nije namenjen ovom API-ju.

Svaka zasticena operacija mora nezavisno dokazati: identitet, policy/role/claim, vlasnistvo, tenant opseg, stanje resursa i validnu promenu stanja. Testiraj BOLA/IDOR, horizontalnu/vertikalnu eskalaciju, client-supplied tenant ID, unscoped upite, javne exporte, nested resurse, zastarela prava. Role provera nije dovoljna kada su bitni ownership ili stanje.

Cookie: Secure, HttpOnly, SameSite, domain/path, expiration, session fixation, key ring, multi-replica.

Data Protection: gde se cuvaju kljucevi, da li opstaju kroz restart, dostupnost svim replikama, encryption at rest, application name/discriminator, rotation, permissions, backup/DR. Ephemeral key ring u productionu invalidira cookies, antiforgery i zasticene payload-e pri restartu.

CSRF/antiforgery: odluku zasnuj na credential modelu. Ne iskljucuj antiforgery samo zato sto endpoint vraca JSON. CORS nije autorizacija; proveri exact origin allowlist, credentials, wildcard, preflight, middleware order.

