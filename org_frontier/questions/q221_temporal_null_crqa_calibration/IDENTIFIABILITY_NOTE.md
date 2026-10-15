# q221 identifiability note: pairwise recurrence vs XOR dynamics (DRAFT, provisional)

> **Target audit (2026-10-15, `TARGET_AUDIT.md`).** The q161 bottleneck-target differences reported here exist only under q161's rule-freeze convention: the frozen node is kept as a perturbed element with its edges retained. Under an IIT background-condition reading, P and Q (and the third survivor pair) have the same target {X,H}; in the second pair, one target becomes ineligible. Major complex and Φ never differ. Pairwise **statistical** non-identifiability (target A) is unaffected.

**Status.** DRAFT. Findings are provisional. Nothing here is preregistered or confirmatory, and none of it is
an IIT-specific claim. The exact-Φ gate follows the pre-specified rules in
[`EXACT_PHI_DECISION_RULES.md`](EXACT_PHI_DECISION_RULES.md). The rules were committed in `82b3d80c`, and the
chronology is disclosed in that file. The bounded search the rules allow (rule 3) **completed within budget**
and has been adjudicated (§6, `identifiability/SEARCH_RECORD.md`).

The counterexample, the finite-sample stress test, the CMI values and the isomorphism check come from Hassan's
parallel analysis. This note reproduces them independently with the lab's own code.

## 1. Scope of the claim

The claim covers **population (expected) pairwise cross-channel match profiles only**:
P(x_i(t) = x_j(t+k)) for i ≠ j at integer lags k. It makes **no** claim that the finite-sample q220 classifier
cannot tell the systems apart (§4).

Two other kinds of information can and do separate the systems:
- auto-recurrence (each channel matched against itself);
- higher-order statistics.

## 2. Systems: the exact rules

Hassan's reported numbers fit **two different readings** of "System A / System B", so both were computed
exactly.

| reading | A | B | in q220's family (deterministic rule plus 8% flip on every node)? |
|---|---|---|---|
| **in-family** | X'=X, Y'=Y, H'=H | X'=X, Y'=Y, H'=X⊕Y | yes, so it has a q161 exact-Φ target |
| **fair-coin** | X, Y i.i.d. fair each step; H'=H (8% flip) | X, Y i.i.d. fair; H'=X⊕Y (8% flip) | **no**: a fair coin is not a deterministic rule plus 8% flip, so q161 has no target |

Hassan's Phase-10 numbers, checked exactly (`identifiability/results/ab_reproduce.txt`):

