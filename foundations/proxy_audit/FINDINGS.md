# Findings: cheap proxies do not track exact IIT‑4.0 Φ

**TL;DR.** Across 270 small random networks where exact IIT‑4.0 Φ is computable,
**no cheap proxy reliably tracks integrated information.** The canonical
empirical proxies (Lempel‑Ziv complexity, pairwise correlation) are essentially
uninformative; total correlation is *anti*‑correlated with Φ; and the single
best detector of "is this system integrated at all?" is the trivial **edge
count**. This quantitatively supports the critique of
[Barrett et al. (2026)](https://consensus.app/papers/details/64009340648f5403bda7a94fb6a62950/)
that what is computed on data are proxies that have never been validated against
the quantity IIT actually defines.

## Main result

Ensemble: 270 networks, `n ∈ {3,4}`, swept over connectivity density and noise
(seed 1). 72 networks had Φ>0; Φ ranged 0.000–2.000.

| Proxy | Spearman ρ (vs Φ) | Pearson r | AUC (detect Φ>0) |
|-------|------:|------:|------:|
| Total correlation | **−0.355** | −0.136 | **0.278** |
| Stochastic interaction | +0.135 | +0.220 | 0.575 |
| LZ complexity | +0.129 | −0.044 | 0.569 |
| Mean \|pairwise corr\| | −0.070 | −0.005 | 0.446 |
| Number of edges | +0.295 | −0.086 | 0.638 |

Read AUC as: 0.5 = chance, 1.0 = perfect, <0.5 = anti‑predictive. The strongest
association of any proxy with Φ is total correlation — and it points the *wrong
way* (more statistical integration → less IIT integration). LZ complexity, the
workhorse "neural complexity" proxy in consciousness research, is barely above
chance at even detecting Φ>0 (AUC 0.569).

## Robustness

**By system size** — the pattern holds, and total correlation's anti‑correlation
strengthens with size:

| Proxy | ρ (n=3) | ρ (n=4) | AUC n=3 | AUC n=4 |
|-------|----:|----:|----:|----:|
| Total correlation | −0.280 | −0.457 | 0.321 | 0.228 |
| Stochastic interaction | +0.175 | +0.107 | 0.593 | 0.583 |
| LZ complexity | +0.049 | +0.204 | 0.539 | 0.602 |
| Number of edges | +0.296 | +0.453 | 0.716 | 0.695 |

**Independent replication** (seed 99, 216 networks): same qualitative picture —
all \|ρ\| ≤ 0.26, total correlation negative (ρ=−0.137, AUC 0.395), stochastic
interaction the best graded tracker (ρ=+0.183), edge count the best detector
(AUC 0.647).

**The relationships are non‑monotonic.** Restricting to integrated systems
(Φ>0) and asking how well a proxy grades *how much* Φ, several proxies **flip
sign** relative to the full ensemble:

| Proxy | ρ (all) | ρ (among Φ>0) |
|-------|----:|----:|
| Total correlation | −0.355 | +0.059 |
| LZ complexity | +0.129 | −0.348 |
| Number of edges | +0.295 | **−0.478** |

Edge count is the *best* discriminator of Φ>0 yet, among integrated systems,
*more* edges means *less* Φ. So a proxy that looks useful for one question is
misleading for the other. Integrated information is not a monotone function of
any of these proxies.

## Interpretation

- **The proxies measure the wrong thing.** Total correlation and pairwise
  correlation capture *statistical* interdependence at stationarity; IIT‑4.0 Φ
  captures *intrinsic, irreducible cause–effect power* in a specific state.
  These come apart — strongly, and sometimes with opposite sign.
- **LZ complexity ≠ integration.** A high‑complexity (random‑looking) trajectory
  can come from a near‑disconnected noisy system with Φ=0, while a deterministic
  integrated system produces a low‑complexity trajectory. LZ tracks
  signal *diversity*, not integration.
- **The most predictive feature is structural, not informational.** That a crude
  edge count out‑detects every information‑theoretic proxy suggests these proxies
  add little over "is the system densely coupled?" — and even that relationship
  reverses for graded Φ.

## Caveats

- Small systems only (`n ∈ {3,4}`); behavior on large/real systems is exactly
  what cannot be checked against exact Φ, and is not claimed here.
- A specific ensemble (Boolean‑gate networks). Other dynamics may differ.
- We audit IIT‑4.0 **system‑level** Φ summarized as the mean over reachable
  states; proxies might track other IIT quantities (e.g. the full Φ‑structure)
  better. That is a natural follow‑up.
- Proxies were taken in standard forms; tuned or state‑specific variants might
  do better.

## Reproduce

See `README.md`. `python -m foundations.proxy_audit.run 15 1 && python -m foundations.proxy_audit.analyze`.
