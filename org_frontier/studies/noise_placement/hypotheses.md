# Where the noise sits: party-side versus mediator-side errors on quorum hubs

Fixed before this study's computation.

## Gap

Every earlier noisy-quorum study (`quorum_noise_sweep`, `quorum_correlated_noise`, `shared_share_ties`,
`five_six_node_quorum_ties`) put the error in the mediator's readings; the parties copied the mediator
exactly. Here the error can sit on the party side instead: each party copies S but gets it wrong with
probability d, independently. This is the "parties that misread the mediator" item in
`five_six_node_quorum_ties/BACKLOG.md`.

## Model

Three parties; S commits OR3 or MAJ3 over its readings; party i's next state is S with probability 1 − d
and ¬S with probability d. Three placements of noise at rate r:

- **mediator**: S misreads each party independently with probability r (probe 464 `input_tpm`); parties exact.
- **party**: S reads exactly; each party flips its copy with probability r.
- **both**: S misreads with probability r and parties flip with probability r.

r ∈ {0, 0.05, 0.1, 0.2, 0.4}; OR3 and MAJ3; 30 cases. For each reachable state, φ of every subset from
`new_big_phi.reachable_subsystems`; whole Φ = maximum full-group φ over states; top tie set = subsets within
1e-9 of the largest subset φ, at the state where it occurs.

Controls: at r = 0 all three placements give the deterministic TPM (1e-12); `mediator` equals probe 464's
`input_tpm` (1e-12) and reproduces MAJ3 whole Φ 0.026981 at r = 0.1 (1e-6).

## Outcomes (threshold 1e-9)

- H1: under `party` noise, MAJ3 whole Φ ≤ 1e-9 at every rate.
- H2: under `both`, MAJ3 whole Φ > 1e-9 at every nonzero rate.
- H3: under `party` noise, OR3's full group is in the top tie set at every nonzero rate.
- H4: for MAJ3, the full group is never in the top tie set at any nonzero rate under any placement.
