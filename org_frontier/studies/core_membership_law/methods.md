# Core-membership law — Stage 4 methods

A reader should reproduce every number from this file and `core_membership.py` alone.

## Shared infrastructure
- Verdict / Φ: `org_frontier/classifier/classifier.py` (`classify_rules`, `cm_from_rules`).
- Major complex (membership): `org_frontier/probes/lib.py` (`major_complex`).
- Instrument controls: `org_frontier/classifier/validate.py`.
- Python: run from the repo root with the project venv active (see `GETTING_STARTED.md`).

## Instrument control (run first)
The battery computes both canonical controls before any result and aborts if either fails: the
factoring control must read dyadic, the irreducible control triadic.

## Definitions (fixed before the run)
- A node is **bidirectionally coupled** iff its connectivity row and column both have an off-diagonal
  edge — it feeds at least one other node and is fed by at least one other node (`cm_from_rules`).
- A node's **influence** is the determination's Boolean sensitivity to it: over all (target node,
  state) pairs, the fraction where flipping the node changes the target's next value.
- A node is **in the core** iff it is in the major complex (`major_complex`), the maximally
  irreducible subset over reachable states.

## Tests
- **H1 (necessity).** Over 600 random 3-node forms (seed 0), count how often a node that is *not*
  bidirectionally coupled appears in the major complex. Decision rule: H1 holds if the rate is ~0%
  (a handful at most, attributable to ties), refuted if non-bidirectional nodes routinely enter.
- **H2 (pivotality).** Among bidirectionally coupled nodes, compute the rank-AUC of influence
  predicting core membership, and the inclusion rate by influence bucket. Decision rule: H2 holds if
  AUC is well above 0.5 and the bucketed inclusion rate is monotone increasing.
- **H4 (rarity).** The triadic rate over the same 600 random 3-node forms. Decision rule: a small
  minority (order 10%), consistent with the population finding.
- **H5 (conjunctive law).** For n = 3, 4, 5, an AND-of-all-parties mediator with each party reading
  it: report Φ and the core. Decision rule: Φ = n−1 with the full node set in the core at every size.

## Reproduction
```
python -m org_frontier.studies.core_membership_law.core_membership
```
Deterministic given the seed; exact Φ has no sampling. The headline numbers are registered in
`ci/reproduce.json`.
