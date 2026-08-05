## Faza 9 - Hydration, state, effect-i i React concurrency

Dokazi deterministicki rendering, ispravno vlasnistvo state-a, bezbedne effect-e i stabilno ponasanje pod concurrent rendering-om i navigacijom.

### Zahtevi audita

- Detektuj hydration razlike izazvane vremenom, random-om, locale-om, vremenskom zonom, browser API-jima, neispravnim HTML-om, data race-om ili flag drift-om.
- Pregledaj duplirani state, derived state, stale closure-e, effect dependency-je, subscription-e, timer-e, observer-e, abort i cleanup.
- Proveri da Suspense, transitions, optimistic update-i, useActionState, useOptimistic i error recovery cuvaju invarijante.
- Spreci double-submit, stale overwrite, izgubljen optimistic rollback, duplu notifikaciju i replay izazvan navigacijom.
- Auditiraj context scope, external store-ove, hydration snapshot-e, stabilnost selector-a i subscription ponasanje.
- Koristi React Compiler samo sa izmerenom kompatibilnoscu, eksplicitnim rollout-om i disable putanjom.

### Obavezni dokazi

- Inventar hydration upozorenja sa deterministickom reprodukcijom.
- Mapa vlasnistva state-a i effect-a za kriticne tokove.
- Pre/posle rendering, memory, interaction i bundle metrike.
- Lista optimistic mutation-a i autoritativnih reconciliation putanja.

### Obavezni failure i acceptance testovi

- Ponovi hydration kroz locale-e, vremenske zone, satove, browser-e i flag stanja.
- Posalji brzo, navigiraj dalje, abortuj, vrati se i proveri jedan autoritativan rezultat.
- Resolve-uj konkurentne request-e van redosleda i blokiraj stale overwrite.
- Canary-uj React Compiler i dokazi correctness, performance, memory i debugging acceptance.

