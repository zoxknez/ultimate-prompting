## 10. Phase F - Prompt And Instruction Architecture

1. Inventory system, developer, user, tool, retrieval, memory, and hidden instructions.
2. Verify instruction precedence is intentional, documented, and tested.
3. Separate trusted control instructions from untrusted data using structural channels and typed fields, not only natural-language delimiters.
4. Remove secrets, authorization policy, hidden business rules, and sensitive internal data from prompts where deterministic controls are required.
5. Validate prompt variables, template escaping, localization, and truncation behavior.
6. Test direct, indirect, multi-turn, encoded, obfuscated, multilingual, multimodal, and tool-result prompt injection.
7. Test instruction collisions caused by retrieved documents, emails, web pages, file metadata, OCR, comments, alt text, code, and tool descriptions.
8. Verify refusal, escalation, and safe-completion logic is enforced outside the model where required.
9. Version prompts and tie every production response and evaluation to a prompt revision.
10. Require review and regression evaluation for prompt changes.

