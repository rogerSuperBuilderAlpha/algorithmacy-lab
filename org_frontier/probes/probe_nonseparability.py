"""Probe 106 (C1) — does non-separability close the N&S residual?

Question: connectivity decides 93% of the n=3 verdict; the last 7% turns on function content (Probe 94).
Parity / XOR determinations are special everywhere (#10, #28, #43, #56). Is "all three nodes
bidirectionally coupled AND the functions carry interaction (non-separable)" the exact condition?
Hypothesis: adding a per-function synergy (interaction) feature to the connectivity features closes the
residual to zero error. Method: enumerate the 4096 wirings; for each compute connectivity features
(edges, bidirectional-node count) and synergy features (the interaction term of each node's function,
summarized); fit a decision tree and check whether the verdict is now separated perfectly.

Run:  ~/iit-playground/venv-4.0/bin/python -m org_frontier.probes.probe_nonseparability
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
from .probe_joint_influence_v2 import _interaction

LABELS = ("A", "B", "C")


def _f(table):
    return lambda a, b: table[(a & 1) | ((b & 1) << 1)]


def main():
    print("PROBE 106 (C1) — connectivity + non-separability as an exact N&S condition")
    print("=" * 70)
    tables = [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]
    Xc, Xcs, y = [], [], []
    for ta in tables:
        for tb in tables:
            for tc in tables:
                fa, fb, fc = _f(ta), _f(tb), _f(tc)
                rules = [lambda x: fa(x[1], x[2]), lambda x: fb(x[0], x[2]), lambda x: fc(x[0], x[1])]
                cm = cm_from_rules(rules)
                in_deg, out_deg = cm.sum(axis=0), cm.sum(axis=1)
                n_bidir = int(sum((in_deg[i] > 0) and (out_deg[i] > 0) for i in range(3)))
                # per-function interaction (synergy): max over the function's two input positions
                syn = [max(_interaction(t, 0), _interaction(t, 1)) for t in (ta, tb, tc)]
                conn = [int(cm.sum()), n_bidir]
                Xc.append(conn)
                Xcs.append(conn + [sum(syn), min(syn), max(syn)])
                y.append(int(verdict(rules, LABELS).structure == "triadic"))
    Xc, Xcs, y = np.array(Xc), np.array(Xcs), np.array(y)

    def acc(X, names, depth):
        t = DecisionTreeClassifier(max_depth=depth, random_state=0).fit(X, y)
        return t.score(X, y), t

    a_conn, _ = acc(Xc, ["n_edges", "n_bidir"], 3)
    a_full, tree = acc(Xcs, ["n_edges", "n_bidir", "syn_sum", "syn_min", "syn_max"], 5)
    print(f"  {len(y)} wirings, {int(y.sum())} triadic")
    print(f"  connectivity only          accuracy = {a_conn:.4f}")
    print(f"  connectivity + synergy     accuracy = {a_full:.4f}")
    # the targeted hand condition: all three nodes bidirectional AND all functions non-separable
    cond = (Xcs[:, 1] == 3) & (Xcs[:, 3] > 0)   # n_bidir==3 and min synergy > 0
    print(f"  hand condition (3 bidirectional AND every function non-separable) agreement = {(cond==y).mean():.4f}")
    print("  mined rule (connectivity + synergy):")
    print(export_text(tree, feature_names=["n_edges", "n_bidir", "syn_sum", "syn_min", "syn_max"]).rstrip())
    print("=" * 70)
    if a_full > a_conn + 0.01:
        print(f"  Reading: synergy lifts the separation from {a_conn:.3f} to {a_full:.3f} — the residual the")
        print("  graph could not decide turns on whether the functions carry interaction, so non-separability")
        print("  is the missing ingredient on top of bidirectional coupling.")
    else:
        print("  Reading: synergy does not lift the separation; the residual is not a non-separability term,")
        print("  and an exact structural-plus-synergy condition for n=3 triadicity remains unfound.")
    print("=" * 70)


if __name__ == "__main__":
    main()
