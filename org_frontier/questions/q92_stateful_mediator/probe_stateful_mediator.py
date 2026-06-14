"""Probe Q92 (H1-H4) — does a mediator's memory substitute for a live read?

Reads the verdict and major complex for the live triad and three memory variants.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q92_stateful_mediator.probe_stateful_mediator
"""

import csv
import os

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q92_stateful_mediator import forms as F


def read(name, builder):
    rules, lab = builder()
    v = verdict(rules, lab)
    core, phi = major_complex(rules, lab)
    core = tuple(core or ())
    print(f"  {name:<18} {v.structure:<8} sysΦ={v.max_phi:.2f}  major={core} (φ={phi:.2f})")
    return {"name": name, "structure": v.structure, "sys_phi": round(float(v.max_phi), 3), "core": core}


def main():
    print("PROBE Q92 (H1-H4) — stateful mediator: does memory substitute for a live read?")
    print("=" * 78)
    live = read("live", F.live)
    track = read("tracking_memory", F.tracking_memory)
    frozen = read("frozen_memory", F.frozen_memory)
    selfm = read("self_memory", F.self_memory)

    h1 = track["structure"] == "triadic"
    h2 = frozen["structure"] == "dyadic"
    h3 = selfm["structure"] == "dyadic"
    h4 = "Mem" in track["core"]
    print("=" * 78)
    print(f"  H1 a tracking memory preserves the triad:          {h1} ({track['structure']})")
    print(f"  H2 a frozen memory collapses to dyadic:            {h2} ({frozen['structure']})")
    print(f"  H3 self-memory alone is dyadic (no recipient):     {h3} ({selfm['structure']})")
    print(f"  H4 the tracking memory node is in the core:        {h4} (core={track['core']})")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "stateful_mediator.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "structure", "sys_phi", "major_complex"])
        for r in (live, track, frozen, selfm):
            w.writerow([r["name"], r["structure"], r["sys_phi"], "|".join(r["core"])])


if __name__ == "__main__":
    main()
