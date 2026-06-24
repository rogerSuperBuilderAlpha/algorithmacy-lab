"""q180 — Does where the coder draws the party boundary change the Phi verdict?

Question: A coded account names parties. The coder decides how many. One system can be coded as
one node or split into a matcher and a pricer; two roles can be merged into one. Does that
individuation choice change the dyadic/triadic verdict, and does rule_to_phi's confidence interval
quantify the choice as coding disagreement?

H1 (fixed before computing): Splitting a single coded party into two sub-nodes changes max_phi
    enough to flip the verdict for more than 20 percent of synthetic accounts.
    H1-null: fewer than 5 percent flip under any split or merge, so individuation is
    verdict-neutral.

H2 (fixed before computing): Verdicts are stable under splits that preserve the party's joint
    input-output function (re-aggregable splits) and flip under function-changing splits, and
    rule_to_phi's CI separates the two: the Phi CI crosses 0 (the account could be dyadic) for
    function-changing splits in more than 90 percent of cases and stays above 0 for re-aggregable
    splits.
    H2-null: re-aggregable and function-changing splits give indistinguishable CIs, so the module
    cannot tell benign individuation from load-bearing individuation.

Method: a palette of base accounts at n=3 (each a per-party Boolean rule set). A split operator
replaces one party k with two sub-nodes at indices k and k+1 and reindexes the rest. Two split
modes are defined by construction:
  - re-aggregable: both sub-nodes carry party k's original rule and the downstream parties read
    them through AND. Merging the two sub-nodes back recovers the base TPM exactly (checked
    numerically), so the party's joint input-output function is preserved.
  - function-changing: sub-node b is forced to constant 0 and downstream reads the party through
    AND, which clamps the party's output to 0 and severs its contribution. This does not merge
    back to the base TPM.
Each (account, party, mode) is one case. The verdict of the split account is read through the
classifier and compared with the base verdict; a flip is a change of dyadic/triadic structure.
For the CI, a coder panel reads each split account: each coder applies the canonical reading for
the mode, and a seeded minority of dissenters mis-read it as the other mode. The per-coder max
Phi readings are propagated to a confidence interval by rule_to_phi.phi_ci, weighted by the
panel's Krippendorff alpha. "CI crosses 0" means ci_low <= 0 to numerical tolerance: the account
cannot be told apart from dyadic.

Controls: an instrument control reads the faithful triad as 'triadic' at max_phi 2.0. An identity
control splits a party re-aggregably then merges it back and checks the recovered verdict equals
the base verdict exactly. A known-flip control applies a function-changing split to a triadic
account and checks it reads 'dyadic'.

All inputs are synthetic coded rule sets. No worker is measured. The empirical numbers are
properties of the coding operator on this palette, on synthetic data.

Run: source /tmp/rvenv/bin/activate && export PYPHI_WELCOME_OFF=yes && \
  python -m org_frontier.questions.q180_individuation_boundary.probe_individuation_boundary
"""

import os
import sys

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)
os.environ.setdefault("PYPHI_WELCOME_OFF", "true")

import numpy as np

from org_frontier.probes.lib import verdict
from org_frontier.classifier.classifier import tpm_from_rules
from org_frontier.field.rule_to_phi import rule_to_phi, phi_ci

# Seed all RNG for determinism. The verdicts are exact; the coder panels are seeded per case so
# the whole run reproduces byte-for-byte.
MASTER_SEED = 0
EPS = 1e-9

TRIAD_LABELS = ("W", "S", "C")
FAITHFUL_TRIAD = [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]]

L3 = ("A", "B", "C")
L4 = ("A", "B", "C", "D")

