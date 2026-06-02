"""Paper 3 — Stage-1 robustness battery for the calibration anchor.

Extends `anchor_chicago.py` with the empirical-genre robustness checks the quantitative paper requires:
effect size (trip-level), temporal stability, a within-stratum (Simpson's-paradox) check, alternative
aggregations, and a power note. Pulls a large shared-authorized sample live from the City of Chicago
Socrata API (resource m6dm-c72p) and computes the battery. Numbers of record are in `results.md`.

Model: pool size k -> Φ = k + 1 (driver + k riders + platform, strict higher-order mediation; computed
in typology_phi.py / pool_form). Outcome = friction (sec/mi). The model predicts friction rises with Φ.

Run:  ~/iit-playground/venv-4.0/bin/python dissertation/paper3_baseline/robustness_anchor.py
(needs network; the harness sandbox must allow the read-only GET.)
"""

import json
import urllib.parse
import urllib.request
from collections import defaultdict

import numpy as np

RESOURCE = "https://data.cityofchicago.org/resource/m6dm-c72p.json"
QUERY = {
    "$select": "trips_pooled,trip_seconds,trip_miles,trip_start_timestamp,pickup_community_area",
    "$where": "shared_trip_authorized=true",
    "$limit": "200000",   # no $order/$offset: those force a full-table sort/scan and time out
}
PHI = lambda k: k + 1.0


def fetch():
    url = f"{RESOURCE}?{urllib.parse.urlencode(QUERY)}"
    with urllib.request.urlopen(url, timeout=120) as r:
        return json.load(r)


def clean(rows):
    out = []
    for r in rows:
        try:
            k = int(r["trips_pooled"]); s = float(r["trip_seconds"]); m = float(r["trip_miles"])
        except (KeyError, TypeError, ValueError):
            continue
        if not (0.5 <= m <= 60 and 120 <= s <= 7200):
            continue
        pace = s / m
        if not (20 <= pace <= 1200) or not (1 <= k <= 4):
            continue
        out.append(dict(k=k, sec=s, mi=m, pace=pace, ts=r["trip_start_timestamp"],
                        area=r.get("pickup_community_area"), phi=PHI(k)))
    return out


def agg_pace_by_k(rows):
    b = defaultdict(lambda: [0.0, 0.0, 0])
    for d in rows:
        b[d["k"]][0] += d["sec"]; b[d["k"]][1] += d["mi"]; b[d["k"]][2] += 1
    return {k: (v[0] / v[1], v[2]) for k, v in b.items()}


def corr_4pt(rows):
    fb = agg_pace_by_k(rows); ks = sorted(fb)
    return float(np.corrcoef([PHI(k) for k in ks], [fb[k][0] for k in ks])[0, 1])


def triplevel(rows):
    phi = np.array([d["phi"] for d in rows]); pace = np.array([d["pace"] for d in rows])
    r = float(np.corrcoef(phi, pace)[0, 1]); sl = float(np.polyfit(phi, pace, 1)[0])
    return r, r * r, sl


def battery(rows):
    print(f"clean trips: {len(rows):,}\n")
    r4 = corr_4pt(rows); r, r2, sl = triplevel(rows)
    fb = agg_pace_by_k(rows); ks = sorted(fb)
    print("(1) OVERALL")
    print("    friction by pool: " + " ".join(f"k{k}:{fb[k][0]:.0f}" for k in ks))
    print(f"    4-point aggregate r = {r4:+.3f};  trip-level r={r:+.3f} R²={r2:.3f} slope={sl:+.1f} sec/mi per +1Φ")

    ts = sorted(d["ts"] for d in rows); med = ts[len(ts) // 2]
    early = [d for d in rows if d["ts"] <= med]; late = [d for d in rows if d["ts"] > med]
    print("(2) TEMPORAL STABILITY (split at median date)")
    for nm, sub in [("early", early), ("late", late)]:
        rr, r2s, sls = triplevel(sub)
        print(f"    {nm}: 4pt r={corr_4pt(sub):+.3f} | trip-level r={rr:+.3f} R²={r2s:.3f} slope={sls:+.1f}")

    print("(3) WITHIN-STRATUM (Simpson's) — friction monotone in pool size within area?")
    by = defaultdict(list)
    for d in rows:
        if d["area"]:
            by[d["area"]].append(d)
    top = sorted(by, key=lambda a: -len(by[a]))[:8]; mono = 0
    for a in top:
        fb2 = agg_pace_by_k(by[a]); ks2 = sorted(fb2); p = [fb2[k][0] for k in ks2]
        ok = len(ks2) >= 3 and all(p[i] <= p[i + 1] for i in range(len(p) - 1)); mono += ok
        print(f"    area {a}: " + " ".join(f"k{k}:{fb2[k][0]:.0f}" for k in ks2) + ("  MONOTONE" if ok else ""))
    print(f"    monotone within {mono}/{len(top)} top areas")

    print("(4) ALTERNATIVE AGGREGATION of friction")
    phis = np.array([PHI(k) for k in ks])
    for nm, arr in [("sum/sum", [fb[k][0] for k in ks]),
                    ("mean pace", [np.mean([d["pace"] for d in rows if d["k"] == k]) for k in ks]),
                    ("median pace", [np.median([d["pace"] for d in rows if d["k"] == k]) for k in ks])]:
        print(f"    {nm:12s}: r(Φ,·) = {np.corrcoef(phis, arr)[0, 1]:+.3f}")

    tot = len(rows); cnt = {k: sum(1 for d in rows if d["k"] == k) for k in ks}
    shares = np.array([100 * cnt[k] / tot for k in ks])
    print("(5) ACHIEVEMENT + power")
    print(f"    share% by pool: " + " ".join(f"k{k}:{100*cnt[k]/tot:.1f}" for k in ks))
    print(f"    log(share)~Φ slope = {np.polyfit(phis, np.log(shares), 1)[0]:+.3f}; r(Φ,share)={np.corrcoef(phis,shares)[0,1]:+.3f}")
    print(f"    match success P(pooled>=2) = {sum(cnt[k] for k in ks if k>=2)/tot:.3f}")
    print(f"    power: N={tot:,} -> significance trivial; report R²={r2:.3f} as the effect size, not p.")


if __name__ == "__main__":
    print("=" * 80)
    print("PAPER 3 — Stage-1 robustness battery (Chicago rideshare pooling anchor)")
    print("=" * 80)
    battery(clean(fetch()))
