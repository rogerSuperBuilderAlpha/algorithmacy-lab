# Q127 — methods

## Model

The Q126 interested-mediator model: the triad W, S, C with W' = S, C' = S, and S' an interested mediator of
the two parties. The mediator holds an agenda a (approve = 1, deny = 0) and at interestedness level k = 0..4
outputs a, regardless of the parties, on the k input states where the parties least warrant a (warrant for
approve is the number of parties on), committing the **faithful baseline** elsewhere. k = 0 is the faithful
mediator; k = 4 ignores the parties.

Q127 varies the faithful baseline, the rule the mediator commits when not imposing its agenda:

| baseline | commits when | output over (00, 01, 10, 11) | minority output-class |
|---|---|---|---|
| AND | both warrant | 0, 0, 0, 1 | 1 (one state) |
| OR | either warrants | 0, 1, 1, 1 | 0 (one state) |
| AGREE (XNOR) | the parties agree | 1, 0, 0, 1 | balanced (2–2) |
| DIFFER (XOR) | the parties differ | 0, 1, 1, 0 | balanced (2–2) |

## Measure

For each baseline and agenda, the run records Φ over {W, S, C} at every interestedness level k and the first
level k* at which the form goes dyadic (Φ_MIP = 0). The fast-collapse agenda is the one with the lower k*.
The minority-output principle predicts the fast agenda is the one whose overrides remove the baseline's
minority output-class. Re-integration is detected when Φ at some k exceeds the faithful (k = 0) value.

Exact IIT-4.0 Φ via the lab's classifier; the control is the AND faithful mediator (the canonical triad,
triadic, Φ = 2.0).

## Reproduce

```
python -m org_frontier.questions.q127_interest_baselines.probe_interest_baselines
```

Output is saved in [`results/output.txt`](results/output.txt). The run is a few seconds (three nodes).
