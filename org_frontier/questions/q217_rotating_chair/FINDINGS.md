# Q217 — Findings: the rotating chair

Probes 453 (three parties) and 454 (four parties). Hypotheses fixed in `hypotheses.md` before each run
(commits 4b4f3d9e, and the H6 addendum before probe 454).

| Form | Whole-system | Major complex | Core Φ | Integrating coalitions | Veto players |
|---|---|---|---|---|---|
| F_fixed (chair A, n=4 incl. idle clock) | dyadic | A,B,C | 2.0 | 3 | A |
| F_rot2 (chair alternates A/B) | dyadic | A,B,C | 2.0 | 2 | A, B |
| F_rot3 (chair cycles A→B→C) | dyadic | A,B,C | 2.0 | 5 | none |
| F4_fixed (chair A, four parties) | dyadic | A,B,C,D | 3.0 | 7 | A |
| F4_rot (chair cycles A→B→C→D) | dyadic | A,B,C,D | 3.0 | 9 | none |

## Verdicts
- **H1 (rotation reads triadic): refuted at the whole-system level.** Every form, fixed included, reads dyadic
  because the clock is a free-running node outside the core (cf. Q177 spectators). The major complex is triadic in all.
- **H2 (clock joins the core): refuted.** The schedule shapes who holds power but is not a member.
- **H3 (rotation dissolves the single veto): partial.** Full rotation leaves no veto player; two-seat
  alternation spreads the veto to both seats. The veto set equals the set of parties that ever hold the chair
  when that set is a strict subset of the parties.
- **H4 (rotation integrates at least as much): holds as a tie.** Core Φ is identical (2.0 at three parties, 3.0 = n−1 at four).
- **H5 (core is all parties): holds.**
- **H6 (no-veto scales to four parties): holds.**

## The finding
Rotating the mediator role is integration-neutral and veto-dissolving: a full rotation keeps the same
irreducible core and core Φ as a fixed hub (Φ = n−1), while removing every single-party bottleneck. The catalog
had no form with a full irreducible core and an empty veto set under a conjunctive mediator.

## Limits
In-silico, designed deterministic forms, conjunctive chairs, followers copy the chair, deterministic clock,
n ≤ 6 nodes. Whole-system verdicts are confounded by the external clock.

## Extension — probe 455 (H7, H8 fixed before the run)

| Form | Whole-system | Max Φ | Major complex | Core Φ | Integrating | Veto |
|---|---|---|---|---|---|---|
| F_rot3_OR | dyadic | 0 | A,B,C | 2.0 | 5 | none |
| F_rot3_XOR | dyadic | 0 | T | 1.0 | 2 | none |
| F_earned3 (AND, gavel passes only when the chair acts) | dyadic | 0 | A,B,C | 2.0 | 8 | none |
| F_earned3_XOR | triadic (7/12 states) | 0.5 | U | 1.0 | 9 | none |

- **H7: holds for OR, refuted for XOR.** An OR chair keeps the full party core at Φ = 2 with no veto. A parity
  chair under rotation loses the party core entirely; the maximal complex shrinks to one clock bit. Rotation is
  veto-dissolving for monotone chairs and core-destroying for a parity chair, the reverse of the fixed-hub
  result where parity binds more readily (gate-logic thread).
- **H8: refuted for the AND chair.** Making the gavel pass only when the chair acts adds integrating coalitions
  (5 → 8) but leaves the clock outside the core and the whole system dyadic. With an XOR chair the earned
  rotation makes the whole system triadic (max Φ 0.5) for the first time in this question, but its maximal complex
  is a single clock bit, so the whole-system reading and the core disagree (cf. Q74, Q152).

## Corrections after independent review (reproduced numbers; interpretations narrowed)

1. **Peak, not persistent, core.** `major_complex` reports the highest-Φ state. In F_rot3 the party core ABC is
   the maximal complex in only 3 of 12 states; clock-only complexes win in the other nine. "Keeps the core"
   means "preserves peak party-core Φ".
2. **The clock does join complexes.** Clock nodes frequently form the maximal complex at non-peak states, and
   F_earned3 has a mixed B,C,U complex at one state. H2's refutation holds only for the peak-Φ core.
3. **Veto freedom is across states only.** In full three-party rotation every state with integrating party
   coalitions has a two-party veto set (AB, BC, or AC); the empty set is their intersection across states. The
   veto rotates; it does not vanish moment by moment.
4. **The XOR empty veto is a clock artifact.** Restricting coalitions to parties, ABC is the only integrating
   coalition for both free and earned XOR rotation, so all three parties are veto players. F_earned3_XOR also has
   the whole five-node complex in two states; singleton U wins only at the peak state. H7 for XOR is therefore
   "core lost at peak; all parties veto among party coalitions".
5. **H4 measured as predicted.** H4 concerned whole-system max Φ: it ties at 0 vs 0. The core-Φ tie (2 vs 2,
   3 vs 3) is a separate, also-reproduced result, not the test of H4.

**Defensible conclusion.** In the tested conjunctive Boolean models, full rotation preserves peak party-core
integration and removes a permanent veto across states. It does not establish continuous core membership,
moment-by-moment veto freedom, or anything about real organizations.
