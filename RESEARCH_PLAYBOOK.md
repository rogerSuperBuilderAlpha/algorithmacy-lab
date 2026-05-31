# Research playbook: from "interesting paper" to a defensible contribution

A reusable process for turning a recent paper or open question into a rigorous, reproducible,
publishable contribution. Distilled from the `psi_vs_phi/` engagement (a direct test of Kearney 2026's
ψ against exact IIT-4.0 Φ), which is the worked example referenced throughout. The steps generalise to
other questions and other fields; substitute your own ground-truth instrument for the exact-Φ oracle.

The order matters less than the discipline. Two rules carry most of the weight:

1. **Validate the instrument on the source's own controls before computing any comparison.** Every
   real bug and overclaim in this project was caught this way — an implementation error in a measure,
   an arithmetic slip in a worked example, a hand-wavy mechanism story that the numbers refuted.
2. **Compute, do not assert.** When a claim can be checked against ground truth or a reviewer flags a
   piece of reasoning, run the numbers rather than arguing. Several "obvious" claims turned out wrong.

---

## Phase 0 — Target selection

- Pick a target that is recent, specific, and has a falsifiable hook. The best targets state an open
  question explicitly ("work must be done to connect X to Y"). That sentence is your research question.
- Confirm you hold, or can build, a **ground-truth instrument** the original authors lacked. Here it
  was an exact-Φ oracle feasible on small systems. Without ground truth you can only compare proxies,
  which is a weaker engagement.
- Decide the scope tier up front: Tier A (the cheapest decisive test) vs Tier B (the harder structural
  claim). Do Tier A first; it is often enough for a complete contribution.

## Phase 1 — Foundation (project folder, concepts, literature)

- Create a dedicated project folder with a clear `README.md` stating the question and the result slot.
- **Concept map** (`concepts.md`): list every theory and construct the target bridges, so you know what
  must be explained and what the failure modes are.
- **Deep research** (the `deep-research` harness): fan out searches, fetch sources, return the ~25–30
  most important papers with full citations, DOIs/arXiv IDs, open-access status, and — most importantly
  — an explicit statement of the open gap your test would fill, and whether anyone has already done it.
- **Ingest** into `literature/`: per-paper notes, a `references.bib`, and PDFs.
  - **Copyright discipline (non-negotiable):** commit only open-access PDFs. For paywalled sources,
    store a note + DOI link, never the PDF. Flag OA status in the `.bib` `note` field.
- **Read the target's full text** and transcribe the key definitions verbatim into your own notes. The
  whole study rests on getting the central object exactly right; do not work from the abstract.

## Phase 2 — Question and hypotheses

- Write `research_question.md`: one falsifiable question, with **pre-registered** hypotheses. State both
  the affirmative (H1) and the structurally-expected null (H0) so that a null is informative rather than
  a non-result. Record any caveats (definitional ambiguities, regimes where the measure is undefined).
- Name the outcome that each hypothesis predicts before running anything.

## Phase 3 — Methods (study comparators first)

- Before writing your own methods, read the methods sections of 2–3 comparator papers in the same genre
  and adopt their best practice (statistics, controls, reporting).
- Write `methods.md` specifying: the system ensemble (exact parameters, not prose), the ground-truth
  computation, the measure under test (full formulas), the controls, and the statistics. A reader should
  be able to reproduce the design without reading the code.
- Reuse verified infrastructure rather than reinventing it. Here: the `proxy_audit` ensemble generator
  and exact-Φ oracle, and the `candidate_audit` measure harness. New code was limited to the measure
  under test and the run/analyse scripts.

## Phase 4 — Implement and VALIDATE THE INSTRUMENT (before any comparison)

- Implement the measure under test directly from the transcribed definitions.
- **Run the source's own worked controls and assert they pass before computing a single comparison
  number.** For ψ: zero on circulant/uniform chains, the closed form on permutations, non-negativity,
  and agreement of two equivalent definitions to machine precision. This is the step that catches
  implementation bugs while they are still cheap to fix.
- Add a small hand-checked worked example for the reader, and verify its arithmetic in code. (Our first
  worked example had an error in the transition matrix; the code check caught it.)

## Phase 5 — Run experiments and build results

