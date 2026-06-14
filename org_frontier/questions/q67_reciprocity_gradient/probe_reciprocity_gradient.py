"""Probe Q67 (H1-H4) — reciprocity gradient: from feed-forward relay to closed ring.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q67_reciprocity_gradient.probe_reciprocity_gradient
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q67_reciprocity_gradient.forms import LEVELS, LABELS, check_controls


def main():
    print("PROBE Q67 (H1-H4) — reciprocity gradient")
    print("=" * 64)
    print(check_controls(verdict))
    data, rows = {}, []
    for name, rules in LEVELS:
        v = verdict(rules, LABELS)
        core, cphi = major_complex(rules, LABELS)
        sz = len(core or ())
        data[name] = (v.structure, v.max_phi, sz, cphi)
        print(f"  {name:<16} {v.structure:<8} Φ_MIP={v.max_phi:.4f}  core={core} (size {sz}, Φ={cphi:.4f})")
        rows.append((name, v.structure, f"{v.max_phi:.6f}", "|".join(core or ()), sz, f"{cphi:.6f}"))
    h1 = data["L0_relay"][0] == "dyadic"
    h2 = data["L1_end_loop"][0] == "triadic" and data["L1_end_loop"][2] == 2
    h3 = data["L2_open_chain"][2] == 2 and data["L3_closed_ring"][2] == 4
    h4 = data["L0_relay"][1] < data["L2_open_chain"][1] < data["L3_closed_ring"][1]
    print("=" * 64)
    print(f"  L0 dyadic: {h1} | L1 triadic core-2: {h2}")
    print(f"  core jumps 2 (L2) -> 4 (L3) at closure: {h3}")
    print(f"  Φ monotone L0<L2<L3: {h4}")
    print(f"  H1 VERDICT: {'CONFIRMED' if h1 else 'REFUTED'}")
    print(f"  H2 VERDICT: {'CONFIRMED' if h2 else 'REFUTED'}")
    print(f"  H3 VERDICT: {'CONFIRMED' if h3 else 'REFUTED'}")
    print(f"  H4 VERDICT: {'CONFIRMED' if h4 else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "reciprocity_gradient.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["level", "structure", "max_phi", "core", "core_size", "core_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()
