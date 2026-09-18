# Conjunctive law on real Boolean renders — findings

**Verdict: LAW_ONLY_UNDER_STRONG_MODEL.** The conjunctive Φ = n−1 law
(#116) is **not** visible as a scaling law in institutional or fitted
OSS Boolean renders. It appears only when `#116` hub wiring is imposed
on the same role counts.

Exact binary IIT-4.0. Datasets: committed `recurrence/` PyPhi /
scikit-learn / Kubernetes CSVs. Hypotheses fixed in `hypotheses.md`.
#43 / #44 pointers only.

## Signature

Major-complex Φ ≈ n−1 **and** \|core\| = n. The n=3 Φ=2 full-core triad
is noted but does **not** clear the H1 bar alone.

## Renders tried

| slug | modeling | n | MC Φ | \|core\| | n−1 | SIG |
|---|---|---|---|---|---|---|
| synth_hub (control) | control | 3,4 | 2,3 | 3,4 | 2,3 | yes |
| pyphi_v9_triad | institutional | 3 | 2.0 | 3 | 2 | yes* |
| sklearn_v10_fourrole | institutional | 4 | 2.0 | 3 | 3 | **no** |
| k8s_v11_prow | institutional | 4 | 2.0 | 3 | 3 | **no** |
| pyphi_v8_fit_core | fitted | 3 | 1.0 | 1 | 2 | **no** |
| forced_hub_n3/n4 | **strong** | 3,4 | 2,3 | 3,4 | 2,3 | yes |

\*n=3 triad match only — not scaling evidence.

## Hypotheses

| H | result |
|---|---|
| H1 real render shows law | **REFUTED** |
| H2 null everywhere | **REFUTED** (strong hub recovers) |
| H3 only under strong modeling | **SUPPORTED** |

## Reading

Real governance elicits deeper or looser cores (author out; bot in as
relay) that sit at Φ=2 with \|core\|<n at n=4. The all-required hub that
carries Φ=n−1 is a modeling choice, not what the institutional rules
encode. No worker measured; renders are elicited/fitted models of OSS
event CSVs.

## Best next

**#46** formal-vs-informal coordination cut.

## Reproduce

```
python org_frontier/studies/conjunctive_law_real_render/analyze_render.py
```
