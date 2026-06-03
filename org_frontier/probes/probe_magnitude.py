"""Probe 17 — what does Φ magnitude track?

Paper 3 withdrew Φ-as-readability-scale. Open question: what does the magnitude index? Over the
complete strict-mediation n=3 family (reusing corpus.population.enumerate_family, 256 forms) compute
Φ and candidate structural features of the determination, and rank-correlate each with Φ.

H17: Φ magnitude tracks structural quantities — the mediator's arity (how many parties it reads),
whether its rule is parity (XOR/XNOR), and the parties' feedback richness — even though it is not a
coordination-readability scale.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_magnitude
"""

import csv
import os

from org_frontier.classifier.classifier import classify_rules, cm_from_rules
from org_frontier.corpus.population import enumerate_family

LABELS = ("W", "S", "C")
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


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
            avg = (i + j) / 2.0 + 1
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    cov = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    vx = sum((rx[i] - mx) ** 2 for i in range(n)) ** 0.5
    vy = sum((ry[i] - my) ** 2 for i in range(n)) ** 0.5
    return cov / (vx * vy) if vx and vy else 0.0


def _s_table(rules):
    """S' as a function of (W, C): evaluate rules[1] over the 4 (W,C) combos."""
    return [rules[1]((w, 0, c)) for c in (0, 1) for w in (0, 1)]   # index w | c<<1


def main():
    phis, arity, parity, party_fb = [], [], [], []
    for _label, rules in enumerate_family():
        v = classify_rules(rules, labels=LABELS)
        cm = cm_from_rules(rules)
        t = _s_table(rules)
        is_parity = tuple(t) in {(0, 1, 1, 0), (1, 0, 0, 1)}     # XOR / XNOR
        s_arity = int(cm[0, 1]) + int(cm[2, 1])                  # how many parties S reads
        fb = int(cm[1, 0]) + int(cm[1, 2])                       # how many parties read S
        phis.append(v.max_phi)
        arity.append(s_arity)
        parity.append(1 if is_parity else 0)
        party_fb.append(fb)

    os.makedirs(_RESULTS, exist_ok=True)
    with open(os.path.join(_RESULTS, "magnitude.csv"), "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["phi", "s_arity", "parity", "party_feedback"])
        for row in zip(phis, arity, parity, party_fb):
            w.writerow(row)

    print("PROBE 17 — what Φ magnitude tracks (256 strict-mediation forms)")
    print("=" * 72)
    print(f"  Spearman ρ(Φ, mediator arity / #parties S reads) : {_spearman(arity, phis):+.3f}")
    print(f"  Spearman ρ(Φ, parity determination)              : {_spearman(parity, phis):+.3f}")
    print(f"  Spearman ρ(Φ, party feedback / #parties read S)  : {_spearman(party_fb, phis):+.3f}")
    print(f"  distinct Φ values: {sorted(set(round(p,3) for p in phis))}")
    print("=" * 72)


if __name__ == "__main__":
    main()
