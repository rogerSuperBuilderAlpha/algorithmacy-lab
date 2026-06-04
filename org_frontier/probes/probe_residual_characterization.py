"""Probe 125 (M1) — characterize the holistic residual.

Question: connectivity decides ~93% of the n=3 verdict, and neither per-node influence (#13) nor
per-function synergy (#106) closes the rest. What do the misclassified wirings share? Hypothesis: the
residual forms carry a dynamical signature — degenerate attractors or a non-invertible global map — that
connectivity does not see. Method: enumerate the 4096 wirings; for each build connectivity features
(edges, bidirectional-node count, strong connectivity), synergy features (per-function interaction), and
global-dynamics features (fixed points, reachable-set size, invertibility, attractor period), plus the
exact verdict; cache the panel; report the residual set under the connectivity rule and the dynamics it
shares.

Writes: org_frontier/probes/results/residual_panel.csv (read by Probes 126, 127).

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_residual_characterization
"""

import csv
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from .lib import verdict
from org_frontier.classifier.classifier import cm_from_rules
from .probe_joint_influence_v2 import _interaction

LABELS = ("A", "B", "C")
RESULTS = os.path.join(os.path.dirname(__file__), "results")
PANEL = os.path.join(RESULTS, "residual_panel.csv")


def _f(table):
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def _strongly_connected(cm):
    n = cm.shape[0]
    def reach(s):
        seen, st = set(), [s]
        while st:
            u = st.pop()
            for v in range(n):
                if cm[u, v] and v not in seen:
                    seen.add(v)
                    st.append(v)
        return seen
    return all(set(range(n)) - {s} <= reach(s) for s in range(n))


def _dynamics(rules):
    states = [tuple((s >> i) & 1 for i in range(3)) for s in range(8)]
    nxt = {s: tuple(int(rules[i](s)) for i in range(3)) for s in states}
    fixed = sum(nxt[s] == s for s in states)
    reachable = len(set(nxt.values()))
    invertible = int(reachable == 8)
    periods = []
    for s in states:
        seen, cur = [], s
        while cur not in seen:
            seen.append(cur)
            cur = nxt[cur]
        periods.append(len(seen) - seen.index(cur))
    return fixed, reachable, invertible, max(periods)


def build_panel():
    os.makedirs(RESULTS, exist_ok=True)
    tables = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]
    rows = []
    for ta in tables:
        for tb in tables:
            for tc in tables:
                fa, fb, fc = _f(ta), _f(tb), _f(tc)
                rules = [lambda x: fa(x[1], x[2]), lambda x: fb(x[0], x[2]), lambda x: fc(x[0], x[1])]
                cm = cm_from_rules(rules)
                in_deg, out_deg = cm.sum(axis=0), cm.sum(axis=1)
                n_bidir = int(sum((in_deg[i] > 0) and (out_deg[i] > 0) for i in range(3)))
                syn = [max(_interaction(t, 0), _interaction(t, 1)) for t in (ta, tb, tc)]
                fixed, reach, inv, per = _dynamics(rules)
                rows.append({
                    "n_edges": int(cm.sum()), "n_bidir": n_bidir,
                    "strongly_connected": int(_strongly_connected(cm)),
                    "syn_sum": sum(syn), "syn_min": min(syn), "syn_max": max(syn),
                    "n_fixed": fixed, "n_reachable": reach, "invertible": inv, "max_period": per,
                    "triadic": int(verdict(rules, LABELS).structure == "triadic"),
                })
    with open(PANEL, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return rows


def main():
    print("PROBE 125 (M1) — characterizing the holistic residual (4096 wirings)")
    print("=" * 68)
    rows = build_panel()
    y = np.array([r["triadic"] for r in rows])
    nbid = np.array([r["n_bidir"] for r in rows])
    rule = (nbid == 3).astype(int)         # the connectivity rule from #94
    residual = rule != y
    fp = (rule == 1) & (y == 0)            # 3-bidirectional but dyadic
    fn = (rule == 0) & (y == 1)            # not-3-bidirectional but triadic
    print(f"  {len(y)} wirings, {int(y.sum())} triadic; connectivity rule (n_bidir==3) accuracy = {1-residual.mean():.4f}")
    print(f"  residual = {int(residual.sum())} forms: {int(fp.sum())} false positives, {int(fn.sum())} false negatives")
    for name, mask in (("residual (misclassified)", residual), ("correctly classified", ~residual)):
        inv = np.mean([r["invertible"] for r, m in zip(rows, mask) if m])
        per = np.mean([r["max_period"] for r, m in zip(rows, mask) if m])
        fx = np.mean([r["n_fixed"] for r, m in zip(rows, mask) if m])
        print(f"  {name:<26} invertible={inv:.2f}  max_period={per:.2f}  n_fixed={fx:.2f}")
    print(f"  wrote {PANEL}")
    print("=" * 68)
    print("  Reading: a clear dynamical difference between the residual and the rest names the missing")
    print("  ingredient connectivity cannot see. Similar dynamics on both sides says the residual is not")
    print("  a dynamics feature, leaving it genuinely holistic.")
    print("=" * 68)


if __name__ == "__main__":
    main()
