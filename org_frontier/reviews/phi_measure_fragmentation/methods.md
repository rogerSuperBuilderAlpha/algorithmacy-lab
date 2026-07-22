# Methods — measures of integrated information: families and validation

## Corpus boundary (explicate)
- **Substantive:** sources that propose, develop, review, or centrally study a quantitative measure of
  integrated information, integration, complexity, or synergy for a system — exact IIT Φ, a practical
  Φ proxy (Φ*, Φ_AR, geometric Φ_G, whole-minus-parts), causal emergence / effective information,
  integrated information decomposition (ΦID) / partial information decomposition (PID) / synergy, total
  correlation / multi-information, or neural (TSE) complexity. A source is in scope if its central
  object is such a measure — its definition, computation, approximation, comparison, or critique.
  Applications that merely use a fixed off-the-shelf measure without engaging the measure itself are
  out of scope.
- **Procedural:** English-language; indexed by the academic semantic-search connectors (Scholar
  Gateway / Consensus, which draw on Semantic Scholar, PubMed, Scopus, arXiv); 2003–present (Tononi's
  information-integration measure paper was 2004; TSE complexity 1994 is admitted as a root). Preprints
  included (much of this literature is on arXiv/bioRxiv), flagged in the `.bib`.
- A source is included iff its title or abstract presents a measure of integration / complexity /
  synergy as its central object.

## Search and harvest (execute)
- **Seed set:** semantic search over the measure vocabulary — "measures of integrated information",
  "practical approximations to integrated information", "integrated information decomposition synergy",
  "causal emergence measure", "complexity measures of neural integration", "whole-minus-parts
  integration measure", and near variants. The union, deduplicated and screened against the boundary
  rule, is the seed corpus (`literature/corpus.jsonl`).
- **Snowball:** `lib/harvest.py` over `seeds.json` (the screened seeds' DOIs) pulls backward references
  and forward citers, for the H3 citation graph. References are elided by some publishers, so the
  inbound-citer channel carries most of the signal.
- **Stopping rule:** search terms are exhausted when new queries return no new in-boundary sources; the
  screened-out count is logged so coverage is auditable.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `measure_family`, `validation`, `substrate`.
- Coders: three independent agents, blind to one another, each → `coding/coder<X>.jsonl`, coding from
  the title + abstract in `literature/corpus.jsonl`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, majority-vote adjudicated
  dataset → `results/frozen.json`.

## Analysis (evaluate)
- **H1** — the `measure_family` distribution over the adjudicated dataset; count families with ≥ 3
  sources and check no family holds a majority.
- **H2** — the `validation` distribution; the share `ground_truth`.
- **H3** — `lib/bibliometrics.py` cluster matrix over the `measure_family` clusters
  (`clusters.json` assigns each seed its adjudicated family); within-family vs cross-family links.
- Report each hypothesis with its statistic and a supported / qualified / challenged verdict, with the
  reliability figure attached. State limitations: elided references, small clusters, agent coders, a
  connector-bounded corpus.
