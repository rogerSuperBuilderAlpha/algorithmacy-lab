# v8 findings — the recurrence instrument on a real recorded series

The behavioral instrument ran on a series the lab did not generate: the PyPhi commit history, encoded
into weekly contributor activity. That milestone is the point of v8. The coordination predictions made
in [HYPOTHESES.md](HYPOTHESES.md) mostly did not hold, and the reason they did not is the finding.
Reproduce with [`analyze.py`](analyze.py).

## What the instrument found

Across both eras, no pair of contributors shows a prominent directed lead-lag. Every diagonal profile
is flat, prominence at or below 0.04, so coupling centrality is near zero for every party including the
maintainer. The recurrence rate and determinism look high (DET 0.83 to 0.97), but the co-active share
shows why: most recurrence is shared inactivity, two contributors both quiet in the same week. The
longest diagonal in the recent era, 98 weeks for dviggiano and ajbailey4, is a 98-week stretch in which
both were inactive, co-active share 0.01. The one pair with substantial genuine co-activity is the
maintainer and the major co-developer, wmayner and rlmv, at a co-active share of 0.33.

The fitted model agrees. A Boolean model fit to the three core-era series predicts 81% of weekly
transitions, and its exact Φ is zero: the contributors, as the weekly activity models them, do not form
an irreducible whole. The major complex collapses to a single node.

## The predictions, settled

- **H1 — the maintainer is the behavioral hub.** Refuted. wmayner is not a distinguishable hub; no
  party has prominent directed coupling, so coupling centrality is near zero for all.
- **H2 — the core dyad couples and sustains.** Refuted as stated, recovered in part. By the raw measure
  the longest diagonal is a co-inactivity artifact between two peripheral contributors. Once recurrence
  is restricted to co-active weeks, wmayner–rlmv is the only pair with real shared activity, the core
  dyad the prediction named.
- **H3 — coordination is synchronous, not led.** Null. Neither holds: no pair shows a prominent peak at
  any lag, synchronous or directed.
- **H4 — the core era is irreducible when modeled.** Refuted. The fitted model is reducible, whole-system
  Φ of zero.
- **H5 — peripheral contributors are near-spectators.** Trivially consistent and uninformative. The
  peripheral contributors score low, but so does everyone, because no directed coupling is present.

## Why the predictions failed, and what it points to

The instrument works. The encoding is too coarse to carry the coordination's causal structure. Weekly
at-least-one-commit activity records when a contributor was present, and presence clusters at the
project level: everyone busy near a release, everyone quiet between. That co-presence, and even more the
co-absence, fills the recurrence plot and leaves no room for a pairwise lead-lag to show. The
maintainer's actual coordinating power lives elsewhere, in the review-and-merge graph, where a
contributor opens a pull request and the maintainer commits the
decision that the change enters the codebase. That is the worker-system-counterpart structure the lab
models, and the commit-week encoding throws it away.

So v8 closes its milestone and opens its real question. The behavioral instrument runs on real data,
the lab's synthetic-data intuitions do not transfer to a coarse activity encoding, and the co-active
correction isolates exactly the one true working pair, which says the instrument is sound and the
encoding is the gap. The next series is event-level: pull requests, reviews, merges, CI runs, with the
parties' states read from the review graph. That is where the maintainer's veto would appear, where Φ
would have an elicited model instead of a fitted one, and where the structural and behavioral readings
could finally meet on real organizational coordination.

## Status

The behavioral instrument has run on real data: the v8 milestone. The structural instrument ran only on
a model fit to the activity, and returned reducible, so the real-data Φ verdict still awaits an elicited
model from event-level data. The validation gap is now concrete and located.
