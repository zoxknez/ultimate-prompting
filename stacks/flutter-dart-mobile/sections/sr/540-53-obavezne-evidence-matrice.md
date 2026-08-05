## 53. Obavezne evidence matrice

Izradi svaku primenljivu matricu. Nedostajuća platforma, artefakt, okruženje, identitet ili recovery putanja mora biti vidljiva, ne tiho isključena.

### 53.1 Matrica platformi i uređaja

- Platforma, OS/browser verzija, arhitektura, device/window klasa, input režim, distributivni kanal, status podrške, dubina testa, vlasnik i dokaz.
- Uključi minimum, tipičan, najnoviji, low-resource, accessibility i reprezentativne vendor/device slučajeve.

### 53.2 Matrica toolchain-a i zavisnosti

- Lokalne, CI, release i production-resolved Flutter, Dart, engine, package graf, native toolchain, platform SDK i generator verzije.
- Označi drift, plutajuće verzije, nepodržane kombinacije, prerelease komponente, provenance native binarnih fajlova i remedijaciju.

### 53.3 Matrica identiteta artefakata

- Commit, dirty stanje, build job, artifact hash, package/bundle ID, version/build, flavor, signing identitet, store/kanal, simboli/source map-e, SBOM, provenance i runtime potvrda.
- Pokrij svaki promoted, staged, production, rollback i incident-rebuild artefakt.

### 53.4 Matrica kritičnih tokova

- Tok, uloga, tenant, početno stanje, mrežno stanje, lifecycle stanje, platforma, očekivana invarijanta, negativan slučaj, telemetrija, rollback i dokaz.
- Uključi autentikaciju, privilegovane mutacije, payment/order gde je primenljivo, offline tokove, file/media tokove, notification/deep-link ulaz i oporavak.

### 53.5 Authorization i tenant matrica

- Actor, subject, uloga, tenant, resurs, operacija, client presentation, serversko sprovođenje, lokalna particija, negativni test, ponašanje opoziva i dokaz.
- Uključi direktan ulaz u rutu, promenjen identifikator, zastareo link, promenu naloga, promenu tenant-a, impersonation, background rad i notifikacije.

### 53.6 Matrica podataka i storage-a

- Klasa podataka, vlasnik, autoritet, lokacija, account/tenant particija, enkripcija, ključ, backup, retention, brisanje, export, migracija, recovery od korupcije i dokaz.
- Uključi memoriju, secure storage, bazu, fajlove, cache, browser storage, notifikacije, logove, crash izveštaje, analitiku i backup-e.

### 53.7 Lifecycle i concurrency matrica

- Operacija, vlasnik, početno stanje, prekid, cancellation, timeout, duplikat, pravilo zastarelog rezultata, account/tenant promena, process death, resume, cleanup i dokaz.
- Pokrij mrežne pozive, stream-ove, state controller-e, background job-ove, isolate-e, platform channel-e, upload/download, payment, migracije i update-e.

### 53.8 Plugin i native-boundary matrica

- Plugin/API, platformska implementacija, native zavisnost, dozvola/entitlement, channel/FFI ugovor, lifecycle, threading, error model, unsupported ponašanje, testovi, vlasnik i dokaz.
- Uključi federated implementacije, platform view-ove, background entrypoint-e, više engine-a, native asset-e i security-sensitive bridge-eve.

### 53.9 Matrica dozvola i hardvera

- Capability, platformska deklaracija, runtime stanje, svrha, pristupljeni podaci, fallback, opoziv, lifecycle, odsustvo hardvera, privacy disclosure, test uređaj i dokaz.
- Uključi denied, permanently denied, restricted, limited, approximate, one-time, while-in-use, background i revoked stanja gde su primenljiva.

### 53.10 Release i rollout matrica

- Platforma/kanal, artefakt, kohorta, preduslov, store/install korak, telemetry gate, acceptance prag, abort trigger, rollback/forward-fix putanja, vlasnik i dokaz.
- Uključi clean install, upgrade iz podržanih verzija, vraćen backup, malo diska, offline launch, prekid update-a, old/new koegzistenciju i support komunikaciju.

### 53.11 Observability i SLO matrica

- Kritični tok ili resurs, SLI, cilj, izvor, dimenzije, sampling, privatnost, alert, vlasnik, runbook, release gate, retention i dokaz.
- Uključi crash-free upotrebu, startup, jank, memoriju, mrežu, auth, migraciju, sync, background rad, notifikacije, update/install i poslovne ishode.

### 53.12 Recovery i incident matrica

- Scenario, detekcija, izvor dokaza, containment, opozvan materijal, trusted source, rebuild/restore korak, uticaj na korisnika, komunikacija, RPO/RTO, vlasnik, validacija i dokaz.
- Uključi gubitak signing ključa, zlonamernu zavisnost, update kompromitaciju, izlaganje podataka, gubitak backend-a, gubitak store-a, telemetry outage, crash loop i destruktivnu migraciju.

