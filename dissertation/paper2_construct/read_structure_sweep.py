"""Paper 2 — the determination is necessary but not sufficient: read structure decides too.

The draft's strong claim is that the ATS form "stays irreducible for ANY determination that is
a genuine joint function of both parties." That is false as stated. Holding the joint
determination S' = W AND C fixed AND the strict mediator topology (no W<->C edge; W and C each
read only the mediator S and their own state), this script sweeps the worker/counterpart READ
functions and shows that Φ ranges from 0 to 2 — so whether the form reads as a triad depends on
the read structure, not the determination alone. In particular the "realistic feedback" reads
(W' = NOT S, C' = S OR C) collapse the form to Φ = 0, while the pure-bottleneck reads
(W' = S, C' = S) give Φ = 2.

Each party's read is a function of (own_state, S). We sweep the 16 two-input Boolean functions
for each, keep only those that genuinely depend on S (a party that ignores the mediator is not
mediated), and report the Φ distribution and which read pairs preserve the triad verdict.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper2_construct/read_structure_sweep.py
"""

import numpy as np
from phi_instrument import tpm_from_rules, cm_from_rules, system_phi_over_states

# 2-input truth tables; value at (own, S) = bit ((own<<1)|S) of tt (own is the high input,
# S the low input). Which tts genuinely depend on S is computed, not hand-listed.
def _val(tt, own, s):
    return (tt >> ((own << 1) | s)) & 1


def _depends_on_s(tt):
    return any(_val(tt, own, 0) != _val(tt, own, 1) for own in (0, 1))


DEPENDS_ON_S = {tt for tt in range(16) if _depends_on_s(tt)}
# Named tts under this ordering: 10 = "S" (copy low), 5 = "~S", 14 = "own|S = S OR C".


def make_read(tt, self_idx):
    """A party at node self_idx reads (own, S=node1): next = bit((own<<1)|S) of tt."""
    return lambda x, tt=tt, si=self_idx: (tt >> ((x[si] << 1) | x[1])) & 1


S_RULE = lambda x: x[0] & x[2]   # joint determination, held fixed


def phi_of(ttW, ttC):
    rules = [make_read(ttW, 0), S_RULE, make_read(ttC, 2)]
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    # enforce strict mediator topology: reject any wiring that introduces a W<->C edge
    if cm[2, 0] or cm[0, 2]:
        return None
    results = system_phi_over_states(tpm, cm)
    phis = [p for _, p in results] or [0.0]
    return float(np.max(phis))


def main():
    print("=" * 84)
    print("PAPER 2 — Φ under fixed joint determination S'=W&C, varying the read structure")
    print("=" * 84)
    rows = []
    for ttW in DEPENDS_ON_S:
        for ttC in DEPENDS_ON_S:
            phi = phi_of(ttW, ttC)
            if phi is not None:
                rows.append((ttW, ttC, phi))
    phis = [r[2] for r in rows]
    pos = [r for r in rows if r[2] > 1e-9]
    print(f"  valid strict-mediation read pairs evaluated : {len(rows)}")
    print(f"  read pairs with Φ > 0 (triad verdict holds) : {len(pos)} "
          f"({100*len(pos)/len(rows):.0f}%)")
    print(f"  read pairs with Φ = 0 (collapses to dyad)   : {len(rows)-len(pos)} "
          f"({100*(len(rows)-len(pos))/len(rows):.0f}%)")
    print(f"  Φ range over read structures: min {min(phis):.3f}  max {max(phis):.3f}")
    print("-" * 84)
    print("  named cases:")
    for ttW, ttC, tag in [(10, 10, "pure bottleneck    (W'=S,   C'=S)"),
                          (5, 14, "realistic feedback (W'=~S,  C'=S OR C)")]:
        p = phi_of(ttW, ttC)
        print(f"    {tag:<46} Φ = {p:.3f}")
    print("-" * 84)
    print("READING: with the SAME genuine joint determination, Φ spans 0..2 across read")
    print("structures, so 'any joint determination keeps it irreducible' is false. The triad")
    print("verdict is a joint property of the determination AND the read structure; Paper 2 now")
    print("states which reads preserve it (those that let each party's state remain a live")
    print("function of the mediator's commit) rather than claiming the determination suffices.")
    print("=" * 84)


if __name__ == "__main__":
    main()
