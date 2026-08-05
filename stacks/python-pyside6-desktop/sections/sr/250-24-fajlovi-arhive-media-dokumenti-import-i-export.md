## 24. Fajlovi, arhive, media, dokumenti, import i export

### 24.1 Obim audita

1. Inventariši svaki prihvaćen i proizveden format fajla, parser, codec, arhivu, sliku, media, PDF, office, CSV, bazu, projekat, backup i export putanju.
2. Zabeleži trust izvor, maksimalnu veličinu, expansion ratio, dubinu rekurzije, path pravila, privremeno skladište, validaciju, sanitizaciju i cleanup.
3. Pregledaj path traversal, zip slip, symlink/hardlink zloupotrebu, alternate stream-ove, special fajlove, device putanje, normalizaciju imena, zabunu ekstenzije i overwrite ponašanje.
4. Proceni limite memorije/CPU-a parser-a, decompression bomb-e, malformed metadata, spoljne reference, makroe, formule, embedded sadržaj i ranjivosti native codec-a.
5. Validiraj atomic export, partial izlaz, pun disk, cancellation, postojeće fajlove, dozvole, network share-ove, removable medije i konkurentni pristup.
6. Razlikuj preview, validaciju, import, konverziju, izvršavanje, external-open i trusted-project semantiku.

### 24.2 Obavezna verifikacija

1. Koristi malicious corpus i fuzz-uj reprezentativne parser-e u izolovanim okruženjima; uključi oversized, recursive, truncated, polyglot i path-manipulating uzorke.
2. Testiraj cancellation i crash import/export-a na svakoj write granici; verifikuj da ne ostaje lažno uspešan izlaz ili korumpiran original.
3. Potvrdi da privremeni fajlovi koriste bezbedne lokacije, restriktivne dozvole, nepredvidiva imena, atomic zamenu i deterministički cleanup.
4. Verifikuj da se spoljni alati i codec-i razrešavaju sa trusted potpisanih lokacija i dobijaju bezbedno quoted argumente i ograničene resurse.
5. Obezbedi da korisnička upozorenja opisuju stvarni rizik i ne postanu jedina kontrola za executable ili active sadržaj.

