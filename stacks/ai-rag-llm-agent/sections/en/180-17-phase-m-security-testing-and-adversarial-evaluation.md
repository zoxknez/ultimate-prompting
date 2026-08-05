## 17. Phase M - Security Testing And Adversarial Evaluation

Build a threat-driven test suite using applicable current guidance from OWASP, MITRE ATLAS, NIST, provider security documentation, and the MCP specification.

Test at least:

1. Direct and indirect prompt injection.
2. System-prompt and secret extraction attempts.
3. Cross-tenant retrieval and memory access.
4. Data and RAG poisoning.
5. Tool-description, tool-output, and MCP-server poisoning.
6. Excessive agency and approval bypass.
7. Privilege escalation and confused-deputy flows.
8. SSRF, unsafe egress, browser exfiltration, and link-based attacks.
9. Code, shell, SQL, template, and rendering injection.
10. Denial of service, token exhaustion, recursive loops, and cost harvesting.
11. Supply-chain compromise of models, datasets, packages, prompts, tools, and MCP servers.
12. Unsafe fallback, fail-open behavior, stale policy, and disabled controls.
13. Multilingual, encoded, obfuscated, multi-turn, and multimodal attacks.
14. Social-engineering attacks that preserve plausible user intent while manipulating action selection.

For each case, record preconditions, expected policy, actual behavior, impact, and mitigation effectiveness.

