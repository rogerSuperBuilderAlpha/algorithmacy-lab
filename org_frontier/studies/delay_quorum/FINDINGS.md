# A relay between the mediator and the parties cuts "any yes" and "all yes" to a third; a noisy majority does not notice

Exact IIT 4.0 Φ (PyPhi pin `b78d0e342`), every reachable subset in every reachable state. Hypotheses
pushed in `83ea99e2` before computation. Controls passed: d = 0 reproduces the deterministic hub TPM and
probe 464's `input_tpm` (1e-12) and the known whole Φ (OR3 3.0, AND3 3.0, MAJ3 0 at r = 0; MAJ3 0.026981
at r = 0.1).

## Setup

Mediator S commits OR3, MAJ3 or AND3 over the parties' current bits, misreading each party with
probability r. Its decision passes down d relays (S → B1 → … → Bd, exact copies) and every party copies
the last relay. d ∈ {0, 1, 2}; r ∈ {0, 0.1}; 18 cases, up to 6 nodes; ~20 min.

## Whole Φ (all nodes, relays included) and the top unit

| form | r | d = 0 | d = 1 | d = 2 | top unit at d ≥ 1 |
|---|---:|---:|---:|---:|---|
| OR3 | 0 | 3.000000 | 1.000000 | 1.000000 | S + one party + relays (2.0); at d = 2 tied with S + two parties + relays |
| AND3 | 0 | 3.000000 | 1.000000 | 1.000000 | same as OR3 (2.0) |
| MAJ3 | 0 | 0 | 0 | 0 | none |
| OR3 | 0.1 | 1.854569 | 0.729000 | 0.729000 | S + one party + B1 (1.347190); at d = 2, S + two parties + relays (1.458000) |
| AND3 | 0.1 | 1.854569 | 0.729000 | 0.729000 | same as OR3 (1.347190; 1.458000) |
| MAJ3 | 0.1 | 0.026981 | 0.026981 | 0.026981 | S + one party (+ relays) (0.107922) |

At d = 0 the full group is the top unit for OR3 and AND3; at every d ≥ 1 it is not. OR3 and AND3 give
identical numbers in every cell. Reachable states: 4, 8, 16 for d = 0, 1, 2. Full data:
[results/results.json](results/results.json).

## Scores

- **H1 SUPPORTED.** Noise-free OR3 and AND3 stay whole-system irreducible at every d (Φ 1.0 at d ≥ 1).
- **H2 SUPPORTED.** Noise-free MAJ3 whole Φ 0 at every d.
- **H3 SUPPORTED.** Noisy MAJ3 whole Φ > 0 at every d, and in fact unchanged: 0.026981 at d = 0, 1, 2,
  with the same top φ 0.107922.
- **H4 SUPPORTED.** Noise-free OR3 whole Φ falls from 3.0 (d = 0) to 1.0 (d = 1).
- **H5 SUPPORTED.** At d = 1 the full system is not in OR3's top tie set; the top units are {S,Pi,B1}
  at φ 2.0.

Descriptive: unlike `commit_response_delay` on the conjunctive triad (Φ 2 → 1 → 2 → 2 for d = 0…3),
OR3 and AND3 do not recover at d = 2 (1.0 at both d = 1 and d = 2). With noise, the whole-system value
at d = 1 and 2 is 0.729000 = 0.9³ to six decimals; we have not derived why.

## Limits

Three-party yes/no hubs; one shared relay chain (not one per party); exact relays; d ≤ 2; one noise
rate; tie cutoff 1e-9.
