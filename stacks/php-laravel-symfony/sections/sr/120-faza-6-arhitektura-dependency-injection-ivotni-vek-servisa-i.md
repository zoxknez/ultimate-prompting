## Faza 6 - Arhitektura, dependency injection, životni vek servisa i skriveni side effect-i

### Cilj

Dokaži granice modula, ownership servisa, efektivni dependency injection i lifecycle semantiku.

### Zahtevi audita

- Mapiraj domene, application servise, adaptere, controller-e, komande, listener-e, subscriber-e, modele, entity-je, repository-je, template-e i infrastrukturu.
- Identifikuj service locator upotrebu, globalne helper-e sa side effect-ima, facade-e, static mutable state, skriven pristup container-u, observer-e, model event-e i magic resolution.
- Proveri efektivne Laravel binding-e, contextual binding-e, singleton i scoped lifecycle, service provider-e, package discovery i deferred boot ponašanje.
- Proveri efektivne Symfony container alias-e, autowiring, autoconfiguration, public ili private servise, decoration, lazy servise, reset tagove i compiled output.
- Prati domain i framework event-e, listener-e, observer-e, middleware, subscriber-e i asynchronous dispatch radi pretpostavki o redosledu i transakciji.
- Odbaci široko refaktorisanje bez dokazane invarijante, ograničenog obima, compatibility plana i regresionog suite-a.

### Obavezni dokazi

- Graf modula i zavisnosti sa autoritativnim ownership-om i dozvoljenim smerom zavisnosti.
- Efektivni container graf ili reprezentativni razrešeni servisi iz produkcionog build-a.
- Mapa side effect-a za listener-e, observer-e, model hook-ove, middleware i constructor-e.

### Kriterijumi prihvatanja

- Kritično ponašanje je u eksplicitnim, testabilnim slojevima sa vlasnikom, a ne u slučajnoj framework magiji.
- Životni vek servisa je ispravan za FPM i svaki podržani dugovečni runtime.

