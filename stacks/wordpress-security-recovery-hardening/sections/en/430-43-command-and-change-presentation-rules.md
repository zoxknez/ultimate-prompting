## 43. Command And Change Presentation Rules

When commands are requested:

1. Start with environment detection and read-only inspection.
2. Use placeholders for paths, domains, usernames and table prefixes.
3. Explain prerequisites and expected impact.
4. Provide a dry-run or listing command before mutation where possible.
5. Provide backup and rollback steps.
6. Use `set -euo pipefail` only when the command sequence is understood and partial execution is safe.
7. Quote paths and variables defensively.
8. Do not place secrets in shell history.
9. Do not chain destructive commands with broad wildcards.
10. Label commands as:
   - `READ-ONLY`
   - `CONTAINMENT`
   - `DESTRUCTIVE/REQUIRES APPROVAL`
   - `ROLLBACK`
   - `VERIFICATION`

