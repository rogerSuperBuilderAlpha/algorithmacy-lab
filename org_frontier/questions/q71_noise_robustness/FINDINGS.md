# Q71 findings — noise robustness of the outreach verdict

All four hypotheses confirmed. The verdict is robust: it degrades gracefully and noise never manufactures
a spurious triad.

| epsilon | read_recipient Φ | broadcast Φ |
|---|---|---|
| 0.00 | 2.0000 | 0.0000 |
| 0.05 | 1.5334 | 0.0000 |
| 0.10 | 1.1554 | 0.0000 |
| 0.20 | 0.6106 | 0.0000 |
| 0.30 | 0.2769 | 0.0000 |
| 0.50 | 0.0000 | 0.0000 |

| H | Result | Verdict |
|---|--------|---------|
| H1 triad survives small noise | Φ=1.53 at eps=0.05, 1.16 at 0.10 | confirmed |
| H2 Φ degrades monotonically | strictly decreasing in epsilon | confirmed |
| H3 maximal noise collapses the triad | Φ=0 at eps=0.5 | confirmed |
| H4 no spurious triad from noise | broadcast Φ=0 throughout | confirmed |

From `probe_noise_robustness.py`.

## What it says

The triadic verdict is robust to stochastic update, not a knife-edge of the deterministic model. The
read-recipient triad keeps positive Φ through moderate noise and falls smoothly toward zero as every
update becomes a coin flip, with no threshold cliff: Φ is a graded, monotone function of the flip
probability. The dyadic broadcast stays at Φ = 0 at every noise level, so noise never manufactures
irreducibility where the deterministic structure had none. The verdict the program reads survives
perturbation in the direction that matters: a small amount of real-world noise leaves a triadic
coordination triadic, and no amount of noise turns a broadcast into a triad.

## Caveats

- **Confirmatory.** The robustness predictions held; none was refuted.
- **In-silico.** Boolean models perturbed by symmetric flip-noise; other noise models (correlated,
  asymmetric) are untested. Φ read ordinally; the smooth decay is a robustness signature, not a difficulty
  scale.
- **One triad.** The read-recipient triad and the broadcast are tested; other forms in the corpus follow
  the same machinery but are untested here.
