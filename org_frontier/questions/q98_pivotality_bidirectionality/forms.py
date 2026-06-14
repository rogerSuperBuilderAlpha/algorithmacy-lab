"""Q98: decoupling a node's reading (in-influence) from its influence (out-influence).

Finding 8 ties core membership to bidirectional coupling and pivotality together. This separates the two
sides of bidirectionality and asks whether one can compensate the other. For each node of a full-family
wiring (each node reads all others), two quantities are computed:

- in-influence: the mean Boolean sensitivity of the node's own update to its inputs — how much it reads.
- out-influence: the mean Boolean sensitivity of the other nodes' updates to this node — how much it is
  read.

Both are reused from Q90's construction; out-influence is exactly Q90's measure. The question is whether
membership in the major complex needs both substantial (a conjunctive gate) or whether a large value on
one axis compensates a small value on the other.

Imported by `probe_pivotality_bidirectionality.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import major_complex
from org_frontier.questions.q90_membership_law_scaling.forms import sample_wiring, _sensitivity, _labels


def node_influences(n, tables, others):
    """Per-node (in_influence, out_influence).

    in_influence(i)  = mean sensitivity of f_i to its own k inputs.
    out_influence(i) = mean over the other nodes j that read i of the sensitivity of f_j to i.
    """
    k = n - 1
    in_infl = [float(np.mean([_sensitivity(tables[i], b, k) for b in range(k)])) for i in range(n)]
    out_infl = []
    for i in range(n):
        sens = []
        for j in range(n):
            if j == i:
                continue
            if i in others[j]:
                sens.append(_sensitivity(tables[j], others[j].index(i), k))
        out_infl.append(float(np.mean(sens)) if sens else 0.0)
    return in_infl, out_infl


def observations(n, N, rng):
    """Yield one dict per node per wiring: in_influence, out_influence, in_core."""
    labels = _labels(n)
    rows = []
    for _ in range(N):
        rules, tables, others = sample_wiring(n, rng)
        core = set(major_complex(rules, labels)[0] or ())
        in_infl, out_infl = node_influences(n, tables, others)
        for i in range(n):
            rows.append({
                "in_influence": round(in_infl[i], 4),
                "out_influence": round(out_infl[i], 4),
                "in_core": labels[i] in core,
            })
    return rows
