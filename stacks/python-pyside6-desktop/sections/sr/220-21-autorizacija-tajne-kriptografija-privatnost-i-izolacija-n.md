## 21. Autorizacija, tajne, kriptografija, privatnost i izolacija naloga

### 21.1 Obim audita

1. Inventariši identitete, sesije, uloge, dozvole, tenant-e, naloge, workspace-e, organizacije, licence, entitlement-e i privilegovane operacije.
2. Mapiraj svaku UI akciju, background akciju, deep link, plugin poziv, WebChannel poziv, IPC zahtev, file operaciju, device komandu i API mutaciju na server-side ili trusted-boundary autorizaciju.
3. Pregledaj OS credential store-ove, keyring-e, DPAPI, Keychain, Secret Service, enkriptovane fajlove, derivaciju ključeva, random generation, rotaciju ključeva, recovery i brisanje.
4. Razlikuj authentication stanje, authorization stanje, cached display podatke, offline grant-ove, license stanje i serverski autoritet.
5. Proceni lokalne napadače, same-user procese, druge OS korisnike, ukradene profile-e, kopirane baze, pregled memorije, logove, crash dump-ove, swap i backup-e.
6. Zabeleži privacy svrhu, minimizaciju, consent, retention, export, brisanje, telemetriju, crash reporting i regionalne zahteve za svaku klasu podataka.

### 21.2 Obavezna verifikacija

1. Izvrši pozitivne i negativne authorization testove za direktan pristup objektu, stale UI, izmenjeno lokalno stanje, deep link-ove, plugin-e, IPC, offline režim i promenu naloga.
2. Verifikuj čuvanje i pribavljanje tajni u instaliranoj aplikaciji, uključujući backup/restore, rotaciju ključeva, revoked credential-e i ponašanje nedostupnog keyring-a.
3. Potvrdi da čišćenje UI polja ili brisanje config unosa stvarno opoziva sesije i uklanja osetljive lokalne artefakte prema politici.
4. Pregledaj logove, telemetriju, crash dump-ove, privremene fajlove, clipboard, screenshot-ove, recent-file liste i support bundle-ove radi curenja osetljivih podataka.
5. Zaustavi readiness kada client-only provere štite serverske resurse ili kada tenant/account identifikatori nedostaju u izolaciji cache-a, queue-a, fajlova ili telemetrije.

