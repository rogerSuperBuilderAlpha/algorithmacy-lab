"""Q10 H2 — the buffer nodes sit outside the major complex at the micro grain.

Form/ensemble: the buffer-pipeline construction on `two_sided_match` at d = 1,2,3 (the
cases with at least one buffer). At each d the micro-grain major complex is read over the
most-integrated reachable state via PyPhi `new_big_phi.maximal_complex` over
`reachable_states` (the machinery `probes/lib.major_complex` wraps), returning
(core_label_tuple, phi). In parallel the singleton phi of each interior buffer {B_i} is
measured at the same map/state (not assumed zero), and the phi of the {W,S,C} core. The
complex is then re-read after black-boxing the buffers over d steps (composing the micro
map on the W-S-C subspace).

Measure: micro-grain core membership core(d); whether {W,S,C} subset of core(d); whether
each interior B_i (i>=2) is excluded; phi_{B_i} per buffer; black-boxed core and Phi.

Controls: instrument control (d=0 core is full {W,S,C} at Phi=2.0, the corpus reference
shared by every Q10 test); buffer phi measured not assumed; pass-through (no B_i->B_i
self-edge) verified as the feed-forward prior; black-boxed re-read as the absorption
contrast.

Decision rule (fixed before run): CONFIRMED if at every d the micro complex contains the
full {W,S,C} core (with at most B_1 as a weak appendix) and excludes every interior B_i
(i>=2) with phi_{B_i} < PHI_EPS; REFUTED if any interior buffer sits inside the complex
with phi_{B_i} > PHI_EPS, or {W,S,C} is not recovered at the micro grain. Black-boxed
absorption is the grain-dependent branch and does not by itself refute. PHI_EPS=1e-9.

Run:
  ~/iit-playground/venv-4.0/bin/python \
    org_frontier/questions/q10_commit_delay/probe_buffer_membership.py
"""

import os
import sys

# Repo root on the path so org_frontier.* and proxy_audit.* import when run as a script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import csv

import numpy as np
import pyphi
from pyphi import new_big_phi

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules
from org_frontier.corpus.forms_library import FORMS_BY_KEY
from foundations.proxy_audit.exact_phi import reachable_states

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

FORM_KEY = "two_sided_match"
LABELS_CORE = ("W", "S", "C")
S_IDX = 1
PHI_EPS = 1e-9
GRID = [1, 2, 3]
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")


# --------------------------------------------------------------------------------------
# The buffer-pipeline construction (verbatim from methods.md)
# --------------------------------------------------------------------------------------

def buffer_pipeline_rules(rules, d, s_idx=S_IDX):
    """d pass-through buffer nodes B_1..B_d on the S-commit -> party-read path.

    nodes: 0..2 = W,S,C ; 3..3+d-1 = B_1..B_d (B_1 head copies S, B_d tail read by parties).
    Each buffer is pure pass-through (no self-OR): b'_i = previous node on the line.
    """
    head = 3
    tail = 3 + d - 1
    read = tail if d > 0 else s_idx

    def lift(rule):
        return lambda x: rule(tuple(x[read] if i == s_idx else x[i] for i in range(3)))

    party = [lift(rules[0]), rules[1], lift(rules[2])]
    party[s_idx] = lambda x, r=rules[1]: r((x[0], x[1], x[2]))
    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)
        buf.append((lambda x, s=src: x[s]))
    return party + buf


def buffer_labels(d):
    return LABELS_CORE + tuple(f"B{i}" for i in range(1, d + 1))


# --------------------------------------------------------------------------------------
# Major complex over reachable states, and fixed-state subsystem phi
# --------------------------------------------------------------------------------------

def major_complex_over_states(tpm, cm, labels):
    """(core_label_tuple, phi, state) of the maximal complex, max over reachable states."""
    n = cm.shape[0]
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    best = (None, -1.0, None)
    for s in reachable_states(tpm, n):
        state = tuple((s >> i) & 1 for i in range(n))
        try:
            mc = new_big_phi.maximal_complex(net, state)
        except Exception:
            continue
        ni = getattr(mc, "node_indices", None)
        if ni is None:
            continue
        phi = float(getattr(mc, "phi", 0.0))
        if phi > best[1]:
            best = (tuple(labels[i] for i in ni), phi, state)
    return best


def subsystem_phi(tpm, cm, state, nodes, labels):
    """phi of a node-subset subsystem at a fixed state (the symmetric grain/state read).

    PyPhi's `Subsystem` rejects the whole-network state as "unreachable" when restricting
    to a node subset (it validates the full state, not the subsystem). The maximal-complex
    state is itself a reachable whole-system state, so the buffer/core singleton phi at that
    state is well-defined; VALIDATE_SUBSYSTEM_STATES is relaxed for this read so the buffer
    phi is measured, not forced to nan (the "measure it, do not assume zero" spec).
    """
    net = pyphi.Network(tpm, cm=cm, node_labels=labels)
    saved = pyphi.config.VALIDATE_SUBSYSTEM_STATES
    pyphi.config.VALIDATE_SUBSYSTEM_STATES = False
    try:
        sub = pyphi.Subsystem(net, state, nodes=nodes)
        return float(new_big_phi.sia(sub).phi)
    except Exception:
        return float("nan")
    finally:
        pyphi.config.VALIDATE_SUBSYSTEM_STATES = saved


