# org_frontier — the algorithmacy lab

A computational lab applying exact IIT-4.0 Φ to organizational coordination, with a runnable research
protocol that takes a question to a finished paper.

The thesis: a coordination form is **dyadic** when its cause-effect structure factors across the
worker–system–counterpart partition (it demands *literacy*), and **triadic** when the structure stays
irreducible (it demands *algorithmacy*). The classifier reads the verdict off exact Φ over the
minimum-information partition. The instrument is validated on its own controls (the
[`foundations/`](../foundations/) arc).

> Results are in-silico: exact Φ on small Boolean models of coordination. They are evidence about the
> models. A validation gap separates them from claims about real organizations. Every paper states this.

## The research protocol — [`protocol/`](protocol/)

A fixed six-stage pipeline, made runnable: review → deep research → five hypotheses fixed before computing
→ methods → run against the exact-Φ instrument → full quantitative paper, reporting nulls and refutations
as first-class results.

- [`protocol/RESEARCH_PROTOCOL.md`](protocol/RESEARCH_PROTOCOL.md) — the spec and quality gates.
- [`protocol/question_pipeline.js`](protocol/question_pipeline.js) — the orchestration that runs all six
  stages for one question.
- [`protocol/methodology_review.md`](protocol/methodology_review.md) and
  [`protocol/literature/deep_research_report.md`](protocol/literature/deep_research_report.md) — the
  methodology validated against established norms (strong inference, multiple working hypotheses,
  pre-registration; the pre-analysis plan, not the bare pre-commitment, is what buys credibility).

## The logbook and programs

- [`probes/PROBES.md`](probes/PROBES.md) — 134 exact-Φ experiments, each with question, hypothesis,
  method, and result. About a third are nulls or refinements.
- [`RESEARCH_PROGRAM_V2.md`](RESEARCH_PROGRAM_V2.md) … [`RESEARCH_PROGRAM_V6.md`](RESEARCH_PROGRAM_V6.md) —
  six iterative programs that produced the logbook, each closing a wave and opening the next.
- [`STRUCTURAL_FINDINGS.md`](STRUCTURAL_FINDINGS.md) — the synthesis: a coordination form demands
  algorithmacy when every party is bound into one irreducible joint determination. Substitutability
  collapses it; mediation depth does not; cheap proxies cannot detect it.
- [`RESEARCH_AGENDA_50_V2.md`](RESEARCH_AGENDA_50_V2.md) — 50 open questions queued for the pipeline.

## Worked questions — [`questions/`](questions/)

Each question taken through the protocol gets its own directory with the review, literature, hypotheses,
methods, probes, results, and a paper.

- [`questions/q43_thompson_interdependence/`](questions/q43_thompson_interdependence/) — the first question
  run end to end through the automated pipeline: does the verdict reproduce Thompson's pooled/sequential/
  reciprocal interdependence ordering? It does not. Four hypotheses confirmed, one refuted (probes
  135–139). [paper](questions/q43_thompson_interdependence/paper.md).

## Sub-studies

- [`classifier/`](classifier/) — the literacy-or-algorithmacy classifier (Φ over the MIP → verdict).
- [`corpus/`](corpus/) — a curated library of named coordination forms with exact Φ, the verdict, and
  structural tags; plus the 256-form population census.
- [`multiparty/`](multiparty/) — how the verdict changes as parties are added.
- [`principal/`](principal/) — does the corporate principal join the irreducible core? Only under
  bidirectional coupling.
- [`proxy_bridge/`](proxy_bridge/) — can a cheap time-series proxy recover the verdict past the exact-Φ
  size ceiling?
- [`landscape/`](landscape/) — a worldwide survey of PyPhi usage and the open application gaps.

## Essays — [`essays/`](essays/)

- [`studying_algorithmacy.md`](essays/studying_algorithmacy.md) — the method this lab runs: the instrument,
  how a form of work becomes a system PyPhi can read, the validate/pre-commit/report-nulls discipline, what
  it has established, and what it cannot do. The repo-specific methodology essay.
- [`literacy_or_algorithmacy.md`](essays/literacy_or_algorithmacy.md) — the thesis and how exact Φ decides
  which literacy a coordination form demands.
- [`pyphi_org_theory_catalog.md`](essays/pyphi_org_theory_catalog.md) — a ~10k-word catalog of every
  experiment, with question/hypothesis/method/result.

## Conventions

Every sub-project follows the protocol: validate the instrument on its own controls before any comparison,
fix hypotheses before computing, compute rather than assert, report nulls as results, and write in the
house style ([`../CLAUDE.md`](../CLAUDE.md)). Read the verdict on the major complex when a form has
spectator nodes.
