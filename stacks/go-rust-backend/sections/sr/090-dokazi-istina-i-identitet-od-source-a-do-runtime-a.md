## Dokazi, istina i identitet od source-a do runtime-a

### Nivoi dokaza

| Nivo | Značenje | Primeri |
| --- | --- | --- |
| `E0` | Samo tvrdnja; nema proverljivog dokaza. | README, ticket, usmeno očekivanje. |
| `E1` | Statički dokaz iz repozitorijuma ili konfiguracije. | Source, manifest, module fajl, lock fajl. |
| `E2` | Dokaz iz razrešenog build-a ili generisanog izlaza. | Dependency graf, generisani kod, linker mapa, build metapodaci. |
| `E3` | Izvršen test, analyzer, benchmark ili kontrolisana reprodukcija. | Exit code, logovi, race izveštaj, Miri nalaz, packet trace. |
| `E4` | Dokaz iz release-like artefakta i ciljnog okruženja. | Hash binarnog fajla, potpis, container digest, target smoke, load ili failover run. |
| `E5` | Posmatrano production ponašanje ili dokazan oporavak. | Telemetrija vezana za reviziju, canary rezultat, restore proba, incident dokaz. |

- Koristi najjači dostupan dokaz, ali nikada ne podiži zaključak iznad stvarno dobijenog nivoa dokaza.
- Za svaku izvršenu proveru zabeleži komandu, radni direktorijum, okruženje, toolchain, target, tag-ove ili feature-e, fixture-e, exit code, trajanje i materijalni izlaz.
- Razdvoji `CONFIRMED`, `PARTIALLY_CONFIRMED`, `UNVERIFIED`, `NOT_APPLICABLE` i `REJECTED`; ne koristi neodređene formulacije green, izgleda dobro, verovatno ili bezbedno.

### Lanac identiteta od source-a do runtime-a

- Zabeleži URL repozitorijuma, commit, branch ili tag, dirty stanje, submodule-e, vendored kod, generisani kod, patch-eve i untracked ulaze.
- Razreši tačne Go i Rust toolchain-e izabrane lokalno, u CI-ju, builder-ima, container-ima i release automatizaciji; zabeleži automatsko preuzimanje toolchain-a ili override ponašanje.
- Sačuvaj module/workspace grafove, checksum-e, lock fajlove, replace ili patch direktive, build skripte, generatore koda, proc macro-e, C toolchain-e, sistemske biblioteke i linker ulaze.
- Zabeleži build tag-ove, promenljive okruženja, `GOOS`, `GOARCH`, `CGO_ENABLED`, target triple-ove, Cargo feature-e, profile-e, `RUSTFLAGS`, linker flag-ove, LTO, panic strategiju i kontrole reproduktivnosti.
- Hash-uj i identifikuj binarne fajlove, biblioteke, debug simbole, source map-e, SBOM-ove, potpise, provenance, container image-e, package manifeste i deployment revizije.
- Proveri runtime verziju, build commit, skup feature-a ili tag-ova, izvor konfiguracije, učitane shared biblioteke, kernel i libc pretpostavke, arhitekturu, endpoint peer-ove i kompatibilnost šeme.
- Uskladi source, artifact, registry, deployment, process, telemetriju, migraciju baze i recovery identitete pre release ocene.
- Otkrij promenljive tag-ove, rebuild pod istom verzijom, zastareo generisani kod, pogrešne simbole, pogrešan image, pogrešnu konfiguraciju, delimičan rollout, mešovitu šemu i koegzistenciju starog i novog binarnog fajla.

### Ugovor kvaliteta nalaza

| Obavezno polje | Zahtev |
| --- | --- |
| Identitet | Stabilan ID nalaza, jezik, podsistem, vlasnik i pogođeni artefakt ili deployment. |
| Dokaz | Fajl i simbol, komanda, target, tag-ovi/feature-i, preduslovi podataka ili saobraćaja, artifact ID i E0-E5 nivo. |
| Uzrok | Root cause i prekršena invarijanta, ne samo simptom ili tekst skenera. |
| Uticaj | Posledice po ispravnost, bezbednost, dostupnost, podatke, latenciju, trošak, kompatibilnost i oporavak. |
| Popravka | Najmanja bezbedna popravka, alternative, odbačene prečice, vlasnik, migracija i rollout ograničenja. |
| Provera | Regresioni, negativni, race ili memory check, target matrica, load/failure scenario, rollout gate i rollback trigger. |

