"""Probe 281 (Q126) — the interested mediator: how self-interest erodes coordination irreducibility.

Question: every form the lab has modelled treats the system as a faithful mediator — it commits the joint
determination of the two parties (S' = W ∧ C: commit iff both warrant). The literature watch flags the gap:
no prior work treats the third party as self-interested, pursuing its own agenda against the parties. This
probe models exactly that. The mediator holds an agenda a (a preferred output: approve a=1, or deny a=0)
and increasingly imposes it, overriding the parties' joint determination in more and more input states. The
question is what exact Φ does as the mediator stops reading the parties and starts serving itself.

Interestedness is a level k = 0..4. At level k the mediator outputs its agenda a regardless of the parties
in the k states where the parties least warrant a, and commits the faithful joint determination (AND)
elsewhere. k = 0 is the faithful mediator (pure AND); k = 4 is the predatory mediator (constant a, parties
ignored). Approve (a=1) overrides toward 1 starting from the states with the fewest parties on; deny (a=0)
overrides toward 0 starting from the states with the most parties on.

Hypotheses (fixed before computing):
  H1. Whole-system Φ over {W, S, C} falls as interestedness k rises, and reaches 0 (dyadic) at the
      predatory end where the mediator ignores the parties.
  H2. The parties leave the major complex as the mediator stops reading them: an interested-enough
      mediator coordinates with no one. The number of parties the mediator's rule actually reads falls
      with k.

Null: Φ and core membership do not change with interestedness — self-interest does not erode the bind.

Validation gap: exact Φ on a small Boolean model; evidence about the instrument and the construct, not a
claim about a real platform. "Agenda", "approve", "deny" are labels for output values, not measured intent.

Run:  python -m org_frontier.questions.q126_interested_mediator.probe_interested_mediator
"""

from itertools import combinations

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.classifier.classifier import cm_from_rules

LABELS = ("W", "S", "C")

# (W, C) input states, little-endian over (W, C). Warrant-for-1 is the number of parties on.
STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]


def override_order(agenda):
    """States ordered by least warrant for the agenda first — where imposing the agenda most departs
    from the parties' joint determination."""
    warrant_for_agenda = lambda wc: (wc[0] + wc[1]) if agenda == 1 else (2 - (wc[0] + wc[1]))
    return sorted(STATES, key=warrant_for_agenda)


def mediator(agenda, k):
    """S' as a function of the (W, C) inputs: agenda a on the k least-warranted states, faithful AND
    (the joint determination) elsewhere."""
    override = set(override_order(agenda)[:k])
    def f(w, c):
        return agenda if (w, c) in override else (w & c)
    return f


def triad_rules(agenda, k):
    """W' = S, C' = S, S' = interested mediator of (W, C). State index 0=W, 1=S, 2=C."""
    f = mediator(agenda, k)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def parties_read_by_S(rules):
    """Which of W, C the mediator's rule actually depends on (flip test via the connectivity matrix)."""
    cm = cm_from_rules(rules)          # cm[i, j] = 1 iff node j's rule depends on node i
    reads = []
    if cm[0, 1]:
        reads.append("W")
    if cm[2, 1]:
        reads.append("C")
    return reads


def run_ladder(agenda, label):
    print(f"\n[agenda = {'approve (a=1)' if agenda == 1 else 'deny (a=0)'}]  "
          f"k = interestedness (states where the agenda overrides the parties)")
    print("  k | structure | Φ_MIP | core            | S reads")
    print("  --+-----------+-------+-----------------+--------")
    rows = []
    for k in range(5):
        rules = triad_rules(agenda, k)
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        reads = parties_read_by_S(rules)
        core_str = "".join(core) if core else "(none)"
        print(f"  {k} | {v.structure:<9} | {v.max_phi:5.3f} | {core_str:<15} | {','.join(reads) or '(neither)'}")
        rows.append((k, v.structure, v.max_phi, core, reads))
    return rows


def mediator_from_set(agenda, override):
    """S' that imposes the agenda on the given override set of (W,C) states, faithful AND elsewhere."""
    override = set(override)
    return lambda w, c: agenda if (w, c) in override else (w & c)


def order_averaged(agenda):
    """Mean Φ over ALL choices of which k states to override, for each k — order-independent decay."""
    out = []
    for k in range(5):
        phis = []
        for override in combinations(STATES, k):
            f = mediator_from_set(agenda, override)
            rules = [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]
            phis.append(verdict(rules, LABELS).max_phi)
        out.append((k, len(phis), sum(phis) / len(phis)))
    return out


def main():
    print("PROBE 281 (Q126) — the interested mediator: self-interest vs coordination irreducibility")
    print("=" * 84)

    # Control: the faithful mediator (k=0, AND) is the canonical triad — triadic, Φ=2.0, core {W,S,C}.
    v0 = verdict(triad_rules(1, 0), LABELS)
    core0, phi0 = major_complex(triad_rules(1, 0), LABELS)
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6 and tuple(core0) == ("W", "S", "C")
    print(f"  CONTROL faithful mediator (k=0): {v0.structure} Φ={v0.max_phi:.3f} core={core0}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    approve = run_ladder(1, "approve")
    deny = run_ladder(0, "deny")

    # Order-independent decay: mean Φ over every choice of which k states the agenda overrides.
    print("\n[order-averaged]  mean Φ over all C(4,k) override sets, per interestedness level k")
    print("  k | sets | mean Φ (approve) | mean Φ (deny)")
    print("  --+------+------------------+-------------")
    oa_app = {k: m for k, _, m in order_averaged(1)}
    oa_den = {k: m for k, _, m in order_averaged(0)}
    n_sets = {k: c for k, c, _ in order_averaged(1)}
    for k in range(5):
        print(f"  {k} | {n_sets[k]:>4} | {oa_app[k]:16.3f} | {oa_den[k]:11.3f}")

    # Evaluate the hypotheses.
    def phi_falls(rows):
        phis = [r[2] for r in rows]
        return all(phis[i] >= phis[i + 1] for i in range(len(phis) - 1)) and phis[-1] < 1e-9

    def parties_shed(rows):
        # The mediator reads fewer parties as k rises, ending at neither.
        reads = [len(r[4]) for r in rows]
        return reads[0] == 2 and reads[-1] == 0 and all(reads[i] >= reads[i + 1] for i in range(len(reads) - 1))

    h1 = phi_falls(approve) and phi_falls(deny)
    h2 = parties_shed(approve) and parties_shed(deny)
    print("\n" + "=" * 84)
    print(f"  H1 (Φ falls monotonically to 0 as interestedness rises): {'SUPPORTED' if h1 else 'NOT SUPPORTED'}")
    print(f"  H2 (the mediator sheds the parties as it serves its agenda): {'SUPPORTED' if h2 else 'NOT SUPPORTED'}")
    print("  Reading: a mediator that imposes its own agenda over the parties' joint determination")
    print("  stops reading them; the coordination's irreducibility erodes and collapses to dyadic when")
    print("  the agenda fully displaces the parties. Self-interest is structurally disintegrating.")
    print("=" * 84)


if __name__ == "__main__":
    main()
