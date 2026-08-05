## Sekvence, identity, generisani kljucevi i distribuirana dodela ID-a

Dokazi uniqueness, exhaustion, ordering i recovery ponasanje svakog generatora identifikatora.

- Inventarisi sekvence, identity kolone, auto-increment, UUID ili ULID generatore, hi-lo allocation i spoljne ID servise.
- Pregledaj cache velicinu, gap-ove, cycling, maksimalnu vrednost, signedness, failover i ponasanje replike.
- Proveri da restore, clone, shard split i kopija okruzenja ne mogu da kreiraju preklapajuce ID opsege.
- Izbegavaj poslovne ordering pretpostavke zasnovane samo na generisanim identifikatorima.
- Testiraj paralelnu dodelu, rollback, retry i bulk import.
- Nadgledaj iscrpljenje i definisi migration plan pre nego sto kapacitet postane kritican.

