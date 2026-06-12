"""Q7 / H3 — the party verdict-collapse point relative to the degenerate endpoint.

Hypothesis (H3): the party verdict collapses relative to the degenerate endpoint — party
noise drives the triadic->dyadic collapse, tested both on the strict Phi_MIP>PHI_EPS verdict
and on an effective near-zero-Phi threshold, against the mediator site.

Form and noise model (methods.md, fixed for every Q7 test). n=3, labels ("W","S","C"). Clean
rules W'=S, S'=W&C, C'=S (#26/#33/#27). Flip-noise of strength p is output noise on one or
more node columns of the state-by-node TPM: a noised clean column value col_clean in {0,1}
per row is replaced by P(out=1) = (1-p)*col_clean + p*(1-col_clean). The connectivity matrix
is the clean form's cm_from_rules(...) (noise rescales probabilities, it adds/removes no edge).
Sites: mediator S = cols (1,); party W = cols (0,).

Measure (both thresholds fixed before the run). For each site, two collapse points read on
the 51-point grid p=0.00..0.50 (step 0.01) via classify(noisy_tpm(p, cols), CM):
  (a) strict-verdict collapse p_v: smallest grid p at which structure reads dyadic
      (Phi_MIP <= PHI_EPS = 1e-9).
  (b) effective collapse p_eff: smallest grid p at which Phi_MIP < 0.01 (1/200 of clean
      Phi=2.0), a near-zero-integration threshold declared here and applied identically to
      both sites.
Record p_v and p_eff for S and W, and whether the major complex stays the full triad {W,S,C}.

Instrument control (run first, abort on failure). The clean form at p=0 must reproduce
triadic, max_phi=2.0 (to 1e-6), MIP "2 parts: {W,SC}"; and the p=0 endpoint of every site
sweep must read 2.0 triadic.

Decision rule (fixed before run), two registers:
  Strict verdict: CONFIRMED if p_v(W) < p_v(S) (party flips at interior p* < 0.5, strictly
    before the mediator's). REFUTED if p_v(W) = p_v(S) = 0.5 or p_v(W) >= p_v(S).
  Effective collapse (reported alongside, decisive when both strict flips sit at 0.5): party
    collapses earlier if p_eff(W) < p_eff(S) by at least one grid step.
The strict register governs the H3 verdict.

Pre-registration: both sites flip strictly only at p=0.5 (strict register expected to REFUTE),
the asymmetry appears on the effective register with p_eff(W) < p_eff(S).

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q7_party_vs_mediator_noise/probe_verdict_flip.py
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
CLEAN_TPM = tpm_from_rules(CLEAN_RULES, n=3)
# Clean connectivity matrix (noise rescales transition probabilities, it adds/removes no edge).
CM = cm_from_rules(CLEAN_RULES, n=3)

# The fixed 51-point grid p = 0.00, 0.01, ..., 0.50.
GRID = [round(k * 0.01, 2) for k in range(51)]

# Thresholds, both fixed before the run.
# PHI_EPS = 1e-9 is the classifier's standard zero cutoff (imported, not retuned).
PHI_EFF = 0.01          # effective near-zero threshold: 1/200 of clean Phi=2.0
GRID_STEP = 0.01

# Injection sites: column tuples noised at strength p.
SITES = {"S": (1,), "W": (0,)}


def noisy_tpm(p, cols):
    """State-by-node TPM with flip-noise p applied as output noise on each column in cols.

    For a noised column c, the clean value sc in {0,1} per row becomes
    P(out=1) = (1-p)*sc + p*(1-sc): the output lands on its clean value with reliability 1-p
    and flips with probability p. Columns not in cols stay deterministic.
    """
    t = CLEAN_TPM.copy()
    for c in cols:
        sc = CLEAN_TPM[:, c]
        t[:, c] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def major_complex_on_tpm(tpm_sbn, cm, labels):
    """(core_label_tuple, phi) of the maximal complex over reachable states of a (stochastic) TPM.

    The same most-integrated-state machinery the classifier reads its verdict at, applied here
    to the noisy TPM so the major complex tracks the noisy form.
    """
    n = cm.shape[0]
    net = pyphi.Network(tpm_sbn, cm=cm, node_labels=labels[:n])
    best = (None, -1.0)
    for s in reachable_states(tpm_sbn, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        node_indices = getattr(mc, "node_indices", None)
        if node_indices is None:
            continue
        if float(mc.phi) > best[1]:
            best = (tuple(labels[i] for i in node_indices), float(mc.phi))
    return best


def instrument_control():
    """Clean form at p=0 must read triadic, max_phi=2.0 (to 1e-6), MIP '2 parts: {W,SC}';
    and every site's p=0 endpoint must reproduce 2.0 triadic. Abort otherwise."""
    v = classify_rules(CLEAN_RULES, labels=LABELS)
    ok_struct = v.structure == "triadic"
    ok_phi = abs(v.max_phi - 2.0) <= 1e-6
    ok_mip = "{W,SC}" in v.mip_partition.replace(" ", "")
    print("INSTRUMENT CONTROL (clean form, p=0)")
    print(f"  classify_rules: structure={v.structure}  max_phi={v.max_phi:.6f}  "
          f"MIP={v.mip_partition!r}")
    ok_sites = True
    for name, cols in SITES.items():
        v0 = classify(noisy_tpm(0.0, cols), CM, labels=LABELS)
        ok = v0.structure == "triadic" and abs(v0.max_phi - 2.0) <= 1e-6
        ok_sites = ok_sites and ok
        print(f"  sweep {name} p=0 cols={cols}: structure={v0.structure}  "
              f"max_phi={v0.max_phi:.6f}  ok={ok}")
    passed = ok_struct and ok_phi and ok_mip and ok_sites
    print(f"  control passed: {passed}")
    print("=" * 72)
    if not passed:
        sys.exit("ABORT: instrument control failed; swept values not trusted.")


