"""Probe Q71 (H1-H4) — is the outreach triadic verdict robust to stochastic noise?

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.questions.q71_noise_robustness.probe_noise_robustness
"""
import csv, os
from org_frontier.probes.lib import max_phi_float
from org_frontier.questions.q71_noise_robustness.forms import READ_RECIPIENT, BROADCAST, noisy_tpm

EPS = [0.0, 0.05, 0.1, 0.2, 0.3, 0.5]


def main():
    print("PROBE Q71 (H1-H4) — noise robustness of the outreach verdict")
    print("=" * 64)
    tri, dy = {}, {}
    for e in EPS:
        pt, _ = max_phi_float(noisy_tpm(READ_RECIPIENT, e))
        pd, _ = max_phi_float(noisy_tpm(BROADCAST, e))
        tri[e], dy[e] = pt, pd
        print(f"  eps={e:<5} read_recipient Φ={pt:.4f}   broadcast Φ={pd:.4f}")
    h1 = tri[0.05] > 1e-6 and tri[0.1] > 1e-6
    h2 = all(tri[EPS[i]] >= tri[EPS[i+1]] - 1e-6 for i in range(len(EPS)-1))
    h3 = tri[0.5] < 0.1
    h4 = all(dy[e] < 0.1 for e in EPS)
    print("=" * 64)
    print(f"  triad survives small noise (eps<=0.1): {h1}")
    print(f"  Phi degrades monotonically with noise: {h2}")
    print(f"  triad Phi collapses at max noise eps=0.5: {h3}")
    print(f"  broadcast stays low (no spurious triad) across noise: {h4}")
    for h, ok in [("H1", h1), ("H2", h2), ("H3", h3), ("H4", h4)]:
        print(f"  {h} VERDICT: {'CONFIRMED' if ok else 'REFUTED'}")
    d_ = os.path.join(os.path.dirname(__file__), "results"); os.makedirs(d_, exist_ok=True)
    with open(os.path.join(d_, "noise_robustness.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(["eps", "read_recipient_phi", "broadcast_phi"])
        for e in EPS: w.writerow([e, f"{tri[e]:.6f}", f"{dy[e]:.6f}"])


if __name__ == "__main__":
    main()
