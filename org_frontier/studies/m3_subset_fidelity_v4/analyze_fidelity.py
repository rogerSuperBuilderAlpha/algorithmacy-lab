"""M3 subset-Φ fidelity against V4 items 1–3 (RESEARCH_AGENDA_V4 item 12).

Does overlay subset Φ on third_party/pyphi_iit4_mv move the reading
keys of V4 items 1–3, or does exact binary Φ already decide them?

Hypotheses, bars, witnesses, and reading keys were fixed in
hypotheses.md before this script existed.

Run from the repo root:
  python org_frontier/studies/m3_subset_fidelity_v4/analyze_fidelity.py
"""

from __future__ import annotations

import csv
import importlib.util
import json
import os
import sys
import time

import numpy as np

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
_THIRD = os.path.join(_REPO_ROOT, "third_party")
for p in (_THIRD, _REPO_ROOT):
    if p not in sys.path:
        sys.path.insert(0, p)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import pyphi
from pyphi import convert, new_big_phi
from pyphi.exceptions import StateUnreachableError

from org_frontier.classifier.classifier import (
    classify,
    classify_rules,
    cm_from_rules,
    tpm_from_rules,
)
from org_frontier.probes.lib import verdict as vlib
from foundations.proxy_audit.exact_phi import reachable_states
from pyphi_iit4_mv import MultivaluedNetwork
from pyphi_iit4_mv.sia_mv import sia
from pyphi_iit4_mv.subsystem_mv import MultivaluedSubsystem

pyphi.config.PROGRESS_BARS = False
pyphi.config.PARALLEL = False

_V41 = os.path.join(
    _REPO_ROOT, "org_frontier", "studies", "joint_obs_cliff_exact_phi",
    "analyze_transfer.py",
)
_spec = importlib.util.spec_from_file_location("v41_transfer", _V41)
_v41 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_v41)

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")

HOLD_AUC = 0.85
HOLD_GAP = 0.10
CLIFF_AUC = 0.70
CLIFF_DROP = 0.20
ABS_TOL = 1e-6
ANCHOR_TOL = 0.010

ALL_KEEPS = ("full", "MA", "MB", "zero", "omit")
# Keeps that enter a replayed AUC or the #3 identity check.
DECISION_KEEPS = {
    "family_s41": ("full", "MA", "MB"),
    "family_s42": ("full",),
    "family_s43": ("full", "zero", "MA"),
    "multifamily": ("full", "MA", "MB", "zero", "omit"),
}

TARGET_KEY = {
    1: "TRANSFER_PARTIAL_EXACT_PHI",
    2: "PHASE_RESTORES_JOINT",
    3: "RETAIN_FAILS_WITH_ZERO",
}

# Published stock-induced anchors (hypotheses.md).
ANCHORS = {
    ("family_s41", "phi_full"): 1.000,
    ("family_s41", "phi_alt"): 0.812,
    ("family_s41", "phi_zero"): 0.792,
    ("multifamily", "phi_full"): 1.000,
    ("multifamily", "phi_alt"): 0.660,
    ("multifamily", "phi_phase"): 1.000,
    ("family_s42", "phi_phase"): 1.000,
    ("multifamily", "phi_zero"): 0.592,
    ("multifamily", "phi_retain"): 0.592,
    ("multifamily", "phi_omit"): 0.559,
    ("family_s43", "phi_full"): 1.000,
    ("family_s43", "phi_zero"): 0.750,
    ("family_s43", "phi_retain"): 0.750,
}

_CACHE: dict = {}


def holds(auc, auc_ref):
    if np.isnan(auc) or np.isnan(auc_ref):
        return False
    return auc >= HOLD_AUC or (auc_ref - auc) <= HOLD_GAP


def cliffs(auc, auc_ref):
    if np.isnan(auc_ref):
        return False
    if np.isnan(auc):
        return auc_ref >= HOLD_AUC
    return auc < CLIFF_AUC or (auc_ref - auc) >= CLIFF_DROP


def _states(tpm, n):
    out = []
    for s in reachable_states(tpm, n):
        out.append(tuple((s >> i) & 1 for i in range(n)))
    return out


def _labels(n):
    return tuple(f"N{i}" for i in range(n))


def stock_max_phi(tpm, cm):
    key = ("stock_full", tpm.tobytes(), bytes(cm.tobytes()))
    hit = _CACHE.get(key)
    if hit is not None:
        return hit
    v = classify(tpm, cm, labels=_labels(cm.shape[0]))
    hit = (float(v.max_phi), 0)
    _CACHE[key] = hit
    return hit


