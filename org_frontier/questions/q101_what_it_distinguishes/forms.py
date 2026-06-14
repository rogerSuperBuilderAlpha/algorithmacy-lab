"""Q101: what a coordination distinguishes — the specified states of the binding distinction.

A distinction does not only have a purview; it specifies a state of that purview, the configuration the
mechanism tells apart. The read-recipient triad's binding distinction (the mediator with purview {E, R})
specifies the joint state (1, 1): the mediator distinguishes precisely the configuration where both parties
are present and the joint determination fires. This module reads the specified joint state of the binding
distinction across triadic forms, against dyadic controls, to ask what coordination distinguishes.

Imported by `probe_what_it_distinguishes.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import new_big_phi as nbp

from org_frontier.classifier.classifier import tpm_from_rules, cm_from_rules
from org_frontier.questions.q99_binding_distinction import forms as q99

TRIADIC = {
    "read_recipient": q99.read_recipient(),
    "all_required_k2": q99.TRIADIC["all_required_k2"],
    "market_N2": q99.TRIADIC["market_all_required_N2"],
}
DYADIC = {
    "broadcast": q99.broadcast(),
    "one_shot": q99.one_shot(),
}


def binding_specified_state(rules, labels):
    """Return (purview_labels, effect_state, cause_state) for the binding distinction — a single-party
    mechanism whose purview spans two or more parties — or None if there is no such distinction."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    try:
        ps = nbp.phi_structure(pyphi.Subsystem(net, tuple(1 for _ in range(n))))
    except Exception:
        return None
    if float(ps.phi) <= 0:
        return None
    for d in ps.distinctions:
        if len(d.mechanism) == 1 and len(d.effect.purview) >= 2:
            purview = tuple(labels[i] for i in d.effect.purview)
            return purview, tuple(int(b) for b in d.effect.purview_state), \
                tuple(int(b) for b in d.cause.purview_state)
    return None


def max_joint_specified_state(rules, labels):
    """The specified effect state of the highest-order distinction (the joint mechanism), as
    (mechanism_labels, purview_labels, effect_state), or None."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    try:
        ps = nbp.phi_structure(pyphi.Subsystem(net, tuple(1 for _ in range(n))))
    except Exception:
        return None
    if float(ps.phi) <= 0:
        return None
    hi = max((d for d in ps.distinctions if len(d.mechanism) >= 2),
             key=lambda d: (len(d.mechanism), float(d.phi)), default=None)
    if hi is None:
        return None
    return (tuple(labels[i] for i in hi.mechanism),
            tuple(labels[i] for i in hi.effect.purview),
            tuple(int(b) for b in hi.effect.purview_state))
