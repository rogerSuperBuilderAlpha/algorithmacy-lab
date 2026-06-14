"""Probe Q94 (H1-H4) — can a form hold two coexisting complexes, and what merges them?

Reads the exclusion-resolved set of disjoint maximal complexes for four configurations of two
coordination units: uncoupled, sharing a spectator, one-way bridged, and mutually bridged.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q94_multiple_complexes.probe_multiple_complexes
"""

import csv
import os

from org_frontier.questions.q94_multiple_complexes import forms as F


def main():
    print("PROBE Q94 (H1-H4) — multiple coexisting complexes")
    print("=" * 78)
    configs = {
        "disjoint": F.disjoint(),
        "shared_spectator": F.shared_spectator(),
        "one_way_bridge": F.one_way_bridge(),
        "mutual_bridge": F.mutual_bridge(),
    }
    tilings = {}
    for name, (rules, lab) in configs.items():
        t = F.max_disjoint_complexes(rules, lab)
        tilings[name] = t
        print(f"  {name:<18} {len(t)} complex(es): {t}")

    nodes = lambda t: set().union(*[set(c) for c, _ in t]) if t else set()
    h1 = len(tilings["disjoint"]) == 2
    h2 = len(tilings["shared_spectator"]) == 2
    h3 = len(tilings["one_way_bridge"]) >= 2
    h4 = len(tilings["mutual_bridge"]) == 1 and nodes(tilings["mutual_bridge"]) >= {"A", "B", "C", "D"}

    print("=" * 78)
    print(f"  H1 two uncoupled units -> two disjoint complexes:           {h1}")
    print(f"  H2 a shared spectator does not merge them (still two):      {h2}")
    print(f"  H3 a one-way bridge does not merge them (>=2 complexes):    {h3}")
    print(f"  H4 a mutual bridge merges them into one spanning complex:   {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "multiple_complexes.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["config", "n_complexes", "tiling"])
        for name, t in tilings.items():
            w.writerow([name, len(t), "; ".join(f"{{{','.join(c)}}}={p}" for c, p in t)])


if __name__ == "__main__":
    main()
