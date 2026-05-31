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

Full craft reference (with verified sources): `paper1_review/literature/integrative_review_methodology.md`.
The genre standard, distilled:

- **An integrative review derives NEW insight through synthesis/critique — it is not a summary** (Cronin &
  George 2023; Torraco 2005/2016). The contribution must be "beyond a review": a theoretical/construct
  contribution (Post et al. 2020). A *theory-driven* review is both **integrative** (synthesize prior work)
  and **generative** (produce the new construct/framework), aligning with prior work while diverging from it
  (Breslin & Gatrell 2023). Payoff = a **new conceptual framework** (here: the algorithmacy construct).
- **State the methodological warrant** (Torraco's case (b): an *emerging* topic needing a construct).
- **Frame by problematization, not gap-spotting** (Alvesson & Sandberg 2011): the variance puzzle as the
  surface of a structural change; five-Cs intro (Lange & Pfarrer 2017).
- **Instrument / ground truth = the literature.** "Validate before comparing" becomes the
  **charitable-extension test** — represent each foreclosed construct in its *strongest* form before showing
  it cannot reach the triad. A straw-manned foreclosure invalidates the contribution (the #1 failure mode).
- **Auditability even though not systematic** (Snyder 2019; Sauer et al. 2023; Rousseau 2024): anchor the
  corpus at the construct's level of analysis; construct-by-construct citation search (forward/backward
  tracing, not keywords); explicit inclusion/exclusion criteria; a **comparison/synthesis table** of the
  foreclosed constructs (× structural commitment × where each stops short).
- **Bridge across disciplines explicitly** (Cronin & George 2023): the contribution lives across fields no
  single one produced (communication / IS / org studies / literacy studies).
- **Construct clarity** for the new construct (Suddaby 2010; Cronbach & Meehl 1955): definition, domain,
  dimensions, discriminant position, nomological network.
- **Future-research agenda is a real contribution** (Elsbach & van Knippenberg 2020): it opens the
  measurement program (Papers 2–3).
- **No measurement formalism** (scope discipline): the construct stands on the triad's structure alone.
- **Register & length:** *Academy of Management Annals* (the existing draft + cited *Annals* reviews are the
  style anchor); ~12–20k words, not the 8k of the IIT papers. **Citation integrity is binding** — management
  reviewers verify every cite; resolve every cite to the `.bib` and confirm it directly.

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
