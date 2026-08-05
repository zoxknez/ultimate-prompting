## Faza M - Idempotentnost, duple isporuke i reconciliation

Pretpostavi da ce se retry, dupli request-i i padovi procesa dogoditi.

- Definisi scope idempotency kljuca, request fingerprint, ownership, expiry i conflict ponasanje.
- Sacuvaj idempotency claim i poslovni rezultat atomski kada je moguce.
- Testiraj duple request-e pre, tokom i posle commit-a, ukljucujuci timeout nakon commit-a.
- Testiraj duple queue poruke, CDC event-e, webhook-ove i scheduled job-ove.
- Koristi database constraint-e kao poslednju odbranu od duplih trajnih efekata.
- Obezbedi reconciliation i manuelne repair procedure za nejasne ishode.

