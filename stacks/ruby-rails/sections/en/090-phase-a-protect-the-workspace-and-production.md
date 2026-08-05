## Phase A - Protect The Workspace And Production

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

- Record dirty files, untracked secrets, local patches, submodules, worktrees and generated artifacts before any change.
- Locate production credentials, deploy manifests, migration ownership, queue controls, storage buckets, shared volumes and backup procedures without printing secret values.
- Identify commands with initializer side effects, destructive callbacks, external network calls or production default targets.
- Create a safety boundary for database writes, job consumption, mail delivery, webhooks, payments and object storage before tests.

