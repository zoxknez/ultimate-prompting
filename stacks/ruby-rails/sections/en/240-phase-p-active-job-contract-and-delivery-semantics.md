## Phase P - Active Job Contract And Delivery Semantics

- Identify the real adapter in each environment and process; development `:async` behavior is not production durability evidence.
- Assume at-least-once delivery unless stronger semantics are proven end to end.
- Audit serialization, GlobalID lookup, missing records, schema evolution, old code consuming new arguments and new code consuming old jobs.
- Define retry classes, backoff, jitter, maximum attempts, discard rules, poison handling and operator workflow.
- Make job effects idempotent at the database or external-system boundary, not only by checking a flag in memory.
- Measure queue age, execution time, retries, failures, saturation and downstream pressure by queue and job class.

