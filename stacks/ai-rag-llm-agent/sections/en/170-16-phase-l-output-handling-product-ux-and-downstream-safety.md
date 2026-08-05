## 16. Phase L - Output Handling, Product UX And Downstream Safety

1. Treat model output as untrusted data.
2. Validate structured outputs against strict schemas and business rules.
3. Encode or sanitize output for HTML, Markdown, SQL, shell, code, email, documents, logs, and other sinks.
4. Prevent XSS, template injection, command injection, unsafe links, formula injection, and downstream prompt injection.
5. Clearly distinguish generated, retrieved, inferred, and verified content.
6. Show citations and evidence at the level needed for the use case.
7. Provide uncertainty, limitations, and escalation paths without deceptive confidence.
8. Verify accessibility, localization, streaming states, cancellation, partial answers, retries, and error recovery.
9. Prevent the UI from implying an action succeeded before the authoritative backend confirms it.
10. Verify regulated or high-impact decisions have appropriate human oversight and explanation paths.

