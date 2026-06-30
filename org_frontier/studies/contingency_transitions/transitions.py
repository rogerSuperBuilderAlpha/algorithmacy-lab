"""Contingency transitions — the operations that move an intermediary between cells.

An intermediary's class is not fixed. A policy move or a business move changes the coordination's form, and
the bypass-counterfactual re-classifies it. This makes the four cells a state machine: contingent, necessary,
partial, reducible are the states, and named operations are the edges. Each operation is modeled as a
before-form and an after-form (the four catalog templates), and both are classified.

The operations map to the levers regulators and firms actually pull:
  open the bypass    — deregulation, mandated interoperability, an antitrust remedy, breaking an exclusive
  erect a constraint — a new law or license, an exclusive contract, a walled garden
  integrate          — building a service that computes a joint condition the direct tie cannot reproduce
  commoditize        — the integration becomes reproducible (open standards), so the bypass can now do it

This extends q106's design operations (which change the mediator's function) with the constraint lever (which
changes whether a bypass exists), the move contingent irreducibility added.
"""


def _relay():
    return ("A", "M", "C"), [lambda x: x[2], lambda x: x[0], lambda x: x[1]], "M", "C", "A", "replace"


def _conjunctive():
    return ("A", "M", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "C", "A", "replace"


def _additive():
    return ("A", "M", "C"), [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], "M", "C", "A", "add"


def _free():
    return ("A", "M", "C"), [lambda x: x[2], lambda x: x[0], lambda x: x[0]], "M", "C", "A", "replace"


TEMPLATES = {"relay": _relay, "conjunctive": _conjunctive, "additive": _additive, "free": _free}

# (operation, before_template, after_template, expected_before, expected_after, real example)
TRANSITIONS = [
    ("open_the_bypass", "relay", "free", "contingent", "reducible",
     "deregulation / mandated interoperability: franchise-law repeal, DMA sideloading, the NAR settlement"),
    ("erect_a_constraint", "free", "relay", "reducible", "contingent",
     "a new law, license, exclusive contract, or walled garden goes up around a free conduit"),
    ("integrate", "relay", "conjunctive", "contingent", "intrinsic",
     "a relay builds a joint-condition service: a payments pipe adds fraud-scoring, a pipe becomes a clearinghouse"),
    ("commoditize", "conjunctive", "free", "intrinsic", "reducible",
     "the integration becomes reproducible: open-standard matching, credit data opened, so the direct tie can do it"),
    ("raise_the_gate", "additive", "relay", "partial", "contingent",
     "a partial intermediary closes its direct channel and forces routing through the gate"),
    ("lower_the_gate", "additive", "free", "partial", "reducible",
     "the direct channel takes over a partial intermediary: self-service erodes the agent until the bypass is default"),
]
