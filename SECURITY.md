# Security Policy

## What this repository is

This repository contains **prompt text** for AI coding agents. It is not an application runtime.

## Reporting issues

If you find:

- a prompt that instructs unsafe destructive defaults,
- a prompt that would leak secrets into reports,
- incorrect security guidance that could cause harm,

open a GitHub issue with the prompt filename, section, and a safe reproduction description.

**Do not** open issues containing real secrets, production dumps, or private keys.

## Secrets

Never commit:

- `.env` files, API keys, keystores, PFX/P12, Apple API keys,
- update signing private keys, cloud tokens, or customer data.

Prompts require agents to **redact** secrets and treat anything in client binaries as potentially public.

## Supply chain

When using these prompts against real projects, prefer:

- locked dependencies,
- official package registries,
- verified container digests,
- isolated CI credentials (no PR access to release/signing secrets).
