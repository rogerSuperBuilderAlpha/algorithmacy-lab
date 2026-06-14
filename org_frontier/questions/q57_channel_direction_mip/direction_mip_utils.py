"""Shared helpers for Q57 channel direction MIP seam probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q56_symmetric_complete_mip.mip_geometry_utils import (  # noqa: E402
    COMPLETE,
    OUTER_C,
    OUTER_W,
    PHI_TOL,
    instrument_control,
    one_sided_ceiling,
    scan_row,
)

TIED_NORM = 0.5
EXCLUDED_NORM = 1.0
NORM_RATIO = 2.0

WORKER_TOPOLOGIES = ("worker_xor", "worker_xnor")
COUNTERPART_TOPOLOGIES = ("counterpart_xor", "counterpart_xnor")


def back_channel_recipient(topology):
    """Outer party whose update rule gains the extra incoming cross-edge."""
    if topology.startswith("worker"):
        return "W"
    if topology.startswith("counterpart"):
        return "C"
    raise ValueError(f"unknown one-sided topology {topology!r}")


def expected_tied_cut(topology):
    """Outer-party singleton cut predicted from back-channel recipient."""
    return OUTER_W if back_channel_recipient(topology) == "W" else OUTER_C


def excluded_outer_cut(tied_cut):
    return OUTER_C if tied_cut == OUTER_W else OUTER_W


def enriched_rows():
    """Sixteen aligned one-sided ceiling pairs with partition scan fields."""
    return [scan_row(r) for r in one_sided_ceiling()]


def tied_outer_cut(row):
    """Official tied outer cut (singleton in tie set)."""
    outer = row["outer_in_official"]
    if len(outer) != 1:
        return None
    return outer[0]


def norm_fields(row):
    """Tied/excluded/complete normalized_phi and ratio for one row."""
    tied_cut = expected_tied_cut(row["topology"])
    excl_cut = excluded_outer_cut(tied_cut)
    tied_norm = row["min_norm"][tied_cut]
    excl_norm = row["min_norm"][excl_cut]
    complete_norm = row["min_norm"][COMPLETE]
    ratio = None
    if tied_norm is not None and excl_norm is not None and tied_norm > PHI_TOL:
        ratio = excl_norm / tied_norm
    return {
        "tied_cut": tied_cut,
        "excl_cut": excl_cut,
        "tied_norm": tied_norm,
        "excl_norm": excl_norm,
        "complete_norm": complete_norm,
        "ratio": ratio,
        "dual_at_sys": row["at_sys"][OUTER_W] and row["at_sys"][OUTER_C],
    }
