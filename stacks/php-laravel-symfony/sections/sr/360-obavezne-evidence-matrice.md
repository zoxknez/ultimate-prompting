## Obavezne evidence matrice

Izradi svaku matricu ispod. Označi nepoznata polja kao `UNVERIFIED`; ne izostavljaj redove zato što dokaz nije dostupan.

| ID | Matrica | Minimalne obavezne kolone |
| --- | --- | --- |
| M1 | Identitet source-a, runtime-a i artifact-a | komponenta; source commit; build PHP; runtime PHP; SAPI; ekstenzije; artifact digest; deployment revision; dokaz |
| M2 | Podržani režimi izvršavanja | režim; binary; INI; ekstenzije; config; lifecycle; owner; test; support status |
| M3 | Composer i supply chain | package ili alat; source; verzija; trust; skripta ili plugin; ranjivost; waiver; expiry; dokaz |
| M4 | Rute, komande, poruke i ovlašćenja | površina; input; autentikacija; autorizacija; tenant; transakcija; idempotency; rate limit; test |
| M5 | Autentikacija i account lifecycle | tok; kredencijal; expiry; rotacija; opoziv; MFA; recovery; abuse kontrola; dokaz |
| M6 | Podaci, ORM, schema i invarijante | entity ili tabela; authority; tenant ključ; invarijanta; constraint; konkurentnost; retention; recovery |
| M7 | Transakcije i spoljni efekti | tok; database granica; izolacija; idempotency; spoljni efekat; crash tačke; reconciliation; owner |
| M8 | Queue-ovi, worker-i i scheduler-i | job ili poruka; transport; delivery; retry; DLQ; ordering; deduplikacija; konkurentnost; shutdown; recovery |
| M9 | Cache, sesije, lock-ovi, fajlovi i search | store; authority; ključ ili namespace; izolacija; konzistentnost; expiry; invalidacija; restore; test |
| M10 | Zavisnosti, limiti i degraded režimi | zavisnost; owner; kredencijal; timeout; retry; rate limit; kapacitet; failure mode; fallback; SLO |
| M11 | Release, migracija, rollback i restore | promena; compatibility prozor; redosled; canary; abort; rollback; forward repair; RPO; RTO; dokaz |
| M12 | Nalazi, popravke i residual risk | nalaz; severity; dokaz; root cause; popravka; test; rollout; owner; rok; residual risk; status |

