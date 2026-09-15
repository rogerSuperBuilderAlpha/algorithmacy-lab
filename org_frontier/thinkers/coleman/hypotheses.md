# Coleman — Stage 3 hypotheses (fixed before computing)

## The rendering that all five share

A **party** is a Boolean node; a **tie** is reading. For the norm forms, A's state is 1 when A complies and
B's or C's is 1 when it sanctions: A **yields only to a joint sanction** (A' = B ∧ C, C1's "combine forces");
a sanctioner **sanctions when A defects** (¬A) and, under closure, also **when the other sanctions** (∨ C —
"either can reward the other for sanctioning A"). A **norm is effective** when the compliance state, A = 1 with
the sanction standing, is a fixed point. For the credit forms, a member's state is 1 when it pays and it
pays when the member it depends on has paid. The **structure** is the major complex; a party's **value added**
V is the core Φ of the whole minus the core Φ with the party deleted (the Burt paper's quantity; a deleted
party's variable is read as 0); **positional advantage** is V minus the largest V among the others.

Forms (rules in `methods.md`): **norm_open** / **norm_closed**; Burt's **info** and **control** brokers,
open and closed, imported from `burt.forms` (the same forms that paper ran); **parents_open** /
**parents_closed** (P1, P2, K1, K2); **ring4** and **two_dyads** (A, B, C, D).

## H1 — Closure makes the norm effective (C1)

- **H1 (Coleman).** The compliance state (A = 1, B = 1, C = 1) is a fixed point of norm_closed and not of
  norm_open; and in norm_closed B and C are members of one complex.
- **H0.** Compliance fixed in the open form too, or not fixed in the closed, or B and C not co-members.
- **Lab prior.** With on the fixed point (worked by hand: open oscillates, closed holds). Open on Φ.

## H2 — Closure is the collective's gain, not the broker's (C1, C5; against Burt H1)

- **H2 (Coleman).** For both of Burt's brokers, closure raises the core's Φ (coreΦ_closed ≥ coreΦ_open) and
  lowers the broker's positional advantage (advantage_closed < advantage_open).
- **H0.** Core Φ falls with closure, or the broker's advantage does not fall.
- **Lab prior.** The Burt paper reported control: closed core {E, X, Y} at 6.000, advantage 0; info: closed
  core {X, Y}, V(E) 0. With on advantage; open on core Φ for the information broker.

## H3 — Intergenerational closure (C4)

- **H3 (Coleman).** In parents_closed the major complex contains both parents and both children; in
  parents_open it does not; and the all-norm fixed point (1111) has a larger basin in the closed form.
- **H0.** Four-member complex in the open form, or fewer than four in the closed, or no larger basin.
- **Lab prior.** Open.

## H4 — The rotating-credit association is one unit (C2, C3)

- **H4 (Coleman).** ring4 is one complex of all four with Φ > 0 and every member's V is positive and equal;
  two_dyads has no complex containing more than two.
- **H0.** Ring not a complex of four, unequal V, or a larger complex among the dyads.
- **Lab prior.** With (Serres H5: the three-ring binds).

## H5 — The public good (C5)

- **H5 (Coleman).** Closing the norm form raises the core's Φ (gain = coreΦ_closed − coreΦ_open > 0), and the
  closer B's value added rises by less than the gain: (V_B,closed − V_B,open) / gain < 1.
- **H0.** No gain, or B captures the whole gain or more.
- **Lab prior.** Open.

## Not tested here

Information channels; the dropout analysis; the definition by function; Burt's (2001) synthesis of closure
within and brokerage beyond, which the Burt paper tested (H5 there).
