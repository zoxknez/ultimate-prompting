## 2. Web Stack, Filter Chainovi I API Ugovor

Utvrdi da li je svaka povrsina servlet MVC, WebFlux, gRPC, WebSocket/SSE, messaging ili management. Ne koristi blokirajuci JPA/JDBC ili filesystem/network rad na reactive event-loop threadovima. U MVC-u pregledaj server thread limite, multipart/body/header limite, proxy headere, compression, static resource ponasanje, CORS, exception resolution i async request handling. U WebFlux-u pregledaj schedulere, blocking granice, cancellation, backpressure, pooled buffere i context propagaciju.

Mapiraj tacan filter redosled za forwarded headers, request/correlation ID, security headere, CORS, CSRF, rate limit, authentication, authorization, logging, exception translation i endpoint dispatch. Security filter-chain matcher i request authorization matcher imaju razlicite opsege; validiraj svaki chain, njegov redosled, match granicu i default. Custom `SecurityFilterChain` menja odgovornost Boot auto-konfiguracije, zato zajedno auditiraj management i application endpoint pravila.

Za svaki HTTP/gRPC/WebSocket endpoint validiraj metod/rutu, auth, status ili gRPC kod, velicinu tela/poruke, content type, response/error semu, granice paginacije/filtera/sortiranja, API verziju/deprecaciju, cache semantiku, request ID, streaming/backpressure i kompatibilnost. Ne iznosi stack trace, exception tekst, SQL detalje, internu topologiju ili debug podatke.

Proceni pouzdane proxy i host granice: forwarded headere, known proxy/network konfiguraciju, HTTPS terminaciju, client IP, redirect/cookie bezbednost, dozvoljene hostove, request limite i client-disconnect cancellation. Ne veruj proizvoljnim forwarded headerima niti slucajno izlozi Swagger, error stranice, debug endpointe ili management detalje javnosti.

