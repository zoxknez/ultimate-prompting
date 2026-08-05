## Faza B - Zajednicki Inventar

Mapiraj: executable jedinice, biblioteke, module/crate-ove, public API, generated code, build scriptove, CLI, servere, workere, schedulere, consumere, migracije, protokole, database sloj, cache, messaging, FFI, filesystem, deployment/ops, test fixture, benchmarke, fuzz targete, CI, container, IaC.

Graf: `repo -> module/workspace -> paket/crate -> executable -> deployment jedinica`.

Oznaci: ciklicne dependency-je; preveliki shared/common; domain zavisan od infrastructure; duplicirane modele; vise implementacija istog poslovnog pravila; deployment jedinicu koja deli bazu bez jasnog vlasnistva; generated code rucno menjan; zastareli executable koji se i dalje builda; feature/build-tag kombinacije koje CI ne proverava.

