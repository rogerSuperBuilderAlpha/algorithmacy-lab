# Q137 — methods

The triad W, S, C. The system rule at interestedness k_S imposes its agenda (approve) on the k_S states where
the parties least warrant it, committing W ∧ C elsewhere (the Q126 ladder). The worker reads only S; the
faithful worker is W' = S, and at interestedness k_W it overrides toward acting regardless (= 1) on k_W of its
two input states. Both are swept over {0, 1, 2}. Per cell: the verdict Φ (max over reachable states) and the
worker's Shapley value of subsystem Φ at the integrating state — absolute and as a share. The control is the
faithful triad (Φ = 2.0, worker Shapley 0.333 = one-sixth).

Caveats: the worker reads only the system in the canonical triad, so its interested rule has few states and
saturates quickly (a richer worker is a limitation). Φ-to-money bridge open (Q122); "value/share" name Shapley
allocations of Φ. Small negative Shapley at collapsed forms are non-monotonicity artifacts.

Reproduce: `python -m org_frontier.questions.q137_interested_worker.probe_interested_worker`
([`results/output.txt`](results/output.txt)).
