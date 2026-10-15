# q221 validation gates (Hassan, 2026-10-15): status and evidence

Status key:
- **MET:** done, with evidence committed.
- **PARTIAL:** done in part; the open part is listed.
- **OPEN:** not done.

No gate below licenses a confirmatory claim. All work is exploratory.

## Pre-gate checks

| check | status | result | evidence |
|---|---|---|---|
| Isomorphism of aff(6,9,5) vs aff(11,9,5) under the 6 node permutations and the 48-group | MET | No node permutation alone maps one to the other. **2 of the 48 maps do**: swap Y and H and flip the values of Y and H (flipping X as well also works). **Isomorphic, so not a counterexample.** | `identifiability/iso_check_hassan_pair.py`, `results/iso_check_hassan_pair.txt` |
| Exact screen of all 7488 pairs | MET | Raw: 7488 → 6816 (no constant node) → 6432 (+ equal marginals) → 180 (+ equal self-recurrence, lags 0..20) → 180 (+ equal cross-recurrence, lags 0..20) → **144 non-isomorphic**. That is 24 unique up to node permutation and **3 unique up to the 48-group**. | `identifiability/screen_exact.py`, `results/screen_exact.{txt,json}` |

## Gates

| # | gate | status | evidence and notes |
|---|---|---|---|
| 1 | Independent pinned-PyPhi rerun for the strongest surviving candidate, covering state and clamp conventions, tie handling and eligibility | **MET** (one independent implementation besides q161's) | **Candidate:** lead pair P = aff(9,6,10), Q = aff(9,15,10). All 3 survivors have tie gap 1.0 and B margin ≥ 1.<br>**Setup:** PyPhi `feature/iit-4.0` @ `b78d0e34`, IIT 4.0, GENERALIZED_INTRINSIC_DIFFERENCE, deterministic TPM (rule 8).<br>**Implementations:** q161 `core_indices` / `bottleneck_set`, plus an own loop (max over reachable states, leave-one-out with clamp-to-0 **and** clamp-to-1). Both agree. Per-state system φ is listed for every subset in every reachable state, and it is identical in P and Q.<br>**Ties:** competing-complex gap 1.0 in both systems.<br>**Eligibility (q220 R2 rule: core ≥ 2, B ≠ ∅, \|B\| < 3):** both pass. P: core {X,H}, B {X,H}. Q: core {X,H}, B {H}.<br>Files: `identifiability/rep_verify.py`, `results/rep_verify.txt`.<br>**Open:** a rerun by a second person, if required. |
| 2 | Candidate finite-sample results with the repo's actual q220 implementation, not a reimplementation | **MET** for the lead pair | `identifiability/adjudicate.py` uses the repo's `org_frontier.recurrence.crqa.trajectory`, which is q220 stage 2's generator, then q220 `stage2/observe.py` `coupling` (timestamp, MIN_PAIRS 30) → `centrality` (floor 0.05) → `bottleneck_scores`. Settings: 600 steps, warmup 20, flip 0.08, lag ±10, R = 400, seeds 43000+.<br>Results: outputs match across P/Q within SE, and BN score is 0.643 / 0.330, equal to set-size chance (`results/adjudicate.txt`).<br>Hassan's `candidate_finite_sample.py` (his own simulator plus q220 `observe`) gives 0.661 / 0.333 on the same pair, and reproduces his own numbers bit-identically on his original pair (`results/pinned_env_runs/`). |
| 3 | Prespecified simple baselines (marginals, self-recurrence, transition counts and likelihood), with uncertainty across forms where applicable | **MET**, with one limit noted | The spec was committed in `35313d47` **before** the run (`identifiability/baselines_survivors.py`).<br>Test accuracy, 400 trajectories per pair:<br>• marginals: 0.46 / 0.50 / 0.52<br>• self-recurrence: 0.53 / 0.43 / 0.46<br>• cross-recurrence: 0.47 / 0.44 / 0.50<br>• transition counts: **1.000** on all three pairs<br>• transition likelihood: **1.000** on all three pairs (Wilson 95% lower bound 0.99)<br>Two near-chance intervals exclude 0.5 (0.427, 0.440). The binomial interval ignores the variance of the single fitted centroid, so these are read as fit noise.<br>**Limit:** uncertainty across independently generated forms is *not applicable*. The 3 pairs are the complete survivor set of a deterministic search, so results are reported per pair. Files: `results/baselines_survivors.{txt,json}`. |
| 4 | Targeted literature review of what is new beyond recurrence analysis and dependence-aware testing | **PARTIAL** | Claim-to-source rows were added to Hassan's matrix (`independent_audit/ADVERSARIAL_GO_NO_GO.md`), with full text checked for Yuan & Shou 2022 and 2024, Gilpin 2025, Wallot & Leonardi 2018 and Williams & Beer 2010. The register is in `literature/LITERATURE_REGISTER_DRAFT.md`.<br>**Not new:** shuffle miscalibration, circular-shift alternatives, pairwise blindness to higher-order structure.<br>**Possibly new:** the exact in-family construction with differing q161 leave-one-out targets (`FINDINGS.md`).<br>**Open:** a targeted search for prior work on IIT bottleneck or leave-one-out (perturbational) targets and their identifiability from observational statistics. Several classical sources are verified only at metadata level. |
| 5 | Strict separation in FINDINGS of exploratory search, pilot calibration, structural prediction and confirmatory evidence | **MET** | `FINDINGS.md` §1–4. The null pilot is scoped to Pearson correlation for independent binary Markov channels, with no CRQA or q220-decoder calibration claim. The conclusion is limited to Hassan's defensible wording. |

## Process constraints (held)

- No new searches after the bounded search. The exact screen re-filtered the existing 7488 candidates.
- q161 and q220 are untouched. The diff against contrib is confined to the q221 folder plus the generated
  `README.md` and `MAP.md` index rows.
- CI `ci/reproduce.py --changed-file`: all 6 checks pass.
- #842 stays a draft. Nothing was posted to Roger.

## Additional mathematical-verification gate (2026-10-15)

| Property | Status | Evidence |
|---|---|---|
| Independent exact-rational profile equality for lead P/Q at all lags | **MET** (mathematics; does not run PyPhi) | independent_audit/exact_all_lags_certificate.py and EXACT_ALL_LAGS_PROOF.md: 144 exact initial rational matches at lags 0–15; Cayley–Hamilton extends to every integer lag. Four focused local tests passed. |
| Non-isomorphism under six permutations × eight value flips | **MET** for lead pair | Independent exact rule-table enumeration in the rational script; zero mappings |
| Pinned IIT target calculation for lead pair | **MET within pinned lab environment**; separate independent external execution not claimed | identifiability/results/rep_verify.txt: core {X,H}, Phi=2 in both, B(P)={X,H}, B(Q)={H}; clamp-to-0 and clamp-to-1 agree |
| Exact full bottleneck-set identification from shared population summary | **REFUTED as universally possible for this pair**, conditional on the pinned IIT target sets | Same summary, distinct complete sets. |
| Impossibility of choosing a correct single node | **NOT ESTABLISHED; in fact this pair admits a common correct node** | H belongs to both reported sets; selecting H scores 1 under q220's tie-aware singleton scoring |
| Latest-head registered CI certificate | **TO RECHECK** after adding ci/reproduce.json manifest entry | New check q221-exact-all-lag-recurrence-proof; requires successful current-head workflow |
| Constructive population sufficiency of one-step state-conditioned node means | **MET under the stated Boolean flip model** | Independent exact-fraction reconstruction of all 24 rule bits for both lead systems using q_j(s)>1/2; independent_audit/exact_all_lags_certificate.py and EXACT_ALL_LAGS_PROOF.md. No claim of minimality or finite-sample guarantee. |
| Novelty of the exact conjunction | **UNRESOLVED** | Partial primary-source review and literature/IDENTIFIABILITY_CLOSEST_PRIOR_ART.md; no exhaustive priority certification |

Do not equate the exact set-valued insufficiency finding with poor finite-sample decoder accuracy, a different numerical Phi, different major-complex membership, or full-trajectory observational equivalence. The registered CI check proves only the mathematical recurrence side; it imports the IIT target sets from independently recorded PyPhi evidence.

