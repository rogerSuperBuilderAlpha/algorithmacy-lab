# q157 — methods

## Ensemble and ground truth

Two random Boolean ensembles supply the forms:

- a 3-node ensemble from `rand_form` (200 draws, seed 0),
- a 4-node ensemble from `rand_form4` (120 draws, seed 1).

Each form's ground truth is its directed read edges, read from `cm_from_rules` by the flip test:
`cm[i, j] = 1` iff node j's rule changes value when node i flips, so j reads i and i leads j.
Forms with no off-diagonal edge contribute nothing and are skipped. The two ensembles are pooled
into the random-ensemble result H1 and H2 are stated on.

## Trajectory

Each kept form is run once as a stochastic dynamical system with `trajectory` (800 steps, flip
0.08). The trajectory seed is `9000 + k` for the 3-node draws and `7000 + k` for the 4-node
draws, so every run reproduces byte-for-byte.

## The two methods

For every true directed edge (i, j):

- DCRP peak-lag sign: `dcrp_orients_edge` calls `peak` on the ordered pair and counts a hit when
  the peak lag is positive (i leads j). Lag 0 counts as a miss.
- transfer entropy: `te_orients_edge` computes the lag-1 binary transfer entropy
  TE(i -> j) = I(j_{t+1} ; i_t | j_t) and TE(j -> i), and counts a hit when TE(i -> j) is the
  larger of the two. A tie counts as a miss. The estimator is the plug-in joint over the three
  binary variables (j_t, i_t, j_{t+1}); it is non-negative and in bits.

Both helpers live in the shared bridge module `org_frontier/recurrence/crqa_phi_bridge.py`, added
as the reusable spine for the directed-orientation arm of the recurrence line.

## Readouts

Per ensemble and pooled: the per-method recovery rate over all directed edges. Pooled: the
agreement contingency table (both correct, DCRP only, TE only, both wrong), the phi coefficient of
the two per-edge hit vectors, and the OR-combine recovery (either method correct) with its lift
over the better single method.

## Instrument control

The faithful worker-system-counterpart triad `[x[1], x[0]&x[2], x[1]]` with labels (W, S, C):
verdict triadic, max_phi 2.0. A clean one-way driver (y copies x's previous state, x independent
noise, 2000 steps, seed 0) confirms the transfer-entropy estimator is directional: forward TE far
exceeds reverse TE. The control prints `CONTROL ... PASS` before any ensemble computation.

## Determinism

Every RNG is seeded: ensemble draws (`random.Random(0)`, `random.Random(1)`), trajectory sampling
(`random.Random(9000 + k)`, `random.Random(7000 + k)`), and the control driver
(`np.random.default_rng(0)`). The probe runs byte-identical on re-run.

## Scope

Exact IIT-4.0 Φ machinery scores the ground-truth wiring on synthetic Boolean forms. In-silico
throughout. The recovery rates are properties of these ensembles and these estimators, not field
measurements.
