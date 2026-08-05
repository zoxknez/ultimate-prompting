## 2. Host, Middleware, Rutiranje I HTTP/gRPC Ugovor

Mapiraj tacan middleware i endpoint redosled. Pregledaj forwarded headers, exception handling, HSTS/HTTPS, static files, routing, CORS, rate limiting, authN/authZ, antiforgery, localization, fallback. Redosled je ponasanje.

Za sve API povrsine validiraj rutu/metod, status, body size, content type, error semu, pagination/filter/sort, verziju, cache, request ID, streaming/backpressure, kompatibilnost. Ne iznosi stack trace, SQL ili internu topologiju.

Proceni proxy/Kestrel granice; ne veruj proizvoljnim forwarded headerima; ne izlazi Swagger/debug/health detalje javno slucajno.

