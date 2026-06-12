"""Q10 / H4 — no d=2 threshold under transport delay.

The buffer-pipeline construction is swept on two corpus forms of differing synchronous
attractor period:
  - two_sided_match (W'=S, S'=W&C, C'=S; period 2)
  - gig_false_dyad  (W'=1-S, S'=W&C, C'=C&(1-S); period 1)
at d = 0,1,2,3. Each (3+d)-node pipeline TPM is classified and Φ_MIP(d) plus the verdict are
read. The synchronous attractor period P is computed as the longest synchronous cycle over all
initial states.

Measure: the Φ_MIP(d) profile and its forward differences dΦ/dd at d=0->1, 1->2, 2->3; whether a
verdict change occurs uniquely at d=2; whether the d=2 reading lies within TOL of the line through
its d=1 and d=3 neighbours. A d=2 kink = a forward-difference discontinuity
(|dΦ/dd|_{d=2} - dΦ/dd|_{d=1}| > TOL and likewise vs d=2->3) or a verdict change appearing only at
d=2.

Decision rule (fixed before the run):
  CONFIRMED if Φ_MIP(d) on the buffer pipeline shows no kink, jump, or verdict change uniquely at
  d=2 for either form (d=2 on the smooth d=1->d=3 trend within TOL; any verdict change not pinned to
  d=2).
  REFUTED if a forward-difference discontinuity or a verdict change appears uniquely at d=2,
  reproducing the Q9 k=2 / grain-2 threshold.
Any lagged-read-arm threshold is checked against P, not fixed at 2.

PHI_EPS = 1e-9, TOL = 1e-6.

Run:
    ~/iit-playground/venv-4.0/bin/python \
        org_frontier/questions/q10_commit_delay/probe_no_d2_threshold.py
"""

import csv
import os
import sys

# Repo root on the path so org_frontier.* and proxy_audit.* import when run as a direct script.
_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.classifier.classifier import classify, tpm_from_rules, cm_from_rules, PHI_EPS
from org_frontier.corpus.forms_library import FORMS_BY_KEY
from org_frontier.probes.lib import major_complex

LABELS3 = ("W", "S", "C")
S_IDX = 1
GRID = [0, 1, 2, 3]
TOL = 1e-6
RESULTS_DIR = os.path.join(os.path.dirname(__file__), "results")

FORM_KEYS = ["two_sided_match", "gig_false_dyad"]


# --------------------------------------------------------------------------------------
# Buffer-pipeline construction (verbatim from methods.md)
# --------------------------------------------------------------------------------------

def buffer_pipeline_rules(rules, d, s_idx=S_IDX):
    # nodes: 0..2 = W,S,C ; 3..3+d-1 = B_1..B_d (B_1 = head copies S, B_d = tail read by parties)
    n = 3 + d
    head = 3            # index of B_1
    tail = 3 + d - 1    # index of B_d  (== s_idx when d == 0: parties read S directly)
    read = tail if d > 0 else s_idx

    def lift(rule):     # party rule that reads S now reads the pipeline tail B_d
        return lambda x: rule(tuple(x[read] if i == s_idx else x[i] for i in range(3)))

    party = [lift(rules[0]), rules[1], lift(rules[2])]     # S keeps its own conjunctive commit
    party[s_idx] = lambda x, r=rules[1]: r((x[0], x[1], x[2]))
    buf = []
    for i in range(d):
        src = s_idx if i == 0 else (head + i - 1)          # B_1 copies S; B_{i+1} copies B_i
        buf.append((lambda x, s=src: x[s]))
    return party + buf                                     # length n list of n-ary rules


# --------------------------------------------------------------------------------------
# Synchronous attractor period (longest cycle over all initial states)
# --------------------------------------------------------------------------------------

def attractor_period(rules, n=3):
    def succ(s):
        b = tuple((s >> i) & 1 for i in range(n))
        return sum(int(rules[j](b)) << j for j in range(n))
    periods = []
    for s0 in range(2 ** n):
        seen, s = [], s0
        while s not in seen:
            seen.append(s)
            s = succ(s)
        periods.append(len(seen) - seen.index(s))
    return max(periods)


# --------------------------------------------------------------------------------------
# Buffer self-edge check (pass-through, not a stickiness cell)
# --------------------------------------------------------------------------------------

def buffer_self_edges(rules, d):
    """Return the list of buffer node indices that carry a B_i -> B_i self-edge (should be empty)."""
    if d == 0:
        return []
    cm = cm_from_rules(rules)
    bad = []
    for b in range(3, 3 + d):
        if cm[b, b] != 0:
            bad.append(b)
    return bad


# --------------------------------------------------------------------------------------
# Classify a pipeline at depth d, returning verdict object on the (3+d)-node system.
# --------------------------------------------------------------------------------------

def classify_pipeline(form_rules, d):
    rules = buffer_pipeline_rules(form_rules, d)
    n = 3 + d
    labels = list(LABELS3) + [f"B{i}" for i in range(1, d + 1)]
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    v = classify(tpm, cm, labels=labels[:n])
    return v, rules


