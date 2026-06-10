"""Q100: cause-effect-structure fingerprints of keystone triads from different coordination kinds.

Q99 found that triads come in structural types — mediated, symmetric, distributed. This reads a richer
fingerprint (distinction and relation counts, orders, dual type) for a keystone triad of each coordination
kind on the record, and asks whether the structure separates kinds the scalar verdict calls identical, and
whether two forms with equal Φ can carry different structure.

Keystones: read_recipient (joint determination, mediated); all_required market k=2 (breadth, mediated);
open chain d=2 (depth, distributed); ring d=2 (symmetric); required market N=2 (symmetric); triage
delegation (Q68 bidirectional).

Imported by `probe_structure_fingerprint.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from foundations.proxy_audit.exact_phi import reachable_states
from foundations.structure_suite.suite import extract_suite
from org_frontier.questions.q99_binding_distinction import forms as q99
from org_frontier.questions.q68_triage_gating import forms as q68

KEYSTONES = {
    "joint_determination": q99.read_recipient(),
    "breadth_market_k2": q99.TRIADIC["all_required_k2"],
    "depth_chain_d2": q99.TRIADIC["open_chain_d2"],
    "ring_d2": q99.TRIADIC["ring_d2"],
    "market_N2": q99.TRIADIC["market_all_required_N2"],
    "delegation_triage": (q68.BIDIRECTIONAL, q68.LABELS),
}


def fingerprint(rules, labels):
    """Return the structural fingerprint at the integrating state: the Φ-structure suite plus the dual
    type and the system Φ."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    states = [tuple(1 for _ in range(n))] + [
        tuple((s >> i) & 1 for i in range(n)) for s in reachable_states(tpm, n)
    ]
    best, best_phi = None, -1.0
    seen = set()
    for st in states:
        if st in seen:
            continue
        seen.add(st)
        suite = extract_suite(tpm, cm, n, st)
        if suite is None:
            continue
        if suite["phi"] > best_phi:
            best_phi, best = suite["phi"], suite
        if st == tuple(1 for _ in range(n)) and suite["phi"] > 0:
            break
    _, dists = q99.ces(rules, labels)
    dtype = q99.dual_type(dists)
    if best is None:
        best = {"phi": 0.0, "n_distinctions": 0, "n_relations": 0, "max_order": 0,
                "mean_order": 0.0, "sum_phi_distinctions": 0.0, "sum_phi_relations": 0.0}
    return {
        "phi": round(float(best["phi"]), 3),
        "n_distinctions": int(best["n_distinctions"]),
        "n_relations": int(best["n_relations"]),
        "max_order": int(best["max_order"]),
        "dual_type": dtype,
    }
