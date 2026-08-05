## Phase O - Execution Plans And Representative Workloads

Use actual plans and realistic data distributions; never optimize from query text alone.

- Capture parameterized and representative values, row estimates, actual rows, loops, timing, buffers and waits when safe.
- Compare cold, warm, common, rare, empty, large-tenant and skewed cases.
- Review join order, access paths, sort, hash, spill, temporary structures and parallelism.
- Detect parameter sensitivity, plan cache instability and prepared-statement generic/custom plan effects.
- Measure application end-to-end latency, not only server execution time.
- Store before/after plans and reject regressions in critical query classes.

