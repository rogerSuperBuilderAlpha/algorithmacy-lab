"""Probe Q79 (H1-H4) — does the triad emerge gradually as the agent reads the recipient probabilistically?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q79_stochastic_threshold.probe_stochastic_threshold
"""
import csv, os
from org_frontier.probes.lib import max_phi_float
from org_frontier.questions.q79_stochastic_threshold.forms import stochastic_tpm

PS = [0.0, 0.25, 0.5, 0.75, 1.0]


def main():
    print("PROBE Q79 (H1-H4) — stochastic emergence of the triad")
    print("=" * 60)
    phi = {}
    for p in PS:
        ph, _ = max_phi_float(stochastic_tpm(p))
        phi[p] = ph
        print(f"  p={p:<5} Φ={ph:.4f}")
    h1 = abs(phi[1.0] - 2.0) < 1e-6 and phi[0.0] < 1e-6
    h2 = all(phi[PS[i]] <= phi[PS[i + 1]] + 1e-6 for i in range(len(PS) - 1))
    h3 = phi[0.25] > 1e-6 and phi[0.5] > 1e-6 and phi[0.75] > 1e-6
    h4 = phi[0.25] > 1e-6  # smallest p>0 already positive => graded, no flat-zero region
    print("=" * 60)
    print(f"  endpoints p=1 Φ=2.0 / p=0 Φ=0: {h1}")
    print(f"  Φ monotone non-decreasing in p: {h2}")
    print(f"  partial reading (0<p<1) gives Φ>0: {h3}")
    print(f"  emergence graded (Φ>0 at smallest p>0): {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "stochastic_threshold.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["p", "max_phi"])
        for p in PS: w.writerow([p, f"{phi[p]:.6f}"])


if __name__ == "__main__":
    main()
