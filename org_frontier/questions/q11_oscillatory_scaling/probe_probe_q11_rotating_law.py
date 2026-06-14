r"""Q11 H1 — the rotating-update ring carries a Phi(n) law distinct from the capped fixed-point ring.

H1: rot_ring(n) (pure cyclic shift, node i copies left neighbor (i-1)%n) is a traveling wave of
synchronous attractor period n. Against the zoo's capped AND-neighbor ring and_ring(n) (#132,
Phi=4 for n>=4, period <=2), the rotating ring should trace a fifth Phi(n) shape rather than
reproduce the cap.

Form/ensemble:
  rot_ring(n) for n=3,4,5,6 (the cycler under test).
  and_ring(n) for matched n=4,5,6 (the capped-family baseline / negative control).
Measure: exact IIT-4.0 max Phi_MIP over reachable states at grain 1 via major_complex; the
sequence [Phi(3),Phi(4),Phi(5),Phi(6)] and its law_class; per-n gap Phi_rot(n)-Phi_and(n) at
n=4,5,6; synchronous period (period helper) certifying rot_ring cycles (period n) while and_ring
collapses (period <= 2).

Controls (run first, required before any Q11 value is trusted):
  - strict-mediation triad (W'=S, S'=W&C, C'=S) reads triadic at Phi=2.0 (instrument sanity).
  - and_ring(3) = 6.0 and and_ring(4) = 4.0, both triadic full core, period <= 2 (#132 anchor).

Decision rule (fixed before run):
  CONFIRM H1 if Phi_rot(n) != 4 at some n>=4 by > 1e-6, OR Phi_rot(n) != Phi_and(n) at some
  matched n in {4,5,6} by > 1e-6 (the two curves are separable over n=3..6).
  REFUTE if Phi_rot(n) = Phi_and(n) within 1e-6 at every matched n=4,5,6 AND Phi_rot reproduces
  the capped Phi=4 (Phi=2 at n=3) constant.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q11_oscillatory_scaling/probe_probe_q11_rotating_law.py \
        2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import csv
import os
import sys

# --- Repo root on sys.path so org_frontier.* and proxy_audit.* import, and the module runs as a
# --- direct script. The probe sits three levels below the repo root.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.probes.lib import major_complex, verdict

TOL = 1e-6
_RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# ----- The forms (exact rules from methods.md) -----------------------------------------------

def rot_ring(n):
    """Pure cyclic shift: node i copies its left neighbor (i-1)%n. Period-n traveling wave."""
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules


def and_ring(n):
    """The zoo's capped fixed-point ring (#132): node i = AND of its two ring neighbors."""
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


def strict_mediation_triad():
    """Instrument-control anchor: W'=S, S'=W&C, C'=S; labels (W,S,C). Reads triadic at Phi=2.0."""
    return [lambda x: int(x[1]), lambda x: int(x[0] & x[2]), lambda x: int(x[1])]


# ----- Helpers -------------------------------------------------------------------------------

def labels_for(n):
    return tuple(f"x{i}" for i in range(n))


def period(rules, n):
    """Longest synchronous attractor cycle length over all 2^n initial states."""
    tpm = tpm_from_rules(rules)
    nxt = lambda s: sum(int(tpm[s, j]) << j for j in range(n))
    mp = 1
    for s0 in range(2 ** n):
        seen = {}
        s = s0
        t = 0
        while s not in seen:
            seen[s] = t
            s = nxt(s)
            t += 1
        mp = max(mp, t - seen[s])
    return mp


def law_class(seq):
    """Name a sequence [Phi(3),Phi(4),Phi(5),Phi(6)] per probe_scaling_zoo.law_class."""
    a, b, c, d = seq
    if max(seq) - min(seq) < 1e-6:
        return "constant"
    if d < a:
        return "decay"
    d1 = [seq[i + 1] - seq[i] for i in range(3)]
    d2 = [d1[i + 1] - d1[i] for i in range(2)]
    if all(abs(x) < 1e-6 for x in d2):
        return "linear"
    return "super-linear"


# ----- Instrument control (run first; abort if it fails) -------------------------------------

def run_instrument_control():
    print("INSTRUMENT CONTROL (must pass before any Q11 value is trusted)")
    print("-" * 70)

    # (1) strict-mediation triad reads triadic at Phi=2.0
    core, phi = major_complex(strict_mediation_triad(), ("W", "S", "C"))
    v = verdict(strict_mediation_triad(), ("W", "S", "C"))
    ok_triad = (v.structure == "triadic") and abs(phi - 2.0) <= TOL
    print(f"  strict-mediation triad: verdict={v.structure}, Phi_MIP={phi:.6f}, core={core}")
    print(f"    required: triadic, Phi=2.0 -> {'PASS' if ok_triad else 'FAIL'}")
    if not ok_triad:
        raise SystemExit("ABORT: strict-mediation triad control failed; instrument mis-wired.")

    # (2) and_ring #132 anchors: n=3 -> 6.0, n=4 -> 4.0, both triadic full core, period <= 2
    anchors = []
    for n, req in ((3, 6.0), (4, 4.0)):
        lab = labels_for(n)
        core, phi = major_complex(and_ring(n), lab)
        v = verdict(and_ring(n), lab)
        per = period(and_ring(n), n)
        full = (core is not None and len(core) == n)
        ok = (v.structure == "triadic") and abs(phi - req) <= TOL and full and per <= 2
        anchors.append(ok)
        print(f"  and_ring(n={n}): verdict={v.structure}, Phi_MIP={phi:.6f}, "
              f"core_size={len(core) if core else 0}/{n}, period={per}")
        print(f"    required: triadic, Phi={req}, full core, period<=2 -> {'PASS' if ok else 'FAIL'}")
    if not all(anchors):
        raise SystemExit("ABORT: and_ring #132 anchor control failed; no Q11 comparison is trusted.")

    print("-" * 70)
    print("  Instrument control PASSED.\n")


