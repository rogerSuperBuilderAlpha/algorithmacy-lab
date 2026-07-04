# Coding protocol (codebook) — how gig/platform-work reviews motivate themselves

Code each source from its title + abstract. Code what the SOURCE does to justify itself, not what this
review predicts. You are one of several independent coders; do not consult another coder's output. Use
`neither` / `no` where a variable does not apply. When genuinely unsure between two values, pick the
better fit — disagreement is expected and measured.

## The distinction (Sandberg & Alvesson 2011)

- **Gap-spotting** — the article motivates itself by pointing to something the literature has *not yet
  done*: an under-studied topic, a fragmented or scattered body of work needing synthesis, a missing
  framework, an absence of prior reviews, "little is known about X," "the literature is fragmented,"
  "no systematic review has examined Y," "we identify research gaps." Most bibliometric and systematic
  reviews sit here: they map a field and list gaps.
- **Problematization** — the article motivates itself by *challenging an assumption* the field takes
  for granted, and building its contribution on overturning or complicating it: "the dominant view
  that X is inadequate," "scholars wrongly assume," "we question the received distinction between,"
  "contrary to the prevailing framing," "this obscures." The article's move is to unsettle a belief,
  not fill a hole.
- **Neither** — the article is descriptive/summary with no clear gap or assumption-challenge framing
  in title+abstract (e.g. a pure overview or a book-review-style synopsis).

A source can mention both; code the DOMINANT motivating move — the one the contribution is built on.

## Variables (one JSON object per source → your JSONL file)

- **slug** — the source id (copy from the corpus).
- **motivation_mode** — the dominant self-motivation: `gap_spotting` | `problematization` |
  `neither`.
- **assumption_targeted** — does the article explicitly challenge or dispute an in-field assumption,
  received view, or taken-for-granted framing? `yes` (it names and contests an assumption — this
  usually but not always coincides with `motivation_mode = problematization`) | `no`.

Note `year` and `cites` are already in the corpus; do not code them.

## Output

Write JSONL to `coding/coder<yourname>.jsonl`, one line per source:
`{"slug":"tan2020","motivation_mode":"gap_spotting","assumption_targeted":"no"}`

Code every source in the corpus (`literature/corpus.jsonl`). If capacity runs low, code in list order
and report how far you got.

## What the hypotheses predict (do NOT let this bias a call — code the source, not the prediction)

- H1 predicts `gap_spotting` dominates. A review that genuinely challenges an assumption is a real
  datum for `problematization` — record it, even though it is the minority code.
- H3 predicts problematizers are cited more. Do not look at `cites` when coding motivation; code the
  framing blind to impact.
