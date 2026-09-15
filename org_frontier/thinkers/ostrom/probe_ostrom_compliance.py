"""Probe — Ostrom H4: quasi-voluntary compliance.

Question.  Ostrom (1990: 94): "The initial sanctions used in these systems are surprisingly low"; compliance
           is quasi-voluntary. Does the mutual form rest at all-comply with no sanction standing, and does a
           single lapse return to it? Coleman's closed norm rests only with the sanction standing.
Hypothesis. H4: 111000 fixed in mutual; each single-defector state returns to it; coleman_closed rests at 111.
Run.       ~/iit-playground/venv-4.0/bin/python -m org_frontier.thinkers.ostrom.probe_ostrom_compliance
"""

from org_frontier.thinkers.ostrom import forms as F


def main():
    print("Ostrom H4 — where compliance rests")
    control = F.run_control()
    labels, rules = F.compile_spec(F.SPECS["mutual"])
    fps = ["".join(map(str, s)) for s in F.fixed_points(rules, 6)]
    print("  mutual fixed points: %s" % (" ".join(fps) or "none"))
    rest = (1, 1, 1, 0, 0, 0)
    fixed = "111000" in fps
    returns = {}
    for i in range(3):
        start = [1, 1, 1, 0, 0, 0]
        start[i] = 0
        ok, path = F.reaches(rules, start, rest)
        returns["".join(map(str, start))] = {"returns": ok, "steps": len(path) - 1,
                                             "path": ["".join(map(str, s)) for s in path]}
        print("    lapse %s -> %s in %d steps" % ("".join(map(str, start)), "rest" if ok else "no rest", len(path) - 1))
    lab_c, rules_c = F.compile_spec(F.SPECS["coleman_closed"])
    fps_c = ["".join(map(str, s)) for s in F.fixed_points(rules_c, 3)]
    coleman_standing = fps_c == ["111"]
    print("  coleman_closed fixed points: %s (sanction standing: %s)" % (" ".join(fps_c), coleman_standing))
    all_return = all(v["returns"] for v in returns.values())
    n = sum([fixed, all_return, coleman_standing])
    status = "CONFIRMED" if n == 3 else ("PARTIAL" if n == 2 else "REFUTED")
    print("H4 (compliance rests with the sanction retired, and a lapse is corrected): %s" % status)
    F.save("probe_ostrom_compliance", {"control": control, "mutual_fixed_points": fps, "lapses": returns,
                                       "coleman_fixed_points": fps_c, "H4": status})


if __name__ == "__main__":
    main()
