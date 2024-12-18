# Django Project Template for my future SaaS sites


## TODO:
- [ ] payments and stripe checkout
- [ ] Plans (TimeFixedPlan, SubscriptionPlan, ....)
- [ ] Remove the abstraction of Submodules.
- [ ] Create a task in `base.tasks` to sync folders...
## Conventions



### tasks.py

* Standard Task: `<do_something>_task`
* Periodic tasks:
  * Weekly task: `<do_something>_weekly`
  * Dairly task: `<do_something>_darily`
  * Hourly task: `<do_something>_hourly`
  * Every X minutes Task : `<do_something>_every_X_min`

