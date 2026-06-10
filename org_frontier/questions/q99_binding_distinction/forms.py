"""Q99: the cause-effect structure of coordination, read for its dual binding pair.

The read-recipient triad's structure carries two paired distinctions: a spanning distinction, whose
mechanism is one party (the mediator) but whose purview is the others jointly ({M}→{E,R}); and a joint
distinction, whose mechanism is the others jointly and whose purview is that party ({E,R}→{M}). The two
are duals — the purview of one is the mechanism of the other. This module reads that structure across
structurally different triads (joint determination, depth as a chain and a ring, a required market) and
dyadic controls, to test whether the dual pair is the common shape of irreducible coordination.

The cause-effect structure is read once at the integrating state (all-ones if reachable, else the
reachable state of maximum structure Φ), via PyPhi's `phi_structure`.

Imported by `probe_binding_distinction.py`.
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
from foundations.proxy_audit.exact_phi import reachable_states
from org_frontier.questions.q64_outreach_breadth_scaling import forms as q64
from org_frontier.questions.q66_chain_core_boundary import forms as q66
from org_frontier.questions.q85_agent_market import forms as q85


# --- curated forms: structurally different triads, and dyadic controls ---

def read_recipient():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("E", "M", "R")


def broadcast():
    return [lambda x: x[1], lambda x: x[0], lambda x: x[1]], ("E", "M", "R")


def one_shot():
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]], ("E", "M", "R")


TRIADIC = {
    "read_recipient": read_recipient(),
    "all_required_k2": (q64.all_required(2), q64.labels(2)),
    "open_chain_d2": (q66.open_chain(2), q66.chain_labels(2)),
    "ring_d2": (q66.ring(2), q66.chain_labels(2)),
    "market_all_required_N2": (q85.all_required(2), q85.labels(2)),
}
DYADIC = {
    "broadcast": broadcast(),
    "one_shot": one_shot(),
    "substitutable_k2": (q64.substitutable(2), q64.labels(2)),
}


def ces(rules, labels):
    """The cause-effect structure at the integrating state: distinctions as
    (mechanism_labels, effect_purview_labels, phi_d), plus the structure Φ."""
    n = len(rules)
    tpm, cm = tpm_from_rules(rules), cm_from_rules(rules)
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    states = [tuple(1 for _ in range(n))] + [
        tuple((s >> i) & 1 for i in range(n)) for s in reachable_states(tpm, n)
    ]
    best, best_phi = None, -1.0
    seen = set()
    for st in states:
        if st in seen:
            continue
        seen.add(st)
        try:
            ps = nbp.phi_structure(pyphi.Subsystem(net, st))
        except Exception:
            continue
        if float(ps.phi) > best_phi:
            best_phi, best = float(ps.phi), ps
        if st == tuple(1 for _ in range(n)) and float(ps.phi) > 0:
            break          # the all-ones integrating state suffices when it integrates
    if best is None:
        return 0.0, []
    dists = [
        (tuple(labels[i] for i in d.mechanism),
         tuple(labels[i] for i in d.effect.purview),
         round(float(d.phi), 3))
        for d in best.distinctions
    ]
    return round(best_phi, 3), dists


def dual_pair(dists):
    """Find a (spanning, joint) dual pair: a 1-party mechanism whose purview P has |P|>=2, and a
    higher-order mechanism equal to P whose purview is that 1-party mechanism. Returns the pair or None."""
    spanning = [(m, p, pd) for m, p, pd in dists if len(m) == 1 and len(p) >= 2]
    for sm, sp, spd in spanning:
        for jm, jp, jpd in dists:
            if len(jm) >= 2 and set(jm) == set(sp) and set(jp) == set(sm):
                return {"spanning": (sm, sp, spd), "joint": (jm, jp, jpd)}
    return None
