## 6. Configuration, Actuator, Supply Chain, And Abuse Controls

Validate typed configuration at startup. Critical configuration or secrets must fail safely at startup, not on the first production request. Review property-source precedence, profiles, environment naming, config-server/secrets integration, keystores, encryption keys, DataSource URLs, `.env` files, source history where permitted, CI logs/artifacts, container layers, fixtures, and configuration endpoints.

Inventory Actuator endpoint access and exposure separately for HTTP and JMX. Use a restrictive allow list, protect sensitive management endpoints, sanitize values, and avoid public `env`, `configprops`, `beans`, `mappings`, heap dump, thread dump, log file, shutdown, or dynamic logger access. Public HTTP exposure must be an explicit decision with network and Spring Security controls, not merely a dependency default.

Define rate limits by trusted client IP, user, API key, tenant, route, failed attempt, operational cost, and active-job count. Validate partition key, proxy/IP behavior, distributed versus per-instance semantics, burst algorithm, queue limits, headers, `Retry-After`, fail-open/fail-closed policy, and memory bounds. Login, reset, expensive search/export/upload, AI, and job creation need distinct controls.

Find injection, SpEL/template injection, unsafe Java deserialization, command/file/path injection, open redirect, SSRF, XML entity risks, log injection, upload abuse, secret exposure, insecure headers, vulnerable dependencies, compromised repositories/plugins, and debug leakage. Pin and review build-plugin and dependency sources; generate/review an SBOM where supported.

