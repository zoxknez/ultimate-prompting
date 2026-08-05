## 39. Production readiness checklist

1. Source-to-installed-runtime identitet je kontinuiran i reproduktivan za svaki podržani release target.
2. Tačni Python, PySide6, Qt, native biblioteke, packaging alati i OS podrška su aktuelni i verifikovani.
3. Architecture, ownership, process, thread, QObject, model, QML, WebEngine, IPC, data, privilege i update mape su kompletne.
4. Ne ostaje nerazrešen P0 ili P1 nalaz bez eksplicitnog ovlašćenog prihvatanja i containment-a.
5. GUI thread, event loop-ovi, worker-i, task-ovi, subprocess-i, helper-i, cancellation, shutdown i zaštita od stale rezultata su verifikovani.
6. QObject vlasništvo, destrukcija, signali, slot-ovi, reentrancy, model/view notifikacije i UI stanje su ispravni pod stress-om.
7. Authentication, authorization, tenant/account izolacija, secret storage, privatnost i privilegovane akcije su verifikovani negativnim testovima.
8. Lokalni podaci, migracije, konkurentnost, offline queue-evi, corruption handling, backup, retention, brisanje i restore su verifikovani.
9. Fajlovi, arhive, parser-i, plugin-i, skripte, WebEngine sadržaj, deep link-ovi, IPC, uređaji i OS ulazi su ograničeni i testirani.
10. Packaging uključuje samo nameravane fajlove i native komponente; package, installer, potpis, notarizacija i instalirano stanje su verifikovani.
11. Fresh install, upgrade matrica, prekinut update, rollback/forward repair, uninstall i restore na čistoj mašini su testirani.
12. Performanse, responsiveness, memorija, CPU, GPU, disk, mreža, capacity i low-resource ponašanje ispunjavaju izmerene budžete.
13. Accessibility, lokalizacija, high DPI, više monitora, screen reader-i, keyboard rad, RTL, IME i reduced motion su testirani.
14. Observability identifikuje tačne release bajtove i dijagnostikuje kritične GUI, worker, update, migration, data i native kvarove bez curenja osetljivih podataka.
15. CI/CD štiti trusted release granice, verifikuje zavisnosti, proizvodi SBOM/provenance i promoviše immutable artefakte.
16. Rollout, abort, emergency release, kompromitovanje signing ključa, kompromitovanje update feed-a, incident containment i trusted rebuild su dokumentovani i uvežbani.
17. Svaka materijalna popravka ima fokusiranu regresiju, packaged verifikaciju, vlasnika, rizik i rollback.
18. Sve primenljive evidence matrice i adversarial scenariji su kompletni ili eksplicitno blokirani sa vlasnikom i acceptance planom.
19. Finalni diff je uzak, reviewable, dokumentovan i bez nepovezanih izmena ili oslabljenih testova.
20. Finalni izveštaj sadrži tačne dokaze, komande, artefakte, hash-eve, rezultate, blocker-e, residual risk, vlasnike i autoritativne izvore.

