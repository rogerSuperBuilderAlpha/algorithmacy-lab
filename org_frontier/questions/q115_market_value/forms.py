"""Q115: the value distribution of a required market at scale.

Q113 found an all-required market at N=2 distributes value equally. This scales it: at N = 2, 3, 4, how is
the value split between the two unique outer parties (worker and counterpart) and the N required agents? The
agents are all required, so none is substitutable; the question is whether scale rewards them or commoditizes
them.

`market_shapley(N)` reuses Q111's Shapley value of subsystem-Φ on the Q85 all-required market.

Imported by `probe_market_value.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q111_shapley_value import forms as q111
from org_frontier.questions.q85_agent_market import forms as q85

SIZES = (2, 3, 4)


def market_shapley(N):
    sv, phi = q111.shapley(q85.all_required(N), q85.labels(N))
    outer = sv["E"]                                    # a unique outer party (worker; counterpart equal)
    agent = sv["M1"]                                   # one required agent (all agents equal)
    return {"phi": phi, "outer": round(outer, 3), "agent": round(agent, 3),
            "total": round(sum(sv.values()), 3), "all": sv}
