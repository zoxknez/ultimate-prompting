## 6. Source-to-installed-runtime identitet

### 6.1 Obim audita

1. Inventariši korene repozitorijuma, submodule-e, generisane direktorijume, build izlaze, vendor foldere, installer projekte, update metadata, skripte i vlasništvo.
2. Zabeleži commit, dirty stanje, branch/tag, hash source arhive, build host, CI run, environment lock i svaki spoljni ulaz koji može promeniti isporučene bajtove.
3. Razlikuj developer interpreter, test interpreter, build interpreter, packaging interpreter, embedded interpreter, helper interpreter i sistemski Python.
4. Mapiraj source module na generisani kod, bytecode, extension module, resurse, Qt plugin-e, executable, installer, update paket i instalirane fajlove.
5. Zabeleži hash-eve executable-a, paketa, installer-a, manifest-a, SBOM-a, potpisa, timestamp-a i update metadata.
6. Poveži instalirani proces, učitane module, Qt biblioteke, plugin putanje, konfiguraciju, schema-u, feature flag-ove i telemetry release identitet sa nameravanim artefaktom.

### 6.2 Obavezna verifikacija

1. Izvrši clean-environment resolve i build; uporedi dependency, generated-code, resource i artifact manifest sa CI i release zapisima.
2. Pregledaj zapakovane i instalirane fajlove, import poreklo, `sys.executable`, `sys.path`, `sys.prefix`, Qt library putanje, plugin putanje i učitane native module.
3. Verifikuj da nijedna writable search putanja, trenutni direktorijum, korisnička plugin putanja ili stari fajl ne mogu zaseniti pouzdane Python ili Qt komponente.
4. Pokreni instaliranu aplikaciju na čistoj mašini ili VM-u i zabeleži tačan binary, command line, okruženje, working directory, biblioteke i release identifikatore.
5. Testiraj update i rollback identitet tako da prijavljena verzija, kod, data schema, resursi i telemetrija ne mogu tiho da se raziđu.

