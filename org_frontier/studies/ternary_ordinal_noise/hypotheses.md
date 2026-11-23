# Ordinal noise: when a three-valued reading can only slip to the neighbouring value

Fixed before this study's computation.

## Gap

`ternary_majority_noise` and `ternary_lift_panel` (both pre-registered earlier today) used uniform
misreadings: a reading slips to either of the two other values with equal chance, so "no" can be read
as "yes". With ordered answers (no < maybe < yes) a more natural error slips only to the neighbouring
value: no ↔ maybe ↔ yes, never no ↔ yes. Item 2 of `ternary_majority_noise/BACKLOG.md` and items 1 and 4
of `ternary_lift_panel/BACKLOG.md`.

Values already seen before this file (uniform noise only): hub median whole Φ 0.012445, 0.022209,
0.033668, 0.029390 and hub min 3.886383, 3.133882, 1.940021, 0.549502 at r = 0.05, 0.1, 0.2, 0.4; triad
|W − C| whole Φ 0.759836 (triadic) and binary XOR 0.292615 (not triadic) at r = 0.1; triad min 2.321394
at r = 0.1. Nothing under ordinal noise has been computed.

## Model

Ordinal misreading at rate r: a reading of 0 becomes 1 with probability r; 2 becomes 1 with
probability r; 1 becomes 0 or 2 with probability r/2 each. Uniform misreading as in the earlier studies.

- Hub (from `ternary_majority_noise`): mediator S + three parties on {0,1,2}; S misreads each party;
  S commits median or min of its readings; parties copy S. r ∈ {0.05, 0.1, 0.2, 0.4}, ordinal noise.
- Triad (from `ternary_lift_panel`): W' = S, C' = S, S' = f(W, C), S misreads each input; f = |W − C|
  (XOR lift) and min (AND lift); binary XOR on {0,1} as reference. r ∈ {0.01, 0.05, 0.1, 0.2, 0.4},
  both noise shapes.

Whole Φ = largest full-system φ over reachable states; at every whole-Φ state, the maximal complex.
"Full core" = the whole system is the maximal complex at every whole-Φ state.

## Controls (must pass)

- C1: uniform-noise hub median at r = 0.1 reproduces 0.022209; uniform triad |W − C| at r = 0.1
  reproduces 0.759836.

## Outcomes (threshold 1e-9)

- H1: under ordinal noise the hub median never has a full core at any rate.
- H2: under ordinal noise the hub min has a full core at every rate.
- H3: ordinal-noise hub min whole Φ ≥ uniform-noise hub min whole Φ at every rate (neighbour slips
  lose less than jumps across the scale).
- H4: under uniform noise the |W − C| triad has a full core at every rate from 0.05 to 0.4.
- H5: under ordinal noise the |W − C| triad has a full core at every rate from 0.05 to 0.4.
- H6: binary XOR never has a full core at any rate.
