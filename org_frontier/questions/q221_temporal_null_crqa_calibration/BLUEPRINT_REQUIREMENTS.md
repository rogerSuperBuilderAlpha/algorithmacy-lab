# q221 blueprint requirements (Hassan, 2026-10-15)

A faithful summary of the research blueprint Hassan sent on 2026-10-15. Where it conflicts with
`design/FEASIBILITY_PLAN.md`, **this file wins**. Approved defaults carried over from the plan (Hassan,
same day) are listed at the end. Every later artifact in this folder is built to these requirements.

## 1. Two tracks, never substitutable

- **Track A — null calibration.** Measure the false-positive rate (FPR) under generating processes where
  the null is known to be true. The unit is the null unit. Report FPR at nominal α = 0.01, 0.05 and 0.10,
  with **0.05 primary**, and show p-value histograms.
- **Track B — structural inference.** Does recurrence predict the exact-Φ bottleneck on **held-out
  forms** better than the **strongest simple baseline**, not just better than chance?
- Keep three things distinct everywhere:
  1. *dependence detection* (is there any cross-dependence?);
  2. *surviving a null* (is the statistic beyond what a given null produces?);
  3. *structural prediction* (does it identify the Φ bottleneck?).

  A pass on one is never reported as a pass on another.

## 2. Phase 0 repo audit (before building)

Read q153, q159 and q161 (read-only), plus q220. Establish:
- how the bottleneck target is defined, and whether it depends on state;
- tie handling in both the target and the prediction;
- what the shuffle null actually tests;
- whether trajectories contain transients or are stationary;
- any fitting or tuning done on the evaluated forms;
- a reuse map.

Name the exact statistic precisely: CRQA vs cross-recurrence profile vs lagged categorical match.

## 3. Literature and novelty gate, with an explicit NO-GO

**Must cover the closest precedents:**
- Gilpin 2025, "Recurrences Reveal Shared Causal Drivers of Complex Time Series";
- the 2022 study showing naive permutation inflates FPR in autocorrelated biological time series (find it and
  verify it);
- Romano et al. 2022, JTSA, permutation tests for time-series dependence (10.1111/jtsa.12638);
- Phipson & Smyth 2010;
- Politis & Romano 1994;
- Künsch 1989;
- Schreiber 1998;
- Schreiber & Schmitz 1996 and 2000;
- Theiler 1992;
- Marwan 2007 and 2011;
- Wallot & Leonardi 2018;
- Albantakis 2023 (IIT 4.0);
- Parzen; Edelson–Krolik.

**Search** Crossref, OpenAlex, Semantic Scholar and arXiv.

**Claim-to-source matrix.** For each close work, record its question, null, data-generating process (DGP),
preserved properties, statistic, unit, limitations and relation to Q221.

**Verification.** A DOI match proves identity, not claim support. Check methods and results.

**NO-GO** if Q221 would only re-show that "naive shuffling is invalid for autocorrelated data", with no new
setting or result.

**The defensible gap:** does recurrence-based bottleneck selection track IIT-defined targets under
controlled temporal dependence, common drivers, observation processes and topology? And which nulls, if
any, give calibrated inference?

**Commit the review before any pilot code.**

## 4. A deliberately small pilot

**Systems.**
- Independent persistent binary channels.
- Common-driver channels.
- Known-coupled channels.
- Optional, if cheap: a periodic stress test and a tie stress test.

**Nulls.**
- Naive shuffle.
- Circular shift.
- One defensible model-based null (Markov).
- Block surrogates only if justified.

**Null validity certificate.** For each null, a short note covering: H0, what is preserved and what is
destroyed, assumptions, known failure cases, and expected domain of validity.

**Fitted-model nulls** must account for parameter estimation in calibration.

**p-values:** Phipson–Smyth, p = (1 + #{surrogate ≥ observed}) / (B + 1).

**Seed streams:** separate streams for generation, simulation, observation, surrogate and inference.

**Status:** the pilot is for debugging and design selection only. It is **never confirmatory**.

**The pilot checks:**
- calibration;
- preservation of nuisance dependence;
- sensitivity to coupling;
- degenerate or tied surrogate distributions;
- runtime;
- sensitivity to series length and persistence.

## 5. Non-CRQA baselines in any structural comparison

- uniform eligible-node;
- train-only class-frequency / majority;
- marginal statistics / entropy;
- autocorrelation / cross-correlation;
- tie-aware chance;
- the original CRQA procedure.

## 6. Statistics

- Hierarchy: family → form → trajectory → observation variant. Holdouts are grouped at form or family level,
  with no form leakage.
- The interval method is chosen by simulation in the pilot, then frozen.
- An equivalence claim needs a prespecified margin and TOST. Without that, the result is reported as
  inconclusive.
- The multiplicity procedure is fixed in advance.
- Size separately for:
  - fixed-process calibration;
  - cross-process calibration;
  - structural generalisation.

## 7. Adversarial challenges get documented dispositions

**Red-team tests A–H:**
- (A) autocorrelated independent channels;
- (B) common driver;
- (C) periodic alignment;
- (D) nonstationarity;
- (E) ties;
- (F) negative structural controls;
- (G) lag window;
- (H) cross-family.

**Identifiability.** Observationally equivalent systems with different Φ targets are at least a stated open
question. Do not claim identifiability, or its absence, without a construction or proof.

## 8. Gates

Order: literature → pilot → adversarial pilot review → preregistration (commit **and push** evidence) →
confirmatory run on a fresh seed stream.

**In this task, stop after the pilot plus `PILOT_RESULTS.md` with a GO/NO-GO verdict.** NO-GO and "question
already answered" are acceptable outcomes. Do not preregister. Do not run the confirmatory study.

## 9. Repo conventions

Use the repo's actual study-folder layout (`org_frontier/questions/q<NN>_<slug>/`, scaffolded by
`org_frontier/protocol/new_question.py`), not the blueprint's suggested tree. q221 is verified free.

## Carried-over rules and approved defaults (Hassan, 2026-10-15)

**Approved defaults:**
- q220's curated (q161) forms are excluded entirely.
- Bottleneck identification is confirmatory only if the pilot shows enough signal.
- Strongest coupling per form: the max-over-pairs statistic.
- Calibration band [0.025, 0.075] at α = 0.05.
- Bonferroni, unless Holm 1979 gets a verified source.
- A faster profile code path is allowed only if a test proves it reproduces q220's output exactly.
- The pilot is framed and disclosed as a **methods check**, not a confirmatory result.

**Process rules:**
- Work in a new git worktree; never touch the #841 branch or its clone, q220 or q161.
- Local commits only, as `wwk5q8z6kk-bit`. No push, no PR, nothing posted on GitHub.
- Heavy work goes through `box-run --no-as-limit --mem 2000`, with at most 4 workers.
- Respect the box's 16 GB of memory.
- No experiments beyond the pilot.
- No monetization content.
- Checkpoint progress in the study folder.
