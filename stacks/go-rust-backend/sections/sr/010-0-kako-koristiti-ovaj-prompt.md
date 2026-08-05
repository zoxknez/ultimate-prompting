## 0. Kako koristiti ovaj prompt

### 0.1 Obavezni ulazi

| Polje | Vrednost |
| --- | --- |
| Repozitorijum, arhiva, moduli, workspace-i i relevantne putanje | `[PUTANJE / URL-OVI]` |
| Poslovna svrha, kritični tokovi i invarijante | `[TOKOVI / INVARIJANTE]` |
| Tehnološka staza i izvršni artefakti | `[GO / RUST / MIXED / BINARIES]` |
| Target-i, arhitekture, libc i operativni sistemi | `[TARGET MATRICA]` |
| Protokoli, klijenti, peer-ovi i obećanja kompatibilnosti | `[HTTP / GRPC / TCP / UDP / QUIC / DRUGO]` |
| Skladišta podataka, redovi, keš, fajlovi i šeme | `[SISTEMI / VLASNICI]` |
| Identitet, tenant, autorizacija i privilegovane operacije | `[MODEL / POLITIKE]` |
| Saobraćaj, konkurentnost, latencija, kapacitet i SLO ciljevi | `[LOAD / BUDŽETI]` |
| Build tag-ovi, Cargo feature-i, profili i release varijante | `[MATRICA]` |
| FFI, cgo, native biblioteke, kernel-i, uređaji ili WASM host-ovi | `[GRANICE]` |
| Deploy, artifact registry, potpisivanje i rollout | `[PLATFORME / KANALI]` |
| Production pristup, ovlašćenje za izmene i režim rada | `[PRISTUP / ODOBRAVAOCI / REŽIM]` |

### 0.2 Nedostajuće informacije i granica dokaza

1. Nastavi bezbedno otkrivanje kada ulazi nisu potpuni; ne blokiraj ceo audit.
2. Zaključuj samo iz stanja repozitorijuma, lock fajlova, razrešenih grafova, generisanog izlaza, build metapodataka, artefakata, runtime dokaza, telemetrije, ograničenja baze i autoritativne dokumentacije.
3. Označi svaku nerešenu materijalnu tvrdnju kao `UNVERIFIED` i navedi tačan pristup, workload, target, fixture, kredencijal, odobrenje ili okruženje potrebno za razrešenje.
4. Ne izdaji bezuslovnu production-ready ocenu kada release, target, dependency, data, failure, deployment ili recovery dokazi nisu dostupni.

