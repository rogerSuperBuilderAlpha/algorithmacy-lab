"""Probe 48 — Φ vs coordination performance (Engel & Malone precedent).

Engel & Malone (2018) found that 4-person groups with higher measured Φ performed a range of tasks
more effectively (higher collective intelligence). Test the analogue on coordination forms: does
exact Φ correlate with a coordination-performance proxy across the strict-mediation family?

Performance proxy = the success rate from Probe 29 (mean over initial states of the attractor
fraction in which the system commits a match). Correlate with Φ over the 256-form family.

H48: Φ correlates positively with the performance proxy — more integrated coordination forms reach
successful determinations more reliably (the Engel-Malone direction), OR the relationship is weak
(as Probe 29 hinted: triadic ≠ automatically higher success). Report whichever holds.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_phi_performance
"""

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family
from .probe_variance import success_rate


def _spearman(xs, ys):
    n = len(xs)
    def ranks(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            for k in range(i, j + 1):
                r[order[k]] = (i + j) / 2.0 + 1
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    vx = sum((rx[i] - mx) ** 2 for i in range(n)) ** 0.5
    vy = sum((ry[i] - my) ** 2 for i in range(n)) ** 0.5
    return cov / (vx * vy) if vx and vy else 0.0


def main():
    phis, perf = [], []
    for _label, rules in enumerate_family():
        v = classify_rules(rules, labels=("W", "S", "C"))
        phis.append(v.max_phi)
        perf.append(success_rate(rules))
    rho = _spearman(phis, perf)

    # mean performance by triadic/dyadic
    tri = [perf[i] for i in range(len(phis)) if phis[i] > 1e-9]
    dya = [perf[i] for i in range(len(phis)) if phis[i] <= 1e-9]
    print("PROBE 48 — Φ vs coordination performance (Engel-Malone precedent)")
    print("=" * 70)
    print(f"  forms: {len(phis)}")
    print(f"  Spearman ρ(Φ, success rate): {rho:+.3f}")
    if tri:
        print(f"  mean success | triadic (Φ>0): {sum(tri)/len(tri):.3f}  (n={len(tri)})")
    if dya:
        print(f"  mean success | dyadic  (Φ=0): {sum(dya)/len(dya):.3f}  (n={len(dya)})")
    print("=" * 70)
    print("  Engel & Malone (2018): higher group Φ -> higher collective performance. Here we test")
    print("  whether exact Φ tracks a coordination-success proxy across the model family.")
    print("=" * 70)


if __name__ == "__main__":
    main()
