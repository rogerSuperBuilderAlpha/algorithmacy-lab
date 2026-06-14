# Q9 — Timescale separation: findings

A slow mediator over fast parties, swept by timescale ratio k=1…6 on the corpus anchor
two_sided_match (W'=S, S'=W∧C, C'=S). Two slow-commit models: deterministic hold-for-k and
probabilistic 1/k. Verdict read off Φ_MIP at PHI_EPS=1e-9. Instrument control passed: both
constructions reduce to the synchronous map at k=1, triadic, Φ_MIP=2.000000, MIP {W,SC}, state
(1,1,1), the Probe 57/62 anchor.

## Headline

Timescale separation flips the verdict rather than only shrinking Φ (H1). The slow mediator
becomes the core instead of dropping out of it. Holding S turns it into a self-absorbed {S}
core, the #43 sticky-mediator direction, and the parties factor out (H2). The flip is real and
clean, and the predicted membership shift is wrong.

## Results

| H | Claim | Verdict | Key numbers |
|---|---|---|---|
| H1 | Slow mediator flips the verdict at a finite interior k*, beyond a magnitude grade | **confirmed** | hold-for-k Φ_MIP(k=1…6)=2.0,0,0,0,0,0; k*_det=2; genuine zero-crossing, dyadic & stays for k=3…6 |
| H2 | At the flip the core sheds S → {W,C} | **refuted** | core {W,S,C}@k=1 → {S}@k≥2, state 000, φ_s=1.0 > φ_wc=0.0; core never {W,C}; #43 direction |
| H3 | hold-for-k and prob-1/k disagree on the verdict | **confirmed** | det flips k*_det=2; prob Φ_MIP=2.0,0.271,0.138,0.092,0.069,0.055, all triadic, k*_prob=none |
| H4 | k* tracks the synchronous attractor period | **refuted** | gig_false_dyad (P=1) k*_det=2; two_sided_match (P=2) k*_det=2; period-independent |
| H5 | Clock-stretching factors by a different fingerprint than #62 sequential | **confirmed (band only)** | hold & 6 sequential orders & grain-2 all Φ_MIP=0, MIP "None" @000; only discriminator: hold dyadic over contiguous band k=2…6 |

## Through-line

The flip is solid (H1) and clean, with Φ_MIP going to exactly 0 and staying dyadic above
k*_det=2, while its mechanism runs opposite to the framework's update-grain prediction. The
Intrinsic Units exclusion logic says a slow unit should drop below the fast pair. The held
mediator instead becomes a self-referential memory device and the core collapses onto {S}. Soft
clock-inertia and the hard OR-stick of #43 reach the same place. The construction is load-bearing:
the deterministic hold flips, the probabilistic 1/k commit never does (H3), so any verdict claim
must name its slow-commit model. The flip is period-independent (H4), and clock-stretching shares
#62's MIP cut and zero residual, differing only in holding over a contiguous ratio band where #62
holds at discrete within-step orderings (H5).

## Numbers trace to

- results/q9_h1_hold_verdict_flip.csv (H1)
- results/h2_hold_membership.csv (H2)
- results/construction_split.csv (H3)
- results/q9_period_lock.csv (H4)
- results/probe_factorization_fingerprint.csv (H5)

Probes: probe_hold_verdict_flip.py, probe_hold_membership.py, probe_construction_split.py,
probe_period_lock.py, probe_factorization_fingerprint.py.
