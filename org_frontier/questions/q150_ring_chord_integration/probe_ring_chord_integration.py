"""q150 — adding one chord across a conjunctive ring: does the long-range AND link raise Φ?

Question: a conjunctive ring of n nodes (each node = AND of its two ring neighbors) integrates
around one long cycle. Adding a single chord between two opposite nodes gives those two nodes a
third input, the chord partner, and creates a shorter competing cycle. Does the chord raise the
ring's Φ by shortening the integration cycle, and does the major complex concentrate on the
chorded arc?

H1: One chord raises ring Φ and shifts the MIP cut off the chord onto the longer arc, because the
    chord creates a shorter competing cycle that is no longer the cheapest cut.
    Null: the chord leaves Φ and the MIP cut unchanged.

H2: The chorded nodes gain Shapley value at the expense of the far arc, so a single long-range tie
    redistributes captured Φ toward its endpoints.
    Null: Shapley values are unchanged by the chord.

Method: take ring(n=6) (each node = AND of its two ring neighbors); add one chord across the
opposite pair (A, D) so each endpoint also ANDs its partner. verdict() reports structure, max Φ_MIP,
and the MIP cut at the max-Φ state; major_complex() reports the irreducible core and its Φ;
shapley() reports the per-node Shapley share of subsystem Φ at the all-ones integrating state.
Control: the unchorded ring, against which both arms are read.

Scope: in-silico. Both forms are synthetic Boolean coordination models, not measured organizations.
The result characterizes how an exact-Φ read of a ring responds to one long-range tie; it does not
measure integration or value capture in any real group. No worker is measured.

Run:
  source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q150_ring_chord_integration.probe_ring_chord_integration
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.questions.q111_shapley_value.forms import shapley
from org_frontier.probes.probe_scaling_zoo import ring

# Fixed seed: verdict/major_complex/shapley are exact and deterministic over the reachable-state
# enumeration, but seed the RNG so any incidental randomness reproduces byte-for-byte on re-run.
RNG = np.random.default_rng(0)

N = 6
LABELS = tuple("ABCDEF")          # A..F  ->  ring indices 0..5
CHORD = (0, 3)                    # the opposite pair joined by the chord: A and D
TOL = 1e-6


def unchorded_ring():
    """ring(n=6): each node is the AND of its two ring neighbors."""
    return ring(N)


def chorded_ring():
    """ring(n=6) plus one chord across the opposite pair (A, D).

    Every node is the AND of its two ring neighbors. The two chord endpoints also AND their
    chord partner, so A reads {F, B, D} and D reads {C, E, A}; the rest of the ring is unchanged.
    """
    return [
        lambda x: x[5] & x[1] & x[3],   # A (0): ring neighbors F,B + chord D
        lambda x: x[0] & x[2],          # B (1): ring neighbors A,C
        lambda x: x[1] & x[3],          # C (2): ring neighbors B,D
        lambda x: x[2] & x[4] & x[0],   # D (3): ring neighbors C,E + chord A
        lambda x: x[3] & x[5],          # E (4): ring neighbors D,F
        lambda x: x[4] & x[0],          # F (5): ring neighbors E,A
    ]


def _chord_side_split(mip_partition, chord_labels):
    """True if both chord endpoints fall on the same side of the MIP cut.

    The classifier renders the cut as e.g. "2 parts: {BC,ADEF}": one brace pair holding the parts
    separated by commas. Split the inside on commas to recover each part, then test whether the two
    chord endpoints share a part. When they share a part the cut does not run between them, so it
    has moved off the chord.
    """
    import re
    inside = re.search(r"\{(.*)\}", mip_partition)
    if not inside:
        return False
    parts = [set(p) for p in inside.group(1).split(",")]
    a, b = chord_labels
    for p in parts:
        if a in p and b in p:
            return True
    return False


def instrument_control():
    """Validate the machinery on a known case before computing anything new.

    The faithful worker-system-counterpart triad reads 'triadic' at max Φ_MIP 2.0.
    """
    v = verdict([lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]], ("W", "S", "C"))
    assert v.structure == "triadic", v.structure
    assert abs(v.max_phi - 2.0) < TOL, v.max_phi
    print(f"CONTROL faithful triad: structure={v.structure}, max Φ_MIP={v.max_phi:.6f}: PASS")


def run():
    instrument_control()

    forms = [("unchorded ring", unchorded_ring()), ("chord A-D    ", chorded_ring())]
    rows = []
    for name, rules in forms:
        v = verdict(rules, LABELS)
        core, core_phi = major_complex(rules, LABELS)
        vals, total = shapley(rules, LABELS)
        rows.append((name, v, core, core_phi, vals, total))

    name0, v0, core0, cphi0, vals0, tot0 = rows[0]
    name1, v1, core1, cphi1, vals1, tot1 = rows[1]

    # ---- table 1: whole-system Φ and the MIP cut --------------------------------------------
    print()
    print("Φ_MIP and the major complex (max over reachable states)")
    print(f"  {'form':<16}{'struct':<10}{'maxΦ':>8}   {'MIP cut':<16}{'major complex':<16}{'coreΦ':>7}")
    for name, v, core, cphi, _, _ in rows:
        cut = v.mip_partition.split(":", 1)[-1].strip() if v.mip_state is not None else "(factors)"
        core_s = "".join(core) if core else "-"
        print(f"  {name:<16}{v.structure:<10}{v.max_phi:>8.4f}   {cut:<16}{core_s:<16}{cphi:>7.4f}")

    # ---- table 2: Shapley split ------------------------------------------------------------
    print()
    print("Shapley share of subsystem Φ at the all-ones integrating state")
    print(f"  {'form':<16}" + "".join(f"{lab:>7}" for lab in LABELS) + f"{'total':>9}")
    print(f"  {name0:<16}" + "".join(f"{vals0[lab]:>7.3f}" for lab in LABELS) + f"{tot0:>9.3f}")
    print(f"  {name1:<16}" + "".join(f"{vals1[lab]:>7.3f}" for lab in LABELS) + f"{tot1:>9.3f}")

    chord_labels = (LABELS[CHORD[0]], LABELS[CHORD[1]])
    far_labels = tuple(lab for lab in LABELS if lab not in chord_labels)
    endpoint0 = sum(vals0[l] for l in chord_labels)
    endpoint1 = sum(vals1[l] for l in chord_labels)
    far0 = sum(vals0[l] for l in far_labels)
    far1 = sum(vals1[l] for l in far_labels)
    print()
    print(f"  chord endpoints {chord_labels}: {endpoint0:.3f} -> {endpoint1:.3f}"
          f"   far arc {far_labels}: {far0:.3f} -> {far1:.3f}")

    # ---- H1: chord raises Φ AND shifts the MIP cut off the chord -----------------------------
    phi_rose = v1.max_phi > v0.max_phi + TOL
    cut_off_chord_0 = _chord_side_split(v0.mip_partition, chord_labels) if v0.mip_state else False
    cut_off_chord_1 = _chord_side_split(v1.mip_partition, chord_labels) if v1.mip_state else False
    cut_shifted_off = cut_off_chord_1 and not cut_off_chord_0
    h1 = phi_rose and cut_shifted_off
    print()
    print(f"H1 detail: Φ {v0.max_phi:.4f} -> {v1.max_phi:.4f} (rose={phi_rose}); "
          f"chord endpoints share a part: unchorded={cut_off_chord_0}, chorded={cut_off_chord_1} "
          f"(cut moved off chord={cut_shifted_off})")
    print(f"H1 chord raises ring Φ and shifts MIP cut off the chord: "
          f"{'SUPPORTED' if h1 else 'REFUTED'}")

    # ---- H2: chord endpoints gain Shapley value at the expense of the far arc ----------------
    endpoints_gained = endpoint1 > endpoint0 + 1e-3
    far_lost = far1 < far0 - 1e-3
    h2 = endpoints_gained and far_lost
    print(f"H2 chord endpoints gain Shapley value at the expense of the far arc: "
          f"{'SUPPORTED' if h2 else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    run()
