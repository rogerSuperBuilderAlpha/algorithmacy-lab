# Dissertation: the transition to algorithmacy

**Roger Hunt III, Bentley University.** A three-paper dissertation on *algorithmacy*, the communication
competency that triadic algorithmic coordination demands. The dissertation sits here because it is the
**application arc** of this repo's integrated-information work. The earlier experiments (`proxy_audit`,
`candidate_audit`, …) built and exercised an exact IIT-4.0 Φ oracle, and **Papers 2 and 3 adopt that Φ as a
formal model** of whether a coordination form is triadic.

> Status: **drafted and recast as a formal-model dissertation.** All three papers and both framing chapters
> are drafted. The dissertation characterizes a formal model of triadic coordination and is explicit that it
> does **not** validate the model against an observed outcome. An earlier rideshare anchor was cut because it
> validated only the trivial party-count axis (see `paper3_baseline/exploratory/`). Empirical validation is
> named as the program's next arc.

## The arc

Equivalently positioned platform participants get divergent coordination outcomes through identical
algorithmic systems, and no current construct explains it. The dissertation argues the puzzle is the surface
of a structural change: **coordination has become triadic** (two parties coordinate through a third that
interprets both, acts on both, and holds its own interest). The competency a triad demands is new in the
way literacy was new against oracy. That competency is **algorithmacy**.

| Paper | Question | Type | Instrument | Status |
|---|---|---|---|---|
| [1](paper1_review/) | Has coordination become triadic, and can existing constructs describe it? | integrative review | the literature (charitable-extension test) | draft complete (~25k) |
| [2](paper2_construct/) | Is a given coordination form modeled as triadic? | construct + formal model | exact IIT-4.0 Φ over the application layer, adopted as a model | draft complete (recast) |
| [3](paper3_baseline/) | What does the model say across organizations, and does its central prediction hold? | formal model + population study + experiment | Φ over the model family, an 86-org simulated population, and a named typology; an agent-based consistency check of the structure axis | draft complete (full paper) |

**Through-line:** Φ measures the one thing the dyadic/triadic distinction needs, the degree to which a
system's cause-effect structure is irreducible to its parts. A coordination form is **triadic** when its
application-layer structure does not factor into independent parties (Φ over its minimum-information partition
is positive), **dyadic** when some partition factors it. The binary verdict is *strictly stronger* than a
cheap factorization test, diverging on >40% of the 4,096-form family. Paper 2 builds that formal model.
Paper 3 grades it across a population of organizations and tests its central prediction in a controlled
experiment. It finds **the binary classification robust** and the **strict-mediation prediction confirmed
behaviorally**, but the **regime ordering weak in the population magnitude** (only the determination function
robustly moves Φ, and strict and partial are indistinguishable once size is fixed, so the ordering rests on the
experiment) and the **graded magnitude unreliable**. It reads Φ as a structural classifier and, at most, an
ordinal indicator anchored at one behavioral contrast, not a finished scale, and it treats the experiment as a
consistency check rather than an independent validation.

## Layout

```
dissertation/
  README.md                       this file
  PROCESS.md                      the repo playbook adapted to the three paper-types
  THREE_PAPER_STRUCTURE_REVIEW.md the format standard + the dissertation's state against it
  FRONT_MATTER.md                 title page · whole-dissertation abstract · ToC · list of tables
  INTRODUCTION.md                 Chapter 1 — framing: the overarching problem + how the papers connect
  CONCLUSION.md                   Chapter 5 — integrative discussion: the combined contribution
  BACK_MATTER.md                  reference handling · Appendix A (computational artifacts) · Appendix B
  sources/                        ingested raw material (existing drafts; PDFs gitignored, DOIs in the bibs)
  paper1_review/    (Chapter 2)   integrative review — draft/DRAFT.md (~25k)
  paper2_construct/ (Chapter 3)   construct + measurement — draft/DRAFT.md (~8k)
  paper3_baseline/  (Chapter 4)   formal model / model-family — draft/DRAFT.md (~8k)
```

**Dissertation structure (complete, with front/back matter):**
Front matter (`FRONT_MATTER.md`: title page, whole-dissertation abstract, ToC, list of tables) ·
Chapter 1 (Introduction) · Chapters 2–4 (the three papers) · Chapter 5 (integrative Conclusion) ·
Back matter (`BACK_MATTER.md`: per-chapter references, Appendix A computational artifacts, Appendix B).
The framing chapters bind the three standalone papers into one argument around the shared through-line,
following the verified three-paper format (see `THREE_PAPER_STRUCTURE_REVIEW.md`). Two items remain for final
assembly: author-supplied content (committee, date, acknowledgments) and Bentley's specific format rules.

## Reuse & environment

Papers 2–3: `from proxy_audit import exact_phi`; `pyphi.new_big_phi.evaluate_partition`; run under
`~/iit-playground/venv-4.0/bin/python`. See [`PROCESS.md`](PROCESS.md) for the per-paper process and the
named load-bearing decisions (P1: fair representation; P2: the modeling choices, above all the
state-individuation rule; P3: characterizing the model rather than validating it against an outcome).