# --------------------------------------------------------------------------------------
# Black-boxing the buffers: compose the micro map over d steps on the W-S-C subspace
# --------------------------------------------------------------------------------------

def blackbox_wsc_tpm(rules, d, s_idx=S_IDX):
    """d-step macro map on the 3-node W-S-C subspace with the buffer pipeline marginalized.

    The micro full-system map runs d micro-steps from a W-S-C state with the buffer line
    initialized to S's committed value (the pipeline filled). After d steps the buffer tail
    carries S's value from d steps ago and the parties have read through the line; the macro
    transition reads off the W,S,C coordinates. This composes the micro map over the buffer
    window and is the absorption contrast (Marshall 2018).
    """
    n_full = 3 + d
    full_rules = buffer_pipeline_rules(rules, d, s_idx=s_idx)
    tpm = np.zeros((2 ** 3, 3))
    for s in range(2 ** 3):
        wsc = [(s >> i) & 1 for i in range(3)]
        # Fill the pipeline with S's current value (steady transport prior); buffers carry S.
        state = wsc + [wsc[s_idx]] * d
        for _ in range(d):
            state = [int(full_rules[j](tuple(state))) for j in range(n_full)]
        for j in range(3):
            tpm[s, j] = float(state[j])
    cm = np.zeros((3, 3), dtype=int)
    for j in range(3):
        for i in range(3):
            if any(abs(tpm[s, j] - tpm[s ^ (1 << i), j]) > 1e-9 for s in range(2 ** 3)):
                cm[i, j] = 1
    return tpm, cm


def has_buffer_self_edge(cm, d):
    """True iff any interior buffer B_i carries a B_i -> B_i self-edge (stickiness, not transport)."""
    for i in range(d):
        idx = 3 + i
        if cm[idx, idx] != 0:
            return True
    return False


# --------------------------------------------------------------------------------------
# Instrument control (run first)
# --------------------------------------------------------------------------------------

def instrument_control():
    """d=0 buffer-pipeline on two_sided_match must read the known triadic {W,S,C} at Phi=2.0,
    and the pipeline must add no nodes at d=0 and carry no buffer self-edge at d>=1."""
    rules = FORMS_BY_KEY[FORM_KEY].rules

    # d=0 endpoint: bare 3-node synchronous form, triadic, Phi=2.0, full {W,S,C} core.
    r0 = buffer_pipeline_rules(rules, 0)
    assert len(r0) == 3, f"d=0 pipeline added nodes: n={len(r0)}"
    tpm0, cm0 = tpm_from_rules(r0), cm_from_rules(r0)
    v0 = classify(tpm0, cm0, labels=LABELS_CORE)
    core0, phi0, _ = major_complex_over_states(tpm0, cm0, LABELS_CORE)
    print("[instrument control] two_sided_match buffer d=0: "
          f"verdict={v0.structure} Phi_MIP={v0.max_phi:.6f} MIP={v0.mip_partition} "
          f"core={core0} core_phi={phi0:.6f}")
    ok = (v0.structure == "triadic"
          and abs(v0.max_phi - 2.0) < 1e-6
          and core0 is not None
          and set(core0) == {"W", "S", "C"})
    assert ok, ("Instrument control FAILED: d=0 endpoint is not the triadic {W,S,C} triad "
                f"at Phi=2.0 (got verdict={v0.structure}, Phi={v0.max_phi}, core={core0}). "
                "Halting; swept values not trusted.")

    # Pass-through check: no buffer self-edge for d=1,2,3.
    for d in GRID:
        rd = buffer_pipeline_rules(rules, d)
        cmd = cm_from_rules(rd)
        assert not has_buffer_self_edge(cmd, d), (
            f"Buffer self-edge present at d={d} — a stickiness cell, not a transport line. Halting.")
    print("[instrument control] pass-through verified (no B_i->B_i self-edge at d=1,2,3)")
    print("[instrument control] PASS\n")


# --------------------------------------------------------------------------------------
# The H2 run
# --------------------------------------------------------------------------------------

