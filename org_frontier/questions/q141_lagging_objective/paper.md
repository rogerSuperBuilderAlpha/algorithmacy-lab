# Q141 — The lagging objective: slow learning keeps the worker in the coordination

## Question

Q128 found a predatory mediator re-integrates the coordination when its objective adapts to both parties, and
Q129 found that immediate adaptation displaces a party from the core. Q141 asks whether the timescale of
adaptation matters: if the objective learns on a lag, through a memory of the parties' joint state, does the
displaced worker return?

## Method

Two forms. Immediate (Q128): the objective reads the parties directly, O' = W ∧ C. Lagged: a memory M holds the
parties' joint state (M' = W ∧ C) and the objective reads the memory (O' = M), so it tracks the joint
determination with a one-step delay. For each: the verdict, the major complex, whether the worker is in it,
and the Φ. Control: the faithful triad. Full method in [`methods.md`](methods.md); hypotheses in
[`hypotheses.md`](hypotheses.md).

## Results

| objective | structure | Φ | major complex | worker in core |
|---|---|---|---|---|
| immediate | triadic | 1.0 | {S, C, O} | no |
| lagged | triadic | 2.0 | {W, S, C, O, M} | yes |

The immediate objective displaces the worker (core {S, C, O}); the lagged objective binds all five nodes into
one core at double the Φ, the worker among them. Raw output in [`results/output.txt`](results/output.txt).

## Discussion

The displacement Q129 read is a property of immediate adaptation, not of self-interest as such. An objective
that reads the parties' joint state and commits in the same step short-circuits the worker — it computes what
the worker would contribute and feeds the commit itself, so the worker falls out of the irreducible core. A
memory that holds the joint state for a step routes the worker's signal through a delay, keeping it in the
active loop, and the whole coordination — worker, system, counterpart, objective, memory — integrates into one
core at higher Φ than the immediate form reaches.

The reading for algorithmic management is that the speed of the platform's learning decides the worker's place.
A system that adapts to the parties in real time substitutes its model of them for their participation and
pushes them out; a system that learns slowly, carrying a memory rather than reacting instantly, keeps them
constitutive. The same self-executing, self-interested objective is inclusive or displacing depending only on
its timescale, and the slower one is the more inclusive. Where the earlier studies read self-interest as the
thing that displaces, Q141 locates the displacement in immediacy: a platform can pursue its own goal and still
hold the worker in the coordination, provided it does not learn too fast.

## Limitations

The lagged form has five nodes to the immediate form's four; the memory is the lag mechanism, and a same-size
delay construction that isolates timescale from node count is the natural next step. One-step lag only; exact Φ
on five nodes; the Φ-to-economic-value bridge is open (Q122).
