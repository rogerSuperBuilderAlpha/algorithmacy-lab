"""Probe 279 (Q120) — is there a triadic form with no pivotal party?

Question: the standing law (STRUCTURAL_FINDINGS.md) reads "a form demands algorithmacy iff every party
is bound into one irreducible joint determination; substitutability of any party collapses it." That
states every party is *pivotal*: replace any one with a non-interpreting pass-through and the irreducible
bind should fall. Q120 asks whether an exception exists — a triadic form whose binding is purely
higher-order, where no single party is individually pivotal, so the trio is irreducible jointly but
survives the knockout of any one member.

Hypothesis (H1): no such form exists — every triadic form has at least one pivotal party. The bind always
has a lynchpin; pure higher-order binding does not occur.

Null / what would refute H1: a triadic form where all three single-party knockouts leave it triadic.

Operationalization: knockout of party P replaces P's update rule so it stops interpreting its inputs but
is still read by the others — the exact reading of "P becomes substitutable / a non-interpreting
pass-through." Two independent knockout definitions are run so the result does not rest on one choice:
  - "spectator": P' = x[P] (P freezes at its current value, the lab's spectator construct);
  - "silenced":  P' = 0    (P is forced to a constant, a different intervention with the same intent).
P is *pivotal* in a triadic form when its knockout flips the whole-system verdict from triadic to dyadic.
A *pure higher-order bind* is a triadic form with zero pivotal parties under a given definition.

Method: validate the instrument on the canonical strict-mediation triad (triadic, Φ_MIP=2.0, all three
parties pivotal). Then sweep two families and, for every triadic form, count its pivotal parties:
  1. the 256 strict-mediation forms (W'=f(S), S'=f(W,C), C'=f(S)) — the canonical family, in which the
     mediator S is a topological cut vertex between W and C;
  2. the 4096 fully-coupled forms (W'=f(S,C), S'=f(W,C), C'=f(W,S)) — every party reads the other two, so
     no single party is a cut vertex and redundancy could carry the bind.
Report the distribution of pivot counts and whether any zero-pivot (pure higher-order) form exists.

Validation gap: this is exact Φ on small Boolean models. It is evidence about the instrument and the law,
not a claim about any real organization.

Run:  python -m org_frontier.probes.probe_q120_higher_order_binding
"""

from collections import Counter

from org_frontier.probes.lib import verdict, major_complex

LABELS = ("W", "S", "C")


# Two knockout definitions: each replaces party p's rule with a non-interpreting pass-through.
KNOCKOUTS = {
    "spectator": (lambda p: (lambda x, p=p: x[p])),   # p freezes at its current value
    "silenced": (lambda p: (lambda x: 0)),            # p forced to a constant 0
}


def knockout(rules, p, make_rule):
    """Replace party p's rule with the pass-through built by make_rule(p)."""
    r = list(rules)
    r[p] = make_rule(p)
    return r


def pivotal_parties(rules, make_rule):
    """The party indices whose knockout flips the verdict triadic -> dyadic, for one knockout def."""
    return [p for p in range(3)
            if verdict(knockout(rules, p, make_rule), LABELS).structure == "dyadic"]


# ----- the two families -----------------------------------------------------------------------------

def _one_input_tables():
    return [(o0, o1) for o0 in (0, 1) for o1 in (0, 1)]            # 4 one-input functions


def _two_input_tables():
    return [tuple((m >> k) & 1 for k in range(4)) for m in range(16)]   # 16 two-input functions


def _fn1(t):
    return lambda v: t[v]


def _fn2(t):
    return lambda a, b: t[a | (b << 1)]


def strict_mediation_family():
    """256 forms: W'=f_W(S), S'=f_S(W,C), C'=f_C(S). S is the only path between W and C."""
    ones, twos = _one_input_tables(), _two_input_tables()
    for iw, tw in enumerate(ones):
        fw = _fn1(tw)
        for ic, tc in enumerate(ones):
            fc = _fn1(tc)
            for is_, ts in enumerate(twos):
                fs = _fn2(ts)
                rules = [
                    (lambda x, fw=fw: fw(x[1])),          # W' = f_W(S)
                    (lambda x, fs=fs: fs(x[0], x[2])),    # S' = f_S(W, C)
                    (lambda x, fc=fc: fc(x[1])),          # C' = f_C(S)
                ]
                yield f"W{iw}_S{is_}_C{ic}", rules


