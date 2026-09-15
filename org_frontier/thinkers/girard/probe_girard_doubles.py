"""Probe — Girard H5: doubles.

Question.  Girard (1965: 122): "Double mediation is a melting-pot in which differences among classes and
           individuals gradually dissolve." Shares — each term's deletion cost — in double mediation and in
           single internal mediation.
Hypothesis. H5: double shares S = M > 0, O = 0; internal shares S ≠ M.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_doubles
"""

from org_frontier.thinkers.girard import forms as F


def main():
    print("Girard H5 — shares in double and in single internal mediation")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("double", "internal")}
    sh = {name: F.shares(name) for name in ("double", "internal")}
    d = sh["double"]
    a = abs(d["S"] - d["M"]) < 1e-9 and d["S"] > 1e-9 and abs(d["O"]) < 1e-9
    b = abs(sh["internal"]["S"] - sh["internal"]["M"]) > 1e-9
    print("  double: S=M>0, O=0 → %s   internal: S≠M → %s" % (a, b))
    n = int(a) + int(b)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H5 (in double mediation the rivals are interchangeable; in single mediation they are not): %s" % status)
    F.save("probe_girard_doubles", {"control": control, "forms": recs, "shares": sh, "H5": status})


if __name__ == "__main__":
    main()
