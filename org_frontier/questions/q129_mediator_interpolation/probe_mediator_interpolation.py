"""Probe 284 (Q129) — faithful to predatory: the phase boundary an adaptive objective holds open.

Question: the interested-mediator arc has two endpoints. A faithful mediator commits the parties' joint
determination (S' = W ∧ C) and the coordination is irreducible (Q120). A predatory mediator commits only
its own objective (S' = O); with a frozen objective the coordination collapses to dyadic (Q126), but with an
objective that reads both parties it stays irreducible (Q128). Q129 fills in between: interpolate the
mediator from faithful to predatory and map where the coordination survives, with the objective frozen and
with it adaptive.

The mediator interpolates by a mix level m = 0..4. On m of the four (W, C) input states it serves its
objective (output O); on the rest it commits faithfully (output W ∧ C). m = 0 is faithful, m = 4 is fully
predatory. The parties read the system (W' = S, C' = S). The objective is either frozen (O' = O) or adaptive
(O' = W ∧ C). Φ is read at each m for each objective, both along a fixed order and averaged over every
choice of which m states serve the objective.

Hypotheses (fixed before computing):
  H1. With a frozen objective, Φ falls as the mediator turns predatory (m rises), reaching dyadic at the
      fully predatory end.
  H2. With an adaptive objective (reads both parties), the coordination stays irreducible across the whole
      interpolation, including the fully predatory end — adaptation holds the phase boundary open.

Null: the objective's adaptation makes no difference to where the coordination collapses.

Validation gap: exact Φ on Boolean models; evidence about the construct and the instrument, not a claim
about a real platform.

Run:  python -m org_frontier.questions.q129_mediator_interpolation.probe_mediator_interpolation
"""

from itertools import combinations

from org_frontier.probes.lib import verdict, major_complex

LABELS = ("W", "S", "C", "O")          # 0=worker, 1=system, 2=counterpart, 3=objective
STATES = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (W, C) inputs

OBJECTIVES = {
    "frozen": lambda x: x[3],            # O' = O
    "adaptive": lambda x: x[0] & x[2],   # O' = W & C
}


def rules(serve_set, obj):
    """S' serves the objective O on serve_set, commits faithful W∧C elsewhere; parties read S; O updates."""
    serve = set(serve_set)
    def s_rule(x):
        return x[3] if (x[0], x[2]) in serve else (x[0] & x[2])
    return [lambda x: x[1], s_rule, lambda x: x[1], obj]


def coordination(serve_set, obj):
    """The irreducible core and the Φ that actually binds the parties. The objective O can be a
    disconnected spectator at low mix, so the verdict is read on the major complex (lab convention).
    Returns (core, phi, bound) where bound is True iff both parties W and C are in the core, and the
    coordination Φ is that core's Φ when both parties are bound, else 0."""
    core, phi = major_complex(rules(serve_set, obj), LABELS)
    core = tuple(core) if core else ()
    bound = ("W" in core) and ("C" in core)
    return core, (phi if bound else 0.0), bound


def main():
    print("PROBE 284 (Q129) — faithful → predatory: the phase boundary an adaptive objective holds open")
    print("=" * 88)

    # Control: m=0 is the faithful triad — its major complex is {W,S,C} at Φ=2.0 (O is a spectator).
    core0, phi0, bound0 = coordination((), OBJECTIVES["frozen"])
    ctrl = bound0 and abs(phi0 - 2.0) < 1e-6
    print(f"  CONTROL faithful mediator (m=0): core={core0} coordination-Φ={phi0:.3f}  "
          f"{'PASS' if ctrl else 'FAIL'}")
    if not ctrl:
        raise SystemExit("Instrument control failed — stopping.")

    # Fixed-order ladder: convert states to objective-serving in a fixed order, m = 0..4.
    order = STATES
    print("\n  Fixed-order interpolation (m = states where the mediator serves its objective O):")
    print("  m | frozen O'=O : Φ / core / bound? | adaptive O'=W&C : Φ / core / bound?")
    print("  --+--------------------------------+-----------------------------------")
    ladders = {name: [] for name in OBJECTIVES}
    for m in range(5):
        serve = order[:m]
        cells = {}
        for name, obj in OBJECTIVES.items():
            core, phi, bound = coordination(serve, obj)
            ladders[name].append(phi)
            cells[name] = f"{phi:5.3f} / {''.join(core) or '(none)':<4} / {'yes' if bound else 'no'}"
        print(f"  {m} | {cells['frozen']:<30} | {cells['adaptive']}")

    # Order-averaged: mean coordination-Φ over every choice of which m states serve the objective.
    print("\n  Order-averaged (mean coordination-Φ over all C(4,m) serve-sets):")
    print("  m | sets | mean Φ frozen | mean Φ adaptive")
    print("  --+------+---------------+----------------")
    oa = {name: [] for name in OBJECTIVES}
    for m in range(5):
        sets = list(combinations(STATES, m))
        for name, obj in OBJECTIVES.items():
            oa[name].append(sum(coordination(s, obj)[1] for s in sets) / len(sets))
        print(f"  {m} | {len(sets):>4} | {oa['frozen'][m]:13.3f} | {oa['adaptive'][m]:14.3f}")

    # Second reading: whole-system irreducibility (Φ_MIP > 0 over all four nodes, the Q128 measure).
    print("\n  Whole-system reading (is the four-node system irreducible? Q128's measure):")
    print("  m | frozen: structure / Φ | adaptive: structure / Φ")
    print("  --+------------------------+------------------------")
    whole = {name: [] for name in OBJECTIVES}
    for m in range(5):
        serve = STATES[:m]
        cells = {}
        for name, obj in OBJECTIVES.items():
            v = verdict(rules(serve, obj), LABELS)
            whole[name].append(v.max_phi)
            cells[name] = f"{v.structure} / {v.max_phi:.3f}"
        print(f"  {m} | {cells['frozen']:<22} | {cells['adaptive']}")

    fr = ladders["frozen"]
    ad = ladders["adaptive"]
    last_bound = lambda L: max((m for m, p in enumerate(L) if p > 1e-9), default=-1)
    last_whole = lambda L: max((m for m, p in enumerate(L) if p > 1e-9), default=-1)

    print("\n" + "=" * 88)
    print(f"  Two readings of 'the coordination survives' diverge, and that divergence is the finding.")
    print(f"  PARTIES BOUND IN THE CORE: frozen holds to m={last_bound(fr)}, adaptive only to m={last_bound(ad)}.")
    print(f"  WHOLE-SYSTEM IRREDUCIBLE:  frozen to m={last_whole(whole['frozen'])}, "
          f"adaptive to m={last_whole(whole['adaptive'])}.")
    print(f"  DISPLACEMENT: an adaptive objective sustains whole-system irreducibility further (it joins the")
    print(f"  core itself), but it does so by displacing a party — so the parties' own binding survives LONGER")
    print(f"  under a frozen objective. Q128's 're-integration' is the system staying irreducible, not the")
    print(f"  parties staying bound. Adaptive self-interest preserves the coordination by entering it and")
    print(f"  pushing a party out; frozen self-interest preserves the parties' bind until it fully defects.")
    print("=" * 88)


if __name__ == "__main__":
    main()
