# Partial synchrony on quorum hubs: members update in blocks, some together and some in turn

Fixed before this study's computation.

## Gap

`update_order_quorum` ran the 24 one-at-a-time orders on OR3, MAJ3 and AND3 and found whole Φ 0 in
72/72; the synchronous hub has whole Φ 3.0 for OR3 and AND3. Its backlog item 2 asks about the cases in
between: some members updating together in a block, blocks in turn.

## Model

Mediator S over three parties (OR3, MAJ3, AND3; parties copy S); no noise. A schedule is an ordered
partition of {S, P1, P2, P3} into blocks; blocks update in order, members of a block update at the same
time from the state left by earlier blocks. All 75 ordered partitions (1 synchronous, 24 one-at-a-time,
50 mixed) × 3 forms = 225 cases.

For each reachable state, φ of every subset from `new_big_phi.reachable_subsystems`; whole Φ = maximum
full-system φ over states; top tie set as in the earlier studies.

Controls: the one-block schedule equals the synchronous hub TPM (1e-12) and gives OR3 3.0, MAJ3 0,
AND3 3.0; each one-at-a-time schedule equals `update_order_quorum.order_tpm` for that order.

## Outcomes (threshold 1e-9)

- H1: for OR3, whole Φ > 1e-9 only under the one-block (synchronous) schedule.
- H2: the same holds for AND3.
- H3: MAJ3 whole Φ ≤ 1e-9 under all 75 schedules.
- H4: under ({S}, {P1,P2,P3}) — S first, then all parties together — OR3's top unit is {P1,P2,P3} with
  φ > 3.0.
