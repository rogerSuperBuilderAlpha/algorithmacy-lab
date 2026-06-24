# Q169 — methods

The instrument generalizes `pp3_moving_target`'s window-fit accuracy loop to the two Q128/Q141
objective forms. A platform commits a Boolean output each step; the worker predicts it. The
platform's rule is a 4-entry truth table over (W, C), indexed W + 2C, and it drifts: one entry
flips every `period` steps (the retrain rate). The counterpart C is hidden (PP1), so the worker
conditions on her observable W.

**Immediate objective** (Q128, O = W ∧ C). The commit is the live joint determination, which turns
on the hidden C. The worker fits a window-majority over her recent observed commits keyed on W. A
flip leaves her window stale until enough post-flip samples accumulate.

**Lagging objective** (Q141, O = M with M = W ∧ C delayed one step). A memory node computes and
stores the joint determination at t-1; the objective emits the stored value at t. The stored memory
is the re-integration channel: the displaced counterpart's contribution reaches the worker as a
memory she already observed, so she predicts the commit by reading the held memory. The read is
exact except for a same-step race — if the served entry flips at the emit step, the platform
re-stores a new value the instant before emit and the worker's held value is stale for that step.

The drift period sweeps over (5000, 800, 300, 120, 60, 30, 15, 8). For each period, accuracy is the
mean over 120 seeded trials of 2000 steps with a window of 40. The control at each period is the
immediate-objective mediator. H1 reads on the advantage at matched moderate drift (period ≥ 60); H2
reads on whether the advantage shrinks toward zero at the fastest drift.

Control: the canonical three-party triad reads triadic, max Φ = 2.0. The Q141 immediate and lagging
objective forms are also read for their structure (both triadic, Φ 1.0 and 2.0), anchoring the
predictive study to the structural re-integration it mirrors.

Everything is seeded with `random.Random`; repeated runs reproduce byte-identically. The empirical
arm runs on synthetic prediction traces, not a measured worker.

Reproduce:
`python -m org_frontier.questions.q169_lagging_objective_prediction_lag.probe_lagging_objective_prediction_lag`
([`results/output.txt`](results/output.txt)).
