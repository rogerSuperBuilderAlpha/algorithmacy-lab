# The veto factors because it treats aligned parties unequally, not because they move in lockstep

One rule, fixed before the run, sorts all 256 strict-mediation forms with zero misses: a form binds iff
both parties track the mediator and the commit is symmetric in the two parties once their alignment is
accounted for. Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), max over reachable states. Hypotheses pushed in
`0cd10cc3` before computation. Controls passed: atlas D1 veto Φ = 0, AND hub Φ = 2.0, census 24/256 triadic.

## Setup

Family: W' = f(S), C' = g(S), S' = h(W, C), every one- and two-input Boolean function (4 × 16 × 4 = 256).
When f and g both track S (copy or negate), every reachable state has C = W (same reading, "lockstep") or
C = ¬W (opposite readings, "anti-lockstep"). The aligned commit is h*(a, b) = h(a, b) for the same reading
and h(a, ¬b) for opposite readings. Rule: triadic iff both reads track S and h* is symmetric and depends
on both inputs (AND, OR, NAND, NOR, XOR, XNOR after alignment).

| | forms | triadic | dyadic |
|---|---:|---:|---:|
| lockstep (W = C in every reachable state) | 64 | 12 | 52 |
| anti-lockstep (W = ¬C in every reachable state) | 64 | 12 | 52 |
| all 256 forms | 256 | 24 (rule predicts the same 24) | 232 |

Triadic values: 2.0 for the AND/OR family
after alignment (16 forms), 0.5 for parity (8 forms).

The atlas's suggested test, breaking the W = C symmetry by giving the counterpart the opposite reading:

| form | Φ |
|---|---:|
| veto, both copy S (atlas D1) | 0 |
| veto, counterpart reads ¬S | 2.0 |
| AND hub, both copy S | 2.0 |
| AND hub, counterpart reads ¬S | 0 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Lockstep is not sufficient to factor: 12 of the 64 lockstep forms bind, including the
  AND, OR, NAND, NOR, XOR and XNOR hubs with both parties copying S.
- **H2 SUPPORTED.** The alignment-symmetry rule classifies all 256 forms correctly (0 mismatches).
- **H3 SUPPORTED.** With the counterpart reading ¬S, the veto binds (Φ = 2.0) and the AND hub factors (Φ = 0).
- **H4 SUPPORTED.** The 256 forms fall into 38 classes under renaming a node's two values; max Φ and the
  verdict agree within every class (0 disagreements).

## What it means

The atlas's account of the veto ("the veto drives the two parties into lockstep") is not right as stated:
the AND hub has the same lockstep and binds. What decides the verdict in this family is whether the
mediator treats the two parties as interchangeable given how they are aligned. When both parties carry
the same information and the rule weighs them unequally (W ∧ ¬C on two equal inputs), the second party
adds nothing the first did not, and the form splits. When the rule weighs them equally, both stay
necessary. Valence matters only through alignment: negating one party's reading of the mediator flips
which commits bind. This sharpens the atlas's second condition ("live values, not frozen ones"): the
parties' values are live in the veto too; what fails is the symmetry of the commit over them.

## Limits

Three-node strict mediation, deterministic Boolean rules, whole-system Φ. The rule is stated for this
family; forms with direct party-to-party edges, memory or noise are untested. Why symmetry is the
deciding property is observed here, not derived from the IIT 4.0 partition algebra.

## Reproduce

```sh
python org_frontier/studies/lockstep_symmetry/run.py --quick   # CI subset, ~2 s
python org_frontier/studies/lockstep_symmetry/run.py --write   # full run, ~5 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
