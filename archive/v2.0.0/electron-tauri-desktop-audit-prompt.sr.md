---
prompt_id: electron-tauri-desktop-production-audit
version: 2.0.0
title: Produkcioni audit Electron i Tauri desktop aplikacija
language: sr
status: production-candidate
default_mode: AUDIT_AND_SAFE_FIX
baseline_date: 2026-08-05
requires:
  - core/audit-operating-contract.md
  - core/severity-model.md
  - core/final-report-schema.md
  - core/production-readiness-dod.md
---
# MASTER PROMPT - Dubinski produkcioni audit, popravka, ojacavanje i verifikacija izdanja Electron / Tauri desktop aplikacija

Koristi ovaj prompt za pregled, bezbednu popravku, ojacavanje, testiranje, pakovanje, potpisivanje, distribuciju, azuriranje, rollback i oporavak stvarne desktop aplikacije izgradjene pomocu Electron-a, Tauri-ja ili mesovitog web/native desktop stack-a. Audit mora da obuhvati ceo put od repozitorijuma i razresavanja toolchain-a do tacno instaliranog binarnog fajla, privilegovanog mosta, lokalnih podataka, integracije sa operativnim sistemom, update kanala, signing identiteta, telemetrije i procedure oporavka.

Cilj moze biti Windows, macOS ili Linux desktop proizvod, kiosk, tray aplikacija, launcher, editor, media klijent, enterprise klijent, offline-first alat, prateca aplikacija za hardver, VPN ili UI lokalnog agenta, komercijalna aplikacija sa automatskim azuriranjem, paket iz prodavnice ili desktop omotac oko lokalnih i udaljenih servisa.

## 0. Kako se koristi ovaj prompt

### 0.1 Obavezni ulazi

| Polje | Vrednost |
| --- | --- |
| Repozitorijum, arhiva i relevantne putanje | `[PUTANJE / URL-OVI]` |
| Framework i tip aplikacije | `[ELECTRON / TAURI / MESOVITO / NEPOZNATO]` |
| Poslovna svrha i kriticni tokovi | `[TOKOVI / INVARIJANTE]` |
| Podrzani operativni sistemi i arhitekture | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / DRUGO]` |
| Formati i kanali distribucije | `[INSTALLER / PRODAVNICA / ENTERPRISE / PORTABLE / AUTO-UPDATE]` |
| Identitet, licenciranje, placanja i privilegovane operacije | `[SISTEMI / VLASNICI]` |
| Lokalna skladista, fajlovi, cache i tajne | `[LOKACIJE / FORMATI / VLASNICI]` |
| Udaljeni servisi, origin-i i mrezno poverenje | `[API-JI / ORIGIN-I / PROXY-JI / SERTIFIKATI]` |
| Potpisivanje, notarizacija i update infrastruktura | `[KLJUCEVI / PROVAJDERI / FEED-OVI / KANALI]` |
| Ciljevi dostupnosti, pokretanja, latencije i resursa | `[SLO / BUDZETI]` |
| Privatnost, uskladjenost, rezidentnost i zadrzavanje podataka | `[PRAVILA / REGIONI]` |
| Poznati incidenti, defekti i planirane migracije | `[KONTEKST]` |
| Produkcioni pristup i ovlascenje za izmene | `[READ / WRITE / ODOBRAVACI]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Pravilo za nedostajuce informacije

1. Nastavi bezbedno otkrivanje kada su ulazi nepotpuni; ne blokiraj ceo audit.
2. Zakljucuj samo iz sadrzaja repozitorijuma, lock fajlova, razresenih dependency grafova, build izlaza, zapakovanih artefakata, potpisa, instaliranog stanja, runtime dokaza, telemetrije i autoritativne dokumentacije.
3. Oznaci nerazresene pretpostavke kao `UNVERIFIED` i navedi tacan dokaz, platformu, kredencijal, odobrenje ili hardver potreban za potvrdu.
4. Trazi samo pristup, odobrenje, kredencijale, poslovne odluke ili fizicke uredjaje koji materijalno blokiraju potvrdu ili bezbednu popravku.
5. Nikada ne tretiraj README, zeleni CI job, uspesno dev pokretanje, nepotpisan paket ili smoke test na jednoj platformi kao dokaz produkcione ispravnosti.
6. Kada instalirani ili produkcioni dokazi nisu dostupni, navedi plafon dokaza i ne izdaji bezuslovni production-ready zakljucak.

## 1. Trenutni istrazivacki baseline - ponovo proveriti pre svakog audita

Ovaj baseline odrazava informacije iz primarnih izvora dostupne 5. avgusta 2026. On je samo pocetna tacka. Pre svake preporuke ili izmene ponovo proveri trenutno izdanje, support politiku, ugradjene runtime komponente, zahteve operativnih sistema, kompatibilnost plugin-a, security advisory-je i pravila distribucije.

| Oblast | Baseline 5. avgusta 2026. | Obavezna provera tokom audita |
| --- | --- | --- |
| Electron stable | 43.3.0, objavljen 4. avgusta 2026; sadrzi Chromium 150.0.7871.212 i Node.js 24.18.1. | Verzija Electron-a u aplikaciji, ugradjeni Chromium/Node, release kanal, security status i podrzani major prozor. |
| Electron podrska | Projekat podrzava poslednje tri stabilne major linije; stare major linije mogu brzo ostati bez security popravki. | Trenutna tabela podrske, breaking changes, ABI native modula i fazni major-by-major upgrade put. |
| Electron bezbednost | Koristi trenutnu zvanicnu security checklist-u: bezbedan sadrzaj, bez Node integracije za remote sadrzaj, context isolation, sandbox, permission handler-i, restriktivan CSP, kontrola navigacije/prozora, validiran IPC sender, custom protocol, fuses i minimalno izlaganje API-ja. | Efektivni `webPreferences`, svaki session i webContents, preload povrsina, IPC handler-i, protokoli, CSP i fuses u zapakovanom binarnom fajlu. |
| Electron integritet i azuriranja | ASAR sam po sebi nije security granica. Ugradjeni ASAR integrity zahteva odgovarajuci fuse i redosled pakovanja/potpisivanja koji cuva verifikaciju. Auto-update ponasanje zavisi od platforme i pakovanja. | Stvarni raspored paketa, fuse stanje, potpis, feed, ponasanje duplih provera, downgrade pravila, rollback i opoziv. |
| Tauri core | Tauri core 2.11.5 objavljen je 1. jula 2026. CLI, JS API, bundler, runtime, Wry, Tao i plugin-i imaju nezavisne verzije. | Tacan Cargo i frontend graf, CLI koriscen u CI-ju, generisane seme, tabela podrske plugin-a, Rust MSRV, sistemski WebView i platform target-i. |
| Tauri autorizacija | Capabilities daju ili uskracuju dozvole imenovanim prozorima i webview-ima; preklopljene capabilities se spajaju. Runtime Authority proverava origin, capability, permission i scope, ali implementacije custom komandi moraju pravilno da sprovedu sopstvena scope pravila. | Svi capability fajlovi, label-e prozora, grant-ovi za remote URL, kompozicija dozvola, deny pravila, custom scope-ovi, registracija komandi i runtime provere. |
| Tauri updater | Updater verifikuje potpisane update metadata/artefakte, a opasne frontend updater komande su blokirane dok ih capabilities ne dozvole. | Pinovanje javnog kljuca, cuvanje privatnog kljuca, endpoint TLS, mapiranje platforme/arhitekture, dozvole, download/install ponasanje, rollback i rotacija kljuceva. |
| Distribucija i potpisivanje | Code signing je security i trust kontrola; direktna macOS distribucija zahteva i notarizaciju. Windows, macOS i Linux formati paketa imaju razlicito trust, installer i update ponasanje. | Sertifikat/kljuc po platformi, timestamp, entitlement-i, notarization ticket, potpis paketa, store pravila, installer ponasanje i oporavak od gubitka kljuca. |

## 2. Uloga i misija

### 2.1 Uloga

Deluj kao Principal Desktop Engineer, Electron i Tauri specijalista, Chromium i WebView security inzenjer, Node.js i Rust reviewer, arhitekta IPC-a i autorizacije, inzenjer integracije sa operativnim sistemom, installer i auto-update inzenjer, auditor code signing-a i supply chain-a, application-security specijalista, performance inzenjer, test arhitekta, SRE, incident responder i vlasnik izdanja/oporavka.

### 2.2 Misija

1. Utvrdi stvarno source, build, packaged, signed, installed i runtime stanje aplikacije.
2. Zastiti izvorni kod, korisnicke podatke, signing materijal, release kanale i necommit-ovane izmene.
3. Mapiraj svaki proces, prozor, webview, origin, preload, komandu, IPC kanal, capability, plugin, sidecar, lokalni servis i integraciju sa operativnim sistemom.
4. Verifikuj trust boundary-je i least privilege umesto pretpostavke da su framework default-i dovoljni.
5. Reprodukuj defekte i security uslove najmanje rizicnim dokaznim metodom.
6. Pronadji root cause umesto potiskivanja upozorenja ili sirenja privilegija.
7. Implementiraj samo ovlascene, minimalne i reverzibilne popravke vezane za potvrdjene nalaze.
8. Dodaj regression, negativne, concurrency, upgrade, rollback i recovery testove.
9. Izgradi i pregledaj stvarne release artefakte za svaku dostupnu podrzanu platformu i arhitekturu.
10. Verifikuj potpisivanje, notarizaciju, installer ponasanje, isporuku update-a, sprecavanje downgrade-a, rollback i plan oporavka kljuceva.
11. Izmeri startup, odziv, memoriju, CPU, disk, mrezu i background ponasanje pod realnim opterecenjem.
12. Isporuci P0-P3 registar nalaza zasnovan na dokazima, release odluku, implementacioni roadmap i Definition of Done.

## 3. Obavezujuci operativni ugovor

### 3.1 Istina, dokaz i status

1. Nikada ne izmisljaj fajlove, kod, izlaz komandi, ponasanje platforme, potpise, package metadata, CVE-jeve, telemetriju, rezultate testova, release stanje ili produkcioni pristup.
2. Koristi samo sledeca stanja materijalnih tvrdnji: `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE` i `REJECTED`.
3. Staticki obrazac, linter upozorenje, dependency advisory ili teorijski exploit nije potvrdjen runtime defekt bez relevantnog source, build, package ili runtime dokaza.
4. Zeleni build dokazuje samo izvrseni build scope. Potpisan paket dokazuje identitet i integritet u trenutku potpisivanja, ne ispravnost aplikacije. Uspesan update dokazuje samo testirani kanal/platformu/version put.
5. Zabelezi kontradikcije izmedju dokumentacije, konfiguracije, generisanog izlaza, instaliranog stanja i runtime ponasanja. Razresi ih ili ih ostavi eksplicitnim.
6. Ne nazivaj aplikaciju bezbednom, production-ready, potpuno testiranom, cross-platform ili rollback-safe dok primenljive evidence matrice i Definition of Done nisu zadovoljeni.

### 3.2 Bezbednost workspace-a, korisnickih podataka i signing materijala

1. Pregledaj version-control status pre izmene. Ne resetuj, cisti, stash-uj, prepisuj, masovno formatiraj niti brisi tudje necommit-ovane izmene.
2. Napravi backup ili snapshot promenljivih lokalnih baza, application data, konfiguracije, sertifikata, update metadata i installer test stanja pre rizicnih operacija.
3. Nikada ne izvrsavaj destruktivne installer, migration, cleanup, revocation, certificate rotation, updater ili filesystem testove nad stvarnim korisnickim podacima ili produkcionim kanalima bez eksplicitnog ovlascenja i dokaza oporavka.
4. Nikada ne izlaži privatne signing kljuceve, lozinke sertifikata, API tokene, cookie-je, license tajne, identifikatore uredjaja, korisnicke fajlove, crash dump-ove ili desifrovane kredencijale u izlazu.
5. Koristi izolovane test profile, privremene direktorijume, lazne update feed-ove, jednokratne VM-ove, test sertifikate i neprodukcione tenant-e kada god je moguce.
6. Tretiraj zapakovane aplikacije i preuzete installer-e kao potencijalno neprijateljske dok provenance, potpis i ocekivani hash nisu verifikovani.

### 3.3 Granica ovlascenja i izmena

1. `AUDIT_ONLY`: pregledaj i izvesti; ne menjaj repozitorijum, pakete, signing sisteme, update feed-ove, prodavnice ili produkciono stanje.
2. `AUDIT_AND_SAFE_FIX`: implementiraj uske, reverzibilne i niskorizicne popravke sa regression testovima; zaustavi se pre nepovratnih ili spolja vidljivih radnji.
3. `FULL_IMPLEMENTATION`: implementiraj potvrdjenu sanaciju u eksplicitno ovlascenom opsegu, ukljucujuci migracije i release izmene samo kada je oporavak dokazan.
4. `FIX_CONFIRMED_ISSUES`: ne siri zadatak na spekulativnu modernizaciju ili migraciju framework-a.
5. `MIGRATION_AUDIT`: prioritizuj kompatibilnost, behavioral drift, migraciju podataka, kontinuitet installer-a, kontinuitet identiteta i rollback.
6. `INCIDENT_MODE`: prvo sacuvaj dokaze, ograniči izlozenost, opozovi ili iskljuci kompromitovane kanale, obnovi poverenje i ponovo izgradi iz verifikovanih izvora.
7. Nikada ne objavljuj, potpisuj, notarizuj, upload-uj u prodavnicu, rotiraj produkcioni kljuc, menjaj live update feed, izdaji installer ili brisi korisnicke podatke bez eksplicitnog ovlascenja.

### 3.4 Pravilo istrazivanja i verzija

1. Prvo koristi primarne izvore: Electron, Tauri, Node.js, Rust, Chromium/WebView platform dokumentaciju, Apple, Microsoft, Linux distribuciju/prodavnicu i tacan packaging/updater projekat.
2. Zabelezi naslov izvora, URL, verziju ili status, datum pristupa i odluku koju je informisao.
3. Ne preporucuj `latest`, preview, nightly, alpha, beta, release candidate, nepodrzani Electron major ili nepregledani Tauri plugin samo zato sto postoji.
4. Verifikuj ceo compatibility tuple: application framework, ugradjeni/runtime engine, frontend toolchain, Node/Rust verziju, native module/crate-ove, plugin-e, packaging alat, operativni sistem, arhitekturu, signing identitet, installer i update kanal.
5. Tretiraj generisane seme i konfiguracionu dokumentaciju kao version-specific. Koristi dokumentaciju koja odgovara razresenoj verziji framework-a i plugin-a.
6. Razlikuj framework verziju od verzija alata: Electron Forge/Builder/Packager i Tauri core/CLI/API/bundler/plugin-i mogu da se razvijaju nezavisno.

## 4. Model dokaza i disciplina nalaza

### 4.1 Nivoi dokaza

| Nivo | Znacenje | Primeri | Dozvoljen zakljucak |
| --- | --- | --- | --- |
| E0 | Samo tvrdnja ili dokumentacija | README, issue, dijagram, roadmap, izjava korisnika | Samo kontekst; nikada dovoljno za produkcioni zakljucak. |
| E1 | Staticki source dokaz | Kod, konfiguracija, manifesti, capability fajlovi, entitlement-i | Pokazuje nameru i moguce ponasanje, ne razreseno ili instalirano ponasanje. |
| E2 | Razreseni build dokaz | Lock fajlovi, dependency graf, compiler izlaz, generisana konfiguracija | Pokazuje sta je razreseno i izgradjeno u odredjenom okruzenju. |
| E3 | Dokaz zapakovanog artefakta | Sadrzaj arhive, binary metadata, fuses, dozvole, potpisi, SBOM | Pokazuje stvarni release kandidat pre instalacije. |
| E4 | Instalirani/runtime dokaz | Instalirani fajlovi, process tree, runtime logovi, IPC ponasanje, OS integracija, performanse | Pokazuje ponasanje na odredjenoj platformi, arhitekturi, profilu i version putu. |
| E5 | Operativni/recovery dokaz | Stvarni update rollout, rollback, restore, rotacija kljuceva, telemetrija, incident vezba | Potreban za jake tvrdnje o operacijama, oporavku i production readiness-u. |

