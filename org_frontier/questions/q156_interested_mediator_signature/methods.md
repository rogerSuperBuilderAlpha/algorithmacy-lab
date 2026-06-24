# q156 — methods

## The wiring graph

One graph carries every form: W' = S, C' = S, S' = f(W, S, C). The parties read the mediator; the
mediator reads both parties and its own previous state. A mediator's rule is an 8-bit truth table
over (W, S, C), indexed tt[4·W + 2·S + C]. The connectivity matrix is identical across all forms
that read all three inputs, so structure other than the mediator's truth table is held fixed.

## The two pools

`enumerate_mediators` in the shared bridge module crqa_phi_bridge splits the truth tables. A rule
is faithful when it is symmetric under swapping the two parties, f(W,S,C) = f(C,S,W), and
interested when it is asymmetric. The harness keeps only rules that read all three inputs and whose
major-complex core, from exact IIT-4.0 Φ, is the full {W, S, C}. This yields 27 faithful and 18
interested forms, all matched on wiring graph and on structural core.

## Behavioral measure

`outgoing_prominence` runs a form as a stochastic dynamical system (trajectory, 500 steps, flip
0.08) and reads the coupling matrix's DCRP peak prominence on the mediator's two outgoing edges,
S→W and S→C, then averages the two. Each form's value is the mean over a fixed block of 16 seeded
trajectories, so it reproduces byte-for-byte.

## Tests

H1 forms every interested × faithful pair (486 pairs) and reports the fraction with interested
prominence below faithful, against a 0.70 threshold. A one-sided Mann-Whitney test on the 18
interested versus 27 faithful per-form means is the companion read, against alpha = 0.05. H2
compares the major-complex core sets of the two pools.

## Control

The instrument control is the worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels
(W,S,C): it must read triadic with max_phi 2.0 and a full {W,S,C} core before any new computation.
The connectivity-identical faithful mediator pool is the control for the behavioral arm.

## Determinism and scope

All RNG is seeded with fixed values, and three runs are byte-identical. Every number is exact
IIT-4.0 Φ and CRQA on synthetic Boolean coordination forms. No field organization is measured.
"Interested", "agenda", and "faithful" name the symmetry of a rule, not measured intent. The
validation gap is the usual one for this line: the construct is exercised in silico, and the
behavioral arm runs on synthetic trajectories.
