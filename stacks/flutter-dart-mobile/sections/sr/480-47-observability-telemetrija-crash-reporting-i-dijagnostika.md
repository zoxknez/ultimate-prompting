## 47. Observability, telemetrija, crash reporting i dijagnostika

Telemetrija mora identifikovati uticaj na korisnika bez postajanja privacy ili stability rizika.

- Definiši event-e, metrike, trace-ove, logove, crash izveštaje, breadcrumb-e, mrežnu dijagnostiku, performance span-ove, release marker-e i signale poslovnog ishoda.
- Dodaj verziju aplikacije, build, platformu, OS/browser, klasu uređaja, flavor, okruženje, feature flag stanje, operation ID i privacy-safe account/tenant korelaciju.
- Redaktuj tokene, kredencijale, authorization header-e, cookie-je, lične podatke, sadržaj fajla, osetljive putanje, notification payload-e, polja formi i sirove vrednosti baze.
- Proveri da se Flutter framework greške, platformske greške, neuhvaćene async greške, isolate greške, native crash-evi, ANR/hang, web greške i update/install greške hvataju bez petlji.
- Upload-uj i zadrži tačne Dart symbol map-e, Android mapping/native simbole, Apple dSYM, Windows/macOS/Linux simbole i web source map-e po artefaktu.
- Definiši sampling, pristanak, opt-out, retention, data residency, kontrole pristupa, brisanje, ponašanje pri vendor outage-u, izolaciju SDK greške i cost limite.
- Napravi dashboard-e i alert-e za crash-free users/sessions, startup, jank, memoriju, mrežne greške, auth greške, migration greške, sync konflikte, update greške i kritične tokove.
- Proveri da svaki actionable alert ima vlasnika, prag, deduplikaciju, runbook, eskalaciju, bezbedne dijagnostičke upite i dokaz zatvaranja.
- Testiraj telemetriju offline, tokom startup greške, posle logout-a, pod crash loop-om, sa blokiranim vendor-ima i kroz staged release/rollback.

