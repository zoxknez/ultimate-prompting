## Faza J - Validacija Ulaza, Serializacija I Predstavljanje Podataka

- Validiraj path, query, header, cookie, form, JSON, XML, GraphQL, CSV i multipart ulaz na trust granici.
- Audituj strong parameters i odbaci `permit!`, siroke nested attribute-e i dodelu privilegovanih polja bez eksplicitne politike.
- Proveri da serializer-i ne otkrivaju interne ID-jeve, tenant kljuceve, tokene, privatna polja ili podatke zavisne od autorizacije.
- Testiraj Unicode normalizaciju, locale, time zone, DST, valutu, decimalnu preciznost, zaokruzivanje, enum evoluciju i parsiranje datuma.
- Tretiraj Marshal, YAML, ERB, template-e i custom deserializer-e kao granice izvrsavanja koda ili konstrukcije objekata.

