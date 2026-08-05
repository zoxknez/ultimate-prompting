## 2. Aktuelni istrazivacki baseline - ponovo proveriti pre svakog audita

Na datum baseline-a, primarni izvori su ukazivali na sledece. Ovo je vremenski ogranicena polazna tacka, a ne trajna istina.

| Komponenta | Baseline na 2026-08-05 | Obavezna audit akcija |
| --- | --- | --- |
| Kubernetes | Podrzane upstream linije `1.36`, `1.35` i `1.34` | Utvrdi tacan patch, podrsku provider-a, skew, uklonjene API-je i upgrade putanju. |
| Docker Engine | `29.x` aktuelna release linija | Proveri tacan engine, containerd, BuildKit, API, storage driver i status podrske. |
| Helm | `4.2.x` stabilna linija; Helm 3 u ogranicenom periodu podrske | Proveri kompatibilnost chart-ova i plugin-a pre prelaska na novu major verziju. |
| SLSA | Specifikacija `1.2` | Mapiraj stvarnu build provenance i izolaciju na primenljive zahteve. |
| Pod Security | Pod Security Standards i ugrađeni Pod Security Admission | Utvrdi enforce, audit i warn posture po namespace-u i izuzecima. |
| GitHub Actions gde se koristi | OIDC, artifact attestations, least privilege i immutable action reference | Proveri trust boundary-je, fork ponasanje, dozvole, izolaciju runner-a i SHA pinning. |
| NIST SSDF | SP 800-218 verzija 1.1 je finalna; novije revizije mogu biti draft | Koristi finalne zahteve osim ako organizacija namerno ne usvoji potvrđen draft. |

