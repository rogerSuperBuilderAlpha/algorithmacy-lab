# Process: the research playbook, adapted to this dissertation

This dissertation follows the repo's [`RESEARCH_PLAYBOOK.md`](../RESEARCH_PLAYBOOK.md), adapted to three
paper-types. The two load-bearing rules carry over unchanged: **validate the instrument on its own controls
before computing any comparison**, and **compute, do not assert**. So do the universal disciplines: run the
full **deep-research harness** (never a quick scan — target ~25–30 sources + an explicit gap check); write
**~the venue's length** explaining every construct and decision; **match the cited papers' register** (read
them first; short noun-phrase section titles; run the de-slop checks); **citation integrity** (every cite
verified, resolves to the `.bib`); **self-review before and after every substantial change**.

What differs is the *instrument* and the *ground truth*, which depend on the paper-type.

## Mode A — integrative review (Paper 1)

- **Instrument / ground truth:** the literature itself. "Validate before comparing" becomes the
  **charitable-extension test** — represent each competing construct in its strongest form before showing it
  cannot reach the triad. A straw-manned foreclosure is the failure mode.
- **Register & length:** *Academy of Management Annals* (the existing draft and the cited *Annals* reviews
  are the style anchor); ~12–20k words, not the 8k of the IIT papers.
- **No measurement formalism** (scope discipline): the construct stands on the triad's structure alone.
- **Citation integrity is the binding constraint:** management reviewers verify every cite.

## Mode B — construct development + measurement (Paper 2)

- **Instrument is literal:** exact IIT-4.0 Φ over an application-layer transition matrix, reusing
  `proxy_audit.exact_phi` and `pyphi.new_big_phi.evaluate_partition` (the worker–system–counterpart
  partition) under `~/iit-playground/venv-4.0/bin/python`.
- **Validate on controls first:** a factoring TPM → Φ ≈ 0; a known-irreducible coupling → Φ > 0 that the
  W–S–C partition cannot reduce. Pre-register the **state-individuation rule** (the single empirical
  commitment) before any computation.
- **Construct-clarity discipline** (Suddaby 2010; Cronbach & Meehl 1955): definition, domain, dimensions,
  discriminant position, nomological network.
- **Compute the worked examples; report the actual Φ values.**

## Mode C — experiment (Paper 3)

- **Instrument:** Paper 2's, applied uniformly across platforms; ground truth = an **observed coordination
  outcome** (the calibration anchor — the load-bearing decision).
- **Robustness/honesty battery** as in the IIT experiments: granularity discipline, seeds where stochastic,
  report what is dropped; validation is feature-tied-to-outcome (the readability precedent).
- **Unit is the platform, not the person.**

## Per-paper load-bearing decisions (name them, don't hide them)

| Paper | Load-bearing decision |
|---|---|
| 1 | fair representation of each foreclosed construct (charitable-extension test) |
| 2 | the state-individuation rule (pre-registered) |
| 3 | the calibration anchor (and the Chicago TNC dataset that supplies it) |

## Reuse & environment

- Φ instrument: `from proxy_audit import exact_phi`; `pyphi.new_big_phi`. Env:
  `~/iit-playground/venv-4.0/bin/python`.
- **Copyright:** source PDFs are paywalled and stay in `sources/pdfs/` (gitignored); DOIs live in each
  paper's `references.bib`. Draft prose is the author's and may be committed (this is a public repo).
