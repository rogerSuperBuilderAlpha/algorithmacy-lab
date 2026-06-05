"""Shared helpers for Q56 symmetric complete MIP geometry probes."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import cm_from_rules, tpm_from_rules  # noqa: E402
from org_frontier.questions.q49_mip_seam_mincut.seam import mip_ties  # noqa: E402
from org_frontier.questions.q54_xor_parity_mechanism.mechanism_utils import (  # noqa: E402
    apply_any_topology,
    instrument_control,
)
from org_frontier.questions.q55_bijective_discriminator.discriminator_utils import (  # noqa: E402
    enriched_panel,
    rules_for_label,
    split_below_ceiling,
)

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

LABELS = ("W", "S", "C")
PHI_TOL = 1e-6

OUTER_W = "2 parts: {W,SC}"
OUTER_C = "2 parts: {WS,C}"
OUTER_S = "2 parts: {S,WC}"
COMPLETE = "3 parts: {W,S,C}"
PARTITION_TYPES = (OUTER_W, OUTER_C, OUTER_S, COMPLETE)
OUTER_PARTY_TYPES = (OUTER_W, OUTER_C)


def ceiling_panel():
    """Thirty-two bijective parity ceiling pairs from Q55."""
    rows = enriched_panel()
    _, ceiling = split_below_ceiling(rows)
    return ceiling


def symmetric_ceiling():
    return [r for r in ceiling_panel() if r["topology"].startswith("symmetric")]


def one_sided_ceiling():
    return [r for r in ceiling_panel() if not r["topology"].startswith("symmetric")]


def rules_for_row(row):
    return apply_any_topology(rules_for_label(row["label"]), row["topology"])


def directional_symmetric(rules):
    """True iff each party has in-degree == out-degree and W mirrors C."""
    cm = cm_from_rules(rules)
    out_deg = {LABELS[i]: int(cm[i].sum()) for i in range(3)}
    in_deg = {LABELS[i]: int(cm[:, i].sum()) for i in range(3)}
    for party in LABELS:
        if out_deg[party] != in_deg[party]:
            return False
    return out_deg["W"] == out_deg["C"] and in_deg["W"] == in_deg["C"]


def partition_scan(rules):
    """Return official ties, system phi, and per-type flags at system phi."""
    v, sia, official = mip_ties(rules, labels=LABELS)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=LABELS)
    sub = pyphi.Subsystem(net, tuple(v.mip_state))
    parts = new_big_phi.system_partitions(sub.node_indices, node_labels=net.node_labels)
    sys_phi = float(sia.phi)
    at_sys = {t: False for t in PARTITION_TYPES}
    min_norm = {t: None for t in PARTITION_TYPES}
    for p in parts:
        r = new_big_phi.evaluate_partition(p, sub, sia.system_state)
        phi = float(r.phi)
        if abs(phi - sys_phi) > PHI_TOL:
            continue
        first = str(p).splitlines()[0].strip()
        if first not in PARTITION_TYPES:
            continue
        at_sys[first] = True
        norm = float(r.normalized_phi)
        if min_norm[first] is None or norm < min_norm[first]:
            min_norm[first] = norm
    return {
        "official": sorted(official),
        "sys_phi": sys_phi,
        "at_sys": at_sys,
        "min_norm": min_norm,
    }


def predict_ties_from_min_norm(scan):
    vals = [v for v in scan["min_norm"].values() if v is not None]
    if not vals:
        return []
    lo = min(vals)
    return sorted(
        t for t in PARTITION_TYPES
        if scan["min_norm"][t] is not None and abs(scan["min_norm"][t] - lo) < PHI_TOL
    )


def scan_row(row):
    rules = rules_for_row(row)
    scan = partition_scan(rules)
    outer_in_official = [t for t in OUTER_PARTY_TYPES if t in scan["official"]]
    return {
        **row,
        "rules": rules,
        "official": scan["official"],
        "sys_phi": scan["sys_phi"],
        "at_sys": scan["at_sys"],
        "min_norm": scan["min_norm"],
        "predicted": predict_ties_from_min_norm(scan),
        "dir_symmetric": directional_symmetric(rules),
        "outer_in_official": outer_in_official,
        "outer_count_official": len(outer_in_official),
    }
