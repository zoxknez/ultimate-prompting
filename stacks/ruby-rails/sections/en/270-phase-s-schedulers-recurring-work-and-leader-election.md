## Phase S - Schedulers, Recurring Work And Leader Election

- Inventory Solid Queue recurring tasks, Sidekiq cron, Whenever, system cron, Kubernetes CronJob, cloud scheduler and custom loops.
- Test overlap, duplicate trigger, missed trigger, clock skew, DST, long execution, restart and manual replay.
- Use database or distributed ownership with fencing where only one active scheduler or task is allowed.
- Make recurring work restartable, observable and safe when execution begins before a deployment and finishes after it.

