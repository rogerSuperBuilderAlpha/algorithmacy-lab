# Q140 — methods

The Q126 interested mediator (AND baseline, approve agenda) at k = 0 (faithful) and k = 1 (interested). For
each, the value v(S) of every coalition S ⊆ {W, S, C} is the integrated information of the subsystem on S at
the verdict's integrating state (Q111's value function). The **parties' maximum collective core payoff** is the
most W and C can keep in a stable allocation: with x_S = v(N) − x_W − x_C, the core constraints reduce to
x_W ≤ v(N) − v(SC), x_C ≤ v(N) − v(WS), x_W + x_C ≤ v(N) − v(S), maximized at x_W + x_C ≥ 0. The mediator's
core take is v(N) minus that. Control: the faithful triad, where v(WSC) = 2.0 and v(WC) = 0 (the parties need
the mediator).

Caveats from Q111/Q122: value-function background, Φ-to-money bridge; "value/core/stable" name cooperative-game
quantities over Φ, not money.

Reproduce: `python -m org_frontier.questions.q140_coalition_stability.probe_coalition_stability`
([`results/output.txt`](results/output.txt)).
