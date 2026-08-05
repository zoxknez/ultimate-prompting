<!-- section:STACK-WORDPRESS-OVERLAY-FOCUS -->
# WordPress Security Recovery & Hardening Stack Overlay

## Mandatory Incident & Hardening Domains

1. **Infection Isolation & Malware Scanning**:
   - Inspect `wp-config.php`, `.htaccess`, `index.php`, `wp-includes/`, mu-plugins, theme functions.
   - Scan for webshells, base64 obfuscation, rogue admin accounts, unauthorized cron events.

2. **Database & User Privilege Audit**:
   - Audit `wp_users` and `wp_usermeta` for unauthorized administrator privileges.
   - Verify table prefix, SQL injection vectors, and orphaned payload tables.

3. **Hardening & Recovery Controls**:
   - Disable file editing (`DISALLOW_FILE_EDIT`), force SSL admin (`FORCE_SSL_ADMIN`).
   - Audit plugin supply chain, REST API exposure, XML-RPC hardening, and backup/restore integrity.
