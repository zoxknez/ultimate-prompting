## 18. Phase 8 - Logs And Timeline

Collect and correlate, when available:

- CDN/WAF requests and security events
- web server access and error logs
- PHP-FPM and application logs
- WordPress audit/security logs
- SSH authentication and sudo logs
- hosting panel login and file-manager logs
- FTP/SFTP logs
- database audit/general logs
- mail logs
- deployment and CI/CD logs
- DNS/registrar change history
- payment provider webhook and dashboard events
- Search Console security/manual-action history

Create a timeline with:

```text
Timestamp UTC | Timestamp local | Source | Actor/IP/account | Event | Asset | Evidence ID | Confidence | Notes
```

Account for log rotation, missing periods, NAT/CDN proxying, spoofable headers and clock drift. Preserve original logs before normalization.

