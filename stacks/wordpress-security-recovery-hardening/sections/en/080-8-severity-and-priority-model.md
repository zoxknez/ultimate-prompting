## 8. Severity And Priority Model

| Priority | Definition | Examples | Target action |
| --- | --- | --- | --- |
| P0 - Critical | Active compromise or immediate material harm | Active webshell, payment skimmer, data exfiltration, malicious admin, attacker-controlled DNS/CDN, ongoing credential theft | Immediate containment, evidence capture and owner escalation |
| P1 - High | Reinfection path, major exposure or unsupported critical platform | Persistence, writable executable uploads, exposed secrets, weak admin controls, EOL PHP, vulnerable abandoned plugin, SEO spam with active backdoor | Resolve before normal production operation |
| P2 - Medium | Security weakness without confirmed active compromise | Missing 2FA, incomplete logging, weak backup testing, excessive privileges, insecure headers | Scheduled remediation with owner and date |
| P3 - Low | Documentation, hygiene or optimization | Missing runbook, stale inventory, minor hardening improvement | Backlog and track |

Severity must reflect exploitability, evidence, exposure, business impact, data sensitivity and persistence potential. Do not lower a finding only because exploitation was not observed in limited logs.

