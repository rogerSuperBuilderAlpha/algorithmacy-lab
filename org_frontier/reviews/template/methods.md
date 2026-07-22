# Methods — <review title>

## Corpus boundary (explicate)
- **Substantive:** <theories / constructs / level of analysis in scope>.
- **Procedural:** <period, fields/subfields, journals, databases; gray literature in or out>.
- A source is included iff <the decidable rule>.

## Search and harvest (execute)
- Seed set: <how the initial seeds were chosen>.
- Snowball: `lib/harvest.py` over `seeds.json` → backward references + forward citers.
- Stopping rule: <e.g. terminate when yield < 5 relevant per 100 references scanned; log the drop>.
- Final corpus: <N> sources (`literature/references.bib`).

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: <list>.
- Coders: <N ≥ 3> independent agents, blind to one another, each → `coding/coder<X>.jsonl`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, Jaccard per set variable,
  majority-vote adjudicated dataset → `results/frozen.json`.

## Analysis (evaluate)
- Content-coding tests: <the cross-tabs each hypothesis needs>.
- Bibliometric tests: `lib/bibliometrics.py` → cluster matrix, spanning counts, mutual density,
  using `clusters.json`.
- Statistics: <report effect size with significance; state minimum detectable effect where a null is
  claimed>.