def stock_subset_phi(tpm, cm, nodes):
    nodes = tuple(nodes)
    n = cm.shape[0]
    if nodes == tuple(range(n)):
        return stock_max_phi(tpm, cm)
    key = ("stock_sub", tpm.tobytes(), bytes(cm.tobytes()), nodes)
    hit = _CACHE.get(key)
    if hit is not None:
        return hit
    net = pyphi.Network(tpm, cm=cm, node_labels=_labels(n))
    best = None
    errors = 0
    for state in _states(tpm, n):
        try:
            sub = pyphi.Subsystem(net, state, nodes=nodes)
            phi = float(new_big_phi.sia(sub).phi)
        except StateUnreachableError:
            continue
        except Exception:
            errors += 1
            best = None
            break
        best = phi if best is None else max(best, phi)
    hit = (float("nan") if best is None else float(best), errors)
    _CACHE[key] = hit
    return hit


def overlay_subset_phi(tpm, cm, nodes):
    nodes = tuple(nodes)
    n = cm.shape[0]
    key = ("overlay_sub", tpm.tobytes(), bytes(cm.tobytes()), nodes)
    hit = _CACHE.get(key)
    if hit is not None:
        return hit
    sbs = convert.state_by_node2state_by_state(tpm)
    net = MultivaluedNetwork(sbs, [2] * n, cm=cm, node_labels=_labels(n))
    best = None
    errors = 0
    for state in _states(tpm, n):
        try:
            sub = MultivaluedSubsystem(net, state, nodes=nodes)
            phi = float(sia(sub).phi)
        except StateUnreachableError:
            continue
        except Exception:
            errors += 1
            best = None
            break
        best = phi if best is None else max(best, phi)
    hit = (float("nan") if best is None else float(best), errors)
    _CACHE[key] = hit
    return hit


def _bundle(rules):
    tpm = tpm_from_rules(rules)
    cm = cm_from_rules(rules)
    return tpm, cm


def induced_rules(rules, n, keep):
    keep = tuple(keep)
    if keep == tuple(range(n)):
        return rules
    return _v41.induce(rules, n, keep)


def keep_map(form):
    n = form["n"]
    a, m, b = _v41.roles_for(form["family"], n)
    return {
        "full": tuple(range(n)),
        "MA": (m, a),
        "MB": (m, b),
        "zero": tuple(i for i in range(n) if i != b),
        "omit": tuple(i for i in range(n) if i != m),
    }


def _screens(phi_of):
    full = phi_of["full"]
    ma = phi_of["MA"]
    mb = phi_of["MB"]
    if np.isfinite(ma) and np.isfinite(mb):
        alt = 0.5 * (ma + mb)
    else:
        alt = float("nan")
    return {
        "phi_full": full,
        "phi_MA": ma,
        "phi_MB": mb,
        "phi_alt": alt,
        "phi_phase": full,
        "phi_zero": phi_of["zero"],
        "phi_retain": ma,
        "phi_omit": phi_of["omit"],
    }


def score_form(form):
    """Return keep Φ and screens for I/S × stock/overlay.

    Also a list of incomplete decision keeps: stock finite, overlay not.
    """
    n = form["n"]
    rules = form["rules"]
    keeps = keep_map(form)
    full_tpm, full_cm = _bundle(rules)
    raw = {}
    incomplete = []
    for estimand in ("I", "S"):
        raw[estimand] = {}
        for engine in ("stock", "overlay"):
            phi_of = {}
            err_of = {}
            for name, keep in keeps.items():
                if estimand == "I":
                    sub = induced_rules(rules, n, keep)
                    tpm, cm = _bundle(sub)
                    nodes = tuple(range(len(sub)))
                else:
                    tpm, cm = full_tpm, full_cm
                    nodes = keep
                if engine == "stock":
                    if estimand == "I":
                        phi, err = stock_max_phi(tpm, cm)
                    else:
                        phi, err = stock_subset_phi(tpm, cm, nodes)
                else:
                    phi, err = overlay_subset_phi(tpm, cm, nodes)
                phi_of[name] = phi
                err_of[name] = err
            raw[estimand][engine] = {
                "phi": phi_of,
                "err": err_of,
                "screens": _screens(phi_of),
            }
    return raw


