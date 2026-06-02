# Paper 3 outline: a formal-model paper, IMRaD structure

Roger Hunt III · Bentley University
Working outline, **v4 — recast as a formal-model contribution** (the draft in `draft/DRAFT.md` is now
authoritative and supersedes this skeleton). Structured loosely as a measurement-style paper, but the
empirical-validation half is deliberately *not* performed: the readability score is named as the goal, and
this paper builds only the model side. The argument-shaped content (unit / model / catalog / typology /
structure-not-seat) is in `ARGUMENT.md`.

The paper computes Φ across the complete W–S–C model family, finds the scores fall onto a few discrete bands,
places real organizations on the populated bands, and reports the headline — a statement about the model, not
an empirical finding — that the score is set by **determination structure**, not technology: a human-run
court is modeled at the same score as an algorithmic platform of the same shape. The score is a property of
the **coordination form, not the person**, and the model is explicitly **not validated against any observed
outcome** (the earlier Chicago anchor was cut; see `exploratory/`).

Target ~8,000 words; short **noun-phrase** section titles; Methods + Results ≈ half the paper.

---

## Abstract (~220 w)
Compression: Paper 2 gives a yes/no classification, not a graded scale; we develop the graded model-internal
side by computing Φ across the complete W–S–C family (16³ = 4,096 wirings) and find the scores fall onto a
few discrete bands (44% reducible; seven non-zero bands; strict mediation the strongest driver, R²=0.20 so Φ
exceeds any feature count); most wirings are not coordination forms, so the enumeration is a coverage check
that locates organizations within the family; the headline (a model result, no anchor needed) is that the
score responds to structure not the mediator's nature — a court is modeled like a platform of the same shape;
the readability score is named as the goal and the outcome validation as future work. State the model
clearly; claim no validation.

## 1. Introduction (~1,000 w)
**Function.** The move from a yes/no model (Paper 2) to a graded model-internal score; name the readability
score as the *goal* (built here on the model side, not validated); fix the unit (form, not person); preview
the design (enumerate the family, compute Φ, place organizations) and the headline (structure, not the
mediator's seat). *No numbers, or the headline only, qualitatively.*

## 2. The Coordination Form as Unit (Background) (~1,300 w)
**Function.** Ground the construct and the unit; the readability parallel in full, including **what we do not
borrow** — the completed validation; the two-stage shape (form-score, then outcome-validation) and that this
paper delivers only the first; Claim A (the score is a property of the form); the variance puzzle (Paper 1)
as the program's destination; Simmel/mediation-triad; orthogonal to governance schemes. *Conceptual — no
numbers.*

## 3. Model and Methods (~2,000 w)
**Function.** Specify the modeling procedure, the catalog, the typology, and what is reported. Moves:
1. **The model** — W–S–C → individuate by Paper 2's rule → exact IIT-4.0 system Φ via `proxy_audit.exact_phi`;
   the three modeling choices (representation, individuation rule, party partition) named as choices.
2. **The catalog (the model family)** — all 16³ = 4,096 three-node wirings + a 48-wiring higher-order family;
   dedup by identical TPM; structural features per wiring. Stated as a **coverage/null check**, not a census
   of coordination — most wirings are not coordination forms. `catalog.py`.
3. **Structural claims fixed before computation** — H1-style: determination structure, not party count, sets
   the score; the family refutes the party-count-only null by separating forms at fixed n.
4. **The typology** — each organization's determination structure fixed in `typology_phi.py` before
   computing; the partial-vs-strict modeling choice; the human-mediated contrast class as the orthogonality
   test.
5. **What we compute and report** — Φ distribution; feature→Φ model (group means + OLS, R²); the **Cerullo
   (2015) caution** carried openly (parity scores highest → read magnitude ordinally); labeled negative and
   positive controls.

## 4. Results (~1,600 w)
**Function.** Report the family's landscape, the typology placements, the structure-not-seat headline. Moves:
1. **The Φ landscape of the family** — Φ over all 4,096 wirings; 44.1% reducible; seven non-zero bands;
   `catalog_landscape.png`. Feature→Φ: strict mediation +0.54 (strongest), parity +0.27, edges +0.24,
   R²=0.20 (Φ exceeds any feature count); parity highest (read against ourselves, per Cerullo).
2. **The typology on the bands** — placement table (13 orgs, 5 levels) on populated bands; negative control
   (dyadic baselines = 0); positive control (Φ separates at fixed n: 0.50/0.83/2.0).
3. **The structure-not-seat headline** — court 2.00 = Uber/ATS/content-mod; staffing/broker 0.83 = Upwork;
   human-mediated interleave with algorithmic by structure. *A model result; no anchor needed.*
*State what the numbers are; save what they mean for Discussion. No outcome/validation results — there are none.*

## 5. Discussion (~1,100 w)
**Function.** Interpret. Moves: the headline's meaning (structure, not the mediator's seat → the model
measures triadic coordination, not algorithms); the catalog makes it more than extrapolation (irreducibility
is the exception; Φ is not a feature count); orthogonal to governance schemes (court=hierarchy and
platform=market share a score; the two hybrids split); the precedent for Φ-beyond-consciousness (Engel &
Malone 2018); the limits, stated larger than an over-eager draft would — **no validation performed**, and the
validation that would complete it must vary structure at a fixed party count. *No new numbers.*

## 6. Limitations (~500 w)
**Function.** The honest bounds: form-not-person (supply-side scale is next work); **everything is
model-internal — no outcome validation is performed**; the earlier rideshare anchor was cut because Φ=k+1 made
it validate only the party-count axis; the structure axis is a model result; magnitude ordinal only
(Cerullo); the three modeling choices are load-bearing; cross-node 3.0 not strictly comparable.

## 7. Conclusion (~300 w)
**Function.** State the contribution (Paper 2's classification developed into a graded model-internal score;
levels emerge from the family; structure not technology sets the score) and the program forward (the outcome
validation — varying structure at fixed n — then the matched supply-side scale). Name → formalize →
(future) validate. No new claims; earn the bridge, don't feign independence.

## 8. Data and Code Availability (~100 w)
Reproduce: `catalog.py` → `analyze_catalog.py` (the family landscape + feature model + figure, zero data
reference); `typology_phi.py` (the organizations, zero data reference). The cut rideshare analysis is in
`exploratory/` with a note explaining why it is outside the dissertation's claims.

---

## Notes
- **Exemplars for structure & voice:** the Flesch/Kincaid/DuBay readability lineage (for the form-level-score
  shape, *not* the completed validation); Engel & Malone 2018 (Φ-beyond-consciousness precedent); Cerullo
  2015 (the magnitude caution to carry openly).
- De-slop with the playbook's mechanical checks; short noun-phrase titles; minimal em-dashes.
