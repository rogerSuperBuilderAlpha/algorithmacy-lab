# Protocol — entry point

A fixed pipeline for taking a research question to a finished quantitative paper, plus the machinery to
run it and the work that validated it.

## What is here

- **`RESEARCH_PROTOCOL.md`** — the six-stage per-question pipeline (review, deep research, five
  hypotheses, methods, run, paper), the quality gates, and the reusable infrastructure each stage uses.
  The authoritative spec.
- **`template/`** — the per-question directory template (`review.md`, `hypotheses.md`, `methods.md`,
  `paper.md`, `FINDINGS.md`, `probe_template.py`). Copy it to `questions/q<NN>_<slug>/` to run a question
  by hand.
- **`question_pipeline.js`** — the Workflow script that runs all six stages automatically for one
  question. Manual execution by the template is the fallback whenever the automated run is brittle.
- **`methodology_review.md`** — a Stage-1 review of the protocol itself against established norms.
- **`literature/deep_research_report.md`** — a Stage-2 deep-research run on the methodology, with
  `references.bib`. Key finding: the per-hypothesis method plan (Stage 4), not the bare pre-commitment
  (Stage 3), is what the evidence shows buys credibility (Brodeur 2024).

## Running a question automatically

Invoke the Workflow tool with the script and the question as args:

```
Workflow({
  scriptPath: "org_frontier/protocol/question_pipeline.js",
  args: { id: "16", slug: "two_coupled_triads",
          question: "<full question text>", startProbe: <next free probe number> }
})
```

The script writes the question's directory under `org_frontier/questions/`, calls the `deep-research`
workflow inline for Stage 2, fixes five hypotheses, designs and runs the probes against the exact-Φ
instrument (validating a known control first), appends the result rows to `probes/PROBES.md`, and assembles
the paper with a de-slop pass. It returns the directory path, the hypotheses, and the per-hypothesis
verdicts.

## The pilot

`questions/q43_thompson_interdependence/` is the first question run end to end through the automated
pipeline: whether the dyadic/triadic verdict reproduces Thompson's (1967) pooled/sequential/reciprocal
interdependence ordering. Result: four hypotheses confirmed, one refuted (probes 135–139). The ordering
breaks, two of the three types are verdict-ambiguous on a single edge, and the proposed two-primitive
replacement fails. The run validated the orchestration with no manual fallback.

## The public write-up

`../essays/how_to_research_with_ai.md` argues the general method, grounded in the methodology research and
the 134-probe track record, with the Q43 pilot as the worked example.

## The queue

`../RESEARCH_AGENDA_50_V2.md` holds 50 questions. Q43 is done; the rest are pending.
