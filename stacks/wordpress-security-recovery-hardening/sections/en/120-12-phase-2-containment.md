## 12. Phase 2 - Containment

Contain the threat without unnecessarily destroying evidence.

Evaluate and document:

- origin access restrictions
- CDN/WAF challenge or deny rules
- temporary authenticated maintenance response
- selective disabling of checkout, forms, XML-RPC, REST routes, uploads or registration
- WordPress file editor disablement
- temporary filesystem write restrictions
- removal of public execution rights from upload directories
- revocation of suspicious sessions and API/application passwords
- suspension of unknown administrators
- isolation of compromised plugins/themes
- blocking known malicious IPs only when useful and not treated as full remediation

Containment is not eradication. A maintenance page alone is insufficient if the origin, API, uploads, cron, admin-ajax, XML-RPC or direct PHP paths remain accessible.