def panel_rows(tag, forms):
    rows = []
    bad = []
    t0 = time.time()
    for i, form in enumerate(forms, start=1):
        raw = score_form(form)
        for estimand in ("I", "S"):
            for engine in ("stock", "overlay"):
                block = raw[estimand][engine]
                rec = {
                    "panel": tag,
                    "name": form["name"],
                    "family": form["family"],
                    "n": form["n"],
                    "triadic": form["triadic"],
                    "estimand": estimand,
                    "engine": engine,
                }
                rec.update(block["screens"])
                rec["errors"] = int(sum(block["err"].values()))
                rows.append(rec)
            for name in DECISION_KEEPS[tag]:
                st = raw[estimand]["stock"]["phi"][name]
                ov = raw[estimand]["overlay"]["phi"][name]
                if np.isfinite(st) and not np.isfinite(ov):
                    bad.append({
                        "panel": tag,
                        "name": form["name"],
                        "estimand": estimand,
                        "keep": name,
                        "stock": st,
                    })
        if i == 1 or i % 12 == 0 or i == len(forms):
            print(
                f"    {tag}: {i}/{len(forms)}  "
                f"({time.time() - t0:.1f}s)",
                flush=True,
            )
    return rows, bad


def auc_table(rows, panel, estimand, engine):
    subset = [
        r for r in rows
        if r["panel"] == panel and r["estimand"] == estimand and r["engine"] == engine
    ]
    out = {}
    for key in (
        "phi_full", "phi_alt", "phi_phase", "phi_zero", "phi_retain", "phi_omit",
    ):
        auc, orient = _v41.oriented_auc(
            [r[key] for r in subset], [r["triadic"] for r in subset]
        )
        out[key] = (auc, orient, len(subset))
    return out


def n3_identity(rows, panel, estimand, engine):
    subset = [
        r for r in rows
        if r["panel"] == panel and r["estimand"] == estimand and r["engine"] == engine
    ]
    same = 0
    for r in subset:
        z, a = r["phi_zero"], r["phi_retain"]
        if np.isfinite(z) and np.isfinite(a) and abs(z - a) < 1e-9:
            same += 1
    return same, len(subset)


def key_cell1(full_f, alt_f, full_m, alt_m):
    h_mi = True
    h2 = (not np.isnan(full_f)) and full_f >= HOLD_AUC and cliffs(alt_f, full_f)
    h3 = cliffs(alt_m, full_m)
    h4 = (
        (not np.isnan(full_f)) and (not np.isnan(full_m))
        and full_f >= HOLD_AUC and full_m >= HOLD_AUC
    )
    if (not h_mi) or (not h4):
        return "CONTROLS_FAIL"
    if h2 and h3 and h4:
        return "TRANSFER_HOLDS_EXACT_PHI"
    if (not h2) and h3 and h4:
        return "TRANSFER_PARTIAL_EXACT_PHI"
    if (not h2) and (not h3) and h4:
        return "EXACT_PHI_ROBUST_MI_ONLY"
    if h2 and (not h3) and h4:
        return "FAMILY_N3_ONLY"
    return "UNCLASSIFIED"


def key_cell2(full_m, alt_m):
    phase_m = full_m
    h1 = cliffs(alt_m, full_m)
    h2 = holds(phase_m, full_m)
    h5 = True
    if not h1:
        return "NO_ALT_CLIFF"
    if h1 and (not h2):
        return "PHASE_FAILS_EXACT_PHI"
    if h1 and h2 and h5:
        return "PHASE_RESTORES_JOINT"
    return "UNCLASSIFIED"


def key_cell3(full_m, zero_m, retain_m, full_f, n_same, n_fam):
    h1 = cliffs(zero_m, full_m)
    h2 = holds(retain_m, full_m)
    h5 = (
        (not np.isnan(full_m)) and (not np.isnan(full_f))
        and full_m >= HOLD_AUC and full_f >= HOLD_AUC
        and n_same == n_fam and n_fam > 0
    )
    if not h5:
        return "CONTROLS_FAIL"
    if not h1:
        return "ZERO_DUTY_SOFT"
    if h1 and h2:
        return "RETAIN_SAVES_ZERO_DUTY"
    if h1 and (not h2):
        return "RETAIN_FAILS_WITH_ZERO"
    return "UNCLASSIFIED"


