"""Probe — Bowen H4: interlocking triangles.

Question.  Bowen (1978: 373–374): when the triangle cannot hold the tension, "one of the involved twosome
           triangles in a fourth person ... The emotional forces duplicate the exact patterns in the new
           triangle," and the system becomes "a series of interlocking triangles." With D involved by A's
           same move: is the major complex a triangle or a unit of four, and does the four retain more Φ
           under anxiety than the three?
Hypothesis. H4: (a) the interlocked core has three parties; (b) the interlocked form's retained fraction
           exceeds the triangled form's at every ε > 0.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_interlock
"""

from org_frontier.thinkers.bowen import forms as F


def main():
    print("Bowen H4 — the triangled form and the interlocked four under uniform anxiety")
    control = F.run_control()
    recs, base = {"triangled": [], "interlocked": []}, {}
    for name in recs:
        base[name] = F.evaluate(name, 0.0)["phi_mip"]
        for e in F.EPS:
            recs[name].append(F.evaluate(name, e, base_phi=base[name]))
    core0 = recs["interlocked"][0]["core"]
    a = len(core0) == 3
    b_each = [recs["interlocked"][i]["fraction"] > recs["triangled"][i]["fraction"] + 1e-9 for i in range(1, len(F.EPS))]
    b = all(b_each)
    print("  interlocked core at ε=0: %s (three parties=%s)   four retains more than three at ε>0: %s" % (
        tuple(core0), a, "".join("Y" if x else "n" for x in b_each)))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H4 (the four resolve into a triangle, and spreading the tension stabilizes): %s" % status)
    F.save("probe_bowen_interlock", {"control": control, "base_phi": base, "forms": recs, "H4": status})


if __name__ == "__main__":
    main()
