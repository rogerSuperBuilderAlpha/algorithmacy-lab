# multiparty — does adding parties change the verdict?

Extends the literacy/algorithmacy classifier past the dissertation's three-node focus. The
question: when a worker coordinates with more than one counterpart through a mediator, does the
form still demand algorithmacy?

## Run

```bash
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.run [n_sample] [seed]   # named forms + n=4 population
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.chains [max_k]            # mediator-chain depth
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.scaling [n] [n_sample] [seed]  # n=5 population
~/iit-playground/venv-4.0/bin/python -m org_frontier.multiparty.robustness [n_sample] [noise] [seed]  # n=4 reachability check
```

`run.py` classifies the named four-party forms and samples the strict-mediation n=4 population.
`chains.py` lengthens the mediator chain. `scaling.py` samples larger n. `robustness.py` rules out
the reachability confound by recomputing the triadic rate with noise.

## Results

See [`FINDINGS.md`](FINDINGS.md). Three findings:

1. **Substitutability collapses irreducibility.** A mediator that can satisfy its determination with
   *either* counterpart (`W ∧ (C1 ∨ C2)`) factors — dyadic. Only an *all-required* conjunction
   (`W ∧ C1 ∧ C2`) stays triadic (Φ = 3.0, reproducing the dissertation's pooled form).
2. **Layered mediation stays triadic.** Two mediators in series (W → S1 → S2 → C) is irreducible
   (Φ = 2.0).
3. **Irreducibility gets rarer with more parties, to the point of vanishing.** Random
   strict-mediation forms are triadic 9.4% of the time at n = 3, 2.3% at n = 4, and **0%** at n = 5
   — and noise robustness checks confirm this is genuine, not an attractor-collapse artifact (n=4:
   deterministic and full-reachability both 3.3%; n=5: 0/60 under full reachability). Triadic forms
   still *exist* at every n (the chains, the all-required pool); random coupling just produces them
   ever more rarely.
4. **Chain depth is Φ-invariant.** Mediator chains stay triadic with Φ = 2.0 at every length
   (n = 3 through 6), MIP always a balanced 2-part cut. Depth does not factor; breadth (more
   parties) does.

## Files

- `forms.py` — named four-party forms with rationale.
- `run.py` — classify named forms; sample the n=4 population; report P(triadic) vs n=3.
- `chains.py` — mediator-chain depth study (Φ vs chain length).
- `scaling.py` — sample larger-n strict-mediation families (n=5 and beyond).
- `robustness.py` — noisy recompute ruling out the reachability confound.
- `results/` — `named.csv`, `population_n{4,5}.csv`, `chains.csv`, `robustness_n4_noisy.csv`.
- `FINDINGS.md` — the results, the org-theory reading, and the robustness checks.
