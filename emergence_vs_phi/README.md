# Causal emergence vs IIT Φ

Two information-theoretic accounts of macro-level causal power, compared head to
head on the same small systems:

- **Effective information (EI)** and **causal emergence** — [Hoel](https://www.mdpi.com/1099-4300/19/5/188)'s
  framework. EI measures the determinism and non-degeneracy of a system's causal
  structure under a uniform intervention; **causal emergence** occurs when a
  *coarse-grained* (macro) description has higher EI than the micro system.
- **Integrated information Φ** — [IIT 4.0](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1011465),
  the irreducible intrinsic cause-effect power of the system, computed exactly
  with PyPhi.

EI is the historical precursor of Φ (Φ is effective information across the
minimum partition), but causal emergence and integration are rarely measured on
the same systems. This experiment asks: **do they agree? where do they diverge?**

## Measures (`emergence.py`)

All derived exactly from the state-by-state TPM:

- `effective_information(P)` — `H(E_bar) − mean_s H(P[s])`, the EI under a
  uniform intervention (Hoel). Maximal (`log2 N`) for a deterministic,
  non-degenerate system; 0 for a fully degenerate one.
- `macro_tpm(P, groups)` — the macro TPM for a coarse-graining, assuming a
  uniform distribution over micro states within each macro state (Hoel 2013).
- `causal_emergence(P)` — `max_φ EI_macro(φ) − EI_micro` over **all** state
  coarse-grainings φ (exhaustive for n=3: Bell(8)=4140 partitions). ≥ 0 by
  construction; > 0 when some macro scale has stronger effective information.

These are unit-checked: EI of a deterministic permutation = `n` bits, EI of a
fully degenerate system = 0, CE ≥ 0, and CE > 0 is detected on noisy networks.

## Design

Restricted to **n = 3** networks (where the emergence search is exact and
tractable), swept across connectivity density and noise `{0, 0.1, 0.2, 0.35}` —
emergence requires indeterminism, so higher noise levels are included. Exact
IIT-4.0 Φ (mean over reachable states) via PyPhi.

## Reproduce

```bash
python -m emergence_vs_phi.run 15 1     # -> results/emergence.csv
python -m emergence_vs_phi.analyze       # -> summary.csv, emergence_vs_phi.png
```

See [`FINDINGS.md`](FINDINGS.md) for results.
