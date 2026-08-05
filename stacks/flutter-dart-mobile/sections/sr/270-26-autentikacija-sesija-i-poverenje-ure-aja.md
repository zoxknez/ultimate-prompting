## 26. Autentikacija, sesija i poverenje uređaja

Autentikacija mora da preživi zlonameran ulaz, lifecycle prekid, rotaciju tokena, rad na više uređaja i promenu naloga.

- Mapiraj sign-in, registraciju, verifikaciju, MFA, passkey, biometric unlock, recovery, refresh, logout, logout-all, enrollment uređaja i brisanje naloga.
- Proveri OAuth/OIDC authorization code sa PKCE, vlasništvo redirect URI-ja, state, nonce, issuer, audience, potpis, clock skew, tip tokena i rotaciju ključeva.
- Čuvaj samo potrebne tajne u platformski odgovarajućem zaštićenom storage-u; proveri lock stanje, backup/restore, migraciju uređaja, rooted/jailbroken ponašanje i uninstall semantiku.
- Audituj refresh single-flight, rotaciju tokena, opoziv, replay, konkurentnu obradu 401, retry zastarelog zahteva, background refresh i UX isteka sesije.
- Odvoji lokalnu biometrijsku pogodnost od serverske autentikacije i autorizacije; definiši fallback, lockout, re-enrollment i odgovor na kompromitovan uređaj.
- Obezbedi da logout i promena naloga očiste memoriju, cache, baze, fajlove, notifikacije, background rad, realtime subscription-e, WebView-e i screenshot-e prema zahtevu.
- Testiraj duple callback-ove, otkazan browser login, pogrešan redirect, deep-link hijack, offline login, istekle ključeve, promenjenu lozinku, opozvan uređaj i stare/nove verzije aplikacije.
- Ne loguj kredencijale, tokene, authorization code-ove, biometrijske rezultate, recovery podatke ili osetljive identity claim-ove.

