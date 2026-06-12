r"""Q11 H4 — the limit-cycle family stays triadic across n.

Both constructed cyclers at every n = 3,4,5,6:
  - rot_ring(n): the rotating-update ring (each node copies its left neighbor; the global
    state rotates one position per step, a traveling wave of period n).
  - commit_ring(n, 2): the periodic-commit mediated form. Mediator S (node 0) holds a
    conjunctive commit S' = AND(members) and releases it once every p=2 micro-steps,
    holding its value otherwise; each member i>=1 reads S. Built as a composed
    state-by-node TPM via the hold_k_tpm pattern (Q9 methods) with the mediator as the
    held node and k = p, so the commit cadence is set independently of member count. The
    observed transition is classified directly from the composed (tpm, cm).

Measure per (n, form): the binary verdict (triadic iff Phi_MIP > PHI_EPS=1e-9) via
classify on the composed map, the major-complex membership (full n-node set vs a shed
node, the center-periphery drop #128), and the MIP partition repr at the max-Phi state.

Standing caveat (#130): no attractor predicate separates the verdict, so this test claims
only that these two built-to-integrate cyclers land triadic, not that cycling implies
triadicity in general.

Decision rule (fixed before run): CONFIRM H4 if both forms read triadic at every
n=3,4,5,6 AND major_complex returns the full n-node set for both at every n. REFUTE if
either form reads dyadic at any n, or its core sheds >=1 node at any n.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q11_oscillatory_scaling/probe_probe_q11_triadic_persistence.py \
        2>&1 | grep -v "Welcome to PyPhi\|pyphi.config"
"""

import csv
import os
import sys

# --- Repo root on sys.path so org_frontier.* and proxy_audit.* import, and the module runs
# --- as a direct script. The probe sits three levels below the repo root.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules
from org_frontier.probes.lib import major_complex
from org_frontier.corpus.forms_library import FORMS_BY_KEY

# proxy_audit.exact_phi lives under foundations/ in this tree; the classifier already wraps
# it. Keep the package importable for the spec's audit hook (bare path first, then the
# foundations-namespaced path that actually exists here).
try:
    from proxy_audit.exact_phi import exact_big_phi  # noqa: F401
except ImportError:
    from foundations.proxy_audit.exact_phi import exact_big_phi  # noqa: F401

# --- Fixed parameters (pre-registered) -----------------------------------------------------------
N_GRID = [3, 4, 5, 6]
COMMIT_P = 2          # commit cadence for the mediated form (a non-trivial cycle)
PHI_EPS = 1e-9
TOL = 1e-6
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# --- The forms (fixed for every test) ------------------------------------------------------------
def rot_ring(n):
    """Rotating-update ring: each node copies its left neighbor (global rotation, period n)."""
    rules = [None] * n
    for i in range(n):
        a = (i - 1) % n
        rules[i] = (lambda x, a=a: int(x[a]))
    return rules


def and_ring(n):
    """The zoo's capped fixed-point ring: each node is AND of its two ring neighbors."""
    rules = [None] * n
    for i in range(n):
        a, b = (i - 1) % n, (i + 1) % n
        rules[i] = (lambda x, a=a, b=b: int(x[a] & x[b]))
    return rules


def commit_ring_tpm(n, p):
    """Periodic-commit mediated form as a composed state-by-node TPM (hold_k_tpm pattern).

    Node 0 is the mediator S. Members are nodes 1..n-1. Inside one observed transition p
    micro-steps run. Every micro-step each member reads the *current* S value; S holds its
    own value for the first p-1 micro-steps and commits S' = AND(members) on the p-th. The
    macro next-state is the state after the full p-window. The commit cadence p is set
    independently of member count. Connectivity inferred by a flip-test.
    """
    s_idx = 0
    members = list(range(1, n))

    def micro(state, commit_S):
        ns = list(state)
        # members read the current mediator value
        for i in members:
            ns[i] = state[s_idx]
        if commit_S:
            ns[s_idx] = int(all(state[i] for i in members)) if members else state[s_idx]
        else:
            ns[s_idx] = state[s_idx]  # S holds its previous value
        return ns

    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        for step in range(p):
            state = micro(state, commit_S=(step == p - 1))  # commit only on the p-th micro-step
        for j in range(n):
            tpm[s, j] = float(state[j])

    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return tpm, cm


