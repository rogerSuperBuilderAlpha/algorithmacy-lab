"""Probe 94 (#45) — a necessary-and-sufficient structural condition for n=3 triadicity.

Question: across all 4096 arbitrary 3-node wirings (each node an arbitrary Boolean function of the other
two), is there a structural condition on the wiring that exactly separates triadic from dyadic? Hypothesis:
yes — triadicity is decided by connectivity, specifically that all three nodes are bidirectionally coupled
and the influence graph is strongly connected. Method: enumerate the 4096 wirings, classify each with the
exact verdict, build structural features (edge count, number of bidirectional nodes, strong connectivity),
and fit a shallow decision tree; if it separates the verdict perfectly, the tree is the N&S condition.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_ns_theorem
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text

from .lib import verdict
from org_frontier.classifier.classifier import cm_from_rules

LABELS = ("A", "B", "C")


def _f(table):
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def _strongly_connected(cm):
    n = cm.shape[0]
    def reach(src):
        seen, stack = set(), [src]
        while stack:
            u = stack.pop()
            for v in range(n):
                if cm[u, v] and v not in seen:
                    seen.add(v)
                    stack.append(v)
        return seen
    return all(len(reach(s)) == n - 1 or reach(s) >= set(range(n)) - {s} for s in range(n)) and \
        all(set(range(n)) - {s} <= reach(s) for s in range(n))


def main():
    print("PROBE 94 (#45) — N&S structural condition for n=3 triadicity (all 4096 wirings)")
    print("=" * 76)
    X, y = [], []
    tables = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]
    for ta in tables:
        for tb in tables:
            for tc in tables:
                fa, fb, fc = _f(ta), _f(tb), _f(tc)
                rules = [lambda x: fa(x[1], x[2]), lambda x: fb(x[0], x[2]), lambda x: fc(x[0], x[1])]
                cm = cm_from_rules(rules)
                in_deg = cm.sum(axis=0)
                out_deg = cm.sum(axis=1)
                n_bidir = int(sum((in_deg[i] > 0) and (out_deg[i] > 0) for i in range(3)))
                feat = [int(cm.sum()), n_bidir, int(_strongly_connected(cm))]
                X.append(feat)
                y.append(int(verdict(rules, LABELS).structure == "triadic"))
    X = np.array(X)
    y = np.array(y)
    names = ["n_edges", "n_bidirectional_nodes", "strongly_connected"]
    tree = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X, y)
    acc = tree.score(X, y)
    print(f"  {len(y)} wirings, {int(y.sum())} triadic ({100*y.mean():.1f}%)")
    print(f"  decision-tree training accuracy on structural features = {acc:.4f}")
    # the simplest hand condition: all three nodes bidirectional and strongly connected
    cond = (X[:, 1] == 3) & (X[:, 2] == 1)
    print(f"  hand condition (3 bidirectional nodes AND strongly connected) agreement = {(cond == y).mean():.4f}")
    print("  mined rule:")
    print(export_text(tree, feature_names=names).rstrip())
    print("=" * 76)
    if acc == 1.0:
        print("  Reading: the verdict is decided exactly by the wiring's connectivity — a structural N&S")
        print("  condition exists for n=3, with no dependence on the specific Boolean functions.")
    else:
        print("  Reading: connectivity alone does not separate the verdict; some wirings with the same")
        print("  connectivity differ in kind, so the function content matters beyond the graph.")
    print("=" * 76)


if __name__ == "__main__":
    main()
