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
