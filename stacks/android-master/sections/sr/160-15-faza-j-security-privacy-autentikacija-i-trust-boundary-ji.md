## 15. Faza J - Security, Privacy, Autentikacija I Trust Boundary-ji

### 15.1 Komponente, Intent-i, Deep Link-ovi I IPC

1. Pregledaj svaku exported activity, service, receiver, provider, intent filter, permission i package-visibility query.
2. Zahtevaj da `android:exported` i custom permission odgovaraju stvarnim caller-ima.
3. Validiraj sve ulazne intent-e, extra-e, clip-ove, URI-je, bundle-ove, pending intent-e i Binder input.
4. Koristi immutable ili odgovarajuce scoped PendingIntent-e i spreci intent redirection.
5. Proveri da broadcast receiver-i, foreground service-i, job-ovi i provider-i sprovode caller i data permission.
6. Proveri da content-provider selection, projection, sort order, file descriptor i URI grant ne mogu izloziti proizvoljne podatke.
7. Testiraj malicious external app scenario za svaki public entry point.
8. Proveri da app link, custom scheme, OAuth callback i share target ne mogu biti hijack-ovani ili confused.

### 15.2 Autentikacija, Session I Autorizacija

1. Mapiraj autentikaciju, token storage, refresh, logout, account switching, biometric gate i server-side autorizaciju.
2. Device-side provere tretiraj kao UX ili defense in depth, a ne kao jedinu authorization boundary.
3. Proveri da je svaki osetljivi API poziv server-side autorizovan za resurs i nalog.
4. Proveri token expiry, clock skew, revocation, refresh rotation, replay i concurrent refresh handling.
5. Proveri da logout cisti sve account-bound podatke, cache, notification, download, cookie, WebView i background rad.
6. Proveri da multi-account state ne curi kroz baze, repository-je, worker-e, notification-e, widget-e ili media session-e.
7. Proveri da je biometric upotreba vezana za ispravnu cryptographic ili product semantiku i da ima bezbedan fallback policy.
8. Testiraj rooted, debug, hooked, tampered, offline i restored-device scenario prema stvarnom threat model-u.
9. Ne tvrdi da root ili integrity detection cine client-side tajne ili autorizaciju bezbednim.

### 15.3 Tajne, Keystore I Kriptografija

1. Identifikuj hardkodovane tajne, embedded kredencijale, private key-eve, signing materijal i reverzibilnu obfuscation.
2. Pretpostavi da se sve sto se isporuci u aplikaciji moze izvuci.
3. Koristi Android Keystore za odgovarajuce device-bound kljuceve i proveri authentication, invalidation, backup, rotation i hardware support semantiku.
4. Proveri da encrypted storage ne koristi static key, fixed IV, insecure mode ili unauthenticated encryption.
5. Proveri cryptographic algoritme, parametre, random generation, encoding i key derivation prema aktuelnim platform smernicama.
6. Izbegavaj custom cryptography.
7. Proveri secret deletion, logout, device migration, reinstall i promene lock screen-a.
8. Proveri da network ili backend dizajn ne zahteva nepovratnu tajnu unutar APK-a.

### 15.4 WebView, Fajlovi, Parser-i I Nepouzdan Sadrzaj

1. Inventarisi svaki WebView i njegova JavaScript, file access, content access, mixed content, debugging, Safe Browsing, cookie i navigation podesavanja.
2. Ogranici ucitane origin-e i external navigation.
3. Nikada ne izlozi sirok JavaScript interface nepouzdanom sadrzaju.
4. Validiraj file, content, data, blob i custom-scheme URL-ove.
5. Proveri da download i upload sprovode size, type, origin, storage, permission i cleanup pravila.
6. HTML, Markdown, SVG, XML, JSON, archive, subtitle, playlist, media metadata, image, PDF i third-party parser input tretiraj kao nepouzdan.
7. Ogranici parser recursion, entity expansion, decompression, allocation i execution time.
8. Proveri da external viewer i share koriste bezbedne URI-je i minimalne grant-ove.

### 15.5 Dozvole, Privacy I Data Safety

1. Inventarisi manifest, runtime, special, role, notification, exact alarm, overlay, accessibility, VPN, media projection, package install, all-files i restricted permission-e.
2. Proveri da je svaka dozvola neophodna, kontekstualna, minimalna i objasnjena pre sistemskog permission prompt-a gde je prikladno.
3. Obradi denial, repeated denial, one-time permission, approximate location, selected photos, auto-reset, revocation i povratak iz Settings-a.
4. Proveri background location, Bluetooth, nearby devices, camera, microphone, contacts, call logs, SMS, health i advertising identifier prema aktuelnom policy-ju.
5. Mapiraj prikupljene, obradjene, deljene, zadrzane, obrisane, export-ovane i backup-ovane podatke.
6. Uporedi ponasanje koda i SDK-ova sa privacy policy-jem, consent-om, Data safety deklaracijom i regionalnim zahtevima.
7. Proveri da analytics, attribution, crash, ads i experimentation SDK-ovi postuju consent i brisanje naloga.
8. Spreci osetljive podatke u logovima, screenshot-ovima, clipboard-u, notification-ima, widget-ima, recents, backup-u, analytics-u i support export-u.
9. Testiraj account deletion i data export end to end gde je primenjivo.
10. Identifikuj child-directed, health, financial, employment, education, biometric ili drugu regulisanu upotrebu koja zahteva strucnu proveru.

