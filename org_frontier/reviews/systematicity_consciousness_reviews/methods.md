# Methods — systematicity in consciousness-science review articles

## Corpus boundary (explicate)
- **Substantive:** review, survey, overview, scoping, or synthesis articles whose subject is the science
  or theory of consciousness — its theories (integrated information, global workspace, higher-order,
  predictive processing, recurrent processing), its neural correlates, its measures and markers, or the
  comparison of these. Primary empirical studies, single-measure methods papers, bare
  adversarial-collaboration experiment reports, protocols, editorials, book reviews, and letters are out
  of scope: the unit is a review of a literature, not a contribution to it.
- **Procedural:** English-language articles indexed by the two semantic-search connectors used (Scholar
  Gateway, Consensus); no journal restriction; no date restriction (the corpus runs 2001–2026). Gray
  literature (preprints) is admitted only where a connector surfaced it as a review; the corpus is
  dominated by journal articles and one book chapter.
- A source is included iff its title+abstract identifies it as a review/survey/overview of consciousness
  science (a review-signal term present, no primary-empirical or off-domain signal) — the decidable rule
  implemented in `build_corpus.py` (`in_boundary`).

## Search and harvest (execute)
- Two academic semantic-search connectors, eight review-oriented queries: "literature review of theories
  of consciousness", "systematic review of integrated information theory of consciousness", "review of
  neural correlates of consciousness", "review of global workspace theory and higher order theories of
  consciousness", "scoping review of computational and mathematical models of consciousness", "review of
  predictive processing and free energy principle theories of consciousness", "review of measures and
  markers of consciousness in disorders of consciousness", "review of machine consciousness and
  artificial consciousness models", plus Consensus queries on global workspace, theory comparison, and
  NCC reviews. Raw returns stored under `literature/raw_scholar_gateway.json` and
  `literature/raw_consensus.json`.
- Merge and dedupe by normalized title; apply the boundary; enrich each kept source's citation count
  from Semantic Scholar by DOI (Consensus's own count is the fallback where no DOI resolves). Screened-out
  candidates are logged to `literature/screened_out.jsonl` (auditable).
- Stopping rule: the two connectors returned a finite ranked set per query (≤20 each); harvesting stopped
  when the eight queries were exhausted and additional Consensus queries returned mostly
  already-seen or out-of-boundary items (primary experiments, single-measure papers). Final corpus: see
  `literature/corpus.jsonl`.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: the seven practices (envisioning, explicating, executing,
  evaluating, encoding, elaborating, expositing), each `yes`/`no`, plus `year` and `cites` copied from
  the corpus.
- Coders: three independent agents, blind to one another, each → `coding/coder{A,B,C}.jsonl`, coding each
  review from its title+abstract only.
- Reliability: `lib/reliability.py` → Fleiss' κ per practice and a majority-vote adjudicated dataset →
  `results/frozen.json`.

## Analysis (evaluate)
- H1: mean practice count per review over the adjudicated dataset, tested against 3.5 (half of seven).
- H2: Pearson r and Spearman ρ between practice count and publication year.
- H3: Spearman ρ between practice count and citation count; publication year reported alongside as the
  pre-registered confound.
- `run.py` writes `results/summary.json` and prints the per-hypothesis verdicts.
