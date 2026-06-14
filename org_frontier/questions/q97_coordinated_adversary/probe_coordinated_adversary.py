"""Probe Q97 (H1-H4) — can a coalition flip the verdict that a single non-core agent cannot?

Reads the verdict and major complex for a coalition of observers, a coalition of sources, a bridging
coalition loop, and the single bidirectional-pivotal control.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q97_coordinated_adversary.probe_coordinated_adversary
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q97_coordinated_adversary import forms as F


def read(name, builder):
    rules, lab = builder()
    v = verdict(rules, lab)
    core, phi = major_complex(rules, lab)
    core = tuple(core or ())
    print(f"  {name:<16} {v.structure:<8} sysΦ={v.max_phi:.2f}  major={core} (φ={phi:.2f})")
    return {"name": name, "structure": v.structure, "sys_phi": round(float(v.max_phi), 3), "core": core}


def main():
    print("PROBE Q97 (H1-H4) — coordinated adversary: can a coalition flip the verdict?")
    print("=" * 78)
    ro = read("two_read_only", F.two_read_only)
    eo = read("two_emit_only", F.two_emit_only)
    loop = read("external_loop", F.external_loop)
    bi = read("single_bidir", F.single_bidir)

    h1 = ro["structure"] == "triadic" and set(ro["core"]) == {"E", "M", "R"}
    h2 = eo["structure"] == "dyadic"
    h3 = set(loop["core"]) == {"E", "M", "R"} or "X2" in loop["core"]
    h4 = bi["structure"] == "triadic" and "X" in bi["core"]
    print("=" * 78)
    print(f"  H1 two read-only agents cannot destroy the triad:          {h1} (core={ro['core']})")
    print(f"  H2 two emit-only sources cannot manufacture a triad:       {h2} ({eo['structure']})")
    print(f"  H3 coalition gains no influence without membership:        {h3} (core={loop['core']})")
    print(f"  H4 a single bidirectional-pivotal agent flips and joins:   {h4} (core={bi['core']})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "coordinated_adversary.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "structure", "sys_phi", "major_complex"])
        for r in (ro, eo, loop, bi):
            w.writerow([r["name"], r["structure"], r["sys_phi"], "|".join(r["core"])])


if __name__ == "__main__":
    main()
