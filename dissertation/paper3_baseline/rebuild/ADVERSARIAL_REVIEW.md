# Paper 3 — adversarial committee review and adjudication (Stage 4, round 1)

Three hostile reviewers read `DRAFT.md` independently against the committed scripts: a case-study
methodologist (R1), an IIT / formal-modeling expert (R2), and an organization theorist / platform
skeptic (R3). **All three reproduced every load-bearing number exactly** (catalog 44.1% / 7 bands /
OLS R²=0.196 / Cerullo 0.85 vs 0.535; typology 0/0.50/0.83/2.00/3.00; cases 2.00/2.00/0.83/0.83/3.00;
controls 0.000/0.830/2.000). The arithmetic is not in dispute. The claims built on it are.

## Verdicts
- **R1 (case-study methodologist): MAJOR.** The five cases are the typology's archetypes relabeled;
  the within-case "analytic operation" is a two-bit lookup, not an operation; the contribution is
  not yet separated from §3.
- **R2 (IIT / formal): MINOR.** The instrument is correct and `phi_core` generalizes Paper 2 exactly
  at n=3. Defects are presentational: the 2.00-band mislabel, the n=4 size artifact, the dedup
  overstatement, "max Φ" wording.
- **R3 (org theorist): MAJOR.** The seat-contrast equivalence is a definitional artifact oversold as
  discovery; the codings carry the result; the §7 orthogonality move launders power; the gap misreads
  the literature.

The split is 2 MAJOR + 1 MINOR, and the MAJORs rest on framing/honesty, not computational error.

## Compute, don't assert: the charges settled by `review_response.py`

Every settleable charge was computed. All confirm the reviewers.

1. **The 2.00 band is NOT the "strict-mediation band" (R2-Obj1) — CONFIRMED, and it cuts both ways.**
   Of the 496 wirings at Φ=2.00, only **16** are strict_mediation=1. Of the 40 canonical
   strict-mediation wirings, the Φ distribution is **16 at 0.00, 8 at 0.50, 16 at 2.00**. So "strict
   mediation → 2.00" is false as a structural rule: the mediator's Boolean function decides the band
   (AND-family → 2.00, parity → 0.50, some → 0). This refutes the §3/§6 label **and** is the
   strongest available evidence for the paper's own "Φ is not a feature checklist" thesis — stronger
   than the R²=0.20 the draft leans on. Turn the defect into the result.
2. **MTurk's 3.00 is a pure size artifact, Φ = n−1 (R2-Obj2, R3-Obj2) — CONFIRMED.** Strict-AND gives
   n=3 → 2.00, n=4 → 3.00, n=5 → 4.00. For this family Φ = n−1 exactly, so 3.00 conveys "n=4 and
   strict," nothing more. The §5.5/§8 "partly a function of size" caveat understates: it is entirely
   size. And it reintroduces the party-count confound §4 explicitly disowns (the cut-anchor lesson).
3. **Dedup removed 0 (R2-Obj3) — CONFIRMED.** 4,096 triads + 48 higher-order = 4,144; no duplicates
   arose. "After removing duplicates" describes a step that did no work. The triad family is complete;
   the 48 higher-order forms are a structured **sample**, not a complete 4-node family — "complete
   family" must not bleed onto n=4.
4. **The equal-Φ pairs are identical TPMs (R3-Obj1) — CONFIRMED.** Uber and NYSE/Nasdaq are
   byte-identical Boolean systems; so are Upwork and ManpowerGroup. Within a pair, equal Φ is a
   theorem, not a finding, and the "literal replication on Φ" framing is the same computation run
   twice. The equality is true by construction — §6 says so; the abstract and §1 do not.
5. **The codings carry the result (R3-Obj2) — CONFIRMED.** Upwork's match as AND → 0.83; as OR →
   **6.00** (the exotic tail). A market-maker reading of the exchange (S′=S) → **0.00**. The band each
   case lands on is an author coding choice, and §5's "rival codings" only move the score in the
   confirming direction.
6. **The partial 0.83 form is reducible at the all-on state (R2-Obj5b) — CONFIRMED.** Per-state:
   0.415 at (0,0,0), 0.83 at the two asymmetric live states, **0.00 at (1,0,1) and (1,1,1)**. Max Φ
   over reachable states is 0.83. The draft's flat "Φ is 0.83" should read "max Φ is 0.83," matching
   Paper 2's reachable-max convention.

## A. Charges that are REAL (confirmed; must be addressed)

