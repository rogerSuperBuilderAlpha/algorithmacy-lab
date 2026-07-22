"""Analysis for the systematicity_consciousness_reviews review: reliability + the three hypothesis tests.

    python -m org_frontier.reviews.systematicity_consciousness_reviews.run

Reads coding/ (independent coder JSONL) and literature/corpus.jsonl, writes results/frozen.json and
results/summary.json, and prints the per-hypothesis verdicts. Standard library only; uses the arm's
reusable reliability tooling and hand-rolled Pearson/Spearman (no third-party deps).
"""

import json
import math
import os

from org_frontier.reviews.lib import reliability

HERE = os.path.dirname(__file__)
PRACTICES = ["envisioning", "explicating", "executing", "evaluating",
             "encoding", "elaborating", "expositing"]


def _load_jsonl(path):
    return [json.loads(l) for l in open(path) if l.strip()] if os.path.exists(path) else []


def _rank(xs):
    order = sorted(range(len(xs)), key=lambda i: xs[i])
    ranks = [0.0] * len(xs)
    i = 0
    while i < len(xs):
        j = i
        while j + 1 < len(xs) and xs[order[j + 1]] == xs[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def _pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sx = sum((x - mx) ** 2 for x in xs)
    sy = sum((y - my) ** 2 for y in ys)
    if sx == 0 or sy == 0:
        return 0.0
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return cov / math.sqrt(sx * sy)


def _spearman(xs, ys):
    if len(xs) < 3:
        return None
    return _pearson(_rank(xs), _rank(ys))


def _p_from_r(r, n):
    """Two-sided p for a correlation via the t distribution; std-lib only (Numerical Recipes betai)."""
    if r is None or n < 4 or abs(r) >= 1.0:
        return None
    df = n - 2
    t = r * math.sqrt(df / (1 - r * r))
    return _betai(df / 2.0, 0.5, df / (df + t * t))


def _betacf(a, b, x):
    fpmin = 1e-30
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < fpmin:
        d = fpmin
    d = 1.0 / d
    h = d
    for m in range(1, 300):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < fpmin:
            d = fpmin
        c = 1.0 + aa / c
        if abs(c) < fpmin:
            c = fpmin
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1.0) < 1e-12:
            break
    return h


def _betai(a, b, x):
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    bt = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b) +
                  a * math.log(x) + b * math.log(1.0 - x))
    if x < (a + 1.0) / (a + b + 2.0):
        return bt * _betacf(a, b, x) / a
    return 1.0 - bt * _betacf(b, a, 1.0 - x) / b


def main():
    corpus = {r["slug"]: r for r in _load_jsonl(os.path.join(HERE, "literature", "corpus.jsonl"))}

    reliability.run(os.path.join(HERE, "coding"), "slug", PRACTICES, [],
                    out=os.path.join(HERE, "results", "frozen.json"))
    frozen = json.load(open(os.path.join(HERE, "results", "frozen.json")))

    counts, years, cites, per_practice = [], [], [], {p: 0 for p in PRACTICES}
    for r in frozen:
        c = sum(1 for p in PRACTICES if r.get(p) == "yes")
        counts.append(c)
        for p in PRACTICES:
            if r.get(p) == "yes":
                per_practice[p] += 1
        meta = corpus.get(r["slug"], {})
        years.append(meta.get("year"))
        cites.append(meta.get("cites"))

    n = len(counts)
    mean_c = sum(counts) / n if n else 0.0

    print("\n" + "=" * 72)
    # H1
    print(f"H1 (fewer than half the practices): mean practices/review = {mean_c:.2f} of 7 "
          f"({100*mean_c/7:.0f}%); threshold 3.5")
    print(f"   verdict: {'SUPPORTED' if mean_c < 3.5 else 'CHALLENGED'}")

    # per-practice adoption
    print("\n   per-practice adoption (share of reviews reporting):")
    for p in PRACTICES:
        print(f"     {p:12} {per_practice[p]:>3}/{n}  {100*per_practice[p]/n:>4.0f}%")

    # H2: practice count vs year
    yv = [(c, y) for c, y in zip(counts, years) if y is not None]
    ry = _pearson([c for c, _ in yv], [y for _, y in yv])
    rho_y = _spearman([c for c, _ in yv], [y for _, y in yv])
    py = _p_from_r(ry, len(yv))
    print(f"\nH2 (adoption rising): practice-count vs year  Pearson r = {ry:+.3f} "
          f"(p={py:.3f}), Spearman rho = {rho_y:+.3f}, n={len(yv)}")
    print(f"   verdict: {'SUPPORTED' if (ry or 0) > 0 and (py or 1) < 0.10 else ('QUALIFIED' if (ry or 0)>0 else 'CHALLENGED')}")

    # H3: practice count vs cites
    cv = [(c, ct) for c, ct in zip(counts, cites) if ct is not None]
    rho_c = _spearman([c for c, _ in cv], [ct for _, ct in cv])
    pc = _p_from_r(rho_c, len(cv))
    # confound: cites vs year
    yc = [(y, ct) for y, ct in zip(years, cites) if y is not None and ct is not None]
    rho_yc = _spearman([y for y, _ in yc], [ct for _, ct in yc])
    print(f"\nH3 (more practices, more cited): practice-count vs cites  Spearman rho = {rho_c:+.3f} "
          f"(p={pc:.3f}), n={len(cv)}")
    print(f"   confound  cites vs year  Spearman rho = {rho_yc:+.3f}")
    print(f"   verdict: {'SUPPORTED' if (rho_c or 0) > 0 and (pc or 1) < 0.10 else ('QUALIFIED' if (rho_c or 0)>0 else 'CHALLENGED')}")

    summary = {
        "n": n,
        "mean_practices": round(mean_c, 3),
        "practice_distribution": {str(k): counts.count(k) for k in range(8)},
        "per_practice_adoption": {p: per_practice[p] for p in PRACTICES},
        "per_practice_share": {p: round(per_practice[p] / n, 3) for p in PRACTICES},
        "H2_year": {"pearson_r": round(ry, 3) if ry is not None else None,
                    "pearson_p": round(py, 4) if py is not None else None,
                    "spearman_rho": round(rho_y, 3) if rho_y is not None else None, "n": len(yv)},
        "H3_cites": {"spearman_rho": round(rho_c, 3) if rho_c is not None else None,
                     "spearman_p": round(pc, 4) if pc is not None else None, "n": len(cv),
                     "confound_cites_year_rho": round(rho_yc, 3) if rho_yc is not None else None},
    }
    os.makedirs(os.path.join(HERE, "results"), exist_ok=True)
    json.dump(summary, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
    print(f"\nwrote results/frozen.json, results/summary.json  (N={n}, mean practices={mean_c:.2f})")


if __name__ == "__main__":
    main()
