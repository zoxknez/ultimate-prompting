## 22. Faza Q - CI/CD, Supply Chain I Release Governance

1. Mapiraj pull-request provere, branch protection, obavezne review-e, build runner-e, cache, artefakte, signing, deployment i Play track promotion.
2. Proveri da CI koristi pinned action-e, image-e, plugin-e, toolchain-e i checksum-e gde je prakticno.
3. Razdvoji izvrsavanje untrusted pull request-a od tajni i signing-a.
4. Proveri da se artefakti proizvode jednom i promovisu, umesto da se drugacije rebuild-uju za svako okruzenje gde je izvodljivo.
5. Proveri da su source revision, dependency state, toolchain, provenance, signing identity i artifact digest sledljivi.
6. Skeniraj source i dependency odgovarajucim alatima, ali potvrdi nalaze i ne curi vlasnicki kod.
7. Proveri SBOM ili dependency inventar, license review, vulnerability response i update ownership.
8. Proveri da signing i Play kredencijali imaju least privilege, kratko trajanje gde je moguce, audit i da nisu dostupni fork-ovima.
9. Proveri da su release notes, versioning, migracije, support readiness, policy deklaracije i rollback plan pregledani pre promocije.
10. Proveri da testovi ne mogu biti precutno preskoceni task alias-om, conditional CI logikom ili changed paths pravilima.
11. Proveri remote i lokalni Gradle cache zbog curenja tajni i cross-branch kontaminacije.
12. Proveri da dependency bot ne merge-uje nekompatibilan upgrade bez project testova.

