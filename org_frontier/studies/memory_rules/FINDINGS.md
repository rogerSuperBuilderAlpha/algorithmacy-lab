# No deterministic memory rule binds a majority; the wrong one-way memory breaks "any yes" and "all yes"

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `aae69f80` before computation. Controls passed: copy/plain reproduces the deterministic hub TPM
(1e-12) and the known whole Φ (OR3 3.0, MAJ3 0, AND3 3.0).

## Setup

Mediator S over three parties, deterministic, no noise. Base rule OR3, MAJ3 or AND3. Each party's next
state reads S and its own last bit: **copy** (S), **and** (S AND own), **or** (S OR own), **toggle**
(S XOR own). The mediator is **plain** (rule over the parties), **toggle** (rule XOR own last bit) or
**vote** (its own last bit counted as a fourth vote, quota + 1). 36 cases, ~24 s.

### Whole Φ (top tie set at the peak state in brackets when the full group is not in it)

| form | mediator | copy | and | or | toggle |
|---|---|---:|---:|---:|---:|
| OR3 | plain | 3.000000 | 0 [SP1: 2.0] | 3.000000 | 3.000000 |
| OR3 | toggle | 3.000000 | 0 [SP1: 2.0] | 3.000000 | 1.500000 |
| OR3 | vote | 0 [SP1P2,SP1P3,SP2P3: 0.077058] | 0 [SP1: 2.0] | 0 [SP2,SP3,SP2P3: 2.0] | 0 [SP2,SP3,SP2P3: 2.0] |
| MAJ3 | plain | 0 [none] | 0 [SP1,SP2,SP1P2: 2.0] | 0 [SP2,SP3,SP2P3: 2.0] | 0 [SP2,SP3,SP2P3: 2.0] |
| MAJ3 | toggle | 0 [S: 1.0] | 0 [SP1,SP2,SP1P2: 2.0] | 0 [SP2,SP3,SP2P3: 2.0] | 0 [SP2,SP3: 1.0] |
| MAJ3 | vote | 0 [SP1P2,SP1P3,SP2P3: 0.077058] | 0 [SP1,SP2,SP1P2: 2.0] | 0 [SP3: 2.0] | 0 [SP2,SP3,SP2P3: 2.0] |
| AND3 | plain | 3.000000 | 3.000000 | 0 [SP3: 2.0] | 3.000000 |
| AND3 | toggle | 3.000000 | 3.000000 | 0 [SP3: 2.0] | 0 [S,P1,P2,P3 singly: 1.0] |
| AND3 | vote | 3.000000 | 3.000000 | 0 [P1,P2,P3: 1.0] | 0 [P1,P2,P3: 1.0] |

Full group in the top tie set, out of 12 form × party cells: plain 6, toggle 5, vote 2.
Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** MAJ3 with a plain mediator has whole Φ 0 under every party rule. In fact MAJ3 has
  whole Φ 0 in all 12 of its cells; units containing S and one or two parties reach φ 2.0 under and/or/toggle parties.
- **H2 REFUTED.** A toggling mediator does not bind MAJ3 (whole Φ 0); {S} alone is the top unit (1.0).
- **H3 REFUTED.** OR3 with and-memory parties, and AND3 with or-memory parties, have whole Φ 0 (top units {S,P1} and {S,P3} at 2.0). OR3 and AND3 stay at 3.0 under the other party rules.
- **H4 REFUTED.** A mediator that counts its own vote does not bind MAJ3 (whole Φ 0; top trios 0.077058).
- **H5 SUPPORTED.** 6 (plain) > 5 (toggle) and 6 > 2 (vote).

Descriptive, not pre-registered:

- The breaking party memory is the one that latches the value the rule does *not* wait for: "any yes"
  breaks when a party, once at no, can never return to yes on its own (and); "all yes" breaks when a
  party, once at yes, can never drop (or). We have not derived why.
- The self-voting mediator turns OR3 into "2 of 4 including myself" and drops it to 0 with every party
  rule; for AND3 it is "all 4 including myself" and keeps 3.0 with copy and and parties.
- With toggling parties and a toggling mediator, OR3 halves (3.0 → 1.5) and AND3 falls to 0.

## Limits

Three-party yes/no hubs, deterministic, no noise; one memory rule shared by all parties; four party
rules and three mediator rules; tie cutoff 1e-9.
