# q167 — methods

## The model

The four-node extended-mind core from battery_extended_mind: W (worker), S (system), C (counterpart), P
(platform). The parties and the platform read the system (W' = S, C' = S, P' = S). The system commits a
g-weighted mix of two branches, S = (1 − g)·(W ∧ C) + g·platform(P, C). The mixing weight g is the
capture share: at g = 0 the system commits the worker's joint determination W ∧ C; as g rises the
platform branch takes over.

The faithful platform branch is P ∧ C, the battery's own form (the control). The interested platform
branch is Q126's mediator(agenda, k) over the platform's inputs (P, C): the platform outputs its agenda a
on the k (P, C) states that least warrant a, faithful AND elsewhere. k = 0 is faithful; approve (a = 1)
overrides toward 1 from the states with the fewest inputs on, deny (a = 0) overrides toward 0 from the
states with the most.

## The sweep and the readings

g runs the fixed grid {0.00, 0.05, …, 0.50} (step 0.05). The faithful control already loses the worker
between 0.00 and 0.10, so the low-g grid resolves g* for every setting. For each (agenda, k) the reading
is the maximal complex of the 16-state TPM, computed with the battery's exact reader
(pyphi.new_big_phi.maximal_complex), taken as the max-Φ complex over the 16 states. Two quantities are
read off the membership:

- **g\*** — the first grid g > 0 at which W has left the major complex (the worker-governs threshold). If
  W keeps her seat across the whole grid, g* is recorded as "none".
- **the post-displacement core** — the core at g*, used to test whether the worker is replaced by the
  counterpart C (the faithful outcome) or by the agenda node P.

The settings are the faithful control, approve k = 1..4, and deny k = 1.

## H1 and H2

H1 compares the g* sequence across rising interest. It holds when g* falls weakly at every step from
faithful through the approve ladder and strictly somewhere ("never displaces within grid" counts as +∞).
H2 compares post-displacement cores: it holds only if the faithful core holds C and not P, every
interested setting that displaces W within the grid has a post-core containing P, and every such post-core
differs from the faithful one. The verdicts are computed from the swept numbers in the probe.

## Reuse

The forms live in the shared bridge `org_frontier/cognition/interested_mediator_forms.py`: `core4_tpm`
builds battery_extended_mind's core4(g) TPM with the platform branch optionally interested, `core4_complex`
runs the battery's exact maximal-complex reader over the 16 states, and `_platform_branch` swaps P ∧ C for
Q126's mediator(agenda, k). The interested gate is Q126's mediator imported unchanged. No Φ is
reimplemented.

## Reproduce

```
python -m org_frontier.questions.q167_capture_meets_agenda.probe_capture_meets_agenda
```

Output is saved in [`results/output.txt`](results/output.txt). The forms are deterministic Boolean gates
and the one RNG seed is fixed at 0; three runs are byte-identical. The run takes under a minute (66
four-node maximal-complex evaluations).