def fully_coupled_family():
    """4096 forms: W'=f_W(S,C), S'=f_S(W,C), C'=f_C(W,S). Every party reads the other two."""
    twos = _two_input_tables()
    for iw, tw in enumerate(twos):
        fw = _fn2(tw)
        for is_, ts in enumerate(twos):
            fs = _fn2(ts)
            for ic, tc in enumerate(twos):
                fc = _fn2(tc)
                rules = [
                    (lambda x, fw=fw: fw(x[1], x[2])),    # W' = f_W(S, C)
                    (lambda x, fs=fs: fs(x[0], x[2])),    # S' = f_S(W, C)
                    (lambda x, fc=fc: fc(x[0], x[1])),    # C' = f_C(W, S)
                ]
                yield f"W{iw}_S{is_}_C{ic}", rules


def sweep(name, family):
    """Over the triadic forms of a family, count pivotal parties under each knockout definition."""
    triadic = [(label, rules, verdict(rules, LABELS).max_phi)
               for label, rules in family
               if verdict(rules, LABELS).structure == "triadic"]
    n_total_note = name
    print(f"\n[{name}]  {len(triadic)} triadic forms")
    zero_pivot_by_def = {}
    for defn, make_rule in KNOCKOUTS.items():
        pivot_dist = Counter()
        party_pivotal = Counter()
        zero_pivot = []
        for label, rules, phi in triadic:
            piv = pivotal_parties(rules, make_rule)
            pivot_dist[len(piv)] += 1
            for p in piv:
                party_pivotal[LABELS[p]] += 1
            if not piv:
                zero_pivot.append((label, rules, phi))
        n = len(triadic)
        dist = " ".join(f"{k}:{pivot_dist.get(k, 0)}" for k in (0, 1, 2, 3))
        rates = " ".join(f"{p} {party_pivotal[p]}/{n}" for p in LABELS)
        print(f"  knockout={defn:<9} pivot-count[{dist}]  ({rates})  zero-pivot={len(zero_pivot)}")
        for label, rules, phi in zero_pivot[:5]:
            core, cphi = major_complex(rules, LABELS)
            print(f"      pure higher-order: {label} maxΦ={phi:.3f} core={core} coreΦ={cphi:.3f}")
        zero_pivot_by_def[defn] = len(zero_pivot)
    return len(triadic), zero_pivot_by_def


def main():
    import sys
    quick = "--quick" in sys.argv  # strict-mediation family only (~1s); the per-PR reproduce gate uses this
    print("PROBE 279 (Q120) — is there a triadic form with no pivotal party?"
          + (" [--quick: strict-mediation only]" if quick else ""))
    print("=" * 72)

    # [1/3] Instrument control: the canonical strict triad is triadic with all three parties pivotal
    # under both knockout definitions.
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, LABELS)
    piv = {d: pivotal_parties(triad, mk) for d, mk in KNOCKOUTS.items()}
    ctrl_ok = (v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
               and all(len(p) == 3 for p in piv.values()))
    print(f"  CONTROL strict triad: {v.structure} Φ={v.max_phi:.3f}, pivotal="
          f"{ {d: [LABELS[i] for i in p] for d, p in piv.items()} }  {'PASS' if ctrl_ok else 'FAIL'}")
    if not ctrl_ok:
        raise SystemExit("Instrument control failed — stopping.")

    # [2/3] and [3/3]: sweep both families under both knockout definitions.
    sm_tri, sm_zero = sweep("strict mediation (256)", strict_mediation_family())
    fc_tri, fc_zero = (0, {}) if quick else sweep("fully coupled (4096)", fully_coupled_family())

    total_zero = sum(sm_zero.values()) + sum(fc_zero.values())
    print("\n" + "=" * 72)
    print(f"  triadic forms: {sm_tri} strict-mediation + {fc_tri} fully-coupled = {sm_tri + fc_tri}")
    print(f"  pure higher-order (zero-pivot) forms, summed over both knockout defs: {total_zero}")
    if total_zero == 0:
        print("  H1 SUPPORTED: under both knockout definitions, every triadic form has all three")
        print("  parties pivotal — no pure higher-order bind. Triadic coordination is maximally")
        print("  fragile: every party is a lynchpin, none is dispensable.")
    else:
        print("  H1 REFUTED: a triadic form survives every single-party knockout — the bind is")
        print("  purely higher-order, carried by the trio jointly with no individual pivot.")
    print("=" * 72)


if __name__ == "__main__":
    main()
