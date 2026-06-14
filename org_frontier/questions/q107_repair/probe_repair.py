"""Probe Q107 (H1-H4) — is repair lever-specific?

Reads the minimal repair of a binding-damaged and a liveness-damaged triad, and tests whether the repair
restores the damaged lever or routes around it.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q107_repair.probe_repair
"""

import csv
import os

from org_frontier.questions.q105_construction_distance import forms as q105
from org_frontier.questions.q107_repair import forms as F


def main():
    print("PROBE Q107 (H1-H4) — repairing a damaged triad")
    print("=" * 74)
    _, triadic = q105.classify_family()
    rows = {}
    for name, (bits, lever_bits) in F.DAMAGE.items():
        dist, steps = F.repair(bits, triadic)
        in_lever = steps <= set(lever_bits)
        rows[name] = {"dist": dist, "steps": sorted(steps), "lever_bits": lever_bits, "in_lever": in_lever}
        print(f"  {name:<18} repair distance {dist} via bits {sorted(steps)}  "
              f"(lever bits {list(lever_bits)}, lever-specific={in_lever})")

    bd = rows["binding_damaged"]
    ld = rows["liveness_damaged"]
    h1 = bd["dist"] >= 1 and ld["dist"] >= 1
    h2 = set(bd["steps"]) <= set(F.MEDIATOR_BITS)
    h3 = set(ld["steps"]) <= set(F.COUNTERPART_READ_BITS)
    # lever-specific: each damaged form's distance-1 repair touches only its own lever, not the other
    h4 = (set(bd["steps"]) & set(F.COUNTERPART_READ_BITS) == set() and
          set(ld["steps"]) & set(F.MEDIATOR_BITS) == set() and
          bd["in_lever"] and ld["in_lever"])
    print("=" * 74)
    print(f"  H1 both damaged triads are repairable:                {h1}")
    print(f"  H2 binding damage is repaired at the mediator:        {h2}")
    print(f"  H3 liveness damage is repaired at the party's read:   {h3}")
    print(f"  H4 repair is lever-specific (no routing around):      {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "repair.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["damage", "repair_distance", "repair_bits", "lever_specific"])
        for name, r in rows.items():
            w.writerow([name, r["dist"], "|".join(map(str, r["steps"])), r["in_lever"]])


if __name__ == "__main__":
    main()
