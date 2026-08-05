## 2. Web Stack, Filter Chains, And API Contract

Identify whether each surface is servlet MVC, WebFlux, gRPC, WebSocket/SSE, messaging, or management. Do not use blocking JPA/JDBC or filesystem/network work on reactive event-loop threads. In MVC, review server thread limits, multipart/body/header limits, proxy headers, compression, static resource behavior, CORS, exception resolution, and async request handling. In WebFlux, review schedulers, blocking boundaries, cancellation, backpressure, pooled buffers, and context propagation.

Map exact filter order for forwarded headers, request/correlation ID, security headers, CORS, CSRF, rate limits, authentication, authorization, logging, exception translation, and endpoint dispatch. Security filter-chain matchers and request authorization matchers are different scopes; validate every chain, its order, match boundary, and default. A custom `SecurityFilterChain` changes Boot auto-configuration responsibility, so audit management and application endpoint rules together.

For every HTTP/gRPC/WebSocket endpoint validate method/route, auth, status or gRPC code, body/message size, content type, response/error schema, pagination/filter/sort bounds, API version/deprecation, cache semantics, request ID, streaming/backpressure, and compatibility. Do not expose stack traces, exception text, SQL details, internal topology, or debug data.

Assess trusted proxy and host boundaries: forwarded headers, known proxy/network configuration, HTTPS termination, client IP, redirect/cookie security, allowed hosts, request limits, and client-disconnect cancellation. Do not trust arbitrary forwarded headers or expose Swagger, error pages, debug endpoints, or management details publicly by accident.

