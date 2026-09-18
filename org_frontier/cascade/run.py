"""CLI: run the lab-default margin cascade on a residual-style panel CSV.

Examples
--------
  python -m org_frontier.cascade.run \\
    --panel org_frontier/studies/holistic_residual_n4_unconstrained/results/residual_panel_n4_unconstrained.csv

  python -m org_frontier.cascade.run --panel path/to/panel.csv --B 0.10 --smoke
"""

from __future__ import annotations

import argparse
import csv
import os
import sys

import numpy as np

from .core import DEFAULT_B, DEFAULT_FEATURES, margin_cascade
from .defaults import TAU_STAR_N4_B10


def load_panel_csv(path, features=DEFAULT_FEATURES, label_col="triadic"):
    rows = list(csv.DictReader(open(path)))
    missing = [f for f in features if f not in rows[0]]
    if missing:
        raise SystemExit(f"panel missing feature columns: {missing}")
    if label_col not in rows[0]:
        raise SystemExit(f"panel missing label column {label_col!r}")
    X = np.array([[float(r[f]) for f in features] for r in rows])
    y = np.array([int(r[label_col]) for r in rows])
    return X, y


def main(argv=None):
    p = argparse.ArgumentParser(
        description=(
            "Margin cascade: Probe-131 cheap RF screen; exact Φ on top-B% "
            "uncertain forms (lab default B=0.10, recomputed per panel)."
        )
    )
    p.add_argument(
        "--panel",
        required=True,
        help="CSV with Probe-131 features + triadic label (exact Φ verdict)",
    )
    p.add_argument(
        "--B",
        type=float,
        default=DEFAULT_B,
        help=f"exact-Φ budget fraction (default {DEFAULT_B})",
    )
    p.add_argument(
        "--label-col",
        default="triadic",
        help="exact binary label column (default: triadic)",
    )
    p.add_argument(
        "--smoke",
        action="store_true",
        help="assert n4 unc control numbers when panel is that residual panel",
    )
    p.add_argument(
        "--write-mask",
        default=None,
        help="optional path to write per-row call_mask + preds CSV",
    )
    args = p.parse_args(argv)

    X, y = load_panel_csv(args.panel, label_col=args.label_col)
    result = margin_cascade(X, y, B=args.B)

    print("MARGIN CASCADE — lab default top-B% selective exact Φ")
    print("=" * 72)
    print(f"  panel:     {args.panel}")
    print(f"  N:         {result.n}   triadic={result.n_tri}")
    print(f"  B:         {args.B}  (default {DEFAULT_B})")
    print(f"  rule:      top-B% by OOF |p−0.5| (recomputed per panel)")
    print(f"  note:      do not freeze τ; τ*(n4,B=10%)={TAU_STAR_N4_B10} is prose-only")
    print("-" * 72)
    for line in result.summary_lines():
        print(line)
    print(
        f"  delta FN|tri (cheap − cascade): "
        f"{100 * (result.always_cheap_fn_among_tri - result.fn_among_tri):+.1f} pp"
    )
    print("=" * 72)

    if args.write_mask:
        os.makedirs(os.path.dirname(os.path.abspath(args.write_mask)) or ".", exist_ok=True)
        with open(args.write_mask, "w", newline="") as fh:
            w = csv.DictWriter(
                fh,
                fieldnames=["idx", "proba", "cheap_pred", "call_exact", "cascade_pred", "y"],
            )
            w.writeheader()
            for i in range(result.n):
                w.writerow({
                    "idx": i,
                    "proba": f"{result.proba[i]:.6f}",
                    "cheap_pred": int(result.cheap_pred[i]),
                    "call_exact": int(result.call_mask[i]),
                    "cascade_pred": int(result.pred[i]),
                    "y": int(result.y_exact[i]),
                })
        print(f"  wrote {args.write_mask}")

    if args.smoke:
        # Control: n4 unc residual panel must reproduce cascade@10% from the study.
        base = os.path.basename(os.path.abspath(args.panel))
        if base != "residual_panel_n4_unconstrained.csv":
            raise SystemExit(
                f"--smoke expects residual_panel_n4_unconstrained.csv, got {base}"
            )
        if abs(args.B - 0.10) > 1e-12:
            raise SystemExit("--smoke expects --B 0.10")
        cheap_miss = int((result.cheap_pred != result.y_exact).sum())
        cheap_fn = int(((result.cheap_pred == 0) & (result.y_exact == 1)).sum())
        print("SMOKE CONTROL")
        print(f"  always-cheap miss/FN: {cheap_miss}/{cheap_fn}  "
              f"{'PASS' if cheap_miss == 75 and cheap_fn == 30 else 'FAIL'}")
        print(f"  cascade@10% miss/FN:  {result.n_miss}/{result.fn}  "
              f"{'PASS' if result.n_miss == 32 and result.fn == 11 else 'FAIL'}")
        print(f"  exact calls:          {result.n_exact}  "
              f"{'PASS' if result.n_exact == 100 else 'FAIL'}")
        if not (cheap_miss == 75 and cheap_fn == 30
                and result.n_miss == 32 and result.fn == 11
                and result.n_exact == 100):
            raise SystemExit("SMOKE FAIL")
        print("  smoke: PASS")

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
