# Delay on quorum hubs: the decision reaches the parties through a relay chain

Fixed before this study's computation.

## Gap

`commit_response_delay` put a transport delay (a chain of buffer nodes) between the mediator and the
parties on the conjunctive triad only, noise-free. `memory_rules/BACKLOG.md` item 4 asks for the same on
the counting quorum hubs (OR3, MAJ3, AND3) that the noise and timing studies use, and with mediator noise.

## Model

Mediator S commits rule q over the three parties' current bits (OR3, MAJ3, AND3), optionally misreading
each party with probability r (probe 464 `input_tpm`). The decision travels down a chain of d relay nodes
S → B1 → … → Bd (each copies its predecessor exactly); every party copies the last relay (S when d = 0).
d ∈ {0, 1, 2}; r ∈ {0, 0.1}; 3 × 2 × 3 = 18 cases; up to 6 nodes.

For each reachable state, φ of every subset from `new_big_phi.reachable_subsystems`; whole Φ = maximum
full-system φ (all nodes, relays included) over states; top tie set = subsets within 1e-9 of the largest
subset φ, at the state where it occurs.

Controls: d = 0 reproduces the deterministic hub TPM at r = 0 and probe 464's `input_tpm` at r = 0.1
(1e-12); whole Φ at d = 0 matches the known values (OR3 3.0, AND3 3.0, MAJ3 0 at r = 0; MAJ3 0.026981 at
r = 0.1).

## Outcomes (threshold 1e-9)

- H1: noise-free OR3 and AND3 have whole Φ > 1e-9 at every d.
- H2: noise-free MAJ3 has whole Φ ≤ 1e-9 at every d.
- H3: noisy MAJ3 (r = 0.1) has whole Φ > 1e-9 at every d.
- H4: noise-free OR3 whole Φ at d = 1 is lower than at d = 0.
- H5: for noise-free OR3 at d = 1, the full system is not in the top tie set.
