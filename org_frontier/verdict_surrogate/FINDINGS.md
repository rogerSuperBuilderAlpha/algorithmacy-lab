# Findings — a learned surrogate recovers the coordination verdict, and ranks it past the size ceiling

A learned combination of cheap features recovers the triadic/dyadic coordination verdict that exact Φ
gives, at AUC 0.99 within the exactly-labelable pool — far above the single-proxy ceiling that
`proxy_bridge/` hit (0.63). Trained only on n ≤ 5 and pointed at held-out forms it never saw, it still
*ranks* triads above dyads perfectly at n = 6 and n = 7 (AUC 1.0). What it does not do is carry its
decision threshold across the ceiling: the fixed probability cut calibrated at n ≤ 5 misses triads at
n = 7 and n = 8, so the surrogate survives as a top-k% screen that flags forms for exact Φ, not as a
standalone classifier. The residual errors are all one-sided — missed triads, never false alarms — and
they concentrate in the strongly-integrated conjunctive and chain forms at large n, a nameable region a
deferral rule cleans up completely. All four pre-registered claims are reported against their success
lines below, including the one whose predicted failure region was wrong.

The dataset: 1131 exactly-labelled forms at n ≤ 5 for training (69 triadic), a held-out 115-form test at
n = 6, 7, 8 (15 triadic), and a timing probe fixing the feasible oracle. Ground truth is exact IIT-4.0 Φ
over the MIP from `org_frontier.classifier.classify_rules`. No feature computes Φ.

## H1 — rescue. **Supported.**

*Pre-registered line: cross-validated AUC ≥ 0.85, above proxy_bridge's 0.63 and above the structural-only
heuristic; the gain comes from discounting the back-channel.*

The learned classifier reaches **AUC 0.99** on the n ≤ 5 pool. It clears the line and buries the
single-proxy ceiling:

| model | AUC |
|---|---|
| learned, all features | **0.99** |
| learned, structural features only | 0.972 |
| learned, dynamical features only | 0.942 |
| best single proxy (`causal_density`) | 0.80 |
| proxy_bridge reference (single dynamical proxy) | 0.63 |
| structural heuristic (hand rule) | 0.45 |

The back-channel discount is the mechanism the pre-registration named, and it holds. On the 256
back-channel forms — dyadic arrangements with a direct worker–counterpart edge that a single dynamical
proxy misreads as integration — the learned model calls the verdict at **0.93 accuracy** where the best
single proxy manages **0.61**. A structural fact the connectivity matrix exposes, invisible to a
trajectory proxy, is what the model learns to read.

**The honest qualifier.** Structural features alone already reach 0.972; the dynamical features add about
0.02. The signal is overwhelmingly structural — top importances are `density` (0.22), `causal_density`
(0.11), `n_reciprocal` (0.11) — so H1 passes, but the dynamical audit earns its place only at the margin.
The falsification condition ("clears 0.85 without beating structural-only") is not met: 0.99 > 0.972. It
is close.

## H2 — extrapolation. **Supported on the pre-registered lines, with a boundary the lines did not name.**

*Pre-registered lines: held-out AUC ≥ 0.75 at n = 6, and above chance at n = 7; the operative metric is
recall on the rare triadic class at a fixed top-k% screening budget.*

Trained only on n ≤ 5, the surrogate ranks the held-out forms cleanly:

| n | forms | triadic | AUC | fixed-cut recall | top-10% screen | top-20% screen |
|---|---|---|---|---|---|---|
| 6 | 95 | 5 | **1.00** | 0.60 | 1.00 | 1.00 |
| 7 | 15 | 5 | **1.00** | 0.00 | 0.40 | 0.60 |
| 8 | 5 | 5 | — | 0.00 | 0.20 | 0.20 |

Pooled held-out AUC is **1.0** (both the full feature set and the size-robust subset). Against the
pre-registered lines — AUC ≥ 0.75 at n = 6, above chance at n = 7 — H2 passes with room to spare.