- Generate the dataset reproducibly under fixed seeds; record everything to CSV keyed by network index.
- Compute the primary statistics plus the robustness battery a referee will ask for. The ones that
  mattered here, all cheap and all worth doing up front:
  - **Aggregation robustness** (report the result under every reasonable aggregation of the target).
  - **Multiple seeds** and a pooled estimate.
  - **Within-stratum breakdowns** (a Simpson's-paradox check).
  - **A power / minimum-detectable-effect statement**, so a null can be read against what the design
    could have found.
  - **A positive control** — a measure that *should* track ground truth — to prove the test is alive.
    Without it, a null is uninterpretable.
- **Effect size vs significance:** with large pooled samples, trivial effects cross significance. Report
  the effect size and what fraction of variance it explains, not just the p-value.

## Phase 6 — Steel-man the objections by building, not arguing

- Anticipate the strongest objections and, where possible, **construct the thing the critic would
  demand** rather than rebutting it in prose. For ψ this meant building a partitioned measure (ϕ_ψ) to
  test whether the missing partition step was the issue, and computing the alternative theory version
  (IIT 3.0) to close the version objection. Both produced new, decisive results.
- Add **analytic minimal examples** that exhibit the mechanism by hand (here, two tiny systems where the
  measure ranks integration backwards), at matched size so no confound remains. Aggregate statistics
  convince; a two-line example makes the mechanism undeniable.

## Phase 7 — Write the paper

- Structure: Abstract, Introduction, Background (explain every construct), Methods, Results, Discussion,
  Limitations, Conclusion, Data/code availability, Acknowledgments, References.
- **Explain every construct and every inferential step.** A reader should not need the source paper to
  follow the argument.
- **Argue, but in the register of the field.** Take positions and rebut objections, using
  concession-then-claim structure ("There are encouraging results. However, …"). Study the actual
  writing of the papers you cite (extract them with `pdftotext`) and match it.
- **Avoid the AI-prose tells:** em-dash punches, bold-for-drama, argument meta-commentary ("we will
  argue four claims"), breathless adjectives ("decisive", "with teeth"), and rhetorical asides ("Hold
  onto this:"). Plain declarative sentences carry more weight.
- Scope claims precisely to what was tested (here: the system-level scalar, not the repertoire-level
  derivation). State what the result does *not* establish.

## Phase 8 — Citation integrity (non-negotiable pass)

- Every in-text citation must resolve to a `references.bib` entry; the `.bib` must back the text.
- Verify author names, years, and venues. Watch for compound surnames (e.g. "Lundbak Olesen", not
  "Olesen & Waade"), single-author works wrongly given "et al.", and preprint-vs-published year
  conflicts (e.g. a concept's preprint year vs its journal year).
- Do not let a citation enter on model output alone; confirm it exists.

## Phase 9 — Reproducibility and version control

- The study must run end-to-end from documented commands (controls → dataset → comparator → analysis →
  figures), built on a versioned oracle. List the exact commands in the paper's availability section.
- Commit each milestone with a descriptive message. Branch off the default branch unless directed
  otherwise. Push only when the user asks. Plan a citable archive (Zenodo DOI + frozen tag) for the
  final version.

## Phase 10 — Review cycles

- Solicit external review. Treat every flagged item as one of three kinds:
  - **A reasoning error** — fix by computing the truth, then rewrite. (Two of our §5/§4 claims were
    wrong and only computation revealed it.)
  - **An overstatement** — soften the modal (a structural *argument*, not a *theorem*).
  - **Polish** — titles, prose, citations, figure captions.
- Re-run the full pipeline after substantive changes so the cited numbers always match the code.

## Phase 11 — Outreach

- Send the original author a courtesy copy before wide circulation, in collegial terms, inviting
  correction. Use their published correspondence address; prepare it as a draft for the human to review
  and send (outward correspondence is the human's call). Only mark it "sent" in the acknowledgments once
  it actually is.

---

## Reusable file layout

```
<project>/
  README.md            question + result slot + pointer to the paper
  concepts.md          concept map of the theories/constructs involved
  research_question.md falsifiable RQ + pre-registered H1/H0 + caveats
  methods.md           design, ensemble params, ground truth, measure, stats
  <measure>.py         the measure under test + its validation controls
  run.py               ensemble -> ground truth + measure(s) -> results/*.csv
  <comparator>.py      alternative-theory or alternative-version oracle
  dissociation.py      hand-built minimal examples exhibiting the mechanism
  analyze.py           all statistics + robustness battery
  figures.py           publication figures
  results/             CSVs, summary, figures
  FINDINGS.md          numbers + verdict + caveats
  results_section.md   prose results (precursor to the paper)
  paper_draft.md       the assembled paper
  literature/
    references.bib     bibliography (OA flagged)
    notes/             per-paper ingestion notes
    pdfs/              open-access PDFs only
    deep_research_report.md
```

## The short version

Find an explicit open question you can answer with ground truth the authors lacked. Pre-register the
hypotheses. Validate the instrument on the source's own controls before computing anything. Run the
robustness battery and a positive control up front. Answer objections by building, not arguing. Compute
every claim. Write plainly and cite honestly. Make it reproducible end to end. Then tell the author.
