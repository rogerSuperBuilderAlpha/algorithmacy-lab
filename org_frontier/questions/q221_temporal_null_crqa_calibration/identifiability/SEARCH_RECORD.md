# Bounded exact-Φ search: completion record (rules 3, 6, 7, 11)

> **Target audit (2026-10-15, `TARGET_AUDIT.md`).** The q161 bottleneck-target differences reported here exist only under q161's rule-freeze convention: the frozen node is kept as a perturbed element with its edges retained. Under an IIT background-condition reading, P and Q (and the third survivor pair) have the same target {X,H}; in the second pair, one target becomes ineligible. Major complex and Φ never differ. Pairwise **statistical** non-identifiability (target A) is unaffected.

**State: COMPLETED within budget.** It was not stopped by the budget and it did not crash.
- Groups examined: 2823 of 2823.
- Search phase: 285.3 s wall. Including the exact re-verification of 20 pairs: 290.4 s. The budget was 1800 s.
- Run: `box-run` job `q221-pair-search-post`, which waited 53 s in the queue and ran 290 s with rc = 0.
- Log: `results/pair_search.txt` (finished 12:29:24 ET). Full output: `results/pair_search.json`.

**Why the branch showed "group 200/2823".** Commit `4465a8d6` (12:25 ET) captured `results/pair_search.txt`
while the run was still in progress. The complete log is committed with this record.

**Pre-rules run.** An earlier run was killed and quarantined; it is disclosed in `../EXACT_PHI_DECISION_RULES.md`
and is not used here.

## Space and filters (fixed in the rules commit `82b3d80c`)

