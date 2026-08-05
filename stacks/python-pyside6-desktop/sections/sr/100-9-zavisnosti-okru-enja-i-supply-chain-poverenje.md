## 9. Zavisnosti, okruženja i supply-chain poverenje

### 9.1 Obim audita

1. Inventariši `pyproject.toml`, requirements fajlove, lock fajlove, constraint-e, editable install-e, VCS/path zavisnosti, privatne index-e, wheelhouse-e i vendor kod.
2. Utvrdi autoritativni resolver i environment workflow: pip, uv, Poetry, PDM, pip-tools, Conda, Hatch, legacy Rye, sistemski paketi ili custom tooling.
3. Pregledaj build backend-e, PEP 517 izolaciju, dinamičke metadata, setup hook-ove, package-data pravila, namespace pakete, entry point-e i executable skripte.
4. Identifikuj source distribucije, kompajlirane wheel pakete, post-install korake, binary download-e, code generator-e i pakete koji izvršavaju kod tokom build-a ili import-a.
5. Proveri dependency confusion, typosquatting, index prioritet, mutable VCS reference, kompromitovane maintainere, napuštene pakete, licencne obaveze i security advisories.
6. Razdvoji runtime zavisnosti, packaging-only zavisnosti, development alate, test alate, opcione extras, platform marker-e i plugin ekosisteme.

### 9.2 Obavezna verifikacija

1. Razreši iz čistog okruženja koristeći commitovan lock/constraint i uporedi hash-eve, verzije, marker-e, wheel tag-ove i tranzitivne grafove kroz CI i release.
2. Preferiraj verifikovane wheel pakete ili reproduktivno izgrađene artefakte; dokumentuj svaki source build, native toolchain, spoljni download i trusted ključ.
3. Generiši i pregledaj SBOM, licencni inventar, vulnerability izveštaj, provenance i dokaze potpisa/hash-a paketa za release graph.
4. Testiraj offline ili controlled-index instalaciju gde je potrebno i dokaži da neočekivani javni paket ne može preuzeti privatno ime.
5. Zaustavi release zbog nerazrešenih kritičnih advisories, nepregledanih executable hook-ova, nepodržanih binary wheel-ova ili nereproduktivnog dependency resolution-a.

