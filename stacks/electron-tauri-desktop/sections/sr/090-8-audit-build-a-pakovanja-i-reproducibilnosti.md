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

