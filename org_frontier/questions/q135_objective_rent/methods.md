# Q135 — methods

The Q128 model: four nodes W, S, C, O with W' = S, S' = O (predatory mediator), C' = S, and O' an adaptation
rule (frozen O' = O, or adaptive O' = W ∧ C / W ∨ C / W ⊕ C). The value of a coalition is the integrated
information of the subsystem on it, read at the verdict's max-Φ state (the integrating state, per Q132's
convention), and a party's Shapley value is its average marginal contribution. Reported per adaptation: total
Φ, the full Shapley split, and the objective's, system's, and collective-parties' shares. The control is the
faithful three-party triad (mediator two-thirds, Q111).

Caveats from Q111/Q122: value-function background, unproven Φ-to-money bridge; small negative Shapley values
at weakly-integrated forms are non-monotonicity artifacts. "Value/share/rent" name Shapley allocations of Φ.

Reproduce: `python -m org_frontier.questions.q135_objective_rent.probe_objective_rent`
([`results/output.txt`](results/output.txt)).
