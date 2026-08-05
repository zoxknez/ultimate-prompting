## 20. Faza 10 - Root-Cause Analiza

Za svaku moguću initial-access putanju navedi:

- hipotezu
- dokaz koji je podržava
- dokaz koji joj protivreči
- dokaz koji nedostaje
- nivo pouzdanosti
- pogođeni vremenski period
- remediation koja zatvara putanju

Proceni najmanje:

- ranjiv ili napušten plugin/tema
- ukradeni WordPress kredencijali
- ukradeni hosting/FTP/SSH kredencijali
- reused lozinka ili nedostatak MFA
- ranjiv susedni sajt na istom nalogu
- nebezbedan custom kod ili upload endpoint
- izložen backup/configuration fajl
- kompromitovan developer računar
- kompromitovan CI/CD ili dependency supply chain
- zlonamerni insider ili vendor pristup
- DNS/CDN/registrar kompromitacija

Ne mešaj prvi pronađeni zlonamerni fajl sa initial-access vektorom.

