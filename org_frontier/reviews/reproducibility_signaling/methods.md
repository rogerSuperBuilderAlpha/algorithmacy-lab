# Methods — reproducibility signaling in management research

## Corpus boundary (explicate)
- **Substantive:** empirical papers in management and organization research — organizational
  behavior, human resource management, strategy, entrepreneurship, corporate governance, operations,
  and adjacent management subfields — that report primary or archival data analysis. Pure conceptual
  pieces, editorials, and stand-alone literature reviews are out of scope (a title-cue screen drops
  reviews, agendas, editorials, and framework papers); a source that shows no empirical data in its
  abstract can still be coded `conceptual` if it slips the screen.
- **Procedural:** English-language; indexed in the Scholar Gateway academic corpus (Wiley-hosted
  semantic search, last corpus update May 2026); published 2015–2025. Retracted records dropped.
- A source is included iff it carries a title and an abstract of at least 120 characters, is not a
  review/editorial by the title screen, and falls in 2015–2025.

## Search and harvest (execute)
- **Search:** twelve semantic-search queries over the Scholar Gateway connector, crossed across
  subfields (OB, HR, strategy, entrepreneurship, leadership, governance, operations, marketing,
  qualitative organizational research) and open-science topics (data sharing, pre-registration,
  registered reports), each windowed to a slice of 2015–2025 so the corpus spreads across the decade
  rather than piling into recent years. Each query returned up to 20 passages.
- **De-duplication and screen:** `build_corpus.py` merges the raw payloads, dedupes by DOI then by
  normalized title, applies the boundary screen, and caps the corpus at 8 sources per publication
  year (2015–2025) to hold an even year spread for the H2 trend test. The result is 88 sources, 8 per
  year. The cap is the stopping rule: within each year, sources are taken in title order until the
  cap is met.
- **No citation snowball.** H1–H3 are content-coding hypotheses on the papers themselves, not
  citation-structure hypotheses, so the bibliometric channel is not used here.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `open_data`, `code_available`, `preregistered`
  (each `yes`/`no`), `method_type` (quantitative | qualitative | mixed | conceptual), `year`.
- Coders: three independent agents, blind to one another, each → `coding/coder<X>.jsonl`, coding from
  the title + abstract in `literature/corpus.jsonl`. The signaling variables use a literal rule:
  `yes` only when the text states or plainly implies the practice; silence is `no`.
- Reliability: `lib/reliability.py` → Fleiss' κ per categorical variable, majority-vote adjudicated
  dataset → `results/frozen.json`.

## Analysis (evaluate)
- **H1** — the any-signal rate (share coded `yes` on at least one of the three signaling variables)
  on the adjudicated dataset; predicted a minority.
- **H2** — the any-signal rate by year period (2015–2019 vs 2020–2025) and by single year, joined to
  the authoritative corpus year; predicted rising.
- **H3** — the any-signal rate for `method_type=quantitative` versus `qualitative`; predicted
  quantitative higher.
- Report each hypothesis with its statistic and a supported / qualified / challenged verdict.

## Load-bearing limitation
Coding is from the abstract, not the full text. Many journals place data-availability and
open-materials statements in a back-matter section that never appears in the abstract. Abstract-only
coding therefore undercounts real practice: every rate reported here is a **lower bound** on what a
full-text audit would find. The direction of the H2 and H3 comparisons is more robust than the
levels, since the undercount applies to every period and method.

## Reproduce
```bash
# from the repo root
python3 -m org_frontier.reviews.reproducibility_signaling.build_corpus \
    org_frontier/reviews/reproducibility_signaling/.raw_search
python3 -m org_frontier.reviews.lib.reliability \
    org_frontier/reviews/reproducibility_signaling/coding \
    --categorical open_data,code_available,preregistered,method_type \
    --out org_frontier/reviews/reproducibility_signaling/results/frozen.json
python3 -m org_frontier.reviews.reproducibility_signaling.run
```
