# Contributing

## Goals

- Keep prompts **truth-first** and executable by agents.
- Keep **EN/SR pairs** semantically aligned.
- Keep version tables **verifiable** (line + official URL; no invented patches).

## Editing prompts

1. Prefer fixing both `.en.md` and `.sr.md` in the same PR.
2. Do not invent unpublished package versions. Prefer:
   - major/minor **line** + “re-check official source at audit time”, or
   - a patch only when cited with source URL and verification date.
3. Update `baselines/sources.json` when changing version claims.
4. Run local checks:

```bash
python scripts/check_parity.py
python scripts/check_baselines.py
```

## Architecture direction (v1)

Prefer composition over mega-monoliths:

```text
core/*          shared operating contract
stacks/*        technology overlays
modes/*         work-mode overlays
*-audit-prompt.*.md   entry prompts (may stay long for convenience)
```

Large stacks (Go/Rust, .NET, Java) should eventually load **core + overlay** instead of one 600-line blob.

## Pull requests

- Small, focused PRs.
- Note which official sources were checked and when.
- No secrets in diffs.

## Commit style

```text
fix: correct MySQL baseline wording
docs: honest v0.9 readiness status in README
feat: reconstruct python-pyside6 full audit contract
```
