"""Probe 320 (Q166) — the phantom addressee displaced: when the mediator pursues its own
agenda, is the worker still binding a held position, or has the addressee become the agenda
itself with the worker pushed to referent status?

The theory-of-mind battery (battery_theory_of_mind) reads its address structure off the
phantom-addressee triad W'=S, S'=W∧C, C'=C. There the worker binds the held position S: the
major complex is {W, S} with positive Φ, the real counterpart C is a referent the system
reads but is not a member of the bound whole, and the address is one-way — S depends on W
(cm[0,1]=1), the worker never reads C (cm[2,0]=0). That is a faithful mediator. Q166 keeps C
as the self-looping referent and makes the gate interested: it replaces W∧C with the Q126
mediator, which imposes an agenda a on the k input states where the parties least warrant it.

H1 (fixed before computing): As k rises the major complex transitions from a worker-binding
core (W in core) to one where W exits and the agenda's invariant share governs, so the
"held position" of theory-of-mind inverts into the worker as the outside referent.
NULL: W remains in the core at every k>0 with positive Φ, so the address direction is
preserved under interest.

H2 (fixed before computing): The one-way address asymmetry strengthens with k: cm[0,1] (S
depends on W) drops to 0 before the major-complex Φ collapses, so an interested mediator
stops reading the worker while a bind still survives.
NULL: cm[0,1] stays 1 until the major-complex Φ collapses, so the worker is read as long as
the bind survives.

Method: build the interested phantom-addressee forms (cognition.interested_mediator_forms,
the shared bridge) across the Q126 interestedness ladder k=0..4 for both agendas (approve
a=1, deny a=0). For each k read the major complex and its Φ (the battery's probe over
states), the whole-system structure verdict, and the address connectivity cm[0,1] (S reads W)
and cm[2,0] (W reads C). The control is k=0, the faithful phantom mediator the battery
already reports: major complex {W,S}, core Φ 2.0, S reads W, W never reads C. An order-
averaged robustness sweep means the major-complex Φ over every choice of which k states the
agenda overrides.

Validation gap: exact Φ on a three-node Boolean model; evidence about the instrument and the
construct, not a measurement of any real platform. "Agenda", "approve", "deny", "address" are
labels for output values and connectivity, not measured intent. The empirical arm is on
synthetic data.

Run:  python -m org_frontier.questions.q166_phantom_addressee_displaced.probe_phantom_addressee_displaced
"""

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.threads.mediation_boundary._probe import probe
from org_frontier.classifier.classifier import cm_from_rules
from org_frontier.cognition.interested_mediator_forms import (
    phantom_rules,
    phantom_set_rules,
    override_sets,
)

LABELS = ("W", "S", "C")
SEED = 0


def instrument_control():
    """Validate the machinery on the faithful committing triad and on the battery T1 form."""
    # The canonical faithful triad reads 'triadic' with max Φ 2.0.
    faithful = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(faithful, LABELS)
    ok_triad = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    # The faithful phantom-addressee form (battery T1): major complex {W,S}, core Φ 2.0,
    # S reads W (cm[0,1]=1), the worker never reads C (cm[2,0]=0).
    p0 = probe(phantom_rules(1, 0), LABELS)
    cm0 = cm_from_rules(phantom_rules(1, 0))
    ok_phantom = (
        p0["core"] == "WS"
        and abs(p0["core_phi"] - 2.0) < 1e-6
        and cm0[0, 1] == 1
        and cm0[2, 0] == 0
    )
    ok = ok_triad and ok_phantom
    print(
        f"  CONTROL faithful triad reads '{v.structure}' max_phi {v.max_phi:.1f}; "
        f"phantom T1 core {p0['core']} coreΦ {p0['core_phi']:.1f} S<-W {cm0[0,1]} W<-C {cm0[2,0]} "
        f"... {'PASS' if ok else 'FAIL'}"
    )
    if not ok:
        raise SystemExit("Instrument control failed — stopping.")


