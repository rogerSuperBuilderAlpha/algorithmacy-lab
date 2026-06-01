# Paper 3 — expanded outline (the drafting blueprint)

**Roger Hunt III · Bentley University**
Working title: *A readability score for coordination: calibrating integrated information as a measure of
triadic demand across organizations*

The drafting blueprint produced by the pipeline (genre research → general outline → topic research +
robustness battery → this expanded outline). Empirical/quantitative genre, structured as a
**readability-measurement paper** wears IMRaD (template: `research/empirical_quantitative_methodology.md`).
Per section: **function · moves (in order) · claims + citations · computed results to report · crystallized
closing · failure mode**. Numbers are in `results.md`; cite them, do not re-derive. ~8,000 words;
Methods + Results ≈ half; short noun-phrase titles; de-slop with the playbook's mechanical checks.

**Genre commitments threaded throughout:** the anchor section copies the readability-validation skeleton
(form-score → sample → observed outcome → correlation → limits) and is named **concurrent criterion
validity**; **H1/H0 are stated in Methods** (validation = hypothesis testing, Landy 1986); the **full
robustness battery** and **labeled controls** are reported; the **party-count confound** is named in the
open; **effect size, not significance** (large N). Φ-terminology lock carried from Paper 2 (system φs over
the MIP).

---

## Abstract (~200 w)
**Function.** One-paragraph compression. **Moves:** (1) Paper 2 gave a triadic/dyadic verdict but a number
is not a scale; (2) we build a portable model — map any organization to Worker–System–Counterpart, compute
Φ — a *readability score for coordination*; (3) anchored in Chicago rideshare pooling, Φ tracks the observed
outcome (friction r=+0.98; trip-level slope +16.8 sec/mi per +1 Φ; stable across windows and within areas);
(4) the calibrated model places a typology across five structural levels, and a human-mediated court scores
identically to an algorithmic platform — structure, not the seat of the mediator, sets the demand. **Report:**
the anchor correlation + one trip-level effect size + the contrast headline. **Failure:** selling portability
with no number.

## 1. Introduction (~1,000 w)
**Function.** The move from a decision procedure (Paper 2) to a calibrated, portable model; fix the unit;
preview the design and the headline. **Moves (in order):**
1. Paper 2 decided *whether* a coordination form is triadic; it withheld *how much*. A Φ value is not a
   difficulty scale until anchored to an outcome that varies with difficulty.
2. The analogy that organizes the paper: a **readability score** — a property of the *text*, validated
   against measured comprehension, saying nothing about a given reader (Flesch 1948; DuBay 2004). Paper 3
   builds the same thing for coordination.
3. Scope commitment (one paragraph; full defense → §2): the unit is the coordination **form**, not the
   person.
4. The contribution: a portable model that maps any organization to W–S–C and computes Φ, calibrated
   against an observed outcome, and demonstrated across organization types.
5. Preview the two-stage design (anchor in rideshare pooling, then place the typology) and the headline:
   a human-mediated **court** scores like **Uber**; structure sets the demand.
**Citations:** Paper 2 (the instrument); Flesch 1948 / DuBay 2004 (readability precedent); Engel & Malone
2018 (Φ has reached groups — the honest nearest prior). **Report:** the headline qualitatively, no tables.
**Crystallized closing:** *A measure that decides whether coordination is triadic becomes useful when it
says how triadic; this paper calibrates it into a scale and reads organizations on it.* **Failure:**
re-arguing Paper 2's triadic/dyadic case; opening with the model procedure (that is Methods).

## 2. The Coordination Form as Unit (Background) (~1,200 w)
**Function.** Ground the construct and the unit; the readability parallel in full; pre-empt "where are the
individuals?". **Moves:**
1. The readability parallel, fully: a text-difficulty score is validated against measured comprehension and
   says nothing about a given reader; it is a property of the form (Flesch 1948; Kincaid et al. 1975;
   DuBay 2004; modern validation, Crossley et al. 2017). The score's predictive power at the individual
   level can be modest and the form-level signal still real (Zheng et al. 2017; Lenzner 2014) — the
   precedent for honest effect sizes later.
2. Claim A: a difficulty score is a property of the coordination form, validated against how coordination
   through it goes, carrying no claim about any individual. The variance puzzle (Paper 1) — why two workers
   facing the same form fare differently — is the matched supply-side instrument's job, later work.
3. The triad is a century-old object, not a coinage: Simmel's third party that transforms the dyad (Simmel
   1950); the org-economics statement that the field measures **dyads** and the triad is the corrective
   (Nooteboom 2006); the three triad forms, of which Paper 3 measures **mediation** (Siltaloppi & Vargo
   2017). Φ measures the mediation triad.
