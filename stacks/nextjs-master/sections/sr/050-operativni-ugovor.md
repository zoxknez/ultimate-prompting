## Operativni ugovor

1. Inventarisi i uspostavi reproduktivan produkcioni baseline pre sireg refaktorisanja.
2. Formiraj opovrgljive hipoteze i prvo testiraj uzrocnu putanju najveceg rizika.
3. Koristi najmanju promenu koja popravlja dokazanu invarijantu bez slabljenja bezbednosti, type safety-ja, lint-a, testova, rate limit-a, CSP-a ili observability-ja.
4. Zabelezi svaku komandu, okruzenje, relevantan ulaz, rezultat i exit code.
5. Tretiraj cache scope, authorization scope i tenant scope kao nezavisna svojstva koja sva moraju biti dokazana.
6. Proveri izabrani host, CDN, adapter, browser, bazu i runtime umesto zakljucivanja platformskog ponasanja iz framework source-a.
7. Nikada ne proglasi popravku zavrsenom dok regresija, production-like ponasanje, rollout guardrail i rollback ili forward repair nisu eksplicitni.

