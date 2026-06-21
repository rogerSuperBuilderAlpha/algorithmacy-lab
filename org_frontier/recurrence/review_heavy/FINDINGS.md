# v10 findings — a review-heavy project, and the governance contrast

v9 read PyPhi, a project with a light review culture and a single maintainer at the gate. v10 reads
scikit-learn, where two approving reviews are required before a merge, and sets the same measures
beside PyPhi's. Governance changes the coordination in measurable, lab-relevant ways. Every prediction
held. Reproduce with [`analyze.py`](analyze.py).

## The contrast

| metric | scikit-learn | PyPhi (v9) |
|---|---|---|
| reviews per PR | 3.2 | 0.3 |
| top merger share | 33% | 59% |
| self-merge rate | 7% | 37% |
| distinct authors | 41 | 22 |
| distinct reviewers | 28 | — |
| distinct mergers | 14 | 4 |
| open-to-merge latency, median days | 1 | 0 |

Heavy review makes the reviewer a party. scikit-learn runs 3.2 reviews per pull request against PyPhi's
0.3, and 475 of 478 review events fall between a pull request's open and its merge. The review role,
nearly absent in v9, carries real coordination weight here.

Heavy review spreads the merge gate. The top merger handled 33% of merges, against the 59% one
maintainer held at PyPhi, and the merge right is held by 14 parties rather than 4. No single party is
the veto; a core team shares the gate.

Heavy review ends self-merging. Self-merges fell from PyPhi's 37% to 7%. A required external approval
means someone other than the author commits the merge, so the gate stops being a rubber stamp the
author can apply to their own work.

The labor funnels. Forty-one authors opened pull requests, 28 parties reviewed them, and 14 merged
them. The review labor is spread wide and the merge right is held narrower, two separable roles that at
PyPhi collapsed into one maintainer.

## The elicited gate is deeper, and excludes the author

The four-role model — author, reviewer approval, merger, codebase, under the institutional rule that a
change enters iff opened, approved, and merged — is irreducible, and both the approval gate and the
merge gate sit in the major complex. The required-approval process is a deeper bottleneck than PyPhi's
single-gate triad.

The major complex is the reviewer, the merger, and the codebase, and it leaves the author out. Under
heavy review the irreducible loop runs among the gates and the code they guard, while the author feeds
a pull request in from outside it. The party that proposes the change is not part of the bound core
that decides whether it enters. PyPhi's single-gate model kept the author in the core; the
review-and-merge structure pushes the author to the boundary, which is the structural face of a process
built to judge a contribution independently of who wrote it.

## The predictions, settled

- **H1 — the reviewer is a substantive party.** Confirmed. 3.2 reviews per pull request, ten times
  PyPhi's rate.
- **H2 — the merge gate is distributed.** Confirmed. Top merger 33%, against PyPhi's 59%.
- **H3 — many reviewers, few mergers.** Confirmed. 28 reviewers, 14 mergers, 41 authors.
- **H4 — the elicited gate is deeper.** Confirmed, and sharper than predicted. Both gates are in the
  core, and the core excludes the author.
- **H5 — review precedes merge, slower lifecycle.** Confirmed, modestly. Reviews fall in the lifecycle
  99% of the time; the median latency is one day against PyPhi's zero, a small gap because scikit-learn
  is well resourced and still merges quickly.

## What v10 establishes

The same instrument reads two governance styles and tells them apart. A light review culture holds the
veto with one maintainer who often self-merges; a heavy review culture spreads the merge gate across a
core team, ends self-merging, and binds a two-gate core that judges a change apart from its author. The
lab's veto-player and disintermediation priors describe the light case; the heavy case is a distributed
gate with a deeper core, the kind of structure the multiparty and oversight threads anticipate. The
window is a bounded recent sample of 150 merged pull requests, and the merge metrics include the
project's review bots among the authors, so the next step is a longer span and a third governance style,
a bot-merged project where the merge actor is a machine and the human veto lives entirely in the
approval.
