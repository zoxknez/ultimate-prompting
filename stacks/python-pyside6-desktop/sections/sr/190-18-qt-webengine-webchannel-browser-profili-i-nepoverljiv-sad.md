## 18. Qt WebEngine, WebChannel, browser profili i nepoverljiv sadržaj

### 18.1 Obim audita

1. Inventariši svaki WebEngine view, profil, page, process model, storage partition, cache, cookie store, download handler, permission zahtev, certificate handler i custom URL schema-u.
2. Zabeleži sva lokalna i remote porekla, pravila navigacije, popup ponašanje, external-open ponašanje, CSP, mixed content, service worker-e, DevTools pristup i command-line switch-eve.
3. Mapiraj WebChannel objekte, izložene metode/property-je/signale, binding porekla, frame binding, validaciju argumenata, autorizaciju i lifetime.
4. Pregledaj JavaScript injection, generisanje HTML-a, pristup lokalnim fajlovima, `qrc` i privilegije custom schema, clipboard, kameru, mikrofon, geolokaciju, notifikacije i screen capture.
5. Proceni izolaciju profila između korisnika, tenant-a, naloga, okruženja i privilegovanog/neprivilegovanog sadržaja.
6. Tretiraj web sadržaj kao attacker-controlled dok poreklo, transport, integritet sadržaja i vlasništvo update-a nisu dokazani.

### 18.2 Obavezna verifikacija

1. Testiraj navigaciju ka malicious, redirected, downgraded, local-file, custom-scheme, popup, iframe i kompromitovanom origin sadržaju.
2. Pokušaj WebChannel pozive sa neautorizovanih origin-a, frame-ova, stale page-eva, restore-ovanih sesija i nakon promene naloga ili okruženja.
3. Verifikuj eksplicitne allowlist-e za navigaciju, external opening, download-e, dozvole, sertifikate i custom-scheme resurse.
4. Pregledaj zapakovane Chromium/Qt WebEngine verzije i security podršku; verifikuj sandbox/process ponašanje na svakoj platformi.
5. Potvrdi da se browser podaci, cookie-ji, credential-i, cache, download-i i service worker-i pravilno uklanjaju ili izoluju pri logout-u i uninstall-u.

