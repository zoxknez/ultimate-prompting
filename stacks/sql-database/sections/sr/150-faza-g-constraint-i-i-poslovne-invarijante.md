## Faza G - Constraint-i i poslovne invarijante

Postavi svaku invarijantu na najjaci atomski sloj koji moze da je sprovede.

- Inventarisi primary, unique, foreign-key, check, exclusion, generated i partial constraint-e.
- Testiraj unique sa NULL vrednostima, collation-om, soft deletion-om, tenant scope-om i paralelnim insert-ima.
- Proveri foreign-key akciju, deferrability, indeksiranje, delete ponasanje i orphan repair.
- Tretiraj aplikativni check-then-write kao nebezbedan kada je potreban database constraint ili atomska naredba.
- Proveri trigger i stored-program invarijante pod bulk load-om, replikacijom, iskljucenim constraint-ima i restore-om.
- Napravi reconciliation upite za svaku kriticnu invarijantu.

