# Q134 — methods

The conjunctive star for n = k + 1 parties: node 0 is the mediator S with S' = P1 ∧ … ∧ Pk; each outer party
Pi reads S (Pi' = S). For k = 2 this is the read-recipient triad. The value of a coalition is the integrated
information of the subsystem on it (`pyphi.new_big_phi.sia`), read at the integrating (all-ones) state — the
verdict's max-Φ state for these conjunctive forms — and a party's Shapley value is its average marginal
contribution. The control is the triad (k = 2), reproducing Q111: total Φ = 2.0, mediator 1.333, share
two-thirds. Reported per n: total Φ, mediator Shapley and share, each outer party's share.

Caveats from Q111/Q122: the value function's background, the unproven Φ-to-money bridge; "value/share/rent"
name Shapley allocations of Φ. Exact Φ scales steeply, so n is taken to 5.

Reproduce: `python -m org_frontier.questions.q134_rent_scaling.probe_rent_scaling`
([`results/output.txt`](results/output.txt)).
