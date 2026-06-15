# Thread — the enricher regime

A second twenty-step dive, into the regime the first thread named but did not understand: the
**enricher** — a mediating system that is in the irreducible core yet dispensable, the value-added
platform. It turned out to be rare, fragile, and locally indistinguishable from a darker neighbour,
and chasing why produced an outside-option theory of platform power. In-silico, on small Boolean
models; reproduce the headline numbers with
`python -m org_frontier.field.threads.enricher_regime`.

## The arc, with its turns

**E1.** The enricher looks robust: single-bit perturbations of the canonical escrow enricher keep it
an enricher most of the time, and never make it a bottleneck. Bottleneck and enricher are not
adjacent — they differ on whether a party fallback exists at all, a structural, not incremental,
fact.

**E2–E3 (the confound).** "In the core" was hiding two things. Some in-core mediators join the full
triad (genuine enrichment); others form an exclusive pair with one party and eject the third —
capture. Separating them inverts the picture from the first thread. Over random forms: genuine
**enrichment is rare (6.0%)**, true bottlenecks rarer (2.6%), and **capture is the dominant in-core
regime (28.2%)**. The first thread's "enricher 23%" was mostly capture.

**E4–E6 (three nulls).** No local property separates enrichment from capture. Not the mediator's
logic, not its symmetry (captures are if anything *more* symmetric), not the balance of pairwise Φ
(both have all three pairs at Φ=2.0). The distinction is not in the mediator. It is a global outcome
of the Φ-competition, with no structural basin enrichment can be engineered toward.

**E5b, E17 (fragility).** Genuine enrichment is not defendable. Perturbing the symmetric escrow
enricher by one bit turns it into capture a third of the time. Any realistic drift breaks it. The
structural gravity of an in-core platform is toward capture.

**E7–E8 (the mechanism).** What separates the regimes is the parties' **outside options**. Strengthen
both parties' alternatives symmetrically and the enricher slides to **bypassed** (disintermediation).
Strengthen only one and it slides to **capture** — and the captured party, the one locked into the
core with the platform, is the one *without* the outside option. The party that has an alternative is
structurally free; the dependent party is bound. Capture is lock-in of the dependent side.

**E9 (the phase diagram).** Mapping each party's option (none / conditional / full) against the other
lays the regimes out cleanly. No options on either side is the bottleneck. Full options on both is
bypass. One full, one none is capture, locking in the side without the option. The enricher sits
alone at the centre, where both options are conditional and symmetric.

**E10–E11 (grounding, and a dark twist).** Thin market, both captive: bottleneck. Captive worker,
mobile counterpart: capture, worker locked in — gig precarity. Thick market, both multi-homing:
bypassed. And the twist: giving the captive worker a full outside option while the counterpart stays
captive does not free the system. It **transfers the lock-in to the counterpart**. Partial
empowerment moves capture; only symmetric options dissolve it.

**E12–E14 (the law).** The pattern scales and is exact. A platform's irreducible core shrinks
monotonically as parties gain options, always retaining itself plus exactly the option-less parties.
Lock-in is real dependence: freeze the platform and the captive party cannot coordinate at all, and
its only escape — its own outside option — is the very move that disintermediates the platform. The
law holds on 60 of 60 random option configurations: **a platform's irreducible core is itself plus
the parties with no outside option.**

**E16 (what the enricher is).** The enricher's fallback works only when the platform permits it — the
parties coordinate directly at the platform's "on" state, not its "off" state. The enricher is the
platform that *enables its own fallback*. It is in the core because it builds the integration, and
dispensable because the integration it builds does not, once built, require it.

**E15, E19 (the boundaries).** The core law is cleanest for the conjunctive platform that needs both
parties; a permissive (OR) platform has a different phase structure. And the lesion test credits a
fallback if the parties coordinate under *some* frozen platform state; a reachability-weighted test
is sharper, though the enricher's enabling state is reachable in the case checked.

**E18, E20 (the instrument).** For a field study, the one thing to measure is which parties have an
outside option. It predicts the platform's fate: captive worker and mobile counterpart → capture;
both mobile → bypassed; neither able to exit → bottleneck; both with portable, platform-enabled
options → the fragile enricher.

## What the thread found

A platform's place in the coordination is governed by the parties' outside options, and the four
regimes are a single phase diagram:

- **Bottleneck** — no party has an outside option. The platform is the sole integrator, in the core
  and indispensable to all. Rare in the random population (2.6%); typical of a thin or captive market.
- **Enricher** — both parties have a *conditional* option the platform itself enables, symmetric. The
  platform deepens the coordination yet is dispensable. Rare (6.0%) and fragile: it sits at the
  centre of the phase diagram, one drift from capture or bypass, and cannot be defended.
- **Capture** — outside options are asymmetric. The platform's core is itself plus the party without
  an option; the party with one is free. This is structural lock-in of the dependent side, and it is
  the dominant in-core regime (28.2%).
- **Bypassed** — both parties have full outside options. The platform is disintermediated.

The general law: **a platform's irreducible core is itself plus exactly the parties with no outside
option.** Disintermediation, capture, and lock-in are all consequences of how outside options are
distributed. The benign reading — a value-added platform that holds the coordination together while
leaving everyone free — is the enricher, and it is the rarest and least stable of the four. The
structural pull of a platform that inserts itself into a coordination is toward capturing whoever
cannot leave.

## Limits

In-silico, on three- and four-node Boolean models; Φ is read only as the binary verdict and the
membership. "Outside option" is encoded coarsely as none / conditional / full, and the law is
sharpest for the conjunctive platform. The lesion test is the looser, non-reachability-weighted
version. And the whole thread inherits the field protocol's gap: these are stipulated models. What a
field study takes from it is the variable to measure — each party's outside option — and the
prediction it licenses, to be confirmed or broken against a real platform.
