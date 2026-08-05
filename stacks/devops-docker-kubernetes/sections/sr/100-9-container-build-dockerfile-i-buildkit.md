## 9. Container build, Dockerfile i BuildKit

**Cilj:** Proizvedi minimalne, reproduktivne OCI artefakte bez tajni i spremne za potrebne platforme.

### 9.1 Obavezne provere

1. Pregledaj build context, `.dockerignore`, stage-ove, base image-e, pravilo digest pinning-a, instalaciju paketa, cache, generisane fajlove, vlasnistvo, timestamp-e i reproduktivnost.
2. Koristi BuildKit secret ili SSH mount za build kredencijale. Odbaci tajne u `ARG`, `ENV`, kopiranim fajlovima, layer-ima, cache export-u, logovima ili image istoriji.
3. Proveri da multi-stage granice sprecavaju curenje kompajlera, package manager-a, izvora, testova, kredencijala i debug alata u runtime image.
4. Pokreni proces kao namerno izabran non-root UID i GID, sa ispravnim vlasnistvom fajlova, writable putanjama, signalima, init ponasanjem, locale-om, sertifikatima, timezone pretpostavkama i shutdown semantikom.
5. Proveri podrsku arhitektura, native biblioteke, rizike emulacije, 32-bit ili 64-bit pretpostavke i ispravnost manifest liste za potrebne platforme.
6. Generisi SBOM i provenance tokom build-a i vezi ih za immutable image digest.
7. Izmeri kompresovanu velicinu, raspakovanu velicinu, reuse layer-a, startup uticaj, vulnerability exposure i operativnu debuggabilnost umesto slepog smanjenja velicine.

### 9.2 Minimalni dokazi

- Reproduktibilna build komanda, verzija builder-a, matrica platformi i image digest-i.
- Pregled image istorije i layer-a sa proverama tajni.
- SBOM, provenance, potpis, scan i runtime smoke dokaz vezan za digest.

### 9.3 Kriterijumi izlaza

1. Nijedan kredencijal nije prisutan u context-u, layer-ima, istoriji, metapodacima, logovima ili exportovanom cache-u.
2. Runtime image sadrzi samo opravdane komponente i ispravno radi kao non-root na potrebnim arhitekturama.
3. Identitet artefakta, SBOM, provenance, potpis i rezultati testova su immutable i međusobno povezani.

