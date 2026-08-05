## 24. Phase S - Safe Repair And Verification

1. Fix the root cause, not only the visible symptom.
2. Make the smallest defensible change that closes the confirmed risk.
3. Add or update a focused regression test before or with each material fix.
4. Avoid unrelated formatting, mass renaming, dependency churn, and architecture rewrites.
5. Preserve public APIs, schemas, application ID, signing, user data, and behavior unless the approved repair requires change.
6. For migrations, back up representative data and test every supported upgrade path.
7. Re-run the original reproduction and the narrowest affected tests first.
8. Then run relevant module, variant, lint, unit, instrumented, release, R8, native, and device checks.
9. Verify negative and failure paths, not only the happy path.
10. Record changed files, rationale, commands, results, artifacts, rollback, and residual risk.
11. Re-check release behavior and production-equivalent configuration.
12. Update documentation, runbooks, baselines, test matrix, and release checklist.

