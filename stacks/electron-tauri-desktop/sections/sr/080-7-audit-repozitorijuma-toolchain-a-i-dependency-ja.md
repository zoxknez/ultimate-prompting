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