| Hassan's claim | in-family | fair-coin |
|---|---|---|
| max \|TPM_A − TPM_B\| = 0.711 | **0.710976 ✔** | 0.21 ✗ |
| both stationary laws uniform | A ✔; **B ✗** (π has entries 12443/62500 and 1591/31250; only single-node and pairwise marginals are uniform) | ✔ |
| 126 cross pair × lag values equal (lags 0–20) | **126/126 exactly equal, all = 1/2 ✔** | 126/126 ✔ |
| CMI I(H';X,Y\|H): A = 0, B = 0.59782081 bits | A = 0 ✔; **B = 0.41078149 ✗** | A = 0 ✔; **B = 0.59782081 ✔** |
| no isomorphism under the 6 label permutations | **✔ none** | — |
| H lag-1 self-match 0.92 (A) vs 0.50 (B) | 0.92 vs **0.749** | 0.92 vs 0.50 ✔ |

**Reading.** Hassan's numbers mix the two readings:
- the TPM difference matches the in-family pair;
- the uniform-B, CMI and H-autocorrelation numbers match the fair-coin pair.

**Resolved: the A/B/C variants (Hassan's naming, `independent_audit/STATIONARY_VARIANT_CORRECTION.md`).**
Every number below was recomputed in exact rational arithmetic under each variant's **own** stationary law, by
`identifiability/variants_abc.py` (output in `results/variants_abc.txt`). In all three variants X' = X and Y' = Y,
with an 8% flip on every node. This is q220's family, so each variant has a q161 deterministic target.

| variant | H rule | stationary law | H lag-1 self-match | CMI I(H';X,Y\|H) | cross pair × lag values equal to A (lags 0..20) | auto-profiles equal to A | q161 target |
|---|---|---|---|---|---|---|---|
| **A** = A_self | H' = H | uniform | 23/25 = 0.92000000 | 0 | — | — | ineligible (∅) |
| **B** = B_xor | H' = X ⊕ Y | **non-uniform** (12443/62500 ×4, 1591/31250 ×4) | 0.74893568 | 0.41078149 | 126/126 (all 1/2) | X, Y yes; H no | ineligible (∅) |
| **C** = B_xor_memory | H' = H ⊕ X ⊕ Y | uniform | 1/2 | 0.59782081 | 126/126 (all 1/2) | X, Y yes; H no | ineligible (∅, `results/ab_hassan_code.txt`) |

**Where each of Hassan's numbers comes from.**
- **C** produced his finite-sample table and the CMI 0.5978. C is the "B" in his committed
  `independent_audit/finite_sample.py`.
- The max TPM difference of 0.711 is the same for A vs B and A vs C.
- The "fair-coin" reading in the table above, where X and Y are i.i.d. fair bits, is a fourth system. It
  matches C on the H statistics only by coincidence of the uniform law, and it has no q161 target. It is
  kept only as a historical record of my earlier reconstruction.

## 3. Population cross-profiles are identical at every integer lag (analytic)

**In-family pair.**
- X and Y are independent binary symmetric Markov chains in both systems, because each reads only itself plus
  independent noise. Each is uniform at every t ≥ 0, including the uniform random start.
- In A, H is a third independent chain, so every cross pair is independent with uniform marginals. Every match
  rate is therefore 1/2.
- In B, H_t = X_{t−1} ⊕ Y_{t−1} ⊕ n_t for t ≥ 1.
  - Y_{t−1} is uniform and independent of (X_s, X_{t−1}, n_t) for every s.
  - So H_t is uniform conditional on X_s, which gives P(X_s = H_t) = 1/2 for every s and t.
  - The same argument with X and Y swapped covers Y–H.
  - X–Y are independent.
- So every ordered cross pair has match probability exactly 1/2 at every integer lag, at every time, and for
  any flip rate.
- This needs no stationarity and no warm-up.

The fair-coin reading follows the same way.

**Exact check.** Rational arithmetic with flip = 2/25 gives 126/126 values equal to 1/2 (6 ordered pairs ×
lags 0..20; negative lags are the reversed pairs).

**What does differ.**
- H's auto-profile: max |A − B| = 0.177 (in-family) and 0.42 (fair-coin).
- P(H_{t+1} = X_t ⊕ Y_t): 0.5 vs 0.92 (1.0 without noise).
- The CMI values above.

## 4. Finite-sample behaviour of q220's actual pipeline (kept separate, per rule 5)

**What the code uses.** q220's pipeline builds profiles only for distinct pairs. `stage2/observe.py`
`coupling` loops over `a < b`, and `centrality` zeroes the diagonal; it then picks the tie-aware argmax. Auto
information therefore enters only through sampling variability.

**Runs.** The pipeline used q220's own `trajectory` → `observe.coupling` (timestamp mode, full series) →
`centrality` → `bottleneck_scores`, with the stage-2 settings: 600 steps after 20 warm-up, MAX_LAG 10, floor
0.05, MIN_PAIRS 30. Each system got 400 trajectories.

| statistic | in-family A | in-family B | fair-coin A | fair-coin B | Hassan A / B (400 runs) | Hassan rerun A / B (200 runs) |
|---|---|---|---|---|---|---|
| mean max pair prominence | 0.0617 | 0.0590 | 0.0418 | 0.0482 | 0.0627 / 0.0542 | 0.0628 / 0.0556 |
| mean max centrality | 0.0571 | 0.0532 | 0.0130 | 0.0265 | 0.0610 / 0.0378 | 0.0668 / 0.0435 |
| any pair > 0.05 | 58.8% | 59.3% | 22.3% | 39.3% | 64.5% / 47.0% | 66% / 53% |
| no-evidence | 41.2% | 40.7% | 77.8% | 60.8% | — | 34% / 47% |
| H lag-1 self-match | 0.920 | 0.750 | 0.920 | 0.501 | 0.920 / 0.501 | — |

Seeds: 41000–41399 (in-family) and 42000–42399 (fair-coin). Standard errors are in
`identifiability/results/finite_sample_*.txt`.

**Reading.**
- **In-family pair:** the pipeline's outputs are close at R = 400. A has slightly higher prominence (0.0617 vs
  0.0590, about 1.5 SE), and the evidence rates are equal.
- **Fair-coin pair:** the direction is *reversed* from Hassan's table.
- **Resolved.** His finite-sample A/B row is variant **A vs C** (see §2). His committed
  `independent_audit/finite_sample.py` was rerun in the pinned repo environment: Python 3.12.15, numpy 2.5.4,
  q220 `stage2.observe`. Every value is **bit-identical** to his committed
  `finite_sample_original_reproduction.json`: prominence 0.06265039 / 0.05416296, centrality 0.06100022 /
  0.03782560, P(prom > 0.05) 0.645 / 0.470, H self-match 0.92002087 / 0.50138982. The output is in
  `results/pinned_env_runs/finite_sample_results.json`.
- His `null_pilot.py` was also rerun in the pinned environment and reproduced `null_pilot_results.json`
  byte-for-byte. The `test_rule_variants.py` regression tests also pass there (2 of 2).

## 5. Exact IIT 4.0 targets (lab instrument, deterministic TPM, rule 8)

**Instrument.**
- Functions: q161 `core_indices`, `bottleneck_set` and `mc_phi`; `probes.lib.verdict`.
- PyPhi: `feature/iit-4.0` at `b78d0e34`, IIT_VERSION 4.0, GENERALIZED_INTRINSIC_DIFFERENCE.
- Output: `identifiability/results/phi_detail.txt`. The post-rules run is byte-identical to the pre-rules run.

| | in-family A (self-copy ×3) | in-family B (X, Y self-copy; H = X⊕Y) |
|---|---|---|
| connectivity | self-loops only | X→X, Y→Y, X→H, Y→H; H has no outputs |
| whole-system verdict max Φ | 0.0 | 0.0 |
| system φ per candidate (every reachable state) | X 1, Y 1, H 1; every 2- and 3-node set 0 | X 1, Y 1, **H 0**; every 2- and 3-node set 0 |
| q161 `core_indices` | (H,), Φ = 1 — a **three-way tie**; H is returned only by first-max tie-breaking | (Y,), Φ = 1 — a **two-way tie** with X |
| mc Φ | 1.0 | 1.0 |
| leave-one-out drops (X, Y, H) | 0, 0, 0 | 0, 0, 0 |
| q161 `bottleneck_set` | **∅** | **∅** |
| eligible target? (core ≥ 2, B ≠ ∅, \|B\| < n) | **no** | **no** |

**Decision (rule 1): REJECTED as an IIT-bottleneck counterexample.**
- Neither system has an eligible, nondegenerate target. Both are sub-dyadic with an empty bottleneck set.
- q161's `build_corpus` and q220's R2 selection would both exclude them.
- One real IIT-level difference does exist: H forms a (single-node) complex in A but not in B. It is not a
  bottleneck difference, and rule 1 says a Φ difference alone is insufficient.
- The fair-coin reading has no q161 target at all.

## 6. Bounded search (rule 3): completed; one representative pair independently reproduced

The full record is in `identifiability/SEARCH_RECORD.md`.

**The search.**
- Space: 8192 three-node forms in q220's family.
- Wall time: 290 s of the 1800 s budget, with all 2823 groups examined.
- Result: 74 candidate pairs, unique up to node permutation × value relabelling, with exactly equal
  population cross-profiles and different, eligible q161 bottleneck sets.

**Adjudication.**
1. 67 pairs have no constant-rule node.
2. 63 of those also pass the core tie-gap check.
3. Of the 63, **60 differ in auto-profiles**. Only **3** pairs agree on every pairwise statistic:
   cross-profiles, auto-profiles and marginals.

**The representative pair.** P: X'=¬H, Y'=X⊕Y, H'=X⊕H vs Q: same, except Y'=¬(X⊕Y⊕H).
- Major complex {X, H}, Φ = 2, and per-state φ are identical in P and Q.
- The q161 bottleneck set B differs: {X, H} vs {H}. The leave-one-out drop for X is 2 in P and 1 in Q.
- The B difference was reproduced by q161 code and by an own PyPhi loop at clamp 0 and clamp 1.
- The B margin is ≥ 1, so it is not a tie artifact.
- The pair is not 48-group isomorphic.
- Cross- and auto-profiles are exactly equal at lags 0..40, hence at every lag.
- Finite sample: q220's pipeline outputs are indistinguishable at R = 400, but its score against the q161
  target is 0.64 for P and 0.33 for Q.

**Stricter exact screen (Hassan, 2026-10-15).** The 7488 raw candidates were screened in exact arithmetic,
in stages. Pairs remaining at each stage (raw pairs, then unique up to the 48-group):

| stage | raw pairs | unique up to the 48-group |
|---|---|---|
| all candidates | 7488 | 74 |
| no constant node | 6816 | 67 |
| + equal stationary channel marginals | 6432 | 67 |
| + equal self-recurrence profiles, lags 0..20 | 180 | 3 |
| + not isomorphic | 144 | 3 |

**Survivors.** The 3 survivors are all GF(2)-affine; none is from the R2 family. P/Q is the lead.

**Finite sample, Hassan's script.** His committed `candidate_finite_sample.py` was run on P/Q in the pinned
environment with seeds 0..299. The tie-aware BN score was 0.661 for P and 0.333 for Q, against set-size chance
of 0.667 and 0.333. So the q220 decoder is at chance on both systems.

**Three-point statistics still separate the pair.** P(Y_{t+1} = X_t ⊕ Y_t) is 0.92 in P and 0.5 in Q. The
finding is therefore **information loss in the pairwise (two-point) recurrence representation**, not
non-identifiability from full trajectories.

**Rule-12 reading.**
- The two systems differ only in a node outside the major complex.
- So this is a **non-identifiability of the q161 leave-one-out bottleneck target from pairwise recurrence**,
  inside q220's family.
- It is **not** a difference in IIT 4.0's major complex or Φ, and it is not an IIT-specific result.
- It also shows the q161 target can change with a rule outside the complex. That is a property of the target
  definition, worth flagging for any study that uses it as ground truth.

## 7. Novelty (honest)

**Classical:** pairwise statistics miss XOR-type synergy.
- The binary XOR, where each input alone carries no information, is the textbook synergy example. Williams &
  Beer 2010 (arXiv:1004.2515, full text checked) use exactly this example.
- Connected information (Schneidman, Still, Berry & Bialek 2003, PRL 91:238701; abstract checked).
- Shannon measures cannot separate dyadic from polyadic dependency (James & Crutchfield 2017, *Entropy*
  19:531; arXiv abstract checked).
- O-information for higher-order interdependence (Rosas, Mediano, Gastpar & Jensen 2019, PRE 100:032305;
  abstract checked).
- Gilpin 2025 (PRX 15:011005, full text §III.2) shows *shared* recurrences recovering multiplicative
  higher-order drivers that pairwise network-inference methods miss.

So "pairwise recurrence profiles do not identify XOR dynamics" is a known phenomenon in a new costume.

**IIT-specific consequence.** It would only matter for CRQA→Φ bottleneck inference if an eligible pair with
different targets exists. The original pair fails that test (§5). The search found eligible pairs (§6), but the targets differ
only through the q161 leave-one-out operationalisation, not through the major complex or Φ. **No IIT-specific
claim is made.** The narrow, defensible contribution is the following. Within the lab's own Boolean family,
there are pairs whose pairwise recurrence statistics (cross and auto) are equal at every lag but whose q161
bottleneck targets differ. So pairwise recurrence cannot be a consistent estimator of that target across the
family. This is an exploratory, single-search finding. It needs locked, independent validation.

## 8. Limitations

- Systems are 3 nodes and synchronous; the q161 Φ convention is used (deterministic TPM, max over reachable
  states, clamp-to-0 leave-one-out).
- Population equivalence is shown only for cross-pair match rates. Joint pair distributions are also equal
  for the in-family pair, because the cross pairs are independent with uniform marginals. That fails for
  general groups found by the search.
- The finite-sample comparisons are Monte Carlo at R = 400 and support no identifiability statement.
- Hassan's generators are now pinned (§2: his finite-sample table is A vs C).
- The search covers only the `nsi` and GF(2)-affine three-node families. No R2-family (`nsi`–`nsi`) pair survives the value-relabelling check.
