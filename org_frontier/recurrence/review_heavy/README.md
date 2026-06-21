# v10 — a review-heavy project, and the governance contrast

v9 read PyPhi, a project with a light review culture and a single maintainer at the gate. v10 runs the
same event-level analysis on scikit-learn, where two approving reviews are required before a merge, and
sets the measures beside PyPhi's. The question is how governance changes the coordination.

## The series

A bounded recent window of scikit-learn's pull-request and review history: 150 merged pull requests and
478 review events. The window is stated, not silent, because scikit-learn has tens of thousands of pull
requests and a sample keeps the scale comparable to PyPhi's full history.

## The pipeline

- [`fetch_events.py`](fetch_events.py) → [`prs.csv`](prs.csv), [`reviews.csv`](reviews.csv) — the frozen
  provenance.
- [`HYPOTHESES.md`](HYPOTHESES.md) — five predictions, committed before the analysis ran.
- [`analyze.py`](analyze.py) — the governance contrast, the lifecycle, and the four-role elicited Φ.
- [`FINDINGS.md`](FINDINGS.md) — the results.

## The result, in one line

Governance changes the coordination, and the same instrument tells the two styles apart. Heavy review
makes the reviewer a party (3.2 reviews per PR against 0.3), spreads the merge gate across a core team
(top merger 33% against 59%), ends self-merging (7% against 37%), and binds a deeper two-gate core that
excludes the author. See [FINDINGS.md](FINDINGS.md).
