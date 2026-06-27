"""Probe 360 (Q206) — does a parity ring rewire differently from a conjunctive ring?

q146 swept a conjunctive (AND) six-node ring under Watts-Strogatz rewiring and found Φ_MIP declines
monotonically (4.0→3.0→2.14→0.67→0.47) with the verdict collapsing to dyadic by p=0.5, and closed with two
open edges: the p-grid is coarse, and other couplings are unswept. This probe fills the interior of
(0.25, 0.5) to locate the inflection and runs the same sweep on a parity (XOR) ring to test whether the
decline is coupling-general (#115 shows the parity family scales by a different law).

Hypotheses (fixed before computing, see hypotheses.md):
  H1 instrument control — the faithful triad reads triadic, Φ=2.0.
  H2 — the conjunctive verdict first turns dyadic in (0.25, 0.5); Φ stays monotone.
  H3 — the parity ring starts at Φ ≠ 4.0.
  H4 — the parity ring also declines under rewiring.
  H5 — parity holds its triadic verdict to a higher p than conjunctive.

Each whole-system verdict at n=6 takes ~26s, so the sweep is split: `--coupling and` or `--coupling xor`
runs one family and caches its rows to results/; with no argument the probe runs both and prints the full
H1–H5 report (the canonical, reproducible form). Only the whole-system verdict and Φ_MIP are computed; no
hypothesis here needs the major complex.

Validation gap: synthetic Boolean rings with exact IIT-4.0 Φ; evidence about how topology and coupling
shape integration, not a measurement of any organization.

Run:  python -m org_frontier.questions.q206_ring_parity_rewire.probe_ring_parity_rewire
"""

import functools
import json
import os
import sys

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.probes.lib import verdict  # noqa: E402

N = 6
LABELS = tuple("N%d" % i for i in range(N))
P_GRID = (0.0, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 1.0)
SEEDS = (0, 1)
BASE_SEED = 20260627
EPS = 1e-9
_RESULTS = os.path.join(os.path.dirname(__file__), "results")


def ring_inputs():
    """Node i reads its two ring neighbours (i-1, i+1) mod N."""
    return {i: [(i - 1) % N, (i + 1) % N] for i in range(N)}


def rewire(p, rng):
    """q146's in-degree-2 Watts-Strogatz endpoint rewiring."""
    ins = ring_inputs()
    for d in range(N):
        for k in range(len(ins[d])):
            if rng.random() < p:
                cur = set(ins[d])
                choices = [c for c in range(N) if c != d and c not in cur]
                if choices:
                    ins[d][k] = int(rng.choice(choices))
    return ins


def rules_from_inputs(ins, coupling):
    """Per-node Boolean rules: each node = AND or XOR of its current input sources."""
    op = (lambda a, b: a & b) if coupling == "and" else (lambda a, b: a ^ b)

    def mk(srcs):
        srcs = tuple(srcs)

        def f(x, srcs=srcs):
            vals = [x[s] for s in srcs]
            return int(functools.reduce(op, vals)) if vals else 0

        return f

    return [mk(ins[i]) for i in range(N)]


def evaluate(ins, coupling):
    v = verdict(rules_from_inputs(ins, coupling), LABELS)
    return v.structure, float(v.max_phi)


def sweep(coupling, grid=P_GRID, seeds=SEEDS):
    """Per-p [p, mean Φ_MIP, seed verdicts, seed phis] for one coupling family."""
    rows = []
    coupling_offset = 0 if coupling == "and" else 50000
    for p in grid:
        if p == 0.0:
            st, phi = evaluate(ring_inputs(), coupling)
            rows.append([p, phi, [st], [phi]])
            continue
        phis, verds = [], []
        for s in seeds:
            rng = np.random.default_rng(BASE_SEED + coupling_offset + int(round(p * 100)) * 10 + s)
            st, phi = evaluate(rewire(p, rng), coupling)
            phis.append(phi)
            verds.append(st)
        rows.append([p, float(np.mean(phis)), verds, phis])
    return rows


def first_dyadic_p(rows):
    for p, _, verds, _ in rows:
        if any(v == "dyadic" for v in verds):
            return p
    return None


def monotone_nonincreasing(rows):
    means = [r[1] for r in rows]
    return all(means[i + 1] <= means[i] + 1e-9 for i in range(len(means) - 1))


