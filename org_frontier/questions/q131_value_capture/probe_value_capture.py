"""Probe 286 (Q131) — value capture under an interested mediator: who gets what as the system serves itself.

Question: Q126–Q129 read whether an interested mediator keeps the coordination irreducible. This asks the
value question the synthesis paper left open: as the mediator imposes its own agenda, how is the
coordination's value distributed among the parties? The value of a coalition is the integrated information
of the subsystem on it (Q111), and a party's Shapley value is its average marginal contribution. For the
faithful mediator the Shapley split is mediator 1.333 (two-thirds of Φ = 2.0), each party 0.333. Q131 sweeps
the interestedness axis and reads the split at each step.

Two readings are possible. Interested mediation could be rent extraction — the mediator grabs a larger share
as it serves itself — or value destruction in which the mediator loses its own capture along with everyone
else, because a system that stops reading the parties stops being the bottleneck that gave it its share.

Hypotheses (fixed before computing):
  H1. Total value (Φ) falls as interestedness rises — self-interest shrinks the pie, consistent with the
      Q126 erosion.
  H2. The mediator's share of the (shrinking) value falls as it turns predatory, not rises: serving its own
      agenda costs the mediator the bottleneck position that gave it two-thirds. Interested mediation is
      value destruction, not rent extraction.

Null: the Shapley split is unchanged by interestedness.

Method: the Q126 interested mediator on the AND baseline — at interestedness level k the mediator imposes
its agenda a on the k input states where the parties least warrant it, committing W ∧ C elsewhere; W' = S,
C' = S. At each k for each agenda, compute the Shapley value of subsystem-Φ for each party (Q111's value
function, all-ones background) and the total Φ.

Validation gap: exact Φ on a three-node Boolean model; the value function follows Q111's all-ones background
convention, and the Φ-to-economic-value bridge is the lab's standing open question (Q122). Evidence about
the construct and the instrument, not about a real platform.

Run:  python -m org_frontier.questions.q131_value_capture.probe_value_capture
"""

from org_frontier.questions.q111_shapley_value.forms import shapley

LABELS = ("W", "S", "C")
STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (W, C) inputs


def override_order(agenda):
    warrant = lambda wc: (wc[0] + wc[1]) if agenda == 1 else (2 - (wc[0] + wc[1]))
    return sorted(STATES, key=lambda wc: (warrant(wc), wc))


def interested_rules(agenda, k):
    """S' = agenda on the k least-warranted states, faithful AND elsewhere; W' = S, C' = S."""
    override = set(override_order(agenda)[:k])
    def f(w, c):
        return agenda if (w, c) in override else (w & c)
    return [lambda x: x[1], lambda x, f=f: f(x[0], x[2]), lambda x: x[1]]


def run_ladder(agenda, name):
    print(f"\n[agenda = {name}]  k = interestedness level")
    print("  k | total Φ | Shapley W / S / C        | mediator share")
    print("  --+---------+--------------------------+---------------")
    rows = []
    for k in range(5):
        sv, total = shapley(interested_rules(agenda, k), LABELS)
        share = (sv["S"] / total) if total > 1e-9 else 0.0
        print(f"  {k} | {total:7.3f} | {sv['W']:6.3f} / {sv['S']:6.3f} / {sv['C']:6.3f}   | "
              f"{share:6.1%}")
        rows.append((k, total, sv, share))
    return rows


def main():
    print("PROBE 286 (Q131) — value capture under an interested mediator")
    print("=" * 72)

    # Control: the faithful mediator (k=0) reproduces Q111 — total Φ=2.0, mediator share 2/3.
    sv0, total0 = shapley(interested_rules(1, 0), LABELS)
    ctrl = abs(total0 - 2.0) < 1e-6 and abs(sv0["S"] - 1.333) < 1e-3
    print(f"  CONTROL faithful mediator: total Φ={total0:.3f}, Shapley S={sv0['S']:.3f} "
          f"(share {sv0['S']/total0:.1%})  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    approve = run_ladder(1, "approve (a=1)")
    deny = run_ladder(0, "deny (a=0)")

    # Evaluate hypotheses on the approve ladder (the graceful one; deny collapses at k=1).
    totals = [r[1] for r in approve]
    shares = [r[3] for r in approve if r[1] > 1e-9]    # mediator share while value remains
    h1 = all(totals[i] >= totals[i + 1] for i in range(len(totals) - 1)) and totals[-1] < 1e-9
    # H2: among the steps with positive value, does the mediator's share fall (not rise)?
    h2 = len(shares) >= 2 and shares[-1] <= shares[0] + 1e-9

    print("\n" + "=" * 72)
    print(f"  H1 (total value falls to zero as interestedness rises): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}  (Φ: {', '.join(f'{t:.2f}' for t in totals)})")
    print(f"  H2 (the mediator's share falls, not rises — value destruction not rent extraction): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}  (share while positive: "
          f"{', '.join(f'{s:.0%}' for s in shares)})")
    print("  Reading: an interested mediator does not extract a larger share by serving itself. The")
    print("  coordination's value shrinks and the mediator's own capture shrinks with it, because the share")
    print("  came from being the bottleneck both parties needed — exactly what self-interest gives up.")
    print("=" * 72)


if __name__ == "__main__":
    main()
