# Indirect loops: when the people a platform answers pass it on to the people it reads

Fixed before this study's computation.

## Gap

`who_hears_back` found that a platform binds only the parties it both reads and answers; parties that are
only read or only answered never join the tightest unit. Its read and answered sets always overlapped.
Its BACKLOG asked what happens when they are disjoint, and whether a loop closed *through other people*
(platform → answered party → read party → platform) binds like a direct loop.

## Model

Platform P, parties A1..A4 (n = 5). P' = A1 ∧ A2 (or A1 ∨ A2). A3, A4 copy P (answered).
A1, A2 either keep their own state (self-loop) or copy an answered party:

- **direct** (control, = `who_hears_back` r = 2, t = 2): A1' = A2' = P; A3, A4 self-loop.
- **disjoint_and**: A1, A2 self-loop; A3' = A4' = P.
- **disjoint_or**: as disjoint_and with P' = A1 ∨ A2.
- **relay_both**: A1' = A3, A2' = A4 (each answered party passes the decision to one read party).
- **relay_one**: A1' = A3; A2 self-loop.
- **relay_cross**: A1' = A4, A2' = A3.

Exact IIT 4.0 φ of every reachable subset in every reachable state. Whole Φ = largest full-group φ over
states; top = largest subset φ over states; top ties within 1e-9 at the first state where it occurs.

Controls: conjunctive triad Φ = 2.0; direct reproduces `who_hears_back` (2, 2): top 2.0, ties PA1, PA2,
PA1A2.

## Outcomes (threshold 1e-9)

- H1: in disjoint_and and disjoint_or, no top tie contains P.
- H2: relay_both has whole Φ > 1e-9 and the full five-node group in its top tie set.
- H3: relay_one's top ties all contain P, A1 and A3.
- H4: relay_cross has the same whole Φ and top φ as relay_both (within 1e-9).
