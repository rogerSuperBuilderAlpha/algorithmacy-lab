# Ten Φ experiments seeded by the sweep

[`iit_experiments.py`](iit_experiments.py) takes the structural side of the sweep's findings and pins
it down on exact Φ. The sweep found that structure and behavior locate a coordination's tight pair
differently, that a relay couples without integrating, and that irreducible forms couple
synchronously. These ten experiments ask what the structure itself is doing. Each prints one result;
the numbers reproduce at the seeds in the script.

## Structure and behavior locate different things

**E1 — the core pair and the tight pair often differ.** Among 46 random irreducible forms with a
two-node major complex, the dynamically tightest pair, scored by sustained directed recurrence,
differs from the Φ-core pair in 33%. The structural core and the behavioral tight pair are related
measures of the same arrangement that disagree a third of the time, which is why a study reads both.

**E7 — Φ and determinism dissociate.** Across 200 random forms the correlation between integrated
information and the best pair's determinism is −0.40, and 48 forms carry determinism above 0.8 with
zero Φ. Sustained behavioral coupling runs opposite to structural irreducibility as often as with it.
A relay is the clear case: clean parallel tracking, nothing integrated.

## What makes a form irreducible

**E3 — feedforward chains integrate nothing.** Relay chains of length two, three, and four all carry
Φ of zero, and the major complex is the single source node. A signal passed cleanly down a chain
leaves no integrated whole behind it, at any length.

**E4 — reciprocity drives irreducibility.** A random form with a reciprocal edge between two parties
has positive Φ in 95% of cases; without any two-cycle, 60%. A mutual tie is the strongest single
structural predictor of irreducibility. The 60% without a two-cycle shows the longer loop also binds:
a three-cycle that closes through all three parties integrates without any pairwise reciprocity.

**E10 — the verdict is robust to a single bit.** Flipping one entry of one party's rule changes the
dyadic-or-triadic verdict in 7% of 2880 perturbations. The structural reading depends on the wiring
as a whole, not on any single transition, which is what a verdict meant to survive a re-encoding
should do.

## Where the third party sits

**E2 — whole-system Φ detects the false dyad.** A true dyad and a false dyad present the same
worker-system pair. `chat_dyad` carries whole-system Φ of zero, the third party decoupled.
`gig_false_dyad` carries whole-system Φ of 2.0, the same presented pair, because the hidden read makes
the whole irreducible. Both keep their major complex on the W-S pair, so the surface and the core look
alike; the whole-system Φ is what separates them.

**E8 — three places the third party can be.** Across the corpus the third party falls into three
arrangements. In the true dyads it is excluded from the core and whole-system Φ is zero: `chat_dyad`,
`gig_dyadic_model`, `ats_feedback_factors`, `pure_relay`. In the constitutive triads it is a core
member and whole-system Φ is positive: `ats_strict_bottleneck`, `two_sided_match`. The false dyad is
its own case: whole-system Φ is 2.0, yet the third stays out of the major complex. A direct
back-channel makes a fourth case, where the third is a core member through the side edge while
whole-system Φ stays zero (`hierarchy_backchannel`, core W-C).

**E6 — the third joins the core only when the system commits.** Two forms share the bottleneck
topology. `ats_strict_bottleneck`, where the system forwards on a conjunction of both parties, has
whole-system Φ of 2.0 and a full W-S-C core. `ats_feedback_factors`, where the system stores and the
parties decide, has whole-system Φ of zero and a W-S core. The same wiring commits or conveys by the
rule alone, and the third party's membership turns on it.

**E9 — the false dyad's membership is the least stable.** Reading the major complex at each reachable
state, the dyadic forms hold one core throughout. The constitutive triads move between two. The false
dyad moves between three (W-S, W-S-C, and C alone), the most state-dependent membership in the corpus.
Its irreducibility is real and its seat shifts with the state, which fits a concealment that depends
on what the parties are doing.

## The veto player and the core are not the same member

**E5 — the cooperative-game veto player sits in the IIT core 38% of the time.** Across 194 random
irreducible forms with a veto player, the veto player is a subset of the major complex in 38%. The
party that sits in every integrating coalition, the cooperative-game pivot, and the party that belongs
to the irreducible whole are different notions that coincide in a minority of forms. The veto-player
and major-complex readings of "the central party" are two lenses, and a study that wants the pivotal
party should say which one it means.

## What this establishes

Whole-system Φ separates a true dyad from a false one, reciprocity is the main driver of
irreducibility with longer loops as a backstop, the verdict survives single-bit perturbation, and the
third party's place in the core turns on whether the system commits. Structural irreducibility and
behavioral coupling are distinct, sometimes opposed, and the cooperative-game pivot and the IIT core
member are distinct too. Paired with [CRQA_EXPERIMENTS.md](CRQA_EXPERIMENTS.md), the structural side
says what a coordination is; the behavioral side says how it runs.
