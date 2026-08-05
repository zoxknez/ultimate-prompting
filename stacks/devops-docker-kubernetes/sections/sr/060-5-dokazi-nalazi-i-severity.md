## 5. Dokazi, nalazi i severity

### 5.1 Sema nalaza

```text
ID
severity: P0 | P1 | P2 | P3
confidence: high | medium | low
evidence_status: CONFIRMED | PARTIALLY_CONFIRMED | UNVERIFIED
domen i pogođeni resursi
nalaz i prekrsena invarijanta
dokaz sa izvorom, komandom, opsegom, vremenom i artefaktom
put otkaza, zloupotrebe ili eksploatacije
poslovni, bezbednosni, availability, data i cost uticaj
blast radius i preduslovi
hitno ogranicavanje ako je potrebno
root cause i doprinoseci uslovi
preporucena popravka i bezbednije alternative
vlasnik, zavisnosti i granica odobrenja
verifikacija i regresioni testovi
rollout, posmatranje i stop uslovi
rollback ili compensating action
rezidualni rizik i odluka o prihvatanju
```

### 5.2 Severity model

| Severity | Znacenje | Tipicni primeri |
| --- | --- | --- |
| `P0` | Aktivan ili neposredan katastrofalan uticaj koji zahteva hitnu koordinisanu akciju. | Kompromitovani produkcioni kredencijali, nekontrolisan destruktivni pristup, aktivna eksfiltracija, neoporavljiv gubitak podataka, potpuni kriticni outage bez bezbednog oporavka. |
| `P1` | Visokoverovatan ili visokouticajan produkcioni rizik. | Cluster-admin CI putanja, javni privileged workload, nevalidan restore dokaz, kriticni servis u jednom regionu bez prihvacenog rizika, eksploatabilan admission bypass. |
| `P2` | Materijalna slabost sa ogranicenim uticajem ili preduslovima. | Presiroke namespace dozvole, nedostajuci disruption test, bucni alarmi, slabo resource podesavanje, drift bez neposrednog puta eksploatacije. |
| `P3` | Niskorizicno hardening, maintainability, evidence ili efficiency pitanje. | Drift dokumentacije, nekriticna mutabilnost taga, nedostajuci ownership metadata, mali nepotreban idle trosak. |

Severity se zasniva na realnom uticaju, verovatnoci, izlozenosti, blast radius-u, oporavljivosti, detektabilnosti i pouzdanosti dokaza. Ne zasniva se samo na oznaci skenera.

### 5.3 Hijerarhija dokaza

1. Uocen korisnicki uticaj, kontrolisan test otkaza ili uspesan izolovani restore sa zabelezenim rezultatima.
2. Live runtime, cloud-provider, cluster, identity, network, storage i telemetrijski dokaz iz autorizovanog opsega.
3. Potvrđen identitet artefakta, potpis, provenance, SBOM, digest, deployment revision i istorija kontrolera.
4. Renderovana konfiguracija, policy evaluacija, infrastructure plan, staticka analiza, testovi i reproduktivan lokalni dokaz.
5. Namera u repozitorijumu, dijagrami, tiketi, komentari i intervjui.
6. Zakljucivanje bez direktne verifikacije.

