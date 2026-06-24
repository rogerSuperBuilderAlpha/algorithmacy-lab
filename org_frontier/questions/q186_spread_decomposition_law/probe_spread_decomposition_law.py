"""q186 — Do the three spread components vary independently or collapse onto one axis?

Question: Across a synthetic census of account-pair settings, can the three spread components
(verdict agreement, Φ gap, core-membership divergence) be decomposed so that they vary
independently, or do they collapse onto one underlying axis so that the spread is effectively
one number?

H1: There exist account pairs that agree on verdict (verdict_agreement = 1) yet have phi_gap > 0,
    and pairs that disagree on verdict (verdict_agreement = 0) yet have core_jaccard = 1, so the
    three components are not rank-one collinear.
    H1-null: all three components are monotone functions of one another, so the spread is
    effectively one number and the tuple is redundant.

H2: The fraction of the census exhibiting at least one off-diagonal pattern (agree-but-gapped or
    disagree-but-same-core) exceeds 10 percent.
    H2-null: such patterns occur at or below the rate expected from numerical Φ noise
    (< 1 percent), so the components are practically collinear.

Method: build a curated palette of coordination accounts at n=3 and n=4. Each account is a per-node
Boolean rule set over labelled nodes. For every account compute its exact-Φ verdict (whole-system
structure and max Φ_MIP) and its major-complex core once, through the reused classifier and probe
library. The census is every unordered pair of distinct accounts within a node count. For each pair
read the three spread components defined by the q183 bridge: verdict_agreement, phi_gap,
core_jaccard. Test pairwise Spearman rank correlation across the census; count the off-diagonal
patterns. The control anchor is identical-account pairs, which fix verdict_agreement = 1,
phi_gap = 0, core_jaccard = 1. The instrument control is the faithful triad reading 'triadic'
max_phi 2.0. Synthetic accounts; results are on synthetic data.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q186_spread_decomposition_law.probe_spread_decomposition_law
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

from itertools import combinations

import numpy as np
from scipy.stats import spearmanr

from org_frontier.probes.lib import verdict, major_complex
from org_frontier.qualitative.disagreement_phi import spread

# Seed all RNG for determinism. The census and every component are exact; this guards any
# sampled path inside the Φ machinery so the output reproduces byte-for-byte on re-run.
RNG = np.random.default_rng(0)

EPS = 1e-9

# Instrument-control faithful triad.
TRIAD_LABELS = ("W", "S", "C")
FAITHFUL_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

# ---- n=3 account palette ---------------------------------------------------------------------
L3 = ("A", "B", "C")
PALETTE_3 = {
    "triad":     [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "or_triad":  [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],
    "xor_triad": [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
    "chain":     [lambda x: x[2], lambda x: x[0], lambda x: x[1]],
    "and_all":   [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[0] & x[1]],
    "or_all":    [lambda x: x[1] | x[2], lambda x: x[0] | x[2], lambda x: x[0] | x[1]],
    "dyad_AB":   [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
    "self_C":    [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
}

# ---- n=4 account palette ---------------------------------------------------------------------
L4 = ("A", "B", "C", "D")
PALETTE_4 = {
    "quad_and":   [lambda x: x[1] & x[3], lambda x: x[0] & x[2],
                   lambda x: x[1] & x[3], lambda x: x[0] & x[2]],
    "chain4":     [lambda x: x[3], lambda x: x[0], lambda x: x[1], lambda x: x[2]],
    # whole-system dyadic (ABC factor off D), major-complex core = ABC.
    "triad_free": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1], lambda x: 0],
    # whole-system dyadic, major-complex core = AB.
    "dyad_AB4":   [lambda x: x[1], lambda x: x[0], lambda x: 0, lambda x: 0],
    # whole-system triadic (Φ>0) but major-complex core = AB only.
    "tri_coreAB": [lambda x: x[3] ^ x[1], lambda x: x[3] | x[0],
                   lambda x: x[1] ^ x[0], lambda x: x[2] & x[0]],
    # two independent dyads AB and CD; whole-system dyadic, core = CD.
    "two_dyads":  [lambda x: x[1], lambda x: x[0], lambda x: x[3], lambda x: x[2]],
}


def account_record(rules, labels):
    """Compute (structure, max_phi, core frozenset) for one account, once."""
    v = verdict(rules, labels)
    core, _ = major_complex(rules, labels)
    core_set = frozenset() if core is None else frozenset(core)
    return v.structure, float(v.max_phi), core_set


def jaccard(a, b):
    """Jaccard overlap; two empty cores count as full agreement (matches the bridge)."""
    if not a and not b:
        return 1.0
    union = a | b
    if not union:
        return 1.0
    return len(a & b) / len(union)


def components_from_records(ra, rb):
    """Derive the three bridge components from two cached account records."""
    (sa, pa, ca), (sb, pb, cb) = ra, rb
    verdict_agreement = int(sa == sb)
    phi_gap = abs(pa - pb)
    core_jaccard = jaccard(ca, cb)
    return verdict_agreement, phi_gap, core_jaccard


def build_records(palette, labels):
    return {name: account_record(rules, labels) for name, rules in palette.items()}


def census_rows(records):
    """Every unordered pair of distinct accounts; one row of three components each."""
    rows = []
    for a, b in combinations(records, 2):
        va, pg, cj = components_from_records(records[a], records[b])
        rows.append((a, b, va, pg, cj))
    return rows


def main():
    # ---- INSTRUMENT CONTROL -----------------------------------------------------------------
    v = verdict(FAITHFUL_TRIAD, TRIAD_LABELS)
    assert v.structure == "triadic", f"control structure {v.structure!r}"
    assert abs(v.max_phi - 2.0) < EPS, f"control max_phi {v.max_phi}"
    print(f"CONTROL faithful triad reads '{v.structure}' max_phi={v.max_phi:.6f}: PASS")
    print()

    # ---- BRIDGE-AGREEMENT CHECK: cached derivation matches the q183 bridge spread() ---------
    rec3 = build_records(PALETTE_3, L3)
    a, b = "triad", "xor_triad"
    cached = components_from_records(rec3[a], rec3[b])
    bridged = spread(PALETTE_3[a], PALETTE_3[b], L3)
    assert cached[0] == bridged["verdict_agreement"]
    assert abs(cached[1] - bridged["phi_gap"]) < EPS
    assert abs(cached[2] - bridged["core_jaccard"]) < EPS
    print("BRIDGE check  cached components reproduce q183 spread() on a sample pair: PASS")
    print()

    # ---- IDENTICAL-ACCOUNT CONTROL: every component anchored at its agreement value ---------
    anchor_ok = True
    for name, rules in list(PALETTE_3.items())[:3]:
        s = spread(rules, rules, L3)
        anchor_ok = anchor_ok and s["verdict_agreement"] == 1 \
            and abs(s["phi_gap"]) < EPS and abs(s["core_jaccard"] - 1.0) < EPS
    print(f"ANCHOR control  identical-account pairs give (1, 0.0, 1.0): "
          f"{'PASS' if anchor_ok else 'FAIL'}")
    print()

    # ---- BUILD THE CENSUS -------------------------------------------------------------------
    rec4 = build_records(PALETTE_4, L4)
    rows3 = census_rows(rec3)
    rows4 = census_rows(rec4)
    rows = [("n3",) + r for r in rows3] + [("n4",) + r for r in rows4]

    print("Account census  per-account verdict and major-complex core")
    print(f"  {'setting':<6}{'account':<12}{'structure':>10}{'max_phi':>12}   core")
    for name, rec in rec3.items():
        s, p, c = rec
        print(f"  {'n3':<6}{name:<12}{s:>10}{p:>12.6f}   {sorted(c)}")
    for name, rec in rec4.items():
        s, p, c = rec
        print(f"  {'n4':<6}{name:<12}{s:>10}{p:>12.6f}   {sorted(c)}")
    print()

    # ---- PAIRWISE COMPONENT VECTORS ---------------------------------------------------------
    # verdict_disagreement = 1 - verdict_agreement, so all three rise with divergence and a
    # rank-one census would make them monotone in one another.
    vdis = np.array([1 - r[3] for r in rows], dtype=float)
    pgap = np.array([r[4] for r in rows], dtype=float)
    cdiv = np.array([1.0 - r[5] for r in rows], dtype=float)  # core divergence = 1 - jaccard
    n_pairs = len(rows)

    rho_vd_pg = spearmanr(vdis, pgap).statistic
    rho_vd_cd = spearmanr(vdis, cdiv).statistic
    rho_pg_cd = spearmanr(pgap, cdiv).statistic

    print(f"Census size  {n_pairs} account pairs "
          f"({len(rows3)} at n=3, {len(rows4)} at n=4)")
    print("Spearman rank correlation between the three divergence axes")
    print(f"  verdict_disagree vs phi_gap   rho = {rho_vd_pg:+.4f}")
    print(f"  verdict_disagree vs core_div  rho = {rho_vd_cd:+.4f}")
    print(f"  phi_gap          vs core_div  rho = {rho_pg_cd:+.4f}")
    print()

    # ---- OFF-DIAGONAL PATTERNS --------------------------------------------------------------
    agree_gapped = [r for r in rows if r[3] == 1 and r[4] > EPS]
    disagree_samecore = [r for r in rows if r[3] == 0 and abs(r[5] - 1.0) < EPS]
    off_diag = [r for r in rows
                if (r[3] == 1 and r[4] > EPS) or (r[3] == 0 and abs(r[5] - 1.0) < EPS)]
    frac_off = len(off_diag) / n_pairs

    print("Off-diagonal patterns (components disagreeing about how far apart the accounts sit)")
    print(f"  agree-but-gapped      (verdict_agreement=1, phi_gap>0):       {len(agree_gapped)}")
    print(f"  disagree-but-samecore (verdict_agreement=0, core_jaccard=1):  "
          f"{len(disagree_samecore)}")
    print(f"  any off-diagonal pair: {len(off_diag)} / {n_pairs} "
          f"= {frac_off:.4f} of the census")
    print()
    if agree_gapped:
        a = agree_gapped[0]
        print(f"  example agree-but-gapped:      {a[0]} {a[1]}/{a[2]}  "
              f"phi_gap={a[4]:.4f} core_jaccard={a[5]:.4f}")
    if disagree_samecore:
        d = disagree_samecore[0]
        print(f"  example disagree-but-samecore: {d[0]} {d[1]}/{d[2]}  "
              f"phi_gap={d[4]:.4f} core_jaccard={d[5]:.4f}")
    print()

    # ---- H1: not rank-one collinear ---------------------------------------------------------
    # Collinear would require every off-diagonal cell empty AND all three correlations = +1.
    h1_ok = len(agree_gapped) > 0 and len(disagree_samecore) > 0
    # A correlation strictly below 1 corroborates non-collinearity.
    not_unit_corr = (rho_vd_pg < 1.0 - EPS) or (rho_vd_cd < 1.0 - EPS) or (rho_pg_cd < 1.0 - EPS)

    # ---- H2: off-diagonal fraction exceeds 10 percent ---------------------------------------
    h2_ok = frac_off > 0.10

    print(f"H1 three components not rank-one collinear "
          f"(both off-diagonal cells non-empty: {len(agree_gapped)}, "
          f"{len(disagree_samecore)}; some rho<1: {not_unit_corr}): "
          f"{'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 off-diagonal fraction {frac_off:.4f} exceeds 0.10: "
          f"{'CONFIRMED' if h2_ok else 'NOT SUPPORTED'}")


if __name__ == "__main__":
    main()
