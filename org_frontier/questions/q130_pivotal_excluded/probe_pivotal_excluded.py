"""Probe 285 (Q130) — pivotal but excluded: necessity without core membership.

Question: two notions of a party's importance have come apart in earlier work. A party is in the core when
it is a member of the major complex, the maximal-Φ subsystem. A party is pivotal when removing it collapses
the form's irreducibility. Q125's majority clique showed they differ — its core is {B, D}, yet knocking out
A or C, both outside the core, still drops the whole-system Φ to zero — and Q129's displacement showed a
coupled objective pushing a pivotal party out of the core. Q130 characterizes the gap: when is a party
necessary to the coordination's irreducibility yet absent from its major complex?

A party P is *in the core* when P is in the major complex. P is *pivotal* when knocking it out (the spectator
construct P' = x[P]) flips the whole-system verdict from triadic to dyadic. A *pivotal-but-excluded* party is
pivotal and not in the core.

Hypotheses (fixed before computing):
  H1. Pivotal-but-excluded parties exist: in some irreducible forms a party is pivotal yet outside the major
      complex. Necessity and membership are distinct.
  H2. A pivotal-but-excluded party is one the core depends on — some core member's rule reads it — so
      removing it changes the core and collapses the form, while its own cause-effect role keeps it out of
      the maximal-Φ subset. Equivalently, the gap tracks core size: when the major complex is a strict
      subset of an all-pivotal form, the excluded parties are pivotal-but-excluded.

Null: pivotality and core membership coincide — every pivotal party is in the core and conversely.

Method: over the homogeneous symmetric four-party forms (Q125's family, where the majority clique lives) and
a set of curated asymmetric forms, classify each party of each irreducible form by (in core, pivotal) and
record whether the core reads the party. Report the joint distribution and characterize the
pivotal-but-excluded class.

Validation gap: exact Φ on small Boolean models; evidence about the instrument and the construct.

Run:  python -m org_frontier.questions.q130_pivotal_excluded.probe_pivotal_excluded
"""

from collections import Counter

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import cm_from_rules

LABELS = ("A", "B", "C", "D")


def is_irreducible(rules):
    return verdict(rules, LABELS).structure == "triadic"


def pivotal(rules, p):
    """Knockout via the spectator construct P' = x[P]; pivotal iff the form turns dyadic."""
    r = list(rules)
    r[p] = lambda x, p=p: x[p]
    return verdict(r, LABELS).structure == "dyadic"


def classify_parties(rules):
    """For each party: (in_core, pivotal, core_reads_it)."""
    core, _phi = major_complex(rules, LABELS)
    core = set(core or ())
    cm = cm_from_rules(rules)                 # cm[i, j] = 1 iff node j's rule depends on node i
    core_idx = {i for i, lab in enumerate(LABELS) if lab in core}
    out = []
    for p in range(4):
        in_core = LABELS[p] in core
        piv = pivotal(rules, p)
        core_reads_p = any(cm[p, j] for j in core_idx)   # some core member reads p
        out.append((LABELS[p], in_core, piv, core_reads_p))
    return core, out


# ----- families (homogeneous symmetric reused from Q125) ---------------------------------------------

def symmetric_functions():
    return [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]


def _node_rule(self_idx, table):
    others = [j for j in range(4) if j != self_idx]
    return lambda x, others=others, table=table: table[x[others[0]] + x[others[1]] + x[others[2]]]


def homogeneous_symmetric_family():
    for m, table in enumerate(symmetric_functions()):
        yield f"sym{m}", [_node_rule(i, table) for i in range(4)]


