# v9, pre-registered hypotheses — event-level PR and review coordination

Committed before the analysis runs. The series is the PyPhi pull-request and review history
(`prs.csv`, `reviews.csv`), the review-and-merge structure v8 pointed to. The totals are known — 104
pull requests, 33 review events — but no merge-actor distribution, latency, or Φ result has been
computed. Two early data points were seen while building the fetch (one early PR merged by the
maintainer, one later PR self-merged), which set the temporal-shift prediction below; the aggregates
are not yet seen.

## The arrangement, and what v9 adds

A pull request is a coordination event with a recorded structure: an author opens it, reviewers may
review, and someone with merge rights commits the decision that the change enters the codebase. The
merge actor is observed, so who commits the determination is a recorded fact. This is the advance over
v8. Φ runs here on an elicited model, the institutional merge rule that a change enters iff a PR is
opened and a party with merge rights merges it, where v8's model was fit to noisy activity. The
empirical question is who occupies the gate, and whether one party holds it.

## Predictions

- **H1 — the maintainer is the merge gate.** wmayner merged a majority of the merged pull requests, the
  empirical [veto player](../../threads/veto_player/THREAD.md): the party most changes pass through to
  enter the codebase.
- **H2 — the merge process is a constitutive triad.** The role triad — author, merge gate, codebase —
  under the institutional merge rule is triadic, the gate in the major complex, the strict-bottleneck
  form. This is the first real-coordination Φ from an elicited model, not a fitted one.
- **H3 — the lifecycle is directed.** A pull request's events run open then merge, a positive latency
  from creation to merge, with review between the two where reviews exist. The author leads, the gate
  commits.
- **H4 — the gate disintermediates over time.** Early pull requests route through the maintainer; later
  ones are increasingly self-merged as contributors gain merge rights. The maintainer's veto moves
  upstream, to granting access, and the merge-time gate loosens, the
  [disintermediation](../../threads/disintermediation/THREAD.md) prior.
- **H5 — few gates, many authors.** The merge right is concentrated: a small number of parties account
  for the merges while authorship is spread across more contributors, so the gate is non-substitutable
  even where it is exercised by self-merge.

## What would refute each

H1 fails if self-merging dominates and no single party merged a majority. H2 fails if the elicited
triad is dyadic. H3 fails if the open-to-merge order does not hold or the latency is zero. H4 fails if
the merge actor stays the maintainer throughout, or if self-merging is constant from the start. H5
fails if mergers are as spread as authors. Nulls and refutations are results here, reported as they
fall.