def keys_for(rows, estimand, engine):
    def A(panel, screen):
        return auc_table(rows, panel, estimand, engine)[screen][0]

    k1 = key_cell1(
        A("family_s41", "phi_full"), A("family_s41", "phi_alt"),
        A("multifamily", "phi_full"), A("multifamily", "phi_alt"),
    )
    k2 = key_cell2(A("multifamily", "phi_full"), A("multifamily", "phi_alt"))
    n_same, n_fam = n3_identity(rows, "family_s43", estimand, engine)
    k3 = key_cell3(
        A("multifamily", "phi_full"), A("multifamily", "phi_zero"),
        A("multifamily", "phi_retain"), A("family_s43", "phi_full"),
        n_same, n_fam,
    )
    return {1: k1, 2: k2, 3: k3}


def fmt_auc(x):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "nan"
    return f"{x:.3f}"


def witness_xor():
    rules = [lambda x: x[0] ^ x[1], lambda x: x[0] ^ x[1]]
    tpm, cm = _bundle(rules)
    stock, e1 = stock_max_phi(tpm, cm)
    overlay, e2 = overlay_subset_phi(tpm, cm, (0, 1))
    return {"stock": stock, "overlay": overlay, "errors": int(e1 + e2)}


def witness_parity():
    rules = [
        lambda x: x[1],
        lambda x: x[0] ^ x[2],
        lambda x: x[1],
    ]
    tpm, cm = _bundle(rules)
    pairs = ((0, 1), (0, 2), (1, 2))
    out = {"pairs": {}}
    for nodes in pairs:
        st, _ = stock_subset_phi(tpm, cm, nodes)
        ov, _ = overlay_subset_phi(tpm, cm, nodes)
        out["pairs"]["".join(str(i) for i in nodes)] = {
            "stock": st, "overlay": ov,
        }
    st_full, _ = stock_max_phi(tpm, cm)
    ov_full, _ = overlay_subset_phi(tpm, cm, (0, 1, 2))
    out["full_stock"] = st_full
    out["full_overlay"] = ov_full
    return out


def _finite_pair(a, b):
    return np.isfinite(a) and np.isfinite(b)


_KEEP_SCREENS = (
    ("full", "phi_full"),
    ("MA", "phi_MA"),
    ("MB", "phi_MB"),
    ("zero", "phi_zero"),
    ("omit", "phi_omit"),
)


def engine_gaps(rows, estimand):
    """Gap tallies for one estimand.

    ``decision`` is the preregistered H2 universe (``DECISION_KEEPS``).
    ``allkeep`` scores every keep on every panel and is descriptive only.
    """
    by_key = {}
    for r in rows:
        if r["estimand"] != estimand:
            continue
        by_key[(r["panel"], r["name"], r["engine"])] = r
    panels_names = sorted({
        (r["panel"], r["name"]) for r in rows if r["estimand"] == estimand
    })
    out = {
        "decision": {"ok": True, "n": 0, "max_abs": 0.0, "gaps": []},
        "allkeep": {"ok": True, "n": 0, "max_abs": 0.0, "gaps": []},
    }
    for panel, name in panels_names:
        st = by_key[(panel, name, "stock")]
        ov = by_key[(panel, name, "overlay")]
        for keep, screen in _KEEP_SCREENS:
            in_decision = keep in DECISION_KEEPS[panel]
            buckets = ["allkeep"]
            if in_decision:
                buckets.append("decision")
            a, b = st[screen], ov[screen]
            mismatch = (not _finite_pair(a, b)) or abs(a - b) > ABS_TOL
            gap = None if not _finite_pair(a, b) else abs(float(a) - float(b))
            rec = {
                "panel": panel,
                "name": name,
                "family": st["family"],
                "n": st["n"],
                "keep": keep,
                "stock": a,
                "overlay": b,
                "abs": gap,
                "h2_decision": in_decision,
            }
            for bucket in buckets:
                slot = out[bucket]
                slot["n"] += 1
                if mismatch:
                    slot["ok"] = False
                    if gap is not None:
                        slot["max_abs"] = max(slot["max_abs"], gap)
                    slot["gaps"].append(rec)
                elif gap is not None and gap > slot["max_abs"]:
                    slot["max_abs"] = gap
    for slot in out.values():
        slot["gaps"].sort(key=lambda g: -1.0 if g["abs"] is None else -g["abs"])
    return out


