# q221 identifiability note: pairwise recurrence vs XOR dynamics (DRAFT, provisional)

**Status.** DRAFT. Findings are provisional. Nothing here is preregistered or confirmatory, and none of it is
an IIT-specific claim. The exact-Φ gate follows the pre-specified rules in
[`EXACT_PHI_DECISION_RULES.md`](EXACT_PHI_DECISION_RULES.md). The rules were committed in `82b3d80c`, and the
chronology is disclosed in that file. The bounded search the rules allow (rule 3) is **still running**, so §6
is pending.

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

**Open item for Hassan:** pin the exact rules behind each of his tables.

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
- **Neither reading reproduces his A/B finite-sample row.** That is further evidence that his rules differ
  from both. *Not resolved; needs his exact generator.*

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

## 6. Bounded search (rule 3): PENDING

**Space.** 8192 three-node forms:
- every q162 `random_wiring` form, with no self-inputs (q220's R2 family);
- every GF(2)-affine form with self-inputs.

**Filters.**
1. Exact profile grouping (numpy).
2. q161 targets only inside groups with more than one member, one computation per relabeling orbit.
3. Exclusions:
   - ineligible targets (rule 1);
   - isomorphic pairs (rule 7);
   - B margin ≤ 1e-4 (rule 2).
4. Exact rational re-verification of candidates, with a core tie-gap check.

**Budget.** 30 minutes of wall time.

A pre-rules partial run was killed and quarantined unread (see the rules file). Results go here when the run
finishes.

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
different targets exists. The original pair fails that test (§5), and the search is pending (§6). **No
IIT-specific claim is made.**

## 8. Limitations

- Systems are 3 nodes and synchronous; the q161 Φ convention is used (deterministic TPM, max over reachable
  states, clamp-to-0 leave-one-out).
- Population equivalence is shown only for cross-pair match rates. Joint pair distributions are also equal
  for the in-family pair, because the cross pairs are independent with uniform marginals. That fails for
  general groups found by the search.
- The finite-sample comparisons are Monte Carlo at R = 400 and support no identifiability statement.
- Hassan's exact generator is not pinned (§2, §4).
