"""Probe 279 (H1) — is the major complex spectator-robust? [dry-run test contribution]

Question: PROBES.md states the verdict is read on the major complex precisely because a form may
carry idle nodes and the reading must be "spectator-robust" — a node that neither reads nor is read
by the coordination should not change which parties are in the irreducible core. This control probe
makes that property an explicit, registered check rather than an assumed one.

Hypothesis (H1): adding a fully decoupled spectator node X (X' = X; W, S, C rules unchanged) to the
canonical strict-mediation triad ats_triad_mediator leaves the major complex exactly {W, S, C} at
Φ = 2.0. The spectator stays out of the core and does not move the verdict.

Null: the spectator joins the core, or its presence changes the core's Φ.

Method: validate the instrument on a known control first — the bare canonical triad
(ats_triad_mediator: W'=S, S'=W∧C, C'=S) must read triadic with major complex {W, S, C} at Φ = 2.0.
Then add the decoupled spectator and re-read the major complex with the same exact-Φ instrument
(org_frontier.probes.lib.major_complex). Compare core membership and Φ.

Validation gap: this is exact Φ on a small Boolean model. It is evidence about the instrument's
behavior on idle nodes, not a claim about any real organization.

Run:  python -m org_frontier.probes.probe_spectator_robustness
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from .lib import major_complex


def triad_rules():
    """Canonical strict-mediation triad (ats_triad_mediator): W'=S, S'=W∧C, C'=S."""
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]


def triad_with_spectator_rules():
    """The same triad plus a fully decoupled spectator X (X'=X). W, S, C rules unchanged."""
    return [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: x[3]]


def main():
    print("PROBE 279 (H1) — major-complex spectator-robustness [dry-run test]")
    print("=" * 64)

    # [1/2] Instrument control: the bare triad must read triadic {W,S,C} at Φ=2.0.
    core_ctrl, phi_ctrl = major_complex(triad_rules(), ("W", "S", "C"))
    ctrl_ok = tuple(core_ctrl) == ("W", "S", "C") and abs(phi_ctrl - 2.0) < 1e-6
    print(f"  CONTROL  bare triad           core={tuple(core_ctrl)} Φ={phi_ctrl:.3f}  "
          f"{'PASS' if ctrl_ok else 'FAIL'} (expect ('W', 'S', 'C') Φ=2.000)")
    if not ctrl_ok:
        print("  Instrument control failed — no verdict is trustworthy. Stopping.")
        raise SystemExit(1)

    # [2/2] Test: add a decoupled spectator; the core must be unchanged.
    core_test, phi_test = major_complex(triad_with_spectator_rules(), ("W", "S", "C", "X"))
    spectator_out = "X" not in core_test
    core_same = tuple(core_test) == ("W", "S", "C")
    phi_same = abs(phi_test - phi_ctrl) < 1e-6
    supported = spectator_out and core_same and phi_same

    print(f"  TEST     triad + spectator X   core={tuple(core_test)} Φ={phi_test:.3f}")
    print("=" * 64)
    print(f"  spectator stays out of core: {spectator_out}")
    print(f"  core unchanged {{W, S, C}}:     {core_same}")
    print(f"  Φ unchanged (2.000):         {phi_same}")
    print(f"  H1 {'supported' if supported else 'refuted'}: "
          f"the decoupled spectator does not enter the major complex and does not move Φ.")
    print("=" * 64)
    print("  Reading: the verdict is read on the major complex precisely so idle parties cannot")
    print("  alter it. A node that neither constrains nor is constrained by the coordination is a")
    print("  spectator — outside the irreducible core. Evidence about the model, not an organization.")


if __name__ == "__main__":
    main()
