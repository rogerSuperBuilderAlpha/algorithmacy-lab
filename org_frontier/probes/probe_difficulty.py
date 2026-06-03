"""Probe 18 — does Φ track coordination difficulty?

Paper 3's behavioral result: Φ and coordination difficulty share a structural cause (an agent-based
experiment found a strict joint determination with no direct channel is harder to coordinate
through). This is an analytic stand-in, not the ABM.

Define an analytic difficulty proxy for a determination f(W, C): coordination is REQUIRED when
success (S' = 1) is possible but neither party can guarantee it alone —
    can_W_force = some w with f(w, c) = 1 for all c ;  can_C_force = symmetric.
    coordination_required = success_possible AND NOT can_W_force AND NOT can_C_force.

H18: triadic verdicts coincide with coordination-required determinations, and the bottleneck
(S = W ∧ C, no channel) is harder by this proxy than an open-channel form. CIRCULARITY IS EXPLICIT:
both Φ and the proxy derive from the determination, so agreement is structural consistency, not
independent validation — reported honestly, as Paper 3 frames its own behavioral check.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_difficulty
"""

import csv
import os

from .lib import verdict

LABELS = ("W", "S", "C")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def _f(t):
    return lambda a, b: t[(a & 1) | ((b & 1) << 1)]


def coordination_required(t):
    f = _f(t)
    success_possible = any(f(w, c) for w in (0, 1) for c in (0, 1))
    can_w = any(all(f(w, c) for c in (0, 1)) for w in (0, 1))
    can_c = any(all(f(w, c) for w in (0, 1)) for c in (0, 1))
    return success_possible and not can_w and not can_c


def main():
    rows = []
    for m in range(16):
        t = tuple((m >> k) & 1 for k in range(4))
        s = _f(t)
        rules = [lambda x: x[1], lambda x, s=s: s(x[0], x[2]), lambda x: x[1]]
        v = verdict(rules, LABELS)
        rows.append({"fn": m, "coordination_required": coordination_required(t),
                     "structure": v.structure, "phi": round(v.max_phi, 3)})

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "difficulty.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    coreq = [r for r in rows if r["coordination_required"]]
    nocoreq = [r for r in rows if not r["coordination_required"]]
    agree = sum((r["coordination_required"]) == (r["structure"] == "triadic") for r in rows)

    print("PROBE 18 — Φ vs coordination difficulty (16 determinations)")
    print("=" * 76)
    print(f"  coordination-required determinations : {len(coreq)}/16")
    print(f"    of these, triadic                  : {sum(r['structure']=='triadic' for r in coreq)}/{len(coreq)}")
    print(f"    not-required, triadic              : {sum(r['structure']=='triadic' for r in nocoreq)}/{len(nocoreq)}")
    print(f"  verdict == coordination-required     : {agree}/16 ({100*agree/16:.0f}% agreement)")

    # Channel-vs-bottleneck contrast (the ABM's key result), reproduced analytically.
    bottleneck = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]          # no W-C channel
    open_chan = [lambda x: x[1] | x[2], lambda x: x[0] & x[2], lambda x: x[1] | x[0]]  # W,C also read each other
    vb, vo = verdict(bottleneck, LABELS), verdict(open_chan, LABELS)
    print("-" * 76)
    print(f"  bottleneck (no channel) : {vb.structure:<8} Φ={vb.max_phi:.3f}  coordination_required=True")
    print(f"  open channel            : {vo.structure:<8} Φ={vo.max_phi:.3f}  (parties coordinate directly)")
    print("=" * 76)
    print("  NOTE: circularity is explicit — both Φ and the proxy derive from the determination;")
    print("  agreement is structural consistency, not independent behavioral validation.")
    print("=" * 76)


if __name__ == "__main__":
    main()
