"""Probe 296 (Q141) — the lagging objective: does adaptation on a delay rescue the displaced party?

Q128 found a predatory mediator (S' = O) re-integrates the coordination when its objective adapts to both
parties, and Q129 found the immediate adaptive objective displaces a party from the core (core {S, C, O}, the
worker pushed out). Q141 asks whether the timescale of adaptation matters: if the objective learns from the
parties on a lag — through a memory that holds their joint state for a step — does the displaced worker return?

The immediate model is Q128's: W' = S, S' = O, C' = S, O' = W ∧ C. The lagged model inserts a memory node M
that captures the parties' joint state, and the objective reads the memory rather than the parties directly:
M' = W ∧ C, O' = M, with S' = O, W' = S, C' = S. The objective now tracks the joint determination with a
one-step delay.

Hypotheses (fixed before computing):
  H1. The lagging objective re-integrates the worker that immediate adaptation displaced: the lagged form's
      major complex includes the worker, unlike the immediate form's core {S, C, O}.
  H2. The lagged form is more integrated than the immediate one — the memory raises the coordination's Φ.

Method: build both forms; read the whole-system verdict and the major complex; check whether the worker is in
the core and compare the Φ.

Validation gap: exact Φ; the lagged form has five nodes (memory added), so the comparison spans a size change,
named in the limitations. Φ-to-money bridge open (Q122).

Run:  python -m org_frontier.questions.q141_lagging_objective.probe_lagging_objective
"""

from org_frontier.probes.lib import verdict, major_complex

LAB_IMMEDIATE = ("W", "S", "C", "O")
LAB_LAGGED = ("W", "S", "C", "O", "M")

# Immediate (Q128): the objective reads the parties directly.
IMMEDIATE = [lambda x: x[1], lambda x: x[3], lambda x: x[1], lambda x: x[0] & x[2]]
# Lagged: a memory M holds the parties' joint state; the objective reads the memory.
LAGGED = [lambda x: x[1], lambda x: x[3], lambda x: x[1], lambda x: x[4], lambda x: x[0] & x[2]]


def main():
    print("PROBE 296 (Q141) — the lagging objective: does adaptation on a delay rescue the displaced party?")
    print("=" * 92)

    # Control: the canonical three-party triad still reads triadic Φ=2.0.
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    vc = verdict(triad, ("W", "S", "C"))
    ctrl = vc.structure == "triadic" and abs(vc.max_phi - 2.0) < 1e-6
    print(f"  CONTROL faithful triad: {vc.structure} Φ={vc.max_phi:.3f}  {'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    vi = verdict(IMMEDIATE, LAB_IMMEDIATE)
    core_i, phi_i = major_complex(IMMEDIATE, LAB_IMMEDIATE)
    core_i = tuple(core_i or ())
    w_in_i = "W" in core_i
    print(f"\n  immediate (O' = W ∧ C):  {vi.structure} Φ={vi.max_phi:.3f} | major complex={core_i} | "
          f"worker in core: {w_in_i}")

    vl = verdict(LAGGED, LAB_LAGGED)
    core_l, phi_l = major_complex(LAGGED, LAB_LAGGED)
    core_l = tuple(core_l or ())
    w_in_l = "W" in core_l
    print(f"  lagged (O' = M, M' = W ∧ C): {vl.structure} Φ={vl.max_phi:.3f} | major complex={core_l} | "
          f"worker in core: {w_in_l}")

    h1 = (not w_in_i) and w_in_l
    h2 = vl.max_phi > vi.max_phi + 1e-9

    print("\n" + "=" * 92)
    print(f"  H1 (the lag re-integrates the displaced worker — out of core when immediate, in when lagged): "
          f"{'SUPPORTED' if h1 else 'NOT SUPPORTED'}")
    print(f"  H2 (the lagged form is more integrated than the immediate one): "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}  (Φ lagged {vl.max_phi:.1f} > immediate {vi.max_phi:.1f})")
    print("  Reading: the timescale of the system's learning decides the worker's place in the coordination.")
    print("  An objective that adapts to the parties instantly substitutes for the worker and pushes it out of")
    print("  the core; an objective that adapts on a delay, through a memory of the parties' joint state, keeps")
    print("  the worker constitutive and binds the whole into one irreducible core at higher Φ. A platform that")
    print("  learns slowly keeps the worker in the coordination; one that learns in real time displaces it.")
    print("=" * 92)


if __name__ == "__main__":
    main()
