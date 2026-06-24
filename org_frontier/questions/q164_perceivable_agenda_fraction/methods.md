# q164 — methods

The study reruns the direct-perception battery's two readings (D1 trace AUC, D2 marginal fit) on the
Q126 interested mediator instead of random strict gates. The shared machinery lives in
`org_frontier/cognition/interested_perception.py`, the bridge module for this empirical line.

## Forms

The triad has nodes (W, S, C). W' = S, C' = S, and S' is the interested mediator of (W, C). The
mediator at level k imposes agenda a on the k least-warranted (W, C) states and commits the faithful
AND elsewhere. k=0 is the faithful gate; k=4 is the constant agenda. The forms are
`mediator(agenda, k)` and `triad_rules(agenda, k)` from the Q126 probe.

## Instrument control

The faithful triad `[lambda x:x[1], lambda x:x[0]&x[2], lambda x:x[1]]` reads verdict `triadic` with
max_phi 2.0 through `org_frontier.probes.lib.verdict`. The probe halts if the control does not pass.

## D1 — trace AUC

The mediator's commit echoes one step on into the worker outcome W' and the counterpart outcome C'.
Each form is run as a stochastic dynamical system with `recurrence.crqa.trajectory` (600 steps,
flip 0.08, seeded per draw). The W↔C cross-recurrence peak prominence comes from
`recurrence.crqa.peak` (max lag 8). For each agenda, 120 interested traces (k=2) and 120 faithful
traces (k=0) are scored, and the rank AUC separates the two. The reported number is the
discrimination AUC max(auc, 1−auc), comparable to the battery's 0.67. The mean over the two agendas
is the D1 reading.

## D2 — marginal fit

With the counterpart C hidden, a worker fits f(W) by majority over hidden C from 200 sampled
(W, C, outcome) draws, then scores f(W) on the four (W, C) states. The fit error is the share
mispredicted. At each k the interested mediator's mean error over 200 trials is compared against a
matched-k random strict gate, a random gate with k of its four entries pushed to the agenda value so
the two differ only in which states carry the agenda and what the baseline is. The plain random
strict gate (battery D2 baseline, error 0.23) is reported alongside.

## Determinism

Every RNG is a seeded `random.Random`. The run reproduces byte-for-byte; three runs were confirmed
identical.

## Verdict rules (fixed before computing)

- H1 SUPPORTED iff the mean D1 AUC < 0.67 − 1e-9.
- H2 SUPPORTED iff the mean matched-k marginal fit error over k ∈ {1, 2, 3} is strictly larger for
  the interested mediator than for the matched random gate.
