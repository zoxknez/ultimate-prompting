## 24. Overlay za migraciju i modernizaciju

### 24.1 Electron major upgrade

1. Upgrade-uj jedan podrzani major odjednom osim ako autoritativni dokaz i testovi opravdaju drugaciji put.
2. Pregledaj breaking changes, uklonjene default-e/API-je, Chromium ponasanje, Node/V8 promene, sandbox/context isolation, protocol/session promene i packaging/updater kompatibilnost.
3. Rebuild-uj i testiraj svaki native module i sidecar na svakom target-u. Verifikuj ABI, dostupnost prebuild-a, fallback compiler i runtime loading.
4. Uporedi sadrzaj paketa, fuses, potpise, dozvole, startup, memoriju, CPU, rendering, media, stampu, pristupacnost i installer/update ponasanje.
5. Pokreni old-version u new-version update i rollback/data-compatibility testove pre sirokog rollout-a.
6. Ne koristi upgrade da mesas nepovezane arhitektonske rewrite-ove osim ako su posebno scoped i reverzibilni.

### 24.2 Tauri 1 u 2 ili major plugin migracija

1. Popisi uklonjene/preimenovane API-je, izdvajanje plugin-a, capability/permission model, generisanu konfiguraciju, command registration, frontend API, mobile promene i bundler razlike.
2. Prevedi allowlist-e u least-privilege capabilities umesto dodeljivanja sirokih default-a radi vracanja funkcionalnosti.
3. Pregledaj v2 permissions, scope-ove, platform podrsku, migraciju podataka i update ponasanje svakog plugin-a nezavisno.
4. Diff-uj generisane seme, capabilities, manifeste, entitlement-e, installer-e i sadrzaj paketa pre i posle migracije.
5. Testiraj sve komande iz dozvoljenih i zabranjenih prozora/origin-a, jer prolazak build-a ne dokazuje ispravnost capabilities.
6. Verifikuj updater signing kljuceve, metadata, package formate, source-version kompatibilnost, rollback i user-data putanje.
7. Audituj Rust async/state/unsafe promene i zahteve sistemskog WebView-a na minimalnim podrzanim platformama.
8. Zadrzi reverzibilnu branch/artifact/data migration putanju dok produkcioni dokaz nije dovoljan.

### 24.3 Electron u Tauri ili Tauri u Electron migracija

1. Pocni od potrebnih capability-ja, platform podrske, WebView/runtime ponasanja, native integracija, updater-a, installer-a, pristupacnosti, enterprise ogranicenja i ukupnog maintenance troska, ne od marketinga velicine binarnog fajla.
2. Mapiraj svaku postojecu privilegiju i IPC/command ugovor. Redizajniraj least privilege umesto mehanickog rekreiranja sirokog bridge-a.
3. Prvo prototipuj najrizicnije tokove: remote sadrzaj, auth, fajlove, native module-e, sidecar-e, uredjaje, media, stampu, updater, signing, prodavnice i enterprise deployment.
4. Definisi kontinuitet data putanje, secure storage-a, bundle identiteta, protocol/file association-a, signing identiteta, kanala, installer-a i update-a.
5. Testiraj UI/rendering i Web API razlike kroz Chromium i sistemske WebView-e, ukljucujuci najstarije podrzane OS verzije.
6. Planiraj koegzistenciju, migraciju, rollback, poredjenje telemetrije, komunikaciju korisniku i podrsku za korisnike koji ne mogu da migriraju.
7. Ne proglasavaj uspeh samo iz feature parity-ja; zahtevaj operational, security, update, accessibility i recovery paritet.
8. Drzi stari produkcioni put recoverable dok adoption i stability gate-ovi nisu zadovoljeni.

