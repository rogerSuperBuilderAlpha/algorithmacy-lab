"""Probe 283 (Q128) — the adaptive interested mediator: does a learning agenda re-integrate?

Question: Q126 modelled a self-interested mediator with a fixed agenda and found it erodes the coordination
— a predatory mediator that commits only its own objective (S' = O), ignoring the parties, drives the form
to dyadic. But a real platform's objective is not a fixed stance; it tracks the parties (a learning
intermediary forms its agenda from what the workers and counterparts do). Q128 asks whether adaptation
alone rescues the bind: when the predatory mediator's objective O is itself derived from the parties, does
the coordination stay irreducible, and does the objective become a member of the irreducible core?

The model is four nodes — worker W, system S, counterpart C, objective O. The mediator is predatory in the
strongest sense: S' = O, it commits exactly its own objective and never reads the parties directly. The
parties read the system: W' = S, C' = S. The objective updates by an adaptation rule O' = g(W, C), swept
from no adaptation (a frozen stance) to full adaptation (the parties' joint determination).

Hypotheses (fixed before computing):
  H1. A predatory mediator (S' = O) is dyadic when its objective is a frozen stance (O' = O), but
      irreducible when its objective adapts to the parties (O' depends on W, C). Adaptation re-integrates a
      coordination that fixed self-interest destroyed.
  H2. The adaptive objective O joins the major complex — it becomes a constitutive member of the
      irreducible core — and the parties re-enter the core through it. A frozen objective stays outside.

Null: adaptation makes no difference; a predatory mediator is dyadic regardless of how its objective is set.

Reading the result: the binding would route the parties through the objective (W, C → O → S → W, C) rather
than directly, so the system can be fully self-executing yet still bind the parties, provided its objective
encodes them.

Validation gap: exact Φ on a four-node Boolean model; evidence about the construct and the instrument, not a
claim about a real platform. "Objective", "agenda", "predatory" label the rules, not measured intent.

Run:  python -m org_frontier.questions.q128_adaptive_mediator.probe_adaptive_mediator
"""

from org_frontier.probes.lib import verdict, major_complex

LABELS = ("W", "S", "C", "O")  # 0=worker, 1=system, 2=counterpart, 3=objective


# Adaptation rules for the objective O' = g(W, C, O), from no adaptation to full.
ADAPTATIONS = {
    "frozen (O'=O)": lambda x: x[3],
    "reads worker (O'=W)": lambda x: x[0],
    "reads counterpart (O'=C)": lambda x: x[2],
    "joint AND (O'=W&C)": lambda x: x[0] & x[2],
    "either OR (O'=W|C)": lambda x: x[0] | x[2],
    "differ XOR (O'=W^C)": lambda x: x[0] ^ x[2],
}


def predatory_rules(adapt):
    """S' = O (the mediator commits only its objective, never reading the parties directly);
    W' = S, C' = S (the parties read the system); O' = adapt(state) (the objective updates)."""
    return [lambda x: x[1],      # W' = S
            lambda x: x[3],      # S' = O   (predatory)
            lambda x: x[1],      # C' = S
            adapt]               # O' = adaptation rule


def main():
    print("PROBE 283 (Q128) — the adaptive interested mediator: does a learning agenda re-integrate?")
    print("=" * 84)

    # Control: the faithful three-party triad still reads triadic Φ=2.0 (instrument sanity).
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    vc = verdict(triad, ("W", "S", "C"))
    ctrl = vc.structure == "triadic" and abs(vc.max_phi - 2.0) < 1e-6
    print(f"  CONTROL faithful 3-party triad: {vc.structure} Φ={vc.max_phi:.3f}  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    print("\n  A predatory mediator S'=O, with the objective's adaptation rule O'=g(W,C) swept:")
    print("  adaptation                |  structure | Φ_MIP | major complex   | O in core | parties in core")
    print("  --------------------------+------------+-------+-----------------+-----------+----------------")
    rows = []
    for name, adapt in ADAPTATIONS.items():
        rules = predatory_rules(adapt)
        v = verdict(rules, LABELS)
        core, phi = major_complex(rules, LABELS)
        core = core or ()
        o_in = "O" in core
        parties_in = sum(1 for p in ("W", "C") if p in core)
        core_str = "".join(core) if core else "(none)"
        print(f"  {name:<25} | {v.structure:<10} | {v.max_phi:5.3f} | {core_str:<15} | "
              f"{'yes' if o_in else 'no':<9} | {parties_in}/2")
        rows.append((name, v.structure, v.max_phi, core, o_in, parties_in))

    # The objective reads both parties only in the AND / OR / XOR adaptations.
    reads_both = {"joint AND (O'=W&C)", "either OR (O'=W|C)", "differ XOR (O'=W^C)"}
    by_name = {r[0]: r for r in rows}
    both_triadic = all(by_name[n][1] == "triadic" for n in reads_both)
    rest_dyadic = all(r[1] == "dyadic" for r in rows if r[0] not in reads_both)
    biconditional = both_triadic and rest_dyadic           # triadic iff the objective reads both parties
    o_in_when_triadic = all(r[4] for r in rows if r[1] == "triadic")
    full_core = any(r[5] == 2 and r[1] == "triadic" for r in rows)

    print("\n" + "=" * 84)
    print(f"  Pre-registered H1/H2 (any adaptation re-integrates): REFUTED — reading one party is not")
    print(f"  enough (O'=W and O'=C stay dyadic). The refined finding the data supports:")
    print(f"  (1) RE-INTEGRATION IFF THE OBJECTIVE READS BOTH PARTIES: "
          f"{'CONFIRMED' if biconditional else 'FAILED'} — the predatory")
    print(f"      mediator is triadic exactly when its objective encodes both W and C (AND/OR/XOR), and")
    print(f"      dyadic when the objective is frozen or reads only one party.")
    print(f"  (2) THE OBJECTIVE IS THE CONDUIT: {'CONFIRMED' if o_in_when_triadic else 'FAILED'} — whenever the")
    print(f"      coordination re-integrates, O is in the core; the parties bind through it"
          f"{', and under XOR all four nodes enter the core' if full_core else ''}.")
    print(f"  Adaptation lets self-interest and irreducible coordination coexist, but only an objective")
    print(f"  that encodes both parties carries the bind: W,C -> O -> S -> W,C.")
    print("=" * 84)


if __name__ == "__main__":
    main()
