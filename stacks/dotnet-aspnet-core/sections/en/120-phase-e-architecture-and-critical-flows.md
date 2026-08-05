## Phase E - Architecture And Critical Flows

Map: HTTP/gRPC/SignalR entries, message consumers, background workers, schedulers, application/use-case layer, domain, persistence, integration adapters, cache, events, security and transaction boundaries, deployment units.

For each critical flow: `entry → authentication → validation → authorization → use case → transaction → database/cache/broker/external service → response → telemetry`.

Establish actual state (monolith / modular monolith / services). Do not recommend microservices merely because there are many projects. Check cycles, domain → infrastructure dependency, shared databases across services, deployment coupling, and unclear data/event ownership.

A controller/Minimal API handler must not own business logic, manage transactions directly, return EF entities, or trust fields the client must not set — unless that is explicit and tested. Do not introduce mediator/CQRS/Minimal APIs/Native AOT merely because they are popular.

