"""Q102: the relation skeleton — over which purviews do a coordination's relations concentrate?

Relations bind distinctions over shared purviews. Q100 found the breadth market carries 128 relations
against the read-recipient triad's 8. This reads where those relations sit: in a mediated triad almost all
relations overlap on the mediator's purview (a hub), and the count explodes because every subset of the
distinctions sharing the hub forms a relation over it. A symmetric triad spreads its relations across
purviews with no single hub.

`relation_skeleton` returns the relation count, the hub purview (the purview carrying the most relations)
and its share, and the maximal relation order (the most distinctions any one relation binds).

Imported by `probe_relation_skeleton.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from collections import Counter

import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.questions.q99_binding_distinction import forms as q99

MEDIATED = {
    "read_recipient": q99.read_recipient(),
    "all_required_k2": q99.TRIADIC["all_required_k2"],
}
SYMMETRIC = {
    "ring_d2": q99.TRIADIC["ring_d2"],
    "market_N2": q99.TRIADIC["market_all_required_N2"],
}


def relation_skeleton(rules, labels):
    n = len(rules)
    net = pyphi.Network(tpm_from_rules(rules), cm=cm_from_rules(rules), node_labels=labels)
    ps = nbp.phi_structure(pyphi.Subsystem(net, tuple(1 for _ in range(n))))
    rels = list(ps.relations)
    if not rels:
        return {"n_relations": 0, "n_distinctions": len(ps.distinctions),
                "hub": (), "hub_share": 0.0, "max_order": 0}
    by_purview = Counter(frozenset(u.index for u in r.purview) for r in rels)
    hub_pv, hub_n = by_purview.most_common(1)[0]
    max_order = max(len(r.mechanisms) for r in rels)
    return {
        "n_relations": len(rels),
        "n_distinctions": len(ps.distinctions),
        "hub": tuple(sorted(labels[i] for i in hub_pv)),
        "hub_share": round(hub_n / len(rels), 3),
        "max_order": max_order,
    }
