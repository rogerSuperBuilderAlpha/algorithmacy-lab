# q149 — review

## Claim under test

The two-thirds mediator rent of the read-recipient triad is a property of the single mediator, not of
mediation in general. Distributing the mediator role across more hubs does not redistribute the rent
toward the parties.

## What holds

The control passes: the read-recipient triad reads total Φ 2.000 with the mediator at 0.666. The
Shapley split is exact (full enumeration of orderings), so the per-node values are not estimates. The
symmetric result is clean and worth stating on its own: ring and pool give spread 0.000 at both sizes,
which is the strongest form H2 could take.

## Where a reviewer should push

1. The negative party Shapley values are the headline and the soft spot. They are correct for the
   integrating state used by `shapley` (all-ones), where a conjunctive multi-hub credits the hubs and
   debits the parties. A reviewer can fairly ask whether the all-ones state is the right reference, or
   whether a different integrating state or a normalized value function would change the sign. The
   finding is conditional on that choice and should be read as such.
2. The H1 test mixes two series: the single-hub/m-hub conjunctive family and the two-hub form, which is
   built differently. The verdict rests on the conjunctive m-hub series, which is the clean monotone
   candidate. The two-hub row is reported for context.
3. n is 5 and 6 only. The exact Shapley split is expensive, so the topology sweep is shallow. The
   non-monotone per-hub pattern is consistent across both sizes, but two points do not establish an
   asymptote.

## Standing

H1 refuted, H2 supported, both on synthetic Boolean forms. The result maps how the exact-Φ Shapley
split moves with topology. It does not measure value capture in any organization, and the gap between
these forms and any field setting is open.
