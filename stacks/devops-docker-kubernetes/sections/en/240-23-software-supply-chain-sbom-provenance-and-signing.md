## 23. Software Supply Chain, SBOM, Provenance And Signing

**Objective:** Prove component origin and block unauthorized or vulnerable artifacts according to risk.

### 23.1 Required Checks

1. Inventory package managers, lockfiles, modules, base images, actions, plugins, charts, operators, binaries, firmware, vendored code, and download scripts.
2. Verify source authenticity, immutable references, checksums, signatures, maintainers, licenses, support, release channels, mirrors, and dependency-confusion resistance.
3. Generate complete SBOMs for source and final artifacts, include transitive and OS dependencies, identify tooling and format, and validate coverage against the built artifact.
4. Generate provenance that identifies source, builder, parameters, dependencies, environment, outputs, and isolation. Evaluate applicable SLSA requirements without overstating level.
5. Sign artifacts and attestations with protected keys or keyless identity, then verify issuer, subject, audience, certificate identity, transparency evidence, digest binding, and policy.
6. Correlate vulnerabilities with reachability, execution context, exposure, exploitability, compensating controls, fix availability, and deployment inventory instead of scanner severity alone.
7. Define time-bound exception, quarantine, revocation, re-sign, rebuild, and emergency replacement procedures.
8. Test admission or promotion rejection for unsigned, incorrectly signed, unverifiable, vulnerable, stale, wrong-source, or wrong-environment artifacts.

### 23.2 Minimum Evidence

- Dependency and component provenance inventory.
- Artifact-bound SBOM, provenance, signature, and verification reports.
- Policy rejection and compromised-component response drill.

### 23.3 Exit Criteria

1. Critical production artifacts are attributable to approved source and protected builders.
2. SBOM, provenance, signature, and vulnerability decisions are bound to the exact deployed digest.
3. Revocation and rebuild paths can remove a compromised component from production within the accepted window.