4. Position the measure against the governance-forms canon: organizations are classified by coordination
   mode — market/hybrid/hierarchy (Williamson 1991), networks (Powell 1990), coordination mechanisms
   (Mintzberg 1980), graded explicit coordination (Gereffi et al. 2005). Paper 3's scale is **orthogonal**:
   it places any form, however already classified, by how irreducibly its coordination runs through a
   mediator.
5. Brief: the instrument is Paper 2's (reference, do not re-derive); Φ = system irreducibility over the MIP.
**Report:** none (conceptual). **Crystallized closing:** *The scale measures the form the way a readability
score measures a text — and like a readability score, it is silent about any one reader.* **Failure:**
turning Background into a second methods section; re-deriving the borrowing argument of Paper 2.

## 3. Data and Methods (~2,200 w) — center of gravity
**Function.** Specify the model to reproduce; state hypotheses; describe the anchor data and the typology
pre-registration; the statistics + robustness design. **Moves (in order):**
1. **The model (procedure).** Map an organization's coordination to a 3-node (or n-node) W–S–C
   application-layer system; individuate states by Paper 2's pre-registered rule; compute exact IIT-4.0
   **system φs over the MIP** via `proxy_audit.exact_phi` (`pyphi.new_big_phi.sia`). Node convention;
   granularity discipline held constant — the source of cross-organization comparability. One sentence:
   the instrument is gated on Paper 2's passed controls (factoring → 0; irreducible → >0).
2. **Hypotheses, fixed before computation** (Landy 1986: validation = hypothesis testing). **H1:** Φ
   computed from determination structure tracks observed coordination difficulty (Φ↔friction positive,
   Φ↔achievement negative). **H0 (the informative null):** Φ tracks only **party count**, not determination
   structure — refuted by the typology (0.83 vs 2.0 at fixed n=3). Use "claims fixed before computation,"
   not "pre-registered."
3. **The validation framing.** Stage 1 is a **concurrent criterion-validity** demonstration: a form-level
   measure correlated with an external criterion on the same units (Cronbach & Meehl 1955; Alavi et al.
   2023). Nearest precedent: an information-theoretic complexity measure validated against a work-
   coordination outcome (Schlick et al. 2015).
4. **The anchor data.** City of Chicago "Transportation Network Providers — Trips, 2018–2022" (`m6dm-c72p`,
   Socrata); shared-authorized sample; completed-trips-only (so pooling, not cancellation/wait, is the
   outcome); outcome variables — **achievement share** and **friction (sec/mi)**; the pooling era (2018–
   2020-03). Calibration weight, not subject. Disintermediation makes pooling the constitutive triad
   (Rosenblat & Stark 2016; Stark & Pais 2020).
5. **Stage-1 modeling.** Each pool size k = a (k+2)-node strict higher-order mediation form; Φ = k+1,
   computed before any data contact (`anchor_chicago.py`, `typology_phi.py`).
6. **Typology pre-registration.** Each organization's determination structure fixed in `typology_phi.py`
   *before* computing Φ, derived from how it coordinates; name the partial-vs-strict modeling choice
   (staffing/broker at 0.83 because parties coordinate directly once matched). The orthogonality test: the
   human-mediated contrast class (Khurana 2002 — search firms as Simmel triads).
