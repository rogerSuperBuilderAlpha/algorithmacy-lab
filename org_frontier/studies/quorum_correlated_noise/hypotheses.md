# Correlated input noise on quorum hubs: hypotheses and methods

Fixed before any value in this study was computed, and committed to the branch before the script runs.

## Prior and gap

`quorum_noise_sweep/` found that the 2-of-3 majority hub (MAJ3) has positive whole-system Φ at every
independent input-error rate tested in (0, 0.5), but never takes the full group as its major complex.
Every error there was independent across parties. Its backlog item 1 asks whether the effect survives
when the mediator's errors are correlated, and item 3 notes that in 22 of 24 noisy interior cases the
largest core φ was the node count times whole-system Φ. This study tests both on three-party hubs.

## Forms and noise models

Same construction as probe 464 and `quorum_noise_sweep/`: node 0 is the mediator S, which commits a
counting rule over what it reads of three parties; each party copies the actual S. Forms: OR3 (1 of 3),
MAJ3 (2 of 3), AND3 (3 of 3). Each reading S makes is wrong with the same marginal probability e under
three models:

- **indep**: each reading flips independently with probability e (probe 464's model).
- **common**: with probability e all three readings flip together; otherwise all are correct.
- **mix**: each reading is flipped by a shared flip (probability q) XOR an independent flip (probability
  q), with q = (1 − sqrt(1 − 2e)) / 2 so the marginal error is e.

Rates e ∈ {0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45}. 72 cases. e = 0.5 is excluded because under
`common` it does not make the readings independent of the true inputs. No forms, models or rates are
added after computation.

Reasoning behind H1 (stated before computing): majority is self-dual, MAJ(¬x) = ¬MAJ(x), so under
`common` P(S′=1 | x) = (1 − e)·MAJ(x) + e·(1 − MAJ(x)) takes only two values, like a commit flip.
OR and AND are not self-dual, so under `common` they take three values.

## Controls

Probe 457's C1 anchors must pass. At e = 0 every model's TPM equals the deterministic TPM entrywise
(1e-12). The `indep` TPM equals probe 464's `input_tpm` entrywise (1e-12) at every rate. Any failure
stops the run with a non-zero exit and no scores.

## Outcomes and decision rules (threshold 1e-9)

- H1 (common-mode noise keeps majority at zero): MAJ3 whole-system Φ ≤ 1e-9 at every nonzero rate under
  `common`. One rate above 1e-9 refutes.
- H2 (any independent component restores it): MAJ3 whole-system Φ > 1e-9 at every nonzero rate under
  `mix`. One rate at or below 1e-9 refutes.
- H3 (extremes keep the full group under correlation): OR3 and AND3 have the full group as the major
  complex in every maximum-φ state at every nonzero rate under `common` and `mix`. One failure refutes.
- H4 (interior never binds the full group): under no model and no nonzero rate is the full group MAJ3's
  maximum-φ major complex. One case refutes.
- H5 (node-count regularity, backlog item 3): in every MAJ3 case with whole-system Φ > 1e-9, the largest
  core φ equals 4 × whole-system Φ within 1e-6 relative. One failure refutes.