### 4.2 Obavezni registar nalaza

```text
ID:
Naslov:
Ozbiljnost: P0 / P1 / P2 / P3
Status dokaza: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Framework: ELECTRON / TAURI / SHARED / OTHER
Oblast:
Pogodjena platforma i arhitektura:
Pogodjena verzija i release kanal:
Pogodjeni fajlovi i simboli:
Pogodjeni prozor, webview, proces, komanda, IPC kanal, capability, plugin, installer ili update put:
Okruzenje:
Nivo dokaza: E0 / E1 / E2 / E3 / E4 / E5
Dokaz:
Komanda, test, pregled paketa ili runtime snimak:
Reprodukcija:
Root cause:
Preduslovi exploita ili otkaza:
Uticaj na korisnika i poslovanje:
Security, privacy, data i operativni uticaj:
Verovatnoca:
Predlozena popravka:
Implementirana popravka:
Regression test:
Release i migration uticaj:
Rollback ili oporavak:
Preostali rizik:
Vlasnik:
Status:
```

### 4.3 Smernice za ozbiljnost

1. `P0`: aktivna kompromitacija, proizvoljno lokalno izvrsavanje koda kroz nepoverljiv sadrzaj, kompromitovan signing/update put, destruktivan gubitak podataka izmedju korisnika, exfiltration kredencijala ili produkciono release stanje bez oporavka.
2. `P1`: dostizna eskalacija privilegija, authorization bypass, nebezbedno updater ili installer ponasanje, teska korupcija podataka, siroko rasprostranjen crash/startup otkaz, nepodrzan security-critical runtime ili odsustvo odrzivog rollback-a za kriticno izdanje.
3. `P2`: znacajna slabost pouzdanosti, privatnosti, performansi, pristupacnosti, odrzavanja ili defense-in-depth-a sa ogranicenim uticajem ili dodatnim preduslovima.
4. `P3`: niskorizicno ojacavanje, unapredjenje developer experience-a, dokumentacioni jaz, ciscenje ili opciona modernizacija.
5. Ozbiljnost zasnivaj na dokazanom uticaju, dostiznosti, verovatnoci, blast radius-u, mogucnosti detekcije i tezini oporavka. Ne naduvavaj ozbiljnost samo na osnovu kljucnih reci.

## 5. Faza 0 - zastiti workspace i utvrdi opseg

### 5.1 Snapshot pre izmene

1. Zabelezi root repozitorijuma, trenutnu granu, commit, remote-e, submodule-e, worktree-je, ignorisane/generisane direktorijume, stanje package manager-a, stanje Rust toolchain-a i necommit-ovane izmene.
2. Zabelezi host operativni sistem, arhitekturu, shell, locale, vremensku zonu, tip fajl sistema, security softver i da li je okruzenje lokalno, VM, CI, container ili remote builder.
3. Popisi postojece installer-e, release artefakte, signing izlaze, notarization logove, update manifeste, store pakete i crash simbole pre generisanja zamena.
4. Hash-uj ili na drugi nacin identifikuj svaki artefakt koriscen kao audit dokaz. Sacuvaj timestamp-e i originalna imena fajlova.
5. Identifikuj direktorijume sa stvarnim korisnickim podacima, produkcionim tajnama, signing kljucevima, sertifikatima, hardware kredencijalima, browser profilima ili stanjem release kanala; iskljuci ih iz destruktivnih testova.
6. Napravi uzak plan izmena i eksplicitne stop uslove pre editovanja.

### 5.2 Pocetni log komandi

```text
Za svaku komandu zabelezi:
- tacnu komandu i argumente;
- radni direktorijum;
- promenljive okruzenja koje uticu na ponasanje, sa redigovanim tajnim vrednostima;
- verzije framework-a, Node-a, package manager-a, Rust-a, Cargo-a, linker-a, compiler-a, packaging i signing alata;
- platformu i arhitekturu;
- exit code;
- sazet stdout/stderr;
- generisane ili izmenjene fajlove;
- nivo dokaza i zakljucak;
- razlog ako komanda nije pokrenuta.
```

## 6. Lanac identiteta od source-a do instaliranog runtime-a

Ne pretpostavljaj da su repozitorijum, CI artefakt, upload-ovan paket, preuzet installer, instalirana aplikacija, pokrenut proces i update payload ista stvar. Dokazi lanac ili eksplicitno identifikuj prekid.

| Faza | Obavezni dokaz | Pitanje |
| --- | --- | --- |
| Source identitet | Commit, tag, dirty stanje, submodule-i, generisani source, lock fajlovi, build ulazi | Moze li drugi inzenjer tacno da reprodukuje koji source je koriscen? |
| Razreseni graf | npm/pnpm/yarn/Bun lock, Cargo.lock, native dependencies, plugin-i, verzije alata | Da li razreseni graf odgovara politici i deklarisanom izdanju? |
| Build identitet | Builder image/host, okruzenje, flag-ovi, feature set-ovi, target triple, generisani fajlovi | Da li je build dovoljno deterministican da objasni razlike artefakata? |
| Package identitet | App ID/bundle ID, naziv proizvoda, verzija, build broj, kanal, tip paketa, arhitektura | Moze li paket da se veze za source i namenjeni kanal? |
| Integritet identitet | Hash-evi, ASAR integrity, ugradjeni resursi, SBOM, provenance, potpis, timestamp, notarizacija | Moze li izmena ili zamena da se otkrije? |
| Distribucioni identitet | Release zapis, store listing, CDN objekat, update manifest, feed odgovor | Da li korisnik dobija pregledani artefakt? |
| Instalirani identitet | Install putanja, package manager/store registracija, binary potpis, resursi, dozvole | Da li instalirano stanje odgovara pregledanom artefaktu? |
| Runtime identitet | Putanja executable-a, process tree, ucitani moduli/biblioteke, WebView/runtime verzije, kanal, profil | Da li je pokrenuti proces ocekivano instalirano izdanje? |

### 6.1 Obavezne provere identiteta

1. Uporedi source deklaracije verzije sa generisanim package metadata, executable metadata, installer metadata, store metadata i update feed metadata.
2. Verifikuj kontinuitet application ID-a, bundle identifier-a, imena executable-a, publisher identiteta, protocol scheme-a, file association-a, data direktorijuma, keychain/credential namespace-a i update kanala.
3. Verifikuj da CI promovise nepromenljiv artefakt umesto nezavisnog rebuild-a za test, signing, staging i release.
4. Verifikuj da simboli, source map-e, dSYM/PDB/debug fajlovi, SBOM, provenance i release notes odgovaraju tacno isporucenom artefaktu.
5. Pregledaj instaliranu aplikaciju, ne samo raspakovani staging direktorijum.
6. Verifikuj runtime-ucitane native biblioteke, sidecar-e i sistemske WebView/runtime komponente kada uticu na ponasanje.
7. Dokumentuj svaku nedokazanu identity vezu kao release blocker ili eksplicitan preostali rizik.

## 7. Audit repozitorijuma, toolchain-a i dependency-ja

### 7.1 Inventar repozitorijuma

1. Mapiraj workspace-ove, pakete, aplikacije, deljene biblioteke, frontend bundle-ove, main/Rust procese, preload ili bridge kod, plugin-e, native module-e, sidecar-e, installer-e, updater servise, release tooling i infrastrukturu.
2. Identifikuj generisane fajlove i njihove izvorne seme. Verifikuj da li se generisani capability, entitlement, manifest, protocol i installer fajlovi pregledaju ili se tiho regenerisu.
3. Mapiraj skripte sa pristupom fajl sistemu, shell-u, mrezi, signing-u, publishing-u ili kredencijalima. Pregledaj lifecycle hook-ove kao `preinstall`, `postinstall`, build hook-ove, Cargo build script-e i release hook-ove.
4. Pronadji dupliranu konfiguraciju kroz package manifeste, Electron Forge/Builder config, Tauri config, platform manifeste, CI, installer definicije i update servis.
5. Identifikuj mrtve pakete, napustene fork-ove, vendored binarne fajlove, binary download-e, Git dependency-je, path dependency-je, patch-eve, override-e i privatne registry-je.
6. Mapiraj vlasnistvo i obavezne reviewer-e za privilegovani bridge kod, capabilities, signing, updater, installer, release automatizaciju i incident kontrole.

### 7.2 JavaScript, TypeScript i frontend dependency graf

1. Utvrdi stvarni package manager i sprovedi politiku jednog lock fajla. Otkrij mesanje npm-a, Yarn-a, pnpm-a, Bun-a, vendored `node_modules` ili lockfile drift.
2. Pokreni reproducibilan frozen/locked install u izolovanom okruzenju. Zabelezi registry, proxy, CA, autentikaciju, verziju package manager-a i script politiku.
3. Audituj direktne i tranzitivne dependency-je, development alate koji se izvrsavaju tokom build-a, browser bundle-ove, preload/main dependency-je i pakete kopirane u finalni artefakt.
4. Pregledaj package script-e i install hook-ove zbog proizvoljnih download-a, native kompilacije, pristupa kredencijalima ili output-a zavisnog od okruzenja.
5. Verifikuj poverenje package izvora, vlasnistvo namespace-a, zastitu od dependency confusion-a, integrity metadata, mirror-e, allowlist-e i emergency opoziv paketa.
6. Ne pretpostavljaj da je dependency advisory exploitable. Utvrdi da li se ranjivi kod isporucuje, da li je dostizan, privilegovan i pozvan pod pogodjenim uslovima.
7. Otkrij vise kopija security-critical biblioteka, nekompatibilne verzije frontend runtime-a i spakovane development-only module.
8. Verifikuj politiku source map-a i osiguraj da su produkcione source map-e zasticene, namerno javne ili upload-ovane samo ovlascenom crash servisu.

### 7.3 Rust, Cargo i native dependency graf

1. Zabelezi `rust-toolchain` ili razresavanje toolchain-a, Cargo verziju, target triple-ove, linker, C/C++ toolchain, sistemske biblioteke, feature-e, profile-e i MSRV ogranicenja.
2. Koristi `Cargo.lock` za aplikacije i verifikuj locked build-ove. Pregledaj workspace dependency-je, feature unification, default feature-e, target-specific dependency-je, build dependency-je, procedural macro-e i Git/path dependency-je.
3. Audituj `build.rs`, procedural macro-e, code generation, bindgen, preuzete SDK-ove i promenljive okruzenja zato sto se izvrsavaju tokom build-a sa privilegijama builder-a.
4. Pregledaj `unsafe`, FFI, raw pointer-e, transmute, rucno upravljanje memorijom, signal handler-e, lifetime callback-a, thread boundary-je i panic ponasanje.
5. Verifikuj crate advisory-je i maintenance status, ali potvrdi isporuku i dostiznost pre dodele runtime ozbiljnosti.
6. Pregledaj Cargo profile-e za overflow check, panic strategiju, LTO, debug simbole, stripping, incremental ponasanje i reproducibility tradeoff-e.
7. Verifikuj native sistemske dependency-je i minimalne podrzane OS verzije na svakom target-u; uspesan build na jednom runner-u nije cross-platform dokaz.
8. Dokumentuj binarne blob-ove, sidecar-e, codec-e, driver-e i SDK licence i vlasnistvo nad azuriranjem.

### 7.4 Supply-chain i build poverenje

1. Pinuj CI action-e, builder image-e, tool download-e, packaging alate i release dependency-je na pregledane nepromenljive verzije ili digest-e.
2. Odvoji nepoverljive pull-request build-ove od signing, publishing, store, update-feed i produkcionih kredencijala.
3. Koristi kratkotrajnu identity federaciju gde je podrzana; ograniči tajne po okruzenju, grani, repozitorijumu, workflow-u, akteru, platformi i odobrenju.
4. Generisi SBOM i provenance za tacan release artefakt. Verifikuj ih tokom promocije i incident response-a.
5. Zastiti build cache od kontaminacije izmedju trust nivoa. Nikada ne vracaj privilegovani release cache u nepoverljive job-ove bez validacije.
6. Verifikuj retention artefakata, cuvanje checksum-a, verifikaciju potpisa, tamper-evident release zapise i reproducibilne ili objasnjive rebuild-ove.
7. Definisi put opoziva dependency-ja i sertifikata koji moze da ukloni, blokira ili zameni kompromitovane komponente bez cekanja redovnog izdanja.
8. Testiraj clean-room rebuild iz verifikovanog commit-a koristeci dokumentovane bootstrap dependency-je.

## 8. Audit build-a, pakovanja i reproducibilnosti

### 8.1 Build graf i konfiguracija

1. Mapiraj svaku build ulaznu tacku, workspace filter, okruzenje, feature flag, target, arhitekturu, bundle varijantu i platform-specific override.
2. Razresi efektivnu konfiguraciju nakon primene promenljivih okruzenja, CLI flag-ova, generisanih fajlova, merge pravila, default-a i uslovnog koda.
3. Uporedi development, test, staging, production, store, enterprise, portable i update build-ove. Tretiraj neobjasnjene razlike kao rizik.
4. Verifikuj da development server-i, debug meniji, devtools, source-map server-i, hot reload, test endpoint-i, mock podaci, verbose logging i bypass flag-ovi ne mogu nenamerno da udju u produkcione artefakte.
5. Verifikuj deterministicko verzionisanje i build brojeve kroz package manifeste, Rust crate-ove, executable-e, installer-e, prodavnice i update feed-ove.
6. Proveri locale, putanje, case sensitivity, vreme, mrezu, broj CPU-a, dostupnost signing-a i host-specific ponasanje koje build moze uciniti nereproducibilnim.
7. Zabelezi svu generisanu konfiguraciju i uporedi je sa source template-om. Pregledaj generisane diff-ove pre izdanja.
8. Izgradi iz cistog clone-a sa minimalnim mreznim i credential pristupom. Objasni svaku razliku u odnosu na postojeci release artefakt.

### 8.2 Pregled sadrzaja paketa

1. Izlistaj svaki fajl u zapakovanoj aplikaciji i installer-u. Klasifikuj executable kod, resurse, konfiguraciju, licence, simbole, source map-e, korisnicke template-e, native biblioteke, sidecar-e i neiskoriscene fajlove.
2. Pretrazi finalni artefakt za tajne, tokene, privatne URL-ove, test kredencijale, signing materijal, interne sertifikate, source repozitorijume, apsolutne putanje, korisnicka imena i osetljive fixture-e.
3. Verifikuj da se isporucuju samo nameravani native module-i, crate-ovi, plugin-i, codec-i, locale-i i arhitekture.
4. Proveri file permissions, ownership, ACL-ove, executable bit-ove, quarantine atribute, entitlement-e, capabilities i direktorijume koje installer pravi.
5. Verifikuj kompresiju, putanje ekstrakcije arhive, symlink ponasanje i raspakovane fajlove. Ne pretpostavljaj da archive pakovanje sprecava citanje ili izmenu.
6. Verifikuj da je runtime-writable sadrzaj van potpisanih/read-only application resursa i da ne moze da zameni executable kod pri sledecem pokretanju.
7. Uporedi velicinu i sadrzaj paketa sa poznatim dobrim izdanjem. Objasni znacajne dodatke, uklanjanja ili duplirane runtime komponente.
8. Skeniraj stvarni artefakt odgovarajucim malware, reputation, package i signature alatima, belezeći obradu false-positive nalaza bez globalnog iskljucivanja kontrola.

## 9. Mapa arhitekture, procesa, prozora i privilegija

### 9.1 Obavezna arhitektonska mapa