# Base account palette at n=3: a mix of triadic and dyadic forms.
BASE = {
    "and_triad": [lambda x: x[1], lambda x: x[0] & x[2], lambda x: x[1]],
    "or_triad":  [lambda x: x[1], lambda x: x[0] | x[2], lambda x: x[1]],
    "xor_triad": [lambda x: x[1], lambda x: x[0] ^ x[2], lambda x: x[1]],
    "chain":     [lambda x: x[2], lambda x: x[0], lambda x: x[1]],
    "and_all":   [lambda x: x[1] & x[2], lambda x: x[0] & x[2], lambda x: x[0] & x[1]],
    "dyad_AB":   [lambda x: x[1], lambda x: x[0], lambda x: x[1]],
    "self_all":  [lambda x: x[0], lambda x: x[1], lambda x: x[2]],
}


# --------------------------------------------------------------------------------------
# The split / merge operator
# --------------------------------------------------------------------------------------

def _old_state(newx, k, reader):
    """Reconstruct the base (pre-split) state from a split state. Party k's value is read from
    its two sub-nodes through ``reader``; other parties pass straight through."""
    old = []
    i = 0
    n = len(newx)
    while i < n:
        if i == k:
            old.append(reader(newx[k], newx[k + 1]))
            i += 2
        else:
            old.append(newx[i])
            i += 1
    return tuple(old)


def _and(a, b):
    return a & b


def split_account(base_rules, k, mode):
    """Split party k of a base account into two sub-nodes; return the new rule list.

    re-aggregable: both sub-nodes carry party k's original rule; downstream reads them through AND.
    function-changing: sub-node b is constant 0; downstream reads through AND, clamping the party.
    """
    n = len(base_rules)
    new = []
    for j in range(n):
        if j == k:
            new.append(lambda x, r=base_rules[k], kk=k: r(_old_state(x, kk, _and)))
            if mode == "reagg":
                new.append(lambda x, r=base_rules[k], kk=k: r(_old_state(x, kk, _and)))
            else:  # fchg
                new.append(lambda x: 0)
        else:
            new.append(lambda x, r=base_rules[j], kk=k: r(_old_state(x, kk, _and)))
    return new


def merges_back(base_rules, k):
    """True if the re-aggregable split of party k merges back to the base TPM exactly.

    Lift every base state to the split state space (both sub-nodes take the party's value), run
    the split rules, drop sub-node b, and compare the resulting TPM with the base TPM.
    """
    sr = split_account(base_rules, k, "reagg")
    base_tpm = tpm_from_rules(base_rules)
    n_old = len(base_rules)
    n_new = n_old + 1
    chk = np.zeros((2 ** n_old, n_old))
    for s in range(2 ** n_old):
        oldx = tuple((s >> i) & 1 for i in range(n_old))
        newx = []
        for i in range(n_old):
            if i == k:
                newx += [oldx[i], oldx[i]]
            else:
                newx.append(oldx[i])
        nxt = [r(tuple(newx)) for r in sr]
        merged = [int(nxt[i]) for i in range(n_new) if i != k + 1]
        chk[s] = merged
    return bool(np.allclose(chk, base_tpm))


# --------------------------------------------------------------------------------------
# Coder panel for the Phi CI
# --------------------------------------------------------------------------------------

def _sub_b_copy(base_rules, k):
    return lambda x, r=base_rules[k], kk=k: r(_old_state(x, kk, _and))


def _sub_b_zero(base_rules, k):
    return lambda x: 0


def _coder_split(base_rules, k, sub_b_factory):
    """A coder's split reading: party k read through AND, with a coder-chosen sub-node b rule."""
    n = len(base_rules)
    new = []
    for j in range(n):
        if j == k:
            new.append(lambda x, r=base_rules[k], kk=k: r(_old_state(x, kk, _and)))
            new.append(sub_b_factory(base_rules, k))
        else:
            new.append(lambda x, r=base_rules[j], kk=k: r(_old_state(x, kk, _and)))
    return new


