"""Q8 / H3 — the verdict-flip gap between parity and conjunctive widens with n.

Hypothesis (H3): the flip-gap G(n) = p_flip(conj, n) - p_flip(parity, n) is larger at
n=4 than at n=3, with parity's own flip moving to lower p as n grows.

Forms and noise model (methods.md, fixed for every Q8 test). Node 0 is the hub S; nodes
1..n-1 are the parties (party' = S). The two hub forms differ only in node 0's commit:
  parity (XOR):       S' = x[1] ^ x[2] ^ ... ^ x[n-1]   (parity_hub(n), #115)
  conjunctive (AND):  S' = x[1] & x[2] & ... & x[n-1]   (single_hub(n),  #116)
Clean Phi: parity = 2^(2-n) (0.5 at n=3, 0.25 at n=4); conjunctive = n-1 (2.0, 3.0). Both
triadic. Both run at n=3 and n=4; LABELS = tuple(f"n{i}" for i in range(n)).
CLEAN_TPM = tpm_from_rules(rules); CM = cm_from_rules(rules), reused for every p.

Flip-noise of strength p is output noise on the hub column (node 0): the clean hub value
sc in {0,1} per row becomes P(S'=1) = (1-p)*sc + p*(1-sc). Party columns stay deterministic.
  Phi_MIP(p) = max_phi_float(noisy_tpm(rules, p))[0]  (max exact IIT-4.0 Phi over states).
  binary verdict at p = classify(noisy_tpm(rules, p), CM, labels=LABELS).structure.
Grid: p = 0.00, 0.01, ..., 0.50 (51 points, step 0.01). Four sweeps reused.

Normalized curve: Phi_hat_form,n(p) = Phi_form,n(p) / Phi_form,n(0).

Two registers (both fixed before the run):
  (a) strict verdict-flip p_v(form,n): smallest grid p where structure reads dyadic
      (Phi_MIP <= PHI_EPS = 1e-9).
  (b) effective collapse p_eff(form,n): smallest grid p where Phi_hat_form,n(p) < 0.01 (a
      fixed near-zero band, identical for both forms and both sizes; no per-size tuning).

Measure: flip-gap G_v(n) = p_v(conj,n) - p_v(parity,n) and G_eff(n) = p_eff(conj,n) -
p_eff(parity,n) at n=3 and n=4; the cross-size difference G(4) - G(3); and whether parity's
own flip moves to lower p with size (p_par*(4) < p_par*(3)).

Decision rule (fixed before run): read jointly with H1 — if H1's strict parity flips are
interior at both sizes, G_v governs; if the strict flips sit at 0.5, the effective register
G_eff governs. CONFIRMED if, on the governing register, G(4) > G(3) AND p_par*(4) < p_par*(3)
while the conjunctive flip stays at/near the endpoint (p_v(conj,n)=0.5 on strict, or
p_eff(conj,n) not earlier than parity's on effective). REFUTED if G(4) <= G(3) or parity's
flip does not move earlier with size.

Pre-registration (honest): on the strict register both forms flip only at 0.5 at both sizes
(G_v=0 both), refuting outright; on the effective register the parity normalized curve is
n-independent so p_eff(parity,3)=p_eff(parity,4) (parity flip does NOT move earlier), and the
conjunctive curve decays faster at n=4, so G_eff is expected to narrow or invert. H3 expected
REFUTED on both registers.

Instrument control (run first, abort on failure): the four clean p=0 endpoints must reproduce
their known verdicts and Phi (parity 0.5/0.25 triadic, conjunctive 2.0/3.0 triadic). The
conjunctive n=3 endpoint (Phi=2.0, triadic) is the strict-mediation reference shared with Q6/Q7.

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q8_parity_vs_conjunctive_noise/probe_gap_scaling.py
"""

import csv
import os
import sys
from functools import reduce

# Repo root on sys.path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import max_phi_float

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

# The fixed 51-point grid p = 0.00, 0.01, ..., 0.50.
GRID = [round(k * 0.01, 2) for k in range(51)]

# Thresholds, both fixed before the run.
# PHI_EPS = 1e-9 is the classifier's standard zero cutoff (imported, not retuned).
PHI_EFF_BAND = 0.01     # effective near-zero band on the normalized curve, same for all sweeps
GRID_STEP = 0.01

