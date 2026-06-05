#!/usr/bin/env python3
"""Reproduce-the-numbers gate.

Runs every check registered in ci/reproduce.json and confirms each one still produces the
numbers a published claim depends on. A check passes only if its command exits zero and its
stdout contains every string in `expect`. Any failure fails the job.

This is the mechanical first pass of the review described in PUBLISHING.md: before anyone argues
about what a result means, CI re-derives it from the committed script. A submission that reports
a number registers it here, so the number is checked on every pull request and can never silently
drift from the script that produced it.

Run:  python ci/reproduce.py            # all checks
      python ci/reproduce.py NAME ...   # only the named checks
"""

import json
import os
import subprocess
import sys
import time

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MANIFEST = os.path.join(REPO_ROOT, "ci", "reproduce.json")


def load_checks():
    with open(MANIFEST) as f:
        data = json.load(f)
    return data["checks"]


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
    checks = load_checks()
    if argv:
        wanted = set(argv)
        checks = [c for c in checks if c["name"] in wanted]
        unknown = wanted - {c["name"] for c in checks}
        if unknown:
            print(f"unknown check(s): {', '.join(sorted(unknown))}")
            return 2
    if not checks:
        print("no checks to run")
        return 1

    print(f"reproduce-the-numbers — {len(checks)} check(s)\n" + "=" * 72)
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
    print("all checks reproduced.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
