## View-ovi, materialized view-ovi, search, spatial i izvedeni podaci

Izvedeni podaci moraju imati eksplicitne freshness, authority, refresh, invalidation i recovery ugovore.

- Inventarisi view-ove, materialized view-ove, indexed view-ove, search indekse, spatial indekse i summary tabele.
- Proveri da ownership i autorizacija nisu oslabljeni definer context-om ili zaobidjenim base-table politikama.
- Definisi freshness SLO, refresh trigger, concurrency mode, failure ponasanje i catch-up proceduru.
- Testiraj schema promene i engine nadogradnje prema sacuvanim definicijama, parser-ima, tokenizer-ima i spatial reference sistemima.
- Usaglasi izvedene agregate i search dokumente sa autoritativnim tabelama.
- Ukljuci vreme rebuild-a izvedenih podataka i storage u RTO i capacity planove.

