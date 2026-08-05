## 11. Phase 1 - Evidence Preservation

Before cleanup:

1. Capture a site and host snapshot where technically and contractually possible.
2. Preserve WordPress files, configuration, database export and relevant logs separately.
3. Hash evidence packages with SHA-256.
4. Preserve metadata, ACLs and extended attributes when supported.
5. Record time synchronization and timezone configuration.
6. Capture current process list, open network listeners and active sessions when host access allows.
7. Preserve volatile evidence before reboot/restart where material.
8. Store evidence outside the compromised web root and restrict access.
9. Redact secrets in working reports but preserve originals in controlled evidence storage.

### Safe collection examples

Adapt paths and commands to the actual environment. Do not present example output as real output.

```bash
# Time and platform context
date --iso-8601=seconds
date -u --iso-8601=seconds
uname -a
id

# Versions
php -v
wp core version --path=/path/to/site --skip-plugins --skip-themes
mysql --version
nginx -v
apachectl -v

# File metadata and hashing
stat /path/to/suspicious-file.php
sha256sum /path/to/suspicious-file.php
find /path/to/site -xdev -type f -printf '%TY-%Tm-%TdT%TH:%TM:%TS %u %g %m %s %p\n' > filesystem-inventory.txt

# Evidence archive example - use a destination outside the web root
tar --acls --xattrs --numeric-owner -cpf /secure-evidence/site-files.tar /path/to/site
sha256sum /secure-evidence/site-files.tar > /secure-evidence/site-files.tar.sha256
```

Never overwrite the only copy of a suspicious file.

