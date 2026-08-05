## 9. Audit zavisnosti i supply chain-a

Audituj razrešen graf i build ponašanje, ne samo nazive paketa.

- Pregledaj direktne, tranzitivne, dev, native, plugin, tool i build-runner zavisnosti sa izvorom, verzijom, licencom, maintainer-om, ritmom izdanja i platformskom podrškom.
- Pregledaj path, git, hosted, SDK, override, lokalne fork-ove, neobjavljene, prerelease i discontinued zavisnosti.
- Proveri disciplinu lock fajla za aplikacije i namernu compatibility politiku za reusable pakete.
- Pregledaj `build.yaml`, builder-e, generatore, skripte, hook-ove, code-mod alate, native build skripte i package setup action-e kao izvršni supply-chain kod.
- Traži dependency confusion, typosquatting, rizik kompromitovanog maintainer-a, napuštene plugin-e, prekomerne native privilegije, dinamička preuzimanja i binarne blob-ove.
- Poveži advisory-je sa stvarno razrešenim verzijama, dostupnim code path-ovima, runtime konfiguracijom, platformom i mitigacijama pre dodeljivanja severity-ja.
- Generiši ili proveri SBOM i provenance za Dart pakete, native biblioteke, embedded framework-e, asset-e i release artefakte.
- Definiši vlasništvo nad update-om, deprecation-om, fork-om, zamenom, odgovorom na ranjivost i hitnim opozivom kritičnih zavisnosti.
- Ne nadograđuj pakete masovno; nadograđuj po compatibility klasteru sa contract testovima, migracionim dokazima, poređenjem performansi i rollback-om.

