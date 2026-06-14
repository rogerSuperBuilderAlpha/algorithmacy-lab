# Q108 — Stage 3 hypotheses (fixed before computation)

Four hypotheses on controllability — which party, varied alone, steers the verdict. Starting from the
read-recipient triad, each party's function is swept while the others stay fixed, and the triadic settings
are counted. A party is a control node if both verdicts are reachable from its sweep. Written and committed
before the run; the instrument was validated on the three sweeps. The predictions follow from the law: the
mediator has a richer function space than the parties, and liveness (Finding 3) requires each party's exact
live read.

## H1 — The mediator is a control node

- **Claim:** Varying the mediator's function reaches both verdicts.
- **H0:** It fixes the verdict.
- **Predicted outcome:** both reachable. H0 refuted.

## H2 — Each outer party is a control node

- **Claim:** Varying the worker's read, and varying the counterpart's read, each reach both verdicts.
- **H0:** Some outer party fixes the verdict.
- **Predicted outcome:** both reachable from each. H0 refuted.

## H3 — The mediator is the dominant control node

- **Claim:** The mediator has more triadic-reachable settings than either outer party.
- **H0:** An outer party has at least as many.
- **Predicted outcome:** the mediator has the most. H0 refuted. The hub is the richest place to steer the
  verdict toward a triad.

## H4 — The outer parties are knife-edge

- **Claim:** Exactly one of each outer party's settings is triadic — only its live identity read preserves
  the triad.
- **H0:** An outer party has more than one triadic setting.
- **Predicted outcome:** exactly one. H0 refuted. A party controls the verdict but cannot robustly maintain
  the triad: any read but the live one breaks it, which is Finding 3 read as a control statement.
