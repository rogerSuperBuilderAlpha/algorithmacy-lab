"""Analysis for the gig_work_motivation review: reliability + the three hypothesis tests.

    python3 -m org_frontier.reviews.gig_work_motivation.run

Reads coding/ (independent coder JSONL) and literature/corpus.jsonl, writes results/frozen.json and
results/summary.json, and prints the per-hypothesis verdicts. Standard library only; uses the arm's
reusable reliability tooling.

H1 - motivation_mode distribution (does gap_spotting dominate?)
H2 - motivation_mode / assumption_targeted split by an early vs. late year cut (does problematization rise?)
H3 - citations-per-year by mode, compared with Mann-Whitney U plus means/medians
"""

import json
import os
from collections import Counter

from org_frontier.reviews.lib import reliability

HERE = os.path.dirname(__file__)
CATEGORICAL = ["motivation_mode", "assumption_targeted"]
NOW = 2026.5          # citation snapshot: mid-2026
YEAR_CUT = 2024       # early = year < 2024, late = year >= 2024


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def _mannwhitney_u(a, b):
    """Two-sided Mann-Whitney U with a normal approximation (ties corrected). Returns (U, p, z)."""
    import math
    na, nb = len(a), len(b)
    if na == 0 or nb == 0:
        return None, None, None
    combined = sorted([(v, 0) for v in a] + [(v, 1) for v in b], key=lambda x: x[0])
    # rank with ties -> average ranks
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg = (i + 1 + j + 1) / 2.0
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    r_a = sum(ranks[k] for k in range(len(combined)) if combined[k][1] == 0)
    u_a = r_a - na * (na + 1) / 2.0
    u_b = na * nb - u_a
    u = min(u_a, u_b)
    mu = na * nb / 2.0
    # tie-corrected variance
    tie_term = 0.0
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        t = j - i + 1
        tie_term += t ** 3 - t
        i = j + 1
    n = na + nb
    var = (na * nb / 12.0) * ((n + 1) - tie_term / (n * (n - 1)))
    if var <= 0:
        return u, 1.0, 0.0
    z = (u - mu) / math.sqrt(var)
    p = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return u, p, z


def _median(xs):
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return None
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2.0


def main():
    corpus = _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))
    by_slug = {r["slug"]: r for r in corpus}

    # --- reliability + adjudicated dataset ---
    reliability.run(os.path.join(HERE, "coding"), "slug", CATEGORICAL, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))
    n = len(frozen)

    print("\n" + "=" * 70)

    # --- H1: motivation_mode distribution ---
    mode = Counter(r["motivation_mode"] for r in frozen)
    gap = mode.get("gap_spotting", 0)
    prob = mode.get("problematization", 0)
    print(f"H1 (gap-spotting dominates): {dict(mode)}")
    print(f"   gap_spotting {gap}/{n} ({100*gap/n:.0f}%);  problematization {prob}/{n} "
          f"({100*prob/n:.0f}%)")
    at = Counter(r["assumption_targeted"] for r in frozen)
    print(f"   assumption_targeted: {dict(at)}")

    # --- H2: mode by year cut ---
    early = [r for r in frozen if by_slug[r["slug"]]["year"] < YEAR_CUT]
    late = [r for r in frozen if by_slug[r["slug"]]["year"] >= YEAR_CUT]
    def prob_share(group):
        if not group:
            return None
        return sum(1 for r in group if r["motivation_mode"] == "problematization") / len(group)
    def assum_share(group):
        if not group:
            return None
        return sum(1 for r in group if r["assumption_targeted"] == "yes") / len(group)
    es, ls = prob_share(early), prob_share(late)
    print(f"\nH2 (problematization rises): early (<{YEAR_CUT}) n={len(early)} "
          f"problematization {es:.0%}; late (>={YEAR_CUT}) n={len(late)} problematization {ls:.0%}")
    print(f"   assumption_targeted=yes share: early {assum_share(early):.0%}; late {assum_share(late):.0%}")

    # --- H3: citations-per-year by mode ---
    def cpy(r):
        c = by_slug[r["slug"]]["cites"] or 0
        elapsed = max(NOW - by_slug[r["slug"]]["year"], 0.5)
        return c / elapsed
    gap_cpy = [cpy(r) for r in frozen if r["motivation_mode"] == "gap_spotting"]
    prob_cpy = [cpy(r) for r in frozen if r["motivation_mode"] == "problematization"]
    u, p, z = _mannwhitney_u(prob_cpy, gap_cpy)
    print(f"\nH3 (problematizers cited more per year):")
    print(f"   gap_spotting   n={len(gap_cpy):2d}  mean cpy {sum(gap_cpy)/len(gap_cpy):5.2f}  "
          f"median {_median(gap_cpy):5.2f}")
    print(f"   problematization n={len(prob_cpy):2d}  mean cpy "
          f"{sum(prob_cpy)/len(prob_cpy):5.2f}  median {_median(prob_cpy):5.2f}")
    if u is not None:
        print(f"   Mann-Whitney U={u:.1f}, z={z:.2f}, p={p:.3f}")

    summary = {
        "n": n,
        "motivation_mode": dict(mode),
        "assumption_targeted": dict(at),
        "H2": {"year_cut": YEAR_CUT,
               "early_n": len(early), "early_problematization_share": es, "early_assum_yes": assum_share(early),
               "late_n": len(late), "late_problematization_share": ls, "late_assum_yes": assum_share(late)},
        "H3": {"gap_n": len(gap_cpy), "gap_mean_cpy": sum(gap_cpy)/len(gap_cpy), "gap_median_cpy": _median(gap_cpy),
               "prob_n": len(prob_cpy), "prob_mean_cpy": sum(prob_cpy)/len(prob_cpy), "prob_median_cpy": _median(prob_cpy),
               "mannwhitney_U": u, "z": z, "p": p},
    }
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print(f"\nwrote results/frozen.json, results/summary.json")


if __name__ == "__main__":
    main()
