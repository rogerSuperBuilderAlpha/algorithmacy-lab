# Latour — findings

Latour's intermediary counts for one in Φ and for one more in membership. A chain of k copy-relays inserted
into a mutual dyad leaves Φ at 2.000 for every k from 0 to 3 — the whole is no more integrated with the
relays than without — but every relay is in the core (H1 refuted). Between the same two parties, both kinds
of mediator are in the core and so is the intermediary; the joint mediator (M' = A ∧ B) evicts A, leaving
{M, B} (H2 partial). Making a difference is necessary for membership and not sufficient: an exogenous source
that determines the whole and is determined by nothing but itself is outside it, core {M, A} (H3 refuted).
The citizen-gun's translation form binds citizen, gun, and act at Φ = 2.000; the autonomous-destiny form
drops the citizen and the act, leaving the gun alone at core Φ = 1.000; the neutral-tool form binds the gun
it was supposed to reduce to a tool, and is structurally identical to translation (H4 partial). The star of
mediators is a whole of four at Φ = 5.000 and out-integrates the star of intermediaries at Φ = 3.000, which
is also a whole of four (H5 confirmed). What Latour's line marks is not membership but Φ: a mediator adds
integration, an intermediary adds a member and no integration.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | the intermediary counts for one | **REFUTED** | chain0..3 Φ_MIP = 2.000 all; cores {A,B}, {A,I1,B}, {A,I1,I2,B}, {A,I1,I2,I3,B} |
| H2 | mediators count, the intermediary does not | **PARTIAL** | intermediary core {A,M,B}; mediator_joint {M,B}; mediator_specific {A,M,B}; all Φ 2.000 |
| H3 | actor = whatever makes a difference | **REFUTED** | source: S makes a difference, core {M,A}, Φ_MIP 0; every core member makes a difference in all forms |
| H4 | citizen-gun: translation binds both, each myth drops one | **PARTIAL** | translation {C,G,X} 2.000; autonomous {G} 1.000 (drops C and X); neutral_tool {C,G,X} 2.000 (keeps G) |
| H5 | the actor-network is the star | **CONFIRMED** | star_mediators {A,M1,M2,M3} 5.000; star_intermediaries {A,M1,M2,M3} 3.000 |

Instrument control (conjunctive triad, Φ = 2.000000, core {A, M, B}) passed in all five probes.

## Caveats

- Intermediaries here sit in loops (a dyad's tie, a triad's cycle, a star read back by its center). The
  lab's probe #19 conveyor, which factors, is not in a loop. Latour's intermediary is an open-chain concept
  applied to closed networks; the paper says which case each result concerns.
- One rendering each of "specificity" (M' = A ⊕ M) and of the citizen-gun readings.
- In-silico: three- to five-node Boolean forms.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_intermediary
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_mediator
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_difference
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_gun
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.latour.probe_latour_star
```
