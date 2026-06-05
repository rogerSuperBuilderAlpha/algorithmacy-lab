"""Shared helpers for Q53 implication Phi ceiling probes (extends Q51 backchannel_utils)."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    LABELS,
    MAX_PHI,
    PHI_TOL,
    implication_forms,
    instrument_control,
    matched_live_reads,
    symmetric_backchannel,
    worker_backchannel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

SYMMETRIC_EQ = 0.830075

TOPOLOGY_SWEEP = (
    "worker_and",
    "counterpart_and",
    "symmetric_and",
    "worker_or",
    "counterpart_or",
    "symmetric_or",
    "cross_wor_cand",
    "cross_wand_cor",
)

XOR_TOPOLOGIES = ("worker_xor", "counterpart_xor", "symmetric_xor")

ALL_TOPOLOGIES = TOPOLOGY_SWEEP + XOR_TOPOLOGIES


def _gate(old_fn, other_bit, op):
    if op == "and":
        return lambda x, o=old_fn, b=other_bit: o(x) & x[b]
    if op == "or":
        return lambda x, o=old_fn, b=other_bit: o(x) | x[b]
    if op == "xor":
        return lambda x, o=old_fn, b=other_bit: o(x) ^ x[b]
    raise ValueError(f"unknown gate op {op!r}")


def apply_topology(rules, topology):
    old_w, old_c = rules[0], rules[2]
    if topology == "worker_and":
        return worker_backchannel(rules)
    if topology == "counterpart_and":
        return [rules[0], rules[1], _gate(old_c, 0, "and")]
    if topology == "symmetric_and":
        return symmetric_backchannel(rules)
    if topology == "worker_or":
        return [_gate(old_w, 2, "or"), rules[1], rules[2]]
    if topology == "counterpart_or":
        return [rules[0], rules[1], _gate(old_c, 0, "or")]
    if topology == "symmetric_or":
        return [_gate(old_w, 2, "or"), rules[1], _gate(old_c, 0, "or")]
    if topology == "cross_wor_cand":
        return [_gate(old_w, 2, "or"), rules[1], _gate(old_c, 0, "and")]
    if topology == "cross_wand_cor":
        return [_gate(old_w, 2, "and"), rules[1], _gate(old_c, 0, "or")]
    if topology == "worker_xor":
        return [_gate(old_w, 2, "xor"), rules[1], rules[2]]
    if topology == "counterpart_xor":
        return [rules[0], rules[1], _gate(old_c, 0, "xor")]
    if topology == "symmetric_xor":
        return [_gate(old_w, 2, "xor"), rules[1], _gate(old_c, 0, "xor")]
    raise ValueError(f"unknown topology {topology!r}")


def matched_implication_panel():
    return list(implication_forms(matched_live_reads))


def at_ceiling(v):
    return v.structure == "triadic" and v.max_phi >= MAX_PHI - PHI_TOL


def exceeds_equilibrium(max_phi):
    return max_phi > SYMMETRIC_EQ + PHI_TOL


def classify_panel(topologies=ALL_TOPOLOGIES):
    rows = []
    for label, rules in matched_implication_panel():
        for topo in topologies:
            bc = apply_topology(rules, topo)
            v = verdict(bc, LABELS)
            rows.append(
                {
                    "label": label,
                    "topology": topo,
                    "structure": v.structure,
                    "max_phi": v.max_phi,
                }
            )
    return rows