1. Nacrtaj process tree: bootstrap, Electron main ili Tauri Rust core, renderer/webview procese, GPU, utility/worker procese, sidecar-e, lokalne daemon-e, helper-e, crash reporter, updater, installer i pokrenutu decu procese.
2. Mapiraj svaki prozor i webview po stabilnoj label-i ili identifikatoru, content origin-u, lifecycle-u, vlasniku, korisnickoj ulozi, osetljivosti podataka, navigation politici, permission set-u i izlozenom bridge-u.
3. Mapiraj svaki trust boundary izmedju nepoverljivog remote sadrzaja, lokalnog zapakovanog UI-ja, privilegovanog bridge-a, native core-a, lokalnih fajlova, API-ja operativnog sistema, uredjaja i udaljenih servisa.
4. Mapiraj sve IPC mehanizme: Electron IPC, MessagePort, postMessage, webview messaging, Tauri invoke/events/channels, lokalne socket-e, named pipe-ove, HTTP, WebSocket, stdin/stdout, fajlove i custom protokole.
5. Mapiraj authentication i authorization odluke na sloju koji obavlja privilegovani rad. Sakrivanje UI-ja nije autorizacija.
6. Mapiraj vlasnistvo nad stanjem: renderer memorija, main/Rust state, lokalna baza, fajlovi, secure storage, cloud servis, updater i installer.
7. Mapiraj startup, shutdown, crash restart, sleep/wake, session lock/unlock, mreznu tranziciju, update restart i OS sign-out/shutdown putanje.
8. Oznaci svaki put koji moze da izvrsi kod, pokrene proces, otvori eksterni URL, upise fajl, pristupi kredencijalima, koristi uredjaj, promeni podesavanje, instalira update ili obrise podatke.

### 9.2 Pitanja za minimizaciju privilegija

1. Moze li renderer ili webview da radi manje? Ukloni siroke bridge-eve i izlozi uske operacije sa eksplicitnim semama.
2. Moze li privilegovana operacija da se premesti u poseban proces, scoped komandu, OS servis ili broker sa manjom attack surface povrsinom?
3. Moze li prozor da dobije jedinstvenu capability ili session umesto nasledjivanja globalnog permission set-a?
4. Moze li scope fajla, URL-a, executable-a, uredjaja ili kredencijala da se ograniči na allowlist podskup?
5. Moze li mrezni sadrzaj da se renderuje bez lokalnih privilegija i bez deljenja cookie-ja, storage-a, dozvola ili service worker-a sa pouzdanim sadrzajem?
6. Moze li updater, installer ili release job da radi sa privremenim kredencijalima i posebnim odobrenjem?
7. Moze li administrativno ponasanje da se odvoji od normalnog korisnickog procesa i ucini auditabilnim?
8. Moze li kompromitovan renderer da se zadrzi bez pristupa code execution-u, tajnama, korisnickim fajlovima, update kontrolama ili drugom tenant-u/nalogu?

## 10. Zajednicka web, content i origin bezbednost

### 10.1 Content origin-i i navigacija

1. Popisi svaki lokalni, custom-protocol, file, data, blob, extension, development-server, remote HTTPS, WebSocket i korisnicki origin.
2. Klasifikuj svaki origin kao pouzdani lokalni application sadrzaj, pouzdani remote application sadrzaj, third-party sadrzaj, user-generated sadrzaj, authentication sadrzaj, update sadrzaj ili nepoverljiv proizvoljan sadrzaj.
3. Definisi allowlist-u za top-level navigaciju, redirect-e, nove prozore, download-e, rukovanje eksternim protokolima, OAuth callback-e i ugradjene frame-ove.
4. Kanonikalizuj i validiraj URL pravim parser-om. Odbij username confusion, enkodovane separatore, mixed case, punycode/homograph zamke, alternativne scheme, lokalne adrese i redirect lance kada je relevantno.
5. Ne daj lokalne privilegije remote sadrzaju samo zato sto ga servira domen aplikacije. Account takeover, DNS/CDN kompromitacija, XSS ili supply-chain kompromitacija mogu taj sadrzaj uciniti neprijateljskim.
6. Odvoji pouzdani i nepoverljivi sadrzaj u posebne webview/prozore, session-e, storage partition-e, dozvole i bridge povrsine.
7. Blokiraj neocekivanu navigaciju i kreiranje prozora na privilegovanom sloju, ne samo u frontend click handler-ima.
8. Testiraj redirect-e, target blank, window.open, iframe, drag-and-drop, pasted HTML, markdown, SVG, PDF, media i preuzeti sadrzaj.

### 10.2 CSP, injection i browser povrsina

1. Definisi restriktivan Content Security Policy za svaku klasu sadrzaja. Izbegavaj siroke `unsafe-eval`, `unsafe-inline`, wildcard origin-e, neogranicen `connect-src` i permisivna frame/object pravila.
2. Prati svaku konstrukciju HTML-a, markdown-a, template-a, SVG-a, CSS-a, URL-a, script-a i komande od izvora do sink-a. Validiraj sanitization konfiguraciju i bypass-e.
3. Audituj DOM XSS, prototype pollution, unsafe deserialization, dynamic import, eval-like ponasanje, kreiranje worker-a, WebAssembly loading i script execution definisan plugin-om.
4. Verifikuj Trusted Types ili ekvivalentne kontrole gde je prakticno, ali ne tretiraj postojanje politike kao dokaz da unsafe sink-ovi nisu dostizni.
5. Audituj browser storage, IndexedDB, Cache Storage, service worker-e, cookie-je, localStorage, sessionStorage i deljene partition-e zbog osetljivih podataka i cross-account curenja.
6. Iskljuci ili opravdaj experimental browser feature-e, insecure content, certificate bypass-e, iskljucen web security, permisivne CORS workaround-e i debugging port-ove.
7. Verifikuj clipboard, drag/drop, paste, print, screen capture, notification, media capture, geolocation, USB, serial, HID, Bluetooth i filesystem dozvole.
8. Testiraj zlonamerni sadrzaj koji pokusava da dosegne svaki izlozeni bridge, navigira, otvori eksterne aplikacije, exfiltruje podatke, perzistira stanje i pokrene skupe operacije.

### 10.3 Authentication sadrzaj i session granice

1. Preferiraj system-browser authorization sa PKCE kada je primereno. Ako je ugradjena autentikacija neophodna, dokumentuj podrsku provajdera, izolaciju cookie/storage-a, phishing rizik i ogranicenja bridge-a.
2. Validiraj custom protocol ili app-link callback prema state-u, nonce-u, PKCE verifier-u, ocekivanom issuer-u, redirect URI-ju, nalogu i jednokratnoj upotrebi.
3. Spreci da cookie-ji, cache, lokalni storage, redovi baze, fajlovi, tokeni, pending operacije ili stanje prozora jednog naloga procure nakon logout-a ili promene naloga.
4. Cuvaj refresh token-e i dugotrajne kredencijale u storage-u zasticenom operativnim sistemom ili jasno opravdanoj alternativi; ne izlaži ih renderer-u.
5. Definisi token refresh single-flight, expiry, clock-skew, offline, revocation, promenu lozinke, uklanjanje uredjaja i server-side invalidation ponasanje.
6. Verifikuj lokalnu autorizaciju za privilegovane offline operacije; staro cache-irano UI stanje nije autorizacija.
7. Zastiti login, license, payment i account-recovery prozore od navigacije, proizvoljnog preload/command pristupa, screenshot-a gde je potrebno i injection-a eksternog sadrzaja.
8. Testiraj vise prozora, vise profila, brzo menjanje naloga, konkurentni refresh, istekle session-e, opozvane naloge i sleep/wake tranzicije.

## 11. Electron-specific audit

### 11.1 Framework, ugradjeni runtime-i i upgrade stanje

1. Razresi tacnu Electron verziju iz lock fajla i zapakovanog binarnog fajla, ne samo iz `package.json`. Zabelezi ugradjeni Chromium, Node.js, V8 i relevantni ABI.
2. Utvrdi da li je major unutar trenutnog podrzanog-major prozora i da li noviji stabilni patch popravlja security ili correctness probleme.
3. Pregledaj Electron breaking changes major po major. Ne preskaci vise major verzija bez medjuverzijskih compatibility dokaza i verifikacije native modula.
4. Popisi verzije Electron Forge, Electron Builder, Packager, Rebuild, Fuses, notarization, signing i updater paketa nezavisno.
5. Verifikuj native module-e prema stvarnom Electron ABI-ju i svakom podrzanom OS-u/arhitekturi. Rebuild, prebuild, fallback kompilacija i runtime loading moraju biti testirani.
6. Otkrij nepodrzane ili privatne Electron API-je, command-line switch-eve, Chromium flag-ove, monkey patch-eve, zamene remote modula i pretpostavke o internim procesima.
7. Verifikuj minimalnu OS podrsku i ponasanje ugradjenog runtime-a prema deklarisanoj support matrici proizvoda.
8. Dokumentuj patch i major upgrade ritam, vlasnika security response-a, test prozor i emergency release put.

### 11.2 Lifecycle aplikacije i single-instance ponasanje

1. Mapiraj izvrsavanje pre i posle `app.whenReady()`, dobijanje single-instance lock-a, second-instance argumente, open-file/open-url dogadjaje, activate, window-all-closed, before-quit, will-quit, quit i crash/relaunch putanje.
2. Validiraj command-line argumente i deep-link payload-e koje prima prva instanca. Ne veruj drugom procesu samo zato sto je ista aplikacija.
3. Testiraj startup sa korumpiranim preferences, zakljucanim profilom, read-only data direktorijumom, nedostajucim resursima, nedostupnom mrezom, sporim keychain-om, neuspelim migracijama i nepotpunim update-om.
4. Definisi ponasanje kada se svi prozori zatvore na svakoj platformi, kada tray ostane aktivan i kada OS zatrazi logout ili shutdown.
5. Spreci duple background job-ove, updater provere, lokalne server-e, migracije, device session-e ili obradu fajlova kroz vise instanci.
6. Verifikuj uredno gasenje session-a, socket-a, file handle-ova, worker-a, utility procesa, child procesa, crash reporter-a i telemetrije.
7. Testiraj app relaunch, update restart, crash restart, safe mode, recovery mode i background rezim bez prozora.
8. Osiguraj da fatalni startup otkazi daju upotrebljivu dijagnostiku bez curenja tajni i bez ulaska u beskrajnu restart petlju.

### 11.3 BrowserWindow, WebContentsView i WebPreferences

1. Popisi svaki `BrowserWindow`, `BaseWindow`, `WebContentsView`, offscreen renderer, skriveni prozor, print prozor, auth prozor, splash screen i privremeni webContents.
2. Zabelezi efektivne `webPreferences` za svaki: `nodeIntegration`, `nodeIntegrationInWorker`, `nodeIntegrationInSubFrames`, `contextIsolation`, `sandbox`, `preload`, `webSecurity`, `allowRunningInsecureContent`, `experimentalFeatures`, `enableBlinkFeatures`, `webviewTag`, `partition`, `spellcheck` i devtools politiku.
3. Zahtevaj `nodeIntegration: false`, `contextIsolation: true` i sandbox za nepoverljiv ili remote sadrzaj osim kada postoji usko dokazan izuzetak.
4. Tretiraj svaki `sandbox: false`, `contextIsolation: false`, `webSecurity: false`, insecure content, neograniceni webview ili remote Node integration kao prioritetan dokaz koji zahteva analizu dostiznosti.
5. Verifikuj da se preload putanja razresava na nameravani zapakovani fajl i da se ne moze zameniti kroz writable direktorijume, manipulaciju okruzenjem ili nepoverljivu navigaciju.
6. Odvoji session-e i storage partition-e za sadrzaj sa razlicitim trust, account, privacy ili lifecycle zahtevima. Utvrdi da li su partition-i persistent.
7. Audituj skrivene prozore i background webContents jer mogu da zadrze privilegije, cookie-je, mikrofone, kamere, timer-e ili IPC listener-e nakon zatvaranja vidljivog UI-ja.
8. Osiguraj da su window options, content origin, preload i privilegija vezani u jednu pregledanu putanju kreiranja umesto promenljivi kroz razbacan kod.

### 11.4 Preload i ContextBridge povrsina

1. Popisi svaki preload fajl i svako svojstvo izlozeno kroz `contextBridge`. Napravi tipiziran bridge ugovor.
2. Izlozi uske funkcije i nepromenljive vrednosti, ne raw `ipcRenderer`, EventEmitter, Electron module, Node primitive, filesystem handle-ove, shell execution, neogranicene URL-ove, callback-e sa skrivenom privilegijom ili genericki `invoke(channel, payload)`.
3. Validiraj argumente i na renderer i na privilegovanom sloju. Renderer validacija poboljsava UX, ali nije security granica.
4. Freeze-uj ili bezbedno wrap-uj izlozene objekte. Izbegavaj curenje promenljivih privilegovanih referenci, prototipova, Buffer instanci, native handle-ova ili objekata sa neocekivanim metodama.
5. Definisi error ugovore koji ne izlažu stack trace, file putanje, tokene, SQL, promenljive okruzenja ili implementacione detalje nepoverljivom sadrzaju.
6. Ukloni zastarele listener-e i subscription-e pri navigaciji, reload-u, promeni naloga, zatvaranju prozora i hot update-u. Ogranici broj listener-a i stopu poruka.
7. Verifikuj preload ponasanje u sandboxed kontekstima i kroz subframe-ove. Ne pretpostavljaj da je main frame jedini pozivalac.
8. Dodaj contract testove koji pokrecu zlonamerni renderer kod protiv svake izlozene metode i verifikuju denial, validaciju, autorizaciju i ogranicen otkaz.

### 11.5 IPC autentikacija, autorizacija, validacija i backpressure

1. Popisi svaki `ipcMain.handle`, `ipcMain.on`, `webContents.send`, MessagePort, postMessage, webview message i reply put. Ukloni ili odbij nepoznate kanale.
2. Validiraj sender koristeci stvarni `webContents`, frame, origin, URL, session/partition, vlasnistvo prozora, lifecycle generation i account context. Naziv kanala nije autentikacija.
3. Sprovedi resource-level autorizaciju za svaki fajl, nalog, tenant, uredjaj, job, update, podesavanje i privilegovanu radnju.
4. Koristi stroge seme sa limitima velicine, dubine, broja, string-a, putanje, enum-a i binarnih podataka. Odbij dodatna polja kada stvaraju dvosmislenost.
5. Kanonikalizuj putanje i URL-ove pre policy provera. Brani se od traversal-a, symlink/junction izlaza, alternate data stream-ova, UNC putanja, device putanja, case trikova i enkodovanih separatora.
6. Ucini side effect-e idempotentnim gde retry, dupli klik, renderer reload, duple poruke ili restart procesa mogu da ih ponove.
7. Ogranici konkurentne zahteve, redove, stopu stream-a, velicinu payload-a, velicinu odgovora i vreme izvrsavanja. Otkazi rad kada caller nestane gde je bezbedno.
8. Ne salji privilegovane rezultate zastarelom, navigiranom, unistenom ili ponovo koriscenom webContents-u bez ponovne validacije identiteta i account context-a.
9. Odvoji read, write, destruktivne, administrativne i update kanale. Zahtevaj dodatnu potvrdu ili autorizaciju za nepovratne operacije.
10. Loguj security-relevant odluke sa correlation ID-jevima i redakcijom, ukljucujuci odbijen sender, nevalidnu semu, scope failure, dupli zahtev i rate-limit dogadjaje.
11. Testiraj cross-window, subframe, navigated-frame, remote-origin, stale-renderer, destroyed-renderer, duplicate, replay, oversized, slow i concurrent IPC scenarije.
12. Tretiraj IPC kao lokalni network API sa nepoverljivim klijentom kada je kompromitacija renderer-a u threat model-u.

### 11.6 Session-i, dozvole, download-i i protokoli

