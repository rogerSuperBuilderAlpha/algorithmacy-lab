# Paper 3 outline (general): an empirical/quantitative paper, IMRaD structure

Roger Hunt III · Bentley University
Working outline, **v3 — re-mapped onto the quantitative empirical genre (IMRaD)**, structured as a
**readability-measurement paper** wears it (the template; see `research/empirical_quantitative_methodology.md`).
The argument-shaped content (unit / model / anchor / baseline / contribution) is preserved in `ARGUMENT.md`;
this file is the section skeleton the draft follows.

The paper produces a **portable model**: it maps any organization's coordination to a Worker–System–Counterpart
application layer, computes Φ, and places it on a scale of triadic demand — a *readability score for
coordination*. The scale is calibrated against an observed coordination outcome (concurrent criterion
validity), then the model is demonstrated across a typology of organization types. The score is a property of
the **coordination form, not the person**.

Target ~8,000 words; short **noun-phrase** section titles; Methods + Results ≈ half the paper.

---

## Abstract (~200 w)
Compression: an instrument exists (Paper 2) but a number is not a scale; we build a portable model that maps
any organization to W–S–C and computes Φ; anchored in rideshare pooling, Φ tracks the observed outcome
(friction r=+0.98, achievement r=−0.91); the calibrated model places a typology across five structural levels,
and a human-mediated court scores identically to an algorithmic platform. Name one computed number per claim.

## 1. Introduction (~1,000 w)
**Function.** The move from a decision procedure (Paper 2) to a calibrated, portable model; fix the unit
(form, not person — briefly); preview the two-stage design and the headline (structure, not the mediator's
seat, sets the score). *Absorbs:* current §1 + the thesis of §2 stated briefly. *No numbers, or the headline
only, qualitatively.*

## 2. The Coordination Form as Unit (Background) (~1,200 w)
**Function.** Ground the construct: the readability parallel in full (a text-difficulty score validated
against comprehension says nothing about a given reader); Claim A (the score is validated against how
coordination goes, not against any individual); the variance puzzle (Paper 1) as the program's destination;
pre-empt "where are the individuals?". *Absorbs:* current §2. *Conceptual — no numbers.*

## 3. Data and Methods (~2,200 w) — center of gravity
**Function.** Specify the model to reproduce, state hypotheses, describe the anchor data and the typology
pre-registration. *Absorbs:* current §3 (the model) + new methods apparatus. Moves:
1. **The model** — map → W–S–C → individuate by Paper 2's rule → exact IIT-4.0 system Φ via
   `proxy_audit.exact_phi`; node convention; granularity discipline held constant (the source of
   comparability). One sentence: instrument gated on Paper 2's passed controls.
2. **Hypotheses fixed before computation** — H1: Φ from determination structure tracks observed coordination
   difficulty (Φ↔friction +, Φ↔achievement −). H0 (informative): Φ tracks only **party count**, not
   determination structure. ("Claims fixed before computation," not "pre-registered.")
3. **The anchor data** — Chicago TNP Trips (`m6dm-c72p`); the sample; completed-trips-only; the outcome
   variables (achievement share, friction sec/mi). Calibration weight, not subject.
4. **Stage-1 modeling** — each pool size as a (k+2)-node strict higher-order form; Φ=k+1 derived before data.
5. **Typology pre-registration** — each organization's determination structure fixed in `typology_phi.py`
   before computing, derived from how it actually coordinates; name the partial-vs-strict modeling choice.
6. **Statistics & robustness design** — correlation/effect size; the robustness battery (second window,
   alternative aggregation, within-stratum Simpson's check, power/MDE); labeled controls.

## 4. Results (~1,800 w)
**Function.** Report the anchor fit, the typology placements, the contrast-class headline, the robustness
numbers. *Absorbs:* current §4–§5 (numbers only). Moves:
1. **Stage-1 anchor** — table by pool size (Φ, n, achievement, friction); Φ vs friction r=+0.98 (monotone
   156→227); Φ vs achievement r=−0.91; log-slope −0.565 (×0.57 per +1 Φ); match success 0.66. Report r²/effect
   size; significance uninformative at N≈48k.
2. **Stage-2 typology** — full placement table (13 orgs, 5 levels); negative control (dyadic baselines = 0);
   positive control (Φ separates at fixed n: 0.83 vs 2.0).
3. **The headline** — court 2.00 = Uber/ATS/content-mod; staffing/broker 0.83 = Upwork; human-mediated forms
   interleave with algorithmic ones by structure.
4. **Robustness** — the battery's numbers (stability across windows; within-stratum; power).
*State what the numbers are; save what they mean for Discussion.*

## 5. Discussion (~1,000 w)
**Function.** Interpret. *Absorbs:* §5 interpretation + §6. Moves: the headline's meaning (structure, not the
seat of the mediator → the model measures triadic coordination, not algorithms); Claim B (the interleaving is
the evidence it is a *model*); the anchor resolves Paper 2's continuous-stream window; shared scores are a
finding, not a defect. *No new numbers.*

## 6. Limitations (~500 w)
**Function.** The honest bounds that make the claim credible: form-not-person (supply-side scale is next
work); one calibration domain (model portability ≠ anchor's domain); Stage-2 placements are structural,
outcome-validated only via the anchor; the **party-count confound named plainly** (the anchor validates Φ's
party-count axis; the typology carries within-size discrimination); cross-node 3.0 not strictly comparable;
tractability bounds the alphabet.

## 7. Conclusion (~300 w)
**Function.** State the contribution (a portable, calibrated instrument for placing any organization's
coordination on a triadic-demand scale); hand the program forward (matched supply-side scale, added domains,
the within-form variance the matched pair explains). No new claims; earn the bridge, don't feign independence.

## 8. Data and Code Availability (~100 w)
Reproduce: `typology_phi.py` (Stage 2, zero data reference) and `anchor_chicago.py --refresh` (Stage 1 live
pull); Chicago resource `m6dm-c72p`.

---

## Notes for the expanded outline (Step 4) and draft (Step 5)
- The **anchor section (§4.1)** copies the readability-validation skeleton (form-score → sample → observed
  outcome → correlation → limits) and is named **concurrent criterion validity**.
- **Exemplars to match for structure & voice:** Rafatbakhsh et al. 2023 (form-score vs observed performance
  at scale); Zheng et al. 2017 (corpus + correlate, honest null); Lenzner 2014 (methods-journal validation
  register); the Flesch/Kincaid/DuBay lineage; one platform-measurement exemplar (TBD in topic research).
- De-slop with the playbook's mechanical checks; short noun-phrase titles (already used above).
