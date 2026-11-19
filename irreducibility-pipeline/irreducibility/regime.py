"""The mediator's position in the irreducible core.

Once a structure reads triadic, the next strategic question is what the mediating system (the
platform, the engine, the manager) is doing in it. The lesion test and the major complex answer it:

    dyadic      the structure factors; there is no irreducible core to hold a position in
    BYPASSED    triadic, but the mediator is outside the core: the parties out-integrate it
    CAPTURE     the mediator is in the core, but the core excludes some party: the mediator and
                part of the arrangement bind each other and leave the rest outside
    BOTTLENECK  every party is in the core, and freezing the mediator stops the others from
                coordinating: the structure runs through it
    ENRICHER    every party is in the core, and the others still coordinate with the mediator
                frozen: it adds to a coordination that would exist without it

The same mediator can hold each position depending on the parties' other ties and options.
Whether a platform is a bottleneck is a property of the whole arrangement, not of the platform.

Provenance: generalised from the lab's mediator-in-core and enricher-regime threads; on
three-party forms it reproduces their five-way classification exactly.
"""

from .core import classify_rules, major_complex

REGIMES = ("dyadic", "BYPASSED", "CAPTURE", "BOTTLENECK", "ENRICHER")


def lesion_survives(rules, labels, mi):
    """Do the non-mediator parties still coordinate (triadic) with the mediator frozen at 0 or 1?"""
    rest = [i for i in range(len(labels)) if i != mi]
    if len(rest) < 2:
        return False
    for c in (0, 1):
        reduced = [(lambda y, _j=j, _c=c: rules[_j](
                     tuple(_c if k == mi else y[rest.index(k)] for k in range(len(labels)))))
                   for j in rest]
        if classify_rules(reduced, tuple(labels[i] for i in rest)).structure == "triadic":
            return True
    return False


def regime(rules, labels, mediator):
    """Five-way regime of the party named ``mediator`` (a label) or at index ``mediator``."""
    labels = tuple(labels)
    mi = labels.index(mediator) if isinstance(mediator, str) else int(mediator)
    v = classify_rules(rules, labels)
    if v.structure == "dyadic":
        return "dyadic"
    core, _ = major_complex(list(rules), labels)
    core = set(core or ())
    if labels[mi] not in core:
        return "BYPASSED"
    if core != set(labels):
        return "CAPTURE"
    return "ENRICHER" if lesion_survives(rules, labels, mi) else "BOTTLENECK"
