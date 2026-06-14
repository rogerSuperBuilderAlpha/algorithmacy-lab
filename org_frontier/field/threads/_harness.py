"""Tiny harness for the mediator-in-core thread: classify a form and say whether the mediator
node sits in the irreducible core. Import P from here in thread steps."""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import major_complex


def P(name, rules, labels, mediator="S", show=True):
    """Classify a form; return (structure, max_phi, core_tuple, core_phi, mediator_in_core)."""
    v = classify_rules(rules, labels)
    core, cphi = major_complex(list(rules), labels)
    core = core or ()
    cphi = max(cphi, 0.0)
    incore = mediator in set(core)
    if show:
        tag = "" if mediator in labels else "  (no mediator node named)"
        print(f"  {name:<40} {v.structure:<8} sysΦ={v.max_phi:5.2f}  "
              f"core={''.join(core) if core else '—':<7} Φ={cphi:4.2f}  "
              f"[{mediator}∈core: {incore}]{tag}")
    return v.structure, round(v.max_phi, 3), core, round(cphi, 3), incore
