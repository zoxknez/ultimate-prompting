## 3. Validacija, Autentikacija I Autorizacija

Tretiraj svaki ulaz kao nepoverljiv. DTO binding nije autorizacija. Spreci over-posting eksplicitnim mapiranjem.

Auditiraj Identity/login/password/MFA/lockout, cookie/session, OIDC/OAuth (redirect URI, state/nonce/PKCE), JWT (signature/issuer/audience/lifetime/clock skew/rotation), refresh token, API keys, logout, user enumeration.

Svaka zasticena operacija mora dokazati identity, policy, ownership, tenant, resource state i validan prelaz. Pronadji BOLA/IDOR, UI-only checks, client-supplied tenant, unscoped queries. Role nije dovoljna kada su bitni ownership ili stanje.

Za cookie browser write: antiforgery, SameSite, origin/Fetch Metadata, precizan CORS. CORS nije autorizacija. Data Protection key ring mora biti perzistiran i deljen u multi-replica okruzenju.

