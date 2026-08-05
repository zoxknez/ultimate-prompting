# Revizioni izvestaj 05 - Electron / Tauri Desktop Audit Prompt

## Status

- Paket: Electron / Tauri / Chromium / WebView / Node.js / Rust desktop aplikacije
- Verzija posle rekonstrukcije: 2.0.0
- Datum baseline-a: 2026-08-05
- EN: zavrseno
- SR: zavrseno
- Strukturni paritet: prosao
- Ciljani kvalitet: production-candidate audit ugovor

## Pocetno stanje

Obe prethodne verzije imale su po 240 linija i 32 naslova. Medjusobni paritet je bio dobar, ali je sadrzaj bio vise prosirena checklist-a nego kompletan produkcioni audit ugovor.

Glavni nedostaci prethodne verzije:

1. Nije postojao dokazni lanac od source commit-a do stvarno instaliranog i pokrenutog procesa.
2. Electron security deo nije dovoljno razdvajao BrowserWindow/WebContentsView, preload, IPC sender identitet, session/partition, permission handler-e, custom protokole, fuses i ASAR integrity.
3. Tauri deo nije dovoljno duboko modelovao capabilities, merge ponasanje, permissions, custom scopes, Runtime Authority, command autorizaciju i plugin granice.
4. Auto-update je bio opisan previse opsto, bez zasebne Electron i Tauri state machine analize, tamper scenarija, downgrade politike, staged rollout-a, rollback-a i key-compromise response-a.
5. Nedostajala je kompletna signing/notarization arhitektura za Windows, macOS i Linux.
6. Installer, store, enterprise i side-by-side channel ponasanje nisu bili dovoljno dokazivi.
7. Lokalni podaci, embedded baze, migracije, korupcija, crash safety, account izolacija i uninstall politika nisu bili dovoljno razradjeni.
8. Nedostajali su obavezni negativni testovi za kompromitovan renderer/webview, stale caller, lokalni IPC impersonation, malicious file/path/URL, update tampering i interrupted install/update.
9. Nije bilo dovoljno detaljnih evidence matrica niti jasnog produkcionog evidence ceiling-a.

## Rekonstrukcija

Nove EN i SR verzije imaju po 1.122 linije i 112 potpuno uskladjenih naslova. Oba fajla nastala su iz jedinstvenog dvojezicnog izvora i imaju isti strukturni oblik svih linija.

Dodato je:

- obavezni source-to-installed-runtime identity chain;
- E0-E5 evidence model i strogi finding register;
- repository, JavaScript/TypeScript, Cargo/Rust, native dependency i supply-chain audit;
- pregled stvarnog package content-a, generisane konfiguracije, artefakta, potpisa i instaliranog stanja;
- mapa procesa, prozora, webview-a, origin-a, privilegija, IPC-a, komandi, sidecar-a i lokalnih servisa;
- shared web/content/origin, CSP, injection, authentication i session boundary audit;
- kompletan Electron overlay za verzije, lifecycle, BrowserWindow/WebContentsView, webPreferences, preload, ContextBridge, IPC, session, permissions, navigation, protocols, fuses, ASAR, utility procese i native module-e;
- kompletan Tauri overlay za ecosystem verzije, system WebView, capabilities, permissions, scopes, Runtime Authority, commands, events, channels, managed state, plugin-e, filesystem, shell, opener, sidecar-e, asset protocol, unsafe Rust i FFI;
- local data, database, migration, file import/export, archive i corruption recovery audit;
- network, proxy, TLS, certificate, localhost, socket, named pipe i service impersonation audit;
- deep link, file association, CLI, tray, notification, autostart, device, media i screen-capture audit;
- zajednicki update trust model plus zasebni Electron i Tauri updater audit;
- Windows, macOS i Linux signing, notarization, repository/store i certificate/key recovery model;
- installer, store, enterprise, portable, repair, upgrade, rollback i uninstall verifikaciju;
- performance, responsiveness, leak, idle, resource-budget, accessibility, localization, high-DPI i input verifikaciju;
- observability, crash, privacy, forensics i incident mode;
- 16 obaveznih adversarial/failure scenarija;
- 12 evidence matrica;
- 22-stavki production readiness checklist;
- 20-stavki Definition of Done;
- zabranjene precice i obavezni final report format.

## Aktuelni baseline

Na dan 5. avgusta 2026. primarni izvori navode:

- Electron 43.3.0 stable, objavljen 4. avgusta 2026, sa Chromium 150.0.7871.212 i Node.js 24.18.1;
- Electron support model poslednje tri stabilne major linije, uz obaveznu proveru trenutne tabele podrske;
- Tauri core 2.11.5, objavljen 1. jula 2026, dok CLI, JS API, runtime, Wry, Tao, bundler i plugin-i imaju nezavisne verzije;
- Tauri capability grant-ovi se spajaju kada isti prozor ili webview pripada vise capabilities;
- Tauri updater zahteva potpis i dangerous frontend update komande ostaju blokirane dok ih capabilities ne dozvole;
- Electron fuses moraju biti provereni u finalnom executable-u i menjaju se posle pakovanja, a pre code signing-a;
- ASAR sam po sebi nije kompletna security granica;
- signing, notarization, installer i updater ponasanje mora da se proverava po platformi i tacnom package formatu.

Baseline zapisi su dodati u `baselines/sources.json`. Prompt zahteva ponovnu proveru primarnih izvora pri svakom realnom auditu.

## Rezultati validacije

- EN linije: 1.122
- SR linije: 1.122
- EN naslovi: 112
- SR naslovi: 112
- Line-shape odstupanja: 0
- Markdown fence blokovi: balansirani
- YAML frontmatter: validan
- JSON baseline manifest: validan
- En dash u SR: 0
- Em dash u SR: 0
- Non-breaking hyphen u SR: 0
- Baseline hardcode scan: prosao
- Repository parity checker: Electron/Tauri par prosao; preostala ocekivana stara odstupanja su Java/Spring i Python/PySide6.

## Zakljucak

Paket je sada samostalan, dokazno orijentisan production audit ugovor za Electron, Tauri i mesovite desktop aplikacije. Najvaznija promena je prelazak sa staticke checklist-e na proveru stvarnog source, build, packaged, signed, installed, runtime, update i recovery stanja za svaku podrzanu platformu i arhitekturu.
