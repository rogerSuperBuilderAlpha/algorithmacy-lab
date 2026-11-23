# Joint pivotality at consensus: which three-party commit rules bind?

Fixed before this study's computation.

## Gap

`lockstep_symmetry` found that in the two-party strict-mediation family a form binds iff both parties
track the mediator and the aligned commit is symmetric. That rule cannot carry over to three parties as
stated: the majority rule is symmetric and factors (coordination-logic atlas). The quorum law covers only
the four counting thresholds; the other 3-input commit rules on a three-party hub have not been run as a
family. Here: all 256 Boolean commit rules S' = h(P1, P2, P3) with every party copying S (P_i' = S).

## Candidate rule (joint pivotality at consensus)

With every party copying S, each reachable state has P1 = P2 = P3 (a "consensus" state, all 0 or all 1).
Call party i pivotal at consensus value a if flipping P_i alone at (a, a, a) changes h. Rule R: the form
is triadic iff there is a consensus value a at which every party is pivotal.

On two parties R gives the same verdicts as the alignment-symmetry rule (AND is jointly pivotal at (1,1);
the veto W ∧ ¬C has W pivotal at (0,0) and C pivotal at (1,1), never both at once). On three parties R
predicts: AND and OR bind, majority factors (no party is pivotal at either consensus), three-way parity
binds.

Counting R's picks: for each consensus value a, h must differ from h(a,a,a) at all three one-flip
neighbours; the four other inputs are free. That gives 2 (value of h(a,a,a)) × 16 = 32 functions per a,
minus the 4 counted at both a = 0 and a = 1 = 60 functions.

## Outcomes (threshold 1e-9; verdict = max whole-system Φ over reachable states)

- H1: rule R classifies all 256 commit rules correctly (60 triadic).
- H2: among the 14 non-constant symmetric commit rules (output fixed by how many parties are on), R
  predicts 12 bind and exactly two factor: majority and its negation (minority). A symmetric rule binds
  iff its output changes between 0 and 1 parties on, or between 2 and 3 parties on.
- H3: every triadic form's whole-system Φ is in {Φ of AND3, Φ of XOR3}, i.e. at most two distinct positive
  values, as in the two-party family (2.0 and 0.5).

Controls: AND3 (= quorum 3-of-3) Φ = 3.0 and MAJ3 Φ = 0, the Q215 values for the same hub.
