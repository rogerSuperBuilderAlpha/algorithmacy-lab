"""Build the coordination-form dataset with exact verdict labels and cheap features.

Each row is one coordination form: its construction, its cheap structural + dynamical features
(none of which computes Φ), and its exact IIT-4.0 verdict from the classifier. Forms at n <= 5 are
the training pool; n in {6,7,8} are the held-out size-extrapolation test. The build is checkpointed
-- rows are appended as computed and existing form_ids are skipped -- so a long run can be resumed
and analysis can proceed on a partial file.

Run (fast pilot, training pool only):
    ~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.build_dataset --max-n 5
Full study (adds the held-out n=6,7,8 test; hours of exact Φ):
    ~/iit-playground/venv-4.0/bin/python -m org_frontier.verdict_surrogate.build_dataset --max-n 8
"""

import argparse
import csv
import os
import sys
import time
import zlib

import numpy as np

from org_frontier.classifier.classifier import classify_rules
from org_frontier.corpus.population import enumerate_family
from . import forms as F

_HERE = os.path.dirname(__file__)
_RESULTS = os.path.join(_HERE, "results")
_DATASET = os.path.join(_RESULTS, "dataset.csv")

# Per-n counts of randomly sampled forms. Constructed forms (chains, conjunctions, back-channel
# variants) are added on top at every n. n=3 also gets the full 256 strict-mediation census.
RANDOM_COUNTS = {3: 60, 4: 300, 5: 250, 6: 70, 7: 6, 8: 0}
BACKCHANNEL_COUNTS = {3: 30, 4: 120, 5: 100, 6: 20, 7: 4, 8: 0}
TRAJ_LEN = 500


def constructed_forms(n):
    """Named forms whose verdict is known by construction, at party count n (n >= 3)."""
    out = []
    k = n - 2                                   # chain depth giving this n
    if k >= 1:
        rules, meta = F.chain(k)
        out.append((f"chain_n{n}", n, rules, {**meta, "expected": "triadic"}))
        out.append((f"chain_bc_n{n}", n, F.add_backchannel(rules, n, None),
                    {"construction": "chain", "has_backchannel": True, "expected": "dyadic?"}))
    rules, meta = F.all_required(n)
    out.append((f"allreq_n{n}", n, rules, {**meta, "expected": "triadic"}))
    out.append((f"allreq_bc_n{n}", n, F.add_backchannel(rules, n, None),
                {"construction": "all_required", "has_backchannel": True, "expected": "dyadic?"}))
    rules, meta = F.substitutable(n)
    out.append((f"subst_n{n}", n, rules, {**meta, "expected": "dyadic"}))
    return out


def iter_forms(max_n):
    """Yield (form_id, n, rules, meta) for every form to label, deterministically ordered."""
    for n in range(3, max_n + 1):
        # n=3 full census of the strict-mediation family (256 forms).
        if n == 3:
            for label, rules in enumerate_family():
                yield f"census_n3_{label}", 3, rules, {"construction": "census", "has_backchannel": False}
        rng = np.random.default_rng(1000 + n)
        for i in range(RANDOM_COUNTS.get(n, 0)):
            rules, meta = F.random_strict_mediation(n, rng)
            yield f"rand_n{n}_{i}", n, rules, meta
        rng_bc = np.random.default_rng(2000 + n)
        for i in range(BACKCHANNEL_COUNTS.get(n, 0)):
            rules, meta = F.random_with_backchannel(n, rng_bc)
            yield f"randbc_n{n}_{i}", n, rules, meta
        for fid, nn, rules, meta in constructed_forms(n):
            yield fid, nn, rules, meta


def _load_done():
    if not os.path.exists(_DATASET):
        return set(), []
    with open(_DATASET) as fh:
        rows = list(csv.DictReader(fh))
    return {r["form_id"] for r in rows}, rows


def main(max_n=5, traj_len=TRAJ_LEN):
    os.makedirs(_RESULTS, exist_ok=True)
    done, _ = _load_done()
    # `n` is carried once, as the first feature in F.FEATURE_KEYS.
    fieldnames = (["form_id", "construction", "has_backchannel", "split"]
                  + F.FEATURE_KEYS + ["phi_max", "n_states", "structure", "triadic"])
    new_file = not os.path.exists(_DATASET)
    fh = open(_DATASET, "a", newline="")
    writer = csv.DictWriter(fh, fieldnames=fieldnames)
    if new_file:
        writer.writeheader()

    todo = [x for x in iter_forms(max_n) if x[0] not in done]
    print(f"verdict_surrogate/build_dataset: {len(todo)} forms to label (max_n={max_n}, "
          f"{len(done)} already done).")
    start = time.time()
    for k, (fid, n, rules, meta) in enumerate(todo):
        feat_rng = np.random.default_rng(zlib.crc32(fid.encode()))   # stable across processes
        t0 = time.time()
        feats = F.cheap_features(rules, n, feat_rng, traj_len)
        v = classify_rules(rules)
        row = {
            "form_id": fid, "construction": meta["construction"],
            "has_backchannel": int(meta["has_backchannel"]),
            "split": "train" if n <= 5 else "test",
            "phi_max": f"{v.max_phi:.6f}", "n_states": v.n_states_evaluated,
            "structure": v.structure, "triadic": int(v.structure == "triadic"),
        }
        row.update({key: feats[key] for key in F.FEATURE_KEYS})
        writer.writerow(row)
        fh.flush()
        dt = time.time() - t0
        if n >= 6 or (k + 1) % 100 == 0:
            print(f"  [{k+1}/{len(todo)}] {fid:<22} n={n} {v.structure:<8} "
                  f"Φ={v.max_phi:.3f}  ({dt:.1f}s, elapsed {time.time()-start:.0f}s)")
            sys.stdout.flush()
    fh.close()
    print(f"Wrote {_DATASET}  ({time.time()-start:.0f}s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-n", type=int, default=5)
    ap.add_argument("--traj-len", type=int, default=TRAJ_LEN)
    args = ap.parse_args()
    main(args.max_n, args.traj_len)