def labels_for(n):
    return tuple(f"x{i}" for i in range(n))


# --- Instrument control --------------------------------------------------------------------------
def instrument_control():
    """Run first; halt on failure. Three anchors must reproduce their established readings:

      - and_ring(4): triadic, max Phi_MIP = 4.0, full 4-node core (#132 capped law).
      - and_ring(3): triadic, max Phi_MIP = 6.0 (the #132 n=3 ring value).
      - strict-mediation triad two_sided_match (W'=S, S'=W&C, C'=S): triadic, Phi_MIP = 2.0.
    """
    checks = []

    # and_ring(4) = 4.0, full core
    lab4 = labels_for(4)
    v4 = classify(tpm_from_rules(and_ring(4)), cm_from_rules(and_ring(4)), labels=lab4)
    core4, _ = major_complex(and_ring(4), lab4)
    ok4 = (v4.structure == "triadic" and abs(v4.max_phi - 4.0) <= TOL
           and core4 is not None and len(core4) == 4)
    checks.append(("and_ring(4) triadic Phi=4.0 full core",
                   ok4, f"structure={v4.structure} Phi={v4.max_phi:.6f} core={core4}"))

    # and_ring(3) = 6.0
    lab3 = labels_for(3)
    v3 = classify(tpm_from_rules(and_ring(3)), cm_from_rules(and_ring(3)), labels=lab3)
    ok3 = (v3.structure == "triadic" and abs(v3.max_phi - 6.0) <= TOL)
    checks.append(("and_ring(3) triadic Phi=6.0",
                   ok3, f"structure={v3.structure} Phi={v3.max_phi:.6f}"))

    # strict-mediation triad: two_sided_match reads triadic at Phi=2.0
    tri = FORMS_BY_KEY["two_sided_match"].rules
    labtri = ("W", "S", "C")
    vt = classify(tpm_from_rules(tri), cm_from_rules(tri), labels=labtri)
    okt = (vt.structure == "triadic" and abs(vt.max_phi - 2.0) <= TOL)
    checks.append(("strict-mediation triad triadic Phi=2.0",
                   okt, f"structure={vt.structure} Phi={vt.max_phi:.6f} MIP={vt.mip_partition}"))

    return checks


# --- Per-(n, form) reading -----------------------------------------------------------------------
def read_rot(n):
    lab = labels_for(n)
    rules = rot_ring(n)
    v = classify(tpm_from_rules(rules), cm_from_rules(rules), labels=lab)
    core, phi_mc = major_complex(rules, lab)
    return v, core, phi_mc, lab


