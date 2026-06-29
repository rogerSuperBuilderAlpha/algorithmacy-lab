"""Contingent vs. intrinsic irreducibility — the bypass-counterfactual classifier.

A party can sit in a triad's irreducible core for two different reasons.

INTRINSIC: it does integrative work no direct edge between its neighbours reproduces, so it
stays in the core even when that forbidden edge is restored. A conjunctive mediator S=W&C is
the type case — handing C a direct line to W does not let the pair recover the joint condition
S computes.

CONTINGENT: it is a conduit that would factor out, held in the core only because the bypass
edge is forbidden. Restore the edge and it leaves. A car dealer relays a car from maker to
buyer and does no integrating; it sits in the core only because franchise law forbids the maker
selling direct. Lift the law and the dealer is disintermediated.

The lab's constitutive law (essays/mediated_or_irreducible.md) says a conduit factors. Contingent
irreducibility is the exception that law does not cover: a conduit that does not factor, because a
constraint removes the alternative to it. This is constraint-contingency, distinct from the
state-contingent membership of q96 (a gated read, which behaves as optionality).

The test restores the forbidden bypass edge and recomputes the major complex:

    party in core, leaves under bypass         -> contingent  (de jure: held by the constraint)
    party in core, stays, margin ~ 0           -> intrinsic   (de facto: held by its own role)
    party in core, stays, 0 < margin           -> partial     (part role, part constraint)
    party not in core                          -> reducible   (a free conduit, already out)

The contingency margin is the whole-system Phi_MIP lost when the bypass opens.
"""

from dataclasses import dataclass

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import PHI_EPS


@dataclass
class ContingencyResult:
    party: str
    kind: str  # "intrinsic" | "contingent" | "partial" | "reducible"
    in_core_constrained: bool
    in_core_bypass: bool
    phi_constrained: float
    phi_bypass: float
    margin: float
    core_constrained: tuple
    core_bypass: tuple

    def line(self):
        return ("%-10s margin=%.3f  %s in core: constrained=%s bypass=%s  (Phi %.3f -> %.3f)"
                % (self.kind, self.margin, self.party,
                   self.in_core_constrained, self.in_core_bypass,
                   self.phi_constrained, self.phi_bypass))


def add_bypass(rules, labels, downstream, upstream, mode="replace"):
    """Return a rule set with the forbidden direct edge restored on `downstream`.

    mode="replace": downstream reads upstream INSTEAD of its mediated source — the maker sells
                    direct and the mediator is disintermediated (the franchise-law counterfactual).
    mode="add":     downstream reads upstream IN ADDITION — a parallel back-channel is opened,
                    downstream' = original OR upstream.
    """
    labels = tuple(labels)
    di = labels.index(downstream)
    ui = labels.index(upstream)
    new = list(rules)
    orig = rules[di]
    if mode == "replace":
        new[di] = lambda x, ui=ui: x[ui]
    elif mode == "add":
        new[di] = lambda x, orig=orig, ui=ui: orig(x) | x[ui]
    else:
        raise ValueError("mode must be 'replace' or 'add', got %r" % mode)
    return new


def contingency_test(rules, labels, party, downstream=None, upstream=None,
                     mode="replace", bypass_rules=None):
    """Classify `party`'s irreducibility via the bypass-counterfactual.

    rules / labels : the constrained system, with the bypass edge forbidden.
    party          : the mediator / broker label to classify.
    downstream, upstream, mode : how to restore the forbidden direct edge (see add_bypass).
    bypass_rules   : pass an explicit bypass rule set to override the downstream/upstream form.

    Returns a ContingencyResult. The margin is whole-system Phi_MIP lost when the bypass opens.
    """
    labels = tuple(labels)
    if bypass_rules is None:
        if downstream is None or upstream is None:
            raise ValueError("supply downstream and upstream, or bypass_rules")
        bypass_rules = add_bypass(rules, labels, downstream, upstream, mode)

    vc = verdict(rules, labels)
    cc, _ = major_complex(rules, labels)
    vb = verdict(bypass_rules, labels)
    cb, _ = major_complex(bypass_rules, labels)

    in_c = party in cc
    in_b = party in cb
    margin = vc.max_phi - vb.max_phi

    if not in_c:
        kind = "reducible"
    elif not in_b:
        kind = "contingent"
    elif margin > PHI_EPS:
        kind = "partial"
    else:
        kind = "intrinsic"

    return ContingencyResult(party, kind, in_c, in_b,
                             float(vc.max_phi), float(vb.max_phi), float(margin),
                             tuple(cc), tuple(cb))