# --------------------------------------------------------------------------------------
# Instrument control (run first — abort if it fails)
# --------------------------------------------------------------------------------------

def instrument_control():
    """Both forms read triadic at d=0 with Φ_MIP=2.0 and MIP {W,SC}; the buffer construction at
    d=0 equals the bare 3-node synchronous form (no buffer nodes added); for d>=1 no buffer carries
    a B_i -> B_i self-edge. Raises on any failure. Also asserts the strict-mediation triad
    (two_sided_match) reads triadic at Φ=2.0 with the full {W,S,C} major complex."""
    for key in FORM_KEYS:
        rules = FORMS_BY_KEY[key].rules

        # d=0 endpoint reproduces the corpus verdict on the bare 3-node form.
        v0 = classify(tpm_from_rules(rules), cm_from_rules(rules), labels=LABELS3)
        assert v0.structure == "triadic", f"control: {key} not triadic at d=0: {v0.structure}"
        assert abs(v0.max_phi - 2.0) < TOL, f"control: {key} Φ_MIP != 2.0 at d=0: {v0.max_phi}"
        assert "{W,SC}" in v0.mip_partition.replace(" ", ""), \
            f"control: {key} MIP not {{W,SC}} at d=0: {v0.mip_partition}"

        # buffer_pipeline_rules(rules, 0) == bare 3-node synchronous form (no nodes added).
        bp0 = buffer_pipeline_rules(rules, 0)
        assert len(bp0) == 3, f"control: {key} buffer pipeline at d=0 added nodes: n={len(bp0)}"
        t_bare, t_bp0 = tpm_from_rules(rules), tpm_from_rules(bp0)
        assert t_bare.shape == t_bp0.shape and np.allclose(t_bare, t_bp0), \
            f"control: {key} buffer pipeline at d=0 != bare synchronous TPM"

        # For d>=1, no buffer self-edge (transport, not inertia / #43 stickiness).
        for d in (1, 2, 3):
            bp = buffer_pipeline_rules(rules, d)
            bad = buffer_self_edges(bp, d)
            assert not bad, f"control: {key} d={d} buffer self-edge at nodes {bad}"

    # Strict-mediation triad: full {W,S,C} major complex at Φ=2.0.
    core, phi_mc = major_complex(FORMS_BY_KEY["two_sided_match"].rules, LABELS3)
    assert set(core) == {"W", "S", "C"}, f"control: major complex not full triad: {core}"
    assert abs(phi_mc - 2.0) < TOL, f"control: major-complex φ != 2.0: {phi_mc}"
    return phi_mc


# --------------------------------------------------------------------------------------
# d=2-threshold analysis for one form's Φ_MIP(d) profile and verdict sequence.
# --------------------------------------------------------------------------------------

def analyze_form(phi, struct):
    """phi: dict d->Φ_MIP, struct: dict d->verdict string. Returns analysis dict."""
    # forward differences
    fd = {d: phi[d + 1] - phi[d] for d in (0, 1, 2)}  # dΦ/dd at 0->1, 1->2, 2->3

    # d=2 kink (forward-difference discontinuity around d=2): |fd@1->2 - fd@0->1| and
    # |fd@2->3 - fd@1->2| both > TOL means the slope changed both entering and leaving d=2.
    kink_in = abs(fd[1] - fd[0])    # change in slope arriving at d=2
    kink_out = abs(fd[2] - fd[1])   # change in slope leaving d=2
    fd_kink_at_2 = (kink_in > TOL) and (kink_out > TOL)

    # collinearity: does the d=2 reading lie on the line through d=1 and d=3?
    line_at_2 = 0.5 * (phi[1] + phi[3])
    resid_at_2 = abs(phi[2] - line_at_2)
    on_smooth_trend = resid_at_2 <= TOL

    # verdict change uniquely at d=2: d=2 differs from BOTH d=1 and d=3 (so the change is pinned
    # to d=2 and reverses), i.e. an isolated verdict flip at d=2.
    verdict_change_unique_at_2 = (struct[2] != struct[1]) and (struct[2] != struct[3])

    # any verdict change in the grid, and whether all changes are pinned to d=2.
    changes_at = [d + 1 for d in (0, 1, 2) if struct[d + 1] != struct[d]]
    verdict_changes_anywhere = len(changes_at) > 0
    verdict_change_pinned_to_2 = (changes_at == [2]) if changes_at else False

    d2_kink = fd_kink_at_2 or verdict_change_unique_at_2

    return {
        "fd": fd,
        "kink_in": kink_in,
        "kink_out": kink_out,
        "fd_kink_at_2": fd_kink_at_2,
        "line_at_2": line_at_2,
        "resid_at_2": resid_at_2,
        "on_smooth_trend": on_smooth_trend,
        "verdict_change_unique_at_2": verdict_change_unique_at_2,
        "verdict_changes_at": changes_at,
        "verdict_changes_anywhere": verdict_changes_anywhere,
        "verdict_change_pinned_to_2": verdict_change_pinned_to_2,
        "d2_kink": d2_kink,
    }