def sweep_site(name, cols):
    """Return (rows, structures, phis) for one site's 51-point sweep, and print the table."""
    rows = []
    structures = {}
    phis = {}
    full_triad = "{W,S,C}"
    print(f"Site {name}  cols={cols}")
    print(f"  {'p':>5}  {'Phi_MIP':>10}  {'structure':>9}  {'MIP':>14}  major_complex")
    for p in GRID:
        tpm = noisy_tpm(p, cols)
        v = classify(tpm, CM, labels=LABELS, eps=PHI_EPS)
        core, mc_phi = major_complex_on_tpm(tpm, CM, LABELS)
        core_str = "{" + ",".join(core) + "}" if core is not None else "(none)"
        structures[p] = v.structure
        phis[p] = v.max_phi
        rows.append({
            "site": name,
            "cols": "".join(str(c) for c in cols),
            "p": p,
            "phi_mip": round(v.max_phi, 6),
            "structure": v.structure,
            "mip_partition": v.mip_partition,
            "major_complex": core_str,
            "major_complex_phi": round(mc_phi, 6),
            "full_triad": core_str == full_triad,
        })
        print(f"  {p:>5.2f}  {v.max_phi:>10.6f}  {v.structure:>9}  "
              f"{v.mip_partition:>14}  {core_str} (phi={mc_phi:.4f})")
    print("-" * 72)
    return rows, structures, phis


def main():
    instrument_control()

    print("Q7 / H3 — party vs mediator verdict-collapse across the 51-point flip-noise grid")
    print("=" * 72)
    print(f"  PHI_EPS = {PHI_EPS:g}   PHI_EFF = {PHI_EFF:g} (1/200 of clean Phi=2.0)")
    print("=" * 72)

    all_rows = []
    structures = {}
    phis = {}
    for name, cols in SITES.items():
        r, st, ph = sweep_site(name, cols)
        all_rows.extend(r)
        structures[name] = st
        phis[name] = ph

    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q7_verdict_flip.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)

    full_triad = "{W,S,C}"

    def first_dyadic(name):
        ds = [p for p in GRID if structures[name][p] == "dyadic"]
        return min(ds) if ds else None

    def first_below_eff(name):
        bs = [p for p in GRID if phis[name][p] < PHI_EFF]
        return min(bs) if bs else None

    def triad_holds_until(name, p_stop):
        """Whether the major complex stays the full triad {W,S,C} up to (and at) p_stop."""
        if p_stop is None:
            chk = GRID
        else:
            chk = [p for p in GRID if p <= p_stop]
        site_rows = {row["p"]: row for row in all_rows if row["site"] == name}
        return all(site_rows[p]["major_complex"] == full_triad for p in chk)

    pv = {name: first_dyadic(name) for name in SITES}
    peff = {name: first_below_eff(name) for name in SITES}

    print("RESULT")
    print(f"  strict-verdict collapse p_v  (smallest p reading dyadic, Phi_MIP<=PHI_EPS):")
    print(f"    p_v(S) = {pv['S']}    p_v(W) = {pv['W']}")
    print(f"  effective collapse p_eff     (smallest p with Phi_MIP < {PHI_EFF}):")
    print(f"    p_eff(S) = {peff['S']}    p_eff(W) = {peff['W']}")
    print(f"  major complex stays full {full_triad} up to p_v(S): "
          f"{triad_holds_until('S', pv['S'])}")
    print(f"  major complex stays full {full_triad} up to p_v(W): "
          f"{triad_holds_until('W', pv['W'])}")
    print("-" * 72)

    # --- Strict register (governs the H3 verdict) ---
    pvW, pvS = pv["W"], pv["S"]
    # Treat "no dyadic on grid" as 0.5+ (never collapses on interior); but on this grid the
    # endpoint p=0.5 is included so collapse, if any, registers there.
    def as_val(x):
        return x if x is not None else float("inf")
    strict_confirmed = (pvW is not None and pvS is not None and as_val(pvW) < as_val(pvS))
    strict_refuted = (
        (pvW == 0.5 and pvS == 0.5)
        or (as_val(pvW) >= as_val(pvS))
    )
    if strict_confirmed:
        strict_verdict = "CONFIRMED"
    elif strict_refuted:
        strict_verdict = "REFUTED"
    else:
        strict_verdict = "PARTIAL"

    # --- Effective register (reported alongside) ---
    peffW, peffS = peff["W"], peff["S"]
    if peffW is not None and peffS is not None:
        eff_earlier = (peffS - peffW) >= (GRID_STEP - 1e-9)  # p_eff(W) < p_eff(S) by >=1 step
    else:
        eff_earlier = False
    eff_register = ("party-earlier" if eff_earlier
                    else ("equal" if peffW == peffS else "mediator-earlier-or-mixed"))

    print(f"  STRICT register: p_v(W)={pvW} vs p_v(S)={pvS}  ->  {strict_verdict}")
    print(f"  EFFECTIVE register: p_eff(W)={peffW} vs p_eff(S)={peffS}  ->  {eff_register}")
    print("=" * 72)
    print(f"  H3 VERDICT (strict register governs): {strict_verdict}")
    print(f"  CSV: {csv_path}")
    return strict_verdict


if __name__ == "__main__":
    main()