**Space.** 8192 three-node forms in q220's family (deterministic rule plus 8% flip on every node):
- 4096 q162 `random_wiring` forms with no self-inputs (`nsi`, which is q220's R2 family);
- 4096 forms whose rules are GF(2)-affine over all three nodes (`aff`).

**Pipeline.**
1. Exact population cross match profiles for all 6 ordered pairs, lags 0..20 each way. These are numpy linear
   algebra on the noisy 8-state chain, grouped at 1e-9.
2. The q161 `core_indices` and `bottleneck_set` targets, computed only for forms in multi-member groups, once
   per node-permutation orbit, on the **deterministic** TPM (rule 8).
3. Exclusions:
   - ineligible targets (rule 1, using q220 R2's rule: core ≥ 2, B ≠ ∅, |B| < 3);
   - pairs isomorphic under any of the 6 node permutations (rule 7);
   - B margin ≤ 1e-4 (rule 2).
4. Exact rational re-verification of profile equality (`fractions`, flip = 2/25) and a core tie-gap check for
   the first 20 unique pairs.

## Accounting

| quantity | count |
|---|---|
| forms | 8192 |
| distinct cross-profile classes | 2999 |
| classes with > 1 member (examined) | 2823, covering 8016 forms |
| forms whose q161 targets were evaluated | 8016, i.e. 1362 Φ orbits |
| forms excluded as ineligible targets | 4656 |
| groups with ≥ 2 eligible members | 901 |
| eligible pairs excluded as node-permutation isomorphic (rule 7) | 420 |
| non-isomorphic eligible pairs with different B | 7488 |
| … of which pass the B margin > 1e-4 | 7488 |
| unique up to node relabeling | 689 (`pair_search`) |
| exactly re-verified (rational profiles, lags −20..20) + core tie gap > 1e-4 | **20/20 pass** |

## Follow-up (`verify_candidates.py`, `results/verify_candidates.{txt,json}`; 27 s)

**A stricter isomorphism check.** Rule 7 covers node permutations only. Each candidate was also checked against
the 48-element group of node permutations × per-node 0/1 value relabelings:
- 1008 of the 7488 pairs are the same transition system with renamed values.
- Their B difference therefore comes only from q161's clamp-to-0 leave-one-out convention.
- **Every `nsi`–`nsi` (R2-family) pair falls in this class.**

**What remains.**
- 6480 pairs are not isomorphic under the 48-group.
- That is 589 unique up to node relabeling, and **74 unique up to the 48-group**.
- By family: 70 are `aff`–`aff` and 4 are `nsi`–`aff`.

**Independent recomputation** for 4 representatives. Each was computed three ways:
- q161 functions on hand-decoded rules;
- an own PyPhi loop (max over reachable states of `maximal_complex`, then leave-one-out) with **clamp-to-0 and
  clamp-to-1**;
- exact rational profiles.

All three agree.

### Simplest verified pair (example)

| | P1 = `nsi (0,3,3)` | P2 = `aff (6,9,5)` |
|---|---|---|
| rules (deterministic) | X' = 0; Y' = ¬H; H' = ¬Y | X' = X ⊕ Y; Y' = ¬H; H' = ¬Y |
| q161 core, Φ | {Y, H}, 2.0 | {Y, H}, 2.0 |
| leave-one-out drops (X, Y, H), clamp 0 | 0, 2, 2 | 0, **1**, 2 |
| same, clamp 1 (own code) | 0, 2, 2 | 0, 1, 2 |
| bottleneck set B | **{Y, H}** | **{H}** |
| core tie gap / B margin | 2.0 / 2.0 | 1.0 / 1.0 |
| eligible | yes | yes |

**Profile equality.** The cross profiles are exactly equal for all 6 ordered pairs at lags −20..20, in
rational arithmetic. They are not all 1/2. The all-lag argument from the rules file then applies: each profile
satisfies a linear recurrence of order ≤ 8, so the difference has order ≤ 16, and 21 consecutive equal lags
give equality at every integer lag.

**Why B differs.**
- In P2, clamping Y leaves X' = X ⊕ 0 = X, a self-loop complex with φ = 1. The residual major-complex Φ is
  therefore 1 and the drop is 1.
- In P1, X is constant, so nothing survives and the drop is 2.
- The intact major complex and its Φ are **identical** in both systems. The targets differ only through the
  residual complex that the q161 leave-one-out definition counts after clamping. That complex sits on a node
  **outside** the major complex.

**What does distinguish the pair.**
- X's marginal: in P1, X_t is i.i.d. Bernoulli(0.08); in P2, X is uniform.
- X's auto-profile.
- `results/candidate_marginals.{txt,json}` (same/different marginal means and auto-profiles across all 74 pairs)
  is queued in `box-run`. **Pending.**

## Outcome under the fixed rules (exploratory; Hassan adjudicates)

**Rules 1–4 and 7.**
- Non-degenerate, eligible q161 bottleneck sets differ by much more than tolerance and are not tie artifacts.
- The pairs are not node-permutation isomorphic, and 74 of them are not even value-relabeling isomorphic.
- Population pairwise cross match profiles are **exactly equal at every integer lag**.

**What may and may not be claimed (rule 12).**
- *May claim:* within q220's model family, the population mean pairwise cross-profile representation does not
  identify the q161 leave-one-out bottleneck target.
- *May not claim:*
  - that the major complex or its Φ differs (it does not, in the example above);
  - that finite-sample q220 classifiers cannot tell these systems apart (rule 5). Univariate marginals
    already separate the example.
- *Not shown for the R2 family:* every R2-family (`nsi`–`nsi`) pair is a value-relabeling artefact of the
  clamp-to-0 convention.

Per Hassan's reconciliation note, any found pair is an **exploratory discovery**. It still needs a fresh,
independent validation under a locked protocol.

## Software and reproducibility (rule 11)

- Python 3.12 venv at `/workspace/algorithmacy-827-venv`: numpy 2.5.4, scipy 1.18.1.
- PyPhi: `feature/iit-4.0` at `b78d0e342d37175cbd55cf35a6d52ae035b4c50f`, IIT 4.0,
  GENERALIZED_INTRINSIC_DIFFERENCE, PARALLEL off.
- No randomness anywhere in the search.
- Reproduce from the repo root:
  ```
  python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.pair_search
  python -m org_frontier.questions.q221_temporal_null_crqa_calibration.identifiability.verify_candidates
  ```

## Adjudication (`adjudicate.py`, `results/adjudicate.{txt,json}`; 37 s) and final independent check (`rep_verify.py`, `results/rep_verify.txt`; 28 s)

This completes the bounded-search verification. No further search was run (rule 6; Hassan's finish line).

**Filtering the 74 candidates (unique up to the 48-group):**

| step | pairs left |
|---|---|
| bounded-search candidates, unique up to node permutation × value relabelling | 74 |
| drop pairs with a constant-rule node in either member (degenerate observation channel) | **67** |
| drop pairs where either member's q161 core is within 1e-4 of a competing complex (tie gap) | **63** (61 `aff`–`aff`, 2 `nsi`–`aff`) |
| … whose univariate marginal means are also equal | 63 |
| … whose 3 auto-profiles (lags 0..20) are also exactly equal | **3** |

The B margin is ≥ 1.0 for every member of every pair. So, for 60 of the 63 surviving pairs, **auto-recurrence
alone tells the two systems apart**. Only 3 pairs agree on every pairwise statistic: cross-profiles, auto-profiles
and marginals.

### The representative surviving pair, independently reproduced

These are the first of the 3 pairs: `aff (9,6,10)` = **P** and `aff (9,15,10)` = **Q**. Both are in q220's family:
a deterministic rule plus an 8% flip on every node.

| | P | Q |
|---|---|---|
| rules | X' = ¬H; **Y' = X ⊕ Y**; H' = X ⊕ H | X' = ¬H; **Y' = ¬(X ⊕ Y ⊕ H)**; H' = X ⊕ H |
| stationary law (noisy chain) | uniform | uniform |
| system φ of every candidate subset, in every reachable state | identical to Q: XH = 2; Y = H = 1; X = 0 or state-unreachable; XY = 0 or unreachable; YH = XYH = 0 | identical to P |
| major complex, Φ | {X, H}, 2.0 | {X, H}, 2.0 |
| leave-one-out drops (X, Y, H): q161 / own clamp-0 / own clamp-1 | 2, 0, 2 (all three agree) | **1**, 0, 2 (all three agree) |
| q161 bottleneck set B | **{X, H}** | **{H}** |
| core tie gap / B margin | 1.0 / 2.0 | 1.0 / 1.0 |
| isomorphic under the 48-group | no | |
| exact cross-profiles, 6 ordered pairs × lags 0..40 | equal | |
| exact auto-profiles, 3 nodes × lags 0..40 | equal | |

**What this pair shows.**
- The two systems differ **only in the rule of Y**, a node outside the major complex.
- The intact major complex, its Φ, and the per-state φ of every candidate subset are identical.
- The q161 bottleneck targets still differ, by more than any tolerance and under either clamp value.
- So the difference is a property of the q161 **leave-one-out bottleneck operationalisation**: the residual Φ
  after removing X depends on the out-of-complex node Y. It is not a difference in IIT 4.0's major complex or Φ.
- The mechanism of the residual difference was not dissected further, because that would be a new audit.

**Recurrence equivalence (rule 4).** Profile equality was shown in exact rational arithmetic for lags 0..40
each way. The linear-recurrence argument from the rules file extends it to every integer lag.

**Finite sample (rule 5).** q220's actual `stage2` pipeline was run with R = 400 trajectories per system: 600
steps after 20 warm-up, MAX_LAG 10, floor 0.05, MIN_PAIRS 30. Both systems used the same seeds, `default_rng(43000 + r)` (common random numbers). Values are mean ± SE.

| statistic | P | Q |
|---|---|---|
| max pair prominence | 0.0607 ± 0.0010 | 0.0606 ± 0.0009 |
| any pair over the floor | 68.0% ± 2.3 | 69.3% ± 2.3 |
| tie-aware pick share X / Y / H | 0.329 / 0.357 / 0.314 | 0.308 / 0.363 / 0.330 |
| tie-aware BN score vs **own** target | 0.643 ± 0.013 | **0.330 ± 0.014** |
| tie-aware BN score vs the **other** system's target | 0.314 | 0.638 |

- At this R, q220's output distribution is the same for P and Q within sampling error.
- Its score against the q161 target is not the same: 0.64 vs 0.33.
- The pipeline "succeeds" on P and fails on Q for a reason it has no access to.
- These are Monte Carlo summaries at one R. They are **not** a proof that the finite-sample estimator
  distributions are equal. Higher-order statistics, such as three-point or joint-pattern statistics, could
  still differ.

**Status.** Exploratory discovery under the fixed rules. It still needs fresh, independent validation under a
locked protocol before any claim is made. It is an observation about the lab's q161 bottleneck target, not
an IIT 4.0 result (rule 12).

## Stricter exact screen over all 7488 candidates (`screen_exact.py`, `results/screen_exact.{txt,json}`; 108 s; no new search)

Hassan asked for this screen on 2026-10-15, after he showed that the first candidate (`nsi (0,3,3)` vs
`aff (6,9,5)`) is trivially separated by X's marginal: 7.97% vs 50.02%.

**Method.**
- Every stage uses exact rational arithmetic with flip = 2/25.
- The stationary law is the noisy chain's own, solved exactly and checked with π P = π.
- The screen covers all 7488 raw candidate pairs, not only the 74 representatives. This matters because value
  relabelling changes the marginals.

| stage | raw pairs | unique up to node permutation | unique up to the 48-group, not isomorphic |
|---|---|---|---|
| S0: all bounded-search candidates | 7488 | 689 | 74 |
| S1: no constant-rule node in either member | 6816 | 593 | 67 |
| S2: + equal stationary channel marginals P(x_i = 1) | 6432 | 525 | 67 |
| S3: + equal self-recurrence profiles, 3 channels × lags 0..20 | **180** | 30 | **3** |
| S4: + exact cross-profile re-check, 6 ordered pairs × lags 0..20 | 180 | 30 | 3 |
| S5: + not 48-group isomorphic | 144 | 24 | **3** |

**Survivors.**
- The 3 surviving pairs, unique up to the 48-group, are all `aff`–`aff`. None is in q220's R2 (`nsi`) family.
- Every survivor has marginals of 1/2 on all three channels.
- The survivors are:
  - `aff (9,6,10)` vs `aff (9,15,10)`, the lead;
  - `aff (9,6,10)` vs `aff (9,15,12)`;
  - `aff (9,6,11)` vs `aff (9,14,10)`.
- In all three, the q161 core tie gap is 1.0 and the B margin is at least 1.0 (`adjudicate.txt`).

**Lead example: P = `aff (9,6,10)`, Q = `aff (9,15,10)`.**
- The exact-Φ results in the pinned environment are in the table above (`rep_verify.txt`).
- Hassan's committed `independent_audit/candidate_finite_sample.py` was rerun on this pair in the pinned
  environment. It used his `simulate` and `measure` unmodified, with seeds 0..299 for each system. The wrapper
  is `lead_pair_finite_sample.py` and the output is
  `results/pinned_env_runs/lead_pair_finite_sample.json`.

| | P (B = {X, H}) | Q (B = {H}) |
|---|---|---|
| mean max prominence | 0.0605 | 0.0617 |
| mean max centrality | 0.0608 | 0.0609 |
| any prominence > 0.05 | 69.3% | 66.7% |
| no evidence | 30.7% | 33.3% |
| tie-aware BN score vs own target (± SE) | 0.661 ± 0.016 | 0.333 ± 0.016 |
| set-size chance | 0.667 | 0.333 |
| score vs the other system's target | 0.337 | 0.662 |

**Reading (exploratory, one form per system).**
- On the q220 decoder's inputs, P and Q look the same.
- On both systems the decoder scores at set-size chance. The difference between its two scores comes only
  from the size of the target set.
- This agrees with the R = 400 run on seeds 43000+ (`adjudicate.txt`: 0.643 and 0.330).

**What still separates P and Q.**
- P and Q are identical on every one- and two-point statistic tested: marginals, auto-profiles and
  cross-profiles at every lag.
- They are **not** observationally equivalent as full processes. A three-point statistic separates them at
  once: P(Y_{t+1} = X_t ⊕ Y_t) is 0.92 in P and 0.5 in Q. Q's Y-update equals X⊕Y only when H = 1, and H is
  uniform.
- So the result is **information loss of the pairwise (two-point) recurrence representation**, univariate and
  cross. It is not structural non-identifiability from the full trajectory.

## Isomorphism check of Hassan's matched candidate `aff (6,9,5)` vs `aff (11,9,5)` (`iso_check_hassan_pair.py`, `results/iso_check_hassan_pair.txt`)

**Rules.**
- a: X' = X ⊕ Y; Y' = ¬H; H' = ¬Y.
- b: X' = ¬(X ⊕ H); Y' = ¬H; H' = ¬Y.

**Shared statistics (exact).** No constant node in either system. All three marginals are 1/2. Self-recurrence
and cross-recurrence profiles are equal at lags 0..20.

**The isomorphism.**
- None of the 6 node permutations alone maps a to b.
- **Two of the 48 maps do.** Swap Y and H and flip the values of Y and H; flipping X as well also works.
- In closed form: set Y~ = ¬H and H~ = ¬Y in a. Then X' = X ⊕ Y = ¬(X ⊕ H~), Y~' = ¬H~ and H~' = ¬Y~. That is
  exactly b.

**Verdict: the pair is the same transition system under relabelling. It is not a counterexample.**
- Its bottleneck sets, {H} vs {Y}, are the *same* target carried through the relabelling: a's H is b's Y~.
- So the difference is not even a clamp-convention artifact.
- The exact screen above already excludes this pair at stage S5. It counts among the 180 − 144 = 36 raw S4
  pairs that are 48-group isomorphic.

The 3 non-isomorphic survivors, with P/Q as the lead, stand as recorded above. Their isomorphism status was
checked with the same 48-group canonical form (`screen_exact.ext_canon`). For P/Q it was also checked explicitly
in `rep_verify.txt`.
