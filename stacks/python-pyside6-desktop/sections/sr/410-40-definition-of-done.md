## 40. Definition of Done

1. Aktuelni repozitorijum, okruženje, toolchain, paket, instalirana aplikacija, runtime i production-like stanje su eksplicitno razdvojeni.
2. Svi kritični tokovi i invarijante imaju evidence-backed vlasništvo, failure ponašanje, recovery i testove.
3. Svaki potvrđeni P0-P2 nalaz ima root cause, najmanju kompletnu popravku ili odobren plan, regression dokaz, release uticaj i vlasnika.
4. Nijedna kritična tvrdnja se ne oslanja samo na source pregled kada su potrebni packaged, installed, runtime, upgrade, rollback ili restore dokazi.
5. Sve podržane kombinacije platforme i arhitekture imaju aktuelan dokaz podrške ili su eksplicitno uklonjene iz tvrdnji.
6. Konkurentnost, QObject lifetime, cancellation, shutdown, promena naloga, duple akcije i stale rezultati su bezbedni.
7. Lokalni podaci i spoljni side effect-i ostaju konzistentni pod duplim, konkurentnim, prekinutim i crash uslovima.
8. Sadržaj paketa, potpisi, installer, updater i instalirane search putanje odolevaju tampering-u i hijacking-u.
9. Fresh install, upgrade, repair, rollback/forward repair, uninstall, backup i restore su operativno upotrebljivi.
10. Zaključci o performansama i accessibility-ju su izmereni na zapakovanim build-ovima i reprezentativnom hardveru.
11. Observability i support dokazi su dovoljni, korelisani, bounded i privacy-safe.
12. CI/CD, signing, promotion, rollout, abort, incident, revocation i trusted rebuild kontrole su reviewable i testirane gde su materijalne.
13. Sve komande, preskočene provere, kvarovi, artefakti, hash-evi, screenshot-ovi, trace-ovi i residual rizici su istinito zabeleženi.
14. Nepovezani fajlovi i korisnički rad su sačuvani; finalni skup izmena je minimalan i reviewable.
15. Finalni zaključak prati plafon dokaza i ne preuveličava bezbednost, kompatibilnost, testiranje ili recovery.

