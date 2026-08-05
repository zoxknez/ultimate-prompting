## 42. Obavezni finalni izveštaj

1. Executive summary i zaključak: `READY`, `READY_WITH_CONDITIONS`, `NOT_READY` ili `INCIDENT`, sa plafonom dokaza.
2. Kontekst aplikacije i release-a: svrha, kritični tokovi, platforme, arhitekture, Python/Qt stek, distribucija, identiteti, podaci, integracije i ograničenja.
3. Source-to-installed-runtime lanac identiteta sa tačnim commit-ima, okruženjima, dependency graph-om, generisanim kodom, hash-evima artefakta, potpisima, instaliranim putanjama i nerazrešenim prekidima.
4. Architecture i trust mape: proces, thread, event loop, QObject, UI/model, QML/WebEngine, IPC/helper, podaci, uređaj, privilegija, installer i update.
5. Tabela verzija/podrške: projekat, resolved, packaged/runtime, aktuelna podržana linija, status, kompatibilnost, akcija i primarni izvor.
6. Tabela nalaza: `ID | P0-P3 | confidence | evidence | platforma | fajl/simbol | uzrok | uticaj | popravka | test | rollback | status | vlasnik`.
7. Implementirane izmene: tačni fajlovi, zavisnosti, generisani izlaz, konfiguracija, dozvole, migracije, package/installer/update izmene i regression rizik.
8. Stvarne komande: komanda, direktorijum, verzije okruženja/alata, platforma, exit code, sažetak izlaza, artefakti i zaključak.
9. Test matrica: unit, integration, GUI, package, install, update, adversarial, performance, accessibility, rollback, restore i blokirane provere.
10. Verifikacija paketa i distribucije: sadržaj, native biblioteke, hash-evi, potpisi, notarizacija, store-ovi, kanali, update metadata, cohort, install i uninstall.
11. Rezultati podataka i oporavka: migracije, konkurentne/duple/prekinute operacije, korupcija, backup, restore, RPO, RTO, rollback, forward repair i reconciliation.
12. Sažetak bezbednosti i privatnosti: autorizacija, izolacija naloga, tajne, fajlovi, plugin-i, WebEngine, IPC, uređaji, lokalni servisi, telemetrija, supply chain i residual risk.
13. Operativna spremnost: budžeti, telemetrija, alert-i, runbook-i, staged rollout, abort, emergency release, kompromitovanje ključa, incident containment i vlasnici.
14. Preostali rad grupisan kao `blocks production`, `needed soon`, `planned refactor` i `optional`, sa vlasnikom, zavisnošću, acceptance kriterijumom i ciljnim datumom.
15. Korišćeni spoljni izvori: naslov, URL, verzija/status, datum pristupa i odluka koju je izvor informisao.

