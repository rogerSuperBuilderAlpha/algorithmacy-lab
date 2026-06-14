"""Q11 / H3 — distributing the parity flip around a ring breaks the decaying law.

Hypothesis (H3): distributing the parity flip around a ring (per-node NOT of the left
neighbor, no shared hub) breaks the parity hub's decaying law Phi=2^(2-n); the rotating-flip
ring stays bounded away from the parity floor where the hub has already fallen below it.

Form / ensemble (methods.md). flip_ring(n): node i is the logical NOT of its left neighbor
(i-1)%n, a traveling flip with synchronous period 2n, for n=3,4,5,6. The reference is
parity_hub(n) from probe_parity_scaling.py (node 0 = XOR of all parties; node i>0 reads node 0),
whose law is Phi=2^(2-n), read at matched n. Labels are tuple(f"x{i}" for i in range(n)).

Measure. The sequence Phi_flip = [Phi_MIP(3), Phi_MIP(4), Phi_MIP(5), Phi_MIP(6)] read by
major_complex(flip_ring(n), labels); its law_class; at each n the gap Phi_flip(n) - 2^(2-n)
against the parity-hub floor; the step ratio Phi_flip(n+1)/Phi_flip(n); and the synchronous
attractor period period(flip_ring(n)) = 2n.

Controls. Instrument control (run first, abort on failure): the strict-mediation conjunctive
triad single_hub(3) must read triadic at Phi=2.0; and parity_hub(5) must reproduce its #115
decay-floor reading, triadic with the full core at Phi=2^(2-5)=0.125. The parity_hub curve at
matched n is the decay baseline. flip_ring and parity_hub are matched on the per-node flip rule
and node count, differing only in topology (distributed ring vs shared hub).

Decision rule (fixed before run). H3 CONFIRMED if at n=5 and n=6 Phi_flip(n) > 2^(2-n)+1e-6
AND the sequence does not halve each step (law_class not 'decay', or the step ratio stays above
0.5+tolerance). H3 REFUTED if Phi_flip(n) tracks 2^(2-n) within 1e-6 at n=5,6, halving toward
the same floor.

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q11_oscillatory_scaling/probe_probe_q11_flip_ring_decay.py
"""

import csv
import os
import sys

# Repo root on sys.path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi

from org_frontier.probes.lib import major_complex, verdict
from org_frontier.probes.probe_parity_scaling import parity_hub
from org_frontier.probes.probe_distributed_mediators import single_hub
from org_frontier.classifier.classifier import tpm_from_rules

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

NS = (3, 4, 5, 6)
RATIO_TOL = 1e-6


def labels(n):
    return tuple(f"x{i}" for i in range(n))


def flip_ring(n):
    """Node i is the logical NOT of its left neighbor (i-1)%n. Traveling flip, period 2n."""
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(1 - x[a]))
    return rules


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
    """Name the law class of seq = [Phi(3), Phi(4), Phi(5), Phi(6)] (from probe_scaling_zoo)."""
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


def parity_floor(n):
    return 2.0 ** (2 - n)


def instrument_control():
    """Strict-mediation conjunctive triad single_hub(3) must read triadic at Phi=2.0.
    parity_hub(5) must reproduce its #115 decay floor: triadic, full core, Phi=0.125."""
    print("INSTRUMENT CONTROL")
    print("=" * 72)

    vc = verdict(single_hub(3), labels(3))
    ok_triad = vc.structure == "triadic" and abs(vc.max_phi - 2.0) <= 1e-6
    print(f"  strict-mediation triad single_hub(3): structure={vc.structure}  "
          f"max_phi={vc.max_phi:.6f}  (require triadic, Phi=2.0)")

    core5, phi5 = major_complex(parity_hub(5), labels(5))
    sz5 = len(core5) if core5 else 0
    v5 = "triadic" if phi5 > 1e-6 else "dyadic"
    ok_parity = v5 == "triadic" and sz5 == 5 and abs(phi5 - 0.125) <= 1e-6
    print(f"  parity_hub(5): verdict={v5}  max_phi_MIP={phi5:.6f}  core_size={sz5}  "
          f"(require triadic, full core n=5, Phi=2^(2-5)=0.125)")

    passed = ok_triad and ok_parity
    print(f"  control passed: {passed}")
    print("=" * 72)
    if not passed:
        sys.exit("ABORT: instrument control failed; Q11 H3 values not trusted.")


