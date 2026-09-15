# Coleman — findings

Closure does what Coleman says and costs what he did not count. With A yielding only to a joint sanction and
B, C sanctioning when A defects, the open structure has no fixed point — the sanction cycles forever — and
the closed one has compliance with the sanction standing as a fixed point, with B and C as the core (H1
confirmed). But the open structure is a whole of three at Φ = 2.000 and the closed one is reducible
(Φ_MIP = 0) with a core of the two sanctioners at 0.369 and A outside: the effective norm is a looser
structure than the ineffective one, and B, who closes, "captures" all of a loss of 1.631 (H5 refuted). On
Burt's own broker forms, closure holds or raises the core's Φ (2 → 2; 2 → 6) and drives the broker's
positional advantage from 2.000 to 0 for both brokers — the Burt paper's H1 read for the collective is
Coleman's confirmation (H2 confirmed). The four-member credit ring is one complex of all four at 2.000 with
every member's value added 2.000; two bilateral credits are a pair (H4 confirmed). Intergenerational closure
does not make the community one: the parents' tie makes the parents the core, {P1, P2} at 2.000, the
children fall out (value added 0), and the all-norm state's basin does not widen (H3 refuted). Across the
five, closure produces rest, coalition, and equality; it does not produce a larger whole except where every
party reads every other disjunctively.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | closure makes the norm effective | **CONFIRMED** | open: no fixed point, core {A, B, C} 2.000; closed: 111 fixed, core {B, C} 0.369 |
| H2 | closure raises the whole and lowers the broker (on Burt's forms) | **CONFIRMED** | info coreΦ 2→2, advantage 2→0; control coreΦ 2→6, advantage 2→0 |
| H3 | intergenerational closure makes the four one | **REFUTED** | open core {P2, K2} 2.000; closed core {P1, P2} 2.000, children V 0; basin(1111) 1/16 both |
| H4 | the credit ring is one unit | **CONFIRMED** | ring4 core all four 2.000, V 2.000 each; two_dyads core {C, D} |
| H5 | the closer captures less than the whole gains | **REFUTED** | gain −1.631; ΔV(B) −1.631; fraction 1.000 |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}).

## Caveats

- The norm form's negations (B' = ¬A) make the open structure a permanent sanction cycle; a rule in which a
  sanction is lifted on compliance with a lag would be another form.
- A deleted party's variable reads 0; for B' = ¬A ∨ C, deleting A makes B a constant 1.
- H2 re-reads the Burt paper's numbers unchanged; it is a reinterpretation, not a new computation.
- The parents form's children (K = P ∧ K′) require both parent and friend to hold the norm; the basin of
  1111 is then the state itself in both forms, and the basin clause could not discriminate.
- In-silico; three- and four-node forms. No community is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_norm
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_broker
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_parents
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_credit
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_public
```
