"""Probe Q75 (H1-H4) — is the triadic core robust to added spectators?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q75_spectator_robustness.probe_spectator_robustness
"""
import csv, os
from org_frontier.probes.lib import major_complex
from org_frontier.questions.q75_spectator_robustness.forms import uncoupled, read_only_spectator, emit_only_spectator


def main():
    print("PROBE Q75 (H1-H4) — spectator robustness of the triadic core")
    print("=" * 70)
    rows = []
    base = {"E", "M", "R"}
    uc = {}
    for k in (1, 2, 3):
        rules, labels = uncoupled(k)
        core, phi = major_complex(rules, labels)
        uc[k] = (set(core or ()), phi)
        print(f"  uncoupled k={k} (n={3+k})  core={core} Φ={phi:.3f}")
        rows.append((f"uncoupled_k{k}", "|".join(core or ()), f"{phi:.4f}"))
    ro_core, ro_phi = major_complex(*read_only_spectator())
    eo_core, eo_phi = major_complex(*emit_only_spectator())
    print(f"  read-only spectator       core={tuple(sorted(ro_core or ()))} Φ={ro_phi:.3f}")
    print(f"  emit-only spectator        core={tuple(sorted(eo_core or ()))} Φ={eo_phi:.3f}")
    rows.append(("read_only", "|".join(ro_core or ()), f"{ro_phi:.4f}"))
    rows.append(("emit_only", "|".join(eo_core or ()), f"{eo_phi:.4f}"))

    h1 = all(uc[k][0] == base and abs(uc[k][1] - 2.0) < 1e-6 for k in (1, 2, 3))
    h2 = set(ro_core or ()) == base
    h3 = set(eo_core or ()) == base
    h4 = h1 and abs(ro_phi - 2.0) < 1e-6 and abs(eo_phi - 2.0) < 1e-6
    print("=" * 70)
    print(f"  uncoupled spectators leave core {{E,M,R}} Φ=2.0 (k=1,2,3): {h1}")
    print(f"  read-only spectator stays out (core {{E,M,R}}): {h2}")
    print(f"  emit-only spectator stays out (core {{E,M,R}}): {h3}")
    print(f"  core Φ invariant at 2.0 across all spectator additions: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "spectator_robustness.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["form", "core", "core_phi"]); w.writerows(rows)


if __name__ == "__main__":
    main()