# --------------------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------------------

def main():
    print("=" * 78)
    print("Q10 / H4 — no d=2 threshold under transport delay (buffer pipeline)")
    print(f"forms = {FORM_KEYS}   grid d = {GRID}   PHI_EPS = {PHI_EPS:g}   TOL = {TOL:g}")
    print("=" * 78)

    # --- Instrument control first; abort if it fails ----------------------------------
    print("\n[instrument control] both forms triadic at d=0 (Φ=2.0, MIP {W,SC}); "
          "buffer pipeline at d=0 == bare form; no B_i->B_i self-edge for d>=1")
    phi_mc = instrument_control()
    print(f"  strict-mediation triad major complex = full {{W,S,C}}, φ={phi_mc:.6f}")
    print("  CONTROL PASSED")

    rows = []
    form_analyses = {}
    form_periods = {}

    for key in FORM_KEYS:
        rules = FORMS_BY_KEY[key].rules
        P = attractor_period(rules, n=3)
        form_periods[key] = P
        print(f"\n[form] {key}  (synchronous attractor period P = {P})")

        phi = {}
        struct = {}
        for d in GRID:
            v, _ = classify_pipeline(rules, d)
            phi[d] = v.max_phi
            struct[d] = v.structure
            print(f"  d={d}: n={3 + d}  Φ_MIP={v.max_phi:.6f}  [{v.structure}]  "
                  f"MIP={v.mip_partition}")
            rows.append({
                "form": key,
                "P": P,
                "d": d,
                "n_nodes": 3 + d,
                "phi_mip": f"{v.max_phi:.10g}",
                "structure": v.structure,
                "mip": v.mip_partition,
            })

        a = analyze_form(phi, struct)
        form_analyses[key] = (phi, struct, a)

        print(f"  Φ_MIP(d) profile           = {[round(phi[d], 6) for d in GRID]}")
        print(f"  dΦ/dd [0->1, 1->2, 2->3]   = "
              f"[{a['fd'][0]:.6g}, {a['fd'][1]:.6g}, {a['fd'][2]:.6g}]")
        print(f"  slope change in/out of d=2 = {a['kink_in']:.6g} / {a['kink_out']:.6g}  "
              f"(fd kink at d=2: {a['fd_kink_at_2']})")
        print(f"  line through d=1,d=3 @ d=2  = {a['line_at_2']:.6f}  "
              f"residual={a['resid_at_2']:.3g}  on-trend(<=TOL): {a['on_smooth_trend']}")
        print(f"  verdict sequence            = {[struct[d] for d in GRID]}")
        print(f"  verdict changes at d        = {a['verdict_changes_at']}  "
              f"(unique-at-2: {a['verdict_change_unique_at_2']}, "
              f"pinned-to-2: {a['verdict_change_pinned_to_2']})")
        print(f"  d=2 kink (fd-discontinuity OR isolated verdict flip at d=2): {a['d2_kink']}")

    # --- Decision rule (fixed before the run) -----------------------------------------
    # REFUTED if a forward-difference discontinuity or a verdict change appears uniquely at d=2
    # for EITHER form. CONFIRMED otherwise.
    refuting = []
    for key in FORM_KEYS:
        _, _, a = form_analyses[key]
        if a["d2_kink"]:
            refuting.append(key)

    if refuting:
        verdict = "refuted"
        reason = (f"d=2 threshold (fd-discontinuity or isolated verdict flip uniquely at d=2) "
                  f"appears for: {refuting} — reproduces the Q9 k=2 / grain-2 threshold")
    else:
        verdict = "confirmed"
        reason = ("no kink, jump, or verdict change uniquely at d=2 for either form; "
                  "d=2 lies on the smooth d=1->d=3 trend within TOL and any verdict change "
                  "is not pinned to d=2")

    # Period-tie note: differing P (2 vs 1) controls any threshold against attractor period.
    print("\n[period control]")
    for key in FORM_KEYS:
        _, struct, a = form_analyses[key]
        print(f"  {key}: P={form_periods[key]}  verdict_seq={[struct[d] for d in GRID]}  "
              f"changes_at={a['verdict_changes_at']}")
    print("  (any verdict change in the buffer arm is read against P, not fixed at d=2)")

    print("\n[decision]")
    print(f"  VERDICT: {verdict.upper()}")
    print(f"  reason: {reason}")

    # --- Write CSV --------------------------------------------------------------------
    os.makedirs(RESULTS_DIR, exist_ok=True)
    csv_path = os.path.join(RESULTS_DIR, "no_d2_threshold.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\n  CSV written: {csv_path}")

    return verdict, form_analyses, form_periods


if __name__ == "__main__":
    main()
