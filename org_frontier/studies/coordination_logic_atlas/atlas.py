"""Coordination-logic atlas: 50 experiments on what makes a coordination form irreducible.

Each experiment is a small Boolean dynamical system whose nodes are the parties of a coordination
form. The verdict is exact IIT-4.0 Φ over the minimum-information partition: Φ_MIP = 0 means the
form factors along a party-line cut (DYADIC); Φ_MIP > 0 means it does not (TRIADIC). Where it
matters, the major complex names which parties form the irreducible core.

The 50 are organized in five themes that probe axes the existing logbook does not sweep
systematically:

  A. Quorum threshold (k-of-n)    — does an interior quorum bind the parties, or do they become
                                    substitutable and factor it?
  B. Topology at fixed node count — which wiring of four parties is irreducible?
  C. Redundancy and degeneracy    — does duplicating an element preserve irreducibility or open a
                                    factorizing backup path?
  D. Inhibition and valence       — does the sign of a coupling (veto, NAND, NOR, implication)
                                    change the verdict its excitatory analogue gets?
  E. Heterogeneity and bias       — asymmetric arity, memory, constant-policy and read-only nodes.

Every experiment carries a prediction fixed from two established principles in this lab
(`org_frontier/probes/PROBES.md`): a party is in the irreducible core only if it both feeds and
reads the determination (bidirectionality), and its membership rises with the determination's
sensitivity to it (pivotality). The run reports where the verdict matched the prediction and where
it did not. Rules are little-endian: rules[j](x) reads x[0], x[1], ... and returns node j's next
bit.

Run from the repo root with the venv active:  python -m org_frontier.studies.coordination_logic_atlas.run
"""

import os
import sys
from dataclasses import dataclass
from typing import Callable, List, Optional, Sequence, Tuple

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import classify_rules
from org_frontier.probes.lib import major_complex
from org_frontier.classifier.validate import factoring_control, irreducible_control


@dataclass
class Experiment:
    eid: str                         # e.g. "A3"
    theme: str
    name: str
    rules: Sequence[Callable]
    labels: Tuple[str, ...]
    predict: str                     # "triadic" | "dyadic"
    rationale: str                   # the pre-registered reason
    anchor: bool = False             # True if it reproduces a known result (control, not novel)


# ----------------------------------------------------------------------------------------------
# Theme A — Quorum threshold (k-of-n). Parties 0..p-1 read the mediator (node p); the mediator
# fires iff at least k parties are active. Prediction: a party is pivotal only when the quorum
# sits at an extreme (k=1: any party can trigger alone; k=p: any party can veto). At an interior
# quorum each party is substitutable, so no party is individually pivotal and the form factors.
# ----------------------------------------------------------------------------------------------

def quorum(p: int, k: int) -> Tuple[List[Callable], Tuple[str, ...]]:
    rules = [(lambda x, _p=p: x[_p]) for _ in range(p)]
    rules.append(lambda x, _p=p, _k=k: int(sum(x[0:_p]) >= _k))
    labels = tuple(f"P{i}" for i in range(p)) + ("S",)
    return rules, labels


def _quorum_exp(p: int, k: int) -> Experiment:
    rules, labels = quorum(p, k)
    extreme = (k == 1 or k == p)
    predict = "triadic" if extreme else "dyadic"
    if extreme:
        why = ("unanimity: every party can veto, so every party is pivotal" if k == p
               else "any-one: every party can trigger alone, so every party is pivotal")
    else:
        why = f"interior quorum {k}/{p}: each party is substitutable, none individually pivotal"
    return Experiment(f"A{p}{k}", "quorum", f"{p}-party k={k}-of-{p}", rules, labels,
                      predict, why, anchor=extreme)


THEME_A = [
    _quorum_exp(2, 1), _quorum_exp(2, 2),
    _quorum_exp(3, 1), _quorum_exp(3, 2), _quorum_exp(3, 3),
    _quorum_exp(4, 1), _quorum_exp(4, 2), _quorum_exp(4, 3), _quorum_exp(4, 4),
    _quorum_exp(5, 1), _quorum_exp(5, 3), _quorum_exp(5, 5),
]


# ----------------------------------------------------------------------------------------------
# Theme B — Topology at a fixed four nodes (A,B,C,D = 0,1,2,3). Same parties, different wiring,
# read as organizational forms. Prediction from bidirectionality: a form is triadic when every
# node both feeds and reads through a shared determination; it is dyadic when it factors into
# independent pieces or when nodes are emit-only / read-only.
# ----------------------------------------------------------------------------------------------

def _b(name, rules, predict, why, anchor=False):
    return Experiment(name.split(" ", 1)[0], "topology", name.split(" ", 1)[1],
                      rules, ("A", "B", "C", "D"), predict, why, anchor)


