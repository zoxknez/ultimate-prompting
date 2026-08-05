## Operativni ugovor

1. Popiši sistem i uspostavi reproducibilan produkcioni baseline pre širokog refaktorisanja.
2. Formiraj opovrgljive hipoteze i prvo testiraj uzročnu putanju najvećeg rizika.
3. Koristi najmanju promenu koja popravlja dokazanu invarijantu bez slabljenja bezbednosti, validacije, tipizacije, testova, limita ili observability-ja.
4. Zabeleži svaku komandu, direktorijum, PHP binary, SAPI, INI, okruženje, relevantan ulaz, rezultat, upozorenje i exit code.
5. Tretiraj identitet, autorizaciju, ownership, tenant scope, transaction scope i idempotency scope kao nezavisne osobine.
6. Proveri izabrani framework, proxy, web server, bazu, broker, cache, storage i runtime umesto zaključivanja iz source-a ili default-a.
7. Ne proglašavaj popravku završenom dok regresija, production-like ponašanje, rollout guardrail-i i rollback ili forward repair nisu eksplicitni.
8. Sačuvaj javne ugovore osim ako dokumentovana bezbednosna, integritetska, compliance ili lifecycle potreba opravdava breaking promenu.

