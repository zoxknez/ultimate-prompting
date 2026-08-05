# Revizija 03 - DevOps / Docker / Kubernetes / Cloud Platform

Datum: 2026-08-05
Status: zavrseno

## Polazno stanje

- Engleska verzija: 163 linija i 23 naslova.
- Srpska verzija: 143 linija i 21 naslova.
- Stari par nije imao strukturni paritet.
- Postojeci sadrzaj je bio dobra kratka checklist-a, ali nije predstavljao kompletan production audit ugovor.

## Glavni problemi stare verzije

1. Nedovoljno precizna granica autorizacije i produkcionih izmena.
2. Mesanje desired state-a, GitOps stanja, live cluster stanja i stvarnog korisnickog ponasanja.
3. Slabo razrađeni CI/CD trust boundary-ji, fork scenariji, self-hosted runner-i, OIDC i artifact substitution.
4. Nedovoljno pokriveni SBOM, provenance, SLSA, potpisivanje, atestacije, karantin i opoziv artefakata.
5. Nedovoljno detaljni Kubernetes control plane, version skew, CRD, webhook, Operator, PSS, RBAC i workload lifecycle zahtevi.
6. Backup se mogao pogresno smatrati potvrđenim bez izolovanog restore-a, integriteta i izmerenog RPO/RTO.
7. Nedostajala je potpuna test matrica za failure, capacity, scaling, incident, rollback, failover i failback.
8. EN i SR verzija su se razlikovale po obimu i redosledu sekcija.

## Nova verzija

- Engleska verzija: 1057 linija i 139 naslova.
- Srpska verzija: 1057 linija i 139 naslova.
- Obe verzije se generisu iz jednog sinhronizovanog dvojezicnog izvora.
- Uvedeni su isti naslovni nivoi, redosled, tabele, code fence blokovi, faze, kriterijumi izlaza i finalni contract.

## Najvaznija unapređenja

- Potpun source-to-production integrity model.
- Docker, BuildKit, runtime, registry i multi-architecture audit.
- Kubernetes control plane, nodovi, workload-i, scheduling, PSS, RBAC, mreza, TLS, storage i stateful sistemi.
- Helm, Kustomize, CRD, Operator, webhook i GitOps failure modeli.
- Terraform ili OpenTofu, cloud foundation, state i destructive-plan kontrole.
- CI/CD, fork, OIDC, runner, cache, artifact i injection threat model.
- SBOM, provenance, SLSA, Sigstore, atestacije, admission i vulnerability trijaza.
- Autoscaling, capacity, performance, chaos, observability, SLO, on-call i FinOps.
- Izolovani restore, failover, failback, incident response i supply-chain compromise vezbe.
- Stroga Definition of Done i verdict pravila koja zabranjuju neosnovan `ready` zakljucak.

## Baseline

Dodat je dated baseline za Kubernetes podrzane linije, Docker Engine 29.x, Helm 4.2.x, SLSA 1.2, Pod Security, GitHub OIDC i artifact attestations, Sigstore i NIST SSDF. Svaki baseline zahteva ponovnu proveru primarnog izvora u vreme stvarnog audita.
