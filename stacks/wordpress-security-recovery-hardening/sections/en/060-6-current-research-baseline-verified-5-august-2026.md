## 6. Current Research Baseline - Verified 5 August 2026

Treat this as a dated snapshot, not permanent truth. Re-check official sources before using version-specific advice.

| Component | Verified baseline | Required interpretation |
| --- | --- | --- |
| WordPress | Latest stable: 7.0.2, released 17 July 2026 as a critical/high security release with forced updates enabled for affected sites | Re-check the release archive before remediation. Only the newest 7.0 release is actively maintained; older backports are courtesy coverage, not a long-term support guarantee. |
| Upcoming WordPress | 7.1 planned for 19 August 2026 | Never recommend a future or pre-release build for production incident recovery unless explicitly requested for testing. |
| PHP recommendation | WordPress recommends PHP 8.3 or greater | Prefer a currently supported PHP branch that is compatible with all required plugins/themes and validated in staging. |
| PHP minimum | WordPress 7.0 supports PHP 7.4 minimum | PHP 7.4 is EOL and is not an acceptable long-term production target. Treat it as P1 technical debt or higher when exposed. |
| PHP upstream support | PHP 8.2-8.5 are supported on the verification date; 8.2 and 8.3 receive security fixes only, while 8.4 and 8.5 remain in active support | Re-check php.net. Prefer an active-support branch where compatibility permits and treat EOL PHP as a blocking production risk. |
| Database recommendation | MySQL 8.0+ or MariaDB 10.11+ | Confirm host and plugin compatibility before migration. Legacy database support does not equal a secure baseline. |
| Web transport | HTTPS support required/recommended | Confirm end-to-end HTTPS, origin validation and secure cookies, not only CDN-fronted HTTPS. |
| Incident response | NIST SP 800-61 Rev. 3 final, April 2025 | Integrate preparation, detection, response, recovery and lessons learned into risk management. |
| Checksums | WP-CLI can verify WordPress core and repository plugin checksums | Checksum success is only one signal and does not cover database, uploads, MU plugins, custom/premium code, host or edge persistence. |

Mandatory official re-check sources:

- https://wordpress.org/download/releases/
- https://wordpress.org/about/requirements/
- https://developer.wordpress.org/advanced-administration/security/hardening/
- https://developer.wordpress.org/cli/commands/core/verify-checksums/
- https://developer.wordpress.org/cli/commands/plugin/verify-checksums/
- https://www.php.net/supported-versions.php
- https://csrc.nist.gov/pubs/sp/800/61/r3/final

For each external claim in the final report, record source URL, page title, access date and the fact it supports.

