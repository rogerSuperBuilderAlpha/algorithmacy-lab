# Hegel — findings

Hegel's genuine middle is the lab's mediator, and his system of three syllogisms is the lab's clique;
between them sits a result about time. The syllogism with a fixed middle — the conjunctive triad — is a
whole of three at Φ = 2.000, exactly the judgment's Φ (the copy dyad, 2.000): the middle adds a member and
no integration (H1 refuted as pre-registered: equal, not more; and the deletion test tripped on a
self-holding singleton, see caveats). Communication and scent — a middle that relays, the source staying
what it was — have Φ = 0 and no complex containing the middle though every term is reachable (H2 confirmed).
An extreme read by the middle that does not read back is outside the core; the syllogism's core is
{A, M, B} and the half-return's {A, M} (H3 confirmed). In the syllogism the middle's removal costs 1.000 on
the pre-registered deletion rule (2.000 when orphans are constants) and an extreme's costs nothing; in the
system, where every term is middle to the other two, each term's removal costs 4.000 (H4 partial). The
system's Φ, 6.000, is three times the syllogism's. The rotating middle — each term middle in turn, by a
three-phase clock — is a whole of three with the clock outside, at Φ = 2.000: a single syllogism's, not the
system's 6.000 (H5 partial). Alternation in time yields one syllogism at a time; the totality is
simultaneity.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | the middle founds the connection | **REFUTED** | M in core ✓; delete M → whole Φ 0 but a self-holding extreme counts as a one-node complex (Φ 1) so the "no complex" clause failed; Φ(syllogism) 2.000 = Φ(judgment) 2.000 |
| H2 | the external middle connects without uniting | **CONFIRMED** | communication, scent: Φ 0; B reachable from A; only complex is {A} holding (1.000) |
| H3 | the real middle is one the extremes return through | **CONFIRMED** | syllogism core {A,M,B}; half_return core {A,M}, B out |
| H4 | the system has no distinguished binder | **PARTIAL** | syllogism shares A 0, M 1.000, B 0 (pre-registered rule; (0, 2, 0) post hoc with constants); system shares 4.000 each; Φ(system) 6.000 = 3 × 2.000 |
| H5 | the alternation of middles is the totality | **PARTIAL** | rotating core {A,B,C} at 2.000, clock out, whole 0; system 6.000; syllogism 2.000 |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}). The H1/H3/H4/H5 "syllogism"
form is the control under Hegel's labels.

## Caveats

- Deletion rule: an orphaned term holds its own state; PyPhi counts a self-holding single node as a
  complex at Φ = 1. This is why "M necessary" failed in H1 and M's share is 1.000 in H4. With orphans as
  constants (post hoc, `results/posthoc_constant_orphans.json`): minus-M has no complex; shares (0, 2, 0).
  The pre-registered verdicts stand as fallen.
- One rendering: conjunctive middle; extremes copy the middle. Rotation by an exogenous three-phase clock.
- In-silico: two- to five-node forms.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_middle
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_external
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_return
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_system
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.hegel.probe_hegel_rotating
```
