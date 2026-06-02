# Paper 3 — execution plan (formal model of triadic demand)

> **RECAST NOTICE (superseding).** This plan predates the formal-model recast. The authoritative artifacts
> are now `draft/DRAFT.md`, `results.md`, and `ARGUMENT.md`. Two things below are obsolete: (1) the
> empirical-**calibration / anchor** spine was **cut** — in the pooling model Φ = k+1, so the Chicago anchor
> validated only the party-count axis (the scripts are demoted to `exploratory/`); (2) the paper claims **no
> validation against the world** — it characterizes the W–S–C **model family** and places organizations on
> it. Read references to "calibration," "anchor," and "calibrated scale" below as superseded.

**Mode:** formal model (no empirical validation). **Status:** executed and drafted — model family enumerated
(4,144 wirings, `catalog.py`/`analyze_catalog.py`), typology placed (`typology_phi.py`), full draft written
(`draft/DRAFT.md`); the rideshare anchor cut to `exploratory/`. Results in `results.md`.

## What it does (reframed)

Turn Paper 2's instrument into a **portable model for analyzing organizations**: map any organization's
coordination to a W–S–C application-layer system, individuate states by the pre-registered rule, compute
Φ, and place the organization on one scale of triadic demand. Calibrate the scale against an observed
coordination outcome in **one data-rich anchor domain** (rideshare pooling), then **place a typology of
organization types** on the validated scale. The score is a property of the **coordination form, not the
person** (the readability analogy). The matched supply-side (individual) scale is later work.

## Decisions taken (this session)

- **Scale design: anchor-then-place** (author).
- **Dataset scope: one anchor domain, model applied broadly** (delegated to me) — Chicago TNC Trips as the
  single calibration weight, with the paper's reach being the organization typology, per the author's
  steer to "explore different types of organizations and come up with a model to analyze them."
- **Anchor outcome:** to confirm with author — candidate is pooled-match success (P(pooled | shared
  authorized) by area×time), with detour cost as a robustness companion. (The Chicago Trips data is
  completed-trips only: no cancellations or wait times, so the pooling outcome is the clean available one.)

## How "our process" maps here

- **The model (§3) is the contribution; the anchor (§4) only licenses the scale.** Keep them distinct.
- **Reuse the instrument** from Paper 2 (`phi_instrument.py`, `proxy_audit.exact_phi`); apply the *same*
  individuation rule, node convention, and granularity discipline to every organization so scores compare.
- **Validate the anchor on real outcomes** (feature-tied-to-outcome, per the readability precedent), not a
  deep model of internal structure.
- **Compute, don't assert:** every Φ is computed and reproducible; the anchor fit is reported, not claimed.
- **Honesty battery:** uniform granularity; report what is coarsened; the human-mediated contrast class as
  the falsification test (model measures triadic structure, not algorithms).

## The organization typology (proposal — refine with author)

Four classes spanning mediated coordination, each modeled as W–S–C and scored by Φ:

1. **Dyadic baselines** (floor, Φ ≈ 0): direct two-party exchange; chat with a language model.
2. **Algorithmic platforms**: rideshare (solo & pooled), food delivery, freelance marketplace, crowdwork.
3. **Algorithmic-institutional gatekeepers**: applicant-tracking/hiring, content moderation, credit/benefit
   scoring.
4. **Human-mediated intermediaries** (the contrast class): a court (judge between parties), a healthcare
   staffing agency (worker–facility), a broker (buyer–seller). Same determination structure, human in the
   mediator seat — the test that the model measures coordination, not algorithms.

## Steps (execution)

1. **Confirm the typology** (author) and the anchor outcome.
2. **Model each organization type** as a W–S–C application-layer system; pre-register each determination
   structure before computing (as Paper 2 did for its worked examples).
3. **Compute Φ per organization** via `phi_instrument.py`, uniform rule.
4. **Acquire/curate the Chicago TNC anchor**; define the pooled-match outcome; compute Φ for solo vs
   pooled configurations and regress Φ against the outcome by area×time. Report the anchor fit.
5. **Place the typology** on the calibrated scale; report the spread; foreground the human-mediated
   contrast.
6. **Write the paper** (intro → unit → model → anchor → baseline-across-types → contribution), de-slop
   pass, consolidated bibliography pass (as Papers 1–2).

## Dependency to resolve at execution time

- **Chicago TNC dataset:** public Chicago Data Portal "Transportation Network Providers — Trips" (2018–
  present). Confirm access path; the outcome is built from `Shared Trip Authorized` + `Trips Pooled` +
  trip seconds/miles. No cancellations/wait in the data — pooling is the clean coordination outcome.

## Deliverable and scope

A **portable, calibrated model** for placing any organization's coordination on a scale of triadic demand,
validated against an observed outcome in one domain and demonstrated across a typology of organization
types. Names the matched supply-side individual scale, additional calibration domains, and the within-form
variance puzzle (Paper 1's opening) as the program it opens. Concede the single-anchor-domain limit in one
sentence and return: a calibrated scale in one domain is the precondition for porting the model.

## Load-bearing decisions

The **calibration anchor** (Claim C) and the **model's portability across organization types** (Claim B).
Not doubts about algorithmacy — questions about the instrument that measures it; naming them is what makes
the result defensible.
