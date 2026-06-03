# Paper 3 rebuild — plan, scope, and final state

> **STATUS: COMPLETE — unanimous ACCEPT (Stage 4).** Paper 3 was rebuilt from scratch with
> brand-new deep research and five real-corporation case studies as the spine, then taken through
> a five-round adversarial panel to unanimous ACCEPT, including a §7 discriminant-checks section
> (dyadic controls + a micro-scenario catalog) added and re-reviewed to ACCEPT. No reviewer found a
> computational error in any round; every load-bearing number has reproduced five times. Cases are
> provisional (public-documentation evidence; the author replaces them with field data). The full
> adjudication is in `ADVERSARIAL_REVIEW.md`.

## Review trajectory and commits (branch `rebuild/paper-by-paper`)

- `700fec7` — from-scratch rework: research, computation, draft.
- `469625e` — Stage 4 round 1: 2 MAJOR + 1 MINOR (all framing; no computational error).
- `05193ef` — round 2: ACCEPT + 2 MINOR + copy-edit.
- `7edc656` — round 3: **unanimous ACCEPT**.
- `3e35f85` — merge §7 discriminant checks (dyadic controls + micro-catalog).
- `31369bc` — round 4 (full panel on merged draft): 1 MINOR + 2 ACCEPT-conditional + corrective.
- `44c1ee3` — round 5: **unanimous ACCEPT** with §7 included.

## What stays vs. what was rebuilt

- **Stayed (the computation).** The model inherited from the ACCEPTed Paper 2. `phi_core.py`
  (PyPhi-only, n-general) reproduces Paper 2's controls exactly at n=3 (0.000 / 0.830 / 2.000).
- **Rebuilt from scratch (the paper).** Framing, research base, architecture, and the cases. The
  4,144-form catalog and the typology are supporting breadth; the five real-corporation case
  studies are the spine.

## The five case studies (LOCKED slate; provisional content, field data later)

