"""Probe 322 (Q168) — the opacity floor under an agenda: does interest raise the worker's surprise floor?

Question: predictive_processing.pp1_irreducible_surprise derives a 0.50-bit residual H(out|W) for the
faithful hidden-counterpart gate (out = W ∧ C, C hidden and uniform): half a bit of surprise no model
removes, set by what the worker cannot see. pp2_active_inference adds that probing W (active inference)
closes the channel she controls but leaves that floor intact. Both fix the output to the faithful gate.
Q126 made the mediator interested: it imposes an agenda on the k states where the parties least warrant it.
This probe recomputes H(out|W) and the W-probing limit with the output drawn from mediator(agenda, k) over
uniform hidden C, sweeping k, and compares against the 0.50-bit faithful floor.

H1 (fixed before computing): The residual surprise H(out|W) for an interested mediator exceeds the 0.50-bit
    floor that PP1 derives for the faithful hidden-counterpart gate, because the agenda adds output variance
    uncorrelated with anything the worker can set or see.
    NULL: H(out|W) under interest equals the 0.50-bit faithful floor, so an agenda adds no irreducible
    surprise.

H2 (fixed before computing): The added surprise is unremovable by active inference: probing W (PP2) leaves
    H(out|W) under the interested mediator unchanged, so the agenda contributes to the opacity floor and not
    to the channel the worker controls.
    NULL: probing W drives interested H(out|W) toward 0, so the agenda's contribution is epistemic and
    self-resolvable.

Method: reuse predictive_processing.residual_surprise_under_mediator (H(out|W), C hidden and uniform) and
    probed_w_limit_under_mediator (the residual that survives probing W), with the gate set to Q126's
    mediator(agenda, k). Sweep k = 0..4 for each agenda (approve a=1, deny a=0). The faithful AND gate's
    k=0 value reproduces PP1's 0.50-bit floor and is the control. H1 holds if some interested k raises
    H(out|W) above 0.50; H2 holds if the W-probing limit equals H(out|W) at every k (probing removes none
    of it).

Determinism: the surprise accounting is exact (closed-form binary entropy over a 4-state truth table); no
    RNG enters the result. A seeded generator is fixed for reproducibility hygiene.

Validation gap: closed-form information theory on a 3-variable Boolean model. Evidence about the instrument
    and the construct, not a claim about a real platform. "Agenda", "approve", "deny", "interest" label
    output values and rule structure, not measured intent. The empirical reading is on synthetic forms.

Run:  python -m org_frontier.questions.q168_opacity_floor_under_agenda.probe_opacity_floor_under_agenda
"""

import numpy as np

from org_frontier.cognition.predictive_processing import (
    residual_surprise_under_mediator,
    probed_w_limit_under_mediator,
)
from org_frontier.questions.q126_interested_mediator.probe_interested_mediator import mediator

RNG = np.random.default_rng(0)  # reproducibility hygiene; the computation is exact and uses no RNG

FAITHFUL_FLOOR = 0.50           # PP1's residual H(out|W) for the faithful AND gate, C hidden and uniform
AGENDAS = ((1, "approve (a=1)"), (0, "deny (a=0)"))


def instrument_control():
    """The faithful hidden-counterpart gate (out = W ∧ C, k=0) must read the 0.50-bit PP1 floor, and the
    canonical faithful triad must read 'triadic' with max_phi 2.0."""
    faithful = mediator(1, 0)  # k=0 approve = pure AND
    floor = residual_surprise_under_mediator(faithful)
    ok_floor = abs(floor - 0.50) < 1e-9

    from org_frontier.probes.lib import verdict
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, ("W", "S", "C"))
    ok_triad = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-9

    ok = ok_floor and ok_triad
    print(f"CONTROL faithful gate H(out|W)={floor:.2f} bits (PP1 floor 0.50); "
          f"faithful triad {v.structure} max_phi={v.max_phi:.1f} -- {'PASS' if ok else 'FAIL'}")
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")


def sweep(agenda):
    """Per k: (k, H(out|W) under the interested mediator, the W-probing limit, the part probing removes)."""
    rows = []
    for k in range(5):
        gate = mediator(agenda, k)
        hout = residual_surprise_under_mediator(gate)
        probed = probed_w_limit_under_mediator(gate)
        removed = hout - probed
        rows.append((k, hout, probed, removed))
    return rows


def print_sweep(label, rows):
    print(f"\n[agenda = {label}]  C hidden and uniform; floor = 0.50 bits (faithful, k=0)")
    print("  k | H(out|W) | vs floor | after probing W | probing removes")
    print("  --+----------+----------+-----------------+----------------")
    for k, hout, probed, removed in rows:
        rel = "=" if abs(hout - FAITHFUL_FLOOR) < 1e-9 else ("> floor" if hout > FAITHFUL_FLOOR else "< floor")
        print(f"  {k} | {hout:8.2f} | {rel:^8} | {probed:15.2f} | {removed:15.2f}")


def main():
    print("PROBE 322 (Q168) — opacity floor under an agenda: interest vs the hidden-counterpart floor")
    print("=" * 92)
    instrument_control()

    sweeps = {}
    for agenda, label in AGENDAS:
        rows = sweep(agenda)
        sweeps[agenda] = rows
        print_sweep(label, rows)

    # ---- H1: does any interested k raise H(out|W) above the 0.50-bit faithful floor? ----
    def exceeds_floor(rows):
        return [(k, hout) for k, hout, _, _ in rows if k > 0 and hout > FAITHFUL_FLOOR + 1e-9]

    over_app = exceeds_floor(sweeps[1])
    over_den = exceeds_floor(sweeps[0])
    h1 = bool(over_app or over_den)

    # ---- H2: does probing W leave H(out|W) unchanged at every k (removes none of it)? ----
    def probing_removes_nothing(rows):
        return all(abs(removed) < 1e-9 for _, _, _, removed in rows)

    h2_app = probing_removes_nothing(sweeps[1])
    h2_den = probing_removes_nothing(sweeps[0])
    h2 = h2_app and h2_den

    print("\n" + "=" * 92)
    print(f"  H1 interest raises H(out|W) above the 0.50-bit faithful floor: "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")
    print(f"  H2 probing W leaves interested H(out|W) unchanged (agenda joins the opacity floor): "
          f"{'CONFIRMED' if h2 else 'NOT SUPPORTED'}")
    print("=" * 92)

    if h1:
        ks = ", ".join(f"k={k} ({h:.2f} bits)" for k, h in (over_app + over_den))
        side = []
        if over_app:
            side.append("approve")
        if over_den:
            side.append("deny")
        print(f"  Reading H1: the interested residual exceeds 0.50 bits at {ks} under the "
              f"{' and '.join(side)} agenda. Overriding a low-warrant state aliases C-driven variance "
              f"into a W-value the faithful gate left determinate, so the agenda adds surprise the worker "
              f"can neither set nor see.")
    else:
        print("  Reading H1: the null holds. No interested k raises H(out|W) above 0.50; an agenda that "
              "only collapses output variance cannot exceed the faithful floor.")
    if h2:
        print("  Reading H2: probing W removes none of H(out|W) at any k. The surplus is C-aliased, so "
              "setting and observing W learns P(out|W) exactly yet leaves the C-driven part intact. The "
              "agenda's contribution sits on the opacity floor, not in the channel the worker controls.")


if __name__ == "__main__":
    main()
