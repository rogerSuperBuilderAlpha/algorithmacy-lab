"""Probe 280 (Q125) — does a pure higher-order bind exist at four parties?

Question: Q120 showed that among three parties no pure higher-order bind exists — every irreducible form
has all three parties pivotal, so removing any one collapses it. The reason a fourth party could change
this is redundancy: with four parties, two can jointly stand in for a third, so a form might stay
irreducible after the knockout of any single party, with the binding carried by the group and no
individual lynchpin. Q125 tests whether that pure higher-order bind appears at four parties.

Hypothesis (H1): a pure higher-order bind exists at four parties — an irreducible form whose verdict
survives the knockout of every single party. The Q120 result is three-party-specific, broken by
four-party redundancy.

Null (refutes H1): no four-party form tested is a pure higher-order bind; every irreducible form has at
least one pivotal party, extending the Q120 result.

Operationalization (same as Q120): a four-party form is *irreducible* when its whole-system Φ over the MIP
exceeds PHI_EPS in some reachable state (the classifier's "triadic"). Knockout of party P replaces its rule
with a non-interpreting pass-through — "spectator" (P' = x[P]) or "silenced" (P' = 0). P is *pivotal* when
its knockout makes the form reducible. A *pure higher-order bind* is an irreducible form with zero pivotal
parties.

Where redundancy lives: the search targets the symmetric four-party forms, where interchangeability is
greatest and a no-pivot bind is most likely. A non-symmetric rule breaks interchangeability, which makes a
no-pivot bind less likely, so the symmetric forms are the right place to look for one.
  1. homogeneous symmetric forms — every node reads the other three through the same symmetric function
     (output depends only on how many of the three inputs are on): 16 forms, exhaustive, the maximally
     redundant family;
  2. canonical heterogeneous forms — each node independently uses one of four canonical symmetric functions
     (OR, majority, AND, parity of its three neighbours): 4^4 = 256 forms, exhaustive over that basis;
  3. curated redundant constructions — hand-built forms with explicit interchangeability (twin parties,
     rings, cliques) where a no-pivot bind would most plausibly arise;
  4. the lab's named multiparty four-party forms, as a cross-check on real constructions.
Exact Φ on four nodes is ~1s per form, so the full 16^4 = 65536 heterogeneous family is not swept; the
canonical basis and curated set stand in for it. The claim is bounded to the forms tested.

Validation gap: exact Φ on small Boolean models; evidence about the instrument and the law, not a claim
about a real organization.

Run:  python -m org_frontier.questions.q125_four_party_higher_order.probe_four_party_higher_order
      python -m org_frontier.questions.q125_four_party_higher_order.probe_four_party_higher_order --quick   # families 1 and 3 only (~min)
"""

from collections import Counter
from itertools import product

from org_frontier.probes.lib import verdict, major_complex

LABELS4 = ("A", "B", "C", "D")

KNOCKOUTS = {
    "spectator": (lambda p: (lambda x, p=p: x[p])),   # p freezes at its current value
    "silenced": (lambda p: (lambda x: 0)),            # p forced to constant 0
}


def is_irreducible(rules, labels):
    return verdict(rules, labels).structure == "triadic"


def pivotal_parties(rules, labels, make_rule):
    """Indices whose knockout makes the form reducible, for one knockout definition."""
    out = []
    for p in range(len(rules)):
        r = list(rules)
        r[p] = make_rule(p)
        if not is_irreducible(r, labels):
            out.append(p)
    return out


# ----- symmetric four-party families ----------------------------------------------------------------

def symmetric_functions():
    """The 16 symmetric Boolean functions of 3 inputs: output depends only on the count of 1s (0..3).
    Each is a 4-bit table indexed by that count."""
    return [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]


def _node_rule(self_idx, table):
    """node' = table[count of 1s among the other three nodes]."""
    others = [j for j in range(4) if j != self_idx]
    return lambda x, others=others, table=table: table[x[others[0]] + x[others[1]] + x[others[2]]]


def homogeneous_symmetric_family():
    """16 forms: every node reads the other three through the same symmetric function."""
    for m, table in enumerate(symmetric_functions()):
        rules = [_node_rule(i, table) for i in range(4)]
        yield f"sym{m}", rules


# Four canonical symmetric functions of three inputs, as (count 0,1,2,3) output tables.
CANONICAL = {
    "OR": (0, 1, 1, 1),     # at least one
    "MAJ": (0, 0, 1, 1),    # at least two
    "AND": (0, 0, 0, 1),    # all three
    "PAR": (0, 1, 0, 1),    # odd count (parity)
}


def canonical_heterogeneous_family():
    """256 forms: each node independently uses one of the four canonical symmetric functions."""
    keys = list(CANONICAL)
    for combo in product(keys, repeat=4):
        rules = [_node_rule(i, CANONICAL[combo[i]]) for i in range(4)]
        yield "/".join(combo), rules


