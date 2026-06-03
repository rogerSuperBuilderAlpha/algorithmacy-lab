"""Named four-party coordination forms.

Node order 0 = W (worker), 1 = S (system/mediator), 2 = C1, 3 = C2 (two counterparts) — except
the chain form, where the nodes are W, S1, S2, C. Each form is rendered as per-party Boolean rules
and carries a rationale. The conjunctive pooled form reproduces the dissertation's higher-order
result (S' = W ∧ C ∧ D gives Φ = 3.0 for pooled rideshare / crowdwork), validating the n = 4
modeling.

The question these forms probe: when a worker coordinates with MORE than one counterpart through a
mediator, does the form still demand algorithmacy?
"""

from dataclasses import dataclass
from typing import Callable, List


@dataclass
class MPForm:
    key: str
    title: str
    rules: List[Callable]
    labels: tuple
    rationale: str
    expected: str


FORMS = [
    MPForm(
        key="pool_all_required",
        title="Platform pools worker with two counterparts; match requires all three",
        rules=[lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
        labels=("W", "S", "C1", "C2"),
        rationale="S commits iff worker AND both counterparts are present (all-required). "
                  "Matches the dissertation's pooled rideshare/crowdwork (Φ = 3.0).",
        expected="triadic",
    ),
    MPForm(
        key="substitutable_counterparts",
        title="Either counterpart suffices (substitutable)",
        rules=[lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[1]],
        labels=("W", "S", "C1", "C2"),
        rationale="S commits iff worker AND (C1 OR C2). The counterparts are interchangeable, so "
                  "the determination does not bind all parties jointly.",
        expected="dyadic",
    ),
    MPForm(
        key="one_counterpart_constitutive",
        title="Only the first counterpart enters the determination",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
        labels=("W", "S", "C1", "C2"),
        rationale="S reads only W and C1; C2 tracks S but is not constitutive. Reduces to the "
                  "three-party case with a spectator.",
        expected="dyadic",
    ),
    MPForm(
        key="decoupled_control",
        title="Second counterpart fully decoupled (control)",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
        labels=("W", "S", "C1", "C2"),
        rationale="C2 is a self-loop, outside the coordination. Must factor (a control).",
        expected="dyadic",
    ),
    MPForm(
        key="mediator_chain",
        title="Two mediators in series (W -> S1 -> S2 -> C)",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]],
        labels=("W", "S1", "S2", "C"),
        rationale="A layered platform: S1 commits from W and S2's state; S2 from S1 and C; the "
                  "ends read only their adjacent mediator. Open question — compute.",
        expected="?",
    ),

    # Breadth x depth: a depth-2 chain whose final mediator serves two counterparts.
    # Tests whether mediation depth rescues a form where the counterparts are substitutable.
    MPForm(
        key="deep_pool_all",
        title="Depth-2 chain, final mediator requires both counterparts",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3] & x[4],
               lambda x: x[2], lambda x: x[2]],
        labels=("W", "S1", "S2", "C1", "C2"),
        rationale="Depth AND an all-required joint determination. Stays triadic.",
        expected="triadic",
    ),
    MPForm(
        key="deep_substitutable",
        title="Depth-2 chain, final mediator accepts either counterpart",
        rules=[lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & (x[3] | x[4]),
               lambda x: x[2], lambda x: x[2]],
        labels=("W", "S1", "S2", "C1", "C2"),
        rationale="Depth does NOT rescue substitutability: still factors (dyadic).",
        expected="dyadic",
    ),

    # Multi-homing: worker and counterpart connected through TWO platforms (S1, S2). Tests whether
    # substitutability of the MEDIATOR factors the form, as substitutability of the counterpart did.
    MPForm(
        key="multihome_either",
        title="Multi-homing: worker/counterpart use either of two platforms",
        rules=[lambda x: x[1] | x[2], lambda x: x[0] & x[3], lambda x: x[0] & x[3],
               lambda x: x[1] | x[2]],
        labels=("W", "S1", "S2", "C"),
        rationale="Redundant platforms, either suffices. Substitutable mediators factor (dyadic).",
        expected="dyadic",
    ),
    MPForm(
        key="multihome_both",
        title="Multi-homing: worker/counterpart must clear both platforms",
        rules=[lambda x: x[1] & x[2], lambda x: x[0] & x[3], lambda x: x[0] & x[3],
               lambda x: x[1] & x[2]],
        labels=("W", "S1", "S2", "C"),
        rationale="Both platforms required (all-binding). Stays triadic.",
        expected="triadic",
    ),
]
