## Faza H - SQL semantika, ispravnost i portabilnost

Pregledaj generisani i rucno pisan SQL po semantickoj ispravnosti, a ne samo sintaksi.

- Proveri three-valued logiku, `NULL`, `NOT IN`, alternative za `IS DISTINCT FROM` i ponasanje agregacija.
- Proveri join cardinality, slucajne Cartesian proizvode, outer-join filtere i umnozavanje duplikata.
- Zahtevaj deterministicki redosled i stabilan unique tie-breaker za pagination i batch obradu.
- Pregledaj implicitne cast-ove, type precedence, timezone konverziju, collation coercion i numeric narrowing.
- Pregledaj upsert, merge, replace, returning, generated-key i affected-row semantiku po engine-u.
- Testiraj svaki produkcioni engine kada deljeni SQL tvrdi portabilnost.

