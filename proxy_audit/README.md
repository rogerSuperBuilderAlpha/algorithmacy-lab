# Proxy audit: do cheap measures track exact IIT‑4.0 Φ?

**Question.** A 2026 review of Integrated Information Theory ([Barrett et al.,
*IIT: the good, the bad and the misunderstood*](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/))
makes a pointed claim: Φ has never been computed on a real physical system, and
what people actually compute on data are **proxies** (Lempel‑Ziv complexity,
PCI, correlation measures), **not approximations** — with no systematic check of
whether those proxies track the integrated information that IIT actually
defines.

This experiment runs that check on systems small enough to compute exact Φ. We
generate an ensemble of small discrete networks, compute their **exact IIT‑4.0
integrated information** with [PyPhi](https://github.com/wmayner/pyphi), and ask
how strongly several cheap, polynomial‑time proxies correlate with it.

## What is compared

**Ground truth — exact IIT‑4.0 Φ** (`exact_phi.py`).
System‑level big‑Φ via `pyphi.new_big_phi.sia`, evaluated over a network's
reachable states. Because Φ is state‑dependent while the proxies are
system‑level, we summarize each network by the **mean (and max) exact Φ over its
reachable states**. A negative system Φ means the system is *reducible* (not an
integrated complex) and is clamped to 0, matching IIT's treatment of complexes.

**Proxies** (`proxies.py`), all computed without IIT's exponential machinery:

| Proxy | Type | Definition |
|-------|------|-----------|
| Total correlation | static | multi‑information of the stationary distribution |
| Stochastic interaction | dynamic | Ay (2001): `Σᵢ H(Xᵢ,ₜ\|Xᵢ,ₜ₋₁) − H(Xₜ\|Xₜ₋₁)` |
| LZ complexity | dynamic | normalized Lempel‑Ziv (LZ76) of a simulated trajectory |
| Mean \|pairwise corr\| | dynamic | mean absolute pairwise correlation of node activity |
| Number of edges | structural | a trivial connectivity baseline |

## Ensemble (`networks.py`)

Random binary networks of `n ∈ {3, 4}` nodes. Each node updates as a (possibly
noisy) Boolean gate (OR / AND / PARITY / MAJORITY / COPY) of its inputs. We
sweep connectivity density `{0.3, 0.5, 0.8}` and noise `{0.0, 0.05, 0.2}` to
span sparse↔dense and deterministic↔noisy regimes, which produces a broad range
of Φ.

## Reproduce

```bash
# from the pyphi-experiments/ directory, with the IIT-4.0 venv:
python -m proxy_audit.run 15 1      # per_cell=15, seed=1  -> results/audit.csv
python -m proxy_audit.analyze        # -> correlation table, summary.csv, plot
```

Outputs land in `results/`:
- `audit.csv` — one row per network (exact Φ + every proxy + metadata)
- `summary.csv` — Spearman ρ, Pearson r, and AUC(Φ>0) for each proxy
- `proxy_vs_phi.png` — scatter grid of each proxy against exact Φ

## Interpreting the output

For each proxy we report:
- **Spearman ρ** — does the proxy *rank* networks by Φ correctly?
- **Pearson r** — linear association.
- **AUC(Φ>0)** — can the proxy *detect* integrated systems (Φ>0) at all?

See `FINDINGS.md` for the results and discussion.
