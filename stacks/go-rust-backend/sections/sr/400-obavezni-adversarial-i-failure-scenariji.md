## Obavezni adversarial i failure scenariji

Izvrši primenljive scenarije sa definisanim preduslovima, posmatranim signalima, pass/fail pragovima, cleanup-om i nivoom dokaza. Ne prijavljuj samo da je sistem preživeo.

1. Dve konkurentne mutacije ciljaju istu invarijantu, agregat, ključ, nalog, kvotu ili stavku inventara.
2. Request ili poruka se ponavlja pre, tokom i posle commit-a, gubitka odgovora, gubitka acknowledgment-a ili pada procesa.
3. Klijent prekida vezu ili deadline ističe dok je database, filesystem, queue, subprocess ili foreign-library rad u toku.
4. Spor ili zlonameran peer šalje delimične frame-ove, prevelike dužine, kompresione bombe, beskonačne stream-ove, nevalidne encoding-e ili kršenja stanja protokola.
5. Database pool, connection limit, file descriptor, memorija, CPU, thread, goroutine, task, red ili ephemeral-port kapacitet se približava iscrpljenju.
6. Downstream zavisnost postaje spora, povremeno pada, vraća overload, zatvara konekcije, menja DNS, rotira sertifikate ili se postepeno oporavlja.
7. Retry umnožavanje nastaje kroz client, proxy, service, database, queue i worker slojeve.
8. Proces dobija graceful shutdown dok prima rad, drži lock-ove, poseduje lease-eve, služi stream-ove, commit-uje transakcije ili objavljuje događaje.
9. Proces panic-uje, abort-uje, biva ubijen ili gubi host tokom delimične inicijalizacije, migracije, upisa, upload-a, objave događaja ili checkpoint-a.
10. Stari i novi binarni fajlovi koegzistiraju sa starim, prelaznim i novim šemama, porukama, kešom i protokolskim peer-ovima.
11. Build tag, feature, target, cgo/native putanja, allocator, TLS backend, database backend ili opciona integracija se razlikuje od najčešće testiranog default-a.
12. Zastareli lock holder, lease owner, leader, cache unos, token, konfiguracioni snapshot ili DNS odgovor nastavlja posle promene ownership-a ili ovlašćenja.
13. Red isporučuje duplikate, menja redosled poruka, odlaže poruke preko pretpostavke, rebalance-uje ownership ili ponavlja poison poruku iz DLQ-a.
14. Tenant, nalog, uloga, namespace ili object identifikatori se menjaju uz očuvanje validne sintakse i autentikacije.
15. Tajne, signing ključevi, sertifikati, token-i, dependency kredencijali ili encryption ključevi se rotiraju, ističu, opozivaju ili privremeno postaju nedostupni.
16. Backup ili snapshot se vraća u izolovano okruženje dok se binarni fajlovi, migracije, ključevi, spoljne zavisnosti i zadržani događaji razlikuju od vremena backup-a.
17. Telemetrija, health, readiness i alert-i se ocenjuju tokom degradacije da dokažu razlikovanje dependency failure-a, overload-a, deadlock-a, curenja, korupcije i oporavka.
18. Rollback se pokušava posle code-only promene, promene konfiguracije, zavisnosti, šeme, protokola i delimično završenog rollout-a.

