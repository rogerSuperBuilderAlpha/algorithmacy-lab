# q220 — Literature: retrospective contextual review (placeholder, not yet written)

**Status: placeholder.** This file stands in for the Stage 2 artifact of
[`RESEARCH_PROTOCOL.md`](../../../protocol/RESEARCH_PROTOCOL.md) (`literature/deep_research_report.md`
with `literature/references.bib`). That stage was not run for q220. Both experimental stages were designed,
preregistered and run against in-lab prior work only (`review.md`): stage 1 was preregistered in `1a77f73`
and run in `4d97bb00`; stage 2 was preregistered in `48e479f4` and run in `f084e3f3`.

When this review is written it will be a **retrospective contextual review, written after the
experiments**. It did not inform the questions, the hypotheses, the decision rules or the estimators, and
it cannot be read as if it had. The verdicts recorded in `results/`, `stage2/results/`, `FINDINGS.md` and
`paper.md` stand as run; the review can change how they are placed against prior work, not what they are.

## What the review has to establish

The protocol's gate: real sources (roughly 15–30) with DOIs or arXiv IDs and open-access status, the open
gap stated explicitly, and a statement of whether that gap is already closed elsewhere. Open-access PDFs may
be committed; paywalled sources are stored as a DOI link only. Every entry is checked against the source
itself (authors, year, venue); no citation enters on model output alone.

## Questions it has to answer

1. **CRQA foundations.** The categorical cross-recurrence measures that `org_frontier/recurrence/crqa.py`
   implements and attributes to Webber and Zbilut (1994), Marwan et al. (2007) and Coco and Dale (2014).
   These three are cited in `paper.md` and do not yet resolve to `references.bib`.
2. **Lagged coupling from irregular or gappy records.** Whether computing lag-k statistics only from
   observation pairs exactly k recorded time steps apart, the timestamp-aware estimator B in stage 2, is an
   established estimator in the literature on unevenly sampled or gappy time series, and under what name.
   Until this is checked, `README.md`, `FINDINGS.md` and `paper.md` describe B neutrally and make no
   claim that it is new.
3. **Missing data and recurrence quantification.** Prior work on how sample loss, and how gaps are handled
   (concatenation, segmentation, imputation), changes recurrence and cross-recurrence measures.
4. **Clock offset and temporal aggregation.** Prior work on timing misalignment between channels and on
   binning or coarse-graining as sources of bias in lagged coupling.
5. **Inference with few clusters.** The two-stage form/seed bootstrap with 12 and 30 forms, and the
   Bonferroni sensitivity check over the 10-test family.
6. **The gap.** Whether anyone has degraded the *observation* of a faithful simulated run and scored the
   behavioural reading against a ground-truth structural measure, as q220 does against exact Φ.

## Source pool

The lab's standing recurrence watch, `org_frontier/research/recurrence/literature/references.bib`, is the
first place to look. Its entries are candidates, not verified citations for this question.