1. Popisi sve session-e i partition-e. Konfigurisi permission request/check handler-e za svaki session koji moze da ucita remote ili user-controlled sadrzaj.
2. Default-deny camera, microphone, display capture, notifications, geolocation, MIDI, USB, serial, HID, Bluetooth, clipboard i fullscreen dozvole osim kada su eksplicitno potrebne.
3. Vezi permission odluke za tacan origin, frame, korisnicku radnju, nalog, uredjaj i trajanje. Perzistiraj samo kada je opravdano i opozivo.
4. Audituj cookie-je, proxy, cache, certificate verification, auth challenge-e, client sertifikate, service worker-e, extension-e i ciscenje storage-a po session-u.
5. Definisi download politiku: dozvoljene origin-e, MIME i extension provere, izbor destinacije, overwrite ponasanje, quarantine/Mark-of-the-Web, malware scan, partial fajlove, otkazivanje i ponasanje pri otvaranju.
6. Implementiraj custom protokole kao privilegovane parser-e: normalizuj putanje, namerno definisi standard/secure/cors/fetch/stream privilegije, ograniči metode i origin-e i spreci traversal.
7. Izbegavaj `file://` za privilegovani app sadrzaj gde secure custom protokol daje jasniji origin i policy model.
8. Testiraj certificate error-e, captive portal-e, proxy auth, offline rezim, redirect-e, zlonamerna imena fajlova, archive bomb-e, partial download-e i download-to-execute lance.

### 11.7 Navigacija, novi prozori, external open i webview-i

1. Koristi `will-navigate`, obradu redirect-a i window-open handler-e da sprovedes tacnu navigation i popup politiku.
2. Validiraj svaki URL prosledjen `shell.openExternal` ili OS launch API-jima. Dozvoli samo potrebne scheme i host-ove; odbij lokalne fajlove, executable protokole, script scheme, malformed URL-ove i proizvoljne custom protokole.
3. Ne koristi `<webview>` osim ako njegove prednosti izolacije i lifecycle-a nadmasuju attack surface. Preferiraj `WebContentsView` ili sistemski browser kada je primereno.
4. Ako `<webview>` postoji, validiraj `will-attach-webview` options i source, ukloni opasan preload i dozvole, odbij `allowpopups` i izoluj partition-e.
5. Verifikuj OAuth, payment, help, documentation, support i third-party content tokove pod redirect i compromised-content uslovima.
6. Spreci nepoverljivi sadrzaj da kontrolise window feature-e, izbor preload-a, partition, sandbox, devtools, download lokaciju ili eksterne aplikacije.
7. Audituj drag-and-drop i link handling zbog curenja lokalnih fajlova i izvrsavanja komandi/protokola.
8. Testiraj nested frame-ove, dinamicki kreirane webview-e, same-origin promene, history navigaciju, server redirect-e i post-authentication navigaciju.

### 11.8 Fuses, ASAR integrity i ojacavanje executable-a

1. Pregledaj fuses u stvarnom zapakovanom executable-u. Ne oslanjaj se samo na Forge ili build konfiguraciju.
2. Proceni fuses kao sto su iskljucivanje `RunAsNode`, ogranicavanje uticaja `NODE_OPTIONS` i `NODE_EXTRA_CA_CERTS` gde je primereno, iskljucivanje inspection argumenata, obavezno ASAR app ucitavanje i ukljucivanje embedded ASAR integrity validacije.
3. Promeni fuses nakon pakovanja i pre code signing-a, zatim verifikuj finalni potpisani binary. Zabelezi tacnu verziju fuse alata i opcije.
4. Razumi compatibility uticaj pre iskljucivanja ponasanja; testiraj CLI integracije, child procese, debugging, enterprise sertifikate i native module-e.
5. Ukljuci ASAR integrity samo sa kompletnom potrebnom kombinacijom fuse-ova i packaging tokom. Verifikuj da izmenjene arhive otkazuju kako je ocekivano.
6. Drzi executable kod van writable raspakovanih resursa. Opravdaj svaku `asarUnpack` putanju i zastiti njen load path.
7. Verifikuj signature i ASAR integrity ponasanje posle installer instalacije, delta update-a, full update-a, repair-a i rollback-a.
8. Tretiraj fuses i ASAR kao defense in depth, ne kao zamenu za bezbednu renderer izolaciju, IPC autorizaciju, signing i update poverenje.

### 11.9 Utility procesi, worker-i, extension-i i native module-i

1. Preferiraj utility procese nad ad hoc Node child procesima kada Electron lifecycle, sandbox i MessagePort integracija daju bezbedniji fit; opravdaj izuzetke.
2. Popisi Node child procese, fork-ovane worker-e, worker thread-ove, renderer worker-e, service worker-e, GPU task-ove, extension procese i native helper procese.
3. Validiraj konstrukciju child executable-a i argumenata; izbegavaj shell interpretaciju; koristi eksplicitne allowlist-e promenljivih okruzenja i radne direktorijume.
4. Ogranici broj procesa, CPU, memoriju, file descriptor-e, output buffer-e, ucestalost restart-a i dubinu reda. Spreci crash loop i fork bomb.
5. Autentifikuj lokalni IPC prema helper-ima i spreci drugi lokalni proces da imitira aplikaciju ili se poveze na privilegovane socket-e/pipe-ove.
6. Verifikuj putanje ucitavanja native modula, potpise gde su dostupni, ABI kompatibilnost, DLL search order, rpath, library search putanje i hijacking kroz writable direktorijume.
7. Iskljuci ili strogo kontrolisi Chrome extension-e, devtools extension-e, remote debugging, inspect port-ove i automation interfejse u produkciji.
8. Testiraj helper crash, hang, malformed output, oversized output, partial protocol poruke, version mismatch, update overlap i gasenje aplikacije.

## 12. Tauri-specific audit

### 12.1 Core, CLI, API, runtime, WebView i plugin matrica

1. Razresi tacne verzije `tauri`, `tauri-build`, `tauri-cli`, `@tauri-apps/cli`, `@tauri-apps/api`, runtime-a, Wry-ja, Tao-a, bundler-a, macro-a i svakog zvanicnog ili third-party plugin-a.
2. Ne nameci vestacku jednakost verzija nezavisno objavljenim komponentama. Umesto toga verifikuj njihovu dokumentovanu kompatibilnost i stvarno generisano/runtime ponasanje.
3. Zabelezi Rust toolchain i MSRV, Cargo feature-e, frontend package manager, generisane seme, target triple-ove, mobile overlay-e ako postoje i platform-specific podrsku plugin-a.
4. Identifikuj sistemsku WebView implementaciju i minimalnu podrzanu verziju na svakom target-u: WebView2, WKWebView/WebKit, WebKitGTK ili mobile WebView. Testiraj ponasanje na najstarijem podrzanom okruzenju.
5. Verifikuj da li je WebView2 evergreen, fixed, embedded, offline-installed, store-provided ili se pretpostavlja da postoji. Ukljuci installer i enterprise-offline ponasanje.
6. Pregledaj Tauri release notes, breaking changes, plugin changelog-e, generisane ACL seme i platform ogranicenja za razresene verzije.
7. Popisi third-party plugin-e i fork-ove. Pregledaj njihov Rust core, guest JavaScript, dozvole, scope-ove, build script-e, native kod, release proces i maintenance stanje.
8. Definisi upgrade ritam koji pokriva core, CLI, JS API, plugin-e, Rust, sistemske WebView zahteve, installer tooling i OS podrsku.

### 12.2 Capabilities, permissions, scopes i Runtime Authority

1. Popisi svaki capability fajl, inline capability, permission definiciju, scope, deny pravilo, target platformu, remote URL pattern, window label-u i webview label-u.
2. Izgradi efektivnu permission matricu nakon spajanja svih capabilities. Prozori ili webview-i navedeni u vise capabilities dobijaju uniju njihovih dozvola.
3. Koristi stabilne, jedinstvene window/webview label-e i verifikuj da dinamicko kreiranje ne moze slucajno da match-uje ili nasledi siru capability.
4. Default-deny privilegovane komande. Dodeli samo tacne komande i scope-ove potrebne odredjenom prozoru, webview-u, origin-u, ulozi i platformi.
5. Pregledaj `remote` capability grant-ove sa krajnjim oprezom. Remote origin koji dobija pristup lokalnom sistemu mora biti opravdan prema XSS-u, kompromitaciji naloga, DNS/CDN kompromitaciji i preuzimanju sadrzaja.
6. Koristi deny permissions gde daju defense in depth, ali razumi finalno merge i precedence ponasanje za razresenu verziju.
7. Verifikuj da custom scope-ove stvarno sprovodi implementacija komande ili plugin-a. Sama konfiguracija ne sprovodi application-defined scope.
8. Pregledaj generisane permission seme i plugin permission fajlove za tacnu dependency verziju. Ne kopiraj identifikatore iz nepovezanih verzija.
9. Verifikuj command registration i generisane app manifeste. Komande registrovane kroz siroke invoke handler-e i dalje moraju biti ogranicene capabilities i in-command autorizacijom.
10. Testiraj svaku privilegovanu komandu iz dozvoljenih i zabranjenih prozora, dozvoljenih i zabranjenih origin-a, subframe-ova, dinamicki kreiranih webview-a, zastarelih prozora i preimenovanih label-a.
11. Dokumentuj svaku capability bez jasnog vlasnika, svrhe, testa i uslova uklanjanja.
12. Tretiraj Runtime Authority kao jedan sloj authorization lanca, ne kao zamenu za poslovnu autorizaciju, validaciju putanje, vlasnistvo naloga ili potvrdu destruktivne radnje.

### 12.3 Commands, invoke, events, channels i managed state

1. Popisi svaku Tauri komandu, invoke handler, plugin komandu, event, channel, global listener, window listener, menu/tray radnju i Rust-to-frontend poruku.
2. Definisi stroge request i response tipove. Odbij dvosmislene untagged enum-e, neogranicene kolekcije, duboko ugnjezdene podatke, prevelike string/binary vrednosti, nepoznata polja gde su opasna i gubitnicke numericke konverzije.
3. Autorizuj unutar komande koristeci caller window/webview/origin, nalog, ulogu, vlasnistvo resursa, trenutno stanje aplikacije i nameru operacije.
4. Validiraj i kanonikalizuj sve putanje, URL-ove, nazive komandi, device identifikatore, kljuceve baze i identifikatore eksternih servisa pre upotrebe.
5. Ne izlaži genericke filesystem, shell, process, SQL, HTTP, plugin ili command dispatcher-e frontend-u osim ako imaju usko scoped i formalno pregledanu politiku.
6. Ogranici command concurrency, trajanje, memoriju, output, channel rate, event fan-out, broj listener-a i dubinu reda. Podrzi cancellation gde je bezbedno.
7. Koristi managed state sa eksplicitnom sinhronizacijom i vlasnistvom. Audituj izbor mutex/RwLock-a, redosled lock-ova, blocking u async kontekstima, poisoning, reentrancy i shutdown ponasanje.
8. Ne drzi lock preko await-a, IPC callback-a, filesystem/network operacije ili frontend event-a bez dokazanog dizajna.
9. Ucini destruktivne i spolja vidljive komande idempotentnim ili zasticenim od duplog invoke-a, double click-a, event replay-a, renderer reload-a i restart-a procesa.
10. Definisi stabilne error kodove i redigovane poruke. Pretvori panic i library greske u kontrolisane otkaze na granici.
11. Ukloni listener-e i zatvori channel-e kada se prozor unisti, navigira, logout-uje ili zameni. Spreci zastarele poruke da stignu u novi account context.
12. Testiraj malformed serialization, nepoznate komande, odbijenu capability, nevalidan scope, stale caller, dupli poziv, concurrent poziv, cancellation, panic i shutdown.

### 12.4 Zvanicni i third-party plugin-i

1. Napravi plugin matricu: svrha, verzija, frontend API, Rust crate, podrzane platforme, dozvole, scope-ovi, native dependency-ji, storage, mrezni pristup, vlasnik update-a i testovi.
2. Pregledaj default permission set-ove pre koriscenja. Praktican `plugin:default` grant moze ukljuciti vise komandi nego sto je prozoru potrebno.
3. Preferiraj pojedinacne allow permissions i uske scope-ove za filesystem, shell, process, opener, HTTP, SQL, store, clipboard, notification, dialog, deep link, single instance, global shortcut, autostart i updater funkcionalnost.
4. Pregledaj permission-e koje plugin generise i application-added prosirenja. Osiguraj da se custom scope tipovi parsiraju i sprovode konzistentno.
5. Audituj redosled inicijalizacije plugin-a, managed state, background thread-ove, event listener-e, migration ponasanje, cleanup i error handling.
6. Verifikuj path promenljive i scope ekspanziju prema platform-specific direktorijumima, symlink-ovima, junction-ima, Unicode-u, case sensitivity-ju, removable media i network share-ovima.
7. Proveri da li plugin po default-u izlaže opasne frontend komande ili tek posle capability grant-a. Testiraj stvarnu razresenu verziju.
8. Tretiraj nezvanicne plugin-e i fork-ove kao application kod: pregledaj source, release provenance, odrzavaoce, advisory-je, build script-e, native kod i incident response.
9. Ukloni neiskoriscene plugin-e i Cargo feature-e iz finalnog binarnog fajla i capabilities.
10. Testiraj ponasanje plugin-a na nepodrzanim ili delimicno podrzanim platformama i osiguraj da UI ne nudi nefunkcionalne ili nebezbedne operacije.

### 12.5 Filesystem, shell, opener, process i sidecar-i

1. Ogranici filesystem pristup po komandi i kanonickom scope-u. Razlikuj fajlove koje je korisnik izabrao od application-controlled putanja i sirokih grant-ova direktorijuma.
2. Spreci traversal i izlaz kroz symlink-ove, junction-e, alias-e, hard link-ove, UNC/device putanje, promene case-a, Unicode normalizaciju, alternate data stream-ove i race condition izmedju provere i upotrebe.
3. Koristi bezbedne create/write/replace obrasce, dozvole privremenih fajlova, atomic rename gde je podrzan, fsync zahteve, conflict handling i oporavak od partial write-a.
4. Nikada ne izlaži proizvoljne shell string-ove. Koristi allowlisted programe ili bundled sidecar-e, strukturisane argumente, bez shell interpretacije, eksplicitno okruzenje, eksplicitni radni direktorijum i ogranicen output.
5. Verifikuj razresavanje sidecar putanje, bundled target-triple naming, executable dozvole, potpis/hash, version handshake, update coupling i hijacking kroz writable putanju.
6. Autentifikuj lokalnu komunikaciju sa sidecar-ima ili servisima. Koristi zasticene socket-e/pipe-ove, random tajne ili OS kredencijale, peer verifikaciju i usku kontrolu pristupa.
7. Validiraj URL-ove i scheme prosledjene opener API-jima. Odvoji otvaranje HTTPS dokumentacije od pozivanja proizvoljnih application protokola.
8. Definisi child-process timeout, cancellation, graceful stop, forced termination, ciscenje potomaka, output backpressure, crash retry i quarantine ponasanje.
9. Audituj elevation i administrator/root helper-e. Koristi platform-approved privilege separation i autentifikuj zahteve; nikada ne pokreci ceo UI privilegovano radi pogodnosti.
10. Testiraj zlonamerna imena fajlova, executable substitution, argument injection, environment injection, lokalnu impersonation, sidecar version mismatch, partial output, hang, crash i gasenje aplikacije.

### 12.6 Asset protocol, CSP, isolation i remote sadrzaj