THEME_B = [
    _b("B1 star (hub B reads all, spokes read hub)",
       [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[1]],
       "triadic", "centralized hub binds all spokes through one determination"),
    _b("B2 complete (each reads the other three)",
       [lambda x: x[1] & x[2] & x[3], lambda x: x[0] & x[2] & x[3],
        lambda x: x[0] & x[1] & x[3], lambda x: x[0] & x[1] & x[2]],
       "triadic", "fully coupled; no party-line cut survives"),
    _b("B3 ring (each reads its two neighbours, AND)",
       [lambda x: x[1] & x[3], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2] & x[0]],
       "triadic", "closed cycle of mutual reads, no factorizing cut"),
    _b("B4 line/chain (A-B-C-D with back-reads)",
       [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3], lambda x: x[2]],
       "triadic", "connected chain, every interior node mediates two sides"),
    _b("B5 two independent dyads ({A,B},{C,D})",
       [lambda x: x[1], lambda x: x[0], lambda x: x[3], lambda x: x[2]],
       "dyadic", "factors into two disjoint pairs", anchor=True),
    _b("B6 two-hub matrix (B,C hubs; A,D read both)",
       [lambda x: x[1] & x[2], lambda x: x[0] & x[3], lambda x: x[0] & x[3], lambda x: x[1] & x[2]],
       "triadic", "matrix org: two mediators jointly bind the workers"),
    _b("B7 feed-forward star (spokes do not read hub)",
       [lambda x: x[0], lambda x: x[0] & x[2] & x[3], lambda x: x[2], lambda x: x[3]],
       "dyadic", "spokes are emit-only sources; the hub is a downstream sink"),
    _b("B8 hub + isolated node (star on A,B,C; D self-loop)",
       [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]],
       "triadic", "triad {A,B,C} binds; D is decoupled and should shed from the core"),
    _b("B9 bipartite (each side reads the other side's AND)",
       [lambda x: x[2] & x[3], lambda x: x[2] & x[3], lambda x: x[0] & x[1], lambda x: x[0] & x[1]],
       "triadic", "complete bipartite coupling, no within-side factorization"),
    _b("B10 directed cycle (pure copy ring, no AND)",
       [lambda x: x[3], lambda x: x[0], lambda x: x[1], lambda x: x[2]],
       "dyadic", "a permutation/relabelling; each node copied, determination is reducible"),
]


# ----------------------------------------------------------------------------------------------
# Theme C — Redundancy and degeneracy. Does duplicating an element preserve irreducibility, or
# open an independent backup path the system can factor through? Labels name the roles.
# ----------------------------------------------------------------------------------------------

THEME_C = [
    Experiment("C1", "redundancy", "duplicate mediator (S1,S2 both = W&C; parties read S1|S2)",
               [lambda x: x[2] | x[3], lambda x: x[2] | x[3],
                lambda x: x[0] & x[1], lambda x: x[0] & x[1]],
               ("W", "C", "S1", "S2"), "triadic",
               "two mediators carry the same determination; degenerate but still irreducible"),
    Experiment("C2", "redundancy", "parallel channels (W->C via S1, W->C via S2, independent)",
               [lambda x: x[0], lambda x: x[2] | x[3], lambda x: x[0], lambda x: x[0]],
               ("W", "C", "S1", "S2"), "dyadic",
               "W feeds two one-way relays to C; no back-coupling, factors W from C"),
    Experiment("C3", "redundancy", "triple-modular mediator (3 copies, majority vote)",
               [lambda x: x[4], lambda x: x[4],
                lambda x: x[0] & x[1], lambda x: x[0] & x[1], lambda x: x[0] & x[1]],
               ("W", "C", "S1", "S2", "S3"), "triadic",
               "TMR over the same AND; the vote node S-stack binds W,C, redundantly"),
    Experiment("C4", "redundancy", "hot standby (S2 acts only when S1 is down)",
               [lambda x: x[2] | x[3], lambda x: x[2] | x[3],
                lambda x: x[0] & x[1], lambda x: (x[0] & x[1]) & (1 - x[2])],
               ("W", "C", "S1", "S2"), "triadic",
               "primary plus failover; the live mediator still binds the parties"),
    Experiment("C5", "redundancy", "degenerate parties (W1,W2 identical inputs to S)",
               [lambda x: x[3], lambda x: x[3], lambda x: x[0] & x[1] & x[2],
                lambda x: x[2]],
               ("W1", "W2", "S", "C"), "triadic",
               "two interchangeable workers; AND keeps each pivotal (each can veto)"),
    Experiment("C6", "redundancy", "substitutable workers (S = W1 OR W2, either suffices)",
               [lambda x: x[3], lambda x: x[3], lambda x: (x[0] | x[1]) & x[3],
                lambda x: x[2]],
               ("W1", "W2", "S", "C"), "dyadic",
               "OR makes either worker droppable; neither W is individually pivotal"),
    Experiment("C7", "redundancy", "redundant copy decoupled (S2 mirrors S1 but nobody reads it)",
               [lambda x: x[2], lambda x: x[2], lambda x: x[0] & x[1], lambda x: x[2]],
               ("W", "C", "S1", "S2"), "triadic",
               "core is {W,S1,C}; the unread copy S2 should shed from the major complex"),
    Experiment("C8", "redundancy", "dual mediators in series (W -> S1 -> S2 -> C and back)",
               [lambda x: x[2], lambda x: x[3], lambda x: x[0] & x[3], lambda x: x[1] & x[2]],
               ("W", "C", "S1", "S2"), "triadic",
               "two mediators chained with feedback; the loop binds all four"),
    Experiment("C9", "redundancy", "backup that factors (independent {W,S1} and {C,S2} pairs)",
               [lambda x: x[2], lambda x: x[3], lambda x: x[0], lambda x: x[1]],
               ("W", "C", "S1", "S2"), "dyadic",
               "two private worker-mediator pairs, no shared determination"),
    Experiment("C10", "redundancy", "shared mediator, redundant readout (C reads S twice-over)",
               [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[1]],
               ("W", "S", "C"), "triadic",
               "trivial readout redundancy; identical to the canonical triad, a control",
               anchor=True),
]


