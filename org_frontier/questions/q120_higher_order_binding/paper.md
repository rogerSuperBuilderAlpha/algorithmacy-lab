# Q120 — No pure higher-order bind: every party in a triadic form is pivotal

## Question

The lab's structural law says a coordination form demands algorithmacy when every party is bound into one
irreducible joint determination, and that substitutability of any party collapses it. Read literally, that
makes every party pivotal. A weaker arrangement is conceivable: a form irreducible as a trio but held
together purely at the higher order, where the binding lives in the three-way interaction and no single
party is individually necessary. Removing any one such party would leave the other two still triadically
bound. Q120 asks whether this pure higher-order bind exists.

The question matters because a pure higher-order bind would be a coordination irreducibility that no
single-party intervention reaches. A platform could not be disintermediated by removing one actor; a
worker's exit would not factor the arrangement. Whether the construct admits this shape sharpens what
"irreducible joint determination" means.

## Method

A party P is pivotal in a triadic form when knocking it out flips the whole-system verdict from triadic to
dyadic. Knockout replaces P's update rule with a non-interpreting pass-through: P stops reading the others,
while the others still read P. Two definitions are run so the result does not depend on one — spectator
(P' = x[P], P freezes at its current value) and silenced (P' = 0, P forced to a constant). A pure
higher-order bind is a triadic form with zero pivotal parties.

Two families of three-party Boolean forms are swept. Strict mediation (256 forms: W' = f(S), S' = f(W, C),
C' = f(S)) makes the mediator S the only path between W and C, so S is a cut vertex. Fully coupled (4096
forms: each party reads the other two) has no cut vertex, so redundancy across the direct edges could
carry a bind no single party holds. The verdict is exact IIT-4.0 Φ over the minimum-information partition,
validated on the canonical strict triad (triadic, Φ_MIP = 2.0, all three parties pivotal). Full method in
[`methods.md`](methods.md); hypotheses fixed before computing in [`hypotheses.md`](hypotheses.md).

## Results

No pure higher-order bind exists in either family, under either knockout definition. The result is sharper
than the hypothesis: every triadic form has all three parties pivotal, not merely one.

| family | forms | triadic | pivot count = 3 | pure higher-order |
|---|---|---|---|---|
| strict mediation | 256 | 24 | 24 | 0 |
| fully coupled | 4096 | 2288 | 2288 | 0 |

The fully-coupled family carries the weight. With the mediator no longer a cut vertex, a triadic bind
could in principle have survived the loss of any one party through the remaining direct edges. Across all
2,288 triadic forms it never does. The 24 triadic strict-mediation forms reproduce the known 9.4% triadic
rate for that family, a check on the sweep. Raw output for both families is in
[`results/full_output.txt`](results/full_output.txt).

## Interpretation

Triadic coordination among three parties is an all-or-nothing property of the trio. A form is triadic
exactly when each of its three parties is individually necessary to it; drop any one and the irreducible
bind factors. This tightens the standing law from one direction of implication ("substitutability of any
party collapses it") to a biconditional on the three-party domain: a form is triadic if and only if all
three parties are pivotal.

The finding closes a way the construct could have been soft. There is no three-party arrangement whose
irreducibility hides from every single-party test, so the disintermediation reading holds without
exception here: a triadic coordination always has a party whose removal collapses it, and in fact every
party is such a lever. The veto-player and substitutability results that the lab reads on specific forms
are not special cases; they are universal on this domain.

## Limitations

The result is exact but in-silico: evidence about the instrument and the law on small Boolean models, not
about a real organization. The knockout is a structural intervention on the update rules, the
model-relative reading of substitutability. The two families are large but fix which parties each rule may
read, so they do not exhaust all three-party wirings. Most important, the claim is for three parties. At
four or more, genuine redundancy becomes possible — two parties jointly standing in for a third — and a
pure higher-order bind could appear there. That is the natural next question, and it is runnable on the
same instrument up to the exact-Φ size ceiling.
