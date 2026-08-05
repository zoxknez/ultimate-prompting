## Phase T - Puma, Rack Server And Process Lifecycle

- Verify server version, Rack compatibility, bind addresses, TLS termination, proxy protocol, request parser and reverse-proxy assumptions.
- Calculate worker and thread topology per host, pod or dyno and compare it with CPU, memory, database, cache and external connection limits.
- Verify `preload_app!`, copy-on-write, worker boot hooks, fork safety, connection re-establishment and background thread handling.
- Test phased restart, rolling restart, graceful shutdown, drain, keep-alive, streaming, websocket and long-request behavior.
- Confirm health probes distinguish process alive, ready for traffic and dependencies degraded without causing an outage cascade.
- Apply equivalent lifecycle analysis to Passenger, Unicorn, Falcon, serverless adapters or custom Rack servers.

