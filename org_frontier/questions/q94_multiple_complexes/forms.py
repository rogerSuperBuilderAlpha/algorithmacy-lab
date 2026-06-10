"""Q94: forms with two coordination units, and the exclusion-resolved set of coexisting complexes.

Finding 8 always reads the single major complex. This asks whether a form can hold two disjoint
irreducible cores at once, and what coupling merges them into one. Two minimal mutual-determination
units are built — a 2-cycle each ({A,B} with A'=B, B'=A) — and coupled in different ways:

- disjoint        : no coupling between the units.
- shared_spectator: both units also read an idle fifth node that reads nothing back.
- one_way_bridge  : the second unit reads the first, but not the reverse.
- mutual_bridge   : the two units read each other.

`disjoint_complexes` resolves PyPhi's irreducible-complex lattice into a tiling of disjoint maximal
complexes (greedy by φ), so the count of coexisting cores can be read.

Imported by `probe_multiple_complexes.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states


def disjoint_complexes_at(rules, labels, state):
    """Exclusion-resolved disjoint maximal complexes at one state: greedy by descending φ."""
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
    cands = []
    for c in nbp.irreducible_complexes(net, state):
        cands.append((frozenset(labels[i] for i in c.node_indices), float(c.phi)))
    cands.sort(key=lambda t: -t[1])
    used, tiling = set(), []
    for nodes, phi in cands:
        if phi <= 1e-9 or nodes & used:
            continue
        tiling.append((tuple(sorted(nodes)), round(phi, 3)))
        used |= nodes
    return tiling


def max_disjoint_complexes(rules, labels):
    """Over reachable states, the tiling with the most disjoint complexes (ties broken by total φ)."""
    n = len(rules)
    tpm = tpm_from_rules(rules)
    best = []
    best_key = (-1, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            tiling = disjoint_complexes_at(rules, labels, state)
        except Exception:
            continue
        key = (len(tiling), sum(p for _, p in tiling))
        if key > best_key:
            best_key, best = key, tiling
    return best


# --- the four configurations (units {A,B} and {C,D}) ---

def disjoint():
    rules = [lambda x: x[1], lambda x: x[0], lambda x: x[3], lambda x: x[2]]
    return rules, ("A", "B", "C", "D")


def shared_spectator():
    # E is an idle spectator both units read; E reads nothing (E' = E).
    rules = [lambda x: x[1] & x[4], lambda x: x[0], lambda x: x[3] & x[4], lambda x: x[2], lambda x: x[4]]
    return rules, ("A", "B", "C", "D", "E")


def one_way_bridge():
    # unit2 reads unit1 (C reads B); unit1 does not read unit2.
    rules = [lambda x: x[1], lambda x: x[0], lambda x: x[3] & x[1], lambda x: x[2]]
    return rules, ("A", "B", "C", "D")


def mutual_bridge():
    # the units read each other: B reads C, C reads B.
    rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[3] & x[1], lambda x: x[2]]
    return rules, ("A", "B", "C", "D")
