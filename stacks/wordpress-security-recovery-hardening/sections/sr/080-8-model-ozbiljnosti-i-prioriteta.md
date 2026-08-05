## 8. Model Ozbiljnosti I Prioriteta

| Prioritet | Definicija | Primeri | Ciljna akcija |
| --- | --- | --- | --- |
| P0 - Kritično | Aktivna kompromitacija ili neposredna materijalna šteta | Aktivan webshell, payment skimmer, exfiltration podataka, zlonamerni admin, napadač kontroliše DNS/CDN, aktivna krađa kredencijala | Odmah containment, čuvanje dokaza i eskalacija vlasniku |
| P1 - Visoko | Putanja ponovne infekcije, velika izloženost ili nepodržana kritična platforma | Persistence, izvršivi writable uploads, izložene tajne, slabe admin kontrole, EOL PHP, napušten ranjiv plugin, SEO spam sa aktivnim backdoor-om | Rešiti pre normalnog production rada |
| P2 - Srednje | Bezbednosna slabost bez potvrđene aktivne kompromitacije | Nema 2FA, nepotpuni logovi, netestiran backup, prevelike privilegije, slabi headers | Planirana remediation akcija sa vlasnikom i rokom |
| P3 - Nisko | Dokumentacija, higijena ili optimizacija | Nedostaje runbook, zastareo inventar, manji hardening nedostatak | Dodati u backlog i pratiti |

Severity mora uzeti u obzir exploitability, kvalitet dokaza, izloženost, poslovni uticaj, osetljivost podataka i potencijal persistence-a. Ne smanjuj ozbiljnost samo zato što eksploatacija nije viđena u ograničenim logovima.

