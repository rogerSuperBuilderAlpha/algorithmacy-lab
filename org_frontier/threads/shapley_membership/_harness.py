"""Harness for the Shapley-vs-membership thread: compute, for each node of a coordination form, its
Shapley value over the coalition game v(S) = phi_s(S), its single-node influence, and whether it is in
the major complex. Tests whether higher-order pivotality (Shapley) predicts membership better than the
single-node influence used in the core-membership study."""

import itertools
import math
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import major_complex
from foundations.proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def phi_s_of_subset(net, tpm, n, subset):
    """max over reachable states of the system integrated information of the subset (0 if < 2 nodes)."""
    if len(subset) < 2:
        return 0.0
    best = 0.0
    for s in reachable_states(tpm, n):
        st = tuple((s >> i) & 1 for i in range(n))
        try:
            sub = pyphi.Subsystem(net, st, nodes=subset)
            best = max(best, float(new_big_phi.sia(sub).phi))
        except Exception:
            pass
    return best


def coalition_values(rules, labels):
    n = len(labels)
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    v = {}
    for r in range(n + 1):
        for S in itertools.combinations(range(n), r):
            v[S] = phi_s_of_subset(net, tpm, n, S)
    return v, tpm, cm


def shapley(v, n):
    out = []
    for i in range(n):
        others = [j for j in range(n) if j != i]
        tot = 0.0
        for r in range(len(others) + 1):
            for S in itertools.combinations(others, r):
                w = math.factorial(len(S)) * math.factorial(n - len(S) - 1) / math.factorial(n)
                tot += w * (v[tuple(sorted(S + (i,)))] - v[tuple(sorted(S))])
        out.append(tot)
    return out


def influence(rules, i, n):
    """Single-node Boolean sensitivity of the determination to node i (the study-A measure)."""
    changed = total = 0
    for s in range(2 ** n):
        cur = tuple((s >> k) & 1 for k in range(n))
        flipped = tuple(b ^ 1 if k == i else b for k, b in enumerate(cur))
        for j in range(n):
            total += 1
            changed += (rules[j](cur) != rules[j](flipped))
    return changed / total


def node_records(rules, labels):
    """For each node: (label, shapley, influence, in_core)."""
    n = len(labels)
    v, tpm, cm = coalition_values(rules, labels)
    sh = shapley(v, n)
    core, _ = major_complex(list(rules), labels)
    core = set(core or ())
    return [(labels[i], round(sh[i], 4), round(influence(rules, i, n), 4), labels[i] in core)
            for i in range(n)]


def auc(scores_labels):
    pos = [s for s, y in scores_labels if y]
    neg = [s for s, y in scores_labels if not y]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return wins / (len(pos) * len(neg))
