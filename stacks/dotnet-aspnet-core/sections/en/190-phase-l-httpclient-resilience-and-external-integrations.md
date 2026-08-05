## Phase L - HttpClient, Resilience, And External Integrations

Use `IHttpClientFactory` or an equivalent managed client; do not create unmanaged `HttpClient` per request. Prefer `Microsoft.Extensions.Http.Resilience` over deprecated `Microsoft.Extensions.Http.Polly`.

Check: timeout, retry with jitter, circuit breaker when justified, concurrency limit, cancellation, auth/secrets, webhook signature and replay protection, schema/version, fallback, sandbox/production separation, telemetry. Do not blindly retry validation, authorization, cancellation, or non-idempotent writes.

If the service fetches a user-supplied URL: validate scheme, hostname, resolved IPv4/IPv6, loopback/private/link-local/cloud-metadata ranges, ports, DNS rebinding, redirect chain, embedded credentials, size/content type, timeout, decompression. String-only URL validation is insufficient.