def curated_redundant_forms():
    """Hand-built four-party forms with explicit interchangeability — the most plausible no-pivot binds."""
    AND, OR, MAJ = CANONICAL["AND"], CANONICAL["OR"], CANONICAL["MAJ"]
    forms = {
        # twin counterparts C,D feed mediator S together; worker A reads S; S reads all three.
        "twin_counterparts_or": [lambda x: x[1], lambda x: x[0] & (x[2] | x[3]),
                                 lambda x: x[1], lambda x: x[1]],
        "twin_counterparts_and": [lambda x: x[1], lambda x: x[0] & x[2] & x[3],
                                  lambda x: x[1], lambda x: x[1]],
        # twin workers A,B feed mediator C; counterpart D reads C.
        "twin_workers_or": [lambda x: x[2], lambda x: x[2], lambda x: (x[0] | x[1]) & x[3],
                            lambda x: x[2]],
        # 4-ring: each reads its left neighbour (rotational).
        "ring_copy": [lambda x: x[3], lambda x: x[0], lambda x: x[1], lambda x: x[2]],
        "ring_and": [lambda x: x[3] & x[1], lambda x: x[0] & x[2], lambda x: x[1] & x[3],
                     lambda x: x[2] & x[0]],
        # mutual-majority clique (already known irreducible); included for completeness.
        "maj_clique": [_node_rule(i, MAJ) for i in range(4)],
        "and_clique": [_node_rule(i, AND) for i in range(4)],
        "or_clique": [_node_rule(i, OR) for i in range(4)],
    }
    for k, rules in forms.items():
        yield k, rules


def named_multiparty_forms():
    """The lab's named four-party forms (multiparty.FORMS), as a cross-check on real constructions."""
    try:
        from org_frontier.multiparty.forms import FORMS
    except Exception:
        return
    for f in FORMS:
        if len(f.rules) == 4:
            yield f.key, f.rules


def sweep(name, family, limit_report=5):
    """Over the irreducible forms of a family, find any with zero pivotal parties under either def."""
    n_total = n_irr = 0
    zero_pivot = {d: [] for d in KNOCKOUTS}
    pivot_hist = {d: Counter() for d in KNOCKOUTS}
    for label, rules in family:
        n_total += 1
        if not is_irreducible(rules, LABELS4):
            continue
        n_irr += 1
        for defn, make_rule in KNOCKOUTS.items():
            piv = pivotal_parties(rules, LABELS4, make_rule)
            pivot_hist[defn][len(piv)] += 1
            if not piv:
                zero_pivot[defn].append((label, rules))
    print(f"\n[{name}]  {n_total} forms, {n_irr} irreducible")
    for defn in KNOCKOUTS:
        dist = " ".join(f"{k}:{pivot_hist[defn].get(k, 0)}" for k in range(5))
        print(f"  knockout={defn:<9} pivot-count[{dist}]  zero-pivot={len(zero_pivot[defn])}")
    # A pure higher-order bind must hold under BOTH definitions.
    both = [lz for lz in zero_pivot["spectator"]
            if lz[0] in {z[0] for z in zero_pivot["silenced"]}]
    print(f"  PURE HIGHER-ORDER (zero-pivot under both defs): {len(both)}")
    for label, rules in both[:limit_report]:
        core, phi = major_complex(rules, LABELS4)
        print(f"    {label}: irreducible Φ core={core} coreΦ={phi:.3f}")
    return n_irr, both


def main():
    import sys
    quick = "--quick" in sys.argv
    print("PROBE 280 (Q125) — does a pure higher-order bind exist at four parties?"
          + (" [--quick]" if quick else ""))
    print("=" * 76)

    # Control: the canonical three-party triad is irreducible with all three parties pivotal (Q120).
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, ("W", "S", "C"))
    piv3 = pivotal_parties(triad, ("W", "S", "C"), KNOCKOUTS["spectator"])
    ctrl = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6 and len(piv3) == 3
    print(f"  CONTROL 3-party triad: {v.structure} Φ={v.max_phi:.3f}, pivotal={len(piv3)}/3  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    found = []
    found += sweep("homogeneous symmetric (16)", homogeneous_symmetric_family())[1]
    found += sweep("curated redundant constructions", curated_redundant_forms())[1]
    found += sweep("named multiparty 4-party", named_multiparty_forms())[1]
    if not quick:
        found += sweep("canonical heterogeneous (256)", canonical_heterogeneous_family())[1]

    print("\n" + "=" * 76)
    print(f"  pure higher-order (zero-pivot under both defs) four-party forms found: {len(found)}")
    if found:
        print("  H1 SUPPORTED: a four-party form survives every single-party knockout — the bind is")
        print("  purely higher-order, carried by the group with no individual pivot. Redundancy at")
        print("  four parties breaks the Q120 three-party result. Example(s):")
        for label, rules in found[:5]:
            core, phi = major_complex(rules, LABELS4)
            print(f"    {label}: core={core} coreΦ={phi:.3f}")
    else:
        print("  H1 REFUTED: no four-party form tested is a pure higher-order bind. Every irreducible")
        print("  form has a pivotal party, extending the Q120 result past three parties: even with")
        print("  four-party redundancy, irreducible coordination keeps an individual lynchpin.")
    print("=" * 76)


if __name__ == "__main__":
    main()