But the AUC and the decision diverge, and that divergence is the finding. **Ranking extrapolates; the
threshold does not.** At n = 6 the top-20% screen catches all five triads and the fixed cut recovers
three of five. At n = 7 the ranking is still perfect (AUC 1.0) yet the fixed cut, calibrated on the
smaller n ≤ 5 systems, has drifted below every triad — recall collapses to zero even as the screen still
catches 60% in its top 20%. At n = 8 the held-out set is degenerate: all five landmark forms are triadic,
so no AUC is defined, and only one of five lands in the top 20%.

This mirrors `learned_surrogate`'s result on the lab's own object — detection extrapolates in size where
magnitude did not — and sharpens it: the verdict extrapolates *as a ranking*, and the surrogate is
therefore an honest **screen run at a fixed budget**, not a probability cut you can port across the
ceiling. Used as a top-20% pre-filter it catches every triad at n = 6 and most at n = 7; used as a fixed
classifier past n = 6 it silently drops them.

## H3 — an honest boundary. **Confirmed in spirit; the predicted region was wrong.**

*Pre-registered candidate region: near-threshold coupling and ambiguous back-channel forms.*

The errors do concentrate — 12 of 115 held-out forms, held-out accuracy **0.896** — and they concentrate
in a single, nameable place. But not the predicted one. Every one of the 12 errors is a **false negative,
a missed triad; there are zero false alarms.** They fall on the strongly-integrated forms, not the
ambiguous weak-coupling ones:

| construction | forms | errors |
|---|---|---|
| all_required | 6 | 5 |
| chain | 6 | 4 |
| substitutable | 3 | 3 |
| random_backchannel | 24 | 0 |
| random_strict | 76 | 0 |

The missed forms carry Φ up to 7.0 (median 3.5) — these are the *most* integrated held-out systems, not
near-threshold ones. The model under-scores them (error probabilities cluster just below the 0.5 cut,
median 0.40) because it never saw triads of that magnitude at n ≤ 5. So the pre-registered guess — errors
hide among ambiguous back-channels — is falsified; the real deferral region is the high-Φ conjunctive and
chain forms at large n.

The deferral rule the region licenses is clean. Abstain where the model is unsure and route those forms to
exact Φ:

| deferral band | abstain fraction | accuracy on decided | errors remaining |
|---|---|---|---|
| \|p − 0.5\| < 0.15 | 0.11 | 0.980 | 2 |
| \|p − 0.5\| < 0.25 | 0.15 | **1.00** | 0 |

Deferring the 15% of forms nearest the boundary sends every error to the exact instrument and leaves the
decided verdicts perfect. H3's spirit — a nameable region with an honest deferral rule — holds; its
specific pre-registered geography does not.

## H4 — altitude guard. **Held.**

No correctness claim is made above the feasible oracle (n > 8), where no exact ground truth exists. The
surrogate is reported throughout as a screen that flags forms for exact Φ, never a replacement. Exact Φ is
not demoted: the contribution is a cheap pre-filter that widens the range the exact instrument can be
pointed at, and — per H2 and H3 — one that must run as a top-k% budget with a deferral band, not as a
standalone cut.

## What this arm settled

Between `proxy_bridge/` (a single cheap proxy fails, AUC 0.63) and `foundations/learned_surrogate/` (a
learned combination detects generic Φ and extrapolates in size), this arm fills the unclaimed cell: a
learned combination, targeting the coordination verdict, on coordination-structured forms, tested past the
ceiling. The verdict is recoverable and the recovery is mostly structural. It extrapolates as a ranking,
degrades to a screen rather than a classifier past n = 6, fails one-sidedly toward caution (missed triads,
no false alarms), and admits a 15%-abstention deferral rule that restores exact-level accuracy on
everything it decides. The surrogate widens the reach of exact Φ; it does not retire it.

## Reproduce

```bash
# from the repo root, with the IIT-4.0 venv
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.build_dataset --max-n 5   # training pool
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.build_dataset --max-n 8   # held-out n=6,7,8 (slow; n=8 forms ~20 min each)
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.train          # H1  -> results/train.json, train.png
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.extrapolate    # H2  -> results/extrapolate.json
~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.boundary       # H3  -> results/boundary.json
```

Numbers above are read directly from `results/train.json`, `results/extrapolate.json`, and
`results/boundary.json`.
