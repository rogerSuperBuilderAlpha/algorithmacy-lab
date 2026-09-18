"""Structural signatures of the catalog templates, for matching Boolean forms.

A form "matches" a template when its connectivity and determination algebra fall under that
template's signature. Additive shares the conjunctive determination and differs by a back-channel
(or by bypass mode in the contingency test); free and relay are included for completeness even
though they do not appear among the 24 triadic strict-mediation forms.
"""

from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.corpus.forms_library import structural_tags

# 2-input truth tables as 4-tuples (f(0,0), f(1,0), f(0,1), f(1,1)) — little-endian a|(b<<1).
PARITY_TABLES = {(0, 1, 1, 0), (1, 0, 0, 1)}  # XOR, XNOR


def is_affine_2(table):
    """A 2-input Boolean function is affine over GF(2) iff f(1,1) = f(0,0) ⊕ f(1,0) ⊕ f(0,1)."""
    t00, t10, t01, t11 = table
    return t11 == (t00 ^ t10 ^ t01)


def depends_on_both(table):
    t00, t10, t01, t11 = table
    reads_a = (t00 != t10) or (t01 != t11)
    reads_b = (t00 != t01) or (t10 != t11)
    return reads_a and reads_b


def commit_table(rules, mediator_index=1):
    """Recover the mediator's 4-entry table under the strict-mediation convention S'=f(W,C)."""
    return tuple(int(rules[mediator_index]([w, 0, c])) for c in (0, 1) for w in (0, 1))


def arity_profile(rules):
    """Per-node input arity from the connectivity matrix (column sum)."""
    cm = cm_from_rules(rules)
    return tuple(int(cm[:, j].sum()) for j in range(cm.shape[1]))


def is_relay(rules):
    """Unary 3-cycle: each node depends on exactly one other (catalog relay signature)."""
    cm = cm_from_rules(rules)
    n = cm.shape[0]
    if n != 3:
        return False
    if any(int(cm[:, j].sum()) != 1 for j in range(n)):
        return False
    # cm[i,j]=1 iff j depends on i; unique predecessor of j is the unique i with cm[i,j]=1
    pred = [int(cm[:, j].argmax()) for j in range(n)]
    seen, cur = [], 0
    for _ in range(n):
        seen.append(cur)
        cur = pred[cur]
    return len(set(seen)) == n and cur == 0


def is_free(rules):
    """Sink already sources upstream; mediator is a dead-end copy (catalog free signature).

    Operationalised for n=3 labelled (source, mediator, sink) = (0, 1, 2): sink depends on source
    and does not depend on mediator; mediator depends on source only.
    """
    cm = cm_from_rules(rules)
    if cm.shape[0] != 3:
        return False
    sink_deps = [i for i in range(3) if cm[i, 2] == 1]
    med_deps = [i for i in range(3) if cm[i, 1] == 1]
    return (0 in sink_deps) and (1 not in sink_deps) and (med_deps == [0])


def is_conjunctive_family(rules):
    """Strict mediation, non-parity joint mediator, parties meet only through it."""
    tags = structural_tags(rules)
    if not tags["strict_mediation"] or not tags["mediator_reads_both"]:
        return False
    table = commit_table(rules)
    if table in PARITY_TABLES:
        return False
    return depends_on_both(table)


def is_parity_family(rules):
    """Strict mediation with an XOR/XNOR mediator — the candidate fifth template."""
    tags = structural_tags(rules)
    if not tags["strict_mediation"] or not tags["mediator_reads_both"]:
        return False
    return commit_table(rules) in PARITY_TABLES


def is_additive_family(rules):
    """Conjunctive determination with a back-channel already present."""
    tags = structural_tags(rules)
    if not tags["back_channel"] or not tags["mediator_reads_both"]:
        return False
    # mediator table under a possibly non-strict wiring: evaluate at S=0
    table = commit_table(rules)
    return depends_on_both(table) and table not in PARITY_TABLES


def match_templates(rules):
    """Return the set of template names whose signature the form matches."""
    hits = set()
    if is_relay(rules):
        hits.add("relay")
    if is_conjunctive_family(rules):
        hits.add("conjunctive")
    if is_additive_family(rules):
        hits.add("additive")
    if is_free(rules):
        hits.add("free")
    if is_parity_family(rules):
        hits.add("parity")
    return hits


FOUR = frozenset({"relay", "conjunctive", "additive", "free"})
