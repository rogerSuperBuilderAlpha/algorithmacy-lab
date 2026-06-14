"""Q90: the full n-node family sampler and the two membership conditions, generalized past n=3.

Probe #12 validated the core-membership law (bidirectional coupling + pivotality) on the complete
three-node family, where each node reads the other two. This lifts the same construction to n = 4 and
n = 5: each node reads all n-1 others through an arbitrary Boolean function, so a wiring is a tuple of
n truth tables. For each node it computes the two quantities the law uses — whether the node is
bidirectionally coupled, and its out-influence (mean Boolean sensitivity of the other nodes to it) —
and whether the node sits in the major complex.

n = 6 is out of reach: one major-complex computation is ~9 minutes at n = 6, so the law cannot be
checked there with the exact instrument, which is itself the size ceiling this study probes against.

Imported by `probe_membership_law_scaling.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import major_complex


def _labels(n):
    return tuple(chr(65 + i) for i in range(n))


def _sensitivity(table, bit, k):
    """Boolean sensitivity of a k-input truth table to input `bit`: fraction of inputs where
    flipping that bit flips the output."""
    return sum(table[c] != table[c ^ (1 << bit)] for c in range(2 ** k)) / float(2 ** k)


def sample_wiring(n, rng):
    """Return (rules, tables, others) for one random full-family wiring on n nodes.

    Node i reads every other node through a random Boolean function of n-1 inputs. `others[i]` lists
    the node indices feeding node i, in input-bit order; `tables[i]` is the truth table.
    """
    k = n - 1
    tables, others, rules = [], [], []
    for i in range(n):
        oth = tuple(j for j in range(n) if j != i)
        table = tuple(int(b) for b in rng.integers(0, 2, 2 ** k))
        others.append(oth)
        tables.append(table)

        def make(table=table, oth=oth):
            def f(x):
                idx = 0
                for b, j in enumerate(oth):
                    idx |= (x[j] & 1) << b
                return int(table[idx])
            return f
        rules.append(make())
    return rules, tables, others


def node_stats(n, tables, others):
    """Per-node (bidirectional, out_influence) for a wiring.

    out_influence(i) = mean over the other nodes j of the sensitivity of f_j to i's input position.
    bidirectional(i) = i reads someone (f_i non-constant) AND i influences someone (out_influence>0).
    """
    k = n - 1
    reads_someone = []
    for i in range(n):
        reads_someone.append(any(_sensitivity(tables[i], b, k) > 0 for b in range(k)))
    out_infl = []
    for i in range(n):
        sens = []
        for j in range(n):
            if j == i:
                continue
            if i in others[j]:
                bit = others[j].index(i)
                sens.append(_sensitivity(tables[j], bit, k))
        out_infl.append(float(np.mean(sens)) if sens else 0.0)
    bidir = [bool(reads_someone[i] and out_infl[i] > 0) for i in range(n)]
    return bidir, out_infl


def observations(n, N, rng):
    """Yield one dict per node per sampled wiring: bidirectional, out_influence, in_core."""
    labels = _labels(n)
    rows = []
    for _ in range(N):
        rules, tables, others = sample_wiring(n, rng)
        core, _phi = major_complex(rules, labels)
        core = set(core or ())
        bidir, out_infl = node_stats(n, tables, others)
        for i in range(n):
            rows.append({
                "n": n,
                "bidirectional": bidir[i],
                "out_influence": round(out_infl[i], 4),
                "in_core": labels[i] in core,
            })
    return rows
