"""Strand G residual — cycle ordering versus the basin-mode EoA gap.

Hypotheses fixed in hypotheses.md before this script produced numbers.
Instruments: org_frontier.ergodicity.eoa (basin) and
org_frontier.ergodicity.settling (cycle-ordering summaries).

Run (full panel):
  python org_frontier/studies/ergodic_cycle_ordering/analyze_ordering.py

Run (CI subset — no random n=3, no n=4; H0–H4 NOT_TESTABLE):
  python org_frontier/studies/ergodic_cycle_ordering/analyze_ordering.py --ci
"""

from __future__ import annotations

import argparse
import csv
import math
import os
import random
import sys
from typing import Callable

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from org_frontier.ergodicity._boolean_ergo import (
    LABELS3,
    PANEL_B1,
    instrument_gates,
    rules_ejected_latch,
    rules_ejected_latch_or,
)
from org_frontier.ergodicity.eoa import (
    REFERENCE_BASIN,
    attractor_partition,
    bit_observable,
    rules_to_next_map,
    run_eoa_parties,
    trajectory_time_average,
    uniform_ensemble,
)
from org_frontier.ergodicity.settling import (
    circular_mean_abs_remainder,
    cofilip_sync_of_cycle,
    exact_basin_gap,
    finite_T_time_average,
    flip_signature,
    hamming_party_rate_of_cycle,
    lag1_autocorr,
    order_excess_of_sequence,
    order_index_of_sequence,
    phase_lag_of_cycle,
    summarize_cycle_ordering,
    summarize_oscillation,
)
from org_frontier.classifier import forms as cforms

HERE = os.path.dirname(__file__)
RESULTS = os.path.join(HERE, "results")
BASIN_FORMS = os.path.join(HERE, "..", "ergodic_eoa_basin", "results", "forms.csv")

# Frozen (hypotheses.md).
HORIZON_PRIMARY = 64
T_GRID = (16, 32, 64, 128, 256, 512)
SEED_RANDOM = 20260930
N_RANDOM = 20
PERM_SEED = 20260930
N_PERM = 2000
N_BOOT = 2000
GAP_MATCH_TOL = 1e-6
CLOSED_FORM_TOL = 1e-8
BASIN_EXACT_TOL = 1e-6
SHRINK_PASS = 0.50
SLOPE_LO = -1.25
SLOPE_HI = -0.75
CV_MAX = 0.02
MATCH_ABS = 1e-3
MATCH_RHO = 0.90
AUC_TOL = 0.05
RHO_TOL = 0.10
SIGN_EPS = 0.05
COLLINEAR_R = 0.99
IDENTITY_MAE = 1e-3
VAR_EPS = 1e-15
PRED_REBUILD_TOL = 1e-9

PURE_ORDER = (
    "order_index",
    "order_excess",
    "cofilip_sync",
    "phase_lag",
    "lag1_autocorr",
)
AMPLITUDE = ("hamming_party_rate", "party_osc_frac", "mean_cycle_var")
REMAINDER = ("pred_gap_cycle", "remainder_allstarts")

GATE_PALETTE = ("AND", "OR", "XOR", "NAND", "NOR", "XNOR", "COPY0", "COPY1")
INPUT_PAIRS = ((0, 1), (0, 2), (1, 2))


def _gate(name: str, a: int, b: int) -> Callable:
    if name == "AND":
        return lambda x, a=a, b=b: x[a] & x[b]
    if name == "OR":
        return lambda x, a=a, b=b: x[a] | x[b]
    if name == "XOR":
        return lambda x, a=a, b=b: x[a] ^ x[b]
    if name == "NAND":
        return lambda x, a=a, b=b: 1 - (x[a] & x[b])
    if name == "NOR":
        return lambda x, a=a, b=b: 1 - (x[a] | x[b])
    if name == "XNOR":
        return lambda x, a=a, b=b: 1 - (x[a] ^ x[b])
    if name == "COPY0":
        return lambda x, a=a, b=b: x[a]
    if name == "COPY1":
        return lambda x, a=a, b=b: x[b]
    raise ValueError(name)


def _rules_signature(rules) -> frozenset:
    rows = []
    for s in range(8):
        cur = tuple((s >> i) & 1 for i in range(3))
        rows.append(tuple(int(r(cur)) for r in rules))
    return frozenset([tuple(rows)])


def _sig_of_builder(builder) -> frozenset:
    return _rules_signature(builder())


def build_random_n3(seed: int, n: int, ban: set) -> list:
    rng = random.Random(seed)
    out = []
    attempts = 0
    while len(out) < n and attempts < n * 200:
        attempts += 1
        rules = []
        for _ in range(3):
            g = rng.choice(GATE_PALETTE)
            pair = rng.choice(INPUT_PAIRS)
            rules.append(_gate(g, pair[0], pair[1]))
        sig = _rules_signature(rules)
        if sig in ban:
            continue
        ban.add(sig)
        name = f"rand3_{seed}_{len(out):02d}"
        frozen = list(rules)
        out.append((name, (lambda frozen=frozen: list(frozen))))
    if len(out) < n:
        raise RuntimeError(f"only drew {len(out)}/{n} random forms")
    return out


LABELS4 = ("W", "S", "C1", "C2")


