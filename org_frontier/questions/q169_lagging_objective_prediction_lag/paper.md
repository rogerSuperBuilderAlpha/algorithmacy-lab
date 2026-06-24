# q169 — A Lagging Objective Lets the Displaced Worker's Model Track the Platform

Q141 established a structural result. An immediate, self-executing objective (O = W and C) displaces
the worker from the coordination's irreducible core; a lagging objective (a memory M = W and C
delayed one step, with the objective reading the memory, O = M) re-integrates her, and at higher Phi.
Q169 asks whether that re-integration carries into prediction. If a lagging objective binds the
worker back into the whole, does it also let her generative model track the platform's commit better
than an immediate objective does?

## The instrument

The study generalizes the cognition arm's window-fit accuracy loop (`pp3_moving_target`). A platform
commits a Boolean output each step and the worker predicts it. The platform's rule drifts: one entry
of its truth table over (W, C) flips every `period` steps, the retrain rate. The counterpart C is
hidden, so the worker conditions on her observable input W.

The two objectives differ in what the worker must predict. The immediate objective commits the live
joint determination W and C, which turns on the hidden C, so the worker can fit only P(O | W). The
lagging objective stores the realized joint determination in a memory node and emits it one step
later. The worker has already observed that realized value, so under the lagging objective she reads
the commit off the memory she holds rather than inferring it through the hidden counterpart in real
time. The drift period sweeps from 5000 down to 8 steps; the control at each period is the
immediate-objective mediator.

## Result

The lagging objective wins at every drift rate. Its accuracy stays near 1.0; the immediate
objective's sits near the hidden-counterpart floor of about 0.75 at slow drift and falls to 0.58 at
the fastest drift. The advantage runs from +0.25 at slow drift to +0.39 at fast drift. H1 holds: the
re-integration is visible in the predictive measure.

H2 fails. It predicted that fast drift would make the lagging memory stale and converge accuracy to
the immediate level. The opposite happens. The stored memory carries a realized value, so drift
corrupts it only through a same-step race at the emit boundary, and lagging accuracy falls only from
1.000 to 0.969 across the whole sweep. The immediate model degrades steeply, so the advantage widens
as drift speeds up. Re-integration through a realized memory is drift-robust.

## What it means

The memory that pulls the worker back into the core is the same memory that delivers the platform's
next commit to her model. A platform whose objective stores and re-emits the parties' realized joint
state keeps the worker both constitutive and able to anticipate it. A platform whose objective fires
on the live hidden counterpart leaves her near a prediction floor she cannot cross by modeling
harder, and faster retraining only widens the gap.

The result is specific to the realized-memory form of the lag, the form Q141's memory node takes. A
lag that instead recomputes the commit on the drifted rule applied to the previous request gives no
predictive advantage at all, because a pure rule-lag is statistically symmetric to the immediate
target under window-fit prediction. What helps the worker's model is not delay as such but a memory
that hands her a value she has already seen realized.

## Scope

Exact Boolean constructions and synthetic drift traces. The study is evidence about the instruments
and the construct, not a measurement of a real platform or worker. One-step lags and one window
length are tested. The Phi-to-economic-value bridge is open (Q122). This is study 1 of an empirical
line that reuses the predictive-processing battery's window-fit machinery on the interested-mediator
objective forms.