# ----------------------------------------------------------------------------------------------
# Theme D — Inhibition and valence. Three nodes W,S,C; parties read the mediator. The mediator's
# determination is inhibitory or mixed-sign. Prediction: the verdict tracks whether the I/O
# function is irreducible, not the sign of the coupling, so monotone-inhibitory mediators mirror
# their excitatory analogues. NOT(x) = 1-x.
# ----------------------------------------------------------------------------------------------

def _d(name, s_rule, predict, why, w_rule=None, c_rule=None, anchor=False):
    w = w_rule or (lambda x: x[1])
    c = c_rule or (lambda x: x[1])
    return Experiment(name.split(" ", 1)[0], "inhibition", name.split(" ", 1)[1],
                      [w, s_rule, c], ("W", "S", "C"), predict, why, anchor)


THEME_D = [
    _d("D1 veto (S = W AND NOT C)", lambda x: x[0] & (1 - x[2]),
       "triadic", "counterpart vetoes; both parties still feed and read the determination"),
    _d("D2 NAND (S = NOT(W AND C))", lambda x: 1 - (x[0] & x[2]),
       "triadic", "De Morgan dual of AND; same irreducible coupling, inverted output"),
    _d("D3 NOR (S = NOT(W OR C))", lambda x: 1 - (x[0] | x[2]),
       "triadic", "dual of OR; monotone-inhibitory, verdict should match OR"),
    _d("D4 implication (S = NOT W OR C)", lambda x: (1 - x[0]) | x[2],
       "triadic", "asymmetric mixed-sign gate; both parties determine S"),
    _d("D5 inverting feedback (parties read NOT S)", lambda x: x[0] & x[2],
       "triadic", "AND mediator but parties read its negation; coupling is intact, just inverted",
       w_rule=lambda x: 1 - x[1], c_rule=lambda x: 1 - x[1]),
    _d("D6 mutual inhibition (S = NOT W AND NOT C)", lambda x: (1 - x[0]) & (1 - x[2]),
       "triadic", "both parties suppress the determination; symmetric, irreducible"),
    _d("D7 one-sided veto, no back-read (C vetoes, C static)", lambda x: x[0] & (1 - x[2]),
       "dyadic", "C never reads S (emit-only veto source); it should drop out, leaving a dyad",
       c_rule=lambda x: x[2]),
    _d("D8 double negation control (S = NOT NOT (W AND C))",
       lambda x: 1 - (1 - (x[0] & x[2])),
       "triadic", "logically identical to AND; a valence control that must read triadic",
       anchor=True),
    _d("D9 XNOR veto-parity (S = NOT(W XOR C))", lambda x: 1 - (x[0] ^ x[2]),
       "triadic", "parity agreement gate; known irreducible, anchors the inhibition theme",
       anchor=True),
]


# ----------------------------------------------------------------------------------------------
# Theme E — Heterogeneity and bias. Asymmetric arity, memory, constant-policy and read-only roles.
# Prediction from bidirectionality + pivotality: constant and read-only nodes shed from the core;
# heterogeneous but bidirectional coupling stays triadic; a party with zero pivotality drops out.
# ----------------------------------------------------------------------------------------------

