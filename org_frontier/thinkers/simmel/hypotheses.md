# Simmel — Stage 3 hypotheses (fixed before computing)

Each hypothesis renders one of Simmel's claims (C1–C5 in `exegesis.md`) as a prediction the instrument can
refute. Two predictions are stated for each: what Simmel's text commits him to, and what the lab's prior
results (`probes/PROBES.md`) lead one to expect. Where they diverge the paper reports which one the
computation favors. Decision rules are in `methods.md`.

## H1 — The superindividual triad (C1)

Simmel: the dyad has no "superindividual energy"; when one member withdraws "only the other remains." Three
members already have such energy "in some measure," because "each pair of elements are now joined by a
broken line" through the third.

- **H1 (Simmel).** In the mutual triad the irreducible whole is the full triple, its Φ exceeds the mutual
  dyad's, and the pair remains bound through the third when their direct tie is removed. In the dyad,
  removing the tie leaves nothing.
- **H0.** The mutual triad's major complex is a pair with a spectator, or its Φ does not exceed the dyad's, or
  the pair with its direct tie removed does not stay in one complex.
- **Lab prior.** Agrees with Simmel: the conjunctive mediator binds A and B through C at Φ = 2.0 (control form).

## H2 — The decisive step (C2)

Simmel: the step from two to three is the decisive one; beyond it "further numerical increase did not change
it in a marked degree." The occasion for a majority "is given so soon as a single unit is added."

- **H2 (Simmel).** Over mutual conjunctive cliques of n = 2, 3, 4, 5 members, the increment in Φ is largest at
  the 2→3 step and diminishes thereafter: ΔΦ(2→3) > ΔΦ(3→4) ≥ ΔΦ(4→5).
- **H0.** Increments are constant or growing with n; the 2→3 step is not distinguished.
- **Lab prior.** Unknown. Chains hold Φ = 2.0 at every length (`multiparty/chains.py`); cliques have not been
  swept.

## H3 — The majority that overrides the individual (C3)

Simmel: "in a combination of two there is no majority which can override the individual," and majority
domination "depress[es] the individuality." The individual in a triad is bound by a whole that can outvote
him.

- **H3 (Simmel).** A triad in which each member follows the majority of the three is irreducible with all
  three members in the core: the majority is a binding whole.
- **H0.** The majority triad factors (dyadic), or its core omits a member.
- **Lab prior.** Refutes Simmel: a mediator computing a 2-of-3 majority factors entirely (probe 10),
  because no party is pivotal enough. The prior was measured on a mediated form, not a mutual one; this is
  the first mutual test.

## H4 — The nonpartisan: mediator or arbitrator (C4)

Simmel: the nonpartisan either mediates — conveys each party's claim in objectified form while the parties
keep the decision, and "seeks to eliminate himself" — or arbitrates, in which case the parties "have put this
ultimate decision out of their own hands" and the purpose of conciliation "has become a person in the
arbitrator."

- **H4 (Simmel).** Along the scale arbitrator → mediator → self-eliminated mediator: the arbitrator is in the
  core (the decision lives in him); the mediator is in the core but binds less (Φ lower); the mediator whose
  parties have united directly is out of the core (reducible). Ordering: Φ_arb > Φ_med > 0 with membership
  in, in, out.
- **H0.** The mediator is already out of the core (no intermediate grade exists), or the ordering fails.
- **Lab prior.** Partly against Simmel's middle term: any contestability by a party drops that party from the
  core categorically (probe 21), which suggests the mediator form may factor rather than bind weakly.

## H5 — The *tertius gaudens* and the balance of forces (C5)

Simmel: the third's advantage requires no great force of his own; "the necessary amount of the energy... is
determined exclusively by the relationship which the energies of the parties exhibit toward each other."
When the two are "practically equal, a minimum of addition often suffices"; when one preponderates, the
third's position is worth nothing.

- **H5 (Simmel).** Holding every rule fixed except the weights of the two contestants and the third in the
  outcome, the third is in the irreducible core when the contestants are balanced, out when one contestant
  is a dictator, and its membership and pivotality fall monotonically between: balanced ≥ intermediate ≥
  dictator, with the third out of the core under the dictator.
- **H0.** The third's core membership does not track the contestants' balance.
- **Lab prior.** Agrees with Simmel: core membership rises with pivotality (probe 11), zero influence excludes,
  balanced influence marks the triadic forms (probe 16).

## Not tested here

The contingency of the *tertius gaudens* and of *divide et impera* on the parties' inability to combine — the
bypass-counterfactual reading — was already run in q214 (probe #368): both classify contingent at margin
2.0. This paper cites that result and does not repeat it.
