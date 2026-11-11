# Exact-Φ gate: decision rules (fixed by Hassan, 2026-10-15)

The numbered rules below are reproduced verbatim from Hassan's instruction (relayed 2026-10-15, about
12:22 ET). This file was committed before the post-rules exact-Φ computation and before the post-rules
bounded search.

## Chronology disclosure (honest record)

These rules arrived *after* some computation had already run:

- **Already computed before the rules.** The exact-Φ targets for the in-family A/B pair, and a first
  exact-profile check, ran at ~12:17–12:19 ET. Raw outputs: `identifiability/results/pre_rules/check_ab.txt`
  and `identifiability/results/pre_rules/phi_detail.txt`.
- **Partial search, killed.** A first bounded search ran pre-rules. It was killed at 12:22:33 ET, at group
  650/2823, and its partial log is kept unchanged in `identifiability/results/pre_rules/`.
  - It did not check isomorphism under relabeling (rule 7).
  - It did not check tie or tolerance margins (rule 2).
  - Its "found 84" count is therefore not a result.
- **Re-run after this commit.** Both computations are run again from scratch with an empty Φ cache, and the
  search now has the rule-7 isomorphism exclusion and the rule-2 margin checks. Only the post-commit outputs
  in `identifiability/results/` are used for the decision.
- **Disclosed, not hidden.** The pre-rules A/B Φ values were seen before these rules were written down. Since
  the A/B computation is deterministic, the re-run can only reproduce those values. This is disclosed rather
  than hidden.

## Rules (verbatim)

1. Reject the original pair as an IIT-bottleneck counterexample if EITHER system lacks an eligible, nondegenerate structural target. A difference in TPM or Φ alone is insufficient.
2. If both targets are eligible and differ, independently reproduce the exact-Φ calculation. Compare major complexes, Φ values, leave-one-node-out drops and bottleneck sets. Check that the difference exceeds numerical tolerance and is not a tie-breaking artifact.
3. A 30-minute bounded search is authorized if the original pair fails. Search 3-node Boolean systems using cheap analytical and recurrence-profile filters first; run PyPhi only on promising candidates.
4. Require genuine recurrence equivalence. Verify population profiles analytically or via TPM calculation, not via Monte Carlo similarity. Record the lag range and whether equivalence holds beyond it (an all-lag argument if possible).
5. Keep finite-sample distinguishability separate.
6. Stop when the budget is exhausted. A failed search is INCONCLUSIVE, not proof of nonexistence. Don't extend it automatically.
7. Node-label symmetry: check transition-system isomorphism under all 6 permutations of 3 node labels. Pairs that differ only by relabeling don't count.
8. Compute exact-Φ targets on the DETERMINISTIC rule TPM (q161 convention), never on the 8%-noise TPM.
9. Use the repo's pinned PyPhi in an isolated venv. Don't modify other environments or the historical q161/q220 outputs.
10. Independently verify the CMI values: 0 bits for A and 0.59782081 bits for B.
11. Record all candidates tested, exclusions, compute cost, software versions and reproducibility info.
12. Claim no new IIT-specific result unless the evidence supports it.
13. Don't open a PR or change the historical record.

## Operational definitions used to apply the rules

These are fixed now, before the post-rules runs.

- **Eligible, nondegenerate target** (rule 1). This is q220's R2 inclusion rule (`q220…/stage2/forms_r2.py`):
  - the q161 `core_indices` core size is ≥ 2;
  - the q161 `bottleneck_set` B is non-empty;
  - |B| < n.

  A system with whole-system Φ = 0, or whose only complexes are single nodes, fails this.
- **Exceeds numerical tolerance / not a tie artifact** (rule 2), for a candidate pair with B_a ≠ B_b:
  - For each system, the gap between its largest leave-one-out drop and its largest drop outside B must be
    > 1e-4. That is 100 × the q161 TOL of 1e-6.
  - The core must not be a tie: no other subsystem may reach the maximal-complex φ within 1e-4 at the
    selecting state. This is checked with the per-candidate listing.
- **Recurrence equivalence** (rule 4): exact rational arithmetic (`fractions.Fraction`, flip = 2/25) on the
  noisy chain, for all 6 ordered pairs, lags 0..20 (so −20..20).
  - **All-lag argument.** The lag-k match rate of system s satisfies a linear recurrence whose order is at
    most 8, the degree of the characteristic polynomial of its 8×8 transition matrix. The difference of two
    such sequences satisfies a linear recurrence of order ≤ 16. If it vanishes at 16 consecutive lags
    (0..15), it vanishes at every lag k ≥ 0.
  - Negative lags are the reversed ordered pair, so they are covered the same way.
- **Isomorphism** (rule 7): two systems are isomorphic if one deterministic rule table equals the other under
  some permutation of the 3 node labels. With the same flip on every node, this is equivalent to the noisy
  TPMs being isomorphic. Isomorphic pairs are excluded.
- **Budget** (rules 3 and 6): 30 minutes wall-clock of the search process under `box-run`, measured from the
  start of stage 1. There is no automatic extension.
- **Software** (rule 9):
  - venv: `/workspace/algorithmacy-827-venv`, Python 3.12, numpy 2.5.4, scipy 1.18.1.
  - PyPhi: `feature/iit-4.0` at commit `b78d0e342d37175cbd55cf35a6d52ae035b4c50f`, installed from the URL
    pinned in `requirements.txt`. It is an isolated venv used only for this repo's checks, and is not
    modified.
  - Config: IIT_VERSION 4.0, REPERTOIRE_DISTANCE GENERALIZED_INTRINSIC_DIFFERENCE, PARALLEL off.
