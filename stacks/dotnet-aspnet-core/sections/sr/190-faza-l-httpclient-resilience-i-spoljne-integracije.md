## Faza L - HttpClient, Resilience I Spoljne Integracije

Koristi `IHttpClientFactory` ili ekvivalentan managed client; ne kreiraj unmanaged `HttpClient` po zahtevu. Preferiraj `Microsoft.Extensions.Http.Resilience` umesto deprecated `Microsoft.Extensions.Http.Polly`.

Proveri: timeout, retry sa jitterom, circuit breaker kada je opravdan, concurrency limit, cancellation, auth/tajne, webhook potpis i replay zastitu, schema/version, fallback, sandbox/production razdvajanje, telemetry. Ne retry-uj validation, authorization, cancellation ili non-idempotent write.

Ako servis preuzima user-supplied URL: validiraj scheme, hostname, resolved IPv4/IPv6, loopback/private/link-local/cloud-metadata, portove, DNS rebinding, redirect chain, embedded credentials, size/content type, timeout, decompression. String-only URL validacija nije dovoljna.

