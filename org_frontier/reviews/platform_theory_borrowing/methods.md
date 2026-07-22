# Methods — theory borrowing in platform-governance research

## Corpus boundary (explicate)
- **Substantive:** sources that study a digital or economic *platform* as an organizational or economic
  object — its governance, strategy, architecture, market structure, ecosystem, complementors, or the
  management/control of platform-mediated work — and that import or engage an identifiable body of
  theory to do so. Pure operations/engineering treatments of "platforms" (product platforms in
  manufacturing, IT middleware, biological ecosystems) are out of scope; a platform-strategy or
  platform-governance framing is in.
- **Procedural:** English-language; indexed by the Scholar Gateway semantic-search connector;
  2001–present (Rochet & Tirole's founding two-sided-market work was 2003, so the field's window opens
  just before). A source is included iff its title or abstract concerns a platform as an
  organizational/economic object and carries a theoretical frame, with a substantive abstract (≥150
  characters).

## Search and harvest (execute)
- **Seed set:** Scholar Gateway `semanticSearch` over eleven natural-language queries crossing platform
  governance / strategy / ecosystem / work with the candidate parent theories (transaction-cost
  economics, two-sided markets, resource dependence, network embeddedness, institutional theory,
  ecosystem theory, agency/algorithmic control, boundary resources), including two period-restricted
  queries (2001–2014, 2005–2016) to recover early platform-economics work.
- **Screening:** candidates deduplicated by DOI and title, then passed through a boundary rule
  (platform-as-organization vocabulary present, off-domain noise absent, abstract substantive). The
  platform-labor cluster was large; to hold the corpus near the arm's ~50–80 target it was capped by
  keeping every governance/strategy/economics/ecosystem source and every pre-2015 source, then filling
  the remaining slots from the platform-labor cluster in (year, title) order. The screened-out set
  (`literature/screened_out.jsonl`, N≈733) is logged so coverage is auditable.
- **Stopping rule:** queries were exhausted when additional queries returned no new in-boundary
  sources.
- **Result:** 80 in-boundary sources (`literature/corpus.jsonl`), 15 pre-2015 and 65 in 2015+.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `parent_theory`, `borrowing_mode`, `multi_theory`, `year`.
- Coders: three independent agents, blind to one another, each → `coding/coder<X>.jsonl`, coding from
  the title + abstract in `literature/corpus.jsonl`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, majority-vote adjudicated
  dataset → `results/frozen.json`.

## Analysis (evaluate)
- **H1** — the `parent_theory` distribution split by period (pre-2015 vs 2015+): economics theories'
  share early, institutional/ecosystem share late.
- **H2** — the `borrowing_mode` distribution (share `apply`).
- **H3** — the `multi_theory` rate (share `yes`).
- Each hypothesis is reported with its statistic and a supported / qualified / challenged verdict, with
  the reliability figure attached. Limitations: agent coders rather than trained humans; a corpus
  bounded by one semantic-search connector and by the platform-labor cap; parent-theory attribution
  from an abstract, which can miss a secondary theory named only in the full text.

This review is content-coding only; it does not use the citation-graph tooling (`lib/harvest.py`,
`lib/bibliometrics.py`), because none of H1–H3 is a cross-citation claim.
