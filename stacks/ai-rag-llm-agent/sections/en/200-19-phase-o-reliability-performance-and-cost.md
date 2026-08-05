## 19. Phase O - Reliability, Performance And Cost

1. Measure end-to-end and component-level latency, including time to first token, retrieval, reranking, tool calls, queues, and retries.
2. Measure token use, cache hit rate, provider cost, tool cost, storage cost, and cost per successful business outcome.
3. Test provider outage, regional failure, rate limiting, quota exhaustion, slow tools, malformed streams, dropped connections, and partial responses.
4. Verify backpressure, queue limits, concurrency control, circuit breakers, bulkheads, cancellation, and load shedding.
5. Prevent retry storms, duplicate side effects, runaway agents, and uncontrolled context growth.
6. Define SLOs, error budgets, budgets per user or tenant, and graceful degradation.
7. Verify caching does not leak data, bypass freshness, preserve deleted content, or mix prompt and authorization contexts.
8. Load test realistic multi-turn and tool-using workloads, not only single model calls.
9. Verify capacity and cost assumptions against measured data.

