## Severity i blokiranje release-a

| Severity | Značenje | Podrazumevani efekat na release |
| --- | --- | --- |
| P0 | Aktivni compromise, katastrofalni integrity ili authorization kvar, rizik neoporavljivog gubitka ili nebezbedno produkciono stanje. | Zaustavi rollout ili traffic, uđi u INCIDENT režim i odmah ograniči incident. |
| P1 | High-confidence kritični exploit, cross-tenant pristup, veliki gubitak ili dupliranje podataka, neispravan recovery ili ozbiljan availability rizik. | Blokiraj release do popravke i verifikacije; zahtevaj odgovornu iznimku samo pod emergency governance-om. |
| P2 | Materijalni defect sa ograničenim uticajem, nedostajuća odbrana, compatibility rizik ili operativna slabost. | Popravi pre release-a ili prihvati sa owner-om, rokom, monitoringom i compensating kontrolom. |
| P3 | Slabost malog uticaja, maintainability problem, optimizacija ili unapređenje dokaza. | Prati sa opravdanim prioritetom i acceptance kriterijumima. |

- Svaka nepoznanica na kritičnoj trust, authorization, transaction, migration ili recovery putanji blokira release dok se ne verifikuje ili eksplicitno risk-accept-uje od odgovorne instance.
- Severity se zasniva na realnom uticaju i exploitability-ju, ne na stilu koda, broju nalaza ili težini popravke.