def read_commit(n, p):
    lab = labels_for(n)
    tpm, cm = commit_ring_tpm(n, p)
    v = classify(tpm, cm, labels=lab)
    # major complex over reachable states from the composed map
    import pyphi
    from pyphi import new_big_phi
    from foundations.proxy_audit.exact_phi import reachable_states
    net = pyphi.Network(tpm, cm=cm, node_labels=lab)
    best = (None, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
            if float(mc.phi) > best[1]:
                best = (tuple(lab[i] for i in mc.node_indices), float(mc.phi))
        except Exception:
            continue
    core, phi_mc = best
    return v, core, phi_mc, lab


def main():
    print("=" * 78)
    print("Q11 H4 — the limit-cycle family stays triadic across n (rot_ring & commit_ring(n,2))")
    print("=" * 78)

    # --- Instrument control (run first; halt on failure) -----------------------------------------
    print("\n[instrument control] anchors must reproduce their established readings")
    all_ok = True
    for name, ok, detail in instrument_control():
        print(f"  {'PASS' if ok else 'FAIL'}  {name}: {detail}")
        all_ok = all_ok and ok
    if not all_ok:
        print("\nINSTRUMENT CONTROL FAILED — aborting. Swept values are not trustworthy.")
        sys.exit(1)
    print("  instrument control PASSED.")

    # --- Sweep both forms at n = 3,4,5,6 ---------------------------------------------------------
    rows = []
    print("\n[sweep] rot_ring(n) and commit_ring(n, 2), n = 3,4,5,6")
    for n in N_GRID:
        # rotating ring
        v, core, phi_mc, lab = read_rot(n)
        full = core is not None and len(core) == n
        rows.append(dict(form="rot_ring", n=n, structure=v.structure, phi_mip=v.max_phi,
                         core=core, core_size=(len(core) if core else 0), full=full,
                         mip_state=v.mip_state, mip_partition=v.mip_partition, phi_mc=phi_mc))
        print(f"  rot_ring(n={n}):     structure={v.structure:>7}  Phi_MIP={v.max_phi:.6f}  "
              f"core={core} (size {len(core) if core else 0}/{n}, full={full})")
        print(f"                       MIP@max-Phi state {v.mip_state}: {v.mip_partition}")

        # mediated periodic-commit form
        v, core, phi_mc, lab = read_commit(n, COMMIT_P)
        full = core is not None and len(core) == n
        rows.append(dict(form=f"commit_ring(p={COMMIT_P})", n=n, structure=v.structure,
                         phi_mip=v.max_phi, core=core, core_size=(len(core) if core else 0),
                         full=full, mip_state=v.mip_state, mip_partition=v.mip_partition,
                         phi_mc=phi_mc))
        print(f"  commit_ring(n={n},2): structure={v.structure:>7}  Phi_MIP={v.max_phi:.6f}  "
              f"core={core} (size {len(core) if core else 0}/{n}, full={full})")
        print(f"                       MIP@max-Phi state {v.mip_state}: {v.mip_partition}")

    # --- Decision rule (fixed before run) --------------------------------------------------------
    all_triadic = all(r["structure"] == "triadic" for r in rows)
    all_full = all(r["full"] for r in rows)
    any_dyadic = any(r["structure"] == "dyadic" for r in rows)
    any_shed = any(not r["full"] for r in rows)

    if all_triadic and all_full:
        verdict = "CONFIRMED"
    elif any_dyadic or any_shed:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"

    print("\n[measures]")
    print(f"  both forms triadic at every n=3,4,5,6: {all_triadic}")
    print(f"  full n-node core for both at every n:  {all_full}")
    if any_dyadic:
        print("  REFUTATION: a dyadic verdict appeared:",
              [(r["form"], r["n"]) for r in rows if r["structure"] == "dyadic"])
    if any_shed:
        print("  REFUTATION: a shed core appeared:",
              [(r["form"], r["n"], r["core_size"]) for r in rows if not r["full"]])

    print(f"\n[decision] H4 {verdict}")

    # --- Write CSV -------------------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "q11_h4_triadic_persistence.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "n", "structure", "phi_mip", "core", "core_size",
                    "full_set", "mip_state", "mip_partition", "phi_major_complex"])
        for r in rows:
            w.writerow([r["form"], r["n"], r["structure"], f"{r['phi_mip']:.12g}",
                        "|".join(r["core"]) if r["core"] else "", r["core_size"],
                        r["full"], r["mip_state"], r["mip_partition"],
                        f"{r['phi_mc']:.12g}"])
    print(f"\n[csv] {csv_path}")

    print("\n[summary]")
    for form in ("rot_ring", f"commit_ring(p={COMMIT_P})"):
        seq = [r for r in rows if r["form"] == form]
        prof = ", ".join(f"n{r['n']}:{r['structure'][:3]}/{r['core_size']}of{r['n']}" for r in seq)
        print(f"  {form}: {prof}")
    print(f"  ->  H4 {verdict}")

    return verdict


if __name__ == "__main__":
    main()
