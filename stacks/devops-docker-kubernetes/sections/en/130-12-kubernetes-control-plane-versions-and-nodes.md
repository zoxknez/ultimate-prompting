## 12. Kubernetes Control Plane, Versions And Nodes

**Objective:** Validate supported cluster foundations, upgrade safety, and failure domains.

### 12.1 Required Checks

1. Inventory distribution, provider, region, control-plane version, node versions, add-ons, CRI, CNI, CSI, kube-proxy mode, DNS, ingress, admission, autoscaler, and support lifecycle.
2. Verify supported version skew among control plane, kubelet, kube-proxy, kubectl, add-ons, operators, APIs, and managed-provider constraints.
3. Scan manifests and live resources for deprecated or removed APIs, conversion dependencies, incompatible CRDs, and webhook upgrade blockers.
4. Verify control-plane endpoint exposure, private access, audit logging, encryption configuration, maintenance policy, backups, and provider responsibility boundaries.
5. Inspect node pools, operating systems, images, patch cadence, taints, labels, architecture, zones, capacity, bootstrap, metadata access, and instance identity.
6. Test node replacement, drain, disruption, upgrade surge, failed node, zone loss assumptions, and recovery of critical add-ons.
7. For self-managed control planes, audit etcd topology, peer and client TLS, encryption, backup, compaction, defragmentation, quorum, restore, and access.

### 12.2 Minimum Evidence

- Cluster component and support-lifecycle inventory.
- Version-skew and deprecated-API report with upgrade blockers.
- Node or zone disruption evidence and control-plane recovery evidence where applicable.

### 12.3 Exit Criteria

1. Cluster and add-on versions are supported or have an approved time-bound remediation.
2. Upgrade blockers, removed APIs, and webhook dependencies are known before change.
3. Node and control-plane failure assumptions are verified, not merely documented.

