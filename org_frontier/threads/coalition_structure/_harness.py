"""Harness for the coalition-structure thread.

The Shapley thread left a residual: a node-level marginal score (Shapley, or best-with-i minus
best-without-i) predicts major-complex membership at AUC ~0.87, not 1.0. This harness asks where the
ceiling comes from by reading the exclusion postulate as cooperative game theory.

Two value functions on subsets S of a coordination form's nodes:
  - phi_s_maxstate(S): max over reachable states of the subset's system integrated information. Used
    for the coalition-structure (partition) comparisons, matching how a coalition's worth is usually
    scored independent of a single state.
  - at a fixed state s*, phi_s_at(S): the subset's integrated information in that state. Used for the
    argmax-equals-complex check, where the major complex is itself defined at one state.

A "coalition structure" is a partition of the node set; its value is the sum of its blocks' worths.
IIT condensation peels off the maximal complex, removes it, and recurses on the rest — a greedy
coalition-structure generator. The optimal structure is the partition maximizing total worth.
"""

import itertools
import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi
from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False


def network(rules, labels):
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    return pyphi.Network(tpm, cm=cm, node_labels=labels), tpm


def phi_s_at(net, st, subset):
    """Integrated information of a subset in one state (0 for the empty set)."""
    if len(subset) < 1:
        return 0.0
    try:
        return float(new_big_phi.sia(pyphi.Subsystem(net, st, nodes=subset)).phi)
    except Exception:
        return 0.0


def phi_s_maxstate(net, tpm, n, subset):
    """Max over reachable states of a subset's integrated information."""
    if len(subset) < 1:
        return 0.0
    best = 0.0
    for s in reachable_states(tpm, n):
        st = tuple((s >> i) & 1 for i in range(n))
        best = max(best, phi_s_at(net, st, subset))
    return best


def complex_over_states(net, tpm, n):
    """The state s* and node set where the maximal complex attains its largest phi across reachable
    states, with that phi. Returns (s_star, frozenset(core), phi) or (None, None, 0.0)."""
    best = (-1.0, None, None)
    for s in reachable_states(tpm, n):
        st = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, st)
        except Exception:
            continue
        if hasattr(mc, "node_indices") and float(mc.phi) > best[0]:
            best = (float(mc.phi), st, frozenset(mc.node_indices))
    if best[1] is None:
        return None, None, 0.0
    return best[1], best[2], best[0]


def argmax_subsets_at(net, st, n):
    """(value dict over all non-empty subsets at st, the max value, the set of argmax subsets)."""
    vals = {frozenset(S): phi_s_at(net, st, S)
            for r in range(1, n + 1) for S in itertools.combinations(range(n), r)}
    mx = max(vals.values())
    argmaxes = {S for S, v in vals.items() if abs(v - mx) < 1e-6}
    return vals, mx, argmaxes


def node_marginal_auc_at(net, st, n, core, auc_pairs):
    """Append (score, in_core) for each node, where score = best-with-i minus best-without-i over
    subsets at st — the node-level marginal that Shapley averages a different way."""
    best_with = [0.0] * n
    best_without = [0.0] * n
    for r in range(1, n + 1):
        for S in itertools.combinations(range(n), r):
            v = phi_s_at(net, st, S)
            for i in range(n):
                if i in S:
                    best_with[i] = max(best_with[i], v)
                else:
                    best_without[i] = max(best_without[i], v)
    for i in range(n):
        auc_pairs.append((best_with[i] - best_without[i], i in core))


def partitions(items):
    """All set partitions of a small list (Bell-number many)."""
    items = list(items)
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for sub in partitions(rest):
        for k in range(len(sub)):
            yield sub[:k] + [[first] + sub[k]] + sub[k + 1:]
        yield [[first]] + sub


def optimal_structure(net, tpm, n):
    """Partition of the node set maximizing total max-state worth of its blocks."""
    worth = {}

    def w(block):
        key = frozenset(block)
        if key not in worth:
            worth[key] = phi_s_maxstate(net, tpm, n, tuple(sorted(block)))
        return worth[key]

    best = (-1.0, None)
    for part in partitions(range(n)):
        tot = sum(w(b) for b in part)
        if tot > best[0]:
            best = (tot, frozenset(frozenset(b) for b in part))
    return best[1]


def condensation(net, tpm, n):
    """Greedy IIT condensation: peel the maximal complex (by max-state worth), recurse on the rest."""
    remaining = set(range(n))
    blocks = []
    while remaining:
        nodes = tuple(sorted(remaining))
        best = (-1.0, None)
        for r in range(1, len(nodes) + 1):
            for S in itertools.combinations(nodes, r):
                val = phi_s_maxstate(net, tpm, n, S)
                if val > best[0]:
                    best = (val, frozenset(S))
        block = best[1] if best[1] else frozenset({nodes[0]})
        blocks.append(block)
        remaining -= set(block)
    return frozenset(blocks)


def auc(pairs):
    pos = [s for s, y in pairs if y]
    neg = [s for s, y in pairs if not y]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > q) + 0.5 * (p == q) for p in pos for q in neg)
    return wins / (len(pos) * len(neg))
