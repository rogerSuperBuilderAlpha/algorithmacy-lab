# v10, pre-registered hypotheses — a review-heavy project, and the governance contrast

Committed before the analysis runs. The series is a bounded recent window of scikit-learn's
pull-request and review history (`prs.csv`, `reviews.csv`), a project with a heavy review process. The
totals are known — 150 merged pull requests and 478 review events, so review intensity is high by
construction of the selection — but no merge-actor distribution, reviewer-set size, lifecycle timing,
or Φ has been computed. v9's PyPhi numbers are on the record and serve as the light-review comparison.

## The contrast

v9 read PyPhi: a light review culture, 0.3 reviews per pull request, a single maintainer who merged the
59% majority. v10 reads scikit-learn, where two approving reviews are required before a merge and the
core team reviews and merges each other's work. The same instrument on the two projects asks how
governance changes the coordination: whether the merge gate stays a single veto or spreads across a
team, whether the reviewer becomes a party in its own right, and whether a required-approval process is
a deeper bottleneck than a single maintainer's merge.

## Predictions

- **H1 — the reviewer is a substantive party.** scikit-learn's reviews per merged pull request far
  exceed PyPhi's 0.3, by an order of magnitude, so the review role carries real coordination weight here
  where it was nearly absent in v9.
- **H2 — the merge gate is distributed.** No single party merged a majority, and the top merger's share
  is well below PyPhi's 59%. Heavy review spreads the merge right across a core team rather than holding
  it with one maintainer.
- **H3 — many reviewers, few mergers.** The set of distinct reviewers is large and well exceeds the set
  of distinct mergers: the review labor is spread wide while the merge right is held by a core team, two
  separable roles.
- **H4 — the elicited gate is deeper.** A four-role model — author, reviewer approval, merger, codebase
  — under the institutional rule that a change enters iff opened, approved, and merged, is irreducible,
  with both the approval and the merge gate in the major complex. The required-approval process is a
  deeper bottleneck than PyPhi's single-gate triad.
- **H5 — review precedes merge, and the lifecycle is slower.** Reviews fall before the merge, the
  approval gate ahead of the merge gate, and the open-to-merge latency is longer than PyPhi's same-day
  median, because heavy review takes time.

## What would refute each

H1 fails if review intensity is near PyPhi's. H2 fails if one party merged a majority. H3 fails if
reviewers are as few as mergers. H4 fails if the four-role model is reducible, or if only one gate sits
in the core. H5 fails if reviews fall outside the open-to-merge span, or if the latency is no longer
than PyPhi's. Nulls and refutations are results, reported as they fall.
