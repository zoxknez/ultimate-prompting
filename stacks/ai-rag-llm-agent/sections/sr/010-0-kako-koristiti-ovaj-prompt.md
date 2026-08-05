## 0. Kako Koristiti Ovaj Prompt

### 0.1 Obavezni Ulazi

Prikupi ili izvedi i eksplicitno zabelezi:

| Polje | Vrednost |
| --- | --- |
| Sistem ili repozitorijum | `[NAME / PATH / URL]` |
| Poslovna namena | `[PURPOSE]` |
| Korisnici | `[INTERNAL / PUBLIC / ENTERPRISE / REGULATED]` |
| Deployment okruzenja | `[LOCAL / DEV / STAGING / PROD]` |
| AI provideri i modeli | `[LIST OR UNKNOWN]` |
| Runtime i orkestracija | `[DIRECT API / SDK / CUSTOM LOOP / WORKFLOW ENGINE]` |
| Izvori znanja | `[FILES / DB / WEB / DRIVE / GIT / OTHER]` |
| Vector, search i memory skladista | `[LIST OR UNKNOWN]` |
| Alati, plugini, MCP serveri i subagenti | `[LIST OR UNKNOWN]` |
| High-impact akcije | `[EMAIL / PAYMENT / DEPLOY / DELETE / SHELL / ACCOUNT / OTHER]` |
| Osetljivi podaci | `[PII / FINANCIAL / HEALTH / LEGAL / BUSINESS / SECRETS / NONE]` |
| Tenancy model | `[SINGLE-TENANT / MULTI-TENANT / UNKNOWN]` |
| Compliance opseg | `[EU AI ACT / GDPR / HIPAA / PCI / SOC 2 / ISO / OTHER / NONE / UNKNOWN]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / SECURITY_AND_EVAL_AUDIT]` |

### 0.2 Pravilo Za Nedostajuce Informacije

Ne blokiraj ceo audit zato sto neki ulazi nedostaju.

1. Zakljucke izvodi samo iz repozitorijuma, konfiguracije, runtime dokaza i autoritativne dokumentacije.
2. Svaku neresenu pretpostavku oznaci kao `UNVERIFIED`.
3. Nastavi sa bezbednim read-only proverama gde je moguce.
4. Trazi samo pristup koji sustinski blokira potvrdu, popravku ili verifikaciju.
5. Nedostatak dokaza nikada ne pretvaraj u pozitivan zakljucak.

### 0.3 Rezim Rada

| Rezim | Dozvoljeno ponasanje |
| --- | --- |
| `AUDIT_ONLY` | Pregledaj, mapiraj, bezbedno testiraj i izvesti. Ne menjaj source, lockfile-ove, podatke, seme, infrastrukturu, promptove ili provider konfiguraciju. |
| `AUDIT_AND_SAFE_FIX` | Primeni potvrdjene, low-risk i reverzibilne popravke sa fokusiranim regression testovima. Vece ili rizicne izmene samo planiraj. |
| `FULL_IMPLEMENTATION` | Implementiraj opravdane izmene postepeno. Napravi backup pre destruktivnog rada. Proveri rollback i recovery. |
| `FIX_CONFIRMED_ISSUES` | Menjaj samo nalaze koji su vec registrovani i potvrdjeni. Ne siri opseg precutno. |
| `SECURITY_AND_EVAL_AUDIT` | Prioritet daj trust boundary-jima, adversarial testovima, eval kvalitetu, dozvolama i incident readiness-u. |

Ako rezim nije naveden, koristi `AUDIT_AND_SAFE_FIX`.

