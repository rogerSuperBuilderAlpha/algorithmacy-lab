"""Probe Q101 (H1-H4) — what does a coordination distinguish?

Reads the specified joint state of the binding distinction across triadic forms and dyadic controls.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q101_what_it_distinguishes.probe_what_it_distinguishes
"""

import csv
import os

from org_frontier.questions.q101_what_it_distinguishes import forms as F


def main():
    print("PROBE Q101 (H1-H4) — the specified joint state of the binding distinction")
    print("=" * 78)
    tri = {}
    for name, (rules, labels) in F.TRIADIC.items():
        bind = F.binding_specified_state(rules, labels)
        joint = F.max_joint_specified_state(rules, labels)
        tri[name] = {"bind": bind, "joint": joint}
        if bind:
            print(f"  {name:<18} binding {bind[0]} specifies effect={bind[1]} cause={bind[2]}")
        if joint:
            print(f"  {'':18} joint   {joint[0]}->{joint[1]} specifies {joint[2]}")
    dya = {}
    for name, (rules, labels) in F.DYADIC.items():
        dya[name] = F.binding_specified_state(rules, labels)
        print(f"  {name:<18} binding {dya[name]}")

    rr = tri["read_recipient"]["bind"]
    h1 = rr is not None and len(rr[0]) >= 2
    h2 = rr is not None and set(rr[1]) == {1}
    h3 = all(v is None for v in dya.values())
    h4 = all(t["bind"] is not None and set(t["bind"][1]) == {1} for t in tri.values())
    print("=" * 78)
    print(f"  H1 the binding distinction specifies a multi-party joint state:   {h1}")
    print(f"  H2 the joint state is the determination-firing (all-ones) config: {h2}")
    print(f"  H3 no dyadic form specifies a multi-party joint state:            {h3}")
    print(f"  H4 every triad distinguishes the all-present success state:       {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "what_it_distinguishes.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "class", "binding_purview", "effect_state", "cause_state"])
        for name, t in tri.items():
            b = t["bind"]
            w.writerow([name, "triadic", "|".join(b[0]) if b else "", b[1] if b else "", b[2] if b else ""])
        for name, b in dya.items():
            w.writerow([name, "dyadic", "|".join(b[0]) if b else "", b[1] if b else "", b[2] if b else ""])


if __name__ == "__main__":
    main()
