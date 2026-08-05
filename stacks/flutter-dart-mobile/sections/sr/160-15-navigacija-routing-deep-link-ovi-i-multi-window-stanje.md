## 15. Navigacija, routing, deep link-ovi i multi-window stanje

Tretiraj navigaciju kao bezbednosnu, lifecycle i state-consistency granicu.

- Popiši Navigator API-je, Router, deklarativne routing pakete, nested navigator-e, shell route-ove, modal rute, restoration ID-jeve i custom tranzicije.
- Proveri da su path, query, fragment, route extras, serializovano stanje i platformski deep-link ulazi parsirani, normalizovani, ograničeni i autorizovani.
- Testiraj cold start, warm start, background resume, ubijen proces, logged-out stanje, istek sesije, pogrešan tenant, nedostajući resurs i duplu isporuku deep link-a.
- Spreči authorization bypass direktnim ulaskom u rutu; skrivanje UI-ja nije autorizacija.
- Proveri browser back/forward, URL sinhronizaciju, refresh, history restoration, canonical URL-ove i ponašanje nepodržanih ruta na web-u.
- Proveri da više prozora, scene-a, desktop instanci, sekundarnih ekrana, notification tap-ova i add-to-app engine-a ne deli ili ne prepisuje pogrešno navigaciono stanje.
- Audituj redirect petlje, async guard-e, zastarele guard-e, race condition između obnove sesije i routing-a i curenje informacija na error stranama.
- Zahtevaj route contract testove i platformske deep-link testove za sve privilegovane i poslovno kritične destinacije.

