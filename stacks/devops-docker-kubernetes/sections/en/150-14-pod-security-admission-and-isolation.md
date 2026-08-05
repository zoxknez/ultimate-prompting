## 14. Pod Security, Admission And Isolation

**Objective:** Enforce a measurable workload-isolation baseline with controlled exceptions.

### 14.1 Required Checks

1. Classify namespaces and workloads against the current Pod Security Standards profiles and document why each exception exists.
2. Configure Pod Security Admission or an equivalent policy layer with deliberate `enforce`, `audit`, and `warn` versions and labels.
3. Verify effective securityContext at pod and container level: UID, GID, supplemental groups, fsGroup, capabilities, privilege escalation, root filesystem, seccomp, AppArmor or SELinux.
4. Audit host namespaces, host ports, device plugins, hostPath, CSI drivers, proc mounts, sysctls, runtimeClass, sandboxed runtimes, and privileged system workloads.
5. Prevent bypass through unlabeled namespaces, namespace creation rights, exempt users, service accounts, runtime classes, debug containers, or webhook failure policy.
6. Test rejected and accepted manifests, upgrade behavior, policy-controller outage, and emergency exception expiry.

### 14.2 Minimum Evidence

- Namespace security-profile and exception matrix.
- Admission test corpus with expected and actual decisions.
- Effective privilege inventory for critical and system workloads.

### 14.3 Exit Criteria

1. Restricted or equivalent posture is enforced where feasible and exceptions are narrow, owned, and expiring.
2. No trivial namespace, identity, runtime, or webhook bypass remains.
3. Policy failure does not silently admit unsafe workloads unless explicitly designed and accepted.

