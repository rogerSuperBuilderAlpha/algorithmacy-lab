# Paper 3 — execution plan (experiment: calibrated baseline scale)

**Mode:** experiment. **Status:** scaffolded, not executed. **Dependency:** the calibration dataset (Chicago
TNC) — deferred per user decision; sort out when we reach this paper.

## What it does

Compute Φ (Paper 2's instrument) across a sample of real platforms under the **pre-registered
state-individuation rule applied uniformly**, then regress Φ against an **observed coordination outcome** to
calibrate a difficulty scale. The score is a property of the **platform, not the person** (the
readability-analogy: a text-difficulty score is validated against measured comprehension and says nothing
about a given reader). The matched supply-side (individual) scale is later work.

## How "our process" maps here

- **The load-bearing decision is the calibration anchor** (outline §3), the way the state alphabet was
  Paper 2's. Name the observed coordination outcome Φ is validated against, and argue the dataset choice
  (large-scale interaction records with outcomes, not self-report).
- **Reuse the instrument** from Paper 2 (`phi_instrument.py`) and the repo's `proxy_audit.exact_phi`; apply
  the *same* individuation rule to every platform so scores are comparable.
- **Robustness/honesty battery** as in the IIT experiments: granularity discipline from the tractability
  limit (small, principled state alphabets); seeds where any step is stochastic; report what is dropped.
- **Validation is feature-tied-to-outcome**, per the readability precedent (successful difficulty
  instruments are feature measures tied to outcomes, not deep models of internal structure).

## Dependency to resolve at execution time

- **Chicago TNC dataset:** the public Chicago Data Portal "Transportation Network Providers — Trips" data
  carries coordination outcomes at scale. When we reach this paper: confirm access, pick the observed
  outcome (e.g. match/cancellation/wait-time behaviour that varies with coordination difficulty), and wire
  the validation regression. (User chose to decide this when we reach Paper 3.)

## Steps (deferred to an execution session)

1. Specify the platform sample and each platform's application-layer state alphabet under the fixed rule.
2. Compute Φ per platform via `phi_instrument.py`.
3. Acquire/curate the calibration dataset; define the observed coordination outcome.
4. Regress platform Φ against the outcome; report the scale and the anchor fit.
5. Report the baseline: the dyadic-limit case low, the irreducible cases high (as Paper 2 predicts); the
   spread establishes that coordination forms differ in measurable triadicity and that the difference
   predicts how coordination goes.
6. Write the paper (intro → unit-is-the-platform → calibration anchor → method → results → contribution).

## Deliverable and scope

A **calibrated, portable instrument** for placing any coordination form on a scale of triadic demand,
validated against observed coordination. Names the matched supply-side individual scale, additional
calibration domains, and the within-platform variance puzzle (Paper 1's opening) as the program the baseline
opens. Concede the single-domain generalization limit in one sentence and return: a calibrated scale in one
domain is the precondition for porting the method.

## Load-bearing decision

The **calibration anchor** (and the dataset that supplies it). Not a doubt about algorithmacy — a question
about the instrument that measures it; naming it is what makes the result defensible.
