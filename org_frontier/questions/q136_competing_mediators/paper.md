# Q136 — Two competing mediators: competition destroys the coordination or stacks another toll

## Question

A single faithful mediator captures two-thirds of the coordination's value (Q111), and the market remedy for
a monopolist's cut is competition. Q136 asks what a second mediator does to the integrated value and its
distribution. Two regimes: substitutes, where the parties can route through either mediator, and complements,
where both are required.

## Method

Four nodes — worker W, mediators S1 and S2, counterpart C — each mediator committing the joint determination
Si' = W ∧ C. Substitutes: the parties read S1 ∨ S2. Complements: the parties read S1 ∧ S2. For each form the
whole-system verdict, the major complex, the total Φ, and the Shapley value of subsystem Φ at the integrating
state. Control: the single faithful mediator. Full method in [`methods.md`](methods.md); hypotheses in
[`hypotheses.md`](hypotheses.md).

## Results

| form | total Φ | each mediator | parties (collective) |
|---|---|---|---|
| substitutes (read either) | 0.0 (dyadic) | — | — |
| complements (read both) | 4.0 | 25% | 50% |

Substitutable mediators factor the coordination: the whole system is dyadic, and the major complex collapses
to a degenerate two-node fragment (Φ ≈ 0.19) — no triad survives. Complementary mediators raise the value to
4.0 and split it equally, each of the four taking a quarter. Raw output in
[`results/output.txt`](results/output.txt).

## Discussion

Competition does not return the mediator's cut to the parties. The substitutes regime is the disintermediation
case — either mediator will do, so neither is necessary — and the structural consequence is not a cheaper
coordination but no coordination: the irreducible bind dissolves and the integrated value goes to zero. There
is nothing to redistribute. The complements regime adds a second mediator in series, both required, and this
raises the total value and distributes it evenly: each mediator's rent falls from two-thirds to a quarter and
each party's share rises from a sixth to a quarter, but the parties hold a larger slice of a larger pie, not a
larger slice of the same one, and they now pass through two bottlenecks rather than one.

The political economy is therefore not the textbook one. The platform's two-thirds is not competed down to a
smaller cut of the same coordination. The structural alternatives are to destroy the coordination's
integrated value by making the platform replaceable, or to add another indispensable platform and split a
larger value evenly. Returning the rent to the parties is not among the options the structure offers.

## Limitations

Exact Φ on a four-node model; the two mediators are identical conjunctive committers, and differentiated
mediators (each reading a different party, or computing different functions) are the natural next case. Value
read at the integrating state; the Φ-to-economic-value bridge is open (Q122).
