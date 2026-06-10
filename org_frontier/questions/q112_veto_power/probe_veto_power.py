"""Probe Q112 (H1-H4) — veto power, and how it differs from value capture.

Reads which parties can collapse the coordination by withdrawing, and sets that against the Shapley value
of Q111 and the sub-coalition values.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q112_veto_power.probe_veto_power
"""

import csv
import os

from org_frontier.questions.q111_shapley_value import forms as q111
from org_frontier.questions.q112_veto_power import forms as F


def main():
    print("PROBE Q112 (H1-H4) — veto power vs value capture")
    print("=" * 72)
    vetoes = F.core_vetoes()
    spec = F.spectator_veto()
    sub = F.subcoalition_values()
    sv, phi = q111.shapley(*q111.read_recipient())
    print(f"  core vetoes (defection collapses the triad): {vetoes}")
    print(f"  spectator veto (defection collapses the core): {spec}")
    print(f"  Shapley values: {sv}")
    print(f"  sub-coalition values: {sub}")

    veto_count = sum(vetoes.values())
    h1 = all(vetoes.values())
    h2 = not spec
    h3 = veto_count == 3 and (max(sv.values()) - min(sv.values())) > 1e-2
    h4 = sub["E,R"] < sub["M,R"] and sub["E,R"] < sub["E,M"]
    print("=" * 72)
    print(f"  H1 every core party holds a veto:                          {h1}")
    print(f"  H2 a non-core spectator holds no veto:                     {h2}")
    print(f"  H3 veto is universal ({veto_count}/3) but value is unequal: {h3}")
    print(f"  H4 the coordination is not a unanimity game (asymmetric):  {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")

    d_ = os.path.join(os.path.dirname(__file__), "results")
    os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "veto_power.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["party", "has_veto", "shapley_value"])
        for p in ("E", "M", "R"):
            w.writerow([p, vetoes[p], sv[p]])
        w.writerow(["X_spectator", spec, ""])


if __name__ == "__main__":
    main()
