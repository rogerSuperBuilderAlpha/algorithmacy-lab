# Quorum input-noise sweep: hypotheses and methods

Fixed before any value in this study was computed. This file is committed to the branch before the
script is run.

## Prior and gap

Probe 464 (`org_frontier/probes/weighted_quorum/input_noise/`) found that the 2-of-3 majority hub,
whose whole-system Φ is 0 without noise, has positive whole-system Φ at input-observation error
η=0.1, while OR and AND keep the full group as their major complex and majority does not. It tested
only η=0, 0.1 and 0.5 and three-party counting rules, and its own limits section says it "establish[es]
a counterexample at 0.1, not a noise threshold or monotonic trend", and that the full-major-complex
extremes-only claim across noisy rules "remains open" (OPEN_QUESTIONS O01). This study fills that gap
with a dense noise grid and adds the four-party counting quorums (1..4 of 4). It is a bounded
extension of probe 464, not a test on real organizations.

## Forms and noise

Same construction as probe 464 (its `input_tpm` and `read_case` are imported unchanged): node 0 is the
mediator S, which commits a quorum rule over what it observes; each party copies the actual S; S sees
each party through an independent bit-flip error η.

- Three parties, weights (1,1,1): quota 1 (OR3), 2 (MAJ3), 3 (AND3).
- Four parties, weights (1,1,1,1): quota 1 (ANY4), 2 (2of4), 3 (3of4), 4 (ALL4).
- η ∈ {0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5}. 70 cases. No forms or rates are added
  after computation.

Interior quorums: MAJ3, 2of4, 3of4. Extreme quorums: OR3, AND3, ANY4, ALL4. "Noisy grid" means
η ∈ {0.01, …, 0.45} (eight rates).

## Controls

Probe 457's C1 anchors must pass. Probe 464's in-function controls run on every case: at η=0 the noisy
TPM equals the deterministic TPM entrywise (1e-12); at η=0.5 the mediator probability is constant
across true inputs, whole-system Φ ≤ 1e-9 and no core holds S with a party. Any failed control stops
the run with a non-zero exit and no scores.

## Outcomes and decision rules (threshold 1e-9 throughout)

- H1 (no noise threshold for majority): MAJ3 whole-system Φ > 1e-9 at every rate in the noisy grid.
  One rate with Φ ≤ 1e-9 refutes.
- H2 (interior quorums never bind the full group): for MAJ3, 2of4 and 3of4, at no rate in the noisy
  grid is the full group the major complex in a state attaining the maximum core φ. One such case
  refutes.
- H3 (extremes keep the full group): OR3, AND3, ANY4 and ALL4 have the full group as the major
  complex in every maximum-φ state at every rate in the noisy grid. One failure refutes.
- H4 (the majority effect generalizes to four parties): 2of4 and 3of4 have whole-system Φ > 1e-9 at
  every rate in the noisy grid. One failure refutes.

Descriptive only (not scored): the rate at which each interior quorum's whole-system Φ peaks on the
grid, and its size relative to the extreme quorum with the same party count at that rate.
