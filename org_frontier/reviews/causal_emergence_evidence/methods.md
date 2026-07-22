# Methods — causal emergence: evidence, formalism, claim direction

## Corpus boundary (explicate)
- **Substantive:** sources whose central concern is causal emergence, downward / top-down causation,
  or macro-scale causation — that is, whether and how a macro-scale (coarse-grained, higher-level)
  description of a system can carry causal power that the micro-scale description does not. Included:
  information-theoretic emergence measures (effective information, integrated information,
  information decomposition), dynamical-systems accounts of emergent macro-variables (dynamical
  independence, computational mechanics, renormalization / coarse-graining), statistical / causal-
  inference treatments of macro causation, and philosophy of the reality of downward causation.
  Excluded: coarse-graining papers with no emergence / causation claim (e.g. molecular-dynamics model
  reduction for computational speed), and pure consciousness-IIT papers that do not raise the
  macro-vs-micro causation question.
- **Procedural:** English-language; indexed by the academic search backends used (Scholar Gateway /
  Semantic Scholar, Consensus); no date floor (Hoel's founding paper is 2013, but the downward-
  causation debate predates it). Preprints included (arXiv is a primary venue for this literature),
  flagged where identifiable.
- A source is included iff its title or abstract makes or evaluates a claim about macro-scale
  causation, causal emergence, or the reality of downward / top-down causation.

## Search and harvest (execute)
- **Seed set:** academic search via ToolSearch-loaded backends
  (`mcp__claude_ai_Scholar_Gateway__semanticSearch`, `mcp__claude_ai_Consensus__search`) over queries
  spanning the subtopics: "causal emergence information theory", "downward causation formal measure",
  "macro causation coarse graining", "emergence effective information", "causal emergence critique /
  deflation", "dynamical independence / computational mechanics", "integrated information
  decomposition". The union, deduplicated and screened against the boundary rule, is the corpus
  (`literature/corpus.jsonl`). The Scholar Gateway backend returned many tangential hits (systems
  medicine, molecular-dynamics coarse-graining); these were screened out by the substantive rule.
- **Snowball:** `lib/harvest.py` over `seeds.json` pulls backward references and forward citers for the
  H3 citation graph. Seeds resolve by DOI where available and by title otherwise. References are
  elided by some publishers, so the inbound-citer channel carries most of the signal.
- **Stopping rule:** search terms are exhausted when new queries return no new in-boundary sources.
  Screened-out tangential hits are not carried, so coverage stays auditable.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `evidence`, `formalism`, `claim_direction`.
- Coders: three independent agents, blind to one another, each → `coding/coder<X>.jsonl`, coding from
  the title + abstract in `literature/corpus.jsonl`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, majority-vote adjudicated
  dataset → `results/frozen.json`.

## Analysis (evaluate)
- **H1** — the `evidence` distribution on the adjudicated dataset (share `empirical` vs
  `conceptual` + `formal_model`).
- **H2** — the `claim_direction` distribution: among sources taking a side (`emergence_real` or
  `deflationary`), whether both hold a substantial share (contested) or one dominates (converged).
- **H3** — the `formalism` distribution (fragmentation of shares) and, from `lib/bibliometrics.py`
  over `clusters.json` (slug → formalism), the formalism-to-formalism citation matrix. If the harvest
  is rate-limited or resolves too few edges, H3 is reported from the coded distribution and the
  matrix half is marked partial.
- Report each hypothesis with its statistic and a supported / qualified / challenged verdict, with the
  reliability figure attached. State limitations: elided references, agent coders, a search-backend-
  bounded corpus, small per-cell counts.
