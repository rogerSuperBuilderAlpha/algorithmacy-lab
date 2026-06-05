"""Shared helpers for Q58 normalization cut geometry probes."""

import os
import sys

import numpy as np
import pyphi
from pyphi import new_big_phi
from pyphi.new_big_phi import normalization_factor

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules  # noqa: E402
from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    COMPLETE,
    PHI_TOL,
    instrument_control,
)
from org_frontier.questions.q57_channel_direction_mip.direction_mip_utils import (  # noqa: E402
    enriched_rows,
    excluded_outer_cut,
    expected_tied_cut,
    norm_fields,
)

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

CUT_RATIO = 2.0
NORM_FACTOR_RATIO = 2.0
PHI_RATIO = 1.0


def subsystem_sia(rules):
    v = verdict(rules, ("W", "S", "C"))
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=("W", "S", "C"))
    sub = pyphi.Subsystem(net, tuple(v.mip_state))
    sia = new_big_phi.sia(sub)
    return sub, sia, float(sia.phi)


def min_norm_detail(rules, cut_type, sys_phi, sub, sia):
    """Min normalized_phi partition row at system Phi with cut geometry."""
    net = sub.network
    parts = new_big_phi.system_partitions(sub.node_indices, node_labels=net.node_labels)
    best = None
    for p in parts:
        first = str(p).splitlines()[0].strip()
        if first != cut_type:
            continue
        ev = new_big_phi.evaluate_partition(p, sub, sia.system_state)
        phi = float(ev.phi)
        if abs(phi - sys_phi) > PHI_TOL:
            continue
        norm_phi = float(ev.normalized_phi)
        nf = float(normalization_factor(p))
        cut_ones = int(np.sum(np.array(p._cut_matrix)))
        if best is None or norm_phi < best["norm_phi"]:
            best = {
                "cut_type": cut_type,
                "norm_phi": norm_phi,
                "phi": phi,
                "norm_factor": nf,
                "cut_ones": cut_ones,
            }
    return best


def geometry_rows():
    """Sixteen pairs with tied, excluded, and complete min-norm geometry."""
    out = []
    for row in enriched_rows():
        nf = norm_fields(row)
        rules = row["rules"]
        sub, sia, sys_phi = subsystem_sia(rules)
        tied_cut = expected_tied_cut(row["topology"])
        excl_cut = excluded_outer_cut(tied_cut)
        tied = min_norm_detail(rules, tied_cut, sys_phi, sub, sia)
        excl = min_norm_detail(rules, excl_cut, sys_phi, sub, sia)
        complete = min_norm_detail(rules, COMPLETE, sys_phi, sub, sia)
        out.append({
            **row,
            "tied_cut": tied_cut,
            "excl_cut": excl_cut,
            "sys_phi": sys_phi,
            "tied": tied,
            "excl": excl,
            "complete": complete,
        })
    return out