THEME_E = [
    Experiment("E1", "heterogeneity", "asymmetric arity (W reads S&C, C reads S only)",
               [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[1]],
               ("W", "S", "C"), "triadic",
               "worker reads more than counterpart; both still bidirectionally coupled"),
    Experiment("E2", "heterogeneity", "party with memory (W' = W OR S)",
               [lambda x: x[0] | x[1], lambda x: x[0] & x[2], lambda x: x[1]],
               ("W", "S", "C"), "triadic",
               "worker self-loop adds memory; coupling to S persists, stays irreducible"),
    Experiment("E3", "heterogeneity", "constant policy node (B always 1; S = W&C&B)",
               [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]],
               ("W", "S", "C", "B"), "triadic",
               "policy bias B is a constant self-loop; triad {W,S,C} binds, B should shed"),
    Experiment("E4", "heterogeneity", "read-only manager (M reads S, feeds nothing)",
               [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[1]],
               ("W", "S", "C", "M"), "triadic",
               "M is a read-only sink; core is {W,S,C}, M should drop out (cf. spectator)"),
    Experiment("E5", "heterogeneity", "dominated party (S follows W; C marginal: S = W AND (C OR 1))",
               [lambda x: x[1], lambda x: x[0] & (x[2] | 1), lambda x: x[1]],
               ("W", "S", "C"), "dyadic",
               "C has zero influence on S (C OR 1 == 1); zero pivotality, C drops, leaves a dyad"),
    Experiment("E6", "heterogeneity", "policy overrides counterpart (S = W AND (C OR B))",
               [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]), lambda x: x[1], lambda x: x[3]],
               ("W", "S", "C", "B"), "triadic",
               "B can substitute for C when B=1; C is conditionally pivotal, expect triadic core"),
    Experiment("E7", "heterogeneity", "one-way manager (M gates S but never reads back)",
               [lambda x: x[1], lambda x: x[0] & x[2] & x[3], lambda x: x[1], lambda x: x[3]],
               ("W", "S", "C", "M"), "triadic",
               "M feeds the determination but is a constant source; {W,S,C} core, M sheds"),
    Experiment("E8", "heterogeneity", "graded fan-out (W feeds S and C; C feeds only S)",
               [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[0]],
               ("W", "S", "C"), "triadic",
               "worker reaches the counterpart both directly and through S; still irreducible"),
    Experiment("E9", "heterogeneity", "two managers, both read-only (M1,M2 watch S)",
               [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1],
                lambda x: x[1], lambda x: x[1]],
               ("W", "S", "C", "M1", "M2"), "triadic",
               "two read-only observers; core stays {W,S,C}, both managers shed"),
]


EXPERIMENTS: List[Experiment] = THEME_A + THEME_B + THEME_C + THEME_D + THEME_E

THEME_ORDER = ["quorum", "topology", "redundancy", "inhibition", "heterogeneity"]
THEME_TITLE = {
    "quorum": "A. Quorum threshold (k-of-n)",
    "topology": "B. Topology at fixed node count",
    "redundancy": "C. Redundancy and degeneracy",
    "inhibition": "D. Inhibition and valence",
    "heterogeneity": "E. Heterogeneity and bias",
}


@dataclass
class Result:
    eid: str
    theme: str
    name: str
    n: int
    predict: str                 # predicted whether the coordination's core binds
    structure: str               # whole-system verdict (sensitive to spectators)
    max_phi: float               # whole-system Φ_MIP
    core: Optional[Tuple[str, ...]]
    core_phi: float              # Φ of the major complex (the instrument for "does it bind")
    core_size: int
    binds: bool                  # core exists and is irreducible (core_phi > eps)
    n_irreducible: int
    matched: bool                # binds == (predict == "triadic")
    anchor: bool
    rationale: str


_EPS = 1e-9


def run_experiment(exp: Experiment) -> Result:
    v = classify_rules(exp.rules, exp.labels)
    core, core_phi = major_complex(list(exp.rules), exp.labels)
    binds = core is not None and core_phi > _EPS
    return Result(
        eid=exp.eid, theme=exp.theme, name=exp.name, n=len(exp.labels),
        predict=exp.predict, structure=v.structure, max_phi=round(v.max_phi, 6),
        core=core, core_phi=round(max(core_phi, 0.0), 6), core_size=(len(core) if core else 0),
        binds=binds, n_irreducible=v.n_states_irreducible,
        matched=(v.structure == exp.predict), anchor=exp.anchor, rationale=exp.rationale,
    )


def validate_instrument() -> bool:
    """Both canonical controls must reproduce before any atlas verdict is trusted."""
    fac = classify_rules(factoring_control())
    irr = classify_rules(irreducible_control())
    return fac.structure == "dyadic" and irr.structure == "triadic"
