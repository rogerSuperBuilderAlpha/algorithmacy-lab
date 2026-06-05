"""Shared helpers for Q55 bijective parity below-vs-ceiling discriminator probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402
from org_frontier.questions.q51_implication_backchannel.backchannel_utils import (  # noqa: E402
    MAX_PHI,
    PHI_TOL,
)
from org_frontier.questions.q54_xor_parity_mechanism.mechanism_utils import (  # noqa: E402
    C_CENTRIC,
    LABELS,
    W_CENTRIC,
    apply_any_topology,
    full_panel,
    instrument_control,
    matched_implication_panel,
    seam_cond_entropy_wc_given_s,
    s_index,
)

MID_RUNG = 0.415037
MIP_BELOW = "2 parts: {S,WC}"
PARITY_TOPOLOGIES = (
    "worker_xor",
    "counterpart_xor",
    "symmetric_xor",
    "worker_xnor",
    "counterpart_xnor",
    "symmetric_xnor",
)
ONE_SIDED_PARITY = ("worker_xor", "counterpart_xor", "worker_xnor", "counterpart_xnor")


def bijective_parity_panel():
    """Forty-eight bijective parity (topology, form) pairs from Q54 full panel."""
    rows = full_panel()
    return [
        r
        for r in rows
        if r["channel_bijective"] and r["topology"] in PARITY_TOPOLOGIES
    ]


def split_below_ceiling(rows):
    below = [r for r in rows if not r["at_ceiling"]]
    ceiling = [r for r in rows if r["at_ceiling"]]
    return below, ceiling


def is_one_sided(topology):
    return topology in ONE_SIDED_PARITY


def xor_misaligned(label, topology):
    """True iff one-sided XOR/XNOR wiring is commit-misaligned (predicted below-ceiling)."""
    s = s_index(label)
    if topology == "worker_xor":
        return s in W_CENTRIC
    if topology == "counterpart_xor":
        return s in C_CENTRIC
    if topology == "worker_xnor":
        return s in C_CENTRIC
    if topology == "counterpart_xnor":
        return s in W_CENTRIC
    return False


def xor_aligned_at_ceiling(label, topology):
    """True iff one-sided XOR wiring is commit-aligned and expected at ceiling."""
    if topology == "worker_xor":
        return s_index(label) in C_CENTRIC
    if topology == "counterpart_xor":
        return s_index(label) in W_CENTRIC
    return False


def xnor_aligned_at_ceiling(label, topology):
    """True iff one-sided XNOR wiring is commit-aligned under inverted rule."""
    if topology == "worker_xnor":
        return s_index(label) in W_CENTRIC
    if topology == "counterpart_xnor":
        return s_index(label) in C_CENTRIC
    return False


def rules_for_label(label):
    for lbl, rules in matched_implication_panel():
        if lbl == label:
            return rules
    raise KeyError(label)


def enriched_row(row):
    """Add rules-derived fields: seam H, MIP first line."""
    rules = rules_for_label(row["label"])
    bc = apply_any_topology(rules, row["topology"])
    v = verdict(bc, LABELS)
    mip_first = v.mip_partition.splitlines()[0]
    return {
        **row,
        "max_phi": v.max_phi,
        "structure": v.structure,
        "mip_first": mip_first,
        "seam_h": seam_cond_entropy_wc_given_s(bc),
        "one_sided": is_one_sided(row["topology"]),
        "misaligned": xor_misaligned(row["label"], row["topology"]),
    }


def enriched_panel():
    return [enriched_row(r) for r in bijective_parity_panel()]
