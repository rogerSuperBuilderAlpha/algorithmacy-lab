# Lockstep or symmetry: why does the one-sided veto factor?

Fixed before this study's computation.

## Gap

The coordination-logic atlas found that the one-sided veto (W' = S, S' = W ∧ ¬C, C' = S; form D1) and
material implication (S' = ¬W ∨ C; D4) read dyadic although both parties feed and read the mediator. Its
explanation: the veto "drives the two parties into lockstep", so the system carries two variables, not
three. Its Limits section leaves the test open: "a construction that breaks the W=C symmetry would test
whether the veto factors for the synchronization reason named here or for a narrower one."

But the atlas's own AND hub (W' = S, S' = W ∧ C, C' = S) also holds W = C in every reachable state (both
parties copy last step's S), and it binds at Φ = 2.0. So lockstep cannot be the whole story. We propose a
narrower rule and test it on the full 256-form strict-mediation family (W' = f(S), C' = g(S),
S' = h(W, C); `org_frontier.corpus.population.enumerate_family`).

## Proposed rule (alignment symmetry)

When both reads are non-constant (f, g ∈ {S, ¬S}), every reachable state has C = W (if f = g) or C = ¬W
(if f ≠ g). Define the aligned commit h*(a, b) = h(a, b) if f = g, else h(a, ¬b). Rule: the form is
triadic iff h* is symmetric (h*(a, b) = h*(b, a)) and depends on both inputs. If either read is constant,
the form factors.

The symmetric two-input functions that depend on both inputs are AND, OR, NAND, NOR, XOR, XNOR, so the
rule picks 6 commits for each of the 4 non-constant read pairs: 24 forms.

## Outcomes (threshold 1e-9; verdict = max whole-system Φ over reachable states)

- H1: lockstep is not sufficient. At least one form whose reachable states all have W = C binds.
  (We report how many lockstep forms bind and how many factor.)
- H2: the alignment-symmetry rule classifies all 256 forms correctly (24 triadic, all of them the rule's 24).
- H3: breaking the lockstep the atlas asked for, by having the counterpart read ¬S: the veto
  (f = S, g = ¬S, h = W ∧ ¬C) binds, and the AND hub with the same reads factors.
- H4: max Φ and the verdict are identical (1e-9) across all forms related by renaming a node's two values
  (the 8 flips of W, S, C), which is why a sign flip on one input can matter: it changes the alignment.

Control: the census count of 24/256 triadic must reproduce; the atlas values D1 (veto) Φ = 0 and the AND
hub Φ = 2.0 must reproduce.