Diverse-case theoretical sampling: span industries and exercise the structural claim (the score
tracks determination structure, not the mediator's seat) via two "same structure, different seat"
twins plus a higher-order extension. Hold party count fixed, vary structure (the cut-anchor lesson).
All five are large, publicly documented corporations; cases use public information only.

| # | Organization | Industry | Structure | Φ band | Seat |
|---|---|---|---|---|---|
| 1 | Uber Technologies | transportation / ride-hailing | strict mediation | 2.00 | algorithmic |
| 2 | NYSE / Nasdaq (securities exchange) | financial markets | strict mediation | 2.00 | market institution (twin of #1) |
| 3 | Upwork Inc. | online labor / professional services | partial mediation | 0.83 | algorithmic |
| 4 | ManpowerGroup | staffing & workforce solutions | partial mediation | 0.83 | human-institutional (twin of #3) |
| 5 | Amazon Mechanical Turk | crowdwork / digital labor | higher-order strict | 3.00 (n=4) | algorithmic |

The two equal-Φ pairs (1≈2 at 2.00; 3≈4 at 0.83) are each an identity-by-construction (not a
"replication") on Φ and a theoretical contrast on the seat, carrying the structure-not-seat
headline; #5 is the higher-order theoretical replication, reported with its size-normalized value
(Φ/(n−1) = 1.00, the strict level). The earlier (vetoed) healthcare-staffing case was dropped; the
slate is corporate-only.

## §7 — discriminant checks (added in the merge, reviewed to ACCEPT)

- **Dyadic negative-control class** (`dyadic_cases.py`, in-body): five real forms judged dyadic,
  predicted Φ=0. Three come up dyadic (telecom, email, SaaS tool); two are reported findings — a
  payment processor at 0.83 (joint authorization) and Craigslist at 1.00 (a contestable coding; a
  clean route-around factors to 0). The control falsified its own predicted zero in 2 of 5, which is
  what a control is for. This is the discriminant-validity evidence the paper lacked.
- **Micro-scenario catalog** (`micro_scenarios.py` → `MICRO_SCENARIOS.md`, an illustration, table in
  the supplement): 103 surface-distinct everyday activities coded by mechanism land on a few
  structural levels; the per-band counts are a property of the authored sample, not a world
  frequency. The point is qualitative: the score reads mechanism, not surface.

## Scope (what Paper 3 does)

1. **Applies the tool generally.** Enumerate the whole W–S–C model family (4,144 wirings), compute Φ
   for each, show the discrete bands, place a typology on the populated bands. Model-internal: the
   score tracks the structure of how parties reach each other, not the technology in the middle. The
   2.00 band is not the "strict-mediation band" — only 16 of 40 strict wirings reach it, the sharper
   "Φ is not a feature checklist" result.
2. **Case studies on five real corporations.** Model each from how it actually coordinates, compute
   Φ, read the case. Grounded analytic applications, not statistical outcome-calibration. The
   equality within a pair is a modeling property (identical coding), not a discovery; the
   contribution is the sector- and seat-blind coding discipline.
3. **Discriminant checks (§7).** The dyadic control class and the micro-catalog (above).

## Artifacts

- Computation: `phi_core.py`, `catalog.py`, `analyze_catalog.py`, `typology.py`, `cases.py`,
  `dyadic_cases.py`, `micro_scenarios.py`, `review_response.py`.
- Paper: `DRAFT.md` (10 sections, Nagel/ORM, no first person). Scaffold: `OUTLINE.md`,
  `OUTLINE_DETAILED.md`. Supplement: `MICRO_SCENARIOS.md`.
- Research notes: `research/{case_study_methodology,framing_and_positioning,organization_mechanisms}.md`.
- Review log: `ADVERSARIAL_REVIEW.md` (five rounds).
- `CASES_FIELDWORK_TEMPLATE.md` — fabricated, conspicuously-tagged fieldwork scaffold, **kept OUT of
  `DRAFT.md` by design**; the author replaces its tagged placeholders with real field data.

## Process (locked, executed, same as Paper 2)

Full from-scratch rebuild, PyPhi-only, compute-don't-assert, Nagel style (CLAUDE.md), ORM register,
Stage 4 adversarial review iterated to ACCEPT.

## The cut-anchor lesson (the methodological rationale, retained)

The earlier rideshare "anchor" was cut because, in the pooling model, Φ = k + 1 for a pool of k
riders, so Φ was a linear function of party count. Correlating it with pooling friction only
validated the party-count axis — the one axis you do not need Φ to see. The scale's novel content is
that determination *structure* separates forms at a *fixed* party count (parity 0.50 vs partial 0.83
vs strict 2.00 at n=3). So the cases hold party count fixed and vary structure. The cut scripts live
in `../exploratory/`; their numbers are cited nowhere.

## Remaining work (standing posture, none blocking, all disclosed in-draft)

- **Fieldwork.** The five cases are provisional; the author gathers primary data to replace the
  public-documentation evidence, using `CASES_FIELDWORK_TEMPLATE.md` as the scaffold (and the
  per-case "what field data must establish" checklists in it).
- **Outcome-validation.** Vary determination structure at a *fixed* party count against an observed
  coordination outcome — the named empirical program the paper opens.
- **Citations.** Re-verify every academic citation against Crossref before submission (the Paper 1/2
  discipline). Firm up the Doty & Glick typology-as-theory specifics.
- **Title.** Open author choice. Working default: "The Structure of the Middle: A Graded Score of
  Coordination Forms and Five Corporate Cases." Alternatives offered; author to pick.
- **Paper 2 coherence (flagged, not yet acted on).** Paper 2 (ACCEPTed) says "Calibration against
  coordination outcomes is Paper 3" (abstract, §4, §10, §11). Paper 3 does case-study application and
  discriminant checks, not statistical outcome-calibration. Soften Paper 2's forward-promise to match
  — e.g. "applying and case-studying the instrument is Paper 3; outcome-calibration is the empirical
  program it opens." An author decision; do not touch Paper 2 unprompted.
