"""Shared helpers for Q59 directed cut-edge enumeration probes."""

import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules  # noqa: E402
from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    PHI_TOL,
    instrument_control,
)
from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    WORKER_TOPOLOGIES,
    back_channel_recipient,
    enriched_rows,
    excluded_outer_cut,
    expected_tied_cut,
)
from org_frontier.questions.q58_normalization_cut_geometry.norm_cut_utils import (  # noqa: E402
    geometry_rows,
    min_norm_detail,
    subsystem_sia,
)

LABELS = ("W", "S", "C")

WORKER_ONLY_TIED = frozenset({"S->W", "W->C", "W->S"})
WORKER_ONLY_EXCL = frozenset({"C->S"})
COUNTERPART_ONLY_TIED = frozenset({"C->S", "C->W", "S->C"})
COUNTERPART_ONLY_EXCL = frozenset({"W->S"})

ADJ_RATIO = 3.0
MEDIATOR_COUNT = 2
ONLY_TIED_SIZE = 3
ONLY_EXCL_SIZE = 1
SYMDIFF_SIZE = 4


def severed_edges(cut_matrix):
    """Directed edges marked severed in a 3x3 cut matrix."""
    cm = np.asarray(cut_matrix)
    return frozenset(
        f"{LABELS[i]}->{LABELS[j]}"
        for i in range(3)
        for j in range(3)
        if cm[i, j]
    )


def cross_edge_from_cm(cm):
    """Back-channel cross-edge label and matrix indices."""
    if cm[0, 2]:
        return "W->C", 0, 2
    if cm[2, 0]:
        return "C->W", 2, 0
    raise ValueError("no single back-channel cross-edge in connectivity matrix")


def cut_matrix_for(rules, cut_type, sys_phi):
    """Min-norm at-system-Phi cut matrix for a partition type."""
    sub, sia, _ = subsystem_sia(rules)
    detail = min_norm_detail(rules, cut_type, sys_phi, sub, sia)
    if detail is None:
        raise ValueError(f"no min-norm row for {cut_type!r}")
    parts = __import__("pyphi").new_big_phi.system_partitions(
        sub.node_indices, node_labels=sub.network.node_labels
    )
    for p in parts:
        first = str(p).splitlines()[0].strip()
        if first != cut_type:
            continue
        ev = __import__("pyphi").new_big_phi.evaluate_partition(p, sub, sia.system_state)
        if abs(float(ev.phi) - sys_phi) > PHI_TOL:
            continue
        if abs(float(ev.normalized_phi) - detail["norm_phi"]) < PHI_TOL:
            return np.array(p._cut_matrix)
    raise ValueError(f"cut matrix not found for {cut_type!r}")


def edge_detail_rows():
    """Sixteen pairs with directed severed-edge inventories."""
    out = []
    for row in geometry_rows():
        rules = row["rules"]
        tied_cut = row["tied_cut"]
        excl_cut = row["excl_cut"]
        sys_phi = row["sys_phi"]
        tied_cm = cut_matrix_for(rules, tied_cut, sys_phi)
        excl_cm = cut_matrix_for(rules, excl_cut, sys_phi)
        tied_set = severed_edges(tied_cm)
        excl_set = severed_edges(excl_cm)
        only_tied = tied_set - excl_set
        only_excl = excl_set - tied_set
        conn = cm_from_rules(rules)
        cross, ci, cj = cross_edge_from_cm(conn)
        adj_tied = int(tied_cm.sum()) - int(tied_cm[ci, cj])
        adj_excl = int(excl_cm.sum()) - int(excl_cm[ci, cj])
        med_count = sum(1 for e in only_tied if "S" in e)
        adj_ratio = adj_tied / adj_excl if adj_excl else None
        out.append({
            **row,
            "tied_cm": tied_cm,
            "excl_cm": excl_cm,
            "tied_set": tied_set,
            "excl_set": excl_set,
            "only_tied": only_tied,
            "only_excl": only_excl,
            "cross_edge": cross,
            "cross_in_tied": cross in tied_set,
            "cross_in_excl": cross in excl_set,
            "adj_tied": adj_tied,
            "adj_excl": adj_excl,
            "adj_equal": adj_tied == adj_excl,
            "adj_ratio": adj_ratio,
            "mediator_only_tied": med_count,
            "recipient": back_channel_recipient(row["topology"]),
        })
    return out


def expected_templates(topology):
    """Return (only_tied, only_excl) frozensets for worker or counterpart recipient."""
    if topology in WORKER_TOPOLOGIES:
        return WORKER_ONLY_TIED, WORKER_ONLY_EXCL
    return COUNTERPART_ONLY_TIED, COUNTERPART_ONLY_EXCL
