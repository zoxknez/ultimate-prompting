## 26. Format Zavrsnog Izvestaja

Isporuci Markdown izvestaj sa:

1. Executive summary i verdict: `ready`, `ready-with-conditions` ili `not-ready`.
2. Opsegom, rezimom rada, okruzenjima, pristupom i ogranicenjima.
3. Technology i specification baseline-om sa primarnim izvorima i datumima pristupa.
4. Inventarom sistema i AI bill of materials.
5. Architecture, data-flow, trust-boundary i permission mapama.
6. Matricom data lifecycle-a, retention-a, delete-a i provider processing-a.
7. Threat model-om i abuse case-ovima.
8. Tabelom nalaza: `ID | P0-P3 | komponenta | evidence | uzrok | uticaj | popravka | verifikacija | status`.
9. Eval dizajnom, dataset-ima, konfiguracijom, stvarnim metrikama, varijansom, failing primerima i ogranicenjima.
10. Implementiranim izmenama i regression testovima.
11. Logom komandi i evaluacija samo sa stvarnim exit statusima.
12. Blokiranim i `UNVERIFIED` oblastima sa tacno navedenim nedostajucim dokazom ili pristupom.
13. Residual risk-ovima, containment-om, vlasnikom i sledecom akcijom.
14. Napomenama o pravnoj i compliance primenjivosti bez nepotvrdjenih pravnih zakljucaka.
15. Production-readiness Definition of Done listom.
16. Spoljnim izvorima: naslov, URL, verzija ili datum, datum pristupa i odluka na koju je izvor uticao.

Pored toga isporuci kratak machine-readable JSON sazetak gde je prakticno.