def run():
    instrument_control()

    rules = FORMS_BY_KEY[FORM_KEY].rules
    rows = []
    refuted_reasons = []
    all_confirm = True

    for d in GRID:
        labels = buffer_labels(d)
        r = buffer_pipeline_rules(rules, d)
        tpm, cm = tpm_from_rules(r), cm_from_rules(r)
        v = classify(tpm, cm, labels=labels)
        core, core_phi, mstate = major_complex_over_states(tpm, cm, labels)
        core_set = set(core) if core else set()

        # phi of each interior buffer singleton at the most-integrated state (measured).
        buf_phis = {}
        if mstate is not None:
            for i in range(1, d + 1):
                idx = 3 + (i - 1)
                buf_phis[f"B{i}"] = subsystem_phi(tpm, cm, mstate, (idx,), labels)
            phi_wsc = subsystem_phi(tpm, cm, mstate, (0, 1, 2), labels)
        else:
            for i in range(1, d + 1):
                buf_phis[f"B{i}"] = float("nan")
            phi_wsc = float("nan")

        # Black-boxed re-read on the W-S-C subspace (absorption contrast).
        bb_tpm, bb_cm = blackbox_wsc_tpm(rules, d)
        vbb = classify(bb_tpm, bb_cm, labels=LABELS_CORE)
        bb_core, bb_phi, _ = major_complex_over_states(bb_tpm, bb_cm, LABELS_CORE)
        bb_core_set = set(bb_core) if bb_core else set()

        wsc_in_core = {"W", "S", "C"}.issubset(core_set)
        # interior buffers are B_i with i >= 2 (B_1 allowed as weak appendix).
        interior = [f"B{i}" for i in range(2, d + 1)]
        interior_excluded = all(b not in core_set for b in interior)
        interior_phi_zero = all(
            (not np.isnan(buf_phis[b])) and buf_phis[b] < PHI_EPS for b in interior
        ) if interior else True
        # any interior buffer inside the complex with phi > eps -> refute
        interior_in_core_live = any(
            (b in core_set) and (not np.isnan(buf_phis[b])) and buf_phis[b] > PHI_EPS
            for b in interior
        )

        confirm_d = wsc_in_core and interior_excluded and interior_phi_zero
        if not confirm_d:
            all_confirm = False
            if not wsc_in_core:
                refuted_reasons.append(f"d={d}: {{W,S,C}} not recovered (core={core_set})")
            if interior_in_core_live:
                bad = [b for b in interior if b in core_set and not np.isnan(buf_phis[b])
                       and buf_phis[b] > PHI_EPS]
                refuted_reasons.append(
                    f"d={d}: interior buffer(s) {bad} inside complex with phi>eps")

        rows.append({
            "d": d,
            "verdict": v.structure,
            "phi_mip": round(v.max_phi, 6),
            "core": "".join(c[0] if len(c) == 1 else c for c in core) if core else "-",
            "core_full": ",".join(core) if core else "-",
            "WSC_subset_core": wsc_in_core,
            "interior_excluded": interior_excluded,
            "mip_state": "".join(str(b) for b in mstate) if mstate else "-",
            "phi_WSC": round(phi_wsc, 6),
            **{f"phi_{b}": round(buf_phis[b], 9) for b in buf_phis},
            "bb_verdict": vbb.structure,
            "bb_phi_mip": round(vbb.max_phi, 6),
            "bb_core": ",".join(bb_core) if bb_core else "-",
            "bb_core_phi": round(bb_phi, 6),
            "bb_absorbs_buffer": (bb_core_set == {"W", "S", "C"} and bb_phi > core_phi + 1e-6),
        })

    # ----- print exact numbers -----
    print("Micro-grain major complex, interior-buffer phi, and black-boxed re-read:\n")
    for r in rows:
        print(f"d={r['d']}  verdict={r['verdict']}  Phi_MIP={r['phi_mip']:.6f}  "
              f"core={r['core_full']}  state={r['mip_state']}")
        print(f"      {{W,S,C}} subset core: {r['WSC_subset_core']}   "
              f"interior B_i(i>=2) excluded: {r['interior_excluded']}   "
              f"phi_{{W,S,C}}={r['phi_WSC']:.6f}")
        bphi = "  ".join(f"phi_{k.split('_')[1]}={v:.9f}"
                         for k, v in r.items() if k.startswith("phi_B"))
        print(f"      buffer singleton phi: {bphi if bphi else '(none)'}")
        print(f"      black-boxed W-S-C: verdict={r['bb_verdict']}  Phi={r['bb_phi_mip']:.6f}  "
              f"core={r['bb_core']}  core_phi={r['bb_core_phi']:.6f}  "
              f"absorbs_buffer={r['bb_absorbs_buffer']}")
        print()

    # ----- verdict (fixed decision rule) -----
    if all_confirm:
        verdict = "CONFIRMED"
        why = ("at every d the micro complex contains full {W,S,C} (at most B1 appendix) and "
               "excludes every interior B_i(i>=2) with phi_{B_i}<PHI_EPS")
    else:
        verdict = "REFUTED"
        why = "; ".join(refuted_reasons) if refuted_reasons else \
            "micro-grain {W,S,C} core / interior-exclusion condition not met"

    print(f"VERDICT: {verdict} — {why}")

    # ----- CSV -----
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "h2_buffer_membership.csv")
    fieldnames = sorted({k for r in rows for k in r.keys()})
    # keep a stable, readable leading order
    lead = ["d", "verdict", "phi_mip", "core_full", "WSC_subset_core", "interior_excluded",
            "mip_state", "phi_WSC", "bb_verdict", "bb_phi_mip", "bb_core", "bb_core_phi",
            "bb_absorbs_buffer"]
    rest = [f for f in fieldnames if f not in lead]
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=lead + rest)
        w.writeheader()
        for r in rows:
            w.writerow(r)
    print(f"\nCSV written: {csv_path}")
    return verdict, rows


if __name__ == "__main__":
    run()
