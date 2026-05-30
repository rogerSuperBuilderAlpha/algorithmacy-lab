# Φ‑structure suite: is scalar Φ an impoverished summary?

**Question.** [Barrett et al. (2026)](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/)
argue that a single number Φ should be replaced by **a suite of quantities** —
a multi‑dimensional characterization of a system's cause‑effect structure. This
experiment takes that proposal literally: it extracts the full IIT‑4.0
Φ‑structure for many `(network, state)` pairs and asks **what the suite captures
that scalar Φ throws away.**

It is the third experiment in this repo, complementing the two audits
([`proxy_audit`](../proxy_audit/), [`candidate_audit`](../candidate_audit/)),
which asked whether *cheaper* measures can stand in for Φ. Here we instead ask
whether Φ itself is *enough*.

## The suite (`suite.py`)

Extracted from a single `pyphi.new_big_phi.phi_structure` call — so correctness
rests on PyPhi:

| Dimension | Meaning |
|-----------|---------|
| `phi` | scalar system integrated information |
| `n_distinctions` | number of irreducible cause‑effect distinctions |
| `sum_phi_distinctions` | total small‑φ of the distinctions |
| `n_relations` | number of relations among distinctions |
| `sum_phi_relations` | total φ of the relations |
| `mean_order` / `max_order` | mechanism order (1 = single unit, 2 = pair, …) |
| `frac_higher_order` | fraction of distinctions of order ≥ 2 |

## Design

Unlike the audits (one Φ per network), this is about **structural variation
across states**, so each row is one `(network, state)` pair. We sample reachable
states from random Boolean networks (`n ∈ {3,4}`), capping states per network
because relation counts (and cost) grow quickly with `n`.

## Analyses (`analyze.py`)

1. **Redundancy with Φ** — rank correlation of each structural dimension with
   scalar Φ. Dimensions with `|ρ|` well below 1 carry information Φ alone misses.
2. **Φ = 0 still has structure** — reducible systems (Φ = 0) can have many
   distinctions and relations; scalar Φ reports "nothing," the structure says
   otherwise.
3. **Same Φ, different structure** — the spread of structural dimensions within
   narrow Φ bands.

Plus a correlation heatmap of the suite and Φ‑vs‑structure scatters.

## Reproduce

```bash
python -m structure_suite.run 1       # -> results/suite.csv
python -m structure_suite.analyze      # -> summary.csv, suite_corr.png, phi_vs_structure.png
```

See [`FINDINGS.md`](FINDINGS.md) for results.
