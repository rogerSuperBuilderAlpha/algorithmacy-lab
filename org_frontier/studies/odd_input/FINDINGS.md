# P's value at the gate's odd input decides whether the whole is irreducible, but only weakly

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `a8886082` before computation. Control passed: andP_and reproduces `forcing_match` andP_and
(whole Φ = 2.000000).

## Setup

P reads R1, R2; R1' = P; R2' = C1; C1' = gate(P, G); G' = P.

| form | platform | gate | odd (P, G) | predicted | reachable states | whole Φ | states with whole φ > 0 | top φ | full bound | pooled top ties |
|---|---|---|---|---|---:|---:|---:|---:|---|---|
| andP_and | AND | P ∧ G | (1, 1) | (control) | 12 | 2.000000 | 2 | 2.000000 | yes | PR1, PR2C1, PR2C1G, PR1R2C1, PR1R2C1G |
| andP_p_notg | AND | P ∧ ¬G | (1, 0) | Φ > 0 | 12 | 0.415037 | 2 | 2.000000 | no | PR1 |
| andP_notp_g | AND | ¬P ∧ G | (0, 1) | Φ = 0 | 12 | 0.000000 | 0 | 2.000000 | no | PR1 |
| orP_p_or_notg | OR | P ∨ ¬G | (0, 1) | Φ > 0 | 12 | 0.415037 | 2 | 2.000000 | no | PR1 |
| orP_notp_or_g | OR | ¬P ∨ G | (1, 0) | Φ = 0 | 12 | 0.000000 | 0 | 2.000000 | no | PR1 |

In the control, whole φ is 2.0 in state (P, R1, R2, C1, G) = (1, 1, 1, 1, 1) and 0.415037 in
(1, 1, 1, 0, 1). In andP_p_notg it is 0.415037 in both of those states. In orP_p_or_notg it is 0.415037 in
(0, 0, 0, 0, 0) and (0, 0, 0, 1, 0).

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** andP_p_notg whole Φ = 0.415037.
- **H2 SUPPORTED.** andP_notp_g whole Φ = 0.
- **H3 SUPPORTED.** orP_p_or_notg whole Φ = 0.415037.
- **H4 SUPPORTED.** orP_notp_or_g whole Φ = 0.
- **P-value rule SUPPORTED; G-value rule REFUTED.**

## Reading

Where Φ > 0 at all, P's value at the gate's odd input pattern decides it, as predicted: for an AND
platform the odd pattern must have P = 1, for an OR platform P = 0. The rival rule based on G's value
fails on all four forms. The result is weaker than the AND–AND case, though. With the odd pattern off the
diagonal, whole Φ is 0.415037 rather than 2.0. The whole group never ties for top, and the relayed loop
PR2C1 drops out of the top tie set. Only the direct loop PR1 reaches 2.0. The AND and OR platform forms
give mirror-image numbers.

## What it means

When a go-between combines a platform's message with a switch the platform also controls, what matters is
how the go-between treats the platform's own message at its one sensitive point. If that matches what
the platform listens for (a "yes" for a "both" platform, a "no" for an "either" platform), the group stays
irreducible. The match is strongest when the switch is treated the same way as the message.

## Limits

Binary, deterministic, synchronous; n = 5; switch driven by P only; one gate per odd pattern and platform.
Ties at 1e-9.

## Reproduce

```sh
python org_frontier/studies/odd_input/run.py --quick   # CI subset, ~10 s
python org_frontier/studies/odd_input/run.py --write   # full run, ~18 s
```

An AI assistant working as the open harness around IIT 4.0/PyPhi wrote the script and this report; every
number is printed by `run.py` or stored in `results/results.json`. No human review is claimed.