def main():
    t_all = time.time()
    print("AGENDA V4 item 12 — M3 SUBSET-Φ FIDELITY VS V4 items 1–3")
    print("=" * 80)
    print("  cited: item1 TRANSFER_PARTIAL_EXACT_PHI; item2 PHASE_RESTORES_JOINT;")
    print("         item3 RETAIN_FAILS_WITH_ZERO; overlay M2; XOR-dyad caveat")
    print("  pointer: hypotheses.md fixed before this script")
    print(
        f"  protocol: |ΔΦ|≤{ABS_TOL:g}; anchor tol {ANCHOR_TOL}; "
        f"hold AUC≥{HOLD_AUC} or within {HOLD_GAP}; "
        f"cliff AUC<{CLIFF_AUC} or drop≥{CLIFF_DROP}"
    )
    print("=" * 80)
    print()

    print("INSTRUMENT CONTROL")
    print("-" * 80)
    faith = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]
    v0 = vlib(faith, ("W", "S", "C"))
    ctrl = v0.structure == "triadic" and abs(v0.max_phi - 2.0) < 1e-6
    print(
        f"  faithful triad: {v0.structure} Φ={v0.max_phi:.6f}  "
        f"{'PASS' if ctrl else 'FAIL'}"
    )
    tpm, cm = _bundle(faith)
    ov_phi, ov_err = overlay_subset_phi(tpm, cm, (0, 1, 2))
    ov_ok = ov_err == 0 and np.isfinite(ov_phi) and abs(ov_phi - 2.0) < 1e-6
    print(
        f"  overlay faithful max Φ={ov_phi:.6f}  "
        f"{'PASS' if ov_ok else 'FAIL'}"
    )
    if not (ctrl and ov_ok):
        raise SystemExit("ABORT: instrument control failed")
    print()

    print("WITNESSES")
    print("-" * 80)
    wx = witness_xor()
    wp = witness_parity()
    xor_gap = wx["overlay"] - wx["stock"]
    print(
        f"  W_xor stock={wx['stock']:.6f}  overlay={wx['overlay']:.6f}  "
        f"gap={xor_gap:.6f}"
    )
    for name, pair in wp["pairs"].items():
        print(
            f"  W_parity pair {name}: stock={pair['stock']:.6f}  "
            f"overlay={pair['overlay']:.6f}"
        )
    print(
        f"  W_parity full: stock={wp['full_stock']:.6f}  "
        f"overlay={wp['full_overlay']:.6f}"
    )
    print()

    print("BUILD PANELS")
    print("-" * 80)
    panels = {}
    for seed, tag in ((41, "family_s41"), (42, "family_s42"), (43, "family_s43")):
        rng = np.random.default_rng(seed)
        panels[tag] = _v41.build_family_n3(rng)
        n_tri = sum(r["triadic"] for r in panels[tag])
        print(f"  {tag}: {len(panels[tag])} forms ({n_tri} tri) seed={seed}")
    panels["multifamily"] = _v41.build_multifamily()
    n_tri_m = sum(r["triadic"] for r in panels["multifamily"])
    print(f"  multifamily: {len(panels['multifamily'])} forms ({n_tri_m} tri)")
    print()

    print("SCORE stock and overlay (induced and background subset)")
    print("-" * 80)
    rows = []
    incomplete = []
    for tag in ("family_s41", "family_s42", "family_s43", "multifamily"):
        got, bad = panel_rows(tag, panels[tag])
        rows.extend(got)
        incomplete.extend(bad)
    print(f"  incomplete decision keeps: {len(incomplete)}")
    print()

    print("PANEL AUCs")
    print("-" * 80)
    aucs = {}
    for estimand in ("I", "S"):
        for engine in ("stock", "overlay"):
            for tag in ("family_s41", "family_s42", "family_s43", "multifamily"):
                table = auc_table(rows, tag, estimand, engine)
                for screen, (auc, orient, n) in table.items():
                    aucs[(tag, estimand, engine, screen)] = (auc, orient, n)
                    if tag == "family_s42" and screen not in ("phi_full", "phi_phase"):
                        continue
                    if tag == "family_s41" and screen == "phi_omit":
                        continue
                    print(
                        f"  {tag:12s} {estimand}/{engine:7s} {screen:12s}  "
                        f"AUC={fmt_auc(auc)}  orient={orient:+d}"
                    )
    print()

    stock_I = keys_for(rows, "I", "stock")
    over_I = keys_for(rows, "I", "overlay")
    stock_S = keys_for(rows, "S", "stock")
    over_S = keys_for(rows, "S", "overlay")

    print("READING KEYS")
    print("-" * 80)
    for cell in (1, 2, 3):
        print(
            f"  #{cell} stock_I={stock_I[cell]}  overlay_I={over_I[cell]}  "
            f"stock_S={stock_S[cell]}  overlay_S={over_S[cell]}"
        )
    print()

    anchor_misses = []
    for (panel, screen), published in ANCHORS.items():
        got = aucs[(panel, "I", "stock", screen)][0]
        if np.isnan(got) or abs(got - published) > ANCHOR_TOL:
            anchor_misses.append((panel, screen, published, got))
    keys_ok = all(stock_I[c] == TARGET_KEY[c] for c in (1, 2, 3))
    h1 = keys_ok and not anchor_misses

    subset_gaps = engine_gaps(rows, "S")
    induced_gaps = engine_gaps(rows, "I")
    h2_slot = subset_gaps["decision"]
    all_slot = subset_gaps["allkeep"]
    h2 = h2_slot["ok"]
    n_h2, max_h2, gaps_h2 = h2_slot["n"], h2_slot["max_abs"], h2_slot["gaps"]
    n_all, max_all, gaps_all = all_slot["n"], all_slot["max_abs"], all_slot["gaps"]
    ind_h2 = induced_gaps["decision"]
    ind_all = induced_gaps["allkeep"]
    h3 = np.isfinite(xor_gap) and xor_gap >= 0.1
    blocked = len(incomplete) > 0
    h4 = (not blocked) and all(over_I[c] == stock_I[c] for c in (1, 2, 3))
    h5 = (not blocked) and all(over_S[c] == stock_S[c] for c in (1, 2, 3))
    estimand_shift = {
        c: stock_S[c] != TARGET_KEY[c] for c in (1, 2, 3)
    }

    if blocked:
        verdict = "M3_BLOCKED"
    elif not h1:
        verdict = "REIMPLEMENT_FAIL"
    elif (not h4) or (not h5):
        verdict = "M3_FLIPS_VERDICT"
    else:
        verdict = "EXACT_BINARY_DECISIVE"

    def yn(flag):
        if blocked and flag is None:
            return "NOT_ADJUDICATED"
        return "SUPPORTED" if flag else "REFUTED"

    h4_label = "NOT_ADJUDICATED" if blocked else ("SUPPORTED" if h4 else "REFUTED")
    h5_label = "NOT_ADJUDICATED" if blocked else ("SUPPORTED" if h5 else "REFUTED")

    shift_txt = " ".join(
        f"item{c}:{'YES' if estimand_shift[c] else 'NO'}" for c in (1, 2, 3)
    )
    reading = (
        f"{verdict} — stock induced keys "
        f"item1 {stock_I[1]} item2 {stock_I[2]} item3 {stock_I[3]}; "
        f"overlay induced item1 {over_I[1]} item2 {over_I[2]} item3 {over_I[3]}; "
        f"stock subset item1 {stock_S[1]} item2 {stock_S[2]} item3 {stock_S[3]}; "
        f"overlay subset item1 {over_S[1]} item2 {over_S[2]} "
        f"item3 {over_S[3]}; "
        f"H2 decision subset gaps {len(gaps_h2)}/{n_h2} max|Δ|={max_h2:.6g}; "
        f"all-keep subset gaps {len(gaps_all)}/{n_all} max|Δ|={max_all:.6g} "
        f"(descriptive); "
        f"W_xor stock={wx['stock']:.6f} overlay={wx['overlay']:.6f}; "
        f"estimand_shift {shift_txt}"
    )

    def A(panel, screen):
        return aucs[(panel, "I", "stock", screen)][0]

    metrics = (
        f"phi_full_f41={fmt_auc(A('family_s41', 'phi_full'))}; "
        f"phi_alt_f41={fmt_auc(A('family_s41', 'phi_alt'))}; "
        f"phi_zero_f41={fmt_auc(A('family_s41', 'phi_zero'))}; "
        f"phi_full_m={fmt_auc(A('multifamily', 'phi_full'))}; "
        f"phi_alt_m={fmt_auc(A('multifamily', 'phi_alt'))}; "
        f"phi_zero_m={fmt_auc(A('multifamily', 'phi_zero'))}; "
        f"phi_retain_m={fmt_auc(A('multifamily', 'phi_retain'))}; "
        f"phi_omit_m={fmt_auc(A('multifamily', 'phi_omit'))}; "
        f"phi_full_f43={fmt_auc(A('family_s43', 'phi_full'))}; "
        f"phi_zero_f43={fmt_auc(A('family_s43', 'phi_zero'))}; "
        f"phi_retain_f43={fmt_auc(A('family_s43', 'phi_retain'))}; "
        f"phi_phase_f42={fmt_auc(A('family_s42', 'phi_phase'))}; "
        f"xor_stock={wx['stock']:.6f}; xor_overlay={wx['overlay']:.6f}; "
        f"h2_decision_subset_gaps={len(gaps_h2)}/{n_h2}; "
        f"h2_max_abs={max_h2:.6g}; "
        f"allkeep_subset_gaps={len(gaps_all)}/{n_all}; "
        f"allkeep_max_abs={max_all:.6g}; "
        f"decision_induced_gaps={len(ind_h2['gaps'])}/{ind_h2['n']}; "
        f"allkeep_induced_gaps={len(ind_all['gaps'])}/{ind_all['n']}"
    )

    print("HYPOTHESIS TESTS")
    print("-" * 80)
    if anchor_misses:
        for panel, screen, published, got in anchor_misses:
            print(
                f"  anchor miss {panel} {screen}: "
                f"published={published:.3f} got={fmt_auc(got)}"
            )
    print(f"  H1 (stock replay recovers #1–#3):       {yn(h1)}")
    print(f"  H2 (subset Φ agrees within 1e-6):       {yn(h2)}")
    print(f"  H3 (XOR dyad inflates by ≥0.1):         {yn(h3)}")
    print(f"  H4 (overlay-induced keys match):        {h4_label}")
    print(f"  H5 (overlay-subset keys match):         {h5_label}")
    print()
    print("STATUS")
    print(f"  verification grid:    {'PASS' if ctrl and ov_ok else 'FAIL'}")
    print(f"  estimand_shift:       {shift_txt}")
    def _unit_count(items):
        return sum(
            1 for g in items
            if g["abs"] is not None and abs(g["abs"] - 1.0) <= 1e-9
        )

    def _fam_txt(items):
        fam_counts = {}
        for g in items:
            fam_counts[g["family"]] = fam_counts.get(g["family"], 0) + 1
        return " ".join(f"{k}={fam_counts[k]}" for k in sorted(fam_counts))

    print(
        f"  H2_decision_subset_gaps: {len(gaps_h2)}/{n_h2}  "
        f"max|Δ|={max_h2:.6g}"
    )
    print(
        f"  allkeep_subset_gaps:  {len(gaps_all)}/{n_all}  "
        f"max|Δ|={max_all:.6g}  descriptive"
    )
    print(
        f"  decision_induced_gaps: {len(ind_h2['gaps'])}/{ind_h2['n']}  "
        f"max|Δ|={ind_h2['max_abs']:.6g}  descriptive"
    )
    print(
        f"  allkeep_induced_gaps: {len(ind_all['gaps'])}/{ind_all['n']}  "
        f"max|Δ|={ind_all['max_abs']:.6g}  descriptive"
    )
    print(f"  H2_gap_unit:          {_unit_count(gaps_h2)}/{len(gaps_h2)}")
    print(f"  H2_gap_families:      {_fam_txt(gaps_h2)}")
    print(f"  allkeep_gap_unit:     {_unit_count(gaps_all)}/{len(gaps_all)}")
    print(f"  allkeep_gap_families: {_fam_txt(gaps_all)}")
    for g in gaps_h2:
        if g["abs"] is None or abs(g["abs"] - 1.0) > 1e-9:
            gs = "nan" if g["abs"] is None else f"{g['abs']:.6g}"
            print(
                f"  H2 nonunit gap:       {g['panel']} {g['name']} "
                f"keep={g['keep']} |Δ|={gs}"
            )
    if gaps_h2:
        print("  largest H2 decision gaps:")
        for g in gaps_h2[:8]:
            gs = "nan" if g["abs"] is None else f"{g['abs']:.6g}"
            print(
                f"    {g['panel']} {g['family']}:{g['name']} n={g['n']} "
                f"keep={g['keep']} |Δ|={gs}"
            )
    if incomplete:
        print("  incomplete keeps (first 8):")
        for item in incomplete[:8]:
            print(
                f"    {item['panel']} {item['name']} {item['estimand']} "
                f"{item['keep']}"
            )
    print()
    print(f"  verdict: {verdict}")
    print(f"  reading: {reading}")
    print(f"  metrics: {metrics}")
    print("  best next:         V4 item 11 answered, GRADED_HOLDS")
    print(f"  elapsed_total={round(time.time() - t_all, 1)}s")
    print("=" * 80)

    os.makedirs(RESULTS, exist_ok=True)
    screen_fields = [
        "phi_full", "phi_alt", "phi_phase", "phi_zero", "phi_retain",
        "phi_omit", "phi_MA", "phi_MB",
    ]
    with open(os.path.join(RESULTS, "panel.csv"), "w", newline="") as fh:
        fields = [
            "panel", "family", "n", "name", "triadic", "estimand", "engine",
            *screen_fields, "errors",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for r in rows:
            out = {k: r[k] for k in (
                "panel", "family", "n", "name", "triadic", "estimand", "engine", "errors",
            )}
            for k in screen_fields:
                val = r[k]
                out[k] = "" if not np.isfinite(val) else f"{val:.6f}"
            w.writerow(out)

    with open(os.path.join(RESULTS, "curves.csv"), "w", newline="") as fh:
        fields = ["panel", "estimand", "engine", "screen", "auc", "orient", "n_forms"]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for (panel, estimand, engine, screen), (auc, orient, n) in sorted(aucs.items()):
            w.writerow({
                "panel": panel,
                "estimand": estimand,
                "engine": engine,
                "screen": screen,
                "auc": "" if np.isnan(auc) else f"{auc:.6f}",
                "orient": orient,
                "n_forms": n,
            })

    with open(os.path.join(RESULTS, "gaps.csv"), "w", newline="") as fh:
        fields = [
            "panel", "family", "n", "name", "keep", "stock", "overlay", "abs",
            "h2_decision",
        ]
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        for g in gaps_all:
            w.writerow({
                "panel": g["panel"],
                "family": g["family"],
                "n": g["n"],
                "name": g["name"],
                "keep": g["keep"],
                "stock": "" if not np.isfinite(g["stock"]) else f"{g['stock']:.6f}",
                "overlay": "" if not np.isfinite(g["overlay"]) else f"{g['overlay']:.6f}",
                "abs": "" if g["abs"] is None else f"{g['abs']:.6e}",
                "h2_decision": "yes" if g["h2_decision"] else "no",
            })

    def _json_phi(x):
        if isinstance(x, float) and not np.isfinite(x):
            return None
        return x

    summary = {
        "verdict": verdict,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": None if blocked else h4,
        "h5": None if blocked else h5,
        "blocked": blocked,
        "n_incomplete": len(incomplete),
        "keys": {
            "stock_I": stock_I,
            "overlay_I": over_I,
            "stock_S": stock_S,
            "overlay_S": over_S,
        },
        "estimand_shift": estimand_shift,
        "anchor_misses": [
            {"panel": p, "screen": s, "published": pub, "got": _json_phi(got)}
            for p, s, pub, got in anchor_misses
        ],
        "h2_universe": "DECISION_KEEPS",
        "h2_decision_comparisons": n_h2,
        "h2_decision_gaps": len(gaps_h2),
        "h2_decision_max_abs": max_h2,
        "allkeep_subset_comparisons": n_all,
        "allkeep_subset_gaps": len(gaps_all),
        "allkeep_subset_max_abs": max_all,
        "allkeep_subset_note": "descriptive; not the H2 universe",
        "decision_induced_comparisons": ind_h2["n"],
        "decision_induced_gaps": len(ind_h2["gaps"]),
        "allkeep_induced_comparisons": ind_all["n"],
        "allkeep_induced_gaps": len(ind_all["gaps"]),
        "w_xor": {k: _json_phi(v) if isinstance(v, float) else v for k, v in wx.items()},
        "w_parity": {
            "full_stock": _json_phi(wp["full_stock"]),
            "full_overlay": _json_phi(wp["full_overlay"]),
            "pairs": {
                name: {ek: _json_phi(ev) for ek, ev in pair.items()}
                for name, pair in wp["pairs"].items()
            },
        },
        "reading": reading,
        "metrics": metrics,
        "scope": "in-silico exact IIT-4.0, n<=4 Boolean panels of V4 items 1-3",
    }
    with open(os.path.join(RESULTS, "summary.json"), "w") as fh:
        json.dump(summary, fh, indent=2)
        fh.write("\n")


if __name__ == "__main__":
    main()
