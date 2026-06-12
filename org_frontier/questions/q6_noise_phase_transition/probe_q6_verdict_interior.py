"""Q6 / H3 — the dyadic/triadic verdict flips only at the degenerate endpoint p=0.5.

Hypothesis (H3): the noisy conjunctive mediated chain reads triadic at every interior grid
point p in {0.01, ..., 0.49} and reads dyadic only at the random-commit endpoint p=0.5; no
finite interior critical p* exists where the triad factors below the degenerate maximum.

Form and noise model (methods.md, fixed for every Q6 test). n=3, labels ("W","S","C"). Clean
rules W'=S, S'=W&C, C'=S (#26/#33/#27). Commit noise p is output noise on the mediator column
of the state-by-node TPM: the clean S' column value s_clean in {0,1} per row is replaced by
P(S'=1) = (1-p)*s_clean + p*(1-s_clean). The W and C columns stay deterministic. The
connectivity matrix is the clean form's cm_from_rules(...).

Measure. structure(p) over the 51-point grid p=0.00..0.50 (step 0.01) via classify(noisy_tpm(p),
cm) with PHI_EPS=1e-9; the smallest p reading dyadic (Phi_MIP <= PHI_EPS); whether it is p=0.5
or an interior point; and whether the major complex stays the full triad {W,S,C} up to it.

Instrument control (run first, abort on failure). The clean form at p=0 must reproduce triadic,
max_phi=2.0 (to 1e-6), MIP "2 parts: {W,SC}".

Decision rule (fixed before run). H3 confirmed if structure(p)=triadic for every interior grid
point and dyadic only at p=0.5. H3 refuted if any interior grid point reads dyadic.

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q6_noise_phase_transition/probe_q6_verdict_interior.py
"""

import csv
import os
import sys

# Repo root on sys.path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np
import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from foundations.proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

LABELS = ("W", "S", "C")
# Clean rules: W'=S, S'=W&C, C'=S  (little-endian state tuple x = (W, S, C)).
CLEAN_RULES = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# The fixed 51-point grid p = 0.00, 0.01, ..., 0.50.
GRID = [round(k * 0.01, 2) for k in range(51)]


def noisy_tpm(p):
    """State-by-node TPM of the conjunctive chain with commit noise p on the mediator column.

    The clean mediator column s_clean in {0,1} per row becomes P(S'=1) = (1-p)*s_clean +
    p*(1-s_clean). W and C columns stay deterministic at their clean values.
    """
    clean = tpm_from_rules(CLEAN_RULES, n=3)
    tpm = clean.copy()
    s_clean = clean[:, 1]
    tpm[:, 1] = (1.0 - p) * s_clean + p * (1.0 - s_clean)
    return tpm


# Clean connectivity matrix (noise rescales transition probabilities, it adds/removes no edge).
CM = cm_from_rules(CLEAN_RULES, n=3)


def major_complex_on_tpm(tpm_sbn, cm, labels):
    """(core_label_tuple, phi) of the maximal complex over reachable states of a (stochastic) TPM.

    The same most-integrated-state machinery the classifier reads its verdict at, applied here
    to the noisy TPM so the major complex tracks the noisy form."""
    n = cm.shape[0]
    net = pyphi.Network(tpm_sbn, cm=cm, node_labels=labels[:n])
    best = (None, -1.0)
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        # maximal_complex returns NullPhiStructure (no node_indices) when nothing is
        # irreducible at this state; skip those, they carry no complex.
        node_indices = getattr(mc, "node_indices", None)
        if node_indices is None:
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in node_indices), float(mc.phi))
    return best


def instrument_control():
    """Clean form at p=0 must read triadic, max_phi=2.0 (to 1e-6), MIP '2 parts: {W,SC}'."""
    v = classify_rules(CLEAN_RULES, labels=LABELS)
    ok_struct = v.structure == "triadic"
    ok_phi = abs(v.max_phi - 2.0) <= 1e-6
    ok_mip = "{W,SC}" in v.mip_partition.replace(" ", "")
    # The p=0 endpoint of the noisy sweep is the same reference value.
    v0 = classify(noisy_tpm(0.0), CM, labels=LABELS)
    ok_sweep0 = v0.structure == "triadic" and abs(v0.max_phi - 2.0) <= 1e-6
    print("INSTRUMENT CONTROL (clean form, p=0)")
    print(f"  classify_rules: structure={v.structure}  max_phi={v.max_phi:.6f}  "
          f"MIP={v.mip_partition!r}")
    print(f"  sweep p=0      : structure={v0.structure}  max_phi={v0.max_phi:.6f}  "
          f"MIP={v0.mip_partition!r}")
    passed = ok_struct and ok_phi and ok_mip and ok_sweep0
    print(f"  control passed: {passed}")
    print("=" * 72)
    if not passed:
        sys.exit("ABORT: instrument control failed; swept values not trusted.")


def main():
    instrument_control()

    rows = []
    structures = {}
    print("Q6 / H3 — verdict across the 51-point commit-noise grid")
    print("=" * 72)
    print(f"  PHI_EPS = {PHI_EPS:g}")
    print(f"  {'p':>5}  {'Phi_MIP':>10}  {'structure':>9}  {'MIP':>14}  major_complex")
    for p in GRID:
        tpm = noisy_tpm(p)
        v = classify(tpm, CM, labels=LABELS, eps=PHI_EPS)
        core, mc_phi = major_complex_on_tpm(tpm, CM, LABELS)
        core_str = "{" + ",".join(core) + "}" if core is not None else "(none)"
        structures[p] = v.structure
        rows.append({
            "p": p,
            "phi_mip": round(v.max_phi, 6),
            "structure": v.structure,
            "mip_partition": v.mip_partition,
            "major_complex": core_str,
            "major_complex_phi": round(mc_phi, 6),
        })
        print(f"  {p:>5.2f}  {v.max_phi:>10.6f}  {v.structure:>9}  "
              f"{v.mip_partition:>14}  {core_str} (phi={mc_phi:.4f})")
    print("=" * 72)

    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q6_verdict_interior.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    interior = [p for p in GRID if 0.0 < p < 0.5]
    dyadic_ps = [p for p in GRID if structures[p] == "dyadic"]
    first_dyadic = min(dyadic_ps) if dyadic_ps else None
    interior_dyadic = [p for p in interior if structures[p] == "dyadic"]

    full_triad = "{W,S,C}"
    triad_until = []
    for p in GRID:
        if structures[p] != "triadic":
            break
        triad_until.append(p)
    mc_full_triad_through_triadic = all(
        r["major_complex"] == full_triad for r in rows if r["structure"] == "triadic"
    )

    n_triadic_interior = sum(1 for p in interior if structures[p] == "triadic")

    print("RESULT")
    print(f"  interior grid points (0.01..0.49): {len(interior)}")
    print(f"  triadic interior points: {n_triadic_interior} / {len(interior)}")
    print(f"  interior points reading dyadic: {interior_dyadic}")
    print(f"  smallest p reading dyadic: {first_dyadic}")
    print(f"  first dyadic is endpoint p=0.5: {first_dyadic == 0.5}")
    print(f"  major complex stays full {full_triad} through all triadic points: "
          f"{mc_full_triad_through_triadic}")

    confirmed = (
        all(structures[p] == "triadic" for p in interior)
        and structures[0.5] == "dyadic"
    )
    if confirmed:
        verdict = "CONFIRMED"
    elif interior_dyadic:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"
    print("=" * 72)
    print(f"  H3 VERDICT: {verdict}")
    print(f"  CSV: {csv_path}")
    return verdict


if __name__ == "__main__":
    main()