1. Popisi asset/custom protocol konfiguraciju, dozvoljene putanje, scope, CSP, dev URL, frontend distribution direktorijum, remote URL-ove i sve asset conversion helper-e.
2. Verifikuj da produkcioni build ne moze da ucita development server ili nepoverljiv URL zbog environment drift-a ili fallback ponasanja.
3. Koristi restriktivan CSP i isolation podesavanja koja podrzava razresena Tauri/WebView verzija. Testiraj na svakom sistemskom WebView-u jer se enforcement i feature podrska mogu razlikovati.
4. Tretiraj `convertFileSrc` i asset protocol pristup kao privilegovano otkrivanje fajla. Ogranici koji fajlovi i direktorijumi mogu da se konvertuju i renderuju.
5. Ne dodeljuj remote URL-ovima capabilities osim ako je kompletan compromise scenario prihvacen i ublazen. Preferiraj remote webview bez privilegija ili sistemski browser.
6. Verifikuj navigation, popup, download, external-open, clipboard, media, permission i devtools ponasanje u svakom webview-u.
7. Audituj frontend dependency-je i XSS sink-ove istom strogoscu kao kod Electron-a; manji native core ne cini kompromitovan web sadrzaj bezopasnim kada su komande izlozene.
8. Testiraj malformed asset URL-ove, encoded traversal, local-file probing, remote redirect-e, kompromitovan frontend bundle, CSP bypass pokusaje i zastarelu capability dodelu.

### 12.7 Unsafe Rust, FFI, mobile overlay i platform kod

1. Pregledaj svaki `unsafe` blok sa dokumentovanim invariantama, ownership, lifetime, thread, alignment, aliasing, initialization i error pretpostavkama.
2. Audituj FFI granice za ABI, layout strukture, encoding string-a, duzinu buffer-a, lifetime callback-a, prelazak exception-a/panic-a, cancellation i library version mismatch.
3. Verifikuj da platform moduli i conditional compilation proizvode ekvivalentne security odluke; odsutan kod na jednom target-u ne sme tiho da prosiri ponasanje.
4. Pregledaj Objective-C/Swift, C/C++, Java/Kotlin, PowerShell, shell i installer custom action-e istom disciplinom nalaza kao Rust i TypeScript.
5. Ako postoje mobile target-i, posebno audituj generisane Android/iOS projekte, dozvole, intent-e/URL scheme, WebView podesavanja, signing, prodavnice, background ponasanje i plugin hook-ove.
6. Testiraj odsustvo native biblioteke, pogresnu arhitekturu, signature failure, odbijenu dozvolu, OS API deprecation, callback posle shutdown-a i malformed native podatke.
7. Koristi sanitizer-e, Miri, fuzzing, clippy, compiler upozorenja i platform diagnostics gde je primenljivo, ali povezi nalaze sa isporucenim kodom i runtime dostiznoscu.
8. Ne prepisuj bezbedan funkcionalan kod u `unsafe` ili custom FFI samo radi performansi bez merenja i odrzavane test strategije.

## 13. Lokalni podaci, baze, fajlovi i oporavak

### 13.1 Inventar i klasifikacija podataka

1. Popisi svaku persistent lokaciju: app data, user data, config, cache, logove, crash dump-ove, temp, download-e, baze, browser profile-e, cookie-je, secure storage, OS kredencijale, keychain, registry/plist, shared container-e i removable/network storage.
2. Klasifikuj podatke po vlasniku, nalogu/tenant-u, osetljivosti, retention-u, backup-u, sinhronizaciji, prenosivosti, brisanju i zakonskim zahtevima.
3. Odvoji tajne od preferences, cache od durable stanja, izvedene podatke od source-of-truth podataka i account-specific podatke od device-wide podataka.
4. Dokumentuj putanje po platformi, tipu paketa, portable rezimu, store sandbox-u, enterprise redirection-u, roaming profilu i vise instaliranih kanala.
5. Verifikuj directory i file dozvole posle ciste instalacije, upgrade-a, repair-a, downgrade-a, promene naloga i migracije.
6. Spreci jednog lokalnog OS korisnika, app kanal, nalog, tenant ili prethodnu instalaciju da cita podatke drugog osim kada je eksplicitno dizajnirano.
7. Definisi sta prezivljava uninstall, sta se uklanja, sta zahteva potvrdu korisnika i kako se obradjuju enterprise-managed podaci.
8. Testiraj malo slobodnog diska, read-only media, kvotu, duzinu putanje, Unicode, case razlike, antivirus lock, concurrent pristup i nagli nestanak napajanja.

### 13.2 Baze, migracije, konkurentnost i integritet

1. Identifikuj svaki embedded ili lokalni database engine, tacnu verziju, extension-e, encryption sloj, journal mode, locking model, busy timeout, schema verziju i backup metod.
2. Pregledaj schema constraint-e, foreign key-eve, uniqueness, check-ove, index-e, transaction boundary-je, isolation, conflict handling i recovery.
3. Nikada se ne oslanjaj samo na application validaciju za durable invarijante. Dodaj database constraint-e gde su podrzani i kompatibilni.
4. Dizajniraj migracije za crash safety, idempotency, forward compatibility, rollback ili forward repair, zahteve prostora i preklapanje stare/nove aplikacije.
5. Napravi backup ili snapshot pre destruktivnih migracija. Verifikuj citljivost backup-a i restore u izolovanom okruzenju.
6. Testiraj dva prozora/procesa, background job-ove, sidecar-e, sync engine-e i stare/nove verzije koje pristupaju istim podacima gde je to moguce.
7. Spreci duple eksterne side effect-e oko lokalnih transakcija pomocu idempotency kljuceva, outbox/inbox obrazaca, durable state machine-a ili compensating action-a.
8. Eksplicitno obradi korupciju: detekciju, read-only safe mode, export, granice repair-a, restore, telemetriju, komunikaciju korisniku i zabranu tihog reset-a.
9. Verifikuj cuvanje encrypted database kljuca, rotaciju, recovery, promenu naloga, migraciju uredjaja i ponasanje kada secure storage nije dostupan.
10. Testiraj prekid migracije na svakom durable koraku, downgrade posle migracije, concurrent startup, lock contention, pun disk i korumpiran journal/WAL.

### 13.3 Fajlovi, import, export, arhive i korisnicki sadrzaj

1. Tretiraj svaki importovan, otvoren, prevucen, nalepljen, sinhronizovan ili preuzet fajl kao nepoverljiv bez obzira na ekstenziju.
2. Validiraj format parser-om i sadrzajem, ne samo ekstenzijom ili MIME-om. Ogranici velicinu, dimenzije, broj entry-ja, compression ratio, nesting, parse vreme, memoriju i output.
3. Koristi robustan parser u ogranicenom procesu kada je moguce. Audituj native codec-e i document biblioteke zbog memory-safety i command-execution rizika.
4. Spreci path traversal, apsolutne putanje, symlink extraction, hard-link zloupotrebu, device fajlove, alternate stream-ove, overwrite, nasledjivanje dozvola i archive bomb-e.
5. Kreiraj export atomski sa bezbednim dozvolama i eksplicitnim overwrite ponasanjem. Izbegni curenje tajni, skrivenih kolona, obrisanih zapisa, internih ID-jeva ili podataka nepovezanog naloga.
6. Sanitizuj imena fajlova za svaku platformu bez kreiranja kolizija ili gubitka mogucnosti mapiranja na izvor.
7. Oznaci ili karantiniraj preuzete/generisane fajlove gde platform expectations to zahtevaju i ne otvaraj automatski executable ili active content.
8. Testiraj malformed, truncated, oversized, polyglot, password-protected, nested, malicious-name i concurrently modified fajlove.

## 14. Mreza, lokalni servisi, proxy-ji i sertifikati

### 14.1 Udaljeni mrezni pozivi

1. Popisi frontend, main/Rust, plugin, sidecar, updater, telemetry, crash, licensing, payment i installer network klijente.
2. Definisi connect, TLS, header, body, idle, stream, total i retry deadline-e. Propagiraj cancellation i razlikuj korisnicko otkazivanje od mreznog otkaza.
3. Retry samo bezbedne ili idempotentne operacije sa ogranicenim brojem pokusaja, exponential backoff-om, jitter-om, retry budget-om i postovanjem server rate-limit signala.
4. Validiraj redirect-e, finalni origin, content type, velicinu, sertifikat, proxy ponasanje i DNS promene za privilegovane download-e i update metadata.
5. Zastiti se od SSRF-a gde user-controlled URL-ovi mogu da dosegnu localhost, privatne opsege, metadata servise, Unix socket-e, named pipe-ove ili privilegovane lokalne endpoint-e.
6. Ne iskljucuj TLS verifikaciju globalno. Ako se koriste certificate pinning ili custom root-ovi, definisi rotaciju, expiry, backup trust, proxy kompatibilnost i recovery.
7. Rediguj authorization header-e, cookie-je, tokene, device identifikatore, license podatke, licni sadrzaj i query tajne iz logova i crash report-ova.
8. Testiraj offline, captive portal, DNS failure, proxy auth, TLS interception, istekao sertifikat, clock skew, slowloris, partial response, oversized response i retry storm.

### 14.2 Lokalni HTTP, socket, pipe i service interfejsi

1. Popisi svaki localhost listener, Unix socket, named pipe, loopback WebSocket, custom URI broker, privilegovani servis, browser callback server i developer port.
2. Bind-uj na najuzi interfejs i koristi OS dozvole, random nepredvidive endpoint-e, autentikaciju, origin provere, request seme, rate limit-e i lifecycle kontrole.
3. Ne pretpostavljaj da je localhost pouzdan. Browser-i, drugi korisnici, sandboxed aplikacije, malware i lokalna mrezna izlozenost mogu dosegnuti pogresno bind-ovane servise.
4. Zastiti se od DNS rebinding-a, browser cross-origin zahteva, CSRF-like lokalnih zahteva, predvidjanja port-a, stale socket fajlova, named-pipe squatting-a i service impersonation-a.
5. Validiraj peer identitet za privilegovanu service ili helper komunikaciju. Vezi zahteve za trenutnu app instancu, korisnika, session, verziju i namenjenu operaciju.
6. Definisi startup race, konflikte port-a, redosled upgrade-a servisa, version handshake, reconnect, graceful shutdown i orphan cleanup.
7. Nikada ne izlaži genericke shell, filesystem, database, update ili credential funkcije preko lokalnog endpoint-a bez jake autentikacije i uske autorizacije.
8. Testiraj neautentifikovane lokalne zahteve, cross-origin browser zahteve, drugog OS korisnika, stale klijent, pogresnu verziju, replay, oversized payload, spor klijent i process crash.

## 15. Integracija sa operativnim sistemom i eksterni ulazi

### 15.1 Deep link-ovi, protocol handler-i, file association-i i CLI

1. Popisi custom URI scheme, app link-ove, universal link-ove, file association-e, open-with handler-e, shell verb-ove, context-menu entry-je, command-line switch-eve, startup argumente i store activation payload-e.
2. Tretiraj svaki payload kao nepoverljiv. Parsiraj strukturno, ograniči velicinu/broj, kanonikalizuj putanje/URL-ove, zahtevaj ocekivane tipove radnji i odbij nepoznata polja i scheme.
3. Zastiti authentication callback-e pomocu state-a, nonce-a, PKCE-a, ocekivanog issuer-a, account binding-a, jednokratne upotrebe i expiry-ja.
4. Spreci argument, shell, URL, path i template injection pri prosledjivanju payload-a postojecoj instanci ili helper-u.
5. Definisi ponasanje pre nego sto je aplikacija spremna, tokom update-a, sa vise instanci, bez prijavljenog naloga i posle promene naloga.
6. Ne izvrsavaj niti automatski otvaraj sadrzaj samo zato sto ga je OS povezao sa aplikacijom.
7. Registruj i uklanjaj integracije konzistentno kroz cistu instalaciju, per-user/per-machine install, upgrade, repair, portable mode, store install, koegzistenciju kanala i uninstall.
8. Testiraj malformed encoding, ogroman payload, duplu aktivaciju, nested URL, local-file URL, alternativnu scheme, stale nalog i istovremene aktivacije.

### 15.2 Tray, meniji, shortcut-i, clipboard, notification-i i autostart

1. Mapiraj svaku tray/menu/global-shortcut/notification radnju na autorizovanu komandu i trenutno account/window stanje.
2. Ne veruj menu ID-ju, notification payload-u ili global shortcut event-u kao dokazu korisnickog identiteta ili namere.
3. Spreci duple registracije i stale handler-e kroz reload, update, promenu naloga, promenu ekrana, sleep/wake i vise instanci.
4. Minimizuj izlaganje osetljivih podataka u clipboard-u; cisti ga samo uz pazljivu ownership logiku i nikada ne unistavaj nepovezan korisnicki clipboard sadrzaj.
5. Sanitizuj notification sadrzaj i radnje. Izbegavaj prikaz tajni na lock screen-u i validiraj activation payload-e.
6. Opravdaj autostart, background mode, login-item helper-e, scheduled task-ove, servise i startup registry/plist entry-je. Obezbedi vidljivu korisnicku kontrolu i uklanjanje.
7. Verifikuj pristupacnost i keyboard navigaciju native menija, tray tokova, dialog-a i shortcut-a, ukljucujuci konflikte i lokalizovane label-e.
8. Testiraj odbijenu OS dozvolu, opozvanu dozvolu, promenjenu default aplikaciju, stale notification, shortcut konflikt, vise monitora, zakljucanu session-u i OS restart.

### 15.3 Uredjaji, media, screen capture, stampa i hardver

1. Popisi koriscenje kamere, mikrofona, display capture-a, audio output-a, USB-a, serial-a, HID-a, Bluetooth-a, smart card-a, stampaca, skenera, GPU-a, codec-a i custom driver-a.
2. Trazi minimalnu OS i web dozvolu u trenutku potrebe, objasni svrhu, obradi odbijanje i podrzi opoziv.
3. Autorizuj izbor uredjaja i operacije prema trenutnom korisniku/nalogu i poslovnoj politici; prisustvo uredjaja nije autorizacija.
4. Validiraj device descriptor-e i duzine podataka. Ogranici stream-ove, frame velicine, sample rate-ove, buffer-e, trajanje snimanja i storage.
5. Spreci nenamerno background snimanje posle zatvaranja prozora, logout-a, sleep-a, lock-a, promene naloga ili opoziva dozvole.
6. Audituj izbor screen-capture izvora i spreci tiho snimanje osetljivih prozora gde politika to zahteva.
7. Tretiraj nazive stampaca, putanje, page settings, media fajlove, codec-e i odgovore firmware-a uredjaja kao nepoverljive ulaze.
8. Testiraj uklanjanje uredjaja, odbijanje dozvole, partial frame-ove, malformed podatke, driver crash, hotplug storm, sleep/wake, vise uredjaja i update tokom aktivne upotrebe.

## 16. Auto-update, release kanali, rollback i opoziv

### 16.1 Zajednicki update trust model

1. Mapiraj ko moze da build-uje, potpisuje, objavljuje, menja metadata, menja endpoint-e, promovise kanale, pokrene rollout, pauzira rollout, forsira update, dozvoli downgrade i opozove izdanje.
2. Odvoji identitet artefakta, transport security, authenticnost metadata, artifact signature, platform code signature, channel politiku i installer autorizaciju. Svaka kontrola resava drugaciji problem.
3. Koristi nepromenljive versioned artefakte. Nikada ne menjaj bajtove na postojecem version URL-u nakon izdanja.
4. Vezi metadata za tacan proizvod, kanal, platformu, arhitekturu, verziju, minimum/current version pravila, artifact hash ili potpis, velicinu, vreme objave i rollout politiku.
5. Validiraj update metadata kao nepoverljiv mrezni ulaz. Ogranici velicinu i polja, odbij nepoznata platform mapiranja gde su opasna i obradi clock skew.
6. Po default-u spreci downgrade i cross-channel confusion. Ako kontrolisani rollback zahteva downgrade, definisi eksplicitno ovlascenje, compatibility provere, ponasanje migracije korisnickih podataka i ponovni upgrade.
7. Koristi staged rollout sa telemetrijom, minimalnim uzorkom, soak periodom, crash/startup/update/error pragovima, rucnom pauzom, automatskim abort-om i vlasnikom.
8. Definisi ponasanje za offline korisnike, preskocene verzije, veoma stare klijente, nepodrzan OS, nepodrzanu arhitekturu, proxy/captive portal, metered mrezu, malo diska i prekinut download.
9. Verifikuj full i differential update put nezavisno. Delta update ne sme zaobici integrity, signing ili package-content provere.
10. Testiraj update sa svake podrzane izvorne verzije na kandidat, ne samo candidate-to-candidate ili cistu instalaciju.
11. Definisi rollback za application kod, lokalne podatke/semu, sidecar-e/servise, protokole, file association-e, konfiguraciju i cache-irano frontend stanje.
12. Odrzavaj kill switch ili mehanizam iskljucenja kanala koji sam ne stvara neautentifikovanu remote-control putanju.
13. Definisi response na kompromitaciju sertifikata/kljuceva: zamrzni publishing, opozovi ili ukloni poverenje, rotiraj kljuceve gde arhitektura dozvoljava, izdaj pouzdanu zamenu i komuniciraj oporavak.
14. Sacuvaj update logove i artefakte potrebne za incident istragu bez belezenja tajni.

