# Dissertation: the transition to algorithmacy

**Roger Hunt III, Bentley University.** A three-paper dissertation on *algorithmacy* — the communication
competency that triadic algorithmic coordination demands. Hosted here because it is the **application arc**
of this repo's integrated-information work: the earlier experiments (`proxy_audit`, `candidate_audit`, …)
validated exact IIT-4.0 Φ as a ground-truth instrument; **Papers 2 and 3 use that instrument** to measure
whether a coordination form is triadic.

> Status: **scaffolded** (structure, ingested source material, and per-paper execution plans). No paper
> drafted in this directory yet — the drafting/experiments run in later sessions per each `PLAN.md`.

## The arc

Equivalently positioned platform participants get divergent coordination outcomes through identical
algorithmic systems, and no current construct explains it. The dissertation argues the puzzle is the surface
of a structural change: **coordination has become triadic** (two parties coordinate through a third that
interprets both, acts on both, and holds its own interest), and the competency a triad demands is new in the
way literacy was new against oracy. That competency is **algorithmacy**.

| Paper | Question | Type | Instrument | Status |
|---|---|---|---|---|
| [1](paper1_review/) | Has coordination become triadic, and can existing constructs describe it? | integrative review | the literature (charitable-extension test) | draft exists (`sources/`), rebuild planned |
| [2](paper2_construct/) | Is a given coordination form triadic? | construct + measurement | exact IIT-4.0 Φ over the application layer | scaffolded |
| [3](paper3_baseline/) | How much algorithmacy does each platform demand? | experiment | Φ calibrated against observed outcomes | scaffolded (TNC data deferred) |

**Through-line:** Φ measures the one thing the dyadic/triadic distinction needs — the degree to which a
system's cause-effect structure is irreducible to its parts. A coordination form is **triadic** when its
application-layer structure is irreducible across the worker–system–counterpart partition, **dyadic** when it
factors. Paper 2 builds that decision procedure; Paper 3 calibrates it into a difficulty scale (the way a
readability score places a text).

## Layout

```
dissertation/
  README.md            this file
  PROCESS.md           the repo playbook adapted to the three paper-types
  sources/             ingested raw material (existing drafts; PDFs gitignored, DOIs in the bibs)
  paper1_review/       OUTLINE.md (v1, verbatim) + PLAN.md
  paper2_construct/    OUTLINE.md + PLAN.md
  paper3_baseline/     OUTLINE.md + PLAN.md
```

## Reuse & environment

Papers 2–3: `from proxy_audit import exact_phi`; `pyphi.new_big_phi.evaluate_partition`; run under
`~/iit-playground/venv-4.0/bin/python`. See [`PROCESS.md`](PROCESS.md) for the per-paper process and the
named load-bearing decisions (P1: fair representation; P2: the state-individuation rule; P3: the calibration
anchor).
