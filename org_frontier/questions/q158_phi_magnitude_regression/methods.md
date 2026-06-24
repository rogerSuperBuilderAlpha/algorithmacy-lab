# q158 — methods

## Forms

The pool is the 3-node forms_library, a random 3-node ensemble (rand_form, 120 draws, seed 0),
and a random 4-node ensemble (rand_form4, 120 draws, seed 1). Each form yields one row. Forms with
no irreducible major complex (Φ <= 0) are dropped, since they carry no magnitude to predict. The
surviving pool is 188 forms with Φ in the range 0.277 to 2.000.

## Variables

x is whole-system md_recurrence DET, read from a sampled trajectory of the form run as a stochastic
dynamical system (STEPS=500, FLIP=0.08). The whole-system recurrence rate RR is read alongside for
reference. y is the exact major-complex Φ from IIT-4.0, the maximum over reachable states of the
maximal complex's φ. Trajectory sampling is seeded per form (a distinct fixed seed per pool member),
so the feature side reproduces byte-for-byte; exact Φ is deterministic.

## Tests

H1 reads the Spearman rank correlation of DET against Φ over the pool, with its p-value.

H2 fits an ordinary least-squares line Φ ~ DET, then compares the mean linear residual of the top-Φ
quartile against the rest. A positive high-Φ residual that exceeds the rest is the underprediction
H2 predicts. The control is a monotone (isotonic, increasing) fit of Φ on DET: if the true relation
were a saturating rise, the monotone fit would cut the residual spread below the line. A monotone
fit that does no better is evidence against a rising-then-flat shape.

## Control

The worker-system-counterpart triad [x[1], x[0]&x[2], x[1]] with labels (W,S,C) reads verdict
triadic, max_phi 2.0, full 3-node core, and major-complex Φ 2.0. The probe asserts these before
computing the result and prints `CONTROL ... PASS`.

## Scope

Every number is exact IIT-4.0 Φ on synthetic Boolean coordination forms. This is an in-silico study
of the CRQA-to-Φ bridge. No field organization is measured, and the validation gap to real
coordination data is open.
