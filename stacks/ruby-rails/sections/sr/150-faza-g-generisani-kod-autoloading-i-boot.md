## Faza G - Generisani Kod, Autoloading I Boot

```text
bin/rails about
bin/rails zeitwerk:check
bin/rails runner 'puts [Rails.version, RUBY_ENGINE, RUBY_VERSION].join(" ")'
bin/rails routes --expanded
```

- Popisi schema fajlove, generisane klijente, protobuf klase, GraphQL tipove, RBI/RBS fajlove, asset manifeste i kod generisan gemovima ili internim alatima.
- Proveri eager load i autoload putanje, inflection pravila, namespace kolizije, engine izolaciju i reload-safe konstante.
- Pregledaj initializer-e za mrezne pozive, upise u bazu, queue registraciju, pristup spoljnim credential-ima, kreiranje thread-ova i zavisnost od redosleda.
- Uporedi development reloader ponasanje sa production eager loading-om i preloading-om.
- Obezbedi da je boot failure eksplicitan i da ne ostavi delimicno zdrav proces koji prihvata saobracaj.

