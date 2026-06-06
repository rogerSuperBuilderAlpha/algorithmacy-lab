"""Probe Q68 (H1-H4) — does a recipient-side triage agent join the core?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q68_triage_gating.probe_triage_gating
"""
import csv, os
from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q68_triage_gating.forms import CONFIGS, LABELS, check_controls


def main():
    print("PROBE Q68 (H1-H4) — recipient-side triage agent")
    print("=" * 64)
    print(check_controls(verdict))
    data, rows = {}, []
    for name, rules in CONFIGS:
        core, phi = major_complex(rules, LABELS)
        t_in = "T" in (core or ())
        data[name] = (core, phi, t_in)
        print(f"  {name:<16} core={core} Φ={phi:.4f}  T_in_core={t_in}  triadic={phi>1e-9}")
        rows.append((name, "|".join(core or ()), f"{phi:.6f}", t_in, phi > 1e-9))
    h1 = not data["monitoring_only"][2]
    h2 = not data["gating_only"][2]
    h3 = data["bidirectional"][2]
    h4 = all(data[n][1] > 1e-9 for n, _ in CONFIGS)
    print("=" * 64)
    print(f"  monitoring T out: {h1} | gating T out: {h2} | bidirectional T in: {h3}")
    print(f"  base triad core present (triadic) in all configs: {h4}")
    print(f"  H1 VERDICT: {'CONFIRMED' if h1 else 'REFUTED'}")
    print(f"  H2 VERDICT: {'CONFIRMED' if h2 else 'REFUTED'}")
    print(f"  H3 VERDICT: {'CONFIRMED' if h3 else 'REFUTED'}")
    print(f"  H4 VERDICT: {'CONFIRMED' if h4 else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "triage_gating.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["config", "core", "phi", "T_in_core", "triadic"]); w.writerows(rows)


if __name__ == "__main__":
    main()