# ----- The H1 test ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Q11 H1 — rotating ring as a fifth Phi(n) law (distinct from the capped Phi=4)")
    print("=" * 70)

    run_instrument_control()

    # rot_ring sequence over n=3,4,5,6
    print("ROT_RING (cycler under test): Phi_MIP over reachable states at grain 1")
    print("-" * 70)
    rot_rows = []
    phi_rot = {}
    for n in (3, 4, 5, 6):
        lab = labels_for(n)
        core, phi = major_complex(rot_ring(n), lab)
        v = verdict(rot_ring(n), lab)
        per = period(rot_ring(n), n)
        phi_rot[n] = phi
        rot_rows.append((n, phi, v.structure, len(core) if core else 0, per))
        print(f"  rot_ring(n={n}): Phi_MIP={phi:.6f}, verdict={v.structure}, "
              f"core_size={len(core) if core else 0}/{n}, period={per} (expect period=={n})")

    seq_rot = [phi_rot[n] for n in (3, 4, 5, 6)]
    lc_rot = law_class(seq_rot)
    print(f"\n  Phi_rot sequence [n=3,4,5,6] = {[round(x,6) for x in seq_rot]}")
    print(f"  law_class(Phi_rot)            = {lc_rot}")

    # and_ring matched baseline at n=4,5,6
    print("\nAND_RING (capped-family baseline): matched n=4,5,6")
    print("-" * 70)
    phi_and = {}
    and_rows = []
    for n in (4, 5, 6):
        lab = labels_for(n)
        core, phi = major_complex(and_ring(n), lab)
        per = period(and_ring(n), n)
        phi_and[n] = phi
        and_rows.append((n, phi, len(core) if core else 0, per))
        print(f"  and_ring(n={n}): Phi_MIP={phi:.6f}, core_size={len(core) if core else 0}/{n}, "
              f"period={per}")

    # per-n gap Phi_rot - Phi_and at matched n=4,5,6
    print("\nHEAD-TO-HEAD gap Phi_rot(n) - Phi_and(n) at matched n=4,5,6")
    print("-" * 70)
    gaps = {}
    for n in (4, 5, 6):
        g = phi_rot[n] - phi_and[n]
        gaps[n] = g
        print(f"  n={n}: Phi_rot={phi_rot[n]:.6f}  Phi_and={phi_and[n]:.6f}  gap={g:+.6f}")

    # ----- Decision rule (fixed before run) -----
    cap_break = any(abs(phi_rot[n] - 4.0) > TOL for n in (4, 5, 6))
    curve_split = any(abs(gaps[n]) > TOL for n in (4, 5, 6))
    confirm = cap_break or curve_split

    # refute branch (for explicit reporting): rot==and at every matched n AND rot reproduces cap
    rot_equals_and = all(abs(gaps[n]) <= TOL for n in (4, 5, 6))
    rot_reproduces_cap = (all(abs(phi_rot[n] - 4.0) <= TOL for n in (4, 5, 6))
                          and abs(phi_rot[3] - 2.0) <= TOL)
    refute = rot_equals_and and rot_reproduces_cap

    verdict_str = "CONFIRMED" if confirm else ("REFUTED" if refute else "PARTIAL")

    print("\n" + "=" * 70)
    print("DECISION")
    print("=" * 70)
    print(f"  Phi_rot(n)!=4 at some n>=4 by >1e-6 : {cap_break}")
    print(f"  Phi_rot(n)!=Phi_and(n) at some matched n by >1e-6 : {curve_split}")
    print(f"  (refute branch) rot==and at all matched n AND rot reproduces cap : {refute}")
    print(f"  VERDICT: H1 {verdict_str}")
    print("=" * 70)

    # ----- write CSV -----
    os.makedirs(_RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(_RESULTS_DIR, "q11_rotating_law.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "n", "phi_mip", "verdict", "core_size", "period",
                    "phi_and_matched", "gap_rot_minus_and"])
        for n, phi, vstr, cs, per in rot_rows:
            ga = f"{gaps[n]:.6f}" if n in gaps else ""
            an = f"{phi_and[n]:.6f}" if n in phi_and else ""
            w.writerow(["rot_ring", n, f"{phi:.6f}", vstr, cs, per, an, ga])
        for n, phi, cs, per in and_rows:
            w.writerow(["and_ring", n, f"{phi:.6f}", "triadic", cs, per, "", ""])
        w.writerow([])
        w.writerow(["law_class_rot", lc_rot])
        w.writerow(["verdict", verdict_str])
    print(f"\n  CSV written: {csv_path}")

    return verdict_str


if __name__ == "__main__":
    main()
