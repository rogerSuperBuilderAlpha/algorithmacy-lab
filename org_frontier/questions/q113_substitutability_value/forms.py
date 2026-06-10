"""Q113: does substitutability erode value, or destroy it?

Q111 valued each party by its Shapley share of the coordination's integrated information. This applies the
value measure to a market of agents: an all-required market, where every agent is needed, against a
substitutable market, where the agents are interchangeable. Finding 5 makes the substitutable market dyadic,
so its total value is zero — substitutability does not merely lower the substitutable agents' share, it
collapses the whole coordination's value.

`shapley_for` reuses Q111's Shapley value of subsystem-Φ on the Q85 market forms.

Imported by `probe_substitutability_value.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q111_shapley_value import forms as q111
from org_frontier.questions.q85_agent_market import forms as q85

ALL_REQUIRED = (q85.all_required(2), q85.labels(2))      # triadic, Φ = 4
SUBSTITUTABLE = (q85.substitutable(2), q85.labels(2))    # dyadic, Φ = 0


def shapley_for(builder):
    rules, labels = builder
    return q111.shapley(rules, labels)
