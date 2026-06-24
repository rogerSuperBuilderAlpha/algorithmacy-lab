"""q184 — Φ spread between a driver's suggestion account and a platform's commit account of one dispatch.

Question: When a gig driver narrates dispatch as a one-way suggestion (dyad) and the platform
narrates it as committing the driver-rider match (false triad), how large is the measured Φ
spread between the two accounts?

H1: The driver's suggestion account scores a dyadic verdict (Φ_MIP = 0 / structure not triadic)
    and the platform's commit account a triadic verdict (Φ_MIP > 0), so verdict_agreement = 0 and
    phi_gap equals the platform account's whole-system max Φ_MIP.
    H1-null: both accounts yield the same verdict and phi_gap = 0, so this disagreement leaves no
    Φ trace.

H2: The rider node R is in the major-complex core under the platform commit account but absent
    from the driver suggestion account's core, giving core_jaccard < 1.
    H2-null: core membership is identical across the two accounts, so the disagreement is purely
    about magnitude and not about who is bound in.

Method: encode two rule sets for the gig_false_dyad setting over labels (D, P, R) =
(Driver, Platform, Rider). The driver suggestion account makes the platform track the driver
only, leaving the rider unbound (a one-way dyad). The platform commit account binds the driver
and the rider through the platform (a false triad, the worker-system-counterpart shape). Run the
q183 bridge `spread(A, B, labels)` on the pair. The instrument control is the faithful triad
`[x1, x0&x2, x1]` reading 'triadic' max_phi 2.0. A consensus control, where both parties narrate
the same commit account, is expected to give zero spread. Synthetic accounts.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q184_gig_dispatch_spread.probe_gig_dispatch_spread
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.qualitative.disagreement_phi import spread

# Seed all RNG for determinism (the spread is exact; this guards any sampled path).
np.random.default_rng(0)

# Instrument-control labels for the faithful triad.
TRIAD_LABELS = ("W", "S", "C")
FAITHFUL_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Gig dispatch labels: Driver, Platform, Rider.
LABELS = ("D", "P", "R")

# Platform commit account: the platform commits the driver-rider match. P binds D and R, and the
# driver and rider each track the platform. This is the worker-system-counterpart (false) triad.
PLATFORM_COMMIT = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# Driver suggestion account: dispatch is a one-way suggestion. The platform tracks the driver
# only; the rider is not bound into the loop. A dyadic rewrite that drops R from the core.
DRIVER_SUGGEST = [lambda x: x[1], lambda x: x[0], lambda x: x[1]]


def main():
    # ---- INSTRUMENT CONTROL ---------------------------------------------------------------
    v = verdict(FAITHFUL_TRIAD, TRIAD_LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < 1e-9, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- CONSENSUS CONTROL: both parties narrate the same commit account ------------------
    s_consensus = spread(PLATFORM_COMMIT, PLATFORM_COMMIT, LABELS)
    print("CONSENSUS control  both parties narrate the same commit account")
    print(f"  verdict_agreement = {s_consensus['verdict_agreement']}")
    print(f"  phi_gap           = {s_consensus['phi_gap']:.6f}")
    print(f"  core_jaccard      = {s_consensus['core_jaccard']:.6f}")
    print(f"  both_verdicts     = {s_consensus['both_verdicts']}")
    consensus_zero = (
        s_consensus["verdict_agreement"] == 1
        and abs(s_consensus["phi_gap"]) < 1e-9
        and abs(s_consensus["core_jaccard"] - 1.0) < 1e-9
    )
    print(f"  consensus gives zero spread: {consensus_zero}")
    print()

    # ---- REAL RESULT: driver suggestion vs platform commit --------------------------------
    s = spread(DRIVER_SUGGEST, PLATFORM_COMMIT, LABELS)
    vD = verdict(DRIVER_SUGGEST, LABELS)
    vP = verdict(PLATFORM_COMMIT, LABELS)
    coreD, phiD = major_complex(DRIVER_SUGGEST, LABELS)
    coreP, phiP = major_complex(PLATFORM_COMMIT, LABELS)
    coreD = set(coreD) if coreD is not None else set()
    coreP = set(coreP) if coreP is not None else set()

    print("Gig dispatch  driver suggestion account (A) vs platform commit account (B)")
    print(f"{'account':<22}{'structure':>12}{'max_phi':>12}   core")
    print(f"{'A=driver suggestion':<22}{vD.structure:>12}{vD.max_phi:>12.6f}   {sorted(coreD)}")
    print(f"{'B=platform commit':<22}{vP.structure:>12}{vP.max_phi:>12.6f}   {sorted(coreP)}")
    print()
    print("Spread")
    print(f"  verdict_agreement = {s['verdict_agreement']}")
    print(f"  phi_gap           = {s['phi_gap']:.6f}")
    print(f"  core_jaccard      = {s['core_jaccard']:.6f}")
    print(f"  both_verdicts     = {s['both_verdicts']}")
    print()

    # ---- H1: dyad-vs-triad split, phi_gap equals the platform account's Φ ------------------
    h1_ok = (
        vD.structure != "triadic"
        and vP.structure == "triadic"
        and s["verdict_agreement"] == 0
        and abs(s["phi_gap"] - float(vP.max_phi)) < 1e-9
    )

    # ---- H2: rider R in the platform core, absent from the driver core ---------------------
    rider_in_platform = "R" in coreP
    rider_in_driver = "R" in coreD
    h2_ok = rider_in_platform and (not rider_in_driver) and (s["core_jaccard"] < 1.0)

    print(f"H1 driver-dyad vs platform-triad split, phi_gap = platform Φ ({vP.max_phi:.6f}): "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 rider bound in the platform core but not the driver core (core_jaccard<1): "
          f"{'SUPPORTED' if h2_ok else 'REFUTED'}")


if __name__ == "__main__":
    main()
