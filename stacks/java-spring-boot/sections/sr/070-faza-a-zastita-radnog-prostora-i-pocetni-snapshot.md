## Faza A - Zastita Radnog Prostora I Pocetni Snapshot

Pre bilo kakve izmene utvrdi root repozitorijuma, branch/status, necommitovane izmene, submodule-e, monorepo ili multi-module strukturu, pocetni commit SHA, aktivne environment promenljive samo po imenima, lokalne `.env`, secret, keystore, truststore i certificate fajlove bez citanja sadrzaja, i rizik da test ili build dodirne produkcione servise. Aktivno spreci testove nad production bazom.

Koristi bezbedne provere kada su primenljive:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
java -version
javac -version
```

Proveri `JAVA_HOME`, PATH rezoluciju, Maven/Gradle toolchain i daemon JDK, CI JDK i JDK iz production image-a. Ne pretpostavljaj da `java` i `javac` pripadaju istoj distribuciji ili verziji.

