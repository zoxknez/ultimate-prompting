## 12. Phase H - Tools, Plugins And MCP

### 12.1 Tool Contracts And Execution

1. Inventory each capability, owner, caller, scope, side effects, data accessed, and reversibility.
2. Use strict argument schemas and deterministic server-side validation.
3. Re-authorize every tool call against the authenticated actor, tenant, resource, and current state.
4. Apply allowlists for tools, commands, paths, hosts, protocols, destinations, and data classes.
5. Isolate filesystem, process, browser, network, and code execution.
6. Prevent SSRF, DNS rebinding, credential forwarding, local-network access, metadata-service access, path traversal, command injection, and unsafe deserialization.
7. Enforce timeouts, output-size limits, rate limits, concurrency limits, and cost budgets.
8. Use idempotency keys for retried side effects and compensating actions for partial failure.
9. Validate and sanitize tool output before it enters prompts, logs, UI, shell, SQL, HTML, templates, or downstream APIs.
10. Log invocation intent, authorization decision, arguments in redacted form, result status, approval, and side effects.

### 12.2 Human Approval And High-Impact Actions

1. Classify tools by impact and reversibility.
2. Require human confirmation for payment, deployment, deletion, publication, account or permission changes, external communication, sensitive export, shell, and other material side effects unless a formally approved automation policy exists.
3. Show the user an accurate action preview and destination before approval.
4. Re-request approval when parameters, resource, amount, recipient, environment, or action meaning changes.
5. Do not infer approval from a prior conversational statement unrelated to the exact action.
6. Test cancellation, timeout, duplicate approval, stale approval, and race conditions.

### 12.3 MCP-Specific Controls

1. Resolve the MCP specification version actually implemented and distinguish stable from draft or release-candidate features.
2. Verify OAuth and authorization behavior against the current normative specification.
3. Validate token audience and prohibit token passthrough.
4. Prevent confused-deputy behavior, privilege escalation, session hijacking, and cross-client state leakage.
5. Validate server identity, redirect URIs, origins, transport security, local binding, and remote endpoint trust.
6. Treat tool descriptions, resource content, prompts, sampling requests, elicitation, and server metadata as untrusted.
7. Detect capability changes and require review before exposing new or broadened capabilities.
8. Pin, verify, inventory, and monitor MCP server packages, images, binaries, and dependencies.
9. Test malicious or compromised MCP servers, poisoned tool metadata, oversized responses, invalid schemas, disconnects, retries, and partial results.
10. Document any use of experimental extensions and the rollback path.