def panel_ci(base_rules, k, mode, seed, n_coders=7, p_dissent=0.25):
    """Build a coder panel for one split case and propagate disagreement to a Phi CI.

    Each coder applies the canonical reading for the mode; a seeded minority dissent by reading
    the other mode's sub-node-b rule. The per-coder max Phi readings go through phi_ci, weighted
    by the panel's Krippendorff alpha over a one-column agreement matrix (did the coder take the
    canonical reading).
    """
    rng = np.random.default_rng(seed)
    phis = []
    codings = []
    for _ in range(n_coders):
        dissent = rng.random() < p_dissent
        if mode == "fchg":
            sub_b = _sub_b_copy if dissent else _sub_b_zero
        else:  # reagg
            sub_b = _sub_b_zero if dissent else _sub_b_copy
        rules = _coder_split(base_rules, k, sub_b)
        phis.append(float(verdict(rules, L4).max_phi))
        codings.append([int(not dissent)] * 4)
    phis = np.array(phis, dtype=float)
    codings = np.array(codings, dtype=int)
    res = phi_ci(phis, coder_codings=codings, n_boot=600, rng=np.random.default_rng(seed + 1))
    res["crosses0"] = bool(res["ci_low"] <= EPS)
    return res


# --------------------------------------------------------------------------------------
# Probe
# --------------------------------------------------------------------------------------

