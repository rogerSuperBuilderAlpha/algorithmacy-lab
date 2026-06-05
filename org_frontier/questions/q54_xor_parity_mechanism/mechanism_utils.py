"""Shared helpers for Q54 XOR parity back-channel mechanism probes."""

import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import tpm_from_rules  # noqa: E402
from org_frontier.probes._info import entropy  # noqa: E402
from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    MAX_PHI,
    PHI_TOL,
    s_index,
)
from org_frontier.questions.q53_impl_phi_ceiling.ceiling_utils import (  # noqa: E402
    ALL_TOPOLOGIES,
    LABELS,
    TOPOLOGY_SWEEP,
    XOR_TOPOLOGIES,
    apply_topology,
    at_ceiling,
    instrument_control,
    matched_implication_panel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

W_CENTRIC = {2, 13}
C_CENTRIC = {4, 11}

PARITY_GATES = {"xor", "xnor"}
MONOTONE_GATES = {"and", "or"}

XNOR_TOPOLOGIES = ("worker_xnor", "counterpart_xnor", "symmetric_xnor")

CHANNEL_OPS = {
    "worker_and": [("and", "w")],
    "counterpart_and": [("and", "c")],
    "symmetric_and": [("and", "w"), ("and", "c")],
    "worker_or": [("or", "w")],
    "counterpart_or": [("or", "c")],
    "symmetric_or": [("or", "w"), ("or", "c")],
    "cross_wor_cand": [("or", "w"), ("and", "c")],
    "cross_wand_cor": [("and", "w"), ("or", "c")],
    "worker_xor": [("xor", "w")],
    "counterpart_xor": [("xor", "c")],
    "symmetric_xor": [("xor", "w"), ("xor", "c")],
    "worker_xnor": [("xnor", "w")],
    "counterpart_xnor": [("xnor", "c")],
    "symmetric_xnor": [("xnor", "w"), ("xnor", "c")],
}


def _eval_gate(op, a, b):
    if op == "and":
        return a & b
    if op == "or":
        return a | b
    if op == "xor":
        return a ^ b
    if op == "xnor":
        return (a ^ b) ^ 1
    raise ValueError(f"unknown gate {op!r}")


def gate_bijective_in_coupled_bit(op):
    """True iff b -> g(a,b) is a bijection on {0,1} for every fixed a in {0,1}."""
    for a in (0, 1):
        outs = {_eval_gate(op, a, b) for b in (0, 1)}
        if len(outs) != 2:
            return False
    return True


def topology_channel_bijective(topology):
    """True iff every active channel edge in the topology uses a bijective gate."""
    ops = CHANNEL_OPS.get(topology, [])
    return all(gate_bijective_in_coupled_bit(op) for op, _ in ops)


def apply_xnor_topology(rules, topology):
    """XNOR back-channel transforms mirroring ceiling_utils XOR pattern."""
    old_w, old_c = rules[0], rules[2]

    def _xnor_gate(old_fn, other_bit):
        return lambda x, o=old_fn, b=other_bit: (o(x) ^ x[b]) ^ 1

    if topology == "worker_xnor":
        return [_xnor_gate(old_w, 2), rules[1], rules[2]]
    if topology == "counterpart_xnor":
        return [rules[0], rules[1], _xnor_gate(old_c, 0)]
    if topology == "symmetric_xnor":
        return [_xnor_gate(old_w, 2), rules[1], _xnor_gate(old_c, 0)]
    raise ValueError(f"unknown xnor topology {topology!r}")


def apply_any_topology(rules, topology):
    if topology in XNOR_TOPOLOGIES:
        return apply_xnor_topology(rules, topology)
    return apply_topology(rules, topology)


def tpm_is_permutation(rules):
    """True iff the eight-state synchronous TPM is a bijection on states."""
    tpm = tpm_from_rules(rules)
    n = tpm.shape[1]
    next_states = []
    for s in range(2 ** n):
        bits = [int(tpm[s, j]) for j in range(n)]
        next_states.append(sum(b << i for i, b in enumerate(bits)))
    return len(set(next_states)) == len(next_states)


def reachable_trajectory(rules, steps_per_start=8):
    """Enumerate a trajectory covering reachable states (deterministic n=3)."""
    tpm = tpm_from_rules(rules)
    n = tpm.shape[1]
    rows = []
    for start in range(2 ** n):
        state = start
        for _ in range(steps_per_start):
            cur = tuple((state >> i) & 1 for i in range(n))
            rows.append(cur)
            bits = [int(tpm[state, j]) for j in range(n)]
            state = sum(b << i for i, b in enumerate(bits))
    return np.array(rows, dtype=int)


def seam_cond_entropy_wc_given_s(rules):
    """H(W,C|S) over the reachable-state trajectory ensemble (bits)."""
    traj = reachable_trajectory(rules)
    h_wsc = entropy(traj, [0, 1, 2])
    h_s = entropy(traj, [1])
    return h_wsc - h_s


def full_panel(topologies=None):
    topologies = list(ALL_TOPOLOGIES) if topologies is None else list(topologies)
    if "symmetric_xnor" not in topologies:
        topologies = topologies + list(XNOR_TOPOLOGIES)
    rows = []
    for label, rules in matched_implication_panel():
        for topo in topologies:
            bc = apply_any_topology(rules, topo)
            v = verdict(bc, LABELS)
            rows.append(
                {
                    "label": label,
                    "s_index": s_index(label),
                    "topology": topo,
                    "structure": v.structure,
                    "max_phi": v.max_phi,
                    "at_ceiling": at_ceiling(v),
                    "channel_bijective": topology_channel_bijective(topo),
                    "tpm_permutation": tpm_is_permutation(bc),
                }
            )
    return rows


def commit_class(s):
    if s in W_CENTRIC:
        return "w_centric"
    if s in C_CENTRIC:
        return "c_centric"
    return "other"


def aligned_one_sided_xor(label, topology, at_phi2):
    """Worker XOR should hit ceiling only on C-centric; counterpart only on W-centric."""
    s = s_index(label)
    if not at_phi2:
        return True
    if topology == "worker_xor":
        return s in C_CENTRIC
    if topology == "counterpart_xor":
        return s in W_CENTRIC
    return True
