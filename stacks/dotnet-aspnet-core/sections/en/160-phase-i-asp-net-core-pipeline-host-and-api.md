## Phase I - ASP.NET Core Pipeline, Host, And API

Map exact middleware order: forwarded headers, exception handling/`IExceptionHandler`, HSTS/HTTPS, static files, routing, CORS, rate limiting, authentication, authorization, antiforgery, localization, endpoint mapping, fallback.

Ordering is behavior, not style. Find controls registered after mapped endpoints and middleware that bypasses required controls.

Check Kestrel/IIS/reverse-proxy boundaries: trusted forwarded headers, allowed hosts, HTTPS termination, client IP, request/header/body limits, keep-alive, request-abort propagation. Do not trust arbitrary forwarded headers. Do not accidentally expose Swagger, development exception pages, debug endpoints, or detailed health publicly.

For Minimal API / MVC / Razor / Blazor / gRPC / SignalR / health / OpenAPI validate: route/method, status, body size, content type, error schema, pagination/filter/sort bounds, API version, cache, request ID, streaming/backpressure, backward compatibility. Do not expose stack traces, SQL details, or internal topology to clients.

DTO binding is not authorization or business validation. Explicitly map allowed fields to prevent over-posting/mass assignment.