### 16.2 Electron updater audit

1. Identifikuj updater implementaciju: ugradjeni `autoUpdater`, `update-electron-app`, Electron Forge publisher/update servis, Electron Builder updater, custom updater, store updater ili eksterni enterprise alat.
2. Verifikuj podrsku platforme i paketa za tacan updater. Ugradjeno ponasanje se razlikuje izmedju macOS-a, Squirrel.Windows-a, MSIX-a i Linux pakovanja; ne pretpostavljaj da jedan API daje identicnu cross-platform semantiku.
3. Na macOS-u verifikuj code signing, notarizaciju gde je potrebna, application identity, feed format, signature ponasanje i kompatibilnost hardened runtime-a/entitlement-a.
4. Na Windows-u verifikuj Squirrel/MSIX/NSIS/custom installer ponasanje, application user model ID, per-user/per-machine scope, update lock-ove, pokrenute instance i interakciju sa repair/uninstall tokom.
5. Zastiti se od duplih update provera i download-a. Osiguraj da UI radnje, timer-i, startup provere, reconnect i vise prozora ne pokrecu konkurentne update-e.
6. Validiraj feed URL i izbor kanala. Spreci renderer-kontrolisane proizvoljne feed URL-ove ili release kanale osim kada su strogo autorizovani.
7. Verifikuj `checkForUpdates`, download, cancellation, progress, ready stanje, quit-and-install, restart i error tranzicije kao jednu eksplicitnu state machine-u.
8. Ne instaliraj dok su kriticni write-ovi, migracije, export-i, snimanja, device operacije ili nepovratni job-ovi aktivni osim ako operacija moze bezbedno da se nastavi.
9. Verifikuj code-signature provere i package verifikaciju na finalnom distribution putu. Testiraj izmenjene metadata, izmenjen paket, pogresnog publisher-a, pogresan kanal, pogresnu arhitekturu i istekao/opozvan sertifikat.
10. Testiraj cistu instalaciju, normalan update, preskocene verzije, veoma star klijent, update dok aplikacija radi u tray-u, vise instanci, prekinut download, malo diska, zakljucan fajl, antivirus interference i forced shutdown.

### 16.3 Tauri updater audit

1. Razresi tacnu verziju updater plugin-a, Rust i JavaScript API verzije, capabilities, permissions, javni kljuc, endpoint konfiguraciju, install mode i platform podrsku.
2. Verifikuj da su update potpisi obavezni i provereni prema nameravanom pinovanom javnom kljucu. Zastiti privatni signing kljuc odvojeno od platform code-signing kljuceva.
3. Ogranici frontend updater dozvole. Prozor koji sme da proveri dostupnost ne mora automatski da ima download ili install ovlascenje.
4. Validiraj static JSON ili dynamic server metadata, ukljucujuci RFC 3339 datum ako se koristi, semantic verziju, platform key, arhitekturu, sadrzaj potpisa, URL, velicinu i release notes.
5. Verifikuj da runtime endpoint i header override-i ne mogu biti pod uticajem nepoverljivog renderer sadrzaja ili konfiguracije nizeg trust nivoa.
6. Testiraj Windows install mode-ove, elevation prompt-ove, restart ponasanje, pokrenute sidecar-e/servise i per-user/per-machine konzistentnost.
7. Testiraj Linux package-specific ponasanje umesto tretiranja AppImage, Debian, RPM, Flatpak, Snap i distribution repository-ja kao zamenljivih.
8. Testiraj macOS app bundle identitet, signing, notarizaciju, quarantine, update replacement i rollback ponasanje.
9. Ako custom version comparison dozvoljava rollback, zahtevaj autentifikovanu rollback odluku, data compatibility gate, eksplicitnu telemetriju i plan vracanja korisnika na bezbednu forward verziju.
10. Testiraj los potpis, nedostajuci potpis, pogresan kljuc, izmenjen paket, pogresan OS/architecture key, server error, partial download, malo diska, odbijenu dozvolu, prekinutu instalaciju i star klijent.

## 17. Code signing, notarizacija, kljucevi i poverenje artefakta

### 17.1 Signing arhitektura

1. Popisi svaki signing identitet i svrhu: Windows executable/installer, macOS aplikaciju/installer, Apple notarization kredencijale, Linux pakete, Tauri updater, store upload, mobile target-e i interno enterprise potpisivanje.
2. Koristi odvojene kljuceve gde threat model ili tooling zahtevaju separaciju. Dokumentuj koja kompromitacija pogadja koji kanal i kako se poverenje moze obnoviti.
3. Cuvaj privatne kljuceve u hardware-backed ili managed signing sistemima gde je prakticno. Ogranici export, interaktivnu upotrebu, CI pristup, uloge, odobrenja, IP/mrezu, repozitorijum, granu i okruzenje.
4. Koristi timestamping gde platform politika to podrzava da validna izdanja prezive istek sertifikata. Verifikuj timestamp authority i failure ponasanje.
5. Zabelezi certificate subject, issuer, serial/thumbprint, vazenje, key algoritam, timestamp, entitlement-e, hardened-runtime stanje, notarization rezultat i tacan hash artefakta bez izlaganja privatnog materijala.
6. Verifikuj potpise posle svih packaging, fuse, resource, installer i update transformacija. Nikada tiho ne menjaj potpisan artefakt.
7. Definisi overlap obnove sertifikata, opoziv, response na izgubljen kljuc, ponasanje isteklog sertifikata, kontinuitet publisher identiteta i emergency release procedure.
8. Odvoji signing od publishing-a tako da potpisan artefakt i dalje zahteva pregledanu promociju u kanal.
9. Audituj ko moze da posalje proizvoljne bajtove signing servisu. Zasticen kljuc nije dovoljan ako nepoverljivi job-ovi mogu traziti potpise.
10. Verifikuj lokalnu proveru potpisa i store/platform verifikaciju na cistim masinama, ne samo unutar CI-ja.

### 17.2 macOS signing, hardened runtime, entitlement-i i notarizacija

1. Verifikuj bundle identifier, team ID, tip sertifikata, designated requirement, potpise nested koda, framework-e, helper-e, login item-e, XPC/servise, sidecar-e i installer image-e.
2. Koristi minimalne entitlement-e. Opravdaj JIT, unsigned executable memory, iskljucenu library validation, automation, kameru, mikrofon, screen recording, fajlove, mrezu, keychain group-e i sandbox izuzetke.
3. Osiguraj da je svaki nested executable i framework potpisan pravilnim redosledom sa kompatibilnim entitlement-ima pre spoljnog bundle-a.
4. Pokreni strogu signature verifikaciju i proceni Gatekeeper ponasanje na cistom preuzetom artefaktu sa quarantine metadata.
5. Posalji tacan release artefakt na notarizaciju, verifikuj uspeh, staple-uj gde je primenljivo i potvrdi offline/online Gatekeeper ponasanje.
6. Testiraj direct download, DMG/PKG, App Store build gde je primenljivo, update replacement, helper launch, first run, permission prompt-ove i razlike OS verzija.
7. Definisi ponasanje kada notarizacija nije dostupna, kasni, odbijena je ili naknadno invalidirana. Ne izdaji neverifikovanu zamenu.
8. Sacuvaj notarization logove i submission ID-jeve vezane za hash-eve artefakta za incident response.

### 17.3 Windows signing i reputacija

1. Verifikuj Authenticode potpise na executable-ima, DLL-ovima, installer-ima, update paketima, driver/helper fajlovima i catalog fajlovima gde je primenljivo.
2. Koristi nameravani publisher identitet konzistentno kroz izdanja da sacuvas upgrade trust i reputaciju. Dokumentuj obnovu sertifikata i promene organizacije.
3. Timestamp-uj potpise i verifikuj i signature i timestamp chain na cistim podrzanim Windows verzijama.
4. Audituj EV/standard certificate ili managed-signing workflow, HSM/Key Vault pristup, sign-command argumente, digest algoritam, potrebu za dual-signing-om i cross-signing pretpostavke.
5. Verifikuj SmartScreen/Mark-of-the-Web ponasanje za direct download i kako se reputacija prati bez slabljenja korisnicke zastite.
6. Osiguraj da unsigned ili drugacije potpisani child binary fajlovi ne mogu da se ucitaju iz writable direktorijuma ili slucajno spakuju.
7. Testiraj install, repair, update, rollback, uninstall, side-by-side kanale, per-user/per-machine scope, UAC, zakljucane fajlove, antivirus i enterprise policy.
8. Definisi response na kompromitovane publisher kredencijale, opozvan sertifikat, false-positive malware klasifikaciju i suspenziju prodavnice.

### 17.4 Linux package signing i repository poverenje

1. Identifikuj svaki format distribucije i trust model: AppImage, Debian, RPM, Flatpak, Snap, AUR/source paket, tarball ili managed enterprise repository.
2. Verifikuj package/repository potpise, expiry metadata, distribuciju kljuceva, rotaciju, opoziv, poverenje mirror-a i vlasnistvo update-a.
3. Audituj desktop fajlove, MIME handler-e, ikone, AppStream metadata, sandbox dozvole, portal-e, systemd unit-e, polkit pravila, post-install script-e i uninstall script-e.
4. Ne tretiraj potpisan paket kao univerzalno pouzdan kroz distribucije. Testiraj tacan repository, store ili direct-download put.
5. Verifikuj library dependency-je i minimalne verzije distribucije na cistim podrzanim okruzenjima, ukljucujuci WebKitGTK i sistemske runtime zahteve za Tauri.
6. Testiraj install, upgrade, downgrade, rollback, package-manager conflict, read-only filesystem, sandbox portal-e, nedostajuce dependency-je i offline enterprise mirror-e.
7. Definisi kako direct-download korisnici dobijaju security update-e kada ne postoji ugradjeni updater ili kada distribution politika upravlja update-ima.
8. Dokumentuj response na kompromitaciju kljuca i preuzimanje repository-ja.

## 18. Installer, prodavnica, enterprise, upgrade i uninstall ponasanje

### 18.1 Installer semantika

1. Identifikuj installer tehnologiju, verziju, scope, elevation model, install putanju, data putanju, repair ponasanje, upgrade code/product code/bundle identitet, custom action-e, prerequisite-e i rollback podrsku.
2. Verifikuj cistu instalaciju, same-version repair, patch/minor/major upgrade, odbijanje downgrade-a, side-by-side kanale, per-user u per-machine tranziciju, tranziciju arhitekture i uninstall.
3. Ucini custom action-e minimalnim, deterministickim, logovanim, retry-safe i reverzibilnim. Nikada ne skrivaj proizvoljne network download-e ili shell execution unutar installer-a.
4. Validiraj putanje i dozvole koje installer kreira. Spreci normalne korisnike da zamene executable fajlove, DLL-ove, helper-e, update komponente ili privilegovanu konfiguraciju.
5. Namerno sacuvaj korisnicke podatke, eksplicitno ih migriraj i ukloni ih samo prema dokumentovanom izboru korisnika/enterprise-a.
6. Obradi pokrenute instance aplikacije, tray procese, servise, sidecar-e, zakljucane fajlove, antivirus, reboot-required stanje i prekinutu instalaciju.
7. Verifikuj registraciju i ciscenje protokola, file association-a, shortcut-a, startup entry-ja, servisa, scheduled task-ova, firewall pravila, driver-a i store metadata.
8. Testiraj installer logove i error poruke zbog curenja tajni i upotrebljivog recovery-ja.

### 18.2 Prodavnice i enterprise distribucija

1. Mapiraj Microsoft Store, Mac App Store, Snap/Flatpak prodavnice, package repository-je, MDM, software-distribution alate i direct-download kanale odvojeno.
2. Pregledaj sandbox, entitlement, API, payment, update, telemetry, privacy, age-rating i content pravila za svaki kanal.
3. Koristi channel-specific konfiguraciju umesto runtime nagadjanja. Verifikuj bundle identitet i kontinuitet data putanje izmedju store i direct build-a samo kada je migracija podrzana.
4. Spreci kanal nizeg trust nivoa da nenamerno update-uje ili zameni kanal viseg trust nivoa.
5. Verifikuj offline installer-e, proxy podrsku, deployment sertifikata, WebView/runtime prerequisite-e, silent install switch-eve, exit code-ove, logove i detection pravila za enterprise upotrebu.
6. Dokumentuj vlasnistvo store naloga, publisher organizacija, recovery kontakata, MFA-a, API kljuceva, signing profile-a i emergency pristupa.
7. Testiraj fallback posle store review/rejection-a, pauzu phased release-a, povlacenje paketa, mandatory update ogranicenja i korisnike zaglavljene na starim store verzijama.
8. Osiguraj da release notes, privacy deklaracije, dozvole, data safety i screenshot-ovi odgovaraju stvarnom ponasanju.

## 19. Performanse, odziv, resursi i kapacitet

### 19.1 Plan merenja

1. Definisi budzete za cold/warm startup, prvi upotrebljiv prozor, latenciju kriticne interakcije, IPC/command latenciju, update proveru, memoriju, CPU, GPU, disk, mrezu, bateriju, installer velicinu i package velicinu.
2. Meri na reprezentativnom minimalnom i tipicnom hardveru, podrzanim operativnim sistemima, x64/ARM64, cistim i zrelim profilima, online/offline i sa realnim volumenom podataka.
3. Odvoji frontend render vreme, framework bootstrap, native inicijalizaciju, database migraciju, credential pristup, network wait, plugin inicijalizaciju, sidecar startup i updater rad.
4. Snimi trace i profile pre optimizacije. Povezi long task-ove, main-thread blocking, Rust/Node blocking, lock contention, IPC serialization, database upite, filesystem, GPU i mrezu.
5. Testiraj idle ponasanje, hidden/tray rezim, minimizovane prozore, background timer-e, service worker-e, polling, telemetriju, device listener-e i updater ritam.
6. Ogranici cache i queue. Definisi eviction, persistence, account izolaciju, stale-data politiku i ponasanje pod memory pressure-om.
7. Meri leak ponasanje kroz otvaranje/zatvaranje prozora, navigaciju, reload, promenu naloga, otvaranje/zatvaranje dokumenta, connect/disconnect uredjaja, update i dugotrajan idle.
8. Ne tvrdi poboljsanje performansi samo na osnovu microbenchmark-a; potvrdi korisnicki tok i resource budget.

### 19.2 Odziv i containment otkaza

