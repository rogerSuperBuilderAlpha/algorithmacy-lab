"""Q8 / H1 — the parity verdict flips at an interior p; the conjunctive verdict holds to the endpoint.

Hypothesis (H1): under hub-output flip-noise, the parity (XOR) hub's triadic->dyadic verdict
flips at some interior p < 0.5, while the conjunctive (AND-all) hub's verdict holds through
every interior p and crosses dyadic only at the degenerate endpoint p=0.5.

Forms and noise model (methods.md, fixed before the run). Node 0 is the hub S; nodes 1..n-1 are
parties, each reading the hub (party' = S). The two hubs differ only in the commit rule on node 0:
  - parity (XOR) hub: S' = x[1] ^ x[2] ^ ... ^ x[n-1]   (parity_hub(n), #115; clean Phi=2^(2-n))
  - conjunctive (AND-all) hub: S' = x[1] & x[2] & ... & x[n-1]  (single_hub(n), #116; clean Phi=n-1)
Both forms at n=3 and n=4. Labels = tuple(f"n{i}" for i in range(n)).
CLEAN_TPM = tpm_from_rules(rules); CM = cm_from_rules(rules) reused for every p (the noise
rescales transition probabilities, it adds/removes no edge).

Flip-noise of strength p is OUTPUT noise on the hub column (node 0) of the state-by-node TPM:
the clean value sc in {0,1} per row becomes P(S'=1) = (1-p)*sc + p*(1-sc); party columns stay
deterministic (Q6/Q7 model, Aguilera 2019: the flip rides in the mechanism's TPM).

Measure (fixed before run). Four 51-point sweeps p=0.00..0.50 step 0.01. At each grid p read the
binary verdict classify(noisy_tpm(rules,p), CM).structure and the major complex over the
most-integrated reachable state. The strict verdict-flip point p_v(form,n) is the smallest grid p
at which structure reads dyadic (Phi_MIP <= PHI_EPS = 1e-9). Record p_v(parity,n), p_v(conj,n) at
n=3,4 and whether the major complex stays the full hub-plus-parties set up to p_v.

Controls.
  Instrument control (run first; abort on failure): the four clean p=0 endpoints must reproduce
  triadic with max_phi 0.5 / 0.25 / 2.0 / 3.0 to 1e-6.
  PHI_EPS = 1e-9 is the classifier's standard zero cutoff (imported, not retuned), applied
  identically to both forms so the parity-vs-conjunctive comparison is symmetric.
  Negative control: at each grid point also record max_phi_float's raw Phi; a dyadic reading must
  carry Phi_MIP <= PHI_EPS while its left neighbour carries Phi_MIP > PHI_EPS (a genuine
  zero-crossing of the same statistic, not a one-point dropout).

Decision rule (fixed before run). H1 is CONFIRMED if at BOTH n=3 and n=4
p_v(parity,n) < 0.5 strictly AND p_v(conj,n) = 0.5. H1 is REFUTED if the parity verdict also
flips only at p=0.5 at either size (p_v(parity,n) = 0.5). Pre-registration trial (coarse 6-point
grid): both forms carry Phi_MIP>0 at every interior p and read dyadic only at 0.5 at both sizes,
so the strict register is expected to refute; this 51-point sweep is the finer pre-registered test.

Run:  ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q8_parity_vs_conjunctive_noise/probe_verdict_flip.py
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

import numpy as np
import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import (
    PHI_EPS,
    classify,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import max_phi_float
from foundations.proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_RESULTS = os.path.join(os.path.dirname(__file__), "results")

# The fixed 51-point grid p = 0.00, 0.01, ..., 0.50.
GRID = [round(k * 0.01, 2) for k in range(51)]
GRID_STEP = 0.01
TOL = 1e-6


# --------------------------------------------------------------------------------------
# The two hub forms (parity_hub #115, single_hub #116), reproduced here so the probe is
# self-contained and runs as a direct script.
# --------------------------------------------------------------------------------------

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


def labels_for(n):
    return tuple(f"n{i}" for i in range(n))


# (form name, builder, n, required clean Phi to 1e-6)
FORMS = [
    ("parity", parity_hub, 3, 0.5),
    ("parity", parity_hub, 4, 0.25),
    ("conjunctive", single_hub, 3, 2.0),
    ("conjunctive", single_hub, 4, 3.0),
]


def noisy_tpm(rules, p):
    """State-by-node TPM with flip-noise p as output noise on the hub column (node 0).

    The clean hub value sc in {0,1} per row becomes P(S'=1) = (1-p)*sc + p*(1-sc): the commit
    lands on its clean value with reliability 1-p and flips with probability p. Party columns
    stay deterministic.
    """
    t = tpm_from_rules(rules).copy()
    sc = t[:, 0]
    t[:, 0] = (1.0 - p) * sc + p * (1.0 - sc)
    return t


def major_complex_on_tpm(tpm_sbn, cm, labels):
    """(core_label_tuple, phi) of the maximal complex over reachable states of a (stochastic) TPM."""
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
    """The four clean p=0 endpoints must reproduce triadic with the tabled Phi to 1e-6. Abort
    otherwise. Also assert the strict-mediation triad reads triadic at Phi=2.0 (cross-check on a
    known form) so the instrument is tied to the Q6/Q7 reference."""
    print("INSTRUMENT CONTROL (clean forms, p=0)")
    passed = True

    # Cross-check on a known reference form: strict-mediation triad W'=S, S'=W&C, C'=S -> Phi=2.0.
    ref_rules = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    ref_cm = cm_from_rules(ref_rules, n=3)
    ref_v = classify(noisy_tpm(ref_rules, 0.0), ref_cm, labels=("W", "S", "C"))
    ref_ok = ref_v.structure == "triadic" and abs(ref_v.max_phi - 2.0) <= TOL
    passed = passed and ref_ok
    print(f"  reference strict-mediation triad: structure={ref_v.structure}  "
          f"max_phi={ref_v.max_phi:.6f}  ok={ref_ok}")

    for name, build, n, req_phi in FORMS:
        rules = build(n)
        labels = labels_for(n)
        cm = cm_from_rules(rules, n=n)
        v = classify(noisy_tpm(rules, 0.0), cm, labels=labels)
        ok = v.structure == "triadic" and abs(v.max_phi - req_phi) <= TOL
        passed = passed and ok
        print(f"  {name:<12} n={n}: structure={v.structure}  max_phi={v.max_phi:.6f}  "
              f"(required {req_phi})  MIP={v.mip_partition!r}  ok={ok}")

    print(f"  control passed: {passed}")
    print("=" * 78)
    if not passed:
        sys.exit("ABORT: instrument control failed; swept values not trusted.")


def sweep(name, build, n):
    """One form's 51-point sweep. Returns rows plus per-p structure / classify-Phi / raw-Phi maps."""
    rules = build(n)
    labels = labels_for(n)
    cm = cm_from_rules(rules, n=n)
    full_set = "{" + ",".join(labels) + "}"

    rows = []
    structures = {}
    phis = {}        # classify's Phi_MIP at the most-integrated reachable state
    raw_phis = {}    # max_phi_float's raw max Phi (negative-control statistic)

    print(f"Form {name}  n={n}  labels={labels}  (clean MIP target)")
    print(f"  {'p':>5}  {'Phi_MIP':>10}  {'raw_Phi':>10}  {'structure':>9}  major_complex")
    for p in GRID:
        tpm = noisy_tpm(rules, p)
        v = classify(tpm, cm, labels=labels, eps=PHI_EPS)
        raw_phi, _ = max_phi_float(tpm)
        core, mc_phi = major_complex_on_tpm(tpm, cm, labels)
        core_str = "{" + ",".join(core) + "}" if core is not None else "(none)"
        structures[p] = v.structure
        phis[p] = v.max_phi
        raw_phis[p] = raw_phi
        rows.append({
            "form": name,
            "n": n,
            "p": p,
            "phi_mip": round(v.max_phi, 9),
            "raw_phi": round(raw_phi, 9),
            "structure": v.structure,
            "mip_partition": v.mip_partition,
            "major_complex": core_str,
            "major_complex_phi": round(mc_phi, 6),
            "full_set": core_str == full_set,
        })
        print(f"  {p:>5.2f}  {v.max_phi:>10.6f}  {raw_phi:>10.6f}  {v.structure:>9}  "
              f"{core_str} (phi={mc_phi:.4f})")
    print("-" * 78)
    return rows, structures, phis, raw_phis, full_set


def main():
    instrument_control()

    print("Q8 / H1 — parity vs conjunctive verdict-flip across the 51-point flip-noise grid")
    print("=" * 78)
    print(f"  PHI_EPS = {PHI_EPS:g}  (standard zero cutoff, applied identically to both forms)")
    print("=" * 78)

    all_rows = []
    data = {}  # (name, n) -> dict
    for name, build, n, _ in FORMS:
        rows, structures, phis, raw_phis, full_set = sweep(name, build, n)
        all_rows.extend(rows)
        data[(name, n)] = {
            "structures": structures, "phis": phis, "raw_phis": raw_phis,
            "full_set": full_set, "rows": rows,
        }

    os.makedirs(_RESULTS, exist_ok=True)
    csv_path = os.path.join(_RESULTS, "q8_verdict_flip.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(all_rows[0].keys()))
        w.writeheader()
        w.writerows(all_rows)

    def first_dyadic(name, n):
        st = data[(name, n)]["structures"]
        ds = [p for p in GRID if st[p] == "dyadic"]
        return min(ds) if ds else None

    def full_holds_until(name, n, p_stop):
        d = data[(name, n)]
        full_set = d["full_set"]
        rows = {row["p"]: row for row in d["rows"]}
        chk = GRID if p_stop is None else [p for p in GRID if p <= p_stop]
        return all(rows[p]["major_complex"] == full_set for p in chk)

    def neg_control(name, n, p_v):
        """A dyadic reading must carry Phi_MIP<=PHI_EPS while its left neighbour carries
        Phi_MIP>PHI_EPS (genuine zero-crossing). Checked at the flip point p_v."""
        if p_v is None:
            return None
        phis = data[(name, n)]["phis"]
        k = GRID.index(p_v)
        here_zero = phis[p_v] <= PHI_EPS
        if k == 0:
            return here_zero  # no left neighbour; flip already at the endpoint of the grid
        left_pos = phis[GRID[k - 1]] > PHI_EPS
        return here_zero and left_pos

    pv = {}
    print("RESULT")
    print(f"  strict verdict-flip point p_v (smallest grid p reading dyadic, Phi_MIP<=PHI_EPS):")
    for name, build, n, _ in FORMS:
        p = first_dyadic(name, n)
        pv[(name, n)] = p
        held = full_holds_until(name, n, p)
        nc = neg_control(name, n, p)
        print(f"    {name:<12} n={n}: p_v={p}   full-set major complex holds up to p_v: {held}"
              f"   zero-crossing check: {nc}")
    print("-" * 78)

    # --- Decision rule (fixed before run) ---
    def lt_half(p):
        return p is not None and p < 0.5 - 1e-9

    parity_interior = lt_half(pv[("parity", 3)]) and lt_half(pv[("parity", 4)])
    conj_at_half = (pv[("conjunctive", 3)] == 0.5) and (pv[("conjunctive", 4)] == 0.5)
    parity_at_half = (pv[("parity", 3)] == 0.5) or (pv[("parity", 4)] == 0.5)

    if parity_interior and conj_at_half:
        verdict = "CONFIRMED"
    elif parity_at_half:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"

    print(f"  p_v(parity,3)={pv[('parity',3)]}  p_v(parity,4)={pv[('parity',4)]}  "
          f"p_v(conj,3)={pv[('conjunctive',3)]}  p_v(conj,4)={pv[('conjunctive',4)]}")
    print(f"  parity flips interior at both sizes: {parity_interior}    "
          f"conjunctive flips only at 0.5 at both sizes: {conj_at_half}")
    print("=" * 78)
    print(f"  H1 VERDICT: {verdict}")
    print(f"  CSV: {csv_path}")
    return verdict


if __name__ == "__main__":
    main()
