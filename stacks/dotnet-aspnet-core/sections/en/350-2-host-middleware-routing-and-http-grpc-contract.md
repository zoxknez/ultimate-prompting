## 2. Host, Middleware, Routing, And HTTP/gRPC Contract

Map exact middleware and endpoint order. Review forwarded headers, exception handling, HSTS/HTTPS, static files, routing, CORS, rate limiting, authN/authZ, antiforgery, localization, fallback. Ordering is behavior.

For all API surfaces validate route/method, status, body size, content type, error schema, pagination/filter/sort, version, cache, request ID, streaming/backpressure, compatibility. Do not expose stack traces, SQL, or internal topology.

Assess proxy/Kestrel boundaries; do not trust arbitrary forwarded headers; do not accidentally expose Swagger/debug/detailed health publicly.