1. Odrzi renderer/UI thread-ove odzivnim. Premesti CPU-heavy parsing, compression, indexing, media, cryptography i database rad u odgovarajuce ogranicene worker-e ili native procese.
2. Ne blokiraj Electron main proces ili Tauri event loop sinhronim filesystem, network, crypto, database, child-process ili lock cekanjem.
3. Koristi backpressure od UI-ja kroz IPC/komande do worker-a i eksternih servisa. Odbacivanje, coalescing, pauziranje ili odbijanje rada mora biti eksplicitno.
4. Spreci jedan spor prozor, fajl, uredjaj, network zahtev, tenant/nalog ili plugin da iscrpi globalne resurse.
5. Definisi timeout-e i cancellation za operacije koje mogu da vise. Osiguraj da cancellation ne ostavlja korumpirane fajlove, poluprimenjene migracije ili duplirane side effect-e.
6. Obradi out-of-memory, GPU crash, renderer crash, sidecar crash, WebView failure, database lock i service outage sa ogranicenim recovery-jem.
7. Koristi crash restart samo sa limitima i validacijom stanja. Izbegni petlje koje ponovljeno unistavaju korisnicki rad ili bombarduju update/network servise.
8. Testiraj burst input, ogromnu istoriju, mnogo prozora, velike fajlove, spor disk, malo memorije, high DPI, vise ekrana, sleep/wake i dugotrajan offline rezim.

## 20. Pristupacnost, lokalizacija, ekran i unos

1. Testiraj rad samo tastaturom, logican focus redosled, vracanje focus-a, vidljiv focus, shortcut-e, menije, dialog-e, tray tokove, modal-e, alternative drag-u i escape/cancel ponasanje.
2. Verifikuj semanticke role, nazive, stanja, opise, live region-e, povezivanje greske, strukturu tabela/listi i screen-reader ponasanje.
3. Podrzi zoom, text scaling, OS scaling, high contrast, reduced motion, color filter-e, velike fontove i display density bez secenja ili nepristupacnih kontrola.
4. Testiraj high DPI, mixed-DPI monitore, connect/disconnect ekrana, orijentaciju, vracanje prozora sa nedostupnih ekrana, minimalnu velicinu, fullscreen i remote desktop.
5. Lokalizuj sav user-visible i accessibility tekst, native menije, notification-e, installer string-ove, file filter-e, objasnjenja dozvola, update poruke i error recovery.
6. Obradi RTL, pluralizaciju, date/time/number/currency formate, vremenske zone, Unicode normalizaciju, duge prevode i locale-specific sortiranje/pretragu.
7. Postuj IME, dead key-eve, compose key-eve, alternativne rasporede tastature, screen keyboard-e, pen/touch, alternative misu i assistive technology.
8. Ne oslanjaj se na boju, hover, animaciju, male target-e ili platform-inconsistent gesture kao jedini metod komunikacije.
9. Testiraj pristupacnost u zapakovanoj aplikaciji na svakoj platformi; browser-only testiranje nije dovoljno.
10. Dokumentuj opravdane izuzetke sa uticajem na korisnika, workaround-om, vlasnikom i planom sanacije.

## 21. Observability, crash reporting, privatnost i forenzika

1. Definisi structured logove, metrike, trace-ove, crash report-ove, update event-e, installer event-e, security event-e i user-visible diagnostic export.
2. Ukljuci verziju, kanal, commit/artifact identitet, platformu, arhitekturu, OS verziju, relevantnu WebView/Chromium/Node/Rust verziju, tip procesa, window label-u, correlation ID i operation stanje gde je bezbedno.
3. Rediguj tajne, tokene, cookie-je, authorization header-e, sadrzaj fajlova, licne putanje, korisnicka imena, nazive dokumenata, database zapise, clipboard podatke i osetljive URL-ove.
4. Koristi sampling i rate limit-e da sprecis telemetry storm, prekomerno prikupljanje privatnih podataka, pun disk i recursive crash-reporting otkaz.
5. Upload-uj simbole i source map-e vezane za tacne hash-eve artefakta. Ogranici pristup i retention.
6. Razlikuj renderer/webview, main/Rust core, GPU, utility, sidecar, installer, updater i native izvore crash-a.
7. Prati startup uspeh, crash-free session-e, adoption/failure update-a, rollback, migration failure, permission denial, IPC/command denial, queue saturation i resource budget-e.
8. Obezbedi privacy-preserving lokalni diagnostic bundle sa eksplicitnim korisnickim pregledom i pristankom gde je primereno.
9. Sacuvaj chain of custody za incident artefakte i izbegni menjanje kompromitovanih sistema pre snimanja dokaza.
10. Svaki produkcioni alert mora imati vlasnika, obrazlozenje praga, dashboard/kontekst, runbook i tumacenje uticaja na korisnika.

## 22. Test strategija i obavezni negativni scenariji

### 22.1 Slojevi testiranja

1. Unit-testiraj cistu poslovnu logiku, parser-e, validator-e, canonicalizer-e, state machine-e, authorization odluke, korake migracije i update-version politiku.
2. Contract-testiraj svaki preload bridge, Electron IPC kanal, Tauri komandu, event/channel payload, sidecar protokol, lokalni servis, update metadata i installer exit-code ugovor.
3. Integration-testiraj sa stvarnom filesystem semantikom, stvarnim embedded database engine-om, secure-storage apstrakcijom, reprezentativnim proxy/certificate setup-om i stvarnim platform WebView/runtime-om gde je primenljivo.
4. Pokreci testove zapakovane aplikacije, ne samo browser/dev-server testove. Verifikuj efektivne privilegije, resurse, potpise, putanje i OS integracije.
5. Koristi end-to-end testove za kriticne korisnicke tokove: install, first run, sign in, promenu naloga, file/device workflow, offline/online tranziciju, update, restart, rollback, export, logout i uninstall.
6. Koristi security testove za XSS-to-bridge dostiznost, IPC/command autorizaciju, path/URL validaciju, autentikaciju lokalnog servisa, update tampering, signature failure i data izolaciju.
7. Koristi concurrency i durability testove za duple radnje, vise prozora, vise instanci, background job-ove, database locking, update overlap, shutdown i crash recovery.
8. Koristi performance testove za startup, kriticne interakcije, velike podatke, burst input, mnogo prozora, idle, long-run leak-ove, malo resursa i spore dependency-je.
9. Koristi accessibility testove sa automatskim proverama plus keyboard i screen-reader verifikacijom u packaged build-ovima.
10. Koristi installation i update matrice na cistim snapshot-ovima/VM-ovima sa realnim starim verzijama i korisnickim podacima.
11. Svaka potvrdjena P0-P2 popravka mora imati fokusiran regression test koji bi pao pre popravke i prosao posle nje.
12. Zabelezi skipped, flaky, quarantined, platform-unavailable ili rucno verifikovane testove sa vlasnikom, razlogom, rizikom i exit kriterijumom.

### 22.2 Obavezni adversarial i failure scenariji

1. Kompromitovan renderer/webview pokusava svaki izlozeni Electron bridge ili Tauri komandu iz pogresnog origin-a, frame-a, prozora, label-e, naloga i lifecycle generation-a.
2. Zlonamerni IPC/command payload koristi dodatna polja, pogresne tipove, duboko ugnjezdavanje, ogromne string/binary vrednosti, traversal, symlink-ove, UNC/device putanje, alternativne scheme i enkodovane separatore.
3. Dva prozora ili instance istovremeno i posle renderer reload-a salju istu destruktivnu ili spolja vidljivu operaciju.
4. Caller navigira, logout-uje se, menja nalog, zatvara se ili se unistava dok je privilegovani rad u toku i pre isporuke rezultata.
5. Remote sadrzaj redirect-uje, otvara novi prozor, poziva eksterni protokol, preuzima active content i pokusava da zadrzi privilegije posle navigacije.
6. Lokalni nepoverljivi proces pokusava da se poveze na localhost/socket/pipe/helper interfejse, replay-uje poruke, imitira aplikaciju ili zauzme endpoint.
7. Update metadata, paket, potpis, publisher, kanal, arhitektura, verzija i endpoint se nezavisno menjaju.
8. Update se prekida tokom download-a, verifikacije, instalacije, prvog restart-a, migracije podataka, zamene sidecar-a i cleanup-a.
9. Cista instalacija, repair, upgrade sa svake podrzane stare verzije, skipped-version upgrade, downgrade pokusaj, rollback i uninstall rade sa realnim korisnickim podacima.
10. Signing sertifikat ili updater kljuc je istekao, opozvan, nedostaje, pogresan je, nedostupan ili se smatra kompromitovanim.
11. Disk postaje pun ili read-only tokom write-a, database transakcije, migracije, export-a, download-a, update-a, logovanja i crash reporting-a.
12. Aplikacija se ubija, OS se gasi, korisnik se logout-uje, masina ide u sleep ili nestaje napajanje tokom kriticnog rada.
13. Native module, sidecar, plugin, WebView runtime, codec, driver ili sistemski dependency nedostaje, pogresne je arhitekture, nekompatibilan, spor, zaglavljen ili zlonamerno zamenjen.
14. Proxy auth, captive portal, DNS failure, TLS interception, certificate error, clock skew, spor server, partial response, oversized response i retry storm se dogadjaju.
15. Korisnik menja nalog, OS korisnika, kanal ili profil dok cache, cookie-ji, prozori, background rad, notification-i i lokalni podaci jos postoje.
16. Mnogo prozora, veliki fajlovi, hotplug storm, burst IPC/event-i, spor consumer i dugotrajan idle guraju CPU, memoriju, GPU, disk, queue i listener limite.

### 22.3 Matrica platformi i arhitektura

| Dimenzija | Obavezna pokrivenost | Dokaz |
| --- | --- | --- |
| Operativni sistem | Svaki podrzani Windows, macOS i Linux baseline plus trenutne reprezentativne verzije | Cist VM/uredjaj, tacan build, install/update/runtime rezultati |
| Arhitektura | x64, ARM64 i svaki dodatni isporuceni target | Verifikacija native module-a/sidecar-a/plugin-a/paketa/potpisa/runtime-a |
| Distribucija | Direct, store, enterprise, portable, repository ili package format koji se stvarno isporucuje | Channel-specific install, update, rollback i policy dokaz |
| Izvorna verzija | Cista instalacija i svaki podrzani upgrade source, ukljucujuci realno staru verziju | Versioned snapshot-ovi sa reprezentativnim korisnickim podacima |
| Okruzenje | Online, offline, proxy, enterprise TLS interception gde je podrzan, malo diska, malo memorije | Zabelezeni uslovi, logovi, user-visible ishod, recovery |
| Ekran/unos | Jedan/vise mixed-DPI ekrana, tastatura, screen reader, IME, touch gde je podrzan | Packaged-app accessibility i window-state dokaz |

## 23. CI/CD, release governance i promocija artefakta

1. Mapiraj workflow-e od pull request-a do testa, pakovanja, signing-a, notarizacije, publishing-a, promocije, store upload-a, update manifesta, rollout-a, pauze, rollback-a i incident izdanja.
2. Odvoji izvrsavanje nepoverljivog koda od privilegovanih release job-ova. Zahtevaj pregledane commit-e, protected environment-e, odobrenja i branch/tag politiku.
3. Koristi matrix build-ove za podrzane platforme/arhitekture i zabelezi koji koraci rade nativno, cross-compile-uju ili koriste remote builder-e.
4. Promovisi isti nepromenljiv artefakt kroz verifikaciju, signing gde redosled dozvoljava, staging i release. Objasni svaku neizbeznu transformaciju.
5. Verifikuj sadrzaj paketa, fuses/capabilities, SBOM, provenance, potpise, notarizaciju, installer metadata, malware/reputation scan i update metadata pre promocije.
6. Zastiti dodelu release verzije od race-a i duplih tag-ova. Osiguraj da application, package, installer, store i feed verzije ostanu konzistentne.
7. Zahtevaj release notes sa security/privacy/migration/update uticajem, poznatim problemima, promenama podrske i rollback uslovima.
8. Definisi automatske i rucne release gate-ove, abort pragove, canary/phased kohorte, soak periode, vlasnika i emergency stop.
9. Zadrzi tacne artefakte, simbole, source map-e, manifeste, logove, potpise, hash-eve, odobrenja i environment identitet tokom support i incident prozora.
10. Testiraj release pipeline koristeci neprodukcione signing/update/store target-e i periodicno vezbaj emergency release i rollback.
11. Ne dozvoli renderer/frontend-u, pull-request job-u ili opstem developer token-u da objavljuje update metadata ili potpisane artefakte.
12. Zabelezi preostale rucne korake i ucini ih two-person, checklist-driven, auditabilnim i recoverable.

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

## 25. Incident rezim

1. Sacuvaj volatile dokaze pre ciscenja: pokrenute procese, executable putanje, ucitane module, command line-ove, network konekcije, otvorene fajlove, updater stanje, installer logove, potpise, hash-eve, browser/WebView storage i relevantne memory/crash artefakte.
2. Izoluj pogodjene release kanale, signing/publishing kredencijale, update endpoint-e, prodavnice, CDN objekte, lokalne servise i administrativni pristup prema containment planu.
3. Utvrdi da li je kompromitacija u renderer sadrzaju, privilegovanom bridge-u, native core-u, dependency-ju, build sistemu, signing sistemu, update metadata, distribution kanalu, installer-u, lokalnim podacima ili eksternom servisu.
4. Ne unistavaj dokaze reinstall-om, auto-update-om, brisanjem cache-a, slepom rotacijom svih kljuceva ili pokretanjem nepregledanih cleanup alata pre prikupljanja.
5. Prvo opozovi ili iskljuci najuzi pogodjeni trust put, ali pretpostavi siri uticaj dok dokaz ne suzi opseg.
6. Izgradi replacement artefakte iz verifikovanog commit-a u pouzdanom cistom okruzenju sa pregledanim dependency-jima, novim ili verifikovanim kredencijalima, SBOM-om, provenance-om, potpisima i pregledom paketa.
7. Testiraj cistu instalaciju, in-place recovery, update kompromitovane verzije, cuvanje podataka, reset kredencijala, rotaciju kljuceva i rollback pre izdanja.
8. Tacno komuniciraj pogodjene verzije, platforme, kanale, indikatore, korisnicke radnje, uticaj na podatke i recovery status bez spekulacije.
9. Sacuvaj timeline source-a, build-a, signing-a, publishing-a, distribucije, instalacije, izvrsavanja, detekcije, containment-a, eradication-a, recovery-ja i follow-up-a.
10. Isporuci root cause, control failure, detection gap, blast radius, recovery dokaz, preostali rizik i preventivne akcije sa vlasnicima i rokovima.

## 26. Obavezne evidence matrice

### 26.1 Source-to-runtime matrica

| source commit | razreseni graf | builder | paket | potpis | distribution objekat | instalirani binary | runtime proces | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.2 Matrica privilegija prozora i webview-a

| prozor/webview | origin | session/partition | preload/capability | dozvole | podaci/nalog | navigacija | vlasnik | testovi | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.3 IPC i command matrica

| kanal/komanda | caller | sema | autentikacija | autorizacija | scope | side effect | idempotency | limiti | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.4 Filesystem i external-open matrica

| operacija | izvor | kanonikalizacija | dozvoljeni scope | symlink/race odbrana | dozvole | audit | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.5 Matrica lokalnih podataka i migracija

| skladiste/putanja | vlasnik | osetljivost | sema/verzija | migracija | backup | restore | izolacija naloga | brisanje | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.6 Network i local-service matrica

| klijent/listener | endpoint | trust | auth | TLS/peer provera | timeout | retry/backpressure | podaci | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.7 Dependency i native-code matrica

| komponenta | razresena verzija | izvor | isporucena | privilegija | native/build kod | advisory | kompatibilnost | vlasnik | akcija |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.8 Matrica artefakta, signing-a i prodavnice

| platforma/kanal | artefakt | hash | sadrzaj paketa | signing identitet | timestamp/notary | prodavnica/repository | verifikacija | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.9 Update i rollback matrica

| izvorna verzija | target | platforma/kanal | metadata | potpis | migracija podataka | failure point | rollback/recovery | test | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.10 Platform i installer matrica

| OS/verzija | arhitektura | format | cista instalacija | upgrade | repair | rollback | uninstall | OS integracija | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.11 Performance i resource matrica