# Clean Phi targets and verdicts for the instrument control.
CLEAN_TARGETS = {
    ("parity", 3): 0.5,
    ("parity", 4): 0.25,
    ("conjunctive", 3): 2.0,
    ("conjunctive", 4): 3.0,
}


def parity_hub(n):
    """0=S, 1..n-1 = parties. S = XOR of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: reduce(lambda a, b: a ^ b, (x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


def single_hub(n):
    """0=S, 1..n-1 = parties. S = AND of all parties; each party reads S."""
    rules = [None] * n
    rules[0] = lambda x: int(all(x[i] for i in range(1, n)))
    for i in range(1, n):
        rules[i] = (lambda x, i=i: x[0])
    return rules


FORMS = {"parity": parity_hub, "conjunctive": single_hub}
SIZES = (3, 4)


def labels_for(n):
    return tuple(f"n{i}" for i in range(n))


def noisy_tpm(clean_tpm, p):
    """State-by-node TPM with flip-noise p as output noise on the hub column (node 0).

    The clean hub value sc in {0,1} per row becomes P(S'=1) = (1-p)*sc + p*(1-sc): the
    commit lands on its clean value with reliability 1-p and flips with probability p. The
    party columns stay deterministic.
    """
    t = clean_tpm.copy()
    sc = clean_tpm[:, 0]
    t[:, 0] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def instrument_control():
    """The four clean p=0 endpoints must reproduce their tabled verdict and Phi (to 1e-6).
    The conjunctive n=3 endpoint (Phi=2.0, triadic) is the strict-mediation reference.
    Abort on any failure."""
    print("INSTRUMENT CONTROL (four clean forms at p=0)")
    print(f"  {'form':<13}{'n':>2}  {'required':>10}  {'verdict':>9}  {'Phi':>10}  ok")
    passed = True
    for (form, n), target in CLEAN_TARGETS.items():
        rules = FORMS[form](n)
        clean_tpm = tpm_from_rules(rules, n=n)
        cm = cm_from_rules(rules, n=n)
        phi0 = max_phi_float(noisy_tpm(clean_tpm, 0.0))[0]
        v0 = classify(noisy_tpm(clean_tpm, 0.0), cm, labels=labels_for(n), eps=PHI_EPS)
        ok = (v0.structure == "triadic") and (abs(phi0 - target) <= 1e-6)
        passed = passed and ok
        print(f"  {form:<13}{n:>2}  {target:>10.6f}  {v0.structure:>9}  {phi0:>10.6f}  {ok}")
    print(f"  control passed: {passed}")
    print("=" * 72)
    if not passed:
        sys.exit("ABORT: instrument control failed; swept values not trusted.")


def sweep(form, n):
    """Return (rows, phis dict p->Phi_MIP, structures dict p->structure, phi0) for one sweep."""
    rules = FORMS[form](n)
    clean_tpm = tpm_from_rules(rules, n=n)
    cm = cm_from_rules(rules, n=n)
    labels = labels_for(n)
    phis, structures = {}, {}
    rows = []
    for p in GRID:
        tpm = noisy_tpm(clean_tpm, p)
        phi = max_phi_float(tpm)[0]
        v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
        phis[p] = phi
        structures[p] = v.structure
        rows.append({
            "form": form, "n": n, "p": p,
            "phi_mip": round(phi, 9),
            "structure": v.structure,
        })
    phi0 = phis[0.0]
    # attach normalized column now that phi0 is known
    for r in rows:
        r["phi_hat"] = round(r["phi_mip"] / phi0, 9) if phi0 != 0 else float("nan")
    return rows, phis, structures, phi0


def first_strict_flip(structures):
    """Smallest grid p reading dyadic (Phi_MIP <= PHI_EPS); None if never on the grid."""
    ds = [p for p in GRID if structures[p] == "dyadic"]
    return min(ds) if ds else None


def first_eff_collapse(phis, phi0):
    """Smallest grid p where the normalized curve Phi_hat < PHI_EFF_BAND; None if never."""
    if phi0 == 0:
        return None
    bs = [p for p in GRID if (phis[p] / phi0) < PHI_EFF_BAND]
    return min(bs) if bs else None


def main():
    instrument_control()

    print("Q8 / H3 — verdict-flip gap (parity vs conjunctive) across n on the 51-point grid")
    print("=" * 72)
    print(f"  PHI_EPS = {PHI_EPS:g}   effective band Phi_hat < {PHI_EFF_BAND:g} "
          f"(same for all forms & sizes)")
    print("=" * 72)

    all_rows = []
    sweeps = {}  # (form, n) -> (phis, structures, phi0)
    for form in FORMS:
        for n in SIZES:
            rows, phis, structures, phi0 = sweep(form, n)
            all_rows.extend(rows)
            sweeps[(form, n)] = (phis, structures, phi0)
            print(f"  {form:<13} n={n}: clean Phi={phi0:.6f}  "
                  f"strict-flip p_v={first_strict_flip(structures)}  "
                  f"eff-collapse p_eff={first_eff_collapse(phis, phi0)}")
    print("-" * 72)

    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q8_gap_scaling.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(
            fh, fieldnames=["form", "n", "p", "phi_mip", "phi_hat", "structure"])
        w.writeheader()
        w.writerows(all_rows)

    # --- collect the two registers ---
    pv = {}    # (form, n) -> strict flip
    peff = {}  # (form, n) -> effective collapse
    for key, (phis, structures, phi0) in sweeps.items():
        pv[key] = first_strict_flip(structures)
        peff[key] = first_eff_collapse(phis, phi0)

    def val(x):
        return x if x is not None else float("inf")

    # Strict register gaps.
    Gv = {}
    for n in SIZES:
        c, par = pv[("conjunctive", n)], pv[("parity", n)]
        Gv[n] = (val(c) - val(par)) if (c is not None and par is not None) else None
    # Effective register gaps.
    Geff = {}
    for n in SIZES:
        c, par = peff[("conjunctive", n)], peff[("parity", n)]
        Geff[n] = (val(c) - val(par)) if (c is not None and par is not None) else None

    print("REGISTERS")
    print("  strict verdict-flip p_v (smallest p reading dyadic, Phi_MIP<=PHI_EPS):")
    for n in SIZES:
        print(f"    n={n}: p_v(parity)={pv[('parity', n)]}  "
              f"p_v(conj)={pv[('conjunctive', n)]}  G_v({n})={Gv[n]}")
    print(f"  effective collapse p_eff (smallest p with Phi_hat < {PHI_EFF_BAND}):")
    for n in SIZES:
        print(f"    n={n}: p_eff(parity)={peff[('parity', n)]}  "
              f"p_eff(conj)={peff[('conjunctive', n)]}  G_eff({n})={Geff[n]}")
    print("-" * 72)

    # --- which register governs (decided by H1's strict parity flips) ---
    par_interior = all(
        (pv[("parity", n)] is not None and pv[("parity", n)] < 0.5) for n in SIZES)
    if par_interior:
        governing = "strict"
        G = Gv
        p_par = {n: pv[("parity", n)] for n in SIZES}
        conj_at_endpoint = all(pv[("conjunctive", n)] == 0.5 for n in SIZES)
    else:
        governing = "effective"
        G = Geff
        p_par = {n: peff[("parity", n)] for n in SIZES}
        # conjunctive "stays at/near endpoint" on effective register = its collapse not earlier
        # than parity's at each n
        conj_at_endpoint = all(
            (peff[("conjunctive", n)] is not None and peff[("parity", n)] is not None
             and peff[("conjunctive", n)] >= peff[("parity", n)]) for n in SIZES)

    print(f"  H1 join: strict parity flips interior at both sizes? {par_interior}")
    print(f"  GOVERNING register: {governing}")
    print("-" * 72)

    # --- decision rule (fixed before run) ---
    g3, g4 = G[3], G[4]
    gap_widens = (g3 is not None and g4 is not None and g4 > g3)
    pp3, pp4 = p_par[3], p_par[4]
    parity_earlier = (pp3 is not None and pp4 is not None and val(pp4) < val(pp3))

    print("DECISION (governing register)")
    print(f"  G(3) = {g3}   G(4) = {g4}   ->  G(4) > G(3)? {gap_widens}")
    print(f"  p_par*(3) = {pp3}   p_par*(4) = {pp4}   ->  p_par*(4) < p_par*(3)? "
          f"{parity_earlier}")
    print(f"  conjunctive flip stays at/near endpoint? {conj_at_endpoint}")

    if gap_widens and parity_earlier and conj_at_endpoint:
        verdict = "CONFIRMED"
    elif (not gap_widens) or (not parity_earlier):
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"

    print("=" * 72)
    print(f"  H3 VERDICT ({governing} register governs): {verdict}")
    print(f"  CSV: {csv_path}")
    return verdict


if __name__ == "__main__":
    main()
