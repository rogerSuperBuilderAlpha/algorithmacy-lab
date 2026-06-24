# q162 — Methods

## Forms

The corpus pools the curated 3-node forms_library, the named multiparty forms (n in {4, 5}), and a
seeded random-wiring ensemble. A random form sets each node to an arbitrary Boolean function of the
others, drawn from a fixed `numpy.random.default_rng(162)`. The ensemble draws 80 forms at n = 3
and 50 at n = 4. The curated multiparty forms carry the n = 5 cases into training. Forms whose
major-complex core has fewer than two nodes are dropped; a sub-dyadic core is neither triadic nor
dyadic.

## Structural labels

Each form is labeled by its exact IIT-4.0 major complex over reachable states:

- `td` — 1 when the core size is three or more (triadic), 0 when it is exactly two (dyadic).
- `msize` — the core size, an integer membership-count class.
- `bneck` — 1 when the leave-one-node-out drop in major-complex Φ has a unique argmax above
  tolerance (a single structural articulation node), 0 when the drop ties or vanishes.

The joint label is the triple `(td, msize, bneck)`. The labels are fixed and trajectory-independent.

## Feature families

One seeded trajectory per form (400 steps, flip 0.08, warmup 20) yields three blocks, all read
through the shared bridge module `org_frontier.recurrence.crqa_phi_bridge`:

- A — coupling prominence: a five-number summary of the off-diagonal pairwise prominences, a
  five-number summary of node coupling centralities, and the prominence spread (11 columns).
- B — md_recurrence: whole-system multidimensional recurrence DET and RR (2 columns).
- C — transfer entropy: a five-number summary of directed lag-1 binary TE over ordered node
  pairs, plus the mean absolute net flow over unordered pairs (6 columns).

Each block has fixed width independent of node count, so one classifier consumes the same columns
for any n.

## Classifier and ablation

A deterministic 1-nearest-neighbor over z-scored feature columns predicts each label separately.
Column means and standard deviations are fit on the training rows; standard deviations below
tolerance are floored to one. Distance ties resolve to the lowest training index. Held-out joint
accuracy is the fraction of test forms with all three labels correct.

The random ensemble is split by a fixed index partition: the last 40 percent is held out as the
test set, the rest joins the curated corpus as training. The split carries no RNG, so the test set
is identical across feature sets and the comparison is a clean ablation.

Four feature sets run on the identical split: A, B, A+B, and A+B+C. H1 reads A against A+B (the
md_recurrence drop). H2 reads A+B against A+B+C (the transfer-entropy gain). A gap within three
points counts as a match.

## Control

The faithful worker-system-counterpart triad `[x[1], x[0]&x[2], x[1]]` with labels (W, S, C) reads
structurally triadic with max_phi 2.0, a full {W, S, C} core (msize 3), and the mediator S (node 1)
as the coupling-centrality argmax of its sampled run. The probe asserts this before computing.

## Determinism

Every trajectory uses `numpy.random.default_rng(seed)` with a fixed per-form seed; the random
ensemble draws from `numpy.random.default_rng(162)`; the Φ library seeds its state search with
`numpy.random.default_rng(0)`; the train/test split is a fixed index partition. Re-runs reproduce
byte for byte.

## Validation gap

Exact IIT-4.0 Φ on small synthetic Boolean coordination forms. Verdict, membership, bottleneck,
coupling prominence, recurrence, and transfer entropy name graph-and-Φ quantities, not measured
organizations. In-silico scope; the CRQA and TE arms run on synthetic trajectories, so every
reported accuracy is a baseline on synthetic data.
