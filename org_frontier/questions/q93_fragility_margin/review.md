# Q93 — Stage 1 review: a fragility metric for the binary verdict

## The question

The verdict is binary at Φ_MIP = 0. Nothing in the corpus measures how close a triadic form sits to the
dyadic boundary, even though the classifier's minimal test cases show a single edge or read can toggle the
verdict. A margin-to-dyadic metric would turn the binary verdict into a gradient, and the natural test is
whether that cheap structural quantity predicts the noise robustness Q71 measured.

## What the lab already knows that bears on this

- **A single edge or read toggles the verdict (Finding 1, `classifier/`).** The verdict is structurally
  fragile; this study quantifies the fragility.
- **Parity determinations support irreducibility most readily (Finding 4).** XOR and XNOR yield triadic
  forms twice as often as monotone functions. Whether they also yield the more robust triads is open.
- **The outreach verdict degrades gracefully under noise (Q71).** Φ falls smoothly rather than snapping to
  zero. This is the dynamical robustness the structural margin is tested against.

## The gap

No metric in the corpus measures the distance from a triadic form to the dyadic boundary, and the relation
between structural distance and dynamical noise survival is uncomputed. Whether the two notions of
robustness agree is the open question.