### A1. The structure-not-seat headline is true by construction and oversold as discovery (R1-B2, R2-Obj4, R3-Obj1)
The deepest convergent finding, confirmed (finding 4). §6 has the honest statement ("a modeling
property, not an empirical discovery"); the abstract and §1 sell it as a finding ("a securities
exchange scores the same as a ride-hailing platform … shown on two real organizations that share
nothing"). The pairs are identical TPMs, so the equal score is a theorem of equal coding. **Fix
(fix-now):** propagate §6's language to the abstract and §1. State the claim as a construction: the
model takes structure as input and not seat, so two forms coded to the same structure score the same;
the cases show this when the coder reduces sector-disparate real organizations to the same structure.
Drop "literal replication" for the within-pair comparison (it is the same computation twice; the
cross-pair seat-contrast is the only non-trivial content).

### A2. The 2.00 band is mislabeled "strict mediation"; the cherry-picking defense leans on it (R2-Obj1)
Confirmed (finding 1). **Fix (fix-now, and an upgrade):** relabel the 2.00 row; state that several
wiring families reach 2.00 and strict-AND is one, while strict-parity collapses to 0.50 and some
strict wirings to 0. Make the 16/40 result the headline evidence that Φ is not a feature checklist.
Re-ground the §6 not-cherry-picked argument: "populated band" addresses point-selection, not the
author's choice of organizations or codings (R3-Obj5), so concede that and lean on the coding
discipline instead.

### A3. The MTurk higher-order case is a size artifact and reintroduces the disowned count confound (R2-Obj2, R3-Obj2)
Confirmed (finding 2). **Needs author steer:** either (a) drop MTurk's number from the ordered
display and keep it as a qualitative "the scale extends when a determination binds more parties"
illustration, explicitly outside the four-case replication slate; or (b) keep it but normalize
(report Φ/(n−1) or relative to the n=4 strict baseline) and state Φ=n−1 plainly. Recommended: (a) —
the four-case core (the two seat-contrast pairs) carries the paper; MTurk as drafted breaks the
party-count control §4 calls central and cannot join the replication design because its magnitude is
incomparable.

### A4. The codings carry the result; §5's rival codings are non-adversarial (R1-B4, R3-Obj2)
Confirmed (finding 5). **Fix (fix-now):** add a sensitivity table per case (AND vs OR match, conduit
vs principal exchange, etc.) showing the band's dependence on the coding, and argue why the
documented mechanism forces the chosen rule. Where it cannot be forced, say so. This is the Paper 2
§5 honesty ("the reads are a declared, contestable choice") carried into the cases.

### A5. No case-invariant unit/layer-selection rule (R1-B4)
The exchange is modeled at the matching layer (2.00) though its clearing layer is higher-order; MTurk
is modeled at the binding layer (higher-order). The layer choice changes the band and is made
differently across cases without a stated rule. **Fix (fix-now):** state a case-invariant rule in §4
(e.g., "model the layer at which the focal dyad's coordination is committed") and apply it visibly in
§5.2 and §5.5.

### A6. The §7 orthogonality move overclaims (R3-Obj3)
"The objection is correct and does not touch the claim" claims too much. Opacity, power, and
accountability are arguably structural to the worker's coordination, not orthogonal contingencies, and
"orthogonal" is asserted, not shown. **Fix (fix-now):** scope Φ as **necessary, not sufficient**, for
an organizational characterization; state explicitly that two equal-Φ forms are **not** claimed
substitutable or equivalent in power, and that a power-aware layer is required and not delivered here.
Keep the Paper-2 opacity/irreducibility separation, but do not extend it to power/accountability
without argument.

### A7. The gap misreads the algorithmic-management literature (R3-Obj4)
"The literature conflates technology with structure / frames it dyadically" is unfair to Vallas &
Schor (2020), who theorize platforms as a distinct structural governance form. **Fix (fix-now):**
narrow the gap to the defensible, true claim — no prior work computes a graded score of triadic
coordination structure such that human and algorithmic mediators of identical structure score the
same — and correct the Vallas & Schor characterization. (The framing note already flags V&S as
structure-and-actor; the draft over-read it.)

### A8. Disclosure corrections (R2-Obj3, R2-Obj5b)
Fix-now: "after removing duplicates" → state dedup removed none and the triad family is complete; the
48 HO forms are a structured sample, not a family. "Φ is 0.83" → "max Φ over reachable states is 0.83"
in §5.3/§5.4.

## B. Reviewer overreach / hold the line

- **"The cases add nothing beyond the typology" (R1-B1), taken to its strongest form, is overreach.**
  R1 itself names the defensible contribution: the cases demonstrate the **coding procedure's
  sector- and seat-blindness** on real, documented, incommensurable organizations — that a market and
  a gig platform reduce to the same two structural bits against the grain of industry and seat. That
  is a real (if modest) demonstration about the coder, not a discovery about the world. Keep the cases;
  reframe what they show (A1). Do not retreat to a typology-only paper.
- **"Borderline-fatal MTurk" (R3) vs "fixable" (R2).** Adjudicated to fixable via A3 (demote, don't
  delete). The size artifact is real; dropping the number from the ordered scale neutralizes it.
- **The instrument and the family are sound (R2 MINOR).** No reviewer found a computational error in
  the measure, the enumeration, or the reproductions. The formal core stands.

## C. Disposition

**Fix-now (no judgment call; reframing + disclosure + the sensitivity table):**
A1 (propagate §6's modeling-property language to abstract/§1; drop "literal replication"), A2 (relabel
the 2.00 band; make 16/40 the checklist result; re-ground cherry-picking on coding discipline), A4
(per-case sensitivity table), A5 (state and apply a unit/layer rule), A6 (Φ necessary-not-sufficient;
no substitutability claim), A7 (narrow the gap; fix Vallas & Schor), A8 (dedup honesty; "max Φ"
wording).

**Needs author steer:**
- A3 — demote MTurk to a scope-extension illustration outside the replication slate (recommended), or
  keep-and-normalize. This changes the case count framing (four-case core + one extension vs five).
- How far to demote the headline (A1): keep "structure not seat" as the framing while relocating it to
  a modeling-property claim, or retitle around the coding-discipline contribution.
- Whether to add the orthogonality scoping (A6) as a limit or to build a power-aware companion as named
  future work.

**Deferred (unchanged; the paper's standing posture):**
- Field data replaces the provisional case evidence (the author's fieldwork).
- Outcome-validation (vary structure at fixed party count against an observed outcome) remains the
  empirical program the paper opens.
- Academic citations to be Crossref-verified at finalization; Doty & Glick typology-as-theory
  specifics to firm up.

## Standing after round 1

The formal core is sound and reproduces; the case-study layer needs honest reframing, not new data.
The strongest single move is to convert two defects into strengths: the 2.00-band composition (16/40)
becomes the checklist result, and the equal-Φ pairs become an explicit demonstration of seat-blind
coding rather than an oversold discovery. None of the eight real charges requires fieldwork; all are
reframing, disclosure, a sensitivity table, and a unit-selection rule. This is the Paper-2-grade
round-1 outcome: MAJOR on framing, fixable without retreating from the contribution.

---

# Stage 4, round 2 (re-review of the corrected draft) + copy-edit pass

The corrected draft went back through the same three reviewers, each diffing it against the round-1
commit (`git diff 700fec7 HEAD -- DRAFT.md`) and re-running the scripts. **Verdict trajectory:
2 MAJOR + 1 MINOR → ACCEPT + 2 MINOR.**

- **R2 (IIT / formal): ACCEPT, up from MINOR.** All five Obj1–Obj5 resolved with the numerically
  correct fix and no new technical error. Every load-bearing number reproduces (the 16/40 split, the
  Φ=n−1 size law, Φ/(n−1)=1.00, dedup=0, Upwork OR→6.00, exchange MM→0.00, partial max 0.83 reducible
  at all-on). Two one-line wording asks, not conditions of acceptance.
- **R1 (case-study methodologist): MINOR, up from MAJOR.** B2/B3/B4/B5 resolved; B1 substantially
  resolved (the §5/§6 reframe separates the cases' contribution from the typology and concedes the
  within-case operation is a coding decision, now disclosed not hidden). Residual: minor wording and
  the MTurk slate placement.
- **R3 (org theorist): MINOR, up from MAJOR.** All five resolved (Obj2 fully on
  coding/sensitivity/layer-rule, partial on MTurk's slate placement). The headline demotion is honest
  and did not hollow the contribution; the §7 power-laundering is fixed (necessary-not-sufficient, no
  substitutability, power/accountability not claimed cleanly bracketed); the gap is now fair to
  Vallas & Schor; §6 concedes the right cherry-picking degree of freedom.

## Convergent residual items (all MINOR; applied in this copy-edit pass)

All three flagged the same short list of wording/labeling items. None needs computation or fieldwork.
Applied this pass:
- **MTurk slate placement (R1, R3).** §4 now reads "Four cases form the replication design; the fifth
  extends it to a higher-order determination," and the §6 table adds a size-normalized row
  (Φ/(n−1): 0.42 / 0.42 / 1.00 / 1.00 / 1.00) so the MTurk cell is no longer raw-next-to-raw.
- **§5.3 state description (R2).** "the two states where one party and the platform are live" →
  "where one party is live" (the platform is off at the maximizing states).
- **§6 "the fixing survives" (R3).** → "the coding reaching the same structure across …" (drops the
  empirical-robustness connotation).
- **§5.5 normalization tautology (R1).** "what the case shows … strict mediation generalizes" → "Read
  normalized, the case is a scope extension … the equal normalized score follows from the n−1
  identity, not from a new finding."
- **§3 meta tics (R1).** "against the paper's convenience" and "read against the paper's own interest"
  removed (rule-7).
- **§7 ¶3 residual (R1).** "both errors corrected, a market scored like a platform" → "the coding
  avoiding both errors: a market coded like a platform … by structure rather than by label or seat."
- **§4 diverse-case vs author-choice (R1, R3).** Added a clause: diverse-case selection is a
  disciplined choice along a declared axis, not the absence of one, with the discipline resting on the
  coding rule (§6).

## Standing after round 2

The panel is at ACCEPT + 2 MINOR, and the MINOR items are now addressed in the copy-edit pass above.
No reviewer found a computational error in either round; every load-bearing number reproduced twice.
The round-1 strategy held: the two defects became the paper's stronger material (the 16/40 strict
split is the headline "Φ is not a checklist" result; the equal-Φ pairs are an explicit seat-blind
coding demonstration), and the contribution is stated at the altitude the evidence supports — a claim
about the coder, not the world. Genuine remaining loose ends, all standing posture, none blocking:
the cases are provisional pending the author's fieldwork; outcome-validation (vary structure at fixed
party count against an observed outcome) is the named empirical program; academic citations to be
Crossref-verified at finalization; Doty & Glick typology-as-theory specifics to firm up.

---

# Stage 4, round 3 (re-review of the copy-edited draft)

The copy-edited draft went back through the same three reviewers, each diffing it against the round-2
corrective commit (`git diff 469625e HEAD -- DRAFT.md`) and re-running the scripts. **Verdict:
unanimous ACCEPT.** Trajectory across three rounds: 2 MAJOR + 1 MINOR → ACCEPT + 2 MINOR →
**3× ACCEPT.**

- **R2 (IIT / formal): ACCEPT, confirmed.** Both round-2 wording asks resolved correctly (§5.3 "where
  one party is live" — the platform is off at the maximizing states; the §6 table split into a raw row
  and a size-normalized row, 0.42/0.42/1.00/1.00/1.00). Every cited number reproduces a third time;
  the copy-edit introduced no technical error. The normalized row checks by hand (0.83/2 = 0.42,
  2.00/2 = 1.00, 3.00/3 = 1.00).
- **R1 (case-study methodologist): ACCEPT, up from MINOR.** All five round-2 residuals resolved with
  verbatim text changes (MTurk relabeled four-case-core-plus-extension with the normalized table row;
  §3 rule-7 meta tics removed; §7 ¶3 re-attributed from "scored" to "coded by structure"; §5.5
  normalization stated as following from the n−1 identity, not a finding; the §4 diverse-case clause).
  No regression. "The paper is ready."
- **R3 (org theorist): ACCEPT, up from MINOR.** All three residuals resolved, two with the exact fix
  named (the MTurk slate relabel; the §6 "survives" → "the coding reaching the same structure"). The
  demotion did not hollow the contribution; no new over-sell. One trivial style note: the new §4
  clause used a "not X, but Y" construction (CLAUDE.md rule 5).

## Applied this pass
- The §4 "not the absence of a choice" construction (R3's lone style note) → "Diverse-case selection
  is still an author's choice, disciplined along a declared axis: …" (removes the banned tic, keeps
  the concession).

## Standing after round 3
The panel is at unanimous ACCEPT. No reviewer found a computational error in any of the three rounds;
every load-bearing number reproduced three times. The contribution is stated at the altitude the
evidence supports — a claim about the coding procedure (sector- and seat-blind structural coding of
real organizations), not a discovery about the world. The honesty postures all hold end to end
(demonstration-not-validation, construction-not-discovery, magnitude-ordinal, power
necessary-not-sufficient, cases provisional). Remaining work is standing posture, none blocking and
all disclosed in-draft: the author's fieldwork replaces the provisional case evidence; outcome-
validation is the named empirical program; academic citations to be Crossref-verified at finalization;
the Doty & Glick typology-as-theory specifics to firm up; and the title is an open author choice.
