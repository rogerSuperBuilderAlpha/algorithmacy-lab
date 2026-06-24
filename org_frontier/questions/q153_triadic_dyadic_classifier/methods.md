# q153 — methods

## Corpus

Three sources of Boolean coordination forms:
- the curated 3-node `forms_library.FORMS`,
- a random 3-node ensemble from `rand_form` (120 draws, seed 0),
- a random 4-node ensemble from `rand_form4` (120 draws, seed 1).

Each form is labeled by its major-complex core size, read from exact IIT-4.0 Φ over the
reachable states: triadic (1) for a core of three or more nodes, dyadic (0) for a two-node core.
Forms with a sub-dyadic core are dropped.

Triadic forms are rare among random wirings. The raw pool ran 18 triadic against 77 dyadic. A
raw majority-class baseline near 0.9 makes accuracy uninformative, so the corpus is balanced to
a fixed ratio: all triadic forms are kept and dyadic forms are sampled with a fixed seed (42) to
1.5 dyadic per triadic. The balanced corpus is n=45 with a majority-class baseline of 0.6000.
Balancing is a pre-registered design choice fixed before scoring; the ratio and seeds are not
tuned to a target accuracy.

## Features

The shared bridge module `org_frontier/recurrence/crqa_phi_bridge.py` extracts four features per
form from a seeded trajectory (500 steps, flip 0.08):
- `det`, `rr` from `md_recurrence` on the whole-system trajectory,
- `lag_var`, the variance of the prominent pairwise lags from `coupling_matrix`,
- `spread`, the count of pairwise links with prominence above 0.05.

Each form gets a distinct fixed trajectory seed, so the feature vector reproduces byte-for-byte.

## Classifier and scoring

A logistic regression on standardized features, scored by 5-fold stratified cross-validation
(seed 0). The reported accuracy is the mean held-out accuracy across folds. The control repeats
the cross-validation on shuffled labels (shuffle seed 7); it should land at the baseline.

Standardized coefficients come from a single full-corpus fit. H2 compares their magnitudes.

## Verdict rules

H1 is SUPPORTED when real held-out accuracy exceeds the majority-class baseline, REFUTED
otherwise. H2 is CONFIRMED when `spread` has the largest-magnitude coefficient, NOT SUPPORTED
otherwise.

## Determinism

All RNG is seeded: ensemble draws, dyadic sampling, corpus order, trajectory sampling, the
cross-validation split, and the label shuffle. The probe runs byte-identical on re-run.

## Control

The worker-system-counterpart triad `[x[1], x[0]&x[2], x[1]]` with labels (W,S,C): verdict
triadic, max_phi 2.0, full 3-node core (label triadic). The control prints before any new
computation.

## Scope

Exact IIT-4.0 Φ on synthetic Boolean forms. In-silico throughout.