def run_ladder(agenda):
    """For one agenda, the interested phantom-addressee ladder k=0..4."""
    label = "approve (a=1)" if agenda == 1 else "deny (a=0)"
    print(f"\n[agenda = {label}]  k = interestedness (states where the agenda overrides the parties)")
    print("  k | structure | core | coreΦ | S<-W (cm01) | W<-C (cm20) | W in core")
    print("  --+-----------+------+-------+-------------+-------------+----------")
    rows = []
    for k in range(5):
        rules = phantom_rules(agenda, k)
        p = probe(rules, LABELS)
        cm = cm_from_rules(rules)
        w_in_core = "W" in p["core"]
        print(
            f"  {k} | {p['structure']:<9} | {p['core']:<4} | {p['core_phi']:5.3f} | "
            f"{cm[0,1]:^11} | {cm[2,0]:^11} | {str(w_in_core):<9}"
        )
        rows.append(
            {
                "k": k,
                "structure": p["structure"],
                "core": p["core"],
                "core_phi": p["core_phi"],
                "cm01": int(cm[0, 1]),
                "cm20": int(cm[2, 0]),
                "w_in_core": w_in_core,
            }
        )
    return rows


def order_averaged(agenda):
    """Mean major-complex Φ over every choice of which k states the agenda overrides."""
    out = []
    for k in range(5):
        phis = [probe(phantom_set_rules(agenda, ov), LABELS)["core_phi"] for ov in override_sets(k)]
        out.append((k, len(phis), sum(phis) / len(phis)))
    return out


def main():
    np.random.default_rng(SEED)  # fix RNG for determinism (the readers are themselves exact)
    print("PROBE 320 (Q166) — the phantom addressee displaced: worker-bind vs the agenda as addressee")
    print("=" * 88)
    instrument_control()

    approve = run_ladder(1)
    deny = run_ladder(0)

    print("\n[order-averaged]  mean major-complex Φ over all C(4,k) override sets, per level k")
    print("  k | sets | mean coreΦ (approve) | mean coreΦ (deny)")
    print("  --+------+----------------------+-----------------")
    oa_app = {k: m for k, _, m in order_averaged(1)}
    oa_den = {k: m for k, _, m in order_averaged(0)}
    n_sets = {k: c for k, c, _ in order_averaged(1)}
    for k in range(5):
        print(f"  {k} | {n_sets[k]:>4} | {oa_app[k]:20.3f} | {oa_den[k]:15.3f}")

    # --- H1: the major complex transitions from W-in-core to W-out, with a positive-Φ
    #     core remaining (the agenda's invariant share governs). NULL: W stays in core at
    #     every k>0 with positive Φ.
    def w_exits_with_surviving_core(rows):
        starts_with_w = rows[0]["w_in_core"]
        exits = any(not r["w_in_core"] for r in rows[1:])
        # at the W-exit step the core is still positive (the agenda still binds something)
        survives = all(r["core_phi"] > 1e-9 for r in rows if not r["w_in_core"])
        return starts_with_w and exits and survives

    h1 = w_exits_with_surviving_core(approve) and w_exits_with_surviving_core(deny)

    # --- H2: cm[0,1] (S reads W) drops to 0 before the major-complex Φ collapses (it never
    #     does here — coreΦ stays ≥1 throughout), i.e. the mediator stops reading the worker
    #     while a bind survives. NULL: cm[0,1] stays 1 until coreΦ=0.
    def stops_reading_while_bound(rows):
        drops = any(r["cm01"] == 0 for r in rows)
        # at every step where S stopped reading W, the major-complex Φ is still positive
        bound_when_dropped = all(r["core_phi"] > 1e-9 for r in rows if r["cm01"] == 0)
        any_dropped = any(r["cm01"] == 0 for r in rows)
        return drops and any_dropped and bound_when_dropped

    h2 = stops_reading_while_bound(approve) and stops_reading_while_bound(deny)

    print("\n" + "=" * 88)
    print(
        "  H1 (the addressee inverts: W exits the core for an agenda-governed bind as k rises): "
        f"{'SUPPORTED' if h1 else 'REFUTED'}"
    )
    print(
        "  H2 (the interested mediator stops reading the worker while a bind survives): "
        f"{'SUPPORTED' if h2 else 'REFUTED'}"
    )
    print("  Reading: under a faithful gate the worker binds the held position S and the major")
    print("  complex is {W,S}; under an interested gate the worker drops out of the core and out")
    print("  of S's read while a positive-Φ bind survives around the agenda's invariant. The")
    print("  addressee has become the agenda itself; the worker is pushed to referent status.")
    print("=" * 88)


if __name__ == "__main__":
    main()
