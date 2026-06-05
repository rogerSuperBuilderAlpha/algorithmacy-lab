# Research protocol: from a queued question to a finished paper

A fixed pipeline for taking one research question through to a complete quantitative paper. It applies to
the 50 questions in `RESEARCH_AGENDA_50_V2.md` and to any future question the lab adds. Each question runs
the same six stages, produces the same artifacts, and passes the same gates.

This protocol is self-contained. It overlaps with `RESEARCH_PLAYBOOK.md`, which covers a different job —
engaging an external paper with a ground-truth instrument the authors lacked. When the two disagree, this
protocol governs question-driven work and the playbook governs paper-engagement work. The shared quality
gates below are stated here in full so a reader needs only this file.

## Two rules that carry the weight

1. **Compute, do not assert.** When a claim can be checked against exact Φ, run it. Across 134 probes the
   claims that sounded obvious and turned out wrong were caught only by running the numbers.
2. **Fix the hypotheses before computing.** Stage 3 writes H1–H5 and their nulls before any test runs, so
   a null is a result and not a non-finding.

## The six stages

Each question lives in its own directory under `org_frontier/questions/q<NN>_<slug>/`. A stage may not
start until the previous stage's gate passes.

### Stage 1 — Cursory review
**Purpose.** Place the question against what the lab already knows, so the new work extends rather than
repeats. **Artifact:** `review.md` — the question stated precisely, the prior probes that bear on it (by
number, from `probes/PROBES.md`), what they found, and the specific gap this question opens. **Reused
infrastructure:** `probes/PROBES.md`, the `RESEARCH_PROGRAM*.md` readings, `STRUCTURAL_FINDINGS.md`.
**Gate:** the review names at least the directly-related probes and states one sentence on why the
question is not already answered. If a prior probe answers it, stop and record that.

### Stage 2 — Deep research
**Purpose.** Find what the wider literature already establishes, and whether anyone has answered the
question outside the lab. **Artifact:** `literature/deep_research_report.md` plus `literature/references.bib`.
**Reused infrastructure:** the bundled `deep-research` workflow (web). **Gate:** the report returns real
sources with DOIs or arXiv IDs and open-access status, states the open gap explicitly, and says whether
the gap is already closed. A scan of two or three known papers is not a substitute; the target is roughly
15–30 sources. Commit only open-access PDFs; for paywalled sources store a DOI link, never the PDF.

### Stage 3 — Five hypotheses
**Purpose.** Turn the question into five falsifiable predictions that together cover the space, in the
spirit of multiple working hypotheses rather than one favored guess. **Artifact:** `hypotheses.md` — H1
through H5, each with the structurally-expected null H0 stated alongside, and the outcome each predicts
named in advance. **Gate:** all five are written and committed before any computation; each is falsifiable
by a test the next stage can design; the five are distinct, not rephrasings of one. **The count is a
discipline, not a principle.** Chamberlin (1890) prescribes "every tenable hypothesis," and the number is
set by the phenomenon. Five guards against single-hypothesis attachment; it is informative only if the
five are identifiable under the instrument (Yanco 2020). Drop to fewer when the question genuinely admits
fewer distinct, separable predictions, and say so.

### Stage 4 — Methods
**Purpose.** Specify, per hypothesis, the exact test. **Artifact:** `methods.md` — for each hypothesis: the
form or ensemble (exact rules or parameters, not prose), the measure (verdict, Φ, major complex, or a
named information measure), the controls, and the statistic that decides the hypothesis. **Reused
infrastructure:** `classifier/classifier.py` (`classify_rules`, `tpm_from_rules`, `cm_from_rules`),
`probes/lib.py` (`verdict`, `major_complex`, `max_phi_float`), `probes/_info.py` (entropy, mutual
information, transfer entropy, O-information), `proxy_audit/exact_phi.py` (exact Φ, trajectories). **Gate:**
a reader could reproduce every test from `methods.md` without the code; each hypothesis has a decision
rule fixed before the run. **This stage carries the credibility.** The evidence on pre-registration is that
fixing hypotheses alone changes little; the complete pre-analysis plan is what reduces p-hacking (Brodeur
2024). The decision rule named here, before the run, is the load-bearing commitment — not the bare act of
listing hypotheses in Stage 3.

