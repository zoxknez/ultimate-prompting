## Faza 3 - Composer graf, autoloading, plugin-ovi, skripte i supply chain

### Cilj

Dokaži determinističan dependency graf usklađen sa politikom i razumi sav kod izvršen tokom instalacije i autoload-a.

### Zahtevi audita

- Validiraj `composer.json` i lock konzistentnost, PHP i extension ograničenja, stability flagove, platform config, repozitorijume, conflict, replace, provide i branch alias-e.
- Popiši Packagist, privatne Composer repozitorijume, VCS, path, artifact i custom repository trust boundary-je.
- Audituj `allow-plugins`, plugin-ove, installer-e, skripte, hook-ove i kod izvršen tokom install, update, dump-autoload ili package discovery koraka.
- Proveri dist arhive, source fallback ponašanje, kredencijale, repository TLS, package provenance, napuštene pakete i reachable advisories.
- Pregledaj PSR-4, classmap, files autoload, authoritative classmap, APCu autoloader, optimized autoload, duplicate class-e i razlike u case-sensitivity-ju.
- Reprodukuj frozen install iz čistog checkout-a i otkrij network, credential, plugin, platform ili generated-file drift.

### Obavezni dokazi

- Razrešeni package graf, poreklo repozitorijuma, checksums, licence, advisories i ownership paketa.
- Allowlist plugin-ova i install skripti sa svrhom, privilegijom, verzijom i putanjom uklanjanja.
- Rezultat čistog frozen install-a i SBOM ili ekvivalentni inventar povezan sa artifact digest-om.

### Kriterijumi prihvatanja

- Lockfile je autoritativan, reproducibilan, pregledan i nije tiho izmenjen tokom build-a ili deployment-a.
- Nijedan nepregledan plugin, skripta, repozitorijum, paket ili source fallback ne može da se izvrši u trusted build-u.

