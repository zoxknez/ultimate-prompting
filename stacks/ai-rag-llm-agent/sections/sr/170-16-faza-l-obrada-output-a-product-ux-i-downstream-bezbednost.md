## 16. Faza L - Obrada Output-a, Product UX I Downstream Bezbednost

1. Model output tretiraj kao untrusted podatak.
2. Validiraj structured output prema strict schema i poslovnim pravilima.
3. Encode ili sanitizuj output za HTML, Markdown, SQL, shell, code, email, dokumente, logove i druge sink-ove.
4. Spreci XSS, template injection, command injection, unsafe link, formula injection i downstream prompt injection.
5. Jasno razdvoji generisan, retrieved, izveden i verifikovan sadrzaj.
6. Prikazi citate i dokaze na nivou potrebnom za use case.
7. Prikazi neizvesnost, ogranicenja i escalation put bez lazne sigurnosti.
8. Proveri accessibility, lokalizaciju, streaming stanja, cancellation, partial answer, retry i error recovery.
9. Spreci UI da sugerise uspeh akcije pre nego sto autoritativni backend to potvrdi.
10. Proveri da regulisane ili high-impact odluke imaju odgovarajuci human oversight i explanation put.