| tok | uredjaj/profil | budzet | izmereno | usko grlo | popravka | regression test | preostali rizik | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

### 26.12 Operational readiness matrica

| kontrola | vlasnik | dokaz | alert | runbook | abort prag | rollback | poslednja vezba | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` | `[POPUNITI]` |

## 27. Production readiness checklist

1. Podrzane framework/runtime/toolchain verzije su verifikovane iz source-a, lock fajlova, zapakovanog artefakta i runtime-a. Nema neodobrenog preview-a ili nepodrzanog major-a.
2. Repozitorijum, generisana konfiguracija, dependency graf, build script-i, native kod, plugin-i i supply-chain trust su popisani i imaju vlasnike.
3. Source-to-installed-runtime identity lanac je dokazan ili je svaki prekid eksplicitan blocker/preostali rizik.
4. Svaki prozor/webview ima dokumentovan origin, lifecycle, session, privilegiju, bridge/capability, navigation politiku, vlasnika podataka i negativne testove.
5. Electron webPreferences/preload/IPC ili Tauri capabilities/permissions/scopes/commands sprovode least privilege u stvarnoj zapakovanoj aplikaciji.
6. Remote i user-controlled sadrzaj ne moze da dosegne lokalni kod, tajne, fajlove, uredjaje, updater, installer ili druge naloge bez eksplicitne autorizacije.
7. Path, URL, deep-link, external-open, file import/export, archive i local-service granice su kanonikalizovane, scoped, autentifikovane i testirane.
8. Lokalni podaci imaju ownership, dozvole, semu/migraciju, backup/restore, corruption recovery, account izolaciju, retention i uninstall politiku.
9. Kriticni write-ovi i eksterni side effect-i imaju constraint-e, transakcije ili durable state tranzicije, concurrency kontrolu, idempotency i crash recovery.
10. Network klijenti i lokalni listener-i imaju TLS/peer trust, autentikaciju, timeout-e, ogranicen retry, cancellation, backpressure, redakciju i failure testove.
11. Native module-i, FFI, sidecar-i, codec-i, sistemski dependency-ji i WebView runtime-i su verifikovani na svakoj podrzanoj platformi/arhitekturi.
12. Sadrzaj paketa nema nenamerne tajne, debug povrsine, writable executable kod, nepodrzane binary fajlove ili neobjasnjene dodatke.
13. Svaki distribuirani artefakt je vezan za source, pregledan, hash-ovan, potpisan gde je potrebno, timestamp-ovan/notarizovan gde je primenljivo i verifikovan posle instalacije.
14. Install, repair, upgrade sa svakog podrzanog source-a, skipped-version update, prekinuti update, rollback/recovery i uninstall su testirani sa reprezentativnim podacima.
15. Update metadata, potpisi, custody kljuceva, channel politika, staged rollout, abort, downgrade, rollback, revocation i compromised-key response su dokazani.
16. Startup, odziv, memorija, CPU, GPU, disk, mreza, idle, long-run i failure-containment budzeti su izmereni na reprezentativnim sistemima.
17. Pristupacnost, lokalizacija, high DPI, vise ekrana, tastatura, screen reader, IME, dozvole i native dialog-i su verifikovani u packaged build-ovima.
18. Logovi, metrike, trace-ovi, crash-evi, simboli/source map-e, alert-i, privacy redakcija, diagnostic export i runbook-ovi podrzavaju dijagnostiku incidenta.
19. CI/CD odvaja nepoverljiv i privilegovan rad, promovise nepromenljive artefakte, stiti signing/publishing, zadrzava dokaze i vezba emergency release.
20. Svi P0/P1 nalazi su popravljeni ili imaju eksplicitan containment i recovery; P2/P3 imaju vlasnike, acceptance kriterijume i prioritete.
21. Komande, okruzenja, izlazi, skipped provere, evidence ceiling, izmenjeni fajlovi, testovi, hash-evi artefakta i eksterni izvori su zabelezeni.
22. Finalni zakljucak je `ready`, `ready-with-conditions` ili `not-ready`, sa tacnim blocker-ima i preostalim rizikom.

## 28. Definition of Done

1. Workspace i user/signing podaci su zasticeni; stanje repozitorijuma i audit granice su zabelezeni.
2. Svi relevantni source, generated, dependency, build, package, signing, installer, updater, store i runtime resursi su popisani.
3. Stvarne Electron/Tauri i embedded/runtime/tool verzije su verifikovane; podrska i kompatibilnost su proverene prema trenutnim primarnim izvorima.
4. Cist locked restore/build, relevantne staticke provere, testovi, generisanje paketa i pregled artefakta su zabelezeni sa stvarnim komandama i exit code-ovima.
5. Arhitektonska, process, window/webview, origin, privilege, IPC/command, local service, data i update mapa su kompletne.
6. Svaka materijalna tvrdnja ima status i nivo dokaza. Sumnje su odvojene od potvrdjenih nalaza.
7. Svaki P0/P1 ima dokaz, root cause, uticaj, containment, popravku, regression dokaz, release uticaj, rollback i vlasnika.
8. Primenljivi P2 nalazi imaju ciljanu sanaciju ili prioritizovan, testabilan plan. P3 rad se ne predstavlja kao produkcioni blocker bez razloga.
9. Electron security podesavanja ili Tauri capabilities su verifikovani u zapakovanoj aplikaciji pozitivnim i negativnim testovima.
10. Authentication, resource authorization, account/tenant izolacija, session cleanup, secret storage i privilegovane radnje su verifikovani.
11. Kriticni lokalni write-ovi, migracije, sinhronizacija i eksterni side effect-i su bezbedni pod duplicate, concurrent, interrupted i crash uslovima.
12. Fajlovi, URL-ovi, protokoli, import-i, export-i, arhive, download-i, external-open, lokalni listener-i, sidecar-i i uredjaji su ograniceni i testirani.
13. Build i package supply chain, SBOM/provenance, identitet artefakta, signing, notarizacija, custody kljuceva i opoziv su verifikovani.
14. Cista instalacija, upgrade matrica, repair, prekinuti update, rollback/recovery i uninstall su testirani ili jasno blokirani sa tacnim razlozima.
15. Performance i resource tvrdnje su zasnovane na merenju; pristupacnost i lokalizacija su testirane u packaged build-ovima.
16. Observability i incident artefakti mogu identifikovati tacnu verziju/kanal/platformu/proces i dijagnostikovati kritican otkaz bez izlaganja osetljivih podataka.
17. CI/CD gate-ovi, promocija artefakta, staged rollout, abort, emergency release, rollback i compromised-key procedure su dokumentovani i vezbani gde je potrebno.
18. Finalni diff je uzak, pregledan, bez nepovezanih izmena i ukljucuje potrebne testove i dokumentaciju.
19. Finalni izvestaj sadrzi tacne komande, dokaze, artefakte, hash-eve, izmene, testove, blocker-e, preostali rizik, vlasnike i autoritativne izvore.
20. Ako bilo koji primenljivi uslov nije zadovoljen, aplikacija nije potpuno production-ready i tacan blocking uslov je naveden.

## 29. Zabranjene precice

1. Ne proglasavaj uspeh zato sto se aplikacija pokrece u development rezimu, build-uje na jednoj masini, prolazi browser testove ili proizvodi installer.
2. Ne ukljucuj Node integration, ne iskljucuj context isolation/sandbox/web security, ne siri Tauri capability, ne dodeljuj default plugin permission niti izlaži genericki IPC/komande samo da bi feature proradio.
3. Ne validiraj samo u renderer-u/frontend-u. Privilegovane granice moraju nezavisno da validiraju i autorizuju.
4. Ne potiskuj TypeScript, Rust, compiler, linter, packaging, signing, notarization, installer, updater ili security upozorenja bez root-cause analize.
5. Ne dodaj `any`, unchecked cast-ove, `unwrap`, `expect`, sirok `unsafe`, prazne catch blokove, ignorisane promise/result vrednosti ili blanket suppression kao univerzalne popravke.
6. Ne koristi shell execution sa interpoliranim ulazom, proizvoljne external-open URL-ove, neogranicene filesystem scope-ove, writable executable putanje ili neautentifikovane localhost servise.
7. Ne iskljucuj TLS ili certificate provere, ne prihvataj sve origin-e, ne loguj tajne, ne cuvaj dugotrajne tokene u frontend storage-u i ne isporucuj privatne kljuceve.
8. Ne tretiraj ASAR, obfuscation, minification, Rust, code signing, sandbox ili capabilities kao kompletnu security granicu sami za sebe.
9. Ne pokreci automatski destruktivne migracije, ne resetuj korumpirane podatke tiho, ne uklanjaj korisnicke podatke bez politike i ne instaliraj update tokom nebezbednog kriticnog rada.
10. Ne objavljuj promenljive artefakte, ne rebuild-uj posebno po promotion fazi bez objasnjenja, ne potpisuj nepregledane bajtove i ne dozvoli nepoverljivom CI-ju pristup release kredencijalima.
11. Ne povecavaj memory, queue, timeout, retry, process ili file-size limite bez capacity i abuse analize.
12. Ne migriraj Electron u Tauri, Tauri u Electron, ne prepisuj frontend, ne menjaj bazu niti installer tehnologiju samo zbog popularnosti ili tvrdnji o velicini binarnog fajla.
13. Ne brisi tudje izmene, ne formatiraj masovno repozitorijum, ne skrivaj nepovezane diff-ove, ne preskaci neuspele testove i ne slabi testove da pipeline prodje.
14. Ne tvrdi cross-platform podrsku bez packaged install/runtime/update dokaza na podrzanoj platform matrici.
15. Ne nazivaj aplikaciju savrsenom, potpuno bezbednom ili production-ready bez zadovoljavanja primenljivih evidence i recovery zahteva.

## 30. Obavezni zavrsni izvestaj

1. Executive summary i zakljucak: `ready`, `ready-with-conditions` ili `not-ready`, sa evidence ceiling-om.
2. Application i release kontekst: framework, verzije, platforme, arhitekture, kanali, kriticni tokovi, podaci, identiteti i ogranicenja.
3. Source-to-installed-runtime identity lanac sa hash-evima artefakta i nerazresenim prekidima.
4. Arhitektonska, process, window/webview, origin, privilege, IPC/command, local service, data, installer i update mapa.
5. Tabela verzija i podrske: project, resolved, packaged/runtime, trenutni stable, support status, kompatibilnost, akcija, izvor.
6. Tabela nalaza: `ID | P0-P3 | dokaz | framework/oblast | platforma | fajl/simbol | uzrok | uticaj | popravka | test | rollback | status`.
7. Implementirane izmene: tacni fajlovi, konfiguracija, dependency-ji, capabilities/permissions, signing/update/installer izmene, migracije i regression rizik.
8. Stvarne komande: komanda, direktorijum, environment/tool verzije, platforma, exit code, sazetak izlaza, generisani artefakti i zakljucak.
9. Build/test/package matrica, adversarial scenariji, performance/resource merenja, accessibility rezultati i blokirane provere.
10. Verifikacija artefakta/paketa/signing-a/notarizacije/prodavnice/update-a sa tacnim hash-evima, identitetima, timestamp-ima i kanalom.
11. Rezultati install, update, migration, rollback, recovery, uninstall i incident-readiness provera.
12. Security i privacy sazetak: renderer/webview izolacija, IPC/command autorizacija, fajlovi/URL-ovi, lokalni servisi, tajne, telemetrija, supply chain i preostali rizik.
13. Operational readiness: SLO/budzeti, telemetrija, alert-i, runbook-ovi, staged rollout, abort, emergency release, kompromitacija kljuca, backup/restore i vlasnici.
14. Preostali rad grupisan kao `blocks production`, `needed soon`, `planned refactor` i `optional`, sa vlasnikom, dependency-jem, acceptance kriterijumom i ciljnim datumom.
15. Eksterni izvori konsultovani: naslov, URL, verzija/status, datum pristupa i odluka koju je informisao.

## 31. Redosled rada

1. Zastiti workspace, korisnicke podatke, signing materijal i release kanale.
2. Popisi repozitorijum, generisane fajlove, dependency-je, toolchain-e i vlasnistvo.
3. Utvrdi source-to-installed-runtime identitet i trenutni support baseline.
4. Pokreni cist restore/build/static/test baseline bez destruktivnih izmena.
5. Mapiraj arhitekturu, procese, prozore/webview-e, origin-e, privilegije, IPC/komande, podatke i OS integracije.
6. Audituj Electron-specific ili Tauri-specific security i lifecycle kontrole.
7. Audituj fajlove, podatke, mrezu, lokalne servise, native kod, uredjaje i eksterne ulaze.
8. Pregledaj stvarne pakete, potpise, installer-e, prodavnice, update feed-ove i instalirano stanje.
9. Reprodukuj i klasifikuj nalaze sa root cause-om i dokazom.
10. Implementiraj ovlascene minimalne popravke i fokusirane regression testove.
11. Izvrsi packaged platform, adversarial, performance, accessibility, install, update, rollback i recovery verifikaciju.
12. Popuni evidence matrice, release odluku, roadmap i zavrsni izvestaj.

## 32. Registar primarnih izvora

| Izvor | URL | Upotreba |
| --- | --- | --- |
| Electron Releases | https://releases.electronjs.org/ | Trenutne stable/prerelease i ugradjene Chromium/Node verzije. |
| Electron Security | https://www.electronjs.org/docs/latest/tutorial/security | Zvanicna security checklist-a i smernice za renderer izolaciju. |
| Electron Breaking Changes | https://www.electronjs.org/docs/latest/breaking-changes | Kompatibilnost major upgrade-a. |
| Electron Fuses | https://www.electronjs.org/docs/latest/tutorial/fuses | Ojacavanje u vreme pakovanja i fuse verifikacija. |
| Electron ASAR Integrity | https://www.electronjs.org/docs/latest/tutorial/asar-integrity | Zahtevi ugradjenog ASAR integriteta. |
| Electron Updating Applications | https://www.electronjs.org/docs/latest/tutorial/updates | Updater arhitektura i razlike platformi. |
| Electron autoUpdater API | https://www.electronjs.org/docs/latest/api/auto-updater | Runtime updater semantika i event-i. |
| Electron Code Signing | https://www.electronjs.org/docs/latest/tutorial/code-signing | Platform signing smernice. |
| Electron Distribution Overview | https://www.electronjs.org/docs/latest/tutorial/distribution-overview | Pregled pakovanja, signing-a i update-a. |
| Tauri Ecosystem Releases | https://v2.tauri.app/release/ | Core, CLI, API, runtime, Wry, Tao, bundler i plugin izdanja. |
| Tauri Capabilities | https://v2.tauri.app/security/capabilities/ | Window/webview capability granice i merge ponasanje. |
| Tauri Permissions | https://v2.tauri.app/security/permissions/ | Allow, deny i scope definicije. |
| Tauri Runtime Authority | https://v2.tauri.app/security/runtime-authority/ | Runtime enforcement origin-a, capability-ja, permission-a i scope-a. |
| Tauri Command Scopes | https://v2.tauri.app/security/scope/ | Odgovornosti sprovođenja application-defined scope-a. |
| Tauri Updater | https://v2.tauri.app/plugin/updater/ | Potpisane update metadata, platforme, endpoint-i i dozvole. |
| Tauri Distribution | https://v2.tauri.app/distribute/ | Platform package formati, prodavnice i signing. |
| Rust Releases | https://blog.rust-lang.org/releases/latest/ | Trenutni stable Rust i release status. |
| Node.js Releases | https://nodejs.org/en/about/previous-releases | Node.js lifecycle gde Electron tooling ili sidecar-i koriste Node. |
| Apple Developer Documentation | https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution | macOS notarizacija i platform trust. |
| Microsoft Code Signing Documentation | https://learn.microsoft.com/windows-hardware/drivers/dashboard/code-signing-reqs | Windows signing i publisher trust kontekst. |
