## Operativni Ugovor

1. Napravi inventar i utvrdi reproducibilan production baseline pre sirokog refactoring-a.
2. Formiraj opovrgljive hipoteze i prvo testiraj uzrocnu putanju sa najvecim rizikom.
3. Koristi najmanju promenu koja popravlja dokazanu invarijantu bez slabljenja security-ja, validacije, typing-a, testova, limita ili observability-ja.
4. Zabelezi svaku komandu, direktorijum, runtime, okruzenje, relevantan input, rezultat, upozorenje i exit code.
5. Tretiraj identitet, autorizaciju, ownership, tenant scope, transaction scope i idempotency scope kao nezavisna svojstva.
6. Proveri izabrani proxy, host, database, broker i runtime umesto izvodjenja ponasanja iz framework source-a.
7. Ne proglasavaj popravku zavrsenom dok regression, production-like ponasanje, rollout guardrail-i i rollback ili forward repair nisu eksplicitni.
8. Sacuvaj javne ugovore osim kada dokumentovani security, integrity, compliance ili lifecycle zahtev opravdava breaking change.

