# The rotating chair: preserved integration and a moving veto

## Abstract
Every mediator in the lab's catalog is a fixed seat, and a fixed conjunctive mediator is the coordination's
veto player. We ask what happens when the mediator role rotates on a clock among the parties. In designed
conjunctive Boolean models under exact IIT-4.0, full rotation preserves peak party-core integration (Φ = 2 at
three parties, Φ = n−1 = 3 at four) and its coverage of reachable states (25%, the same as a fixed chair),
while transferring the veto between successive chairs: whenever party-only integrating coalitions exist, the
current and previous chairs hold the veto, so no party retains it across states. Two-seat rotation leaves both
seats as permanent veto players. An XOR chair is the boundary case: under free rotation the party core is never the maximal complex and
all three parties hold the veto (under earned XOR rotation ABC is the exact maximal complex in 4/12 states,
with all three parties still holding the veto). The result depends on chair logic, and concerns the tested models only.

## Question
Does a rotating chair keep a coordination irreducible, and who holds its bottleneck?

## Method
Parties copy the current chair; the chair's next state is the AND (or OR, XOR) of the other parties. A mod-k
clock selects the chair; in "earned" variants it advances only when the chair is active. Forms: fixed chair,
two-seat alternation, and full rotation at three parties; fixed and full rotation at four. Measures: the
maximal complex per reachable state (pyphi IIT-4.0) and at the peak-Φ state; party-only integrating
coalitions (size ≥ 2, φ_s > 0) per state; the per-state veto set and its intersection across states; the
whole-system verdict (`classify_rules`). Hypotheses H1–H5 were committed before probe 453, H6 before 454,
and H7–H8 before 455. Probe 456 is a post-hoc per-state audit run after independent review.

## Results
**Pre-registered.** Peak party-core Φ is unchanged by full rotation (2 vs 2; 3 vs 3). The cross-state party
veto is {A} for a fixed chair, {A, B} for two-seat alternation, and empty for full rotation at three and four
parties (H3 partial, H6 holds). Whole-system max Φ is 0 for both fixed and rotating forms, so H4 is a tie at
0 vs 0 and H1 is refuted at the whole-system level. H2 is refuted for the peak core (no clock node in it); clock nodes form the
maximal complex in many other states. H7 holds for OR and fails for XOR. H8 fails for AND.

**Exploratory audit findings (probe 456, identified after the original hypotheses).**
1. *A moving veto.* Whenever party-only integrating coalitions exist (half the evaluated states), full
   rotation gives the veto to the current and previous chairs: in all six eligible three-party states and all
   eight four-party states.
2. *Equal state coverage.* The party core is the maximal complex in 25% of distinct reachable states for both
   the fixed chair and full rotation (2/8, 3/12, 4/16). This is coverage of states counted uniformly, not
   persistence or time spent in the core. Clock-only cores occur in both controls; we do not claim a clock causes them.

**Boundary case.** With an XOR chair the party core is never the maximal complex under free rotation (0/12),
and among party coalitions all three parties are veto players. An earned XOR rotation reads triadic at the
whole-system level (max Φ 0.5); ABC is the exact maximal complex in 4/12 states, and all three parties
remain veto players.

## Discussion
The lab's political-economy results locate the mediator's rent and veto in a fixed seat (Q111–Q112, the
veto-player thread). In these models rotation leaves peak integration and state coverage as they were and moves
the veto with the gavel: the bottleneck travels as a current-and-previous pair rather than resting with one
party. As a prior to test against data, rotating chairs, on-call rotations, and term-limited moderators would be
expected to show a handed-over veto rather than none, and the effect should depend on how the chair combines
inputs.

## Limits
In-silico evidence about designed deterministic Boolean models with at most four parties and a clock that is
external (free-running) in most forms and endogenous (advancing only when the chair acts) in the earned variants. State coverage counts reachable states uniformly and does not measure temporal persistence along
trajectories. The veto results are per state and across states, not along time. The two audit findings are
exploratory. Nothing here establishes how real leadership rotation behaves. Open next: trajectory-weighted
persistence, noisy schedules and other endogenous schedules (for example, an elected chair), more chair logics, and a field case.
