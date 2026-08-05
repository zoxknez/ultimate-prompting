## Faza 7 - Fastify 5, Plugin-i, Encapsulation I Scheme

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Identifikuj tacne Fastify core i plugin verzije i proveri LTS i Node support kompatibilnost.
- Mapiraj plugin DAG, redosled registracije, prefix-e, decorator-e, hook-ove, scheme i encapsulation granice.
- Detektuj slucajno globalno izlaganje, nedostajuce decorator zavisnosti, duplu registraciju i scope-dependent ponasanje.
- Tretiraj JSON Schema definicije kao application kod jer validator-i i serializer-i mogu dinamicki da ih kompajliraju.
- Nikada ne kompajliraj user-provided scheme; pregledaj Ajv opcije, formate, keyword-e, shared ID-jeve i serializer ponasanje.
- Drzi database ili eksterne pozive van pocetne schema validacije i koristi odgovarajuce hook-ove za async provere.

### Obavezni Dokazi

- Proizvedi i sacuvaj plugin i encapsulation graf.
- Proizvedi i sacuvaj inventar schema, serializer-a i hook-ova.
- Proizvedi i sacuvaj dokaz podrske core-a i plugin-a.

### Obavezni Failure I Acceptance Testovi

- Dokazi da sibling plugin ne moze da pristupi nenameravanom decorator-u.
- Dokazi da untrusted schema input se odbija pre kompilacije.
- Dokazi da response serializacija sprecava curenje privatnih polja.

