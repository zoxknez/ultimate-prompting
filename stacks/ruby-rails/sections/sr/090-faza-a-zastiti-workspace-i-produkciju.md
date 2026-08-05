## Faza A - Zastiti Workspace I Produkciju

```text
git status --short --branch
git rev-parse HEAD
git remote -v
ruby --version
ruby -e 'puts [RUBY_ENGINE, RUBY_VERSION, RUBY_PATCHLEVEL, RUBY_PLATFORM].join(" ")'
gem --version
bundle --version
bundle env
```

- Zabelezi dirty fajlove, untracked tajne, lokalne patch-eve, submodule-e, worktree-eve i generisane artefakte pre bilo koje izmene.
- Pronadji production credential-e, deploy manifeste, vlasnistvo migracija, queue kontrole, storage bucket-e, shared volume-e i backup procedure bez prikaza vrednosti tajni.
- Identifikuj komande sa initializer side effect-ima, destruktivnim callback-ovima, spoljnim mreznim pozivima ili production default target-ima.
- Napravi safety granicu za upise u bazu, trosenje jobova, slanje mailova, webhook-ove, placanja i object storage pre testova.

