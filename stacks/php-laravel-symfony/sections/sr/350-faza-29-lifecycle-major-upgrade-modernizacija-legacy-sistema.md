## Faza 29 - Lifecycle, major upgrade, modernizacija legacy sistema i decommissioning

### Cilj

Planiraj rad na podržanim verzijama, migraciju framework-a i runtime-a, compatibility, rollback i retirement bez skrivenog rizika.

### Zahtevi audita

- Prati PHP, framework, Composer, ekstenzije, database driver-e, operativne sisteme, web servere, biblioteke i servise prema zvaničnim support prozorima.
- Inventariši deprecated PHP feature-e, framework API-je, recipes, bundle-ove, package-e, annotation-e, konfiguracione formate i promene ponašanja.
- Za Laravel major upgrade proveri PHP zahteve, podršku first-party package-a, skeleton promene, auth, queue, cache, database, test i deployment kompatibilnost.
- Za Symfony major ili LTS migracije proveri recipes, Flex, podršku bundle-ova, deprecation-e, container, security, serializer, Messenger, Doctrine i Runtime promene.
- Pokreni dual-line compatibility testove, reprezentativne data migracije, mixed-version deployment, performance poređenje, canary, rollback i forward repair.
- Ukloni abandoned package-e, nesigurne plugin-e, mrtve rute, debug alate, neiskorišćene kredencijale, zastarelu infrastrukturu i nepodržane runtime putanje uz dokaz.

### Obavezni dokazi

- Support i upgrade matrica sa owner-om, rokom, blocker-ima, compatibility dokazom i rollback-om.
- Dual-version build, test, data, load, deployment i recovery dokaz.
- Decommission dokaz za kod, rute, package-e, tajne, podatke, worker-e, infrastrukturu i observability.

### Kriterijumi prihvatanja

- Nijedna nepodržana ili abandoned komponenta ne ostaje na kritičnoj produkcionoj putanji bez odobrene vremenski ograničene mitigacije.
- Upgrade i retirement planovi čuvaju podatke, ugovore, ovlašćenja, operacije i testiranu recovery putanju.

