"""Q106: a catalog of design operations and their verdict effects.

Each operation is a named edit to a coordination form that moves the verdict in a stated direction. The
law has two conditions a party must meet — the mediator binding it into the joint determination, and the
party keeping itself live to the commit — plus the requirement that all parties be jointly needed rather
than substitutable. Three levers, then: binding, liveness, requirement. Each carries a build operation
(dyadic to triadic) and its inverse break operation (triadic to dyadic).

Each entry is (lever, direction, before_rules, before_labels, after_rules, after_labels). The build and
break of a lever are inverses: the build's output form is the break's input form.

Imported by `probe_design_operations.py`.
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.questions.q64_outreach_breadth_scaling import forms as q64

L3 = ("E", "M", "R")
BROADCAST = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]            # M' = E        (dyadic)
READ_RECIPIENT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]  # M' = E & R   (triadic)
ONE_SHOT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[2]]      # R' = R        (dyadic, liveness broken)

ALL_REQUIRED = (q64.all_required(2), q64.labels(2))                     # triadic
SUBSTITUTABLE = (q64.substitutable(2), q64.labels(2))                   # dyadic

OPERATIONS = {
    "add_binding": ("binding", "build", BROADCAST, L3, READ_RECIPIENT, L3),
    "remove_binding": ("binding", "break", READ_RECIPIENT, L3, BROADCAST, L3),
    "restore_liveness": ("liveness", "build", ONE_SHOT, L3, READ_RECIPIENT, L3),
    "break_liveness": ("liveness", "break", READ_RECIPIENT, L3, ONE_SHOT, L3),
    "require_all": ("requirement", "build", SUBSTITUTABLE[0], SUBSTITUTABLE[1],
                    ALL_REQUIRED[0], ALL_REQUIRED[1]),
    "substitute": ("requirement", "break", ALL_REQUIRED[0], ALL_REQUIRED[1],
                   SUBSTITUTABLE[0], SUBSTITUTABLE[1]),
}
