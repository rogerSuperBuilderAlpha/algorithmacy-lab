# Findings: high_noise_tie_onset

Hypotheses were committed (c68fdb4a) before computing. Values seen beforehand: the η = 0.3 and 0.4 results
of `tie_set_membership` and `placement_equality` only.

## Scores

- **H1 SUPPORTED.** Each form has one switch rate. OR3: full group unique top at 0.31–0.35, tie set = all 7
  subsets containing S at 0.36–0.39. ANY4: unique at 0.31–0.32, all 15 subsets containing S at 0.33–0.39.
- **H2 REFUTED.** OR3 switches at 0.36, ANY4 at 0.33.
- **H3 SUPPORTED.** Below the switch the top sits at the all-zero state (0000 / 00000); from the switch
  upward it sits at S = 0 with every party 1 (0111 / 01111), tied with all-ones (1111 / 11111).

## Exact numbers

| form | η | whole Φ | top states | ties |
|---|---|---|---|---|
| OR3 | 0.35 | 0.311846 | 0000 | 1 (SP1P2P3) |
| OR3 | 0.36 | 0.026429 | 0111, 1111 | 7 |
| ANY4 | 0.32 | 0.379397 | 00000 | 1 |
| ANY4 | 0.33 | 0.008841 | 01111, 11111 | 15 |

## Why the switch is sharp (descriptive, added after scoring)

After scoring, run.py was extended to print the raw full-group φ PyPhi returns at two states, without the
`> 1e-9` filter the earlier studies used. At the all-zero state it falls smoothly and then jumps to a
negative value at exactly the switch rate:

- OR3 all-zero: 0.457943 (0.31) … 0.345459 (0.34), 0.311846 (0.35), **−0.181471** (0.36), −0.138200 (0.39).
- ANY4 all-zero: 0.421308 (0.31), 0.379397 (0.32), **−0.184887** (0.33), −0.105020 (0.39).
- The S = 0, parties = 1 state changes smoothly throughout (OR3 0.026593 → 0.024355; ANY4 0.008189 → 0.009532).

So the "cliff" in max whole Φ is not a gradual crossover between two states. It is the all-zero state's
φ changing sign in PyPhi's output, which drops that state out of the running. A negative φ is outside what
IIT 4.0 defines as a meaningful Φ value; we report it as PyPhi's output and do not interpret it. Earlier
studies that filtered states at `> 1e-9` would have silently hidden such values.
