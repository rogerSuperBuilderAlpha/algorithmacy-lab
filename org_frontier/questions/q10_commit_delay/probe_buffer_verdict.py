r"""Q10 H1 — transport delay grades Phi down but does not flip the verdict.

The buffer-pipeline construction inserts d pure pass-through buffer nodes B_1..B_d on the path
from S's conjunctive commit to the parties' read, on the `two_sided_match` anchor form
(W'=S, S'=W&C, C'=S; labels (W,S,C), node 0=W, 1=S, 2=C; S_IDX=1). The system has n = 3 + d
nodes: W(0), S(1), C(2), B_1(3) .. B_d(3+d-1). The buffer head B_1 copies S, each B_{i+1} copies
B_i, so the tail B_d carries S's value from d steps ago. The parties read B_d in place of S (at
d=0 they read S directly). Each buffer is pure pass-through with NO B_i->B_i self-edge (transport,
not inertia), verified by the cm_from_rules flip-test. Each form is classified by the exact
IIT-4.0 Phi_MIP classifier on the (3+d)-node TPM; the verdict is read on the W-S-C core.

H1 CONFIRMED if the verdict reads triadic at every d=0,1,2,3 with no flip, while Phi_MIP(d) falls
monotonically (dPhi/dd <= 0) or holds at the chain value 2.0. H1 REFUTED if the verdict reads
dyadic at any d in 1..3, or if Phi_MIP(d) rises with d.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q10_commit_delay/probe_buffer_verdict.py \
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

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules
from org_frontier.corpus.forms_library import FORMS_BY_KEY

# proxy_audit.exact_phi lives under foundations/ in this tree; the classifier already wraps it, so
# the probe only needs the package importable for the spec's audit hook. Try the bare path first,
# fall back to the foundations-namespaced path that actually exists here.
try:
    from proxy_audit.exact_phi import exact_big_phi  # noqa: F401
except ImportError:
    from foundations.proxy_audit.exact_phi import exact_big_phi  # noqa: F401

# --- Fixed parameters (pre-registered) -----------------------------------------------------------
FORM_KEY = "two_sided_match"
LABELS_CORE = ("W", "S", "C")
S_IDX = 1
D_GRID = [0, 1, 2, 3]
PHI_EPS = 1e-9
TOL = 1e-6
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


def buffer_pipeline_rules(rules, d, s_idx=S_IDX):
    """Buffer-pipeline rules on n = 3 + d nodes.

    nodes: 0..2 = W,S,C ; 3..3+d-1 = B_1..B_d (B_1 = head copies S, B_d = tail read by parties).
    S commits its conjunctive update from the current party states; the parties read the pipeline
    tail B_d in place of S (read S directly at d=0). Each buffer is pure pass-through with no
    self-edge: B_1 copies S, B_{i+1} copies B_i.
    """
    head = 3                 # index of B_1
    tail = 3 + d - 1         # index of B_d  (== s_idx only conceptually; at d=0 there is no buffer)
    read = tail if d > 0 else s_idx

    def lift(rule):          # a party rule that reads S now reads the pipeline tail B_d
        return lambda x, r=rule, rd=read: r(
            tuple(x[rd] if i == s_idx else x[i] for i in range(3))
        )

    party = [lift(rules[0]), rules[1], lift(rules[2])]   # W' and C' read the tail
    party[s_idx] = lambda x, r=rules[1]: r((x[0], x[1], x[2]))   # S keeps its own conjunctive commit

    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)        # B_1 copies S; B_{i+1} copies B_i
        buf.append(lambda x, s=src: x[s])
    return party + buf                                   # length n list of n-ary rules


def labels_for(d):
    return LABELS_CORE + tuple(f"B{i + 1}" for i in range(d))


def buffers_have_no_self_edge(rules, d):
    """Pass-through verification: cm_from_rules shows no B_i -> B_i self-edge."""
    if d == 0:
        return True, []
    cm = cm_from_rules(rules)
    self_edges = []
    for i in range(d):
        node = 3 + i
        if cm[node, node] != 0:
            self_edges.append(i + 1)
    return (len(self_edges) == 0), self_edges


def instrument_control():
    """Strict-mediation triad reproduces its known verdict: triadic, Phi_MIP=2.0, MIP {W,SC}.

    The d=0 buffer-pipeline endpoint must equal the bare synchronous form (no buffer nodes), the
    Probe 57/62 reference. Abort if it does not reproduce.
    """
    rules = FORMS_BY_KEY[FORM_KEY].rules
    r0 = buffer_pipeline_rules(rules, 0)

    # (a) the d=0 pipeline must be the bare 3-node synchronous form (no buffer nodes added).
    base = tpm_from_rules(rules)
    pipe0 = tpm_from_rules(r0)
    equals_base = (len(r0) == 3) and np.array_equal(base, pipe0)

    # (b) the d=0 endpoint must read the established corpus anchor verdict.
    v = classify(pipe0, cm_from_rules(r0), labels=LABELS_CORE)
    ok = (
        equals_base
        and v.structure == "triadic"
        and abs(v.max_phi - 2.0) <= TOL
        and "{W,SC}" in v.mip_partition
    )
    return ok, v, equals_base


def main():
    rules = FORMS_BY_KEY[FORM_KEY].rules

    print("=" * 78)
    print("Q10 H1 — buffer-pipeline transport delay on two_sided_match (W'=S, S'=W&C, C'=S)")
    print("=" * 78)

    # --- Instrument control (run first; halt on failure) -----------------------------------------
    print("\n[instrument control] strict-mediation triad must read triadic, Phi_MIP=2.0, MIP {W,SC}")
    ok, vc, equals_base = instrument_control()
    print(f"  d=0 pipeline == bare 3-node synchronous form: {equals_base}")
    print(f"  d=0: structure={vc.structure}  Phi_MIP={vc.max_phi:.6f}  "
          f"MIP={vc.mip_partition}  state={vc.mip_state}")
    if not ok:
        print("\nINSTRUMENT CONTROL FAILED — aborting. Swept values are not trustworthy.")
        sys.exit(1)
    print("  instrument control PASSED.")

    # --- Sweep the grid --------------------------------------------------------------------------
    print("\n[sweep] d = 0,1,2,3 — classify(buffer_pipeline_rules(rules, d)) on the W-S-C core")
    rows = []
    for d in D_GRID:
        r = buffer_pipeline_rules(rules, d)
        labels = labels_for(d)
        tpm, cm = tpm_from_rules(r), cm_from_rules(r)
        v = classify(tpm, cm, labels=labels)
        no_self, self_edges = buffers_have_no_self_edge(r, d)
        rows.append({
            "d": d,
            "n_nodes": 3 + d,
            "structure": v.structure,
            "phi_mip": v.max_phi,
            "mip_partition": v.mip_partition,
            "mip_state": v.mip_state,
            "no_self_edge": no_self,
            "self_edges": self_edges,
        })
        print(f"  d={d}: n={3 + d}  structure={v.structure:>7}  Phi_MIP={v.max_phi:.6f}  "
              f"MIP={v.mip_partition}  pass-through(no self-edge)={no_self}")

    # --- Pass-through verification (negative control) --------------------------------------------
    all_pass_through = all(r["no_self_edge"] for r in rows)
    print("\n[pass-through control] no B_i -> B_i self-edge at any d (transport, not inertia): "
          f"{all_pass_through}")
    if not all_pass_through:
        bad = [(r["d"], r["self_edges"]) for r in rows if not r["no_self_edge"]]
        print(f"  STICKINESS DETECTED (self-edges) at: {bad} — Phi change would be inertia, not depth.")

    # --- Verdict / Phi_MIP profile and forward differences ---------------------------------------
    by_d = {r["d"]: r for r in rows}
    phi = [by_d[d]["phi_mip"] for d in D_GRID]
    diffs = [(D_GRID[i], D_GRID[i + 1], phi[i + 1] - phi[i]) for i in range(len(D_GRID) - 1)]

    all_triadic = all(r["structure"] == "triadic" for r in rows)
    dyadic_ds = [r["d"] for r in rows if r["structure"] == "dyadic" or r["phi_mip"] <= PHI_EPS]
    monotone_nonincreasing = all(dd <= TOL for (_, _, dd) in diffs)   # dPhi/dd <= 0 within TOL
    holds_at_chain = all(abs(p - 2.0) <= TOL for p in phi)            # holds at the chain value 2.0
    rises = any(dd > TOL for (_, _, dd) in diffs)                     # Phi_MIP rises with d

    print("\n[measures]")
    print(f"  verdict at each d: " +
          ", ".join(f"d={r['d']}:{r['structure']}" for r in rows))
    print(f"  Phi_MIP(d=0..3) = [{', '.join(f'{p:.6f}' for p in phi)}]")
    print("  forward differences dPhi/dd:")
    for (a, b, dd) in diffs:
        print(f"    d={a}->{b}: {dd:+.6f}")
    print(f"  all d triadic (no flip): {all_triadic}")
    print(f"  dyadic reading at any d in 1..3: {[d for d in dyadic_ds if d >= 1]}")
    print(f"  Phi_MIP monotone non-increasing (dPhi/dd <= 0): {monotone_nonincreasing}")
    print(f"  Phi_MIP holds at chain value 2.0 at every d: {holds_at_chain}")
    print(f"  Phi_MIP rises with d: {rises}")

    # --- Trend register --------------------------------------------------------------------------
    print("\n[trend register] any dyadic reading at d in 1..3 (W-C pair factoring, #32/#62 axis): "
          f"{[d for d in dyadic_ds if d >= 1]}")

    # --- Decision rule (fixed before run) --------------------------------------------------------
    if all_triadic and not rises and (monotone_nonincreasing or holds_at_chain):
        verdict = "CONFIRMED"
    elif (not all_triadic) or any(d >= 1 for d in dyadic_ds) or rises:
        verdict = "REFUTED"
    else:
        verdict = "PARTIAL"
    print(f"\n[decision] H1 {verdict}")

    # --- Write CSV -------------------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "q10_h1_buffer_verdict.csv")
    with open(csv_path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["form", "construction", "d", "n_nodes", "structure", "phi_mip",
                    "mip_partition", "mip_state", "no_self_edge", "dphi_dd_forward"])
        diff_by_a = {a: dd for (a, _, dd) in diffs}
        for r in rows:
            dd = diff_by_a.get(r["d"], "")
            w.writerow([FORM_KEY, "buffer_pipeline", r["d"], r["n_nodes"], r["structure"],
                        f"{r['phi_mip']:.12g}", r["mip_partition"], r["mip_state"],
                        r["no_self_edge"], f"{dd:.12g}" if dd != "" else ""])
    print(f"\n[csv] {csv_path}")

    print("\n[summary]")
    profile = ", ".join(f"{p:.3f}" for p in phi)
    verds = ", ".join(f"{r['structure']}" for r in rows)
    print(f"  Phi_MIP(d=0..3) = [{profile}]")
    print(f"  verdict(d=0..3) = [{verds}]")
    print(f"  H1 {verdict}")

    return verdict


if __name__ == "__main__":
    main()
