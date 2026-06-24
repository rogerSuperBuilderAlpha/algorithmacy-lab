# Q169 findings — the lagging objective lets the worker's model track the platform better

H1 holds and H2 fails. The Q141 re-integration is visible in a predictive measure: a lagging
objective lets the worker's generative model track the platform's commit far better than an
immediate self-executing objective does, at every drift rate tested. The advantage does not vanish
as drift speeds up; it grows.

| drift period | immediate acc | lagging acc | advantage |
|---|---|---|---|
| 5000 | 0.749 | 1.000 | +0.251 |
| 800 | 0.750 | 1.000 | +0.250 |
| 300 | 0.738 | 0.999 | +0.261 |
| 120 | 0.743 | 0.998 | +0.255 |
| 60 | 0.727 | 0.996 | +0.269 |
| 30 | 0.677 | 0.992 | +0.315 |
| 15 | 0.614 | 0.984 | +0.370 |
| 8 | 0.576 | 0.969 | +0.393 |

| H | Result |
|---|---|
| H1 (lagging objective predicts the platform better at matched drift) | SUPPORTED |
| H2 (the lagging advantage vanishes as drift speeds up) | NOT SUPPORTED (advantage +0.251 at slow drift grows to +0.393 at fast drift) |

## Reading

Under the immediate objective the commit is the live joint determination W and C, which turns on the
hidden counterpart C. The worker can only fit P(O | W) from her observable input, and that model
sits near the hidden-counterpart floor (about 0.75) and degrades further as drift outpaces her
window (down to 0.58 at the fastest drift). Under the lagging objective a memory node stores the
realized joint determination and the objective emits it one step later. The worker has already
observed that realized value, so she reads the commit off the held memory and tracks the platform
near-perfectly. This is the predictive face of Q141's structural result: the memory that pulls the
worker back into the core is the same memory that delivers the platform's next commit to her model.

H2 predicted that fast drift would make the memory stale and erase the advantage. It does not. The
stored memory carries a realized value, so drift corrupts it only through a same-step race at the
emit boundary, a small effect (lagging accuracy falls only from 1.000 to 0.969 across the whole
sweep). The immediate model has no such protection and falls steeply, so the advantage widens as
drift speeds up rather than closing. Re-integration through a realized memory is drift-robust, not
fragile.

## Limitations

Exact Boolean constructions and synthetic drift traces; evidence about the instruments and the
construct, not a measurement of a real platform. The lagging objective here stores a realized joint
determination, the form Q141's memory node takes (M' = W and C, then O' = M). A different lag
mechanism that recomputes the commit on the drifted rule applied to the previous request shows no
predictive advantage at all (a pure rule-lag is statistically symmetric to the immediate target
under window-fit prediction), so the result is specific to the realized-memory form, not to lagging
in general. One-step lags and one window length are tested; longer lags, partial-memory objectives,
and a worker who also observes C are untested. "Objective", "memory", "commit" label node rules and
output values, not measured intent. The Phi-to-economic-value bridge is open (Q122).
