#!/usr/bin/env python3
"""Reproduce-the-numbers gate.

Confirms that registered numbers still reproduce from their committed scripts. A check passes only
if its command exits zero and its stdout contains every string in `expect`. Any failure fails the job.

This is the mechanical first pass of the review in PUBLISHING.md: before anyone argues about what a
result means, CI re-derives it from the script. A submission that reports a number registers it here,
so the number can never silently drift from the script that produced it.

As the manifest grows, re-running every check on every pull request stops being feasible (exact Φ is
expensive). So a pull request reproduces only the numbers it could have affected — the instrument
control plus the studies whose files it changed — while the full manifest is reproduced nightly.

Run:  python ci/reproduce.py                  # all checks (the nightly / full job)
      python ci/reproduce.py --changed-file F  # core checks + checks for studies whose files are
                                               #   listed in F; slow checks are skipped (nightly-only)
      python ci/reproduce.py NAME ...          # only the named checks

Manifest entries may set:
  "core": true   always run, including in --changed-file mode (the instrument control)
  "slow": true   skipped in --changed-file mode; reproduced only by the full / nightly job
"""

import argparse
import json
import os
import subprocess
import sys
import time

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MANIFEST = os.path.join(REPO_ROOT, "ci", "reproduce.json")

# A change to any of these can move numbers anywhere, so it triggers the full (non-slow) set even in
# --changed-file mode: the shared instrument, the corpus, the probe library, and the gate itself.
SHARED_PREFIXES = (
    "org_frontier/classifier/",
    "org_frontier/corpus/",
    "org_frontier/probes/lib.py",
    "org_frontier/probes/_info.py",
    "foundations/proxy_audit/",
    "ci/reproduce.py",
)
# Note: ci/reproduce.json (the manifest) is deliberately NOT a shared-infra trigger. Adding a study's
# checks should run only that study's checks (selected by its changed dir) plus core, not the whole
# manifest. Modifications to an existing check's expected value are caught by the nightly full run.


def load_checks():
    with open(MANIFEST) as f:
        return json.load(f)["checks"]


def study_dir_of(check):
    """The package directory a check's command runs from, e.g.
    'python -m org_frontier.questions.q45_x.probe_y' -> 'org_frontier/questions/q45_x'."""
    toks = check["cmd"].split()
    if "-m" in toks:
        module = toks[toks.index("-m") + 1]
        return "/".join(module.split(".")[:-1])
    return None


def select_changed(checks, changed_paths):
    """Core checks always; on a shared-infra change, every non-slow check; otherwise the non-slow
    checks for studies whose directory contains a changed file."""
    changed = [p for p in (s.strip() for s in changed_paths) if p]
    shared = any(p.startswith(SHARED_PREFIXES) for p in changed)
    selected = []
    for c in checks:
        if c.get("slow"):
            continue
        if c.get("core") or shared:
            selected.append(c)
            continue
        d = study_dir_of(c)
        if d and any(p == d or p.startswith(d + "/") for p in changed):
            selected.append(c)
    return selected


def run_check(check):
    """Return (passed, detail). A check passes if the command exits 0 and stdout holds every
    expected string."""
    cmd = check["cmd"].split()
    if cmd and cmd[0] == "python":
        cmd[0] = sys.executable  # use the job's interpreter, not whatever 'python' resolves to
    env = dict(os.environ, PYPHI_WELCOME_OFF="true", PYTHONUNBUFFERED="1")
    timeout = check.get("timeout", 600)
    try:
        proc = subprocess.run(
            cmd, cwd=REPO_ROOT, env=env, capture_output=True, text=True, timeout=timeout
        )
    except subprocess.TimeoutExpired:
        return False, f"timed out after {timeout}s"
    out = proc.stdout + proc.stderr
    if proc.returncode != 0:
        tail = "\n".join(out.strip().splitlines()[-8:])
        return False, f"exit {proc.returncode}\n{tail}"
    missing = [s for s in check.get("expect", []) if s not in out]
    if missing:
        return False, "missing expected string(s): " + "; ".join(repr(m) for m in missing)
    return True, "ok"


def main(argv):
    ap = argparse.ArgumentParser(description="Reproduce registered numbers from their scripts.")
    ap.add_argument("--changed-file", help="file of changed paths; run core + touched-study checks")
    ap.add_argument("names", nargs="*", help="run only these named checks")
    args = ap.parse_args(argv)

    checks = load_checks()
    if args.changed_file:
        with open(args.changed_file) as f:
            checks = select_changed(checks, f.read().splitlines())
        label = "changed-study"
    elif args.names:
        wanted = set(args.names)
        unknown = wanted - {c["name"] for c in checks}
        if unknown:
            print(f"unknown check(s): {', '.join(sorted(unknown))}")
            return 2
        checks = [c for c in checks if c["name"] in wanted]
        label = "named"
    else:
        label = "full"

    if not checks:
        print("reproduce-the-numbers — no checks selected; nothing to reproduce.")
        return 0

    print(f"reproduce-the-numbers ({label}) — {len(checks)} check(s)\n" + "=" * 72)
    failures = 0
    for c in checks:
        t0 = time.monotonic()
        passed, detail = run_check(c)
        dt = time.monotonic() - t0
        mark = "PASS" if passed else "FAIL"
        failures += not passed
        print(f"  {mark}  {c['name']:<34} {dt:6.1f}s   {c.get('source', '')}")
        if not passed:
            for line in detail.splitlines():
                print(f"          {line}")
    print("=" * 72)
    if failures:
        print(f"{failures} check(s) failed — a published number did not reproduce.")
        return 1
    print("all selected checks reproduced.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
