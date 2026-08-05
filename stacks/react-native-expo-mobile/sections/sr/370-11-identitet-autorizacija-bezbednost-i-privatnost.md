## 11. Identitet, autorizacija, bezbednost i privatnost

### 11.1 Autentikacija i session lifecycle
- Auditiraj password, OAuth 2.0, OIDC, social login, magic link, device code, MFA, passkey, biometric unlock, API key i enterprise identity tokove koji stvarno postoje.
- Proveri state, nonce, PKCE, redirect URI, issuer, audience, algoritam, key rollover, clock skew i deep-link handoff.
- Posebno definisi semantiku access token-a, refresh token-a, session-a, registracije uredjaja, biometric gate-a i lokalnog otkljucavanja.
- Testiraj refresh race, replay, opoziv, logout, reset lozinke, deaktivaciju naloga, gubitak uredjaja, reinstall, restore i promenu naloga.
- Ne tretiraj biometriju ili posedovanje uredjaja kao serversku autorizaciju osim kada protokol eksplicitno dokazuje to svojstvo.
- Spreci pojavu tokena i osetljivih identity podataka u URL-u, logovima, analytics-u, crash report-u, clipboard-u, screenshot-u, backup-u ili bundle sadrzaju.

### 11.2 Autorizacija, BOLA i tenant izolacija
- Napravi authorization matricu za svaki read, mutation, upload, download, share, export, deep link, notification akciju, native mogucnost i background operaciju.
- Zahtevaj serversku autorizaciju za resource ownership, rolu, tenant, entitlement, subscription i state tranziciju.
- Testiraj direktnu zamenu identifikatora, stale cache dozvolu, replay offline akcije, promenu naloga, promenu tenant-a, restore navigaciju i notification akciju.
- Ukljuci tenant i authorization dimenzije u lokalne kljuceve, cache kljuceve, query kljuceve, fajlove, redove baze, queue, logove i telemetriju.
- Auditiraj admin, support, impersonation, family, delegated, shared-device, enterprise-managed i break-glass tokove.
- Proveri da logout i brisanje naloga ponistavaju ili uklanjaju svaki tenant-scoped artefakt i pending operaciju.

### 11.3 Secure storage, kriptografija i poverenje u uredjaj
- Popisi Keychain, Keystore, SecureStore, enkriptovanu bazu, fajlove, AsyncStorage, MMKV, preference, cookie, WebView storage, logove i backup.
- Klasifikuj svaku sacuvanu vrednost po osetljivosti, retention-u, backup podobnosti, dostupnosti dok je uredjaj zakljucan, biometric zahtevu, sharing grupi i pravilu brisanja.
- Koristi platformske kriptografske API-je i verzionisane envelope; auditiraj jedinstvenost nonce-a, rotaciju kljuca, algorithm agility, migraciju, korupciju i oporavak.
- Ne hardkoduj tajne, privatne kljuceve, certificate pin-ove, update signing kljuceve, backend kredencijale ili privilegovane API tokene u klijentske artefakte.
- Tretiraj root, jailbreak, hooking, instrumentation, emulator i tamper detekciju kao signal rizika, a ne nepogresivu authorization kontrolu.
- Testiraj migraciju uredjaja, OS upgrade, reinstall, backup restore, invalidaciju kljuca, promenu biometric enrollment-a i kvar secure hardware-a.

### 11.4 Privatnost i upravljanje podacima
- Mapiraj licne, osetljive, finansijske, zdravstvene, decje, lokacijske, biometrijske, advertising, diagnostics i device podatke od prikupljanja do brisanja.
- Proveri consent, purpose limitation, data minimization, retention, export, brisanje, access request i regional transfer ponasanje.
- Uskladi stvarno ponasanje SDK-a sa privacy policy, store deklaracijama, Apple privacy manifest-om, required-reason API-jima i Google Play Data safety.
- Auditiraj prikupljanje analytics, attribution, advertising, crash, support, experimentation, session replay, push, maps i payment SDK-a.
- Obezbedi korisniku vidljive kontrole gde su potrebne i dokazi da opt-out sprecava prikupljanje, a ne samo skriva UI.
- Testiraj brisanje i logout kroz lokalno skladiste, native SDK storage, WebView storage, pending upload, cache, push registraciju i backend stanje.

