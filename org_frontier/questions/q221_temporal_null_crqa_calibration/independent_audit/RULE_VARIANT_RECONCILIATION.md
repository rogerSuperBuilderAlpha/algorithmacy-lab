# Critical rule-variant reconciliation — do not pool A/B results

**Status:** adversarial audit finding, 2026-10-15. This is not a new confirmatory analysis.

The repository's `identifiability/phi_detail.py` defines:

- A_self: `X'=X, Y'=Y, H'=H`.
- B_xor: `X'=X, Y'=Y, H'=X XOR Y`.

Some earlier independent exploratory experiments instead define:

- B_xor_memory: `X'=X, Y'=Y, H'=H XOR X XOR Y`.

These **are different transition systems**. The difference cannot be reconciled by changing a label. The previously reported H self-lag-one match near 0.50, higher-order XOR diagnostic, and CMI values must be associated with their exact rules, noise convention, stationary law, and conditioning set.

The pinned-PyPhi log `identifiability/results/phi_detail.txt` reports for **B_xor** `I(H'; X,Y | H)=0.410781` bits, whereas the often-cited `1-h2(0.08)=0.597821` bits applies to a different channel/update configuration. It also reports q161 major-complex targets of single-node complexes and empty bottleneck sets for both A_self and B_xor. These are not eligible positive bottleneck targets.

## Required corrections and tests

1. Define an immutable, explicit truth-table fixture for **each** variant. Record little-endian state indexing, deterministic TPM, causal connectivity, and noisy 0.08-flip TPM separately.
2. Compute the exact stationary law for each noisy chain. Do not substitute the deterministic reachable-state distribution when evaluating CMI of noisy trajectories.
3. Calculate `I(H_{t+1}; X_t,Y_t | H_t)` by enumerating the joint distribution for **each** variant and compare to an independent entropy-based calculation.
4. Run finite-sample prominence comparisons using exactly the same rule fixture as the corresponding exact-Φ calculation. Do not copy results between variants.
5. Report which cross-channel profile equivalence claims hold for each variant. Distinguish all-lag population equality from finite-sample feature-distribution equality.
6. Preserve prior exploratory outputs as historical artifacts; correct the mapping of results to variants rather than rewriting old numbers.
7. If the bounded search yields a candidate, pin its complete truth table, eligibility criteria, q161 exact-Φ outputs, and independently reproduced profile equivalence. A successful search is still exploratory and must be independently validated.

## Decision

**NO-GO** for an IIT-specific claim based on either existing A/B variant. **GO** for transparent reconciliation and a separately validated, nondegenerate candidate if the bounded search supplies one.

The earlier independent finite-sample data files are not to be interpreted as exact-Φ verification of the repository's B_xor system until their rule fixtures are reconciled.
