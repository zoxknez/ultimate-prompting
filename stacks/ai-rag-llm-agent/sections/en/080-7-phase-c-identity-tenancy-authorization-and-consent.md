## 7. Phase C - Identity, Tenancy, Authorization And Consent

1. Verify authentication on every externally reachable and internal privileged path.
2. Verify tenant context cannot be supplied or overridden by untrusted input.
3. Test object-level and action-level authorization for retrieval, tools, memory, exports, admin actions, and background jobs.
4. Apply retrieval ACL filters before candidate content is made available to the model.
5. Test post-filtering bypasses, metadata loss, cache leakage, shared-index leakage, and cross-tenant joins.
6. Verify least-privilege scopes for provider APIs, cloud identities, OAuth, MCP, databases, storage, browser sessions, and code execution.
7. Verify consent, disclosure, and revocation for memory, personalization, recording, transcription, and high-impact actions.
8. Verify approvals cannot be replayed, widened, substituted, or reused after parameters change.
9. Include positive and negative authorization tests.

