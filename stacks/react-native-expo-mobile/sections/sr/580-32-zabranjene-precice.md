## 32. Zabranjene precice
- Ne tvrdi production spremnost samo na osnovu Expo Go, Metro, simulatora, emulatora, debug build-a, typecheck-a, lint-a, Expo Doctor-a ili zelenog cloud build-a.
- Ne brisi lock fajl, native projekat, generisani fajl, cache, lokalne podatke, signing zapis, simbole ili forenzicki dokaz da bi build prosao.
- Ne pokreci sirok dependency upgrade, automatsku fix komandu, clean prebuild, pod update, promenu Gradle verzije ili framework migraciju bez pregleda i rollback-a.
- Ne objavljuj OTA, ne salji u store, ne promovisi track, ne menjaj kanal, ne rotiraj kljuc, ne opozivaj kredencijal i ne menjaj production podatke bez izricitog odobrenja.
- Ne potiskuj crash, ANR, warning, permission gresku, migration failure, update failure ili neuspesan test umesto popravke osnovnog uzroka.
- Ne tretiraj client-side validaciju, skriven UI, biometriju, root detekciju, certificate pinning ili TypeScript tipove kao potpunu autorizaciju.
- Ne koristi mutable tag, nedokumentovan lokalni patch, nepregledan config plugin, nepotpisan update ili neverifikovan artefakt za production.
- Ne proglasavaj rollback spremnim kada ga sprecavaju podaci, native runtime, backend ugovor, lokalna schema ili update kompatibilnost.
- Ne generalizuj Android dokaz na Apple, Apple dokaz na Android, jedan uredjaj na sve uredjaje ili jedan workflow na sve workflow-e.
- Ne izmisljaj output komande, ponasanje uredjaja, store stanje, telemetriju, potpis, kredencijal, rollout status, restore rezultat ili sigurnost.

