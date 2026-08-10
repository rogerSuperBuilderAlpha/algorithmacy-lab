#!/usr/bin/env python3
"""Gate G4: everything a draft must pass before a human is asked to read it.

The v4 pipeline puts one optimization pass on the prose and then stops. That only
works if the mechanical faults are caught mechanically, so this runs after every
applied fix rather than once at the end -- the review record shows fixes installing
new faults ("the proposed fix adds an agentless passive -- the disease as cure"),
and a fix that is not re-checked is a fix on trust.

Four checks plus the ceiling and the disc markers:

  apparatus   notes and bibliography reconcile both directions, no placeholders
  carryover   no sentence shared with v1, v2, v3, or the v3 long draft
  bans        no construction a previous panel already cut
  film        the film is present often enough and never absent too long
  ceiling     body within the word limit
  disc        no unresolved [DISC:...] markers, or an explicit deferral

Usage:
    python3 v4/tools/run_gate.py chapter/chapter_v4.md
    python3 v4/tools/run_gate.py chapter/chapter_v4.md --allow-disc   # markers permitted
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CEILING = 5000
DISC = re.compile(r"\[DISC:[^\]]*\]")


def run(label, cmd):
    print("=" * 72)
    print(label)
    print("=" * 72)
    r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    if r.stderr.strip():
        sys.stderr.write(r.stderr)
    print()
    return r.returncode == 0


def body_words(path):
    raw = Path(path).read_text(encoding="utf-8")
    body = re.split(r"(?m)^##\s*Notes\s*$", raw)[0]
    body = re.sub(r"(?m)^#.*$", "", body)
    return len(re.findall(r"[A-Za-z][A-Za-z'’-]*", body))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--allow-disc", action="store_true",
                    help="permit unresolved [DISC:...] markers (pre-viewing drafts)")
    ap.add_argument("--ceiling", type=int, default=CEILING)
    args = ap.parse_args()

    draft = Path(args.draft)
    if not draft.is_absolute():
        draft = ROOT / draft
    if not draft.exists():
        sys.exit("draft not found: %s" % draft)
    rel = draft.relative_to(ROOT)

    results = {}
    results["apparatus"] = run("APPARATUS", ["python3", "check_apparatus.py", str(rel)])
    results["carryover"] = run("CARRYOVER", ["python3", "v4/tools/check_carryover.py", str(rel)])
    results["bans"] = run("BANS", ["python3", "v4/tools/check_bans.py", str(rel), "--quiet"])
    results["film"] = run("FILM", ["python3", "v4/tools/check_film.py", str(rel)])

    print("=" * 72)
    print("CEILING AND DISC MARKERS")
    print("=" * 72)
    n = body_words(draft)
    results["ceiling"] = n <= args.ceiling
    print("  body: %d words against a ceiling of %d  %s"
          % (n, args.ceiling, "ok" if results["ceiling"] else "OVER by %d" % (n - args.ceiling)))
    print("  the ceiling is the call's stated 3,000-5,000 range and remains unconfirmed;")
    print("  see v4/ASSUMPTIONS.md")

    markers = DISC.findall(draft.read_text(encoding="utf-8"))
    if markers:
        print("  %d unresolved disc markers: %s" % (len(markers), ", ".join(sorted(set(markers))[:8])))
        print("  each needs the Criterion disc; nothing here may be guessed")
        results["disc"] = args.allow_disc
    else:
        print("  no unresolved disc markers")
        results["disc"] = True
    print()

    print("=" * 72)
    width = max(len(k) for k in results)
    for k, ok in results.items():
        print("  %-*s %s" % (width, k, "pass" if ok else "FAIL"))
    print("=" * 72)
    failed = [k for k, ok in results.items() if not ok]
    if failed:
        print("G4 FAIL: %s" % ", ".join(failed))
        return 1
    print("G4 PASS -- ready for verification (phase 5)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
