# Methods — how gig/platform-work reviews motivate themselves

## Corpus boundary (explicate)
- **Substantive:** review, agenda-setting, systematic-review, bibliometric-review, and meta-analytic
  articles whose subject is gig work, platform work, on-demand labor, crowdwork, digital labor, or the
  algorithmic management of platform workers. A source is in-boundary iff its title/abstract presents a
  synthesis, mapping, typology, or research agenda *about the literature* on gig/platform work. Primary
  empirical studies (single case studies, surveys, ethnographies, interview studies) are out. Pure
  sharing-economy-as-consumption reviews, crowdfunding reviews, and open-innovation crowdsourcing
  reviews are out (adjacent literatures, not gig/platform *work*).
- **Procedural:** English-language; indexed by the semantic-search connectors; 2017-present (the
  gig-economy review literature is post-2015). Preprints and working papers included where the
  connector returned citation counts, flagged in the corpus.
- A source is included iff it clears both gates above and the connector reports a citation count and a
  publication year (both required for H3).

## Search and harvest (execute)
- **Discovery:** the academic semantic-search connectors (Consensus over Semantic Scholar / Scopus /
  PubMed / ArXiv; Scholar Gateway over Wiley) queried with: "gig economy review", "platform work
  literature review", "gig work future research agenda", "on-demand economy platform labor review",
  "gig economy bibliometric analysis", "algorithmic management gig workers systematic review",
  "crowdwork online freelancing sharing economy systematic literature review research agenda".
  Consensus returns citation counts and years directly, which H3 requires; Scholar Gateway was used as
  a review-type cross-check.
- **Screening:** each candidate was screened against the boundary rule. Primary studies, book reviews,
  editorials-without-synthesis, and off-boundary adjacent reviews were dropped. The union of in-boundary
  reviews, deduplicated, is `literature/corpus.jsonl` (N = 49).
- **Stopping rule:** queries were exhausted when new queries returned no new in-boundary reviews with
  citation metadata. The final query (crowdwork/sharing) returned mostly already-seen or off-boundary
  items, so search stopped.
- **Citation snapshot:** citation counts are a single snapshot (July 2026) from the connector. They are
  not corrected for field or database coverage, and they favor older sources; H3 normalizes by
  citations-per-year.

## Coding (encode)
- Codebook: `coding_protocol.md`. Variables: `motivation_mode` (gap_spotting | problematization |
  neither), `assumption_targeted` (yes | no).
- Coders: three independent agents (coderA, coderB, coderC), blind to one another, each coding from the
  title + abstract in `literature/corpus.jsonl`, each writing `coding/coder<X>.jsonl`.
- Reliability: `lib/reliability.py` -> Fleiss' kappa per categorical variable, majority-vote
  adjudicated dataset -> `results/frozen.json`.

## Analysis (evaluate)
- **H1** - the `motivation_mode` distribution on the adjudicated dataset (share `gap_spotting`).
- **H2** - `motivation_mode` and `assumption_targeted` split by an early vs. late year cut.
- **H3** - citations-per-year (cites / years-elapsed, years-elapsed floored at 0.5) compared between
  `problematization` and `gap_spotting` sources: Mann-Whitney U, plus means and medians.
- Report each hypothesis with its statistic and a supported / qualified / challenged verdict, with the
  reliability figure attached. Limitations: agent (not human) coders; motivation coded from
  title+abstract, which compresses the fuller framing an introduction would carry; connector-bounded
  corpus; unresolved DOIs for connector-sourced items; a citation snapshot dominated by a few old,
  highly cited agenda pieces.
