"""Probe — Coleman H3: intergenerational closure.

Question.  Coleman (1988: S107): with a tie between the parents, "parent A is reinforced by parent D in
           sanctioning his child's actions" and D "constitutes a monitor not only for his own child, C, but
           also for the other child, B." Two parents, two children who are friends; with and without the
           parents' tie. Who is the complex, and how large is the basin of the all-norm state?
Hypothesis. H3: closed core = all four; open core smaller; basin(1111) larger under closure.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.coleman.probe_coleman_parents
"""

from org_frontier.thinkers.coleman import forms as F


def main():
    print("Coleman H3 — two parents, two children")
    control = F.run_control()
    recs = {}
    for name in ("parents_open", "parents_closed"):
        recs[name] = F.evaluate(name)
        labels, rules = F.compile_spec(F.SPECS[name])
        recs[name]["basin_1111"] = F.basin(rules, 4, (1, 1, 1, 1))
        print("    basin of the all-norm state: %d of 16" % recs[name]["basin_1111"])
    all4 = {"P1", "P2", "K1", "K2"}
    a = set(recs["parents_closed"]["core"]) == all4
    b = set(recs["parents_open"]["core"]) != all4
    c = recs["parents_closed"]["basin_1111"] > recs["parents_open"]["basin_1111"]
    print("  closed core is all four=%s   open core smaller=%s   basin larger under closure=%s" % (a, b, c))
    n = int(a) + int(b) + int(c)
    status = "CONFIRMED" if n == 3 else ("PARTIAL" if n == 2 else "REFUTED")
    print("H3 (intergenerational closure makes the community one and the norm wider): %s" % status)
    F.save("probe_coleman_parents", {"control": control, "forms": recs, "H3": status})


if __name__ == "__main__":
    main()
