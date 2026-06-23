# Q125 — No pure higher-order bind at four parties: redundancy keeps every party pivotal

## Question

Q120 showed that among three parties no pure higher-order bind exists: every irreducible coordination form
has all three parties pivotal, so removing any one collapses it. That result was argued to be specific to
three parties, for a concrete reason. With four parties, redundancy becomes possible — two parties can
jointly stand in for a third — so a form might remain irreducible after the knockout of any single party,
the binding carried by the group with no individual lynchpin. Q125 asks whether this pure higher-order bind
appears at four parties.

The stakes are the same as Q120, one party wider. A pure higher-order bind would be a coordination
irreducibility that no single-party intervention reaches: a platform that no one actor can disintermediate,
a worker whose exit does not factor the arrangement. Whether four-party redundancy creates this shape bears
on how robust the substitutability reading of the construct is.

## Method

A four-party form is irreducible when its whole-system Φ over the minimum-information partition exceeds
PHI_EPS in some reachable state. Knockout of party P replaces its rule with a non-interpreting pass-through,
under two definitions — spectator (P' = x[P]) and silenced (P' = 0). P is pivotal when its knockout makes
the form reducible; a pure higher-order bind has zero pivotal parties under both. The control is the
canonical three-party triad (irreducible, Φ_MIP = 2.0, all three parties pivotal), reproducing Q120.

Exact Φ on four nodes costs about a second per form, so the full 16^4 = 65536 four-party symmetric family
cannot be swept. The search is aimed where a no-pivot bind is most likely — the symmetric forms, where
interchangeability is greatest, plus hand-built redundant constructions. A non-symmetric rule breaks
interchangeability and makes a no-pivot bind less likely, so these forms are the right place to look. Four
families: the 16 homogeneous symmetric forms (every node reads the other three through the same symmetric
function), the 256 canonical heterogeneous forms (each node uses one of OR/majority/AND/parity), curated
redundant constructions (twin parties, rings, cliques), and the lab's named four-party forms. Full method
in [`methods.md`](methods.md); hypotheses fixed before computing in [`hypotheses.md`](hypotheses.md).

## Results

No pure higher-order bind exists among the forms tested, under either knockout definition. Across 267
irreducible four-party forms, every one has all four parties pivotal.

| family | forms | irreducible | pivot count = 4 | pure higher-order |
|---|---|---|---|---|
| homogeneous symmetric | 16 | 14 | 14 | 0 |
| curated redundant | 8 | 6 | 6 | 0 |
| named multiparty 4-party | 7 | 3 | 3 | 0 |
| canonical heterogeneous | 256 | 244 | 244 | 0 |
| total | 287 | 267 | 267 | 0 |

The majority clique is the sharpest case. Every party reads the other three, so the structure is maximally
interchangeable, and its whole-system Φ is positive (1.66). Its irreducible core, though, is only the pair
{B, D}. Knocking out A or C — parties outside that core — still drops the whole-system Φ to zero. Pivotality
to the whole-system irreducibility is broader than membership in the major complex. Raw output is in
[`results/full_output.txt`](results/full_output.txt).

## Interpretation

Redundancy was the reason to expect four parties to differ, and it does not deliver. Even where two parties
could in principle cover for a third, no irreducible form survives the loss of any single one. The Q120
picture holds one party wider: irreducible coordination keeps an individual lynchpin, and every party is
one. A form is irreducible exactly when each of its parties is individually necessary to it.

The majority-clique case adds a second point. A party can sit outside the irreducible core and still be
necessary to the form's irreducibility. Core membership marks where the integrated structure concentrates;
pivotality marks what the integration depends on, and the two come apart. The disintermediation reading of
the construct survives at four parties: there is no arrangement here whose binding hides from every
single-party test.

## Limitations

The search is targeted, not exhaustive, and the claim is bounded to the forms tested. The full four-party
symmetric family (65536 forms) and all non-symmetric wirings are beyond what exact Φ can sweep at a second
per form, so a pure higher-order bind in some untested four-party form is not ruled out. The forms tested
are the symmetric and explicitly redundant ones, chosen because a no-pivot bind is most likely there, which
makes the null strong evidence rather than proof. Five or more parties are untouched and are the natural
next step, up to the exact-Φ size ceiling. The result is exact but in-silico — evidence about the instrument
and the law, not about a real organization.
