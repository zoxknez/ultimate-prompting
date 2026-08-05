## Faza 18 - Konfiguracija, tajne i feature flag-ovi

Dokazi poreklo konfiguracije, scope, validaciju, exposure, reload, rollout i recovery za svaku klasu okruzenja.

### Zahtevi audita

- Inventarisi build-time, server, edge, browser, preview, test, migration, worker i operativnu konfiguraciju.
- Validiraj obavezne vrednosti, formate, opsege, URL-ove, secret reference i cross-field invarijante pre traffic-a.
- Dokazi koje vrednosti se inlinuju u client bundle ili static output i spreci nebezbedno javno izlaganje.
- Pregledaj secret-manager pristup, least privilege, rotaciju, overlap, revocation, audit, backup, restore i lokalno koriscenje.
- Za flag-ove definisi owner-a, svrhu, targeting, default, fail-open/closed, telemetry, expiry, kill switch i cleanup.
- Spreci preview-e i nepoverljive branch-eve da naslede produkcione tajne, podatke, callback-e, cookie-je, domene ili analytics.

### Obavezni dokazi

- Konfiguracioni provenance i exposure klasifikacija.
- Environment validation izlaz za svaku klasu.
- Client-bundle i static-output secret-canary scan-ovi.
- Secret i flag rotation, revocation, expiry i rollback runbook-ovi.

### Obavezni failure i acceptance testovi

- Pokreni sa nedostajucim, malformed, stale i konfliktnim config-om.
- Rotiraj signing/encryption kljuceve kroz dokumentovani overlap prozor.
- Iskljuci flag servis i proveri definisane default-e i kill switch-eve.
- Izgradi nepoverljivi preview i dokazi produkcionu izolaciju.

