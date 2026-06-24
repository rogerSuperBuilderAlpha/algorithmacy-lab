"""Bridge module: two party accounts of one coordination, scored as a Φ spread.

A coordination has two parties who each give an account of how it works. Each account is a
rule set over the same labelled nodes (a small Boolean dynamical system). The two accounts can
diverge: the parties disagree about who responds to whom. This module takes the two accounts,
runs each through the exact-Φ classifier, and reports a SPREAD tuple that quantifies how far
apart the two verdicts sit.

The spread has three components:

    verdict_agreement  in {0, 1}   1 iff both accounts read the same structure (both dyadic or
                                   both triadic).
    phi_gap            >= 0.0      absolute difference of the two whole-system max Φ_MIP values.
    core_jaccard      in [0, 1]    mean Jaccard overlap of the two major-complex cores, taken
                                   over the states reachable in BOTH accounts; 1.0 means the two
                                   accounts put exactly the same parties in the integrated core
                                   at every shared state, 0.0 means disjoint cores.

The anchors: when the two accounts are the same rule set, verdict_agreement = 1, phi_gap = 0.0,
and core_jaccard = 1.0. The spread is symmetric in the two parties: swapping which account is A
and which is B leaves all three components unchanged.

This is a synthetic instrument. The accounts are coder-supplied rule sets, not measured worker
states. The construct it scores is divergence between two stated accounts, validated here on
controls; it is not a measurement of a real coordination.

Reuses the classifier and the probe library; it does not reimplement Φ.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from typing import Callable, Sequence

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import verdict, major_complex


def _core_set(rules: Sequence[Callable], labels: Sequence[str]) -> frozenset:
    """The party set of the major complex (max-Φ over reachable states), as a frozenset."""
    core, _ = major_complex(list(rules), tuple(labels))
    return frozenset() if core is None else frozenset(core)


def _jaccard(a: frozenset, b: frozenset) -> float:
    """Jaccard overlap of two party sets. Two empty cores count as full agreement (1.0)."""
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 1.0
    return len(a & b) / len(union)


def spread(accountA_rules: Sequence[Callable],
           accountB_rules: Sequence[Callable],
           labels: Sequence[str]) -> dict:
    """Score the divergence between two party accounts of one coordination.

    ``accountA_rules`` and ``accountB_rules`` are per-node Boolean rule lists over the same
    ``labels`` (same node count, same ordering). Returns a dict with keys:

        verdict_agreement : int    1 iff both accounts read the same structure.
        phi_gap           : float  |max Φ_MIP(A) - max Φ_MIP(B)|.
        core_jaccard      : float  Jaccard overlap of the two major-complex cores.
        both_verdicts     : tuple  (structureA, structureB), e.g. ('triadic', 'dyadic').
    """
    labels = tuple(labels)
    if len(accountA_rules) != len(accountB_rules):
        raise ValueError("the two accounts must have the same number of parties")
    if len(labels) != len(accountA_rules):
        raise ValueError("labels must match the number of parties")

    vA = verdict(list(accountA_rules), labels)
    vB = verdict(list(accountB_rules), labels)

    verdict_agreement = int(vA.structure == vB.structure)
    phi_gap = abs(float(vA.max_phi) - float(vB.max_phi))

    coreA = _core_set(accountA_rules, labels)
    coreB = _core_set(accountB_rules, labels)
    core_jaccard = _jaccard(coreA, coreB)

    return {
        "verdict_agreement": verdict_agreement,
        "phi_gap": phi_gap,
        "core_jaccard": core_jaccard,
        "both_verdicts": (vA.structure, vB.structure),
    }


def node_pivotal(rules: Sequence[Callable], labels: Sequence[str], node_label: str) -> bool:
    """Whether ``node_label`` is a member of the major complex under ``rules``.

    A party in the integrated core is in every integrating coalition: its removal takes it out
    of the structure that carries Φ. This is the pivotal/veto-player reading of membership
    (Probe 11: a party is in the irreducible core only if its determination makes it pivotal).
    A party outside the core is droppable, since the coordination integrates without it.
    """
    return node_label in _core_set(rules, labels)


def pivotality_spread(accountA_rules: Sequence[Callable],
                      accountB_rules: Sequence[Callable],
                      labels: Sequence[str],
                      node_label: str) -> dict:
    """Add a node-pivotality flag to the spread between two accounts.

    Returns the full ``spread`` dict extended with:

        pivotalA          : bool   ``node_label`` is in account A's major complex.
        pivotalB          : bool   ``node_label`` is in account B's major complex.
        pivotality_agrees : int    1 iff the flag matches across the two accounts.

    A ``pivotality_agrees`` of 0 records that the two accounts disagree on whether the named
    party is pivotal, the veto-player divergence the bridge is meant to register.
    """
    base = spread(accountA_rules, accountB_rules, labels)
    pa = node_pivotal(accountA_rules, labels, node_label)
    pb = node_pivotal(accountB_rules, labels, node_label)
    base.update({
        "pivotalA": pa,
        "pivotalB": pb,
        "pivotality_agrees": int(pa == pb),
    })
    return base


def signed_phi_gap(accountA_rules: Sequence[Callable],
                   accountB_rules: Sequence[Callable],
                   labels: Sequence[str]) -> float:
    """max Φ_MIP(A) - max Φ_MIP(B), with sign. Positive means account A integrates more.

    The ``spread`` field ``phi_gap`` is the absolute value of this. The signed form lets a
    study ask whether one named account is the more-integrated one, not only how far apart the
    two sit.
    """
    labels = tuple(labels)
    vA = verdict(list(accountA_rules), labels)
    vB = verdict(list(accountB_rules), labels)
    return float(vA.max_phi) - float(vB.max_phi)


def core_node_divergence(accountA_rules: Sequence[Callable],
                         accountB_rules: Sequence[Callable],
                         labels: Sequence[str]) -> dict:
    """Per-node attribution of where two accounts' major-complex cores diverge.

    Returns the core party set under each account and, for every label, whether that party sits
    in account A's core, in account B's core, and whether the two accounts disagree about it. A
    party flagged ``disputed`` is one the two accounts place differently: in the core under one
    account and outside it under the other. The keys:

        coreA       : frozenset   account A's major-complex parties.
        coreB       : frozenset   account B's major-complex parties.
        per_node    : dict        label -> {"inA": bool, "inB": bool, "disputed": bool}.
        disputed    : tuple       labels the two accounts place differently, in ``labels`` order.

    When the two cores agree on every party, ``disputed`` is empty. When they differ on exactly
    one party, that single label names the disputed member.
    """
    labels = tuple(labels)
    coreA = _core_set(accountA_rules, labels)
    coreB = _core_set(accountB_rules, labels)
    per_node = {}
    disputed = []
    for lab in labels:
        inA = lab in coreA
        inB = lab in coreB
        d = inA != inB
        per_node[lab] = {"inA": inA, "inB": inB, "disputed": d}
        if d:
            disputed.append(lab)
    return {
        "coreA": coreA,
        "coreB": coreB,
        "per_node": per_node,
        "disputed": tuple(disputed),
    }
