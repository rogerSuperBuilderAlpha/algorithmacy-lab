# Q138 — methods

The triad W, S, C. The mediator's default rule is the predatory constant 1 (always approve). The regulator
forces m of the four (W, C) input states back to the faithful AND commit, in highest-warrant order (state
(1,1) first, then (0,1)/(1,0), then (0,0)). For each m = 0..4: the verdict Φ (max over reachable states) and
the Shapley value of subsystem Φ at the integrating state, giving the mediator's share and the parties'
collective share. Control: fully faithful (m = 4), reproducing Q111 (Φ = 2.0, mediator two-thirds).

The forcing order matters; highest-warrant-first is the natural regulatory target (force the commit where the
parties most warrant it). Caveats from Q111/Q122: value-function background, Φ-to-money bridge; "value/share/
rent" name Shapley allocations of Φ.

Reproduce: `python -m org_frontier.questions.q138_faithful_fraction.probe_faithful_fraction`
([`results/output.txt`](results/output.txt)).
