# Recovery speed after a nudge does not track Φ; the number of resting patterns does

Hypotheses pushed in `ac0bf6f3` before computation. Φ values are the committed ones from
`memory_rules` (36 cases, 13 with whole Φ > 0) and `update_order_quorum` (72 cases, all whole Φ 0); this
study computes only the dynamics of the same deterministic TPMs. Control: the synchronous OR3 hub has 3
attractors on 4 states (all-0, all-1, and a 2-cycle).

## Measures

- **recovery**: from each attractor state, flip one party's bit; steps until on an attractor again;
  mean over attractor states × 3 parties.
- **same-attractor rate**: share of those flips that return to the starting attractor.
- **transient**: mean steps from each of the 16 start states to an attractor.

## Results (memory_rules: 13 whole Φ > 0 vs 23 whole Φ = 0)

| measure | median, Φ > 0 | median, Φ = 0 | test | p |
|---|---:|---:|---|---:|
| recovery | 1.0 | 1.0 | one-sided, shorter for Φ > 0 | 0.970 |
| same-attractor rate | 0.5 | 0.125 | one-sided, higher for Φ > 0 | 0.087 |
| transient | 0.75 | 0.75 | two-sided | 0.628 |
| attractors (exploratory) | 2 | 5 | two-sided | 0.0031 |

Across all 108 cases, Spearman(recovery, top subset φ) = **+0.368** (p = 9.1e-5): longer recovery goes
with a *higher* top φ, the opposite sign from H3. In `update_order_quorum`, recovery is 1.0 in 48
orders (top φ 0, 1 or 6), 1.1667 in 12 (top φ 2) and 1.3333 in 12 (top φ 6).

Full data: [results/results.json](results/results.json).

## Scores

- **H1 REFUTED.** Recovery is not shorter for whole Φ > 0 (medians 1.0 and 1.0; p 0.970).
- **H2 REFUTED.** The same-attractor rate is higher for whole Φ > 0 (0.5 vs 0.125) but p = 0.087.
- **H3 REFUTED.** The rank correlation is positive (+0.368), not negative.
- **H4 SUPPORTED.** Transient length does not separate the classes (p 0.628), replicating
  `ergodic_settling_time`'s null on a different panel.

Exploratory, not pre-registered: whole Φ > 0 cases have fewer attractors (median 2 vs 5, two-sided
p = 0.0031). That fits the higher same-attractor rate (0.5 vs 0.125), which itself
did not reach p < 0.05.

## Limits

Deterministic TPMs only; 36 cases in the class contrast; one flip at a time; the Φ classes come from
two earlier studies, so the panel is not a random sample of forms. The attractor-count contrast was
found after looking and needs its own pre-registered test.
