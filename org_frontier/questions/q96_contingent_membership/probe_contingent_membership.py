"""Probe Q96 (H1-H4) — does state-contingent participation integrate?

Reads the verdict and major complex for the contingent form, against the always-on and never controls.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q96_contingent_membership.probe_contingent_membership
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q96_contingent_membership import forms as F


def read(name, builder):
    rules, lab = builder()
    v = verdict(rules, lab)
    core, phi = major_complex(rules, lab)
    core = tuple(core or ())
    print(f"  {name:<12} {v.structure:<8} sysΦ={v.max_phi:.3f}  major={core} (φ={phi:.3f})")
    return {"name": name, "structure": v.structure, "sys_phi": round(float(v.max_phi), 3), "core": core}


def main():
    print("PROBE Q96 (H1-H4) — state-contingent membership of the recipient")
    print("=" * 74)
    cont = read("contingent", F.contingent)
    always = read("always", F.always)
    never = read("never", F.never)

    h1 = cont["structure"] == "triadic"
    h2 = cont["sys_phi"] < 2.0
    h3 = "R" in cont["core"]
    h4 = "T" in cont["core"]
    print("=" * 74)
    print(f"  H1 contingent participation integrates (triadic):     {h1} ({cont['structure']})")
    print(f"  H2 contingency weakens it (Φ < always-on 2.0):        {h2} ({cont['sys_phi']})")
    print(f"  H3 the recipient is in the contingent core:           {h3} (core={cont['core']})")
    print(f"  H4 the gate is in the contingent core:                {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "contingent_membership.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "structure", "sys_phi", "major_complex"])
        for r in (cont, always, never):
            w.writerow([r["name"], r["structure"], r["sys_phi"], "|".join(r["core"])])


if __name__ == "__main__":
    main()
