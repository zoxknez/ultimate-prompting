# Validation Report - Library 2.1.0 (Maintenance Architecture Rework)

Validation date: 2026-08-05
Repository: Ultimate Production Audit Prompt Library

## Scope

This report covers the 16 active English/Serbian prompt pairs, their frontmatter, structural parity,
composition determinism against the frozen `v2.0.0` archive, source manifests, baseline hardcode rules,
and the mock-provider eval regression suite. It intentionally contains only aggregated results - no
holdout case content, raw model output, or per-finding adjudication detail (there is no private holdout
suite yet; see Known Limitations).

## Content vs. Architecture

**No prompt content changed.** All 32 root `*.en.md` / `*.sr.md` files are byte-identical to the tagged
`v2.0.0` release - verified mechanically (`compose.py --check`), not asserted. What changed is how the
library is built and maintained: each prompt is now composed from `stacks/<id>/sections/<locale>/` pieces
split at the original heading boundaries with zero rewording, plus one proven shared module. See
`CHANGELOG.md` for the full breakdown. Per the release-versioning rule this repository committed to
(byte-identical content, additive-only tooling change), this is `2.1.0`, not a breaking `3.0.0`.

## Automated Checks

The full release gate (`python scripts/validate_release.py --static`) runs, in order:

```bash
python scripts/check_integrity.py
python scripts/check_parity.py
python scripts/check_baselines.py
python scripts/compose.py --check-lock
python scripts/compose.py --check
python scripts/check_section_loss.py
python scripts/check_eval_coverage.py
python scripts/run_evals.py --suite regression --provider mock
```

All eight passed on this validation date. `evals/sandbox.py --verify` was also run separately and passed.

### Integrity checker coverage

- exactly 16 active EN/SR pairs
- matching prompt version metadata; version 2.0.0 for every active pair's content
- English and Serbian language declaration
- equal line count, line-shape sequence, and H1-H3 heading-depth sequence within each pair
- balanced fenced code blocks; valid YAML frontmatter
- referenced JSON source manifest existence and parseability
- no en dash, em dash, or non-breaking hyphen in Serbian prompts

### Composition and section-loss coverage

- `compose.py --check`: all 32 files reconstruct byte-for-byte from their `stacks/<id>/sections/` pieces
- `compose.py --check-lock`: `COMPOSITION_LOCK.json` input hashes match the current tree exactly
- `check_section_loss.py`: every one of the 1,856 section-ids recorded in
  `archive/v2.0.0/SECTION_INVENTORY.json` (across all 16 stacks, both locales) is present verbatim in the
  reconstruction - 0 lost

### Eval regression coverage

- 18 public fixture packages across 16 stacks, run through `evals/providers/mock.py`
- `run_evals.py` gates on recall = 100%, precision = 100%, and zero forbidden-finding hits per fixture -
  it fails loudly on any regression, not just on a crash
- 1 fixture (`NEXT-INJECTION-001`) is tagged `injection_test: true`; `repository_instruction_resistance_rate`
  is reported separately for this category (see Known Limitations for what this number does and does not
  prove under the mock provider)

## Results

- active prompt pairs: 16
- active prompt files: 32
- total active prompt lines: 31,606
- structural parity failures: 0
- frontmatter failures: 0
- source-manifest JSON failures: 0
- composition byte-equivalence failures: 0 / 32
- section-ids lost vs. v2.0.0 archive: 0 / 1,856
- public eval fixtures passing (mock provider): 18 / 18
- verified shared contract modules: 1 (`contracts/evidence/finding-status-vocabulary-standard.{en,sr}.md`,
  extracted only after confirming byte-identical meaning across both locales for the 2 stacks that use it)

## Integrity Artifacts

- `PROMPT_CATALOG.json`: version, line count, heading count, and SHA-256 for every active prompt file.
- `MANIFEST.sha256`: SHA-256 hashes for release-relevant repository files, regenerated from the current tree.
- `COMPOSITION_LOCK.json`: input-hash lock over every file that participates in composing a prompt.
- `archive/v2.0.0/SECTION_INVENTORY.json`: the frozen structural baseline `check_section_loss.py` proves against.
- `reviews/` contains a Serbian revision report for every package (unchanged from v2.0.0).
- `baselines/` contains dated primary-source manifests, now correctly pointed to by `baselines/index.json`.

## Known Limitations

- Automated structural parity does not prove perfect semantic translation.
- Structural parity does not prove every external URL stays available or every framework behavior is
  unchanged - `check_source_links.py` runs daily in CI for the former; nothing automates the latter.
- The 18 public fixtures are run only against a deterministic mock provider that returns a synthetic
  finding and never reads fixture file content. This proves the harness plumbing works (schema validation,
  scoring, gating, aggregation) - it does not measure real audit quality on any real model. Live
  `openai`/`anthropic` provider adapters exist (`evals/providers/`) but have not been exercised against a
  real API key by this repository's own tooling.
- `repository_instruction_resistance_rate` on the mock provider is 100% only because the mock provider
  never reads the embedded injected instruction in the first place - it is not evidence that any real
  model resists prompt injection. A meaningful result requires a live-provider run.
- Only 2 of 16 stacks (`ai-rag-llm-agent`, `android-master`) have a proven shared contract module. The
  other 14 were independently authored and differ in structure and (for stacks like
  `wordpress-security-recovery-hardening`) evidence-model semantics - most content remains intentionally
  stack-local rather than forced into false uniformity.
- There is no private holdout suite, no multi-provider statistical comparison run, and no completed
  fixture set at the scale described in early planning (64 public + 16 holdout, 8+ approved P0 / 16+ P1).
  `evals/harness.py` now supports multi-run statistical aggregation (`run_evals.py --runs N`) and the
  safe-fix sandbox (`evals/sandbox.py`) now really applies patches and executes verification commands via
  subprocess, rather than reporting a hardcoded pass - but both need real fixture content and a live
  provider to produce a meaningful signal at scale.

## Release Decision

`READY FOR USE AS A PRODUCTION-CANDIDATE PROMPT LIBRARY WITH DOCUMENTED LIMITATIONS.` The prompt content
itself is unchanged from the validated v2.0.0 release. The maintenance architecture and eval/safe-fix
infrastructure built in this cycle are verified to do what they claim - real byte-equivalence, real
section-loss checking, real patch application, real subprocess-based verification - but the harness has
not yet been run at scale against a live model, and the fixture set is not yet large enough to support the
full release-threshold matrix (macro/micro recall and precision, per-stack P0/P1 recall, hallucination and
unsupported-finding rates) that a v2.1.0 GA release should ultimately be gated on.
