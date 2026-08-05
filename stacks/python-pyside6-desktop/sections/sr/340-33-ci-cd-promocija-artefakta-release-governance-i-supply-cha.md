## 33. CI/CD, promocija artefakta, release governance i supply chain

### 33.1 Obim audita

1. Mapiraj repozitorijum, branch protection, review, CI runner-e, reusable workflow-e, cache-eve, artefakte, package index-e, signing servise, notarizaciju, store-ove, update feed-ove i deployment odobrenja.
2. Razlikuj trusted i untrusted code putanje, posebno fork-ove, pull request-ove, dependency update bot-ove, self-hosted runner-e i generisane artefakte.
3. Pregledaj workflow injection, command quoting, izlaganje tajni, mutable action reference, cache poisoning, zamenu artefakta, environment approval-e i OIDC scope.
4. Zahtevaj locked i verifikovane zavisnosti, pinovane toolchain-e, kontrolisane spoljne download-e, SBOM, provenance, potpis i vulnerability/license gate-ove.
5. Izgradi jednom po target-u i promoviši iste immutable bajtove kroz test, signing, staging i produkciju gde platformska pravila dozvoljavaju.
6. Definiši release vlasništvo, segregation of duties, emergency putanju, kompromitovanje ključa, package-index kompromitovanje, runner kompromitovanje i trusted rebuild.

### 33.2 Obavezna verifikacija

1. Reprodukuj release build-ove na čistim runner-ima i uporedi dependency, resource, native-library, package i installer manifest-e i hash-eve.
2. Dokaži da untrusted kod ne može čitati signing ključeve, objavljivati pakete, mutirati release artefakte, trovati trusted cache ili odobriti produkciju.
3. Verifikuj da se potpisi, provenance, SBOM, release notes, version metadata i update metadata odnose na iste pregledane bajtove.
4. Vežbaj expiry credential-a, outage signing servisa, notarization kvar, store rejection, kompromitovanu zavisnost, revoked ključ i emergency rebuild.
5. Čuvaj auditabilan zapis odobravaoca, source commit-a, toolchain-a, zavisnosti, hash-eva artefakta, potpisa, kanala, cohort-a, rollout-a, abort-a i rollback-a.

