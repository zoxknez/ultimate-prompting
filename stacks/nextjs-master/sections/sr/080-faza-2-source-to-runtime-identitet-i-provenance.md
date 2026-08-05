## Faza 2 - Source-to-runtime identitet i provenance

Dokazi identitet koda, zavisnosti, generisanog izlaza, artefakta, deployment-a, runtime konfiguracije, scheme i browser-visible release-a.

### Zahtevi audita

- Povezi repozitorijum, commit, dirty state, lockfile digest, toolchain, klasu okruzenja i build invokaciju.
- Zabelezi resolved pakete, patch-eve, override-e, native module, lifecycle skripte, generisane asset-e i build-time mrezni pristup.
- Identifikuj build izlaz, route manifest, function bundle-ove, static asset-e, image digest, source map-e i deployment identifikator.
- Vezi deployment reviziju za logove, trace-ove, error-e, bezbednu dijagnostiku i browser-visible build metadata.
- Zabelezi efektivni config, flag-ove, region, runtime, schema verziju, cache namespace i deployment ID.
- Odbaci mutable tag-ove, rebuild-per-environment promociju ili tvrdnje nevezane za immutable identifikatore.

### Obavezni dokazi

- Tabela korelacije commit-lockfile-artefakt-deployment-runtime.
- Build manifest sa toolchain-om, dependency graph-om, generisanim ulazima i output digest-ima.
- Runtime release metadata u logovima, trace-ovima, error-ima i bezbednim response-ima.
- Dokaz da se isti immutable artefakt promovise kroz okruzenja.

### Obavezni failure i acceptance testovi

- Detektuj namerno nepodudaran deployment identifikator pre nego sto dobije saobracaj.
- Drzi stari tab otvoren kroz deployment i proveri asset/server kompatibilnost.
- Reprodukuj release iz cistog okruzenja i uporedi autoritativne digest-e.
- Povezi runtime error sa tacnim commit-om, artefaktom, config-om, schemom i flag stanjem.

