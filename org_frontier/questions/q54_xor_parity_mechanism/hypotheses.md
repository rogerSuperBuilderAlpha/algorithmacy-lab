# Q54 — Stage 3 hypotheses (fixed before computation)

Five working hypotheses on which structural feature of XOR parity back-channels enables Φ=2.0 restoration
on matched-read implication forms when conjunctive AND/OR gates cap at 0.830075. Written and committed
before any test runs. Grows from Q53 probes #167 and #169.

## H1 — Channel-gate bijectivity is necessary and sufficient for Φ=2.0
- **Claim:** Every (topology, form) pair that reaches Φ=2.0 uses a bijective gate in the coupled bit on
  every active channel edge; no pair with a non-bijective monotone gate reaches the ceiling.
- **H0:** At least one Φ=2.0 pair has a non-bijective channel gate, or at least one bijective-gate pair
  fails to reach Φ=2.0.
- **Predicted outcome:** Perfect separation: 100% of Φ=2.0 pairs bijective; 0% of non-bijective pairs at
  ceiling. H0 refuted only if both conditions hold.

## H2 — Global TPM permutation accompanies Φ=2.0 restoration
- **Claim:** Φ=2.0 under XOR back-channels requires the eight-state TPM to be a permutation (bijective
  global dynamics); monotone-gated topologies that cap at 0.830075 yield non-permutation TPMs on the same
  forms.
- **H0:** At least one Φ=2.0 pair has a non-permutation TPM, or at least one monotone-gated triadic pair
  at 0.830075 has a permutation TPM.
- **Predicted outcome:** All Φ=2.0 pairs permutation; no symmetric-AND pair at 0.830075 permutation. H0
  refuted if either exception appears.

## H3 — Seam conditional entropy peaks at Φ=2.0 XOR pairs
- **Claim:** Matched implication forms under XOR topologies that reach Φ=2.0 achieve strictly higher
  conditional entropy H(W,C|S) over the reachable-state ensemble than the same forms under symmetric-AND
  at 0.830075.
- **H0:** Mean H(W,C|S) for Φ=2.0 XOR pairs is not greater than mean for symmetric-AND pairs (difference
  ≤ 0 + 1e−6 bits).
- **Predicted outcome:** Strict positive gap in mean seam distinguishability. H0 refuted if XOR mean exceeds
  AND mean.

## H4 — One-sided Φ=2.0 requires commit-topology alignment
- **Claim:** Worker-side XOR reaches Φ=2.0 only on C-centric commits {4,11}; counterpart-side XOR only on
  W-centric {2,13}; symmetric XOR restores all eight matched forms.
- **H0:** At least one misaligned one-sided XOR pair reaches Φ=2.0, or symmetric XOR fails on any matched
  form.
- **Predicted outcome:** Zero misalignments; eight of eight symmetric at ceiling. H0 refuted on any violation.

## H5 — Parity-class gates are necessary; monotone gates never restore Φ=2.0
- **Claim:** Only parity-class channel gates {XOR, XNOR} can restore Φ=2.0 on matched implication forms;
  monotone gates {AND, OR} and mixed cross topologies never do, even when bijectivity holds elsewhere.
- **H0:** At least one monotone-gated pair reaches Φ≥2.0 − 1e−9, or at least one XNOR topology fails to
  reach Φ=2.0 on a form where symmetric XOR succeeds.
- **Predicted outcome:** Zero monotone at ceiling; XNOR mirrors XOR on the symmetric panel (eight of eight
  at 2.0). H0 refuted if monotone hits ceiling or XNOR underperforms XOR.
