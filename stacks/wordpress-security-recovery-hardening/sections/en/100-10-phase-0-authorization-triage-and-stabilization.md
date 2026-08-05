## 10. Phase 0 - Authorization, Triage And Stabilization

1. Confirm owner authorization and exact assets in scope.
2. Record current time in local timezone and UTC.
3. Determine whether the incident is active.
4. Identify immediate safety concerns:
   - payment card capture
   - credential theft
   - data exfiltration
   - public malware delivery
   - attacker access still active
   - DNS or CDN takeover
   - destructive activity or ransomware
5. Decide whether to:
   - preserve service while blocking malicious paths
   - place the origin behind an authenticated maintenance response
   - restrict access by IP/VPN
   - disable checkout, login, registration or uploads selectively
   - contact the host/CDN/payment provider
6. Document business impact, downtime constraint and rollback owner.

### Immediate stop-and-escalate conditions

Stop routine work and escalate when:

- active payment skimming or likely cardholder-data exposure is found
- confirmed personal-data exfiltration is found
- attacker still controls registrar, DNS, CDN, hosting panel or root account
- evidence suggests compromise of multiple customer accounts on shared hosting
- destructive actions are occurring
- legal hold, insurance, law-enforcement or regulatory requirements apply
- the environment is outside the responder's authorization

