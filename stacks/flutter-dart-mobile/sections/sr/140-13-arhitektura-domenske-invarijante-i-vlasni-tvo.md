## 13. Arhitektura, domenske invarijante i vlasništvo

Ocenjuj arhitekturu po očuvanom ponašanju, ne po nazivima foldera ili brendu state management-a.

- Mapiraj presentation, application, domain, data, platform, infrastructure i integration odgovornosti i stvarni smer zavisnosti.
- Zapiši eksplicitne invarijante za identitet, autorizaciju, novac, inventar, kvote, redosled, promene statusa, offline akcije, sinhronizaciju, brisanje i oporavak.
- Prati svaki kritični tok od korisničkog ulaza kroz stanje, repozitorijum, lokalni cache, platformski servis, backend, persistenciju, telemetriju i prikazani rezultat.
- Proveri vlasništvo nad promenljivim stanjem, lifecycle-om, cancellation-om, retry-jima, subscription-ima, stream-ovima, controller-ima, cache-om, database handle-ovima i platformskim resursima.
- Otkrij poslovnu logiku dupliranu kroz widget-e, view model-e, provider-e, bloc-ove, repozitorijume, backend klijente, native kod i push handler-e.
- Proveri dependency inversion gde poboljšava testabilnost i platformsku izolaciju; odbaci ceremonijalnu apstrakciju koja skriva ponašanje ili error semantiku.
- Identifikuj god object-e, kružne zavisnosti, service-locator coupling, feature leakage, deljene promenljive modele, implicitne singleton-e i cross-feature side effect-e.
- Proveri da je platformski kod izolovan iza eksplicitnih ugovora sa fallback-om, obradom nepodržanog stanja, testovima i observability-jem.
- Ne refaktoriši arhitekturu široko bez potvrđenog rizika, merljivog ishoda, plana kompatibilnosti, migracione sekvence i rollback-a.

