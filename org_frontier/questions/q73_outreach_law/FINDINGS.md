# Q73 findings — the outreach-coordination law

Pillars P1-P4 are re-derived here; P5 is carried from the registered Q71 and Q72 checks (not re-derived by
this probe). All hold and the law stands.

| Pillar | Keystone | Result | Source |
|---|---|---|---|
| P1 joint determination | read_recipient vs broadcast | triadic Φ=2.0 vs dyadic | re-derived |
| P2 liveness decides | read_recipient vs one_shot (same wiring) | triadic vs dyadic | re-derived |
| P3 substitutability collapses | all_required vs substitutable | triadic Φ=3.0 vs dyadic | re-derived |
| P4 closure binds the whole | closed ring | core {E,A1,A2,R}, Φ=4.0 | re-derived |
| P5 structural, not cheap | Q71 noise, Q72 proxy | robust; no proxy recovers it | carried (q71/q72) |

From `probe_law_pillars.py` (P1-P4 re-derived) and the registered Q71/Q72 checks (P5).

## The law

**Agent-mediated outreach demands algorithmacy if and only if the parties that constitute its irreducible
core are bound into a single joint determination that stays live.** The core is not always every party:
under mediation depth it localizes to an end pair (Q65, Q66). Five conditions govern the verdict:

1. **Joint determination.** The mediating agent must read all parties. An agent that ignores the recipient
   broadcasts, and the form factors (Q63, Q64).
2. **Liveness and reciprocity.** Each party must stay live to the commit. A read-but-frozen recipient
   leaves the form dyadic, and reciprocity binds at a threshold, not by degrees: a single back-edge seeds
   a local core while the whole still factors (Q63, Q67).
3. **Non-substitutability.** Interchangeability of any party — counterpart, recipient, or agent —
   collapses the triad. Only an all-required joint determination is irreducible; substitutable or pooled
   forms factor at every breadth (Q64, Q70).
4. **The core and delegation.** Mediation depth preserves the triad but localizes the core to a symmetric
   end pair; a closed loop binds the whole at higher Φ. A bidirectionally-coupled recipient agent joins
   the core and displaces the sender, and when both sides delegate the two agents become the core with
   both humans displaced — but only while the agents are specific and required (Q65, Q66, Q68, Q69, Q70).
5. **Structural, not cheap.** The verdict is robust to noise and is not recoverable by any cheap proxy;
   cost correlates with it at best and collides with it at worst. The exact computation is required
   (Q71, Q72).

## Scope

In-silico throughout: exact Φ on small Boolean models of coordination, evidence about the models and
separated from claims about real inboxes by the validation gap. The law is a structural account of when
agent-mediated outreach is irreducible; it does not say whether a given message is welcome, ethical, or
worth a reply. Φ magnitude is read ordinally.
