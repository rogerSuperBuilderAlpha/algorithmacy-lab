"""Probe Q106 (H1-H4) — the catalog of design operations.

Reads the verdict before and after each named operation, and tests the build/break directions, the
inverse-pair structure, and the three-lever partition.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q106_design_operations.probe_design_operations
"""

import csv
import os
from collections import defaultdict

from org_frontier.probes.lib import verdict
from org_frontier.questions.q106_design_operations import forms as F


def main():
    print("PROBE Q106 (H1-H4) — design operations and their verdict effects")
    print("=" * 80)
    rows = {}
    for name, (lever, direction, br, bl, ar, al) in F.OPERATIONS.items():
        before = verdict(br, bl).structure
        after = verdict(ar, al).structure
        rows[name] = {"lever": lever, "direction": direction, "before": before, "after": after}
        print(f"  {name:<18} [{lever:<11} {direction:<5}] {before:<8} -> {after}")

    builds = [r for r in rows.values() if r["direction"] == "build"]
    breaks = [r for r in rows.values() if r["direction"] == "break"]
    by_lever = defaultdict(lambda: {"build": 0, "break": 0})
    for r in rows.values():
        by_lever[r["lever"]][r["direction"]] += 1

    h1 = all(r["before"] == "dyadic" and r["after"] == "triadic" for r in builds)
    h2 = all(r["before"] == "triadic" and r["after"] == "dyadic" for r in breaks)
    # inverse pairs: per lever, build's after == break's before (triadic), build's before == break's after
    h3 = True
    for lever in by_lever:
        b = next(r for r in rows.values() if r["lever"] == lever and r["direction"] == "build")
        k = next(r for r in rows.values() if r["lever"] == lever and r["direction"] == "break")
        if not (b["after"] == k["before"] and b["before"] == k["after"]):
            h3 = False
    h4 = len(by_lever) == 3 and all(v["build"] == 1 and v["break"] == 1 for v in by_lever.values())

    print("=" * 80)
    print(f"  levers: {dict(by_lever)}")
    print(f"  H1 every build operation: dyadic -> triadic:          {h1}")
    print(f"  H2 every break operation: triadic -> dyadic:          {h2}")
    print(f"  H3 build and break are inverse pairs per lever:       {h3}")
    print(f"  H4 three levers, each one build and one break:        {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "design_operations.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["operation", "lever", "direction", "before", "after"])
        for name, r in rows.items():
            w.writerow([name, r["lever"], r["direction"], r["before"], r["after"]])


if __name__ == "__main__":
    main()
