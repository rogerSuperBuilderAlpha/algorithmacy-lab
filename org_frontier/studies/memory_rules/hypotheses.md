# Memory rules: members whose next state depends on their own last state, deterministically

Fixed before this study's computation.

## Gap

`lazy_update` gave nodes a *random* memory (keep the last state with probability λ). Its backlog item 4
asks for *deterministic* memory: a party or mediator whose rule reads its own last state as an input
(a self-loop in the connectivity matrix). `ergodic_sticky_returns` and `timescale_separation` used sticky
or held mediators on the conjunctive/parity forms, not on the counting quorum hubs, and never put a
deterministic self-loop on the parties.

## Model

Mediator S over three parties, deterministic, no noise. Base rule q(P) ∈ {OR3, MAJ3, AND3}.

Party rules (each party i, same rule for all), reading S and its own last bit Pi:

- **copy**: Pi' = S (the base hub)
- **and**: Pi' = S AND Pi
- **or**: Pi' = S OR Pi
- **toggle**: Pi' = S XOR Pi

Mediator rules:

- **plain**: S' = q(P)
- **toggle**: S' = q(P) XOR S
- **vote**: S counts its own last bit as a fourth vote at the same quota plus one:
  S' = [P1 + P2 + P3 + S ≥ k + 1], with k = 1, 2, 3 for OR3, MAJ3, AND3.

3 × 4 × 3 = 36 cases. For each reachable state, φ of every subset from `new_big_phi.reachable_subsystems`;
whole Φ = maximum full-group φ over states; top tie set = subsets within 1e-9 of the largest subset φ.

Controls: copy/plain reproduces the deterministic hub TPM (1e-12) and its known whole Φ (OR3 3.0, AND3
3.0, MAJ3 0; `gate_c1`).

## Outcomes (threshold 1e-9)

- H1: MAJ3 with a plain mediator has whole Φ ≤ 1e-9 under every party rule (and, or, toggle).
- H2: MAJ3 with a toggle mediator and copying parties has whole Φ > 1e-9.
- H3: OR3 and AND3 with a plain mediator have whole Φ > 1e-9 under every party rule.
- H4: MAJ3 with a vote mediator and copying parties has whole Φ > 1e-9.
- H5: in every case where the mediator has a self-loop (toggle or vote), the full group is in the top tie
  set less often than with a plain mediator, counted over the 12 form × party-rule cells.
