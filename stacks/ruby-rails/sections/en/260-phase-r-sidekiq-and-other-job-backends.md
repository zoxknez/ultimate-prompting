## Phase R - Sidekiq And Other Job Backends

- For Sidekiq, verify Redis or Valkey durability, namespaces, eviction policy, network timeouts, pool sizing, concurrency and shutdown.
- Audit server and client middleware, retry sets, scheduled sets, dead sets, uniqueness plugins and Web UI exposure.
- Ensure job classes and all dependencies are thread-safe under the configured concurrency and runtime.
- For GoodJob, Delayed Job, Resque, Shoryuken or custom workers, document actual acknowledgement, visibility, locking, retry and shutdown semantics.
- Never infer exactly-once execution from a uniqueness plugin or queue backend marketing claim.

