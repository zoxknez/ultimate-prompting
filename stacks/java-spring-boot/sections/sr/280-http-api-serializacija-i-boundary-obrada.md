## HTTP, API, Serializacija I Boundary Obrada

### Inventar Endpoint-a I Ugovora

- Generiši inventar MVC, WebFlux, functional, GraphQL, WebSocket, SSE, RSocket, gRPC, Actuator, management, callback, webhook i internih endpoint-a.
- Zabeleži putanju, metod, media type, verziju, publiku, authentication, authorization, tenant pravilo, request limit, timeout, idempotency, transaction granicu, response ugovor i owner-a.
- Uporedi runtime mapping-e sa source-om, OpenAPI/AsyncAPI/GraphQL schema-ma, API gateway konfiguracijom, generisanim klijentima, testovima i dokumentacijom.
- Detektuj dvosmislene mapping-e, zasenjene route-ove, slučajnu Actuator izloženost, test-only endpoint-e, deprecated verzije i management portove dostupne nepoverljivim mrežama.
- Testiraj direktan pristup koji zaobilazi UI, gateway, client-side provere, service mesh ili očekivani redosled poziva.

### HTTP I Proxy Semantika

- Proveri trusted proxy granice, forwarded header-e, scheme, host, port, client IP, path prefix, TLS terminaciju, mutual TLS i konstrukciju redirect-a.
- Testiraj request smuggling varijante, duple header-e, konfliktne content length vrednosti, transfer encoding, prevelike header-e, malformed cookie-je, kodirane putanje i razlike u normalizaciji kroz hop-ove.
- Definiši i proveri timeout budget za accept, header-e, body, handler, downstream pozive, upis odgovora, keep-alive, idle konekcije, streaming i graceful shutdown.
- Pregledaj compression, decompression limite, range request-e, conditional request-e, caching header-e, ETag semantiku, redirect-e, retry i tretman safe/idempotent metoda.
- Proveri da error mapping koristi stabilne status kodove i Problem Details bez stack trace-a, tajni, internih identifikatora, tenant podataka ili kontradiktornog retry uputstva.

### Serializacija I Evolucija Schema-e

- Inventariši svaki `ObjectMapper`, codec, modul, naming strategy, polymorphic konfiguraciju, date/time pravilo, numeric pravilo, unknown-field policy i custom serializer/deserializer.
- Tretiraj Jackson 2 i Jackson 3 kao različite compatibility površine; proveri package promene, dostupnost modula, coercion default-e, polymorphism i generisane klijente tokom migracije.
- Audituj JSON, XML, YAML, CSV, protobuf, Avro, Java serialization, Kryo, MessagePack i custom binary formate za type confusion, gadget putanje, entity expansion, depth, size i allocation limite.
- Testiraj old producer/new consumer, new producer/old consumer, odsutna polja, nepoznata polja, preimenovane enum-e, promenjen redosled polja, nullability, precision, velike brojeve i duple key-eve.
- Verzioniši spoljne ugovore eksplicitno i dokaži da database, event, cache, file i API schema promene mogu koegzistirati tokom rolling deployment-a i rollback-a.

### Validacija, Fajlovi, Arhive I Webhook-ovi

- Validiraj sintaksnu formu, semantičko značenje, authorization, ownership, state, kvotu, svežinu i cross-field invarijante na autoritativnoj granici.
- Primeni eksplicitne limite na request size, multipart delove, nazive fajlova, putanje, dimenzije, redove, ćelije, archive entry-je, dekompresovane bajtove, rekurziju, parser vreme i privremeni storage.
- Spreči traversal, symlink escape, overwrite, polyglot sadržaj, content-type spoofing, formula injection, decompression bomb, zlonamerno document/media parsiranje i nebezbedne spoljne converter-e.
- Za webhook proveri signature scheme, raw-body obradu, timestamp window, key rotation, replay zaštitu, event identitet, ordering, idempotency i acknowledgement strategiju.
- Stavi nepoverljive fajlove i event-e u karantin dok validacija i scanning ne završe; definiši deletion, retention, privacy, retry i forensic evidence ponašanje.


