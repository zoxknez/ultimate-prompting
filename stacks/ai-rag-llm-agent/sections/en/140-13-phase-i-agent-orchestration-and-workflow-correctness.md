## 13. Phase I - Agent Orchestration And Workflow Correctness

1. Model the agent as a state machine with explicit states, transitions, ownership, and failure handling.
2. Define maximum steps, wall time, tokens, cost, tool calls, retries, recursion, subagents, and parallelism.
3. Implement stop conditions, loop detection, duplicate-work prevention, cancellation, and budget exhaustion behavior.
4. Verify planner, executor, critic, router, and subagent boundaries do not broaden authority.
5. Verify delegated tasks carry least-privilege identity, tenant context, budgets, and provenance.
6. Test stale state, conflicting parallel actions, duplicate events, out-of-order results, retries, and partial completion.
7. Require durable workflow semantics for long-running or externally visible actions.
8. Distinguish at-least-once delivery from exactly-once business effect.
9. Provide rollback or compensating actions for multi-step side effects.
10. Prefer deterministic workflows for known processes and use models only where judgment or language capability is needed.
11. Verify the final answer accurately reflects completed, failed, skipped, and pending actions.

