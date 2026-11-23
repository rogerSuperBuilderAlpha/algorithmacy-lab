# Three-party commits bind when every party is pivotal at a consensus, once PyPhi's ties are counted

The pre-registered rule misses 10 of 256 rules under PyPhi's default tie-breaking, but those misses, and
14 more rules, turn out to depend on an arbitrary choice among tied states; scored over all tied choices,
the rule is exact. Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), max over reachable states. Hypotheses pushed in
`3137165f` before computation. Controls passed: AND3 Φ = 3.0, MAJ3 Φ = 0 (the Q215 values).

## Setup

Four nodes: parties P1, P2, P3 each copy S; S' = h(P1, P2, P3) for all 256 Boolean h. Every reachable
state has P1 = P2 = P3 (a consensus). Rule R (fixed in advance): triadic iff at some consensus value
every party is pivotal (flipping it alone changes h). R picks 60 rules.

## Results

| measure | value |
|---|---:|
| triadic under default tie-breaking | 50 / 256 |
| rule R's picks | 60 |
| mismatches, default tie-breaking | 10 (all predicted triadic, found Φ = 0) |
| forms whose verdict depends on the tie choice (post hoc) | 24 |
| triadic under at least one tie choice (post hoc) | 60, identical to R's picks |
| triadic under every tie choice (post hoc) | 36 |
| forms whose verdict differs from their twin with all 0/1 values renamed | 20 |

Distinct triadic Φ (default tie-breaking): 0.25 (10 rules), 0.471679 (22), 0.5 (12), 1.0 (2), 3.0 (4).
The 24 tie-dependent rules range between 0 and 0.25 or between 0 and 0.471679 depending on the tie choice.
All 24 are pivotal at exactly one of the two consensus values.

Symmetric rules (output by number of parties on, 0–3):

| profile | rule | Φ |
|---|---|---:|
| 0001, 0111, 1000, 1110 | AND3, OR3, NOR3, NAND3 | 3.0 |
| 0110, 1001 | not-all-equal, all-equal | 1.0 |
| 0100, 0010, 1101, 1011 | exactly one, exactly two, and their negations | 0.471679 |
| 0101, 1010 | three-way parity and its negation | 0.25 |
| 0011, 1100 | majority, minority | 0 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED as pre-registered.** Under default tie-breaking 50 rules bind, not 60; the 10 misses are
  rules R calls triadic that read Φ = 0 (e.g. h = P1 ⊕ (P2 ∧ P3), mask 106).
- **H2 SUPPORTED.** Of the 14 non-constant symmetric rules, 12 bind and exactly majority and minority factor.
- **H3 REFUTED.** Triadic Φ takes five values, not two.

Post hoc (not pre-registered). PyPhi's `system_intrinsic_information` notes "State ties are arbitrarily
broken (for now)." For mask 106 at state (1,1,1,1), four cause states tie at intrinsic information 0.5, and
PyPhi takes the first. Its 0/1-renamed twin (mask 169) has the mirror-image tie but takes a cause state
that is not the mirror of 106's choice, so one reads 0 and the other 0.25. Evaluating Φ under every tied
(cause, effect) pair, 24 forms change verdict with the choice. Counting a form as triadic when any tied
choice binds, R matches all 256.

## What it means

The two-party symmetry rule generalises to three parties as a pivotality rule: the coordinator binds the
three only if there is a moment of agreement at which each one of them could, alone, change the decision.
Majority fails because at unanimity no single defector changes a majority. AND, OR, the "exactly one" rules
and parity pass. That links the lab's membership account (pivotality) to the verdict directly.

The tie result is a caution for the instrument. For about one rule in ten here, the yes/no verdict depends
on an arbitrary choice PyPhi makes between equally good cause or effect states, and swapping every 0 and
1, which should change nothing, changes the verdict for 20 rules. Verdicts on forms like these should
report the tie range, not one number.

## Limits

Four nodes, all parties copying S, deterministic rules. The tie audit enumerates tied cause and effect
states of the whole system only, not ties inside the partition search. Rule R is a description that fits;
we have not derived it from the IIT 4.0 definitions.

## Reproduce

```sh
python org_frontier/studies/consensus_pivotality/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/consensus_pivotality/run.py --write   # full run, ~1.7 min
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
