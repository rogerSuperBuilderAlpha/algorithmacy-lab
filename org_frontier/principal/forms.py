"""Coordination forms with a corporate principal P who authors the mediator.

Paper 1 of the dissertation argues platforms are corporate-authored: a four-feature mediator with a
corporate principal whose objectives neither the worker nor the counterpart controls. None of the
other experiments model that principal. These do.

Nodes: 0 = W (worker), 1 = S (system/mediator), 2 = C (counterpart), 3 = P (principal). The baseline
W–S–C triad (S' = W ∧ C, each end tracks S) is irreducible on its own (Φ = 2.0). Each form adds the
principal a different way, and the question is whether P joins the irreducible core (the major
complex) or sits outside it.
"""

from dataclasses import dataclass
from typing import Callable, List

LABELS = ("W", "S", "C", "P")


@dataclass
class PForm:
    key: str
    title: str
    rules: List[Callable]
    rationale: str


FORMS = [
    PForm(
        key="passive_principal",
        title="Principal owns the system but does not act (static)",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
        rationale="S' = W ∧ C (the bare triad); P is a self-loop. Pure ownership, no dynamics.",
    ),
    PForm(
        key="extractive_monitor",
        title="Principal monitors outcomes but does not shape the determination",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
        rationale="P reads S (monitors the commit); S does not read P. One-directional, downstream.",
    ),
    PForm(
        key="gates_static_P",
        title="Principal gates each determination but does not respond",
        rules=[lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]],
        rationale="S' = W ∧ C ∧ P (P must enable each commit); P is static. One-directional, upstream.",
    ),
    PForm(
        key="gates_and_monitors",
        title="Principal both gates the determination and responds to outcomes",
        rules=[lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
        rationale="S' = W ∧ C ∧ P and P' = S. Bidirectional: P shapes the commit and tracks it.",
    ),
]
