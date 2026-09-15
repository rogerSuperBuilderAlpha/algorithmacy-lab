"""Probe — Ostrom H5: clearly defined boundaries.

Question.  Ostrom (1990: 90): who may withdraw "must be clearly defined." An outsider who reads the commons
           but is not read, against a breach in which a member's compliance turns on the outsider.
Hypothesis. H5: bounded has self's core and Φ with V(O) = 0; breached differs in core or has lower Φ.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_boundary
"""

from org_frontier.thinkers.ostrom import forms as F


def main():
    print("Ostrom H5 — the outsider, bounded and breached")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("self", "bounded", "breached")}
    s, b, x = recs["self"], recs["bounded"], recs["breached"]
    bounded_ok = set(b["core"]) == set(s["core"]) and abs(b["core_phi"] - s["core_phi"]) < 1e-6 \
        and abs(b["value_added"]["O"]) < 1e-9
    breached_ok = set(x["core"]) != set(s["core"]) or x["core_phi"] < s["core_phi"] - 1e-6
    print("  bounded leaves the enterprise unchanged=%s   breach changes it=%s" % (bounded_ok, breached_ok))
    status = "CONFIRMED" if bounded_ok and breached_ok else ("PARTIAL" if bounded_ok else "REFUTED")
    print("H5 (a defined boundary keeps the outsider out; a breach changes the whole): %s" % status)
    F.save("probe_ostrom_boundary", {"control": control, "forms": recs, "H5": status})


if __name__ == "__main__":
    main()
