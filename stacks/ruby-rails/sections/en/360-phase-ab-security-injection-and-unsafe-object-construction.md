## Phase AB - Security, Injection And Unsafe Object Construction

- Audit SQL, shell, command, template, HTML, JavaScript, CSS, header, log, LDAP and expression injection paths.
- Review `html_safe`, `raw`, `sanitize`, dynamic SQL, Arel fragments, `send`, `constantize`, `eval`, `instance_eval` and metaprogramming from input.
- Reject untrusted `Marshal.load`, unsafe YAML, arbitrary object deserialization and signed-data assumptions without key and purpose separation.
- Audit open redirects, host authorization, request forgery, file disclosure, path traversal, ReDoS and resource-exhaustion endpoints.
- Triage Brakeman and dependency advisories with reproduction and framework-version context; never ignore or auto-fix blindly.

