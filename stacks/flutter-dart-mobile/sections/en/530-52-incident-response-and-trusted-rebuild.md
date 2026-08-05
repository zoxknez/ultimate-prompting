## 52. Incident Response And Trusted Rebuild

Preserve evidence and restore trust before optimizing normal delivery.

- Define triggers for active compromise, credential leakage, signing-key compromise, malicious dependency, update-channel compromise, data exposure, crash loop, destructive migration, and widespread outage.
- Preserve repository state, CI logs, dependency resolution, generated output, build artifacts, signatures, store metadata, update metadata, telemetry, backend logs, device evidence, and timelines.
- Contain with the narrowest safe controls: revoke credentials, disable flags/routes, stop rollout, remove malicious artifacts, block versions, isolate services, and protect user data.
- Assess client-version reach, store propagation delay, offline devices, old installers, cached web assets, background jobs, tokens, and persisted malicious state.
- Revoke and rotate affected secrets, certificates, keys, tokens, signing identities, update keys, push credentials, and vendor access with dependency-aware sequencing.
- Rebuild from a verified commit in a clean trusted environment with re-resolved dependencies, reviewed generated code, new provenance, new signatures, and artifact comparison.
- Validate eradication, backward compatibility, user remediation, forced update or minimum-version policy, recovery of offline clients, and recurrence detection.
- Document decisions, approvals, communications, legal/privacy obligations, store/vendor coordination, residual risk, and follow-up ownership.
- Do not destroy evidence, clean compromised systems before capture, publish unverifiable fixes, or declare closure without trusted-build and operational proof.

