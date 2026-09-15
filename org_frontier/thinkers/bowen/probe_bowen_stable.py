"""Probe — Bowen H1: the triangle is the smallest stable relationship system.

Question.  Bowen (1978: 373): "A two-person system may be stable as long as it is calm, but when anxiety
           increases, it immediately involves the most vulnerable other person to become a triangle."
           Under uniform flip noise ε, does the triangled form retain more of its Φ than the dyad?
Hypothesis. H1: at every ε in {0.05, 0.1, 0.2, 0.3} the triangled form's retained fraction exceeds the
           dyad's and its major complex stays {A, B, C}.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.bowen.probe_bowen_stable
"""

from org_frontier.thinkers.bowen import forms as F


def main():
    print("Bowen H1 — dyad and triangle under uniform anxiety")
    control = F.run_control()
    recs = {"dyad": [], "triangled": []}
    base = {}
    for name in recs:
        base[name] = F.evaluate(name, 0.0)["phi_mip"]
        for e in F.EPS:
            recs[name].append(F.evaluate(name, e, base_phi=base[name]))
    better, full = [], []
    for i, e in enumerate(F.EPS[1:], start=1):
        fd, ft = recs["dyad"][i]["fraction"], recs["triangled"][i]["fraction"]
        better.append(ft > fd + 1e-9)
        full.append(set(recs["triangled"][i]["core"]) == {"A", "B", "C"})
    print("  triangle retains more than dyad at ε>0: %s   triangle core stays {A,B,C}: %s" % (
        "".join("Y" if b else "n" for b in better), "".join("Y" if b else "n" for b in full)))
    if all(better) and all(full):
        status = "CONFIRMED"
    elif any(better):
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H1 (the triangle retains more of its integration under anxiety than the dyad): %s" % status)
    F.save("probe_bowen_stable", {"control": control, "base_phi": base, "forms": recs, "H1": status})


if __name__ == "__main__":
    main()
