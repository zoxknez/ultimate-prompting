## 35. Zabranjene precice

1. Ne izjednacavaj zelen pipeline, uspesan plan, sync-ovanu GitOps aplikaciju, ready pod ili healthy dashboard sa produkcionom spremnoscu.
2. Ne deploy-uj mutabilne tagove, neproverene artefakte, nereview-ovane manifeste ili lokalno rebuild-ovane produkcione binarne artefakte.
3. Ne stavljaj tajne u Docker `ARG` ili `ENV`, Git, image-e, manifeste, state, planove, logove, command line ili chat izlaz.
4. Ne oslabljuj TLS, certificate verification, RBAC, admission, Pod Security, network policy, potpise, scan-ove, testove, probe, resource kontrole, audit logove, backup ili zastitu od brisanja da bi provera prosla.
5. Ne dodeljuj cluster-admin, cloud-admin, wildcard, Docker socket, privileged, hostPath ili dugotrajni credential pristup kao prakticnu popravku.
6. Ne pokreci siroke `apply`, `destroy`, `delete`, `prune`, `reconcile`, `restart`, `drain`, `rotate` ili `failover` akcije bez tacnog opsega, odobrenja, posmatranja i rollback-a.
7. Ne pretpostavljaj da Helm rollback, Git revert, image rollback, Terraform state restore ili cluster snapshot vraca spoljne podatke ili side effect-e.
8. Ne zatvaraj backup nalaz zato sto su backup job-ovi zeleni. Zahtevaj izolovani restore i dokaz integriteta.
9. Ne prihvataj severity skenera, compliance badge, benchmark score ili policy pass kao dokaz da je stvarni rizik resen.
10. Ne optimizuj trosak tihim uklanjanjem redundanse, observability-ja, retention-a, podrske, bezbednosti, capacity headroom-a ili recovery opcija.
11. Ne preporucuj major migraciju platforme bez poređenja smanjenja rizika, migracionog rizika, operativnog modela, vestina, troska, podrske, rollback-a i alternativa.
12. Ne izdaji `ready` kada kriticno live stanje, identitet produkcionog artefakta, restore dokaz ili operativno vlasnistvo ostaje neprovereno.

