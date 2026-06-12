"""Q10 / H3 — the buffer pipeline and the lagged read disagree.

Both transport-delay constructions are swept on `two_sided_match` over the grid d = 0,1,2,3.

(A) Buffer pipeline: `buffer_pipeline_rules(rules, d)` builds a (3+d)-node form with d
    pass-through buffer nodes B_1..B_d carrying S's committed value forward d steps. It is
    classified by `classify(tpm_from_rules, cm_from_rules)`; the verdict is read on the whole
    system and the major-complex core is projected onto W-S-C. The construction adds nodes, so
    it is NOT a single 3-node TPM.

(B) Lagged read: `lagged_read_tpm(rules, d)` has no buffer nodes. On the 3-node W-S-C space the
    parties read S as it was d synchronous steps earlier, built as the d-fold composition of the
    synchronous map with the party read delayed by d. This is a single composed/strided 3-node
    TPM by construction. Its connectivity is inferred by flip-test on the composed TPM; Φ_MIP is
    read by `classify`, and the verdict is dyadic iff Φ_MIP <= PHI_EPS.

Decision rule (fixed before the run): H3 is CONFIRMED if at some d in 1..3 v_lag(d) reads
dyadic while v_buf(d) reads triadic at the same d, OR the two return different W-S-C major
complexes at the same d, with the lagged map expressible as a composed/strided 3-node TPM the
buffer pipeline is not. H3 is REFUTED if the two return the same verdict AND the same W-S-C
major-complex membership at every d.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q10_commit_delay/probe_construction_split.py
"""

import csv
import os
import sys

# Repo root on the path so the org_frontier.* and proxy_audit.* packages import when this file
# is run as a direct script. q10_commit_delay/ -> questions/ -> org_frontier/ -> repo root.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules, PHI_EPS
from org_frontier.corpus.forms_library import FORMS_BY_KEY
from org_frontier.probes.lib import max_phi_float, major_complex

FORM_KEY = "two_sided_match"
LABELS = ("W", "S", "C")
S_IDX = 1
N = 3
GRID = [0, 1, 2, 3]
TOL = 1e-6
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# --------------------------------------------------------------------------------------
# The two transport-delay constructions (verbatim from methods.md)
# --------------------------------------------------------------------------------------

def buffer_pipeline_rules(rules, d, s_idx=S_IDX):
    """(3+d)-node pass-through buffer pipeline. Parties read the pipeline tail B_d in place of S.

    nodes: 0..2 = W,S,C ; 3..3+d-1 = B_1..B_d (B_1 = head copies S, B_d = tail read by parties).
    Each buffer is pure pass-through (no self-OR), so cm has no B_i -> B_i self-edge.
    """
    n = 3 + d
    head = 3                                       # index of B_1
    tail = 3 + d - 1                               # index of B_d (== s_idx when d == 0)
    read = tail if d > 0 else s_idx

    def lift(rule):                                # party rule that read S now reads tail B_d
        return lambda x: rule(tuple(x[read] if i == s_idx else x[i] for i in range(3)))

    party = [lift(rules[0]), rules[1], lift(rules[2])]     # S keeps its own conjunctive commit
    party[s_idx] = lambda x, r=rules[1]: r((x[0], x[1], x[2]))
    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)  # B_1 copies S; B_{i+1} copies B_i
        buf.append((lambda x, s=src: x[s]))
    return party + buf                             # length n list of n-ary rules


def lagged_read_tpm(rules, d, n=N, s_idx=S_IDX):
    """d-fold composition of the synchronous map with the party read of S delayed by d.

    A single composed/strided 3-node state-by-node TPM by construction.
    """
    base = tpm_from_rules(rules)                   # synchronous state-by-node, 3 nodes
    if d == 0:
        return base
    tpm = np.zeros((2 ** n, n))
    for s in range(2 ** n):
        state = [(s >> i) & 1 for i in range(n)]
        # advance S (and the system) d steps; parties commit reading S from d steps back
        hist = [state[:]]
        cur = state[:]
        for _ in range(d):
            nxt = [int(rules[j](tuple(cur))) for j in range(n)]
            hist.append(nxt)
            cur = nxt
        lagged_S = hist[0][s_idx]                  # S as it was d steps before the read
        read_state = list(cur)
        read_state[s_idx] = lagged_S
        for j in range(n):
            tpm[s, j] = float(rules[j](tuple(read_state))) if j != s_idx else float(cur[s_idx])
    return tpm


