## 30. Obavezni zavrsni izvestaj

1. Executive summary i zakljucak: `ready`, `ready-with-conditions` ili `not-ready`, sa evidence ceiling-om.
2. Application i release kontekst: framework, verzije, platforme, arhitekture, kanali, kriticni tokovi, podaci, identiteti i ogranicenja.
3. Source-to-installed-runtime identity lanac sa hash-evima artefakta i nerazresenim prekidima.
4. Arhitektonska, process, window/webview, origin, privilege, IPC/command, local service, data, installer i update mapa.
5. Tabela verzija i podrske: project, resolved, packaged/runtime, trenutni stable, support status, kompatibilnost, akcija, izvor.
6. Tabela nalaza: `ID | P0-P3 | dokaz | framework/oblast | platforma | fajl/simbol | uzrok | uticaj | popravka | test | rollback | status`.
7. Implementirane izmene: tacni fajlovi, konfiguracija, dependency-ji, capabilities/permissions, signing/update/installer izmene, migracije i regression rizik.
8. Stvarne komande: komanda, direktorijum, environment/tool verzije, platforma, exit code, sazetak izlaza, generisani artefakti i zakljucak.
9. Build/test/package matrica, adversarial scenariji, performance/resource merenja, accessibility rezultati i blokirane provere.
10. Verifikacija artefakta/paketa/signing-a/notarizacije/prodavnice/update-a sa tacnim hash-evima, identitetima, timestamp-ima i kanalom.
11. Rezultati install, update, migration, rollback, recovery, uninstall i incident-readiness provera.
12. Security i privacy sazetak: renderer/webview izolacija, IPC/command autorizacija, fajlovi/URL-ovi, lokalni servisi, tajne, telemetrija, supply chain i preostali rizik.
13. Operational readiness: SLO/budzeti, telemetrija, alert-i, runbook-ovi, staged rollout, abort, emergency release, kompromitacija kljuca, backup/restore i vlasnici.
14. Preostali rad grupisan kao `blocks production`, `needed soon`, `planned refactor` i `optional`, sa vlasnikom, dependency-jem, acceptance kriterijumom i ciljnim datumom.
15. Eksterni izvori konsultovani: naslov, URL, verzija/status, datum pristupa i odluka koju je informisao.