7. **Statistics & robustness design.** Correlation + **trip-level regression** (the effect size, N≈193k);
   the battery — second time window, alternative aggregation, within-stratum (Simpson's), power/MDE; the
   **labeled controls** (negative = dyadic baselines Φ=0; positive = Φ separates at fixed n).
**Report:** the *design* numbers (Φ=k+1; the structural levels as model outputs), not yet the data fit.
**Crystallized closing:** *Fix the determination structure before computing, apply one rule to every
organization, and the scores are comparable and the test is honest.* **Failure:** letting the
determination-structure assignments look post-hoc — pre-registration is the objectivity guarantee, as the
state alphabet was in Paper 2.

## 4. Results (~1,800 w)
**Function.** Report the anchor fit, the typology placements, the contrast headline, the robustness numbers.
**Moves (in order):**
1. **Stage-1 anchor.** Table by pool size (Φ, n, achievement share, friction). Φ vs friction **r=+0.98**
   (4 points), friction monotone 156→227; trip-level regression **slope +16.8 sec/mi per +1 Φ, R²=0.019,
   N≈193k**; achievement share 33/35/26/6%, log(share)~Φ slope **−0.54 (×0.58 per +1 Φ)**, r=−0.88; match
   success P(pooled≥2 | authorized) = 0.66. State: Φ from structure alone orders the forms as observed
   difficulty does, on both cost and rarity axes. **Effect size, not significance** at N≈193k.
2. **Robustness.** Temporal: r +0.976 (early) vs +0.975 (late). Within-stratum (Simpson's): friction
   monotone in pool size within **7 of 8** top community areas. Alternative aggregation: r +0.98 / +0.95 /
   +0.94. (The relation is stable, not a pooling artifact, robust to aggregation.)
3. **Stage-2 typology.** Full placement table (13 organizations, five levels: 0 / 0.5 / 0.83 / 2.0 / 3.0).
   **Negative control:** dyadic baselines = 0.00. **Positive control:** Φ separates at fixed party count
   (partial 0.83 vs strict 2.0 vs parity 0.5, all n=3) — Φ beyond a party counter.
4. **The headline.** Court = **2.00** = Uber/ATS/content-moderation; staffing agency + broker = **0.83** =
   Upwork. Human-mediated forms interleave with algorithmic ones at every level, sorted by structure.
**Citations:** results.md (numbers); the platform domain (Rosenblat & Stark; Stark & Pais; Vallas & Schor;
Sun et al. 2024). **Crystallized closing:** *The same procedure that scores Uber scores a courtroom, and it
puts them at the same place.* **Failure:** importing interpretation ("this proves portability") here; presenting
the 4-node Φ=3.0 as strictly comparable to the 3-node scale (flag it size-driven).

## 5. Discussion (~1,000 w)
**Function.** Interpret the headline; argue portability; situate the result. **Moves:** (1) the headline's
meaning — structure, not the seat of the mediator, sets the demand → the model measures triadic
coordination, not algorithms; (2) Claim B — the interleaving across human- and algorithm-mediated forms is
the evidence it is a *model*, not a platform study, and that the scale is orthogonal to the market/hierarchy/
network classifications (Williamson; Powell; Gereffi); (3) the anchor settles Paper 2's open continuous-
stream window (the granularity that calibrates is the one that counts); (4) several organizations sharing a
score is a finding, not a defect; (5) the form-level/per-individual split (strong aggregate, modest trip-
level R²) is exactly the readability stance, and reinforces Claim A. **Report:** re-reference the headline;
no new numbers. **Crystallized closing:** *Coordination has a readability, and it is a property of the form,
not the worker.* **Failure:** overclaiming — placements are model outputs, outcome-validated only via the
anchor; no causation from observational records.

## 6. Limitations (~500 w)
**Function.** The honest bounds. **Moves:** (1) measures the form, not the person (supply-side scale is next
work); (2) one calibration domain — model portability and the anchor's domain are different claims; (3)
Stage-2 placements are structural, outcome-validated only via the anchor; (4) **the party-count confound,
named plainly** — the anchor validates Φ's party-count axis (friction runs through party count); the
fixed-n positive control and the typology carry the within-size discrimination; (5) cross-node Φ=3.0 not
strictly comparable to the 3-node scale; (6) tractability bounds the state alphabet, applied uniformly; (7)
observational association, not causal. **Failure:** burying the confound — it is the sharpest reviewer
target; name it.

## 7. Conclusion (~300 w)
**Function.** Contribution + forward hand-off. **Moves:** a portable, calibrated instrument for placing any
organization's coordination on a triadic-demand scale; next work = the matched supply-side individual scale,
additional calibration domains, the within-form variance the matched pair explains. **Crystallized closing:**
*Paper 1 named the triad, Paper 2 measured it, and this paper reads organizations on the scale; what remains
is the worker.* **Failure:** new claims; feigning independence from the arc.

## 8. Data and Code Availability (~100 w)
Reproduce: `typology_phi.py` (Stage 2, zero data reference); `anchor_chicago.py --refresh` (Stage-1 headline);
`robustness_anchor.py` (the battery). Chicago resource `m6dm-c72p`, Socrata; bounded queries documented in
the scripts.

---

## Drafting order (Step 5)
Draft Methods (§3) and Results (§4) first — the spine of a quantitative paper, and where the numbers anchor
the prose — then §2, then §1, then §5–§7. De-slop after a complete draft, grounded in the readability/
methods-paper register (Rafatbakhsh; Zheng; Lenzner) + `STYLE_NOTES.md` + the playbook's mechanical checks
(em-dash count, the meta-narration phrase list, the section-title list read alone). Then the consolidated
bibliography + citation-integrity pass (delegate verification, as for Paper 2).
