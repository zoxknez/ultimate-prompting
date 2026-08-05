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