### Stage 5 — Run the tests
**Purpose.** Execute the methods and capture results. **Artifact:** `probe_*.py` scripts (the existing
probe pattern — module docstring with question, hypothesis, method, and run command), `results/` outputs,
and new rows appended to `probes/PROBES.md` continuing the global numbering. **Gate (instrument
validation, non-negotiable):** before trusting any comparison, the instrument must reproduce a known
control — a form whose verdict is already established (a strict-mediation triad reads triadic at Φ=2.0; a
relay reads dyadic). Run on `~/iit-playground/venv-4.0/bin/python`. Record exact numbers; a probe that
refutes its hypothesis is logged as refuted.

### Stage 6 — The paper
**Purpose.** Write the finding as a complete quantitative paper. **Artifact:** `paper.md` with the standard
structure — Abstract, Introduction, Related work (from Stage 2), Hypotheses, Methods, Results, Discussion,
Limitations, References — and a compact `FINDINGS.md` (numbers, verdicts, caveats). **Gate:** every number
in the paper traces to a `results/` file or a logged probe; H1–H5 appear as fixed in Stage 3; refuted
hypotheses are reported as refuted; the prose passes the de-slop checks below; every citation resolves to
`references.bib`.

## Quality gates that apply throughout

- **Instrument validation before comparison.** Stage 5 will not produce a comparison number until a known
  control passes. Most real bugs surface here.
- **The validation gap.** A passed computational test is evidence about the model, and at most about a
  second model that reproduces it (docking; Axtell 1996). It is not yet evidence about a real organization.
  Cross-model agreement establishes internal validity; external validity to organizations is a separate,
  unmet claim. Every paper states this in Limitations and does not overread the in-silico result.
- **Honest nulls.** A refuted or partial hypothesis is a first-class result. The 134-probe logbook is
  roughly one-third nulls and refinements, and that mix is what makes it credible.
- **De-slop pass on all prose** (`CLAUDE.md`). No first person. Cut the antithesis machine (`, not X`,
  `X rather than Y`, `is not a/the/an`), self-narration of rigor, and metronomic short openers. Mechanical
  check per ~1,000 words: the combined antithesis count well under five, self-honesty phrases at zero,
  fragment openers at most one in three. Section titles are short noun phrases.
- **Citation integrity.** Every in-text citation resolves to a real source in `references.bib`; author
  names, years, and venues verified; no citation enters on model output alone.
- **Reproducibility.** The paper's methods plus the committed `probe_*.py` reproduce every figure from the
  venv. Commit each stage; push to `origin/worktree/org-frontier`; leave `dissertation/` untouched.

## Running it

Two ways to run the pipeline:

- **Automated:** the Workflow script `org_frontier/protocol/question_pipeline.js`, invoked with the
  question text and id as `args`. It runs the six stages in order, calling the `deep-research` workflow
  inline for Stage 2 (a workflow may call one other workflow; deeper nesting is not allowed). See
  `protocol/README.md` for the invocation.
- **Manual:** copy `org_frontier/protocol/template/` to `questions/q<NN>_<slug>/` and fill each artifact by
  following the stages. This is the fallback whenever the automated run is brittle, and it is the
  authoritative definition of what each stage must produce.

## The short version

Place the question against the logbook. Research the literature for real and confirm the gap is open. Fix
five falsifiable hypotheses with their nulls before computing anything. Specify each test exactly. Validate
the instrument on a known control, then run, logging refutations as refutations. Write a paper that
explains every construct, cites honestly, and survives the de-slop checks. Make it reproducible from the
venv.
</content>
