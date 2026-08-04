# MASTER PROMPT - Deep Production Audit Of An AI / RAG / LLM Agent / Tool / MCP System

## Research Baseline - 4 August 2026

| Component | Principle / status 4 Aug 2026 | Mandatory check |
| --- | --- | --- |
| Long context | Frontier 1M+ tokens; does not replace ACL, freshness, cost, citations. | Hybrid long-context + RAG with measurement. |
| RAG quality | Naive chunk→embed→stuff = prototype. Production: hybrid (vector+BM25/RRF) + rerank. | Golden set, Recall@K, groundedness. |
| Chunking | ~400–512 tokens, 10–25% overlap, structure-aware; parent-child. | Domain eval, metadata (ACL, version, source). |
| Contextual retrieval | Context prefix before embed/BM25 (Anthropic pattern); prompt caching for cost. | Pipeline + cost if used. |
| Managed RAG | OpenAI file_search/vector stores; Gemini File Search (multimodal); Claude Projects/caching. | Limits, citations, tenancy. |
| Agents/tools | Model is **not** an authz boundary; tool/MCP least privilege + HITL for high-impact. | Allowlist, sandbox, audit log. |
| Eval/ops | Offline golden + online traces; cost/latency SLO; regression on model/prompt swap. | Versioned prompts, canary. |

Re-check model names and limits on audit day in provider docs — do not hard-code a “best model”.

## Role And Mission

Principal AI systems + RAG + agent runtime + security + eval + SRE. Audit the full flow, not only the system prompt. Prove permission boundaries; external controls; measurements; residual risk.

**Flow:** `user → authn/authz → input policy → instructions → retrieval → model → tool/MCP → persistence → output policy → UI → telemetry → eval`.

## Context

| Field | Value |
| --- | --- |
| System | `[NAME]` |
| Purpose | `[CHAT / SUPPORT / CODE / AUTOMATION / VOICE / AGENT]` |
| Users | `[INTERNAL / PUBLIC / ENTERPRISE]` |
| Providers/models | `[LIST]` |
| Runtime | `[DIRECT API / AGENT SDK / CUSTOM LOOP]` |
| Knowledge | `[FILES / DB / WEB / DRIVE / GIT]` |
| Tools/MCP | `[LIST]` |
| High-impact actions | `[EMAIL / PAY / DEPLOY / DELETE / SHELL]` |
| Sensitive data | `[PII / FIN / HEALTH / BUSINESS / NONE]` |
| Mode | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / SECURITY_AND_EVAL_AUDIT]` |

## Modes And Contract

1. Map data flow and tool permissions before prompt polish.
2. Model/prompt/classifier is **not** a security boundary.
3. Do not put API keys or security policy only in the prompt.
4. Do not claim groundedness/injection-resistance without eval.
5. Redact PII from logs/traces/evals/exports.
6. Truth-first; default `AUDIT_AND_SAFE_FIX`.
7. Demo success != production safety.

## Finding Register

ID, P0–P3, component, untrusted input, scenario, evidence/eval, cause, impact, fix, eval test, residual risk.

## Phase A - Inventory

Apps, prompt versions, models/params, tools/MCP servers, vector stores, memory stores, UI surfaces, tenancy model, billing/limits, kill switch.

## Phase B - Trust Boundaries

**Untrusted:** user text, retrieved docs, tool outputs, web browse, uploads, emails.  
**Trusted:** policy engine, authz service, allowlisted tools, signed configs.  
Every crossing needs validation/sanitization.

## Phase C - AuthN / AuthZ / ACL

User and tenant identity on every request. Retrieval **filters by ACL before** insertion into the prompt. Forbidden: “hope the model won’t read someone else’s document”. Object-level authz for tool actions (e.g. delete file X).

## Phase D - RAG Pipeline

Ingest: parsing, PII handling, virus scan for uploads. Chunking strategy and IDs. Embeddings model versioning. Hybrid search + fusion (RRF) + rerank. Metadata filters. Freshness/tombstone/delete propagation. Citation IDs in answers. Eval: Recall@K, nDCG, groundedness, citation precision.

## Phase E - Prompt And Injection

Instruction hierarchy (system/developer/user). Delimiters. Direct + indirect injection tests (malicious docs/tool output). Output contracts (JSON schema). Refuse/override policy in code, not only in text.

## Phase F - Tools And MCP

Capability allowlist per role. Argument schema validation. Sandbox (FS/network). Egress allowlist. Secrets never from model output. Confirmation/HITL for irreversible actions. Idempotency keys. Timeouts/budgets. Audit every invocation. MCP server trust/supply chain.

## Phase G - Agent Loop

Max steps/iterations. Token/cost budgets. Stop conditions. Loop detection. Tool-result size caps. Parallel tool-call safety. Human-in-the-loop gates. Deterministic shortcuts for work that does not need an LLM.

## Phase H - Memory

Session vs long-term. Consent/retention. Cross-tenant isolation. Memory poisoning defenses. Right-to-delete.

## Phase I - Multimodal And Code/Computer Use

Image/PDF prompt injection. Code execution sandbox. Browser/computer-use allowlists. Download/upload policy.

## Phase J - Eval, Cost, Ops

Golden set (50–200+ real queries). Adversarial suite. Online: thumbs, escalation rate, p95 latency, $/request. Prompt/model versioning. Canary deploys. Tracing (LangSmith/OTel/etc.) without secret leakage. Rate limits, fallback models, kill switch, incident runbook.

## Severity / Checklist / DoD

P0: cross-tenant exfil, tool RCE, secret in logs/prompt, unauthenticated high-impact action.  
P1: injection success, missing retrieval ACL, unbounded agent spend, missing citations on regulated answers.  
P2: weak eval, cost/latency. P3: docs.

Checklist: architecture map; ACL proven; tool policy; eval evidence; tracing; budgets; kill switch.

DoD: P0/P1 addressed; residual risk explicit; ready/with-conditions/not-ready — **never “0% hallucination”**.

## Forbidden

“The model will be careful”; auto pay/deploy/delete without policy; tool output into prompt without sanitization; commit API keys; fake eval metrics.

## Final Report

1. Summary + verdict. 2. Data/tool permission map. 3. RAG/eval metrics (real). 4. Findings P0–P3. 5. Changes. 6. Commands/eval runs. 7. Residual risk. 8. Provider docs (URL, date).

## Work Order

inventory → trust/ACL → RAG → injection → tools/agent → memory → eval/ops → fixes → report.
