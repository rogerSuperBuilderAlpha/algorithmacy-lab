# v9 — event-level PR and review coordination

v8 ran the recurrence instrument on weekly commit activity and found it too coarse: it recorded
co-presence, not the review-and-merge structure where a maintainer's gatekeeping lives. v9 reads that
structure directly, from PyPhi's pull-request history, where the merge actor is observed.

## The advance over v8

A pull request records who committed the determination: an author opens it, reviewers may review, and
a party with merge rights merges it into the codebase. The merge actor is a recorded fact, so Φ runs
on an elicited institutional model — the merge rule, known from how the platform works — where v8's
model was fit to noisy activity. The empirical question becomes who occupies the gate, and how the gate
behaves over time.

## The pipeline

- [`fetch_events.py`](fetch_events.py) → [`prs.csv`](prs.csv), [`reviews.csv`](reviews.csv) — 104 pull
  requests (author, state, open and merge dates, merge actor) and 33 review events, the frozen
  provenance.
- [`HYPOTHESES.md`](HYPOTHESES.md) — five predictions, committed before the analysis ran.
- [`analyze.py`](analyze.py) — the merge gate, the disintermediation trend, the lifecycle order, and
  the elicited-model Φ.
- [`FINDINGS.md`](FINDINGS.md) — the results.

## The result, in one line

Where v8 was mostly null, v9 confirms its predictions, because the encoding now carries the causal
content. The maintainer is the dominant merge gate, a 59% veto player against 22 authors and 4
mergers; the gate disintermediates over a decade, self-merge rising from 0% to 79%; the open-to-merge
lifecycle is directed but fast; and the elicited merge triad is irreducible at Φ of 2.0, the first
real-coordination Φ from an elicited model. See [FINDINGS.md](FINDINGS.md).
