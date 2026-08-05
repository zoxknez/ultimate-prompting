## Phase A - Workspace Safety And Initial Snapshot

Before any change, establish repository root, branch/status, uncommitted changes, submodules, monorepo or multi-module structure, initial commit SHA, active environment variable names only, local `.env`, secret, keystore, truststore, and certificate files without reading their contents, and the risk that a test/build could touch production services. Prevent tests from using a production database.

When applicable, safely run and record:

```text
git status --short --branch
git rev-parse --show-toplevel
git rev-parse HEAD
git submodule status
java -version
javac -version
```

Verify `JAVA_HOME`, PATH resolution, Maven/Gradle toolchain and daemon JDK, CI JDK, and JDK in the production image. Do not assume `java` and `javac` use the same distribution or version.

