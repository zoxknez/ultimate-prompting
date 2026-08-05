## 3. Validacija, Autentikacija I Autorizacija

Tretiraj svaki path/query/header/cookie/form/file/JSON payload, gRPC poruku, WebSocket poruku, webhook, queue poruku, scheduled input, konfiguracionu vrednost i generisanu vrednost kao nepoverljivu. Validiraj tip, format, enum, numericka/string ogranicenja, Unicode normalizaciju, dubinu objekta, broj elemenata kolekcije, nepoznata polja, velicinu fajla i semanticka poslovna pravila. Bean Validation ne zamenjuje autorizaciju ili semanticku validaciju. Eksplicitno mapiraj dozvoljena DTO polja u domenske izmene da sprecis mass assignment.

Auditiraj registraciju/login, password hashing, reset/email verifikaciju, MFA, account lockout/rate limit, session fixation, cookie flagove, OIDC/OAuth redirect URI/state/nonce/PKCE, JWT potpis/issuer/audience/expiry/key rotation, refresh-token rotaciju/revokaciju/detekciju reuse-a, API kljuceve, logout, invalidaciju aktivnih sesija i user enumeration. Koristi framework i identity-provider protokole; ne izmisljaj token ili kriptografske formate.

Svaka zasticena operacija mora nezavisno dokazati identitet, authority/policy, vlasnistvo, tenant opseg, stanje resursa i validan prelaz. Pregledaj `authorizeHttpRequests`, matcher redosled, method security, `@PreAuthorize`, custom `AuthorizationManager`, service-layer provere, repository filtere, async executor security-context propagaciju i actor context message consumera. Testiraj BOLA/IDOR, horizontalnu/vertikalnu eskalaciju, samo-UI provere, client-supplied tenant ID, unscoped upite, javne exporte/downloadove, nested-resource pristup i zastarela prava. Request autorizacija nije dovoljna za object ownership.

Za namerno javne/static putanje preferiraj eksplicitan `permitAll` umesto zaobilazenja celog security chaina, tako da security headeri i druge zastite ostanu aktivni. Za browser cookie upise proveri CSRF, SameSite, origin/referrer ili Fetch Metadata provere i precizne CORS credentials/origin. CORS nije autorizacija.

