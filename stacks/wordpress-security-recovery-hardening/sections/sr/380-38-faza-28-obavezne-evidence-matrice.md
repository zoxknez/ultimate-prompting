## 38. Faza 28 - Obavezne Evidence Matrice

Popuni svaku primenljivu matricu. Prazna matrica nije dokaz.

### M1 - Matrica asset-a i kontrolnih ravni

| Asset/control plane | Vlasnik | Putanja pristupa | Autentikacija | Logovi | Poslednja izmena | Evidence status | Rizik |
| --- | --- | --- | --- | --- | --- | --- | --- |

### M2 - Source-to-runtime integrity matrica

| Komponenta | Source/provenance | Očekivana verzija/hash | Instalirana verzija/hash | Runtime dokaz | Drift | Odluka |
| --- | --- | --- | --- | --- | --- | --- |

### M3 - Persistence matrica

| Persistence površina | Metod pregleda | Rezultat | Evidence ID | Remediation | Verifikacija |
| --- | --- | --- | --- | --- | --- |

### M4 - Matrica identiteta i tajni

| Identitet/tajna | Scope | Poslednja rotacija | Sumnjiva aktivnost | Akcija | Potvrđena revokacija |
| --- | --- | --- | --- | --- | --- |

### M5 - Database integrity matrica

| Data domen/tabela | Indikator/query | Pogođeni objekti | Metod mutacije | Backup/rollback | Verifikacija |
| --- | --- | --- | --- | --- | --- |

### M6 - Matrica zakazanog izvršavanja

| Scheduler | Hook/job | Vlasnik | Payload/argumenti | Poslednje/sledeće izvršavanje | Odluka | Verifikacija |
| --- | --- | --- | --- | --- | --- | --- |

### M7 - Edge i cache matrica

| Sloj | Vlasnik konfiguracije | Sumnjivo stanje | Dokaz | Invalidacija/izmena | Verifikacija |
| --- | --- | --- | --- | --- | --- |

### M8 - Backup i restore matrica

| Backup | Vreme | Pre mogućeg kompromitovanja | Integritet | Izolovano skeniranje | Restore test | Data gap | Odluka |
| --- | --- | --- | --- | --- | --- | --- | --- |

### M9 - Vulnerability i patch matrica

| Komponenta | Instalirano | Fixed/supported target | Izloženost | Exploit dokaz | Patch/izmena | Regression rezultat |
| --- | --- | --- | --- | --- | --- | --- |

### M10 - Matrica funkcionalnih kritičnih tokova

| Tok | Anonymous/auth uloga | Očekivano | Rezultat | Security assertion | Dokaz |
| --- | --- | --- | --- | --- | --- |

### M11 - Matrica obaveštavanja i stakeholder-a

| Stakeholder | Okidač | Vlasnik odluke | Rok/izvor | Status | Dokaz |
| --- | --- | --- | --- | --- | --- |

### M12 - Matrica povratka u produkciju

| Gate | Obavezni dokaz | Rezultat | Otvoren rizik | Odobravalac | Vreme |
| --- | --- | --- | --- | --- | --- |

