## 6. Phase B - Architecture, Data Flow And Trust Boundaries

1. Draw the actual request and state flow, including asynchronous and retry paths.
2. Mark every trust boundary, data store, external dependency, and privilege transition.
3. Classify inputs as trusted, authenticated-but-untrusted, third-party, model-generated, retrieved, or operator-controlled.
4. Track tenant and user identity through the full chain, including queues, caches, traces, tool calls, and background jobs.
5. Identify where context is merged, truncated, summarized, cached, or persisted.
6. Identify control-plane versus data-plane functions.
7. Prove where deterministic validation, authorization, policy enforcement, and output encoding occur.
8. Flag any boundary that relies only on model compliance.

