"""Shared helpers for Q52 phi-ladder mechanism probes (extends Q51 backchannel_utils)."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.corpus.population import _two_input_tables  # noqa: E402
from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    CANON,
    IMPLICATION_INDICES,
    LABELS,
    LIVE_INDICES,
    MAX_PHI,
    PHI_TOL,
    complementary_reads,
    edge_count,
    implication_forms,
    instrument_control,
    matched_live_reads,
    symmetric_backchannel,
    w_index,
    c_index,
    s_index,
    worker_backchannel,
)
from org_frontier.probes.lib import verdict  # noqa: E402

W_CENTRIC = {2, 13}
C_CENTRIC = {4, 11}
HIGH_PHI = 0.830075
MID_PHI = 0.415037
SYMMETRIC_PHI = 0.830075


def commit_out_at(label, w_bit, c_bit):
    """S' output at fixed (W, C) for the form's commit index."""
    si = s_index(label)
    table = _two_input_tables()[si]
    return table[w_bit | (c_bit << 1)]


def w_centric_high_predicted(label):
    """Party-read polarity matches W-centric distinguishing output at (W=1,C=0)."""
    iw = w_index(label)
    out_10 = commit_out_at(label, 1, 0)
    return out_10 != (iw == 2)


def ladder_rung(label, structure, max_phi):
    if structure == "dyadic":
        return "dyadic"
    if abs(max_phi - HIGH_PHI) < PHI_TOL:
        return "high"
    if abs(max_phi - MID_PHI) < PHI_TOL:
        return "mid"
    return "other"


def worker_bc_verdict(label, rules):
    bc = worker_backchannel(rules)
    v = verdict(bc, LABELS)
    return v, bc
