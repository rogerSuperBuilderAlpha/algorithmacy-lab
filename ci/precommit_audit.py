#!/usr/bin/env python3
"""Pre-commitment audit: were the hypotheses committed before the results?

The second pass of the review in PUBLISHING.md. For every question directory a commit range touches,
this finds the first commit that adds `hypotheses.md` and the first commit that adds `FINDINGS.md` or
anything under `results/`, and reports whether the hypotheses came first. It reads the git history of
the range only, so it works on a pull request's own commits even when the published record has been
squashed or the clone is shallow.

Run on a pull request from the repo root:

    python ci/precommit_audit.py origin/contrib..HEAD
    python ci/precommit_audit.py origin/contrib..HEAD --strict   # exit 1 on any violation

A directory whose hypotheses and results first appear in the same commit is reported as
`same-commit`: the order is not auditable from history and the reviewer has to ask.
"""

import argparse
import subprocess
import sys
from collections import defaultdict

RESULT_MARKERS = ("FINDINGS.md", "results/")


def _is_result(rest: str) -> bool:
    """`FINDINGS.md`, or anything under a `results/` directory at any depth of the question dir."""
    return rest.startswith(RESULT_MARKERS) or "/results/" in rest


def _commits(rng: str) -> list:
    """Commits in the range, oldest first, with the files each one adds."""
    out = subprocess.run(
        ["git", "log", "--reverse", "--format=%H %ad", "--date=short", "--name-only",
         "--diff-filter=A", rng],
        capture_output=True, text=True, check=True,
    ).stdout
    commits, cur = [], None
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) == 2 and len(parts[0]) == 40 and parts[1].count("-") == 2:
            cur = {"sha": parts[0], "date": parts[1], "files": []}
            commits.append(cur)
        elif cur is not None:
            cur["files"].append(line.strip())
    return commits


def audit(rng: str) -> list:
    first_hyp, first_res = {}, {}
    for c in _commits(rng):
        for f in c["files"]:
            if "/questions/" not in f and "/studies/" not in f:
                continue
            parts = f.split("/")
            try:
                i = parts.index("questions") if "questions" in parts else parts.index("studies")
            except ValueError:
                continue
            if len(parts) < i + 3:
                continue
            d = "/".join(parts[: i + 2])
            rest = "/".join(parts[i + 2:])
            if rest == "hypotheses.md" and d not in first_hyp:
                first_hyp[d] = c
            if _is_result(rest) and d not in first_res:
                first_res[d] = c
    rows = []
    for d in sorted(set(first_hyp) | set(first_res)):
        h, r = first_hyp.get(d), first_res.get(d)
        if h and not r:
            verdict = "hypotheses-only"
        elif r and not h:
            verdict = "results-without-hypotheses"
        elif h["sha"] == r["sha"]:
            verdict = "same-commit"
        else:
            # The range is oldest-first, so compare positions, not dates.
            verdict = "ok" if _pos(h, rng) < _pos(r, rng) else "results-first"
        rows.append((d, verdict, h, r))
    return rows


_POS = {}


def _pos(c: dict, rng: str) -> int:
    if rng not in _POS:
        _POS[rng] = {x["sha"]: i for i, x in enumerate(_commits(rng))}
    return _POS[rng][c["sha"]]


def main(argv) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("range", help="git commit range, e.g. origin/contrib..HEAD")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero on results-first, results-without-hypotheses, or same-commit")
    args = ap.parse_args(argv)
    rows = audit(args.range)
    if not rows:
        print(f"pre-commitment audit ({args.range}) — no question or study directories touched.")
        return 0
    print(f"pre-commitment audit ({args.range}) — {len(rows)} director{'y' if len(rows) == 1 else 'ies'}")
    print("=" * 72)
    bad = 0
    for d, verdict, h, r in rows:
        hs = f"hypotheses {h['sha'][:8]} {h['date']}" if h else "hypotheses —"
        rs = f"results {r['sha'][:8]} {r['date']}" if r else "results —"
        flag = "OK  " if verdict in ("ok", "hypotheses-only") else "WARN"
        bad += flag == "WARN"
        print(f"  {flag}  {verdict:<28} {d}\n        {hs}; {rs}")
    print("=" * 72)
    if bad:
        print(f"{bad} director{'y' if bad == 1 else 'ies'} where the order is wrong or not auditable; "
              "the reviewer asks the author.")
        return 1 if args.strict else 0
    print("hypotheses precede results everywhere the range touches.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
