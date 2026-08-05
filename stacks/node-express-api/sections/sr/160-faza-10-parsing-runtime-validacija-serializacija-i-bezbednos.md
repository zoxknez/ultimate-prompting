## Faza 10 - Parsing, Runtime Validacija, Serializacija I Bezbednost Output-a

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Tretiraj path, query, header-e, cookie-je, body, multipart polja, fajlove, metadata i upstream response-e kao untrusted.
- Definisi body, field, depth, array, string, number, file-count, header, decompression i total request limite.
- Primeni strukturne scheme, semantic validaciju, cross-field pravila, authorization-aware constraint-e i field allowlist-e.
- Spreci mass assignment, prototype pollution, unsafe merge, coercion dvosmislenost, duplicate-key dvosmislenost i gubitak precision-a.
- Validiraj datume, time zone, trajanja, novac, identifikatore, Unicode normalization i regex complexity.
- Definisi output scheme ili serializer-e za osetljive API-je i proveri da ih koriste error i alternativne response putanje.

### Obavezni Dokazi

- Proizvedi i sacuvaj inventar input i output schema.
- Proizvedi i sacuvaj matricu limita, coercion-a i field allowlist-e.
- Proizvedi i sacuvaj serialization i content-type dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da prevelik i duboko ugnjezden input se jeftino odbija.
- Dokazi da prototype kljucevi ne mogu da promene application objekte.
- Dokazi da privatna polja se nikada ne pojavljuju kroz alternativne response putanje.