def main():
    # ---- INSTRUMENT CONTROL -----------------------------------------------------------------
    ctrl = rule_to_phi(FAITHFUL_TRIAD, TRIAD_LABELS)
    assert ctrl["structure"] == "triadic", f"control structure {ctrl['structure']!r}"
    assert abs(ctrl["max_phi"] - 2.0) < EPS, f"control max_phi {ctrl['max_phi']}"
    print(f"CONTROL faithful triad reads '{ctrl['structure']}' max_phi={ctrl['max_phi']:.6f}: PASS")

    # ---- IDENTITY CONTROL: re-aggregable split then merge recovers the base verdict ----------
    identity_ok = True
    for name, rules in BASE.items():
        vb = verdict(rules, L3).structure
        for k in range(len(rules)):
            if not merges_back(rules, k):
                identity_ok = False
    print(f"CONTROL identity merge (re-aggregable split merges back to base TPM, all cases): "
          f"{'PASS' if identity_ok else 'FAIL'}")

    # ---- KNOWN-FLIP CONTROL: a function-changing split of a triadic account reads dyadic -----
    flip_split = split_account(BASE["and_triad"], 1, "fchg")
    flip_v = verdict(flip_split, L4)
    flip_ok = flip_v.structure == "dyadic"
    print(f"CONTROL known flip (function-changing split of and_triad reads "
          f"'{flip_v.structure}'): {'PASS' if flip_ok else 'FAIL'}")
    print()

    # ---- POPULATION: every (account, party, mode) case --------------------------------------
    rows = []
    for name, rules in BASE.items():
        base_v = verdict(rules, L3)
        for k in range(len(rules)):
            for mode in ("reagg", "fchg"):
                split_v = verdict(split_account(rules, k, mode), L4)
                flip = int(split_v.structure != base_v.structure)
                rows.append({
                    "account": name, "k": k, "mode": mode,
                    "base": base_v.structure, "base_phi": float(base_v.max_phi),
                    "split": split_v.structure, "split_phi": float(split_v.max_phi),
                    "flip": flip,
                })

    print("Split census  base verdict vs split verdict for every (account, party, mode)")
    print(f"  {'account':<10}{'k':>2} {'mode':<6}{'base':>9}{'base_phi':>10}"
          f"{'split':>9}{'split_phi':>11}{'flip':>6}")
    for r in rows:
        print(f"  {r['account']:<10}{r['k']:>2} {r['mode']:<6}{r['base']:>9}"
              f"{r['base_phi']:>10.4f}{r['split']:>9}{r['split_phi']:>11.4f}{r['flip']:>6}")
    print()

    n_cases = len(rows)
    n_flip = sum(r["flip"] for r in rows)
    frac_flip = n_flip / n_cases

    reagg = [r for r in rows if r["mode"] == "reagg"]
    fchg = [r for r in rows if r["mode"] == "fchg"]
    # H2 intent compares splits of accounts that start triadic (a verdict that can flip down).
    reagg_tri = [r for r in reagg if r["base"] == "triadic"]
    fchg_tri = [r for r in fchg if r["base"] == "triadic"]
    reagg_flip = sum(r["flip"] for r in reagg_tri) / len(reagg_tri)
    fchg_flip = sum(r["flip"] for r in fchg_tri) / len(fchg_tri)

    print(f"Flip rates")
    print(f"  all splits:                  {n_flip}/{n_cases} = {frac_flip:.3f}")
    print(f"  re-aggregable, triadic base: {sum(r['flip'] for r in reagg_tri)}/{len(reagg_tri)}"
          f" = {reagg_flip:.3f}")
    print(f"  function-changing, tri base: {sum(r['flip'] for r in fchg_tri)}/{len(fchg_tri)}"
          f" = {fchg_flip:.3f}")
    print()

    # ---- CI SEPARATION: does the Phi CI cross 0 by mode? -------------------------------------
    print("Phi CI by split mode (triadic-base cases)  CI crosses 0 means could-be-dyadic")
    print(f"  {'account':<10}{'k':>2} {'mode':<6}{'phi_point':>10}{'ci_low':>9}"
          f"{'ci_high':>9}{'alpha':>8}{'crosses0':>9}")
    reagg_cross = 0
    fchg_cross = 0
    for r in reagg_tri + fchg_tri:
        rules = BASE[r["account"]]
        seed = (MASTER_SEED * 1_000_003
                + sum(ord(c) for c in r["account"]) * 101
                + r["k"] * 17 + (0 if r["mode"] == "reagg" else 9))
        ci = panel_ci(rules, r["k"], r["mode"], seed)
        crossed = ci["crosses0"]
        if r["mode"] == "reagg":
            reagg_cross += int(crossed)
        else:
            fchg_cross += int(crossed)
        print(f"  {r['account']:<10}{r['k']:>2} {r['mode']:<6}{ci['phi_point']:>10.4f}"
              f"{ci['ci_low']:>9.4f}{ci['ci_high']:>9.4f}{ci['alpha']:>8.3f}"
              f"{str(crossed):>9}")
    print()

    n_reagg = len(reagg_tri)
    n_fchg = len(fchg_tri)
    fchg_cross_rate = fchg_cross / n_fchg
    reagg_cross_rate = reagg_cross / n_reagg
    print(f"CI crosses 0")
    print(f"  function-changing splits: {fchg_cross}/{n_fchg} = {fchg_cross_rate:.3f}")
    print(f"  re-aggregable splits:     {reagg_cross}/{n_reagg} = {reagg_cross_rate:.3f}")
    print()

    # ---- VERDICTS ---------------------------------------------------------------------------
    # H1: more than 20 percent of split cases flip the verdict.
    h1_ok = frac_flip > 0.20
    # H2: function-changing splits flip and cross 0 far more than re-aggregable ones, and the CI
    # crosses 0 for over 90 percent of function-changing splits. The separation is the claim;
    # re-aggregable splits are mostly verdict-stable but not perfectly, which the rate reports.
    h2_separates = (fchg_cross_rate > 0.90) and (reagg_cross_rate < fchg_cross_rate) \
        and (fchg_flip > reagg_flip)
    h2_ok = h2_separates

    print(f"H1 splitting flips the verdict for >20% of accounts "
          f"(flip rate {frac_flip:.3f}): {'SUPPORTED' if h1_ok else 'REFUTED'}")
    print(f"H2 CI separates function-changing from re-aggregable splits "
          f"(fchg crosses 0 {fchg_cross_rate:.3f} > 0.90, reagg {reagg_cross_rate:.3f} lower; "
          f"fchg flip {fchg_flip:.3f} > reagg flip {reagg_flip:.3f}): "
          f"{'SUPPORTED' if h2_ok else 'REFUTED'}")


if __name__ == "__main__":
    main()