def run():
    instrument_control()

    print()
    print("H3 — flip_ring (distributed parity ring) vs parity_hub decay floor 2^(2-n)")
    print("=" * 72)
    header = (f"  {'n':<4}{'period':<9}{'core':<7}{'Phi_flip':<12}"
              f"{'floor 2^(2-n)':<15}{'gap':<14}{'Phi_hub':<10}")
    print(header)

    phi_flip = {}
    phi_hub = {}
    core_flip = {}
    per = {}
    rows = []
    for n in NS:
        lab = labels(n)
        cf, pf = major_complex(flip_ring(n), lab)
        ch, ph = major_complex(parity_hub(n), lab)
        p = period(flip_ring(n), n)
        phi_flip[n] = pf
        phi_hub[n] = ph
        core_flip[n] = len(cf) if cf else 0
        per[n] = p
        floor = parity_floor(n)
        gap = pf - floor
        print(f"  {n:<4}{p:<9}{core_flip[n]:<7}{pf:<12.6f}"
              f"{floor:<15.6f}{gap:<14.6f}{ph:<10.6f}")
        rows.append({
            "n": n,
            "period_flip": p,
            "core_size_flip": core_flip[n],
            "phi_flip": f"{pf:.6f}",
            "parity_floor": f"{floor:.6f}",
            "gap_flip_minus_floor": f"{gap:.6f}",
            "phi_parity_hub": f"{ph:.6f}",
        })

    seq = [phi_flip[n] for n in NS]
    lc = law_class(seq)

    print("=" * 72)
    print(f"  Phi_flip sequence [n=3,4,5,6] = {[round(v, 6) for v in seq]}")
    print(f"  law_class(Phi_flip)          = {lc}")
    print(f"  Phi_hub  sequence [n=3,4,5,6] = {[round(phi_hub[n], 6) for n in NS]}")
    print(f"  floor 2^(2-n)    [n=3,4,5,6] = {[round(parity_floor(n), 6) for n in NS]}")

    ratios = {}
    print("  step ratios Phi_flip(n+1)/Phi_flip(n):")
    for n in NS[:-1]:
        r = phi_flip[n + 1] / phi_flip[n] if phi_flip[n] != 0 else float("inf")
        ratios[n] = r
        print(f"    n={n}->{n + 1}: {r:.6f}")

    print("  gaps Phi_flip(n) - 2^(2-n):")
    for n in NS:
        print(f"    n={n}: {phi_flip[n] - parity_floor(n):.6f}")

    # Decision rule (fixed before run).
    above_floor_56 = all(phi_flip[n] > parity_floor(n) + 1e-6 for n in (5, 6))
    not_decay = lc != "decay"
    ratios_hold = all(ratios[n] > 0.5 + RATIO_TOL for n in NS[:-1])
    not_halving = not_decay or ratios_hold

    tracks_floor_56 = all(abs(phi_flip[n] - parity_floor(n)) <= 1e-6 for n in (5, 6))

    if above_floor_56 and not_halving:
        verdict_str = "confirmed"
    elif tracks_floor_56:
        verdict_str = "refuted"
    else:
        verdict_str = "partial"

    print("=" * 72)
    print("DECISION (fixed before run):")
    print(f"  Phi_flip(5)>floor+1e-6 and Phi_flip(6)>floor+1e-6 : {above_floor_56}")
    print(f"  law_class != 'decay'                              : {not_decay}")
    print(f"  all step ratios > 0.5+tol                         : {ratios_hold}")
    print(f"  does not halve each step (not_decay OR ratios)    : {not_halving}")
    print(f"  tracks floor within 1e-6 at n=5,6 (refute branch) : {tracks_floor_56}")
    print(f"  VERDICT: {verdict_str.upper()}")
    print("=" * 72)

    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q11_flip_ring_decay.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"  wrote {csv_path}")

    return verdict_str


if __name__ == "__main__":
    run()
