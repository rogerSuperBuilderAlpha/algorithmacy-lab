"""A fast exact-Φ probe for the mediation-boundary deep dive.

One call returns everything the chain reads off a coordination form: the dyadic-or-triadic verdict,
the maximum Φ over reachable states, the partition that achieves it, and the major-complex membership.
Rules are per-node Boolean callables on the little-endian state tuple, the lab's standard encoding.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.threads.coalition_structure._harness import network, complex_over_states


def probe(rules, labels):
    """Return a dict: structure, phi (max Φ over states), mip (partition repr), core (major complex)."""
    v = classify_rules(rules, labels)
    net, tpm = network(rules, labels)
    _, core, core_phi = complex_over_states(net, tpm, len(rules))
    members = "".join(labels[i] for i in sorted(core)) if core else "-"
    return {
        "structure": v.structure,
        "phi": round(v.max_phi, 3),
        "mip": v.mip_partition,
        "core": members,
        "core_phi": round(core_phi, 3),
    }


def show(tag, rules, labels):
    p = probe(rules, labels)
    print(f"  {tag:<46} {p['structure']:<8} Φ={p['phi']:<6} core={p['core']:<5} (coreΦ={p['core_phi']})")
    return p
