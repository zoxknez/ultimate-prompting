## 4. Model dokaza i disciplina nalaza

### 4.1 Nivoi dokaza

| Nivo | Znacenje | Primeri | Dozvoljen zakljucak |
| --- | --- | --- | --- |
| E0 | Samo tvrdnja ili dokumentacija | README, issue, dijagram, roadmap, izjava korisnika | Samo kontekst; nikada dovoljno za produkcioni zakljucak. |
| E1 | Staticki source dokaz | Kod, konfiguracija, manifesti, capability fajlovi, entitlement-i | Pokazuje nameru i moguce ponasanje, ne razreseno ili instalirano ponasanje. |
| E2 | Razreseni build dokaz | Lock fajlovi, dependency graf, compiler izlaz, generisana konfiguracija | Pokazuje sta je razreseno i izgradjeno u odredjenom okruzenju. |
| E3 | Dokaz zapakovanog artefakta | Sadrzaj arhive, binary metadata, fuses, dozvole, potpisi, SBOM | Pokazuje stvarni release kandidat pre instalacije. |
| E4 | Instalirani/runtime dokaz | Instalirani fajlovi, process tree, runtime logovi, IPC ponasanje, OS integracija, performanse | Pokazuje ponasanje na odredjenoj platformi, arhitekturi, profilu i version putu. |
| E5 | Operativni/recovery dokaz | Stvarni update rollout, rollback, restore, rotacija kljuceva, telemetrija, incident vezba | Potreban za jake tvrdnje o operacijama, oporavku i production readiness-u. |

### 4.2 Obavezni registar nalaza

```text
ID:
Naslov:
Ozbiljnost: P0 / P1 / P2 / P3
Status dokaza: CONFIRMED / PARTIALLY_CONFIRMED / UNVERIFIED
Framework: ELECTRON / TAURI / SHARED / OTHER
Oblast:
Pogodjena platforma i arhitektura:
Pogodjena verzija i release kanal:
Pogodjeni fajlovi i simboli:
Pogodjeni prozor, webview, proces, komanda, IPC kanal, capability, plugin, installer ili update put:
Okruzenje:
Nivo dokaza: E0 / E1 / E2 / E3 / E4 / E5
Dokaz:
Komanda, test, pregled paketa ili runtime snimak:
Reprodukcija:
Root cause:
Preduslovi exploita ili otkaza:
Uticaj na korisnika i poslovanje:
Security, privacy, data i operativni uticaj:
Verovatnoca:
Predlozena popravka:
Implementirana popravka:
Regression test:
Release i migration uticaj:
Rollback ili oporavak:
Preostali rizik:
Vlasnik:
Status:
```

### 4.3 Smernice za ozbiljnost

1. `P0`: aktivna kompromitacija, proizvoljno lokalno izvrsavanje koda kroz nepoverljiv sadrzaj, kompromitovan signing/update put, destruktivan gubitak podataka izmedju korisnika, exfiltration kredencijala ili produkciono release stanje bez oporavka.
2. `P1`: dostizna eskalacija privilegija, authorization bypass, nebezbedno updater ili installer ponasanje, teska korupcija podataka, siroko rasprostranjen crash/startup otkaz, nepodrzan security-critical runtime ili odsustvo odrzivog rollback-a za kriticno izdanje.
3. `P2`: znacajna slabost pouzdanosti, privatnosti, performansi, pristupacnosti, odrzavanja ili defense-in-depth-a sa ogranicenim uticajem ili dodatnim preduslovima.
4. `P3`: niskorizicno ojacavanje, unapredjenje developer experience-a, dokumentacioni jaz, ciscenje ili opciona modernizacija.
5. Ozbiljnost zasnivaj na dokazanom uticaju, dostiznosti, verovatnoci, blast radius-u, mogucnosti detekcije i tezini oporavka. Ne naduvavaj ozbiljnost samo na osnovu kljucnih reci.

