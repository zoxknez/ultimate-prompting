## 4. Model dokaza i disciplina nalaza

### 4.1 Nivoi dokaza

| Nivo | Značenje | Primeri |
| --- | --- | --- |
| E0 | Samo tvrdnja ili pretpostavka. | README tvrdnja, komentar, ticket, nedokumentovano sećanje. |
| E1 | Statički source ili konfiguracioni dokaz. | Dart kod, pubspec, native manifest, CI fajl, entitlement. |
| E2 | Razrešen ili generisan dokaz. | pubspec.lock, dependency graf, generated registrant, build konfiguracija, compiled metadata. |
| E3 | Izvršen build, test ili artifact dokaz. | Analyzer izlaz, testovi, release build, pregled potpisanog artefakta, analiza veličine. |
| E4 | Instaliran device, browser ili kontrolisani environment dokaz. | Pokretanje na stvarnom uređaju, browser matrica, migracija, update test, profiler trace. |
| E5 | Production ili production-equivalent operativni dokaz. | Telemetrija, staged rollout, restore proba, incident replay, SLO trend. |

### 4.2 Registar nalaza

Svaki materijalni nalaz mora da sadrži sva polja ispod. Nedostajuća polja smanjuju pouzdanost i mogu blokirati odobrenje remedijacije.

| Polje | Obavezan sadržaj |
| --- | --- |
| ID i severity | Stabilan identifikator i P0-P3 nivo. |
| Naslov i pogođeni scope | Platforma, flavor, modul, ruta, funkcija, nalog, tenant, verzija i okruženje. |
| Status i nivo dokaza | Status tvrdnje plus E0-E5 nivo. |
| Dokaz i reprodukcija | Fajlovi, simboli, komande, artifact ID-jevi, device/browser matrica, telemetrija i deterministički koraci. |
| Root cause | Osnovni tehnički i procesni uzrok, ne samo simptom. |
| Uticaj i exploitability | Uticaj na korisnika, podatke, bezbednost, dostupnost, trošak, store, usklađenost i oporavak. |
| Remedijacija i alternative | Minimalna bezbedna popravka, dugoročna opcija, odbačene prečice i vlasništvo. |
| Provera i rollback | Regresioni testovi, negativni testovi, platformska matrica, rollout gate-ovi, rollback trigger i oporavak. |

### 4.3 Severity model

- `P0`: aktivna kompromitacija, kompromitacija signing/update lanca, sistemski neovlašćen pristup, destruktivna korupcija, neoporavljiv gubitak podataka ili kritičan prekid koji zahteva trenutno ograničavanje.
- `P1`: kredibilan ozbiljan bezbednosni, privacy, authorization, payment, migration, release, availability ili recovery problem sa velikim uticajem na korisnike ili poslovanje.
- `P2`: materijalan problem ispravnosti, performansi, accessibility-ja, kompatibilnosti, održavanja, observability-ja ili operacija koji treba planirati.
- `P3`: niskorizično unapređenje hardening-a, čišćenja, dokumentacije, dubine testova, developer experience-a ili optimizacije.
- Severity mora da odražava dokazani uticaj, dostupnost, preduslove, uočljivost, oporavak i izloženost, ne strah ili formulaciju skenera.

