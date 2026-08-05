## 20. Phase P - Observability, Auditability And Incident Response

1. Trace the request across identity, policy, retrieval, model, tool, workflow, state, and output boundaries.
2. Record model, prompt, retrieval, tool, policy, dataset, and deployment versions.
3. Use current OpenTelemetry GenAI conventions or an explicitly documented equivalent where suitable, while respecting their stability status.
4. Do not record full prompts, completions, retrieved documents, tool arguments, or memory by default when they may contain sensitive data.
5. Implement redaction, sampling, access controls, retention, and secure export for telemetry.
6. Log authorization and approval decisions separately from model reasoning.
7. Monitor injection signals, policy violations, unusual tool use, exfiltration patterns, token spikes, loops, latency, errors, and model or retrieval drift.
8. Define alerts, owners, escalation, triage, containment, evidence preservation, notification, and post-incident review.
9. Test kill switches for models, tools, retrieval, memory writes, and autonomous actions.
10. Verify backup, restore, replay, rollback, and disaster-recovery procedures.
11. Maintain a runbook for compromised prompts, poisoned corpora, leaked secrets, malicious MCP servers, provider incidents, and unsafe model regressions.

