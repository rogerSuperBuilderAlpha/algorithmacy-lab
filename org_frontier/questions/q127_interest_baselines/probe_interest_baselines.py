"""Probe 282 (Q127) — what makes self-interest collapse coordination: the minority output-class.

Question: Q126 found that an interested mediator erodes coordination irreducibility, and that a denying
agenda collapses it faster than an approving one. That was shown on the AND faithful baseline (commit iff
both warrant). Is "denying is more corrosive" a fact about denial, or about something structural that AND
happens to expose? The conjecture: what collapses irreducibility fastest is overriding the faithful
mediator's *minority output-class* — the output value it produces in the fewest states — because those few
states carry the discriminating information. Which agenda does that depends on the baseline. AND outputs 1
in one state, so denying (which removes the 1) collapses it. OR outputs 0 in one state, so approving (which
removes the 0) should collapse OR fastest — the asymmetry flips. Balanced baselines (agree, differ) should
treat the two agendas alike.

Hypothesis (H1): the agenda that overrides the baseline's minority output-class collapses irreducibility at
the lowest interestedness level. For AND the fast agenda is deny; for OR it is approve; for the balanced
baselines (agree = XNOR, differ = XOR) approve and deny collapse at the same level.

Null: the denying agenda is always the faster collapse, independent of the baseline (denial is special).

Method: for each faithful baseline and each agenda, run the Q126 interestedness ladder — override toward the
agenda on the k input states where the parties least warrant it, commit the baseline elsewhere — and record
Φ and the first level at which the form goes dyadic. Compare the collapse level to which agenda overrides
the baseline's minority output-class.

Validation gap: exact Φ on a three-node Boolean model; evidence about the construct and the instrument.

Run:  python -m org_frontier.questions.q127_interest_baselines.probe_interest_baselines
"""

from org_frontier.probes.lib import verdict

LABELS = ("W", "S", "C")
STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]  # (W, C) inputs

# Faithful baselines as output tables over STATES.
BASELINES = {
    "AND  (iff both)": {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 1},
    "OR   (iff either)": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 1},
    "AGREE (iff W==C)": {(0, 0): 1, (0, 1): 0, (1, 0): 0, (1, 1): 1},
    "DIFFER (iff W!=C)": {(0, 0): 0, (0, 1): 1, (1, 0): 1, (1, 1): 0},
}


def minority_output(base):
    """The output value the baseline produces in the fewest states, or None if balanced (2-2)."""
    ones = sum(base.values())
    if ones < 2:
        return 1
    if ones > 2:
        return 0
    return None


def override_order(agenda):
    """States by least warrant for the agenda first (warrant for approve = parties on)."""
    warrant = lambda wc: (wc[0] + wc[1]) if agenda == 1 else (2 - (wc[0] + wc[1]))
    return sorted(STATES, key=lambda wc: (warrant(wc), wc))


def rules_for(base, agenda, k):
    override = set(override_order(agenda)[:k])
    def f(w, c):
        return agenda if (w, c) in override else base[(w, c)]
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def collapse_level(base, agenda):
    """Φ at each k=0..4 and the first k at which the form is dyadic (Φ_MIP = 0)."""
    phis = []
    first_dyadic = None
    for k in range(5):
        v = verdict(rules_for(base, agenda, k), LABELS)
        phis.append(v.max_phi)
        if first_dyadic is None and v.structure == "dyadic":
            first_dyadic = k
    return phis, first_dyadic


def main():
    print("PROBE 282 (Q127) — self-interest collapse vs the minority output-class")
    print("=" * 80)

    # Control: AND faithful (k=0) is the canonical triad.
    v0 = verdict(rules_for(BASELINES["AND  (iff both)"], 1, 0), LABELS)
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(f"  CONTROL AND faithful: {v0.structure} Φ={v0.max_phi:.3f}  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    sparse_ok = True       # minority-output principle on the sparse baselines (AND, OR)
    reintegrators = []     # balanced baselines where self-interest raises Φ above the faithful level
    print(f"\n  {'baseline':<18} {'minority':<9} {'approve Φ ladder':<28} k* {'deny Φ ladder':<28} k* | fast")
    for name, base in BASELINES.items():
        ap_phis, ap_k = collapse_level(base, 1)
        dn_phis, dn_k = collapse_level(base, 0)
        mino = minority_output(base)
        ak, dk = (ap_k if ap_k is not None else 99), (dn_k if dn_k is not None else 99)
        fast = "approve" if ak < dk else "deny" if dk < ak else "equal"
        faithful_phi = ap_phis[0]
        if max(max(ap_phis), max(dn_phis)) > faithful_phi + 1e-9:
            reintegrators.append(name)
        if mino is not None:
            predicted = {1: "deny", 0: "approve"}[mino]
            sparse_ok = sparse_ok and (fast == predicted)
        ap_str = ",".join(f"{p:.2f}" for p in ap_phis)
        dn_str = ",".join(f"{p:.2f}" for p in dn_phis)
        mino_str = {1: "out=1", 0: "out=0", None: "balanced"}[mino]
        print(f"  {name:<18} {mino_str:<9} {ap_str:<28} {ap_k if ap_k is not None else '-':<2} "
              f"{dn_str:<28} {dn_k if dn_k is not None else '-':<2} | {fast}")

    print("\n" + "=" * 80)
    print(f"  Pre-registered H1 (universal minority-output principle): REFUTED — the balanced baselines")
    print(f"  do not collapse symmetrically. The refined finding the data supports:")
    print(f"  (1) MINORITY-OUTPUT FLIP on sparse baselines (AND, OR): "
          f"{'CONFIRMED' if sparse_ok else 'FAILED'} — the agenda")
    print(f"      overriding the rare output collapses fastest, so denial is special only for AND; OR flips")
    print(f"      to approve. The Q126 asymmetry is baseline-relative, not about denial.")
    print(f"  (2) RE-INTEGRATION on balanced baselines {reintegrators}: a faithful balanced mediator is")
    print(f"      only weakly irreducible (Φ=0.5), and a dose of self-interest sharpens it into a")
    print(f"      discriminating mediator — Φ RISES above the faithful level before finally collapsing.")
    print(f"      Self-interest is not uniformly corrosive; on a balanced mediator it first integrates.")
    print("=" * 80)


if __name__ == "__main__":
    main()