def curated_asymmetric_forms():
    """Forms where a party feeds the core without symmetry — to separate the asymmetric route from the
    symmetry-degeneracy route."""
    AND3 = (0, 0, 0, 1)
    forms = {
        # A scaffolds a B,C,D core: B,C,D form a majority among themselves and also read A; A reads no one.
        "scaffold_input": [
            lambda x: x[0],                                      # A' = A (fixed input)
            lambda x: 1 if (x[0] + x[2] + x[3]) >= 2 else 0,     # B' = MAJ(A,C,D)
            lambda x: 1 if (x[0] + x[1] + x[3]) >= 2 else 0,     # C' = MAJ(A,B,D)
            lambda x: 1 if (x[0] + x[1] + x[2]) >= 2 else 0,     # D' = MAJ(A,B,C)
        ],
        # AND-clique with one party that only emits (read by all, reads none).
        "emit_only_member": [
            lambda x: x[0],                                      # A' = A
            lambda x: x[0] & x[2] & x[3],                        # B' = A&C&D
            lambda x: x[0] & x[1] & x[3],                        # C' = A&B&D
            lambda x: x[0] & x[1] & x[2],                        # D' = A&B&C
        ],
    }
    for k, r in forms.items():
        yield k, r


def sweep(name, family):
    n_irr = 0
    cells = Counter()              # (in_core, pivotal) -> count
    pe_core_reads = Counter()      # for pivotal-but-excluded: does the core read it?
    core_sizes = Counter()
    examples = []
    for label, rules in family:
        if not is_irreducible(rules):
            continue
        n_irr += 1
        core, parties = classify_parties(rules)
        core_sizes[len(core)] += 1
        n_pe = 0
        for lab, in_core, piv, core_reads in parties:
            cells[(in_core, piv)] += 1
            if piv and not in_core:
                n_pe += 1
                pe_core_reads[core_reads] += 1
        if n_pe and len(examples) < 6:
            examples.append((label, "".join(sorted(core)), n_pe))
    print(f"\n[{name}]  {n_irr} irreducible forms")
    print(f"  party classes (in_core, pivotal): "
          + ", ".join(f"{k}={cells[k]}" for k in [(True, True), (True, False), (False, True), (False, False)]))
    print(f"  core sizes: " + ", ".join(f"{s}:{core_sizes[s]}" for s in sorted(core_sizes)))
    pe_total = cells[(False, True)]
    print(f"  pivotal-but-excluded parties: {pe_total}  "
          f"(core reads them: {pe_core_reads[True]}; core does not: {pe_core_reads[False]})")
    for label, core, n in examples:
        print(f"    {label}: core={{{core}}}, {n} pivotal-but-excluded")
    return cells, pe_core_reads


def main():
    print("PROBE 285 (Q130) — pivotal but excluded: necessity without core membership")
    print("=" * 80)

    # Control: the canonical 3-party triad — every party both in core and pivotal.
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    core3, _ = major_complex(triad, ("W", "S", "C"))
    v3 = verdict(triad, ("W", "S", "C"))
    ctrl = v3.structure == "triadic" and set(core3) == {"W", "S", "C"}
    print(f"  CONTROL 3-party triad: {v3.structure}, core={core3} (all in core)  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    c1, pe1 = sweep("homogeneous symmetric (Q125 family)", homogeneous_symmetric_family())
    c2, pe2 = sweep("curated asymmetric (scaffold / emit-only)", curated_asymmetric_forms())

    pe_total = c1[(False, True)] + c2[(False, True)]
    core_not_pivotal = c1[(True, False)] + c2[(True, False)]
    pe_core_reads_T = pe1[True] + pe2[True]
    pe_core_reads_F = pe1[False] + pe2[False]

    print("\n" + "=" * 80)
    h1 = pe_total > 0
    h2 = pe_total > 0 and pe_core_reads_F == 0      # every pivotal-but-excluded party is read by the core
    print(f"  H1 (pivotal-but-excluded parties exist): {'SUPPORTED' if h1 else 'NOT SUPPORTED'} "
          f"({pe_total} found)")
    print(f"  H2 (the core reads every pivotal-but-excluded party): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'} "
          f"(core reads {pe_core_reads_T}, does not {pe_core_reads_F})")
    print(f"  core-but-not-pivotal parties: {core_not_pivotal}")
    print("  Reading: necessity and membership are distinct. A party can be required for the coordination's")
    print("  irreducibility — its removal collapses the form — while sitting outside the maximal-Φ core,")
    print("  because the core depends on it as an input without it being part of the integrated whole.")
    print("=" * 80)


if __name__ == "__main__":
    main()
