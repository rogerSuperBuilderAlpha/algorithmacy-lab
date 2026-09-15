"""Probe — Granovetter H2: the forbidden triad.

Question.  Granovetter (1973: 1363): with A–B and A–C strong, the B–C tie "is always present (whether weak or
           strong)"; the open triad is the one that does not occur. Is the open triad less integrated than
           its weak closure, and that less than its strong closure?
Hypothesis. H2: Φ(open) < Φ(weak-closed) < Φ(strong-closed), all three in the core each time.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.granovetter.probe_granovetter_triad
"""

from org_frontier.thinkers.granovetter import forms as F

fs = frozenset


def main():
    print("Granovetter H2 — the forbidden triad and its two closures")
    control = F.run_control()
    recs = {}
    for name, p in (("open", F.ABSENT), ("weak_closed", F.WEAK), ("strong_closed", F.STRONG)):
        lab, ties = F.graph(("A", "B", "C"), {fs("AB"): F.STRONG, fs("AC"): F.STRONG, fs("BC"): p})
        recs[name] = F.evaluate(name, lab, ties)
    po, pw, ps = (recs[k]["phi_mip"] for k in ("open", "weak_closed", "strong_closed"))
    all_in = all(set(r["core"]) == {"A", "B", "C"} for r in recs.values())
    ordered = po < pw - 1e-9 < ps - 2e-9
    print("  Φ open=%.3f weak=%.3f strong=%.3f  ordered=%s  all three in every core=%s" % (po, pw, ps, ordered, all_in))
    if ordered and all_in:
        status = "CONFIRMED"
    elif po < ps - 1e-9:
        status = "PARTIAL"
    else:
        status = "REFUTED"
    print("H2 (closure of any strength raises the triad's integration, weak below strong): %s" % status)
    F.save("probe_granovetter_triad", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()
