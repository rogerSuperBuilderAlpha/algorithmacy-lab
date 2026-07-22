# Hypotheses — how gig/platform-work reviews motivate themselves

*Committed before any coding. The question: when a review or agenda-setting article on gig and
platform work justifies its existence, does it spot a gap (an under-studied area, a fragmented or
incomplete literature) or does it problematize (challenge an assumption the field takes for granted,
in the sense of Sandberg & Alvesson 2011)? And does one style of motivation draw more citations?*

The distinction is Sandberg & Alvesson's. Gap-spotting builds a research question by finding
something the literature has not yet covered and offering to cover it. Problematization builds one by
identifying and disputing an assumption underlying existing work. Their claim, and the field's
stylized fact this review tests, is that gap-spotting dominates published reviews and that
problematization is rarer but more generative.

Each hypothesis names the knowledge claim it tests (in the knowledge-weaving typology), its
operationalization, and the outcome that supports versus challenges it.

## H1 — Gap-spotting dominates
- **Knowledge claim (stylized fact):** most gig/platform-work reviews motivate themselves by
  gap-spotting — naming a literature gap, a fragmented field, or an under-studied area — rather than
  by challenging an in-field assumption.
- **Operationalization:** `motivation_mode` coded per source as `gap_spotting`, `problematization`,
  or `neither`. Proportion `gap_spotting` among the coded corpus.
- **Predicts:** `gap_spotting` is a clear majority (well over half); `problematization` a minority.
- **Challenged if:** `problematization` reaches or exceeds `gap_spotting`, or `gap_spotting` is not a
  majority.

## H2 — Problematization rises modestly over time
- **Knowledge claim (enduring critique):** as the field matures, more reviews move from cataloguing
  gaps to contesting assumptions.
- **Operationalization:** share of `problematization` (and of `assumption_targeted = yes`) in an
  earlier vs. a later year split of the corpus.
- **Predicts:** the later period has a modestly higher problematization share than the earlier period.
- **Challenged if:** the problematization share is flat or falls over time.

## H3 — Problematizing reviews are cited more per year
- **Knowledge claim (key assumption):** problematization is the higher-impact move; the field rewards
  assumption-challenging reviews with more attention.
- **Operationalization:** citations-per-year (total citations ÷ years since publication, with the
  current year counted as a fractional minimum) compared between `problematization` and `gap_spotting`
  sources; Mann–Whitney U on the two distributions, plus a comparison of means and medians.
- **Predicts:** problematizing reviews have a higher median citations-per-year than gap-spotting ones.
- **Challenged if:** gap-spotting reviews are cited at least as much per year, or the difference is
  negligible / runs the other way.

## Method fixed in advance
- Corpus boundary and search: `coding_protocol.md` and the corpus build (semantic-connector discovery
  over gig/platform-work review queries; screen out primary studies; keep review / agenda-setting /
  bibliometric-review / meta-analytic articles).
- Coders: three independent agents, blind to one another, on `coding_protocol.md`, coding from
  title + abstract only.
- Reliability reported (Fleiss' κ per categorical variable). Any hypothesis the data contradict is
  reported as challenged. Citation counts are a snapshot and favor older sources unless normalized —
  hence the per-year normalization in H3.
