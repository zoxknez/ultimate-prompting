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

