## Faza I - ASP.NET Core Pipeline, Host I API

Mapiraj tacan redosled middleware-a: forwarded headers, exception handling/`IExceptionHandler`, HSTS/HTTPS, static files, routing, CORS, rate limiting, authentication, authorization, antiforgery, localization, endpoint mapping, fallback.

Redosled je ponasanje, ne stil. Pronadji kontrole registrovane posle mapiranih endpointa i middleware koji zaobilazi potrebne kontrole.

Proveri Kestrel/IIS/reverse proxy granice: trusted forwarded headers, allowed hosts, HTTPS terminaciju, client IP, request/header/body limite, keep-alive, request-abort propagaciju. Ne veruj proizvoljnim forwarded headerima. Ne izlazi Swagger, development exception pages, debug endpointe ili detaljan health javno slucajno.

Za Minimal API / MVC / Razor / Blazor / gRPC / SignalR / health / OpenAPI proveri: rutu/metod, status, velicinu tela, content type, error semu, paginaciju/filter/sort bounds, API verziju, cache, request ID, streaming/backpressure, kompatibilnost unazad. Ne iznosi stack trace, SQL detalje ili internu topologiju klijentima.

DTO binding nije autorizacija niti poslovna validacija. Eksplicitno mapiraj dozvoljena polja da sprecis over-posting/mass assignment.

