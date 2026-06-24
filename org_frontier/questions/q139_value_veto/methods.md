# Q139 — methods

The Q126/Q127 interested mediator on two baselines — AND (sparse) and XOR (balanced) — approve agenda. At each
interestedness level k with positive Φ: the **veto count** is the number of the three parties whose knockout
(spectator P' = x[P]) flips the verdict to dyadic; the **value share** is the mediator's Shapley value of
subsystem Φ at the integrating state over the total; the **gap** is that share minus 1/3 (its equal share of a
universal three-party veto). Control: the faithful triad (Φ = 2.0, veto 3/3, mediator value two-thirds, gap
+1/3). Forms with Φ = 0 are reported as dead (nothing to veto).

Caveats from Q111/Q122: value-function background, Φ-to-money bridge; "value/share/veto" name structural
quantities, not money or legal power.

Reproduce: `python -m org_frontier.questions.q139_value_veto.probe_value_veto`
([`results/output.txt`](results/output.txt)).
