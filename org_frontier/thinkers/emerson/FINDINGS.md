# Emerson — findings

All four balancing operations balance, and none of them takes anything from the strong actor except the
first. The C–A–B network — A served by B or C, each served by A alone — is a whole of three at Φ = 2.000 in
which A adds the whole (V 2.000) and the dependents add nothing; A's positional advantage is 2.000 (H1
confirmed). Withdrawal drops B from the complex and leaves A and C a pair at 2.000 with V 1.000 each (H2
confirmed): the one operation that lowers A's value added, by halving it. Extension — the B–C tie — makes an
OR-clique at 6.000 with every member's V 4.000 and A's advantage 0 (H3 confirmed). Status-giving makes A and
B a pair at 2.000 with V 2.000 each and C outside adding nothing (H4 confirmed). Extension and coalition both
bring A's advantage to 0, and coalition raises the weak from 0 to 6.000 as Emerson says; but extension
raises A too, from 2.000 to 4.000, rather than reducing him (H5 partial). The distinction Emerson drew
between the two survives in a form he did not name: under extension each member adds 4.000 to a whole of
6.000, so a pair at 2.000 outlives any deletion — a network; under coalition each member adds 6.000, the
whole, so nothing outlives a deletion — a collective actor.

## Verdicts

| H | claim | verdict | key numbers |
|---|---|---|---|
| H1 | the C–A–B network is unbalanced with A indispensable | **CONFIRMED** | core all three 2.000; V(A) 2.000, V(B) = V(C) 0; advantage 2.000 |
| H2 | withdrawal balances | **CONFIRMED** | core {A, C} 2.000; V(A) = V(C) 1.000; B out; advantage 0 |
| H3 | extension balances and keeps three actors | **CONFIRMED** | core all three 6.000; every V 4.000; advantage 0 |
| H4 | status-giving balances A–B only | **CONFIRMED** | core {A, B} 2.000; V(A) = V(B) 2.000; V(C) 0 |
| H5 | extension reduces the strong; coalition raises the weak | **PARTIAL** | both advantage 0; V(A) 2 → 4 under extension (rises); V(B), V(C) 0 → 6 under coalition |

Instrument control passed in all five probes (Φ = 2.000000, core {A, M, B}).

## Caveats

- Withdrawal is rendered as B holding its own state; a constant B would be another form. The withdrawal
  form's core is read over reachable states, and at states where B is on, A is on regardless of C.
- Coalition is rendered as B and C acting only together and A denied alternatives, which is the Ostrom
  paper's self-governance clique; a coalition without denying A alternatives is the Blau paper's organized
  form (core {B, C}, A outside).
- Value added reads a deleted variable as 0.
- In-silico; three-node forms. No exchange is measured.

## Reproduce

```
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_network
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_withdrawal
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_extension
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_status
~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.emerson.probe_emerson_coalition
```