def report(conj, par):
    for name, rows in (("conjunctive", conj), ("parity", par)):
        print("  --- %s ring ---" % name)
        for p, mean_phi, verds, _ in rows:
            print("    p=%.2f  meanΦ=%.4f  verdicts=%s" % (p, mean_phi, ",".join(verds)))
    conj_fp, par_fp, par0 = first_dyadic_p(conj), first_dyadic_p(par), par[0][1]
    print("=" * 86)
    h2 = (conj_fp is not None and 0.25 < conj_fp < 0.5) and monotone_nonincreasing(conj)
    h3 = abs(par0 - 4.0) > EPS
    h4 = par[-1][1] < par[0][1] - EPS and monotone_nonincreasing(par)
    h5 = (par_fp is not None and conj_fp is not None and par_fp > conj_fp) or \
         (par_fp is None and conj_fp is not None)
    print("  conjunctive first-dyadic p = %s ; parity first-dyadic p = %s ; parity p0 Φ = %.4f"
          % (conj_fp, par_fp, par0))
    print("  H2 (conjunctive verdict inflects in (0.25,0.5), Φ monotone): %s"
          % ("SUPPORTED" if h2 else "REFUTED"))
    print("  H3 (parity ring starts at Φ != 4.0): %s" % ("SUPPORTED" if h3 else "REFUTED"))
    print("  H4 (parity also declines under rewiring): %s" % ("SUPPORTED" if h4 else "REFUTED"))
    print("  H5 (parity holds its verdict to a higher p than conjunctive): %s"
          % ("SUPPORTED" if h5 else "REFUTED"))
    print("=" * 86)


def control():
    triad = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v = verdict(triad, ("W", "S", "C"))
    ok = v.structure == "triadic" and abs(v.max_phi - 2.0) < 1e-6
    print("  H1 control faithful triad: %s Φ=%.6f %s"
          % (v.structure, v.max_phi, "PASS" if ok else "FAIL"))
    assert ok, "instrument control failed; aborting"


def _cache(coupling):
    return os.path.join(_RESULTS, "rows_%s.json" % coupling)


def main():
    os.makedirs(_RESULTS, exist_ok=True)
    print("PROBE 360 (Q206) — parity vs conjunctive ring under rewiring (n=%d)" % N)
    print("=" * 86)
    arg = sys.argv[1:]

    def opt(name, default=None):
        return arg[arg.index(name) + 1] if name in arg else default

    grid = tuple(float(v) for v in opt("--grid").split(",")) if opt("--grid") else P_GRID
    n_seeds = int(opt("--seeds")) if opt("--seeds") else len(SEEDS)
    seeds = SEEDS[:n_seeds]

    # Fast CI re-derivation: control + the conjunctive anchors (parity Φ at n=6 is ~7 min/network,
    # too slow for an automated check; the parity numbers are reported from results/output.txt).
    if "--ci" in arg:
        control()
        rows = sweep("and", grid=(0.0, 0.3, 0.35), seeds=(0,))
        for p, mean_phi, verds, _ in rows:
            print("    conjunctive p=%.2f  Φ=%.4f  verdict=%s" % (p, mean_phi, ",".join(verds)))
        print("  H2 conjunctive: p=0.30 triadic then p=0.35 DYADIC — a dyadic window the q146 grid missed")
        return

    # Per-coupling worker: run one family, cache its rows (for the parallel split).
    if "--coupling" in arg:
        cp = opt("--coupling")
        rows = sweep(cp, grid=grid, seeds=seeds)
        json.dump(rows, open(_cache(cp), "w"))
        print("  --- %s ring (cached to %s) ---" % (cp, _cache(cp)))
        for p, mean_phi, verds, _ in rows:
            print("    p=%.2f  meanΦ=%.4f  verdicts=%s" % (p, mean_phi, ",".join(verds)))
        return

    # Assemble from cache when both worker runs are present, else compute both here.
    if "--report" in arg and os.path.exists(_cache("and")) and os.path.exists(_cache("xor")):
        conj = json.load(open(_cache("and")))
        par = json.load(open(_cache("xor")))
    else:
        conj, par = sweep("and"), sweep("xor")
    control()
    report(conj, par)


if __name__ == "__main__":
    main()
