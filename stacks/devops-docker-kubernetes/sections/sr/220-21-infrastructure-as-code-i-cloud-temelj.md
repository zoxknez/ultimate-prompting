## 21. Infrastructure as code i cloud temelj

**Cilj:** Ucini cloud izmene preglednim, deterministickim, least-privileged i oporavljivim.

### 21.1 Obavezne provere

1. Popisi IaC root-ove, module, provider-e, backend-e, workspace ili stack-ove, vlasnistvo state-a, lock mehanizam, okruzenja, import-e, generisan kod i rucne resurse.
2. Namerno pinuj provider i module constraint-e, proveri checksum i provenance, i odbaci nereview-ovano remote izvrsavanje ili mutabilne module source-ove.
3. Zastiti state sifrovanjem, least privilege-om, versioning-om, locking-om, backup-om, recovery-jem, audit logovima, razdvajanjem i rukovanjem svesnim tajni.
4. Pregledaj planove za replacement, brisanje, force-new, implicitne default vrednosti, unknown vrednosti, data source-ove, provider side effect-e, quota uticaj i blast radius.
5. Detektuj drift, unmanaged resurse, import-e, moved block-ove, tainted resurse, state surgery, console izmene, orphan zavisnosti i zastarele output-e.
6. Audituj temelje organizacije, naloga, projekta, regiona, mreze, IAM-a, KMS-a, logging-a, budzeta, kvote, podrske i break-glass-a pre aplikacionih resursa.
7. Testiraj plan, policy, apply u izolaciji, partial failure, prekinut apply, import, rollback ili forward-fix, restore state-a i ponasanje pri outage-u provider-a.
8. Nikada ne pokreci produkcioni apply sa nereview-ovane lokalne radne stanice kada je potreban kontrolisan pipeline.

### 21.2 Minimalni dokazi

- Inventar IaC topologije, vlasnistva, backend-a, state-a i dozvola.
- Pregled reprezentativnog plana sa analizom destruktivnih i unknown vrednosti.
- Dokaz backup-a state-a, restore-a, prekida i usklađivanja drift-a.

### 21.3 Kriterijumi izlaza

1. Produkcione infrastrukturne izmene su review-ovane, pripisive, policy-proverene i izvrsene kroz odobrene identitete.
2. State je zasticen i oporavljiv bez otkrivanja tajni.
3. Destruktivni, replacement, drift i partial-apply rizici su eksplicitni pre izvrsavanja.

