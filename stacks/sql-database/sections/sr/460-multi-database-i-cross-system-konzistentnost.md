## Multi-database i cross-system konzistentnost

Kada poslovni tok obuhvata vise baza ili servisa, dokumentuj odsustvo jedne atomske granice.

- Mapiraj autoritativni sistem za svako polje, objekat i state transition.
- Pregledaj upotrebu distribuiranih transakcija, two-phase commit, retention prepared transakcija i pad koordinatora.
- Preferiraj eksplicitne saga, outbox, inbox i reconciliation ugovore kada globalna atomicnost nije dostupna.
- Testiraj duple, nedostajuce, promenjenog redosleda i zakasnele cross-system event-e.
- Definisi conflict autoritet i manuelni repair za divergentne sisteme.
- Ukljuci stanje spoljnih sistema u rollback, restore i disaster-recovery planiranje.

