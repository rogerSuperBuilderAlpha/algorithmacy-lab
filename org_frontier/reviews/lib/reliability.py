"""Intercoder reliability for a systematic literature review.

Takes N coder files (one JSON object per source, keyed by a source id), and reports, per coded
variable, the agreement among coders and an adjudicated majority-vote dataset. This is the step that
turns a set of judgment calls into a defensible measurement: a review that reports Fleiss' kappa has
answered the "one reader coded it" objection that single-coder reviews cannot.

Two kinds of variable are handled:

  * categorical (a single label per source) — reported with Fleiss' kappa and mean pairwise percent
    agreement. Landis & Koch read kappa > 0.80 as "almost perfect", 0.61-0.80 "substantial".
  * set-valued (a list of labels per source, e.g. which dimensions a source develops) — reported
    with mean pairwise Jaccard overlap, since kappa is not defined on sets.

Adjudication is a plain majority vote: the modal label for categorical variables, and, for
set-valued variables, every element chosen by at least ceil(N/2) coders.

Coder files are JSONL (one object per line) or a JSON list. Each object needs an id field (default
"slug") and the variables to score. Example, three coders each producing lines like:

    {"slug": "smith2020", "substrate": "social", "claim_type": "assumption", "cells": ["mechanism"]}

Run:

    python -m org_frontier.reviews.lib.reliability coding/ --id slug \\
        --categorical substrate,claim_type --set cells --out results/frozen.json

Prints a reliability table and writes the adjudicated dataset. Standard library only.
"""

import argparse
import glob
import itertools
import json
import math
import os
from collections import Counter


def load_coders(path):
    """Return {coder_name: {source_id: record}} from a directory or list of JSONL/JSON files."""
    files = []
    if os.path.isdir(path):
        files = sorted(glob.glob(os.path.join(path, "*.jsonl")) + glob.glob(os.path.join(path, "*.json")))
    else:
        files = [path]
    coders = {}
    for f in files:
        name = os.path.splitext(os.path.basename(f))[0]
        text = open(f).read().strip()
        records = []
        if text.startswith("["):
            records = json.loads(text)
        else:
            for line in text.splitlines():
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        coders[name] = records
    return coders


def _index(coders, id_field):
    """Reshape to {coder: {source_id: record}} and return the source ids common to all coders."""
    indexed = {}
    for name, records in coders.items():
        indexed[name] = {r[id_field]: r for r in records if id_field in r}
    common = set.intersection(*[set(d) for d in indexed.values()]) if indexed else set()
    return indexed, sorted(common)


def fleiss_kappa(indexed, ids, var, missing="na"):
    """Fleiss' kappa and mean pairwise percent agreement for a categorical variable across coders."""
    names = sorted(indexed)
    k = len(names)
    if k < 2 or not ids:
        return None, None
    cats = sorted({indexed[n][s].get(var, missing) for n in names for s in ids})
    cat_total = Counter()
    p_items = []
    for s in ids:
        counts = Counter(indexed[n][s].get(var, missing) for n in names)
        for c in cats:
            cat_total[c] += counts.get(c, 0)
        p_items.append((sum(v * v for v in counts.values()) - k) / (k * (k - 1)))
    p_bar = sum(p_items) / len(ids)
    pj = [cat_total[c] / (len(ids) * k) for c in cats]
    p_e = sum(p * p for p in pj)
    kappa = (p_bar - p_e) / (1 - p_e) if (1 - p_e) > 1e-12 else 1.0
    agrees = []
    for a, b in itertools.combinations(names, 2):
        agrees.append(sum(1 for s in ids if indexed[a][s].get(var) == indexed[b][s].get(var)) / len(ids))
    return kappa, sum(agrees) / len(agrees)


def mean_jaccard(indexed, ids, var):
    """Mean pairwise Jaccard overlap for a set-valued variable across coders."""
    names = sorted(indexed)
    jac = []
    for s in ids:
        for a, b in itertools.combinations(names, 2):
            A = set(indexed[a][s].get(var, []) or [])
            B = set(indexed[b][s].get(var, []) or [])
            jac.append(len(A & B) / len(A | B) if (A or B) else 1.0)
    return sum(jac) / len(jac) if jac else None


def adjudicate(indexed, ids, id_field, categorical, set_valued, missing="na"):
    """Majority-vote frozen dataset: modal label per categorical var; elements chosen by >= ceil(N/2)
    coders per set var."""
    names = sorted(indexed)
    threshold = math.ceil(len(names) / 2)
    frozen = []
    for s in ids:
        rec = {id_field: s}
        for var in categorical:
            rec[var] = Counter(indexed[n][s].get(var, missing) for n in names).most_common(1)[0][0]
        for var in set_valued:
            tally = Counter()
            for n in names:
                for c in indexed[n][s].get(var, []) or []:
                    tally[c] += 1
            rec[var] = sorted([c for c, v in tally.items() if v >= threshold])
        frozen.append(rec)
    return frozen


def _label(kappa):
    if kappa is None:
        return ""
    if kappa > 0.80:
        return "almost perfect"
    if kappa > 0.60:
        return "substantial"
    if kappa > 0.40:
        return "moderate"
    if kappa > 0.20:
        return "fair"
    return "slight"


def run(path, id_field, categorical, set_valued, out=None):
    coders = load_coders(path)
    indexed, ids = _index(coders, id_field)
    print(f"coders: {sorted(indexed)}  |  common sources: {len(ids)}")
    print("\nintercoder reliability")
    print(f"  {'variable':16}{'Fleiss kappa':>14}{'agreement':>12}   interpretation")
    for var in categorical:
        kappa, agr = fleiss_kappa(indexed, ids, var)
        if kappa is not None:
            print(f"  {var:16}{kappa:>14.3f}{agr:>11.1%}   {_label(kappa)}")
    for var in set_valued:
        jac = mean_jaccard(indexed, ids, var)
        if jac is not None:
            print(f"  {var:16}{'(set)':>14}{jac:>11.3f}   mean Jaccard")
    if out:
        frozen = adjudicate(indexed, ids, id_field, categorical, set_valued)
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        json.dump(frozen, open(out, "w"), indent=0)
        print(f"\nadjudicated (majority-vote) dataset: {len(frozen)} sources -> {out}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", help="directory of coder JSONL files (or one file)")
    ap.add_argument("--id", default="slug", help="the source-id field (default: slug)")
    ap.add_argument("--categorical", default="", help="comma-separated categorical variable names")
    ap.add_argument("--set", dest="set_valued", default="", help="comma-separated set-valued variable names")
    ap.add_argument("--out", default=None, help="write the adjudicated majority-vote dataset here (JSON)")
    a = ap.parse_args()
    cat = [v for v in a.categorical.split(",") if v]
    setv = [v for v in a.set_valued.split(",") if v]
    run(a.path, a.id, cat, setv, a.out)


if __name__ == "__main__":
    main()
