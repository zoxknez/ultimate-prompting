## 9. Phase E - Provider, Model And Runtime Configuration

1. Resolve the actual provider endpoints, models, aliases, versions, regions, and feature flags used in each environment.
2. Check lifecycle, deprecation, compatibility, model-card or system-card constraints, and provider-specific safety guidance from primary sources.
3. Verify timeouts, retries, backoff, rate limits, concurrency, quotas, maximum output, stop behavior, cancellation, and error mapping.
4. Verify deterministic tasks do not depend on unnecessary model calls.
5. Verify model routing cannot silently downgrade security, privacy, quality, context, tool support, or residency requirements.
6. Verify fallback behavior is explicit, observable, tested, and policy-compatible.
7. Test malformed responses, refusals, empty responses, partial streams, duplicate events, provider outages, and quota exhaustion.
8. Verify structured output uses strict schemas where appropriate and is still validated server-side.
9. Verify model-generated confidence is not treated as calibrated probability without evidence.

