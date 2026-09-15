"""Probe — Girard H2: external and internal mediation.

Question.  Girard (1965: 9): external mediation when the distance eliminates "any contact between the two
           spheres"; internal when the spheres "penetrate each other." Amadis does not read Don Quixote; a
           rival does. Who is in the complex in each?
Hypothesis. H2: external — M in no complex, S and O not one; internal — core {S, M, O}.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.girard.probe_girard_mediation
"""

from org_frontier.thinkers.girard import forms as F


def main():
    print("Girard H2 — Amadis and the rival")
    control = F.run_control()
    recs = {name: F.evaluate(name) for name in ("external", "internal")}
    ext_core = set(recs["external"]["core"])
    ext_ok = "M" not in ext_core and not ({"S", "O"} <= ext_core)
    int_ok = set(recs["internal"]["core"]) == {"S", "M", "O"}
    print("  external: M outside and S,O not one=%s   internal: core is {S,M,O}=%s" % (ext_ok, int_ok))
    n = int(ext_ok) + int(int_ok)
    status = "CONFIRMED" if n == 2 else ("PARTIAL" if n == 1 else "REFUTED")
    print("H2 (the distant mediator touches nothing; the near one makes the three one): %s" % status)
    F.save("probe_girard_mediation", {"control": control, "forms": recs, "H2": status})


if __name__ == "__main__":
    main()
