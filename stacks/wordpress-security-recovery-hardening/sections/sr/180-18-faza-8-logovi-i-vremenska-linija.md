## 18. Faza 8 - Logovi I Vremenska Linija

Prikupi i koreliši, kada postoje:

- CDN/WAF zahteve i security events
- web server access i error logove
- PHP-FPM i application logove
- WordPress audit/security logove
- SSH authentication i sudo logove
- hosting panel login i file-manager logove
- FTP/SFTP logove
- database audit/general logove
- mail logove
- deployment i CI/CD logove
- DNS/registrar change history
- payment provider webhook i dashboard događaje
- Search Console security/manual-action istoriju

Napravi vremensku liniju:

```text
Timestamp UTC | Timestamp lokalno | Izvor | Akter/IP/nalog | Događaj | Asset | Evidence ID | Pouzdanost | Napomene
```

Uzmi u obzir rotaciju logova, prazne periode, NAT/CDN proxy, spoofable header-e i clock drift. Sačuvaj originalne logove pre normalizacije.