def buffer_labels(d):
    return tuple(list(LABELS) + [f"B{i}" for i in range(1, d + 1)])


def cm_flip_test(tpm, n):
    """Connectivity matrix inferred by flip-test on a (possibly composed) state-by-node TPM."""
    cm = np.zeros((n, n), dtype=int)
    for j in range(n):
        for i in range(n):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** n)):
                cm[i, j] = 1
    return cm


def has_buffer_self_edge(rules, d):
    """True iff any buffer node carries a B_i -> B_i self-edge (would be a stickiness cell)."""
    if d == 0:
        return False
    n = 3 + d
    cm = cm_from_rules(rules, n)
    for bi in range(3, n):
        if cm[bi, bi] == 1:
            return True
    return False


# --------------------------------------------------------------------------------------
# Instrument control (run first — abort if it fails)
# --------------------------------------------------------------------------------------

def instrument_control(rules):
    """The strict-mediation triad reads triadic at Φ_MIP=2.0 with MIP {W,SC} and full {W,S,C}
    major complex; both constructions reduce to the synchronous map at d=0. Raises on failure.
    """
    # (1) The corpus form's synchronous verdict: triadic, Φ_MIP=2.0, MIP {W,SC}.
    v0 = classify(tpm_from_rules(rules), cm_from_rules(rules), labels=LABELS)
    assert v0.structure == "triadic", f"control: {FORM_KEY} not triadic synchronously: {v0.structure}"
    assert abs(v0.max_phi - 2.0) < TOL, f"control: {FORM_KEY} Φ_MIP != 2.0: {v0.max_phi}"
    assert "{W,SC}" in v0.mip_partition.replace(" ", ""), \
        f"control: {FORM_KEY} MIP not {{W,SC}}: {v0.mip_partition}"
    core0, phi_mc0 = major_complex(rules, LABELS)
    assert set(core0) == {"W", "S", "C"}, f"control: major complex not full triad: {core0}"

    # (2) Buffer pipeline at d=0 equals the bare 3-node synchronous form (no buffer nodes).
    bp0 = buffer_pipeline_rules(rules, 0)
    assert len(bp0) == 3, f"control: buffer d=0 added nodes: n={len(bp0)}"
    tpm_b0 = tpm_from_rules(bp0)
    assert np.array_equal(tpm_b0, tpm_from_rules(rules)), \
        "control: buffer d=0 TPM != synchronous TPM"
    vb0 = classify(tpm_b0, cm_from_rules(bp0), labels=LABELS)
    assert vb0.structure == "triadic" and abs(vb0.max_phi - 2.0) < TOL, \
        f"control: buffer d=0 not triadic/2.0: {vb0.structure}, {vb0.max_phi}"

    # (3) Lagged read at d=0 equals the bare synchronous map.
    lr0 = lagged_read_tpm(rules, 0)
    assert np.array_equal(lr0, tpm_from_rules(rules)), "control: lagged d=0 TPM != synchronous TPM"
    phi_l0, cm_l0 = max_phi_float(lr0)
    vl0 = classify(lr0, cm_l0, labels=LABELS)
    assert vl0.structure == "triadic" and abs(vl0.max_phi - 2.0) < TOL, \
        f"control: lagged d=0 not triadic/2.0: {vl0.structure}, {vl0.max_phi}"

    # (4) Pass-through check: no buffer self-edge for d>=1.
    for d in (1, 2, 3):
        bp = buffer_pipeline_rules(rules, d)
        assert not has_buffer_self_edge(bp, d), f"control: buffer self-edge at d={d}"

    return v0.max_phi, phi_mc0, vb0.max_phi, vl0.max_phi


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def main():
    rules = FORMS_BY_KEY[FORM_KEY].rules

    print("=" * 78)
    print("Q10 / H3 — buffer pipeline vs lagged read construction split")
    print(f"form = {FORM_KEY}   grid d = {GRID}   PHI_EPS = {PHI_EPS:g}   TOL = {TOL:g}")
    print("=" * 78)

    # --- Instrument control first; abort if it fails ----------------------------------
    print("\n[instrument control] strict-mediation triad reads triadic at Φ=2.0; both")
    print("                     constructions reduce to the synchronous map at d=0")
    phi_form, phi_mc, phi_buf0, phi_lag0 = instrument_control(rules)
    print(f"  {FORM_KEY} synchronous: triadic, Φ_MIP={phi_form:.6f}, MIP {{W,SC}}")
    print(f"  major complex (strict-mediation triad): full {{W,S,C}}, φ={phi_mc:.6f}")
    print(f"  buffer pipeline d=0: triadic, Φ_MIP={phi_buf0:.6f} (no buffer nodes)")
    print(f"  lagged read   d=0: triadic, Φ_MIP={phi_lag0:.6f} (== synchronous 3-node TPM)")
    print("  pass-through verified: no B_i -> B_i self-edge at d=1,2,3")
    print("  CONTROL PASSED")

    # --- Sweep both constructions over the grid ---------------------------------------
    rows = []
    disagrees = []
    print("\n[sweep] d : buffer pipeline (classify, core->W-S-C) | lagged read (composed 3-node TPM)")
    for d in GRID:
        # (A) buffer pipeline
        bp = buffer_pipeline_rules(rules, d)
        blabels = buffer_labels(d)
        tpm_b = tpm_from_rules(bp)
        cm_b = cm_from_rules(bp)
        vb = classify(tpm_b, cm_b, labels=blabels)
        v_buf = vb.structure
        # major complex on the full (3+d)-node form, projected onto W-S-C
        core_b_full, phi_mc_b = major_complex(bp, blabels)
        core_b_wsc = tuple(sorted(x for x in core_b_full if x in LABELS))
        buf_is_single_tpm = (len(bp) == 3)        # only at d=0; otherwise adds nodes

        # (B) lagged read — single composed/strided 3-node TPM
        tpm_l = lagged_read_tpm(rules, d)
        cm_l = cm_flip_test(tpm_l, N)
        vl = classify(tpm_l, cm_l, labels=LABELS)
        phi_lag = vl.max_phi
        v_lag = "dyadic" if phi_lag <= PHI_EPS else "triadic"
        if v_lag == "triadic":
            core_l, _phi_mc_l = major_complex_from_tpm(tpm_l, cm_l, LABELS)
        else:
            core_l = ()
        lag_is_single_tpm = True                  # by construction

        verdict_disagree = (v_buf != v_lag)
        # compare W-S-C major-complex membership (only meaningful when both triadic)
        mc_disagree = False
        if v_buf == "triadic" and v_lag == "triadic":
            mc_disagree = (set(core_b_wsc) != set(core_l))
        pair_disagrees = verdict_disagree or mc_disagree
        if pair_disagrees:
            disagrees.append(d)

        print(f"  d={d}: BUF Φ_MIP={vb.max_phi:.6f} [{v_buf}] core(W-S-C)={core_b_wsc} "
              f"full={core_b_full}")
        print(f"         LAG Φ_MIP={phi_lag:.6f} [{v_lag}] core={core_l}  "
              f"disagrees={pair_disagrees}")
        rows.append({
            "d": d,
            "buf_phi_mip": f"{vb.max_phi:.10g}",
            "buf_structure": v_buf,
            "buf_mip": vb.mip_partition,
            "buf_core_full": "|".join(core_b_full) if core_b_full else "",
            "buf_core_wsc": "|".join(core_b_wsc) if core_b_wsc else "",
            "buf_is_single_3node_tpm": buf_is_single_tpm,
            "lag_phi_mip": f"{phi_lag:.10g}",
            "lag_structure": v_lag,
            "lag_mip": vl.mip_partition,
            "lag_core_wsc": "|".join(core_l) if core_l else "",
            "lag_is_single_3node_tpm": lag_is_single_tpm,
            "verdict_disagree": verdict_disagree,
            "mc_disagree": mc_disagree,
            "pair_disagrees": pair_disagrees,
        })

    # --- Decision rule (fixed before the run) -----------------------------------------
    # CONFIRMED if at some d in 1..3 v_lag dyadic while v_buf triadic, OR different W-S-C major
    # complexes at the same d, with lagged map a single composed/strided 3-node TPM the buffer
    # pipeline is not. REFUTED if same verdict AND same W-S-C membership at every d.
    confirm_d = None
    confirm_reason = None
    for r in rows:
        if r["d"] == 0:
            continue
        lag_dyadic_buf_triadic = (r["lag_structure"] == "dyadic"
                                  and r["buf_structure"] == "triadic")
        diff_mc = r["mc_disagree"]
        # representational fact: lagged is a single 3-node TPM the buffer pipeline is not
        repr_distinct = (r["lag_is_single_3node_tpm"] and not r["buf_is_single_3node_tpm"])
        if (lag_dyadic_buf_triadic or diff_mc) and repr_distinct:
            confirm_d = r["d"]
            if lag_dyadic_buf_triadic:
                confirm_reason = (f"at d={r['d']} v_lag=dyadic while v_buf=triadic; "
                                  f"lagged map is a single composed 3-node TPM, buffer is not")
            else:
                confirm_reason = (f"at d={r['d']} the two return different W-S-C major complexes "
                                  f"(buf={r['buf_core_wsc']} vs lag={r['lag_core_wsc']}); "
                                  f"lagged map is a single composed 3-node TPM, buffer is not")
            break

    if confirm_d is not None:
        verdict = "confirmed"
        reason = confirm_reason
    else:
        # refuted iff same verdict and same W-S-C membership at every d
        any_disagree = any(r["pair_disagrees"] for r in rows)
        if not any_disagree:
            verdict = "refuted"
            reason = ("the two constructions return the same verdict and same W-S-C major-complex "
                      "membership at every d (IIT reads the lag, not its representation)")
        else:
            # disagreement exists but not in the confirmed shape (e.g. only at d=0, or buf dyadic)
            verdict = "partial"
            reason = (f"the constructions disagree at d={disagrees} but not in the predicted "
                      f"v_lag-dyadic-while-v_buf-triadic / different-W-S-C-complex shape at d>=1")

    print("\n[decision]")
    print(f"  disagreement d-values (d>=0) = {disagrees if disagrees else 'none'}")
    print(f"  VERDICT: {verdict.upper()}")
    print(f"  reason: {reason}")
    print("  representational fact: lagged read = single composed/strided 3-node TPM; "
          "buffer pipeline = added depth (3+d nodes).")

    # --- Write CSV --------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "construction_split.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\n  CSV written: {csv_path}")

    return verdict, disagrees, rows


def major_complex_from_tpm(tpm, cm, labels):
    """(core_label_tuple, phi) of the maximal complex over reachable states, given a TPM + cm."""
    import pyphi
    from pyphi import new_big_phi
    from foundations.proxy_audit.exact_phi import reachable_states
    n = cm.shape[0]
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
            if float(mc.phi) > best[1]:
                best = (tuple(labels[i] for i in mc.node_indices), float(mc.phi))
        except Exception:
            continue
    core = best[0] if best[0] is not None else ()
    return tuple(sorted(x for x in core if x in labels)), best[1]


if __name__ == "__main__":
    main()
