# A slow mediator never makes a majority irreducible; slow parties make a noisy one more so

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `237dc499` before computation. Controls passed: λ = 0 gives the deterministic TPM at r = 0 and
probe 464's `input_tpm` at r = 0.1 (1e-12); MAJ3 whole Φ at λ = 0, r = 0.1 is 0.026981 (noise_placement).

## Setup

Three parties, mediator S commits OR3 or MAJ3, optionally misreading each party with probability r. Each
lazy node keeps its last state with probability λ, else updates as usual. Laziness on the **mediator**, the
**party** side, or **all** four nodes; λ ∈ {0, 0.1, 0.25, 0.5, 0.75}; r ∈ {0, 0.1}; 60 cases, ~62 s.
`all` at λ = 0.75 is the per-node marginal of one-at-a-time random update (each of four nodes picked with
probability 1/4). "Top" is the largest subset φ over states; ties are listed at the state where it occurs.

### Whole Φ

| form | r | placement | λ=0 | 0.1 | 0.25 | 0.5 | 0.75 |
|---|---:|---|---:|---:|---:|---:|---:|
| OR3 | 0 | mediator | 3.000000 | 1.314391 | 0.560207 | 0.184461 | 0.056983 |
| OR3 | 0 | party | 3.000000 | 2.584905 | 2.002920 | 1.106767 | 0.406460 |
| OR3 | 0 | all | 3.000000 | 1.408158 | 0.733059 | 0.368922 | 0.195650 |
| OR3 | 0.1 | mediator | 1.854569 | 0.814415 | 0.351372 | 0.119111 | 0.038026 |
| OR3 | 0.1 | party | 1.854569 | 1.854569 | 1.482943 | 0.907687 | 0.383362 |
| OR3 | 0.1 | all | 1.854569 | 0.887603 | 0.472844 | 0.247948 | 0.136619 |
| MAJ3 | 0 | mediator / party / all | 0 | 0 | 0 | 0 | 0 |
| MAJ3 | 0.1 | mediator | 0.026981 | 0.026981 | 0.026981 | 0.026981 | 0.003744 |
| MAJ3 | 0.1 | party | 0.026981 | 0.029593 | 0.034237 | 0.043729 | 0.053014 |
| MAJ3 | 0.1 | all | 0.026981 | 0.024485 | 0.021635 | 0.018110 | 0.013277 |

### Where the top sits (r = 0)

| form | placement | full group top up to | top after that |
|---|---|---|---|
| OR3 | mediator | λ = 0.25 | {S} alone (0.415037 at 0.5, 0.678072 at 0.75) |
| OR3 | party | λ = 0.5 | a single party (0.750000 at 0.75) |
| OR3 | all | λ = 0 only | {S,P1} at 0.1 (1.620000), single nodes from 0.5 |
| MAJ3 | mediator | never | {S} alone (0.042718 at 0.1 → 0.677479 at 0.75) |
| MAJ3 | party | never | trios {S,Pi,Pj} (1.505053 at 0.1), a single party at 0.75 |

Full data: [results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Noise-free MAJ3 with lazy parties: whole Φ 0 at every λ, though trios {S,Pi,Pj} bind
  (top 1.505053 at λ = 0.1).
- **H2 REFUTED.** A lazy mediator does not make noise-free MAJ3 integrated: whole Φ 0 at every λ. The
  mediator's self-loop makes {S} alone the top unit (φ 0.042718 at λ = 0.1 up to 0.677479 at 0.75).
- **H3 SUPPORTED.** Noise-free OR3 under `all`: 3.000000 → 1.408158 → 0.733059 → 0.368922 → 0.195650.
- **H4 SUPPORTED.** At the one-at-a-time marginal (`all`, λ = 0.75) OR3 stays triadic (whole Φ 0.195650),
  unlike #62's deterministic sequential update (6/6 orders dyadic on the conjunctive form).
- **H5 SUPPORTED.** MAJ3's full group is never in the top tie set at any λ > 0.

Descriptive, not pre-registered:

- With mediator noise r = 0.1, the lazy mediator leaves MAJ3 whole Φ at 0.026981 to six decimals for
  λ = 0.1, 0.25 and 0.5, then drops to 0.003744 at 0.75. We have not derived why.
- Lazy parties raise noisy MAJ3 whole Φ with λ (0.026981 → 0.053014 at 0.75); lazy everyone lowers it
  (→ 0.013277).
- OR3 with r = 0.1 and lazy parties at λ = 0.1 equals the λ = 0 value (1.854569) to six decimals.
- Under laziness the parties' memory makes all 16 states reachable (4 without it, and with a lazy
  mediator alone).

## Limits

Three-party yes/no hubs; laziness is independent per node and the same λ for every lazy node; the exact
one-at-a-time update (not conditionally independent) is not computed; five λ values; tie cutoff 1e-9.