def rules_and_pool():
    return [
        lambda x: x[1],
        lambda x: x[0] & x[2] & x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_or_pool():
    return [
        lambda x: x[1],
        lambda x: x[0] | x[2] | x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_maj_homog():
    def maj(x):
        return 1 if sum(x) >= 2 else 0

    return [maj, maj, maj, maj]


def rules_chain_ws_c1c2():
    return [
        lambda x: x[1],
        lambda x: x[0],
        lambda x: x[1],
        lambda x: x[2],
    ]


def rules_hub_s():
    return [
        lambda x: x[1],
        lambda x: x[0] ^ x[2] ^ x[3],
        lambda x: x[1],
        lambda x: x[1],
    ]


def rules_dual_latch():
    return [
        lambda x: x[1],
        lambda x: (x[0] & x[2] & x[3]) | x[1],
        lambda x: x[1],
        lambda x: x[1],
    ]


PANEL_N4 = {
    "and_pool": rules_and_pool,
    "or_pool": rules_or_pool,
    "maj_homog": rules_maj_homog,
    "chain_ws_c1c2": rules_chain_ws_c1c2,
    "hub_s": rules_hub_s,
    "dual_latch": rules_dual_latch,
}


def build_panel(ci: bool):
    panel = []
    for name, builder in PANEL_B1.items():
        panel.append((name, builder, LABELS3, "g2_core"))
    for name, builder in cforms.FORMS.items():
        panel.append((name, builder, LABELS3, "classifier"))
    panel.append(("ejected_latch", rules_ejected_latch, LABELS3, "ejection"))
    panel.append(("ejected_latch_or", rules_ejected_latch_or, LABELS3, "ejection"))
    if not ci:
        ban = {_sig_of_builder(b) for _, b, _, _ in panel if len(b()) == 3}
        for name, builder in build_random_n3(SEED_RANDOM, N_RANDOM, ban):
            panel.append((name, builder, LABELS3, "random_n3"))
        for name, builder in PANEL_N4.items():
            panel.append((name, builder, LABELS4, "n4"))
    return panel


def load_basin_committed():
    out = {}
    with open(BASIN_FORMS, newline="") as fh:
        for row in csv.DictReader(fh):
            if row["mode"] != "basin":
                continue
            if abs(float(row["noise"]) - 0.0) > 1e-12:
                continue
            out[row["form"]] = row
    return out


def standardize(xs):
    m = sum(xs) / float(len(xs))
    var = sum((x - m) ** 2 for x in xs) / float(len(xs))
    sd = math.sqrt(var) if var > 0 else 1.0
    if sd < 1e-15:
        sd = 1.0
    return [(x - m) / sd for x in xs], m, sd


def _var(xs):
    m = sum(xs) / float(len(xs))
    return sum((x - m) ** 2 for x in xs) / float(len(xs))


def _ranks(vals):
    n = len(vals)
    order = sorted(range(n), key=lambda i: vals[i])
    r = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
            j += 1
        avg = 0.5 * (i + j) + 1.0
        for k in range(i, j + 1):
            r[order[k]] = avg
        i = j + 1
    return r


def _pearson(a, b):
    n = len(a)
    ma = sum(a) / n
    mb = sum(b) / n
    num = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    da = math.sqrt(sum((a[i] - ma) ** 2 for i in range(n)))
    db = math.sqrt(sum((b[i] - mb) ** 2 for i in range(n)))
    if da == 0 or db == 0:
        return float("nan")
    return num / (da * db)


def spearman_rho(xs, ys):
    n = len(xs)
    if n < 3:
        return float("nan"), float("nan")
    rx, ry = _ranks(xs), _ranks(ys)
    rho = _pearson(rx, ry)
    if math.isnan(rho):
        return rho, float("nan")
    rng = random.Random(PERM_SEED)
    extreme = 0
    for _ in range(N_PERM):
        shuffled = list(ry)
        rng.shuffle(shuffled)
        r = _pearson(rx, shuffled)
        if math.isnan(r) or abs(r) >= abs(rho) - 1e-15:
            extreme += 1
    return rho, extreme / float(N_PERM)


def partial_spearman(xs, ys, controls):
    n = len(xs)
    if n < 3:
        return float("nan"), float("nan")
    rx, ry = _ranks(xs), _ranks(ys)
    R = [_ranks(c) for c in controls]
    k = 1 + len(R)

    def residualize(target):
        AtA = [[0.0] * k for _ in range(k)]
        Aty = [0.0] * k
        for i in range(n):
            row = [1.0] + [R[j][i] for j in range(len(R))]
            for a in range(k):
                Aty[a] += row[a] * target[i]
                for b in range(k):
                    AtA[a][b] += row[a] * row[b]
        M = [AtA[a][:] + [Aty[a]] for a in range(k)]
        for col in range(k):
            pivot = col
            for r in range(col + 1, k):
                if abs(M[r][col]) > abs(M[pivot][col]):
                    pivot = r
            M[col], M[pivot] = M[pivot], M[col]
            if abs(M[col][col]) < 1e-15:
                return [float("nan")] * n
            div = M[col][col]
            for c in range(col, k + 1):
                M[col][c] /= div
            for r in range(k):
                if r == col:
                    continue
                fac = M[r][col]
                for c in range(col, k + 1):
                    M[r][c] -= fac * M[col][c]
        beta = [M[a][k] for a in range(k)]
        out = []
        for i in range(n):
            pred = beta[0] + sum(beta[1 + j] * R[j][i] for j in range(len(R)))
            out.append(target[i] - pred)
        return out

    ex = residualize(rx)
    ey = residualize(ry)
    if any(math.isnan(v) for v in ex + ey):
        return float("nan"), float("nan")
    rho = _pearson(ex, ey)
    if math.isnan(rho):
        return rho, float("nan")
    rng = random.Random(PERM_SEED)
    extreme = 0
    for _ in range(N_PERM):
        shuffled = list(ey)
        rng.shuffle(shuffled)
        r = _pearson(ex, shuffled)
        if math.isnan(r) or abs(r) >= abs(rho) - 1e-15:
            extreme += 1
    return rho, extreme / float(N_PERM)


def logistic_fit(y, X_cols):
    n = len(y)
    k = 1 + len(X_cols)
    rows = []
    for i in range(n):
        rows.append([1.0] + [X_cols[j][i] for j in range(len(X_cols))])
    beta = [0.0] * k
    for _ in range(50):
        Wz = [0.0] * k
        H = [[0.0] * k for _ in range(k)]
        for i in range(n):
            eta = sum(beta[a] * rows[i][a] for a in range(k))
            if eta >= 0:
                p = 1.0 / (1.0 + math.exp(-eta))
            else:
                e = math.exp(eta)
                p = e / (1.0 + e)
            w = max(p * (1.0 - p), 1e-12)
            resid = y[i] - p
            for a in range(k):
                Wz[a] += rows[i][a] * resid
                for b in range(k):
                    H[a][b] += w * rows[i][a] * rows[i][b]
        M = [H[a][:] + [Wz[a]] for a in range(k)]
        singular = False
        for col in range(k):
            pivot = col
            for r in range(col + 1, k):
                if abs(M[r][col]) > abs(M[pivot][col]):
                    pivot = r
            M[col], M[pivot] = M[pivot], M[col]
            if abs(M[col][col]) < 1e-15:
                singular = True
                break
            div = M[col][col]
            for c in range(col, k + 1):
                M[col][c] /= div
            for r in range(k):
                if r == col:
                    continue
                fac = M[r][col]
                for c in range(col, k + 1):
                    M[r][c] -= fac * M[col][c]
        if singular:
            break
        delta = [M[a][k] for a in range(k)]
        beta = [beta[a] + delta[a] for a in range(k)]
        if max(abs(d) for d in delta) < 1e-10:
            break
    H = [[0.0] * k for _ in range(k)]
    for i in range(n):
        eta = sum(beta[a] * rows[i][a] for a in range(k))
        if eta >= 0:
            p = 1.0 / (1.0 + math.exp(-eta))
        else:
            e = math.exp(eta)
            p = e / (1.0 + e)
        w = max(p * (1.0 - p), 1e-12)
        for a in range(k):
            for b in range(k):
                H[a][b] += w * rows[i][a] * rows[i][b]
    aug = [H[a][:] + [1.0 if a == b else 0.0 for b in range(k)] for a in range(k)]
    invertible = True
    for col in range(k):
        pivot = col
        for r in range(col + 1, k):
            if abs(aug[r][col]) > abs(aug[pivot][col]):
                pivot = r
        aug[col], aug[pivot] = aug[pivot], aug[col]
        if abs(aug[col][col]) < 1e-15:
            invertible = False
            break
        div = aug[col][col]
        for c in range(2 * k):
            aug[col][c] /= div
        for r in range(k):
            if r == col:
                continue
            fac = aug[r][col]
            for c in range(2 * k):
                aug[r][c] -= fac * aug[col][c]
    ses, ps = [], []
    for a in range(k):
        if not invertible or aug[a][k + a] < 0:
            ses.append(float("nan"))
            ps.append(float("nan"))
            continue
        se = math.sqrt(aug[a][k + a])
        ses.append(se)
        if se <= 0 or math.isnan(se):
            ps.append(float("nan"))
        else:
            z = abs(beta[a] / se)
            ps.append(math.erfc(z / math.sqrt(2.0)))
    return beta, ses, ps


def rank_auc(scores, labels) -> float:
    pos = [s for s, lab in zip(scores, labels) if lab]
    neg = [s for s, lab in zip(scores, labels) if not lab]
    if not pos or not neg:
        return float("nan")
    wins = sum((p > n_) + 0.5 * (p == n_) for p in pos for n_ in neg)
    return wins / (len(pos) * len(neg))


def auc_permutation_p(scores, labels):
    obs = rank_auc(scores, labels)
    if math.isnan(obs):
        return obs, float("nan")
    rng = random.Random(PERM_SEED)
    extreme = 0
    for _ in range(N_PERM):
        shuffled = list(labels)
        rng.shuffle(shuffled)
        a = rank_auc(scores, shuffled)
        if math.isnan(a) or abs(a - 0.5) >= abs(obs - 0.5) - 1e-15:
            extreme += 1
    return obs, extreme / float(N_PERM)


def bootstrap_auc_ci(scores, labels):
    pos_idx = [i for i, lab in enumerate(labels) if lab]
    neg_idx = [i for i, lab in enumerate(labels) if not lab]
    if not pos_idx or not neg_idx:
        return float("nan"), float("nan"), float("nan")
    rng = random.Random(PERM_SEED)
    aucs = []
    for _ in range(N_BOOT):
        pi = [pos_idx[rng.randrange(len(pos_idx))] for _ in range(len(pos_idx))]
        ni = [neg_idx[rng.randrange(len(neg_idx))] for _ in range(len(neg_idx))]
        sc = [scores[i] for i in pi + ni]
        lb = [True] * len(pi) + [False] * len(ni)
        aucs.append(rank_auc(sc, lb))
    aucs.sort()
    lo = aucs[int(0.025 * (N_BOOT - 1))]
    hi = aucs[int(0.975 * (N_BOOT - 1))]
    return rank_auc(scores, labels), lo, hi


def ols_slope(xs, ys):
    n = len(xs)
    if n < 2:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    if den <= 0:
        return float("nan")
    return num / den


def write_csv(path, rows, fields=None):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not rows:
        if fields:
            with open(path, "w", newline="") as fh:
                csv.DictWriter(fh, fieldnames=fields).writeheader()
        return
    if fields is None:
        fields = []
        seen = set()
        for r in rows:
            for k in r.keys():
                if k not in seen:
                    seen.add(k)
                    fields.append(k)
    with open(path, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            out = {}
            for k in fields:
                v = r.get(k, "")
                if isinstance(v, float):
                    if math.isinf(v):
                        out[k] = "inf" if v > 0 else "-inf"
                    elif math.isnan(v):
                        out[k] = "nan"
                    else:
                        out[k] = f"{v:.8f}"
                elif isinstance(v, bool):
                    out[k] = int(v)
                else:
                    out[k] = v
            w.writerow(out)


def _fmt(v, spec=".6f"):
    if isinstance(v, float) and math.isnan(v):
        return "nan"
    if isinstance(v, float) and math.isinf(v):
        return "inf" if v > 0 else "-inf"
    if isinstance(v, float):
        return format(v, spec)
    return str(v)


def status_line(label, status):
    print(f"{label:<56}{status}")


def max_closed_form_error(nxt, parties, horizon):
    n = len(next(iter(nxt)))
    worst = 0.0
    for idx in parties:
        obs = bit_observable(idx)
        for start in uniform_ensemble(n):
            closed = finite_T_time_average(nxt, start, obs, horizon)
            walked = trajectory_time_average(
                nxt, start, obs, horizon=horizon, noise=0.0
            )
            worst = max(worst, abs(closed - walked))
    return worst


def cycle_detail(name, nxt, labels, parties, horizon, summary):
    """Per-(cycle, party bit) audit rows. Checks the form-level prediction."""
    n = len(labels)
    part = attractor_partition(nxt)
    cycles = part["cycles"]
    ens = uniform_ensemble(n)
    mass = [0] * len(cycles)
    for st in ens:
        mass[part["basin_of"][st]] += 1
    total = float(len(ens))
    n_parties = len(parties)
    pred_acc = 0.0
    rows = []
    for i, cyc in enumerate(cycles):
        weight = mass[i] / total
        sig = flip_signature(cyc, parties)
        sync = cofilip_sync_of_cycle(cyc, parties)
        lag = phase_lag_of_cycle(cyc, parties)
        ham = hamming_party_rate_of_cycle(cyc, parties)
        for idx in parties:
            vals = [float(st[idx]) for st in cyc]
            pred = circular_mean_abs_remainder(vals, horizon)
            pred_acc += weight * pred / float(n_parties)
            ac = lag1_autocorr(vals)
            rows.append(
                {
                    "form": name,
                    "cycle_index": i,
                    "period": len(cyc),
                    "basin_mass": weight,
                    "party_index": idx,
                    "party_label": labels[idx],
                    "signature": sig,
                    "cofilip_sync": sync,
                    "phase_lag": lag,
                    "hamming_party_rate": ham,
                    "pred_abs_remainder": pred,
                    "order_index": order_index_of_sequence(vals, horizon),
                    "order_excess": order_excess_of_sequence(vals, horizon),
                    "lag1_autocorr": 0.0 if ac is None else ac,
                }
            )
    if abs(pred_acc - summary.pred_gap_cycle) > PRED_REBUILD_TOL:
        raise RuntimeError(
            f"{name}: rebuilt pred_gap_cycle {pred_acc} != summary {summary.pred_gap_cycle}"
        )
    return rows


def evaluate_form(name, builder, labels, group, committed, *, with_grid):
    rules = builder()
    n = len(labels)
    parties = tuple(i for i, lab in enumerate(labels) if lab != "S")
    nxt = rules_to_next_map(rules, n=n)
    crow = committed[name]
    whole_structure = crow["whole_structure"]
    whole_phi = float(crow["whole_phi"])
    committed_gap = float(crow["gap_mean"])

    party_res = run_eoa_parties(
        nxt,
        parties,
        labels=labels,
        horizon=HORIZON_PRIMARY,
        noise=0.0,
        reference_mode=REFERENCE_BASIN,
        n=n,
    )
    gap_party = party_res.gap_mean
    closed_err = max_closed_form_error(nxt, parties, HORIZON_PRIMARY)
    basin_exact = exact_basin_gap(nxt, parties, horizon=HORIZON_PRIMARY, n=n)
    ordering = summarize_cycle_ordering(
        nxt, parties, horizon=HORIZON_PRIMARY, n=n
    )
    osc = summarize_oscillation(nxt, parties, n=n)
    cycle_rows = cycle_detail(name, nxt, labels, parties, HORIZON_PRIMARY, ordering)

    gaps_T = {}
    slope = float("nan")
    cv_gapT = float("nan")
    if with_grid:
        for T in T_GRID:
            res_T = run_eoa_parties(
                nxt,
                parties,
                labels=labels,
                horizon=T,
                noise=0.0,
                reference_mode=REFERENCE_BASIN,
                n=n,
            )
            gaps_T[T] = res_T.gap_mean
        logT = [math.log(T) for T in T_GRID]
        logG = [math.log(gaps_T[T] + 1e-12) for T in T_GRID]
        slope = ols_slope(logT, logG)
        gapT_vals = [gaps_T[T] * T for T in T_GRID]
        mean_gapT = sum(gapT_vals) / len(gapT_vals)
        if mean_gapT > 0:
            var_gapT = sum((v - mean_gapT) ** 2 for v in gapT_vals) / len(gapT_vals)
            cv_gapT = math.sqrt(var_gapT) / mean_gapT
        else:
            cv_gapT = 0.0

    row = {
        "form": name,
        "group": group,
        "n": n,
        "whole_structure": whole_structure,
        "whole_phi": whole_phi,
        "triadic": whole_structure == "triadic",
        "committed_gap": committed_gap,
        "gap_party": gap_party,
        "gap_match": abs(gap_party - committed_gap) <= GAP_MATCH_TOL,
        "closed_form_err": closed_err,
        "exact_basin_gap": basin_exact,
        "basin_exact_match": abs(basin_exact - gap_party) <= BASIN_EXACT_TOL,
        "closed_form_match": closed_err <= CLOSED_FORM_TOL,
        "pred_gap_cycle": ordering.pred_gap_cycle,
        "remainder_allstarts": ordering.remainder_allstarts,
        "order_index": ordering.order_index,
        "order_excess": ordering.order_excess,
        "cofilip_sync": ordering.cofilip_sync,
        "phase_lag": ordering.phase_lag,
        "lag1_autocorr": ordering.lag1_autocorr,
        "hamming_party_rate": ordering.hamming_party_rate,
        "party_osc_frac": osc.party_osc_frac,
        "mean_cycle_var": osc.mean_cycle_var,
        "dominant_signature": ordering.dominant_signature,
        "n_attractors": ordering.n_attractors,
        "mean_period": osc.mean_period,
        "t_scale_slope": slope,
        "gapT_cv": cv_gapT,
        "abs_pred_minus_gap": abs(ordering.pred_gap_cycle - gap_party),
    }
    for T in T_GRID:
        row[f"gap_T{T}"] = gaps_T.get(T, float("nan"))
    return row, cycle_rows


def absorption(gaps, triadic, phis, covariate, *, allow_identity):
    """Shrink rule, plus the identity clause for remainder covariates."""
    y = [1.0 if t else 0.0 for t in triadic]
    constant = _var(covariate) < VAR_EPS
    pearson = _pearson(gaps, covariate)
    mae = sum(abs(a - b) for a, b in zip(gaps, covariate)) / float(len(gaps))
    identity = bool(
        allow_identity
        and (not math.isnan(pearson))
        and abs(pearson) >= COLLINEAR_R
        and mae <= IDENTITY_MAE
    )
    if constant:
        # The gap–Φ correlation does not depend on the covariate. A
        # constant control cannot be partialled out; the mediation
        # hypothesis is REFUTED. Pearson against a constant is undefined.
        rho_uni, rho_uni_p = spearman_rho(gaps, phis)
        return {
            "beta_uni": float("nan"),
            "p_uni": float("nan"),
            "beta_partial": float("nan"),
            "p_partial": float("nan"),
            "beta_ratio": float("nan"),
            "rho_uni": rho_uni,
            "rho_uni_p": rho_uni_p,
            "rho_partial": float("nan"),
            "rho_partial_p": float("nan"),
            "pearson_gap": float("nan"),
            "mae_gap": mae,
            "identity": False,
            "passes": False,
            "exclude": False,
            "spearman_drop": False,
        }
    g_std, _, _ = standardize(gaps)
    c_std, _, _ = standardize(covariate)
    b_uni, _, p_uni = logistic_fit(y, [g_std])
    b_part, _, p_part = logistic_fit(y, [g_std, c_std])
    beta_uni = b_uni[1]
    beta_partial = b_part[1]
    if abs(beta_uni) < 1e-15 or math.isnan(beta_uni) or math.isnan(beta_partial):
        ratio = float("nan")
    else:
        ratio = abs(beta_partial) / abs(beta_uni)
    rho_uni, rho_uni_p = spearman_rho(gaps, phis)
    rho_part, rho_part_p = partial_spearman(gaps, phis, [covariate])
    spearman_drop = (
        (not math.isnan(rho_uni))
        and (not math.isnan(rho_part))
        and abs(rho_part) < abs(rho_uni)
    )
    shrink = (not math.isnan(ratio)) and ratio <= SHRINK_PASS and spearman_drop
    passes = (not constant) and (identity or shrink)
    return {
        "beta_uni": beta_uni,
        "p_uni": p_uni[1],
        "beta_partial": beta_partial,
        "p_partial": p_part[1],
        "beta_ratio": ratio,
        "rho_uni": rho_uni,
        "rho_uni_p": rho_uni_p,
        "rho_partial": rho_part,
        "rho_partial_p": rho_part_p,
        "pearson_gap": pearson,
        "mae_gap": mae,
        "identity": identity,
        "passes": passes,
        "exclude": identity,
        "spearman_drop": spearman_drop,
    }


def _finite(v):
    return isinstance(v, float) and not math.isnan(v) and not math.isinf(v)


def ranking_winner(mech_rows):
    eligible = [
        m
        for m in mech_rows
        if m["passes"] and not m["exclude"] and _finite(m["beta_ratio"])
    ]

    def key(m):
        drop = 0.0
        if _finite(m["rho_uni"]) and _finite(m["rho_partial"]):
            drop = abs(m["rho_uni"]) - abs(m["rho_partial"])
        return (m["beta_ratio"], -drop)

    if not eligible:
        return ""
    eligible.sort(key=key)
    return eligible[0]["covariate"]


def descriptive_lowest(mech_rows):
    cands = [
        m
        for m in mech_rows
        if (not m["exclude"]) and _finite(m["beta_ratio"])
    ]
    if not cands:
        return None
    cands.sort(key=lambda m: m["beta_ratio"])
    return cands[0]


def verdict_word(h0, h1, h3, winner):
    if not h0:
        return "ORDERING_ASSOC_FLUKE"
    if winner in PURE_ORDER:
        return "ORDERING_DRIVES_GAP"
    if winner == "pred_gap_cycle":
        return "CYCLE_REMAINDER_ABSORBS"
    if winner == "remainder_allstarts":
        return "ALLSTART_REMAINDER_ABSORBS"
    if winner in AMPLITUDE:
        return "AMPLITUDE_NOT_ORDER"
    if not winner:
        if h1 and h3:
            return "REMAINDER_NOT_ORDER"
        return "ORDERING_NULL"
    return "ORDERING_INCONCLUSIVE"


def h5_ok(form_rows):
    return all(
        r["gap_match"] and r["basin_exact_match"] and r["closed_form_match"]
        for r in form_rows
    )


def print_h5(form_rows, status):
    status_line("H5 (closed form and committed gaps):", status)
    worst_closed = max(r["closed_form_err"] for r in form_rows)
    worst_csv = max(abs(r["gap_party"] - r["committed_gap"]) for r in form_rows)
    worst_basin = max(abs(r["exact_basin_gap"] - r["gap_party"]) for r in form_rows)
    print(
        f"  max_closed_err={_fmt(worst_closed, '.3e')}  "
        f"max|gap-csv|={_fmt(worst_csv, '.3e')}  "
        f"max|exact-gap|={_fmt(worst_basin, '.3e')}"
    )


def print_absorption(label, med):
    status_line(label, "SUPPORTED" if med["passes"] else "REFUTED")
    ident = "1" if med["identity"] else "0"
    print(
        f"  β_ratio={_fmt(med['beta_ratio'])}  "
        f"partial_ρ={_fmt(med['rho_partial'])}  "
        f"ρ_uni={_fmt(med['rho_uni'])}  "
        f"pearson={_fmt(med['pearson_gap'])}  "
        f"MAE={_fmt(med['mae_gap'], '.3e')}  "
        f"identity={ident}"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ci", action="store_true", help="CI subset (no random n=3, no n=4)")
    args = ap.parse_args()
    ci = args.ci

    gates = instrument_gates()
    print(
        f"memoryless whole: {gates['memoryless'].structure} "
        f"Φ={gates['memoryless'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_memoryless'] else 'FAIL'}"
    )
    print(
        f"sticky whole:     {gates['sticky'].structure} "
        f"Φ={gates['sticky'].max_phi:.6f}  "
        f"{'PASS' if gates['ctrl_sticky'] else 'FAIL'}"
    )
    if not gates["ok"]:
        raise SystemExit("instrument gates failed")

    committed = load_basin_committed()
    panel = build_panel(ci)
    missing = [name for name, _, _, _ in panel if name not in committed]
    if missing:
        raise SystemExit(f"committed basin CSV missing forms: {missing}")

    form_rows = []
    cycle_rows = []
    for name, builder, labels, group in panel:
        row, crows = evaluate_form(
            name, builder, labels, group, committed, with_grid=not ci
        )
        form_rows.append(row)
        cycle_rows.extend(crows)

    n_tri = sum(1 for r in form_rows if r["triadic"])
    n_dya = len(form_rows) - n_tri
    print(f"panel: n={len(form_rows)} triadic={n_tri} dyadic={n_dya}")
    if not ci and (len(form_rows) != 42 or n_tri != 17):
        raise SystemExit(
            f"frozen panel expected n=42 triadic=17, got n={len(form_rows)} triadic={n_tri}"
        )

    h5 = h5_ok(form_rows)
    h5_status = "SUPPORTED" if h5 else "REFUTED"
    print_h5(form_rows, h5_status)
    if not h5:
        for r in form_rows:
            if not (r["gap_match"] and r["basin_exact_match"] and r["closed_form_match"]):
                print(
                    f"  H5 FAIL {r['form']}: gap={r['gap_party']:.8f} "
                    f"csv={r['committed_gap']:.8f} "
                    f"exact={r['exact_basin_gap']:.8f} "
                    f"closed_err={r['closed_form_err']:.3e}"
                )
        summary = {
            "ci": int(ci),
            "n_forms": len(form_rows),
            "h5": h5_status,
            "h0": "NOT_TESTABLE",
            "h1": "NOT_TESTABLE",
            "h2": "NOT_TESTABLE",
            "h3": "NOT_TESTABLE",
            "verdict": "ORDERING_NOT_TESTABLE",
            "winner": "",
        }
        write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
        write_csv(os.path.join(RESULTS, "cycles.csv"), cycle_rows)
        write_csv(os.path.join(RESULTS, "summary.csv"), [summary])
        print("verdict: ORDERING_NOT_TESTABLE")
        raise SystemExit("H5 gate failed — aborting H0–H4")

    labels_h4 = (
        ("H4a (order_index absorbs):", "order_index"),
        ("H4b (order_excess absorbs):", "order_excess"),
        ("H4c (cofilip_sync absorbs):", "cofilip_sync"),
        ("H4d (phase_lag absorbs):", "phase_lag"),
        ("H4e (lag1_autocorr absorbs):", "lag1_autocorr"),
        ("H4f (hamming_party_rate absorbs):", "hamming_party_rate"),
        ("H4g (party_osc_frac absorbs):", "party_osc_frac"),
        ("H4h (mean_cycle_var absorbs):", "mean_cycle_var"),
        ("H4i (remainder_allstarts absorbs):", "remainder_allstarts"),
    )

    if ci:
        for label, _name in (
            ("H0 (AUC not a fluke):", None),
            ("H1 (phase remainder identity):", None),
            ("H2 (predicted gap tracks triadic):", None),
            ("H3 (residualizing on predicted gap):", None),
        ):
            status_line(label, "NOT_TESTABLE")
        for label, _name in labels_h4:
            status_line(label, "NOT_TESTABLE")
        print("verdict: ORDERING_INCONCLUSIVE")
        print("ranking winner: (none)")
        summary = {
            "ci": 1,
            "n_forms": len(form_rows),
            "n_triadic": n_tri,
            "n_dyadic": n_dya,
            "h5": h5_status,
            "h0": "NOT_TESTABLE",
            "h1": "NOT_TESTABLE",
            "h2": "NOT_TESTABLE",
            "h3": "NOT_TESTABLE",
            "verdict": "ORDERING_INCONCLUSIVE",
            "winner": "",
        }
        write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
        write_csv(os.path.join(RESULTS, "cycles.csv"), cycle_rows)
        write_csv(os.path.join(RESULTS, "summary.csv"), [summary])
        return

    gaps = [r["gap_party"] for r in form_rows]
    phis = [r["whole_phi"] for r in form_rows]
    triadic = [r["triadic"] for r in form_rows]
    preds = [r["pred_gap_cycle"] for r in form_rows]

    auc, auc_lo, auc_hi = bootstrap_auc_ci(gaps, triadic)
    _, auc_p = auc_permutation_p(gaps, triadic)
    h0 = (auc_lo > 0.5) and (auc_p < 0.05)
    h0_status = "SUPPORTED" if h0 else "REFUTED"
    status_line("H0 (AUC not a fluke):", h0_status)
    print(
        f"  AUC={auc:.4f}  bootstrap95=[{auc_lo:.4f}, {auc_hi:.4f}]  "
        f"perm_p={auc_p:.4f}"
    )
    pred_auc, pred_lo, pred_hi = bootstrap_auc_ci(preds, triadic)
    _, pred_p = auc_permutation_p(preds, triadic)
    print(
        f"  pred_AUC={pred_auc:.4f}  "
        f"pred_bootstrap95=[{pred_lo:.4f}, {pred_hi:.4f}]  "
        f"pred_perm_p={pred_p:.4f}"
    )

    slopes = [r["t_scale_slope"] for r in form_rows]
    mean_slope = sum(slopes) / float(len(slopes))
    # Omit forms whose mean gap·T is 0 (hypotheses.md). A positive-mean
    # form with CV exactly 0 stays in the average.
    cvs = []
    for r in form_rows:
        vals = [r[f"gap_T{T}"] * T for T in T_GRID]
        mean_v = sum(vals) / float(len(vals))
        if mean_v > 0:
            var_v = sum((v - mean_v) ** 2 for v in vals) / float(len(vals))
            cvs.append(math.sqrt(var_v) / mean_v)
    if cvs:
        mean_cv = sum(cvs) / float(len(cvs))
        cv_ok = mean_cv <= CV_MAX
    else:
        mean_cv = 0.0
        cv_ok = True
    slope_ok = SLOPE_LO <= mean_slope <= SLOPE_HI
    abs_diffs = [abs(p - g) for p, g in zip(preds, gaps)]
    max_abs = max(abs_diffs)
    mean_abs = sum(abs_diffs) / float(len(abs_diffs))
    match_abs_ok = max_abs <= MATCH_ABS
    if _var(preds) < VAR_EPS and _var(gaps) < VAR_EPS:
        rho_match = float("nan")
        match_rho_ok = match_abs_ok
    else:
        rho_match, _rho_match_p = spearman_rho(preds, gaps)
        match_rho_ok = (not math.isnan(rho_match)) and rho_match >= MATCH_RHO
    h1 = slope_ok and cv_ok and match_abs_ok and match_rho_ok
    h1_status = "SUPPORTED" if h1 else "REFUTED"
    status_line("H1 (phase remainder identity):", h1_status)
    print(
        f"  mean_loglog_slope={mean_slope:.4f}  "
        f"mean_gapT_cv={mean_cv:.4f}  "
        f"max|pred-gap|={_fmt(max_abs, '.3e')}  "
        f"mean|pred-gap|={_fmt(mean_abs, '.3e')}  "
        f"spearman_pred_gap={_fmt(rho_match)}"
    )

    auc_gap = rank_auc(gaps, triadic)
    auc_pred = rank_auc(preds, triadic)
    rho_gap, rho_gap_p = spearman_rho(gaps, phis)
    rho_pred, rho_pred_p = spearman_rho(preds, phis)
    auc_close = (not math.isnan(auc_gap)) and (not math.isnan(auc_pred)) and (
        abs(auc_pred - auc_gap) <= AUC_TOL
    )
    rho_close = (
        (not math.isnan(rho_gap))
        and (not math.isnan(rho_pred))
        and abs(rho_pred - rho_gap) <= RHO_TOL
    )
    same_sign = (
        (not math.isnan(rho_gap))
        and (not math.isnan(rho_pred))
        and (
            (rho_pred * rho_gap > 0)
            or (abs(rho_pred) < SIGN_EPS and abs(rho_gap) < SIGN_EPS)
        )
    )
    h2 = auc_close and rho_close and same_sign
    h2_status = "SUPPORTED" if h2 else "REFUTED"
    status_line("H2 (predicted gap tracks triadic):", h2_status)
    print(
        f"  AUC_gap={auc_gap:.4f}  AUC_pred={auc_pred:.4f}  "
        f"ΔAUC={auc_pred - auc_gap:.4f}  "
        f"ρ_gap={_fmt(rho_gap)}  ρ_pred={_fmt(rho_pred)}  "
        f"ρ_gap_p={rho_gap_p:.4f}  ρ_pred_p={rho_pred_p:.4f}"
    )

    covariate_order = (
        ("pred_gap_cycle", True),
        ("order_index", False),
        ("order_excess", False),
        ("cofilip_sync", False),
        ("phase_lag", False),
        ("lag1_autocorr", False),
        ("hamming_party_rate", False),
        ("party_osc_frac", False),
        ("mean_cycle_var", False),
        ("remainder_allstarts", True),
    )
    meds = {}
    for name, allow_id in covariate_order:
        meds[name] = absorption(
            gaps,
            triadic,
            phis,
            [r[name] for r in form_rows],
            allow_identity=allow_id,
        )

    h3 = meds["pred_gap_cycle"]["passes"]
    h3_status = "SUPPORTED" if h3 else "REFUTED"
    print_absorption("H3 (residualizing on predicted gap):", meds["pred_gap_cycle"])

    h4_status = {}
    for label, name in labels_h4:
        h4_status[name] = "SUPPORTED" if meds[name]["passes"] else "REFUTED"
        print_absorption(label, meds[name])

    mech_rows = []
    for name, _allow in covariate_order:
        med = meds[name]
        role = (
            "pure_order"
            if name in PURE_ORDER
            else "amplitude"
            if name in AMPLITUDE
            else "remainder"
        )
        mech_rows.append(
            {
                "covariate": name,
                "role": role,
                "passes": med["passes"],
                "exclude": med["exclude"],
                "identity": med["identity"],
                "beta_uni": med["beta_uni"],
                "p_uni": med["p_uni"],
                "beta_partial": med["beta_partial"],
                "p_partial": med["p_partial"],
                "beta_ratio": med["beta_ratio"],
                "rho_uni": med["rho_uni"],
                "rho_uni_p": med["rho_uni_p"],
                "rho_partial": med["rho_partial"],
                "rho_partial_p": med["rho_partial_p"],
                "pearson_gap": med["pearson_gap"],
                "mae_gap": med["mae_gap"],
                "spearman_drop": med["spearman_drop"],
            }
        )

    # Descriptive census of attractor periods. At T=64 the residual
    # window r = T mod p is what makes order_index / order_excess
    # identically zero when r ∈ {0, 1, p-1}. Not a hypothesis.
    period_counts = {}
    seen_cycles = set()
    for crow in cycle_rows:
        key = (crow["form"], crow["cycle_index"])
        if key in seen_cycles:
            continue
        seen_cycles.add(key)
        period = int(crow["period"])
        period_counts[period] = period_counts.get(period, 0) + 1
    period_bits = " ".join(
        f"p{p}={period_counts[p]}" for p in sorted(period_counts)
    )
    window_bits = " ".join(
        f"p{p}:r={HORIZON_PRIMARY % p}" for p in sorted(period_counts)
    )
    print(f"periods: {period_bits}")
    print(f"windows_T64: {window_bits}")
    nz_by_period = {}
    n_nz = 0
    for crow in cycle_rows:
        if abs(float(crow["pred_abs_remainder"])) <= 1e-12:
            continue
        n_nz += 1
        period = int(crow["period"])
        nz_by_period[period] = nz_by_period.get(period, 0) + 1
    nz_bits = " ".join(f"p{p}={nz_by_period[p]}" for p in sorted(nz_by_period))
    print(f"nonzero_bit_remainders={n_nz}/{len(cycle_rows)} {nz_bits}")

    winner = ranking_winner(mech_rows)
    verdict = verdict_word(h0, h1, h3, winner)
    print(f"verdict: {verdict}")
    print(f"ranking winner: {winner if winner else '(none)'}")
    low = descriptive_lowest(mech_rows)
    if low is not None:
        print(
            f"descriptive lowest β_ratio: {low['covariate']} "
            f"({_fmt(low['beta_ratio'])})"
        )

    summary = {
        "ci": 0,
        "n_forms": len(form_rows),
        "n_triadic": n_tri,
        "n_dyadic": n_dya,
        "h0": h0_status,
        "h1": h1_status,
        "h2": h2_status,
        "h3": h3_status,
        "h4a": h4_status["order_index"],
        "h4b": h4_status["order_excess"],
        "h4c": h4_status["cofilip_sync"],
        "h4d": h4_status["phase_lag"],
        "h4e": h4_status["lag1_autocorr"],
        "h4f": h4_status["hamming_party_rate"],
        "h4g": h4_status["party_osc_frac"],
        "h4h": h4_status["mean_cycle_var"],
        "h4i": h4_status["remainder_allstarts"],
        "h5": h5_status,
        "verdict": verdict,
        "winner": winner,
        "auc": auc,
        "auc_ci_lo": auc_lo,
        "auc_ci_hi": auc_hi,
        "auc_perm_p": auc_p,
        "pred_auc": pred_auc,
        "pred_auc_ci_lo": pred_lo,
        "pred_auc_ci_hi": pred_hi,
        "pred_auc_perm_p": pred_p,
        "mean_t_slope": mean_slope,
        "mean_gapT_cv": mean_cv,
        "max_abs_pred_gap": max_abs,
        "mean_abs_pred_gap": mean_abs,
        "spearman_pred_gap": rho_match,
        "auc_gap": auc_gap,
        "auc_pred": auc_pred,
        "rho_gap": rho_gap,
        "rho_gap_p": rho_gap_p,
        "rho_pred": rho_pred,
        "rho_pred_p": rho_pred_p,
        "beta_gap_uni": meds["pred_gap_cycle"]["beta_uni"],
        "beta_gap_uni_p": meds["pred_gap_cycle"]["p_uni"],
    }
    write_csv(os.path.join(RESULTS, "forms.csv"), form_rows)
    write_csv(os.path.join(RESULTS, "cycles.csv"), cycle_rows)
    write_csv(os.path.join(RESULTS, "summary.csv"), [summary])
    write_csv(os.path.join(RESULTS, "mechanisms.csv"), mech_rows)


if __name__ == "__main__":
    main()
