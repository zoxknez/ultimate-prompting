## 24. Faza 14 - Verifikacija I Praćenje Ponovne Infekcije

Verifikacija mora uključiti nezavisan dokaz, a ne samo odsustvo vidljivih simptoma.

### Tehnička verifikacija

- ponovi core i repository-plugin checksum provere
- ponovi filesystem inventar i uporedi razlike
- ponovo skeniraj sve izvršive i script lokacije
- potvrdi users, application passwords, cron, systemd, SSH keys, DB triggers/events i CDN rules
- potvrdi da PHP nije izvršiv u zabranjenim direktorijumima
- potvrdi prikupljanje logova i alert-e
- testiraj authenticated i unauthenticated sesije
- testiraj različite user-agent i referrer vrednosti radi conditional malware/SEO spam-a
- testiraj direktan origin i CDN putanje kada je ovlašćeno
- proveri Search Console i javne search rezultate
- proveri payment stranice zbog neovlašćenih skripti i network zahteva

### Periodi monitoringa

Monitoring definiši prema riziku, a ne kao garantovano pravilo od 24-72 sata:

- intenzivno praćenje: prvih 24-72 sata
- pojačano praćenje: 7-14 dana
- normalni dugoročni monitoring: stalno

Prati izmene fajlova, privilegovane login-e, neuspešne login-e, nove korisnike, plugin/theme izmene, cron izmene, nagle skokove outbound mail-a, WAF događaje, neobične POST zahteve, PHP greške, DNS/CDN izmene i search-index anomalije.

