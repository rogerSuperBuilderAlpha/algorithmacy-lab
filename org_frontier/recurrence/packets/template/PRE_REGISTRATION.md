# Pre-registration template — a recurrence study

Fill this in and commit it before running `run_study.py`, so the git history shows the predictions, the
encoding, and the decision rules were fixed before any result was seen. Each instance's `HYPOTHESES.md`
([v9](../../event_series/HYPOTHESES.md) is a worked example) is this template filled. Delete the guidance in
brackets as you go.

## The arrangement

[Name the coordination, the parties, and the recorded behavior that stands in for each party's state over
time. State what is already known about the data — totals, who the actors are — and what has not yet been
computed. If any data point was seen while building the fetch, say which, since it bounds what the
predictions can claim.]

## The encoding

[State the bit calibration: for each series, when is the party active versus inactive at a time step, and
what alternative encoding the evidence leaves open. Cross-recurrence reads these series directly; Φ
reads the Boolean model below. Name both.]

- Series: [party → recorded behavior → active-when rule]
- Boolean model: [each party's determination rule — who reads whom — and the documented or elicited source
  for it. Mark each rule elicited from evidence versus assumed.]

## Predictions

[Commit each prediction to one instrument. The behavioral predictions are read by cross-recurrence; the
structural ones by Φ. Number them.]

- **H1 — [the behavioral coupling].** [e.g. two parties track each other in sustained episodes, high
  determinism, a consistent peak lag that reads who leads.]
- **H2 — [the structural verdict].** [e.g. the role model is triadic, with party X in the major complex,
  the strict-bottleneck form.]
- **H3 — [the lead-lag / direction].** [e.g. the cross-recurrence profile peaks at a positive lag, party X
  leads party Y by k steps, the observable trace of a directed read edge.]
- **H4 — [the pairing prediction].** [where the two instruments agree, and the one place they are predicted
  to part — the false dyad, the relay, or the back-channel the sweep flags.]

## What would refute each

[For every prediction, the result that overturns it. Cross-recurrence: a flat profile, low determinism, a
peak lag near zero or inconsistent. Φ: a dyadic verdict where a triad was predicted, or a different core.
Nulls and refutations are results, reported as they fall.]

## Decision rules

- The instrument controls must pass before any verdict is read: a decoupled model gives Φ = 0, a fully
  coupled one gives Φ > 0. `run_study.py` checks this first.
- Cross-recurrence prominence, not the raw recurrence rate, separates a real lead-lag from the binary
  recurrence floor; read the peak only when prominence clears the stated threshold.
- Φ is read off the elicited model, not fit to the behavior. A model fit to activity is a labeled first
  pass and weaker than an elicited one, and the writeup says which it is.
