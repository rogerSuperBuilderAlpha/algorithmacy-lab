#!/usr/bin/env python3
"""Reproduce every number the proposal cites, from the code in this repository.

A check passes only if its command exits zero and its output contains every expected string.

    python reproduce.py            # all checks
    python reproduce.py --fast     # skip the slower checks (the proxy study)
    python reproduce.py NAME ...   # only the named checks
"""

import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    with open(os.path.join(ROOT, "reproduce.json"), encoding="utf-8") as f:
        checks = json.load(f)["checks"]
    fast = "--fast" in argv
    names = [a for a in argv if not a.startswith("--")]
    if names:
        checks = [c for c in checks if c["name"] in names]
    elif fast:
        checks = [c for c in checks if not c.get("slow")]
    env = dict(os.environ, PYPHI_WELCOME_OFF="yes")
    failed = 0
    for c in checks:
        t0 = time.time()
        p = subprocess.run([sys.executable] + c["cmd"].split()[1:], cwd=ROOT, env=env,
                           capture_output=True, text=True, timeout=c.get("timeout", 600))
        out = p.stdout + p.stderr
        missing = [e for e in c["expect"] if e not in out]
        ok = p.returncode in c.get("ok_codes", [0]) and not missing
        failed += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {c['name']:<34} {time.time() - t0:6.1f}s   {c['what']}")
        for m in missing:
            print(f"        missing: {m!r}")
        if p.returncode not in c.get("ok_codes", [0]):
            print(f"        exit code {p.returncode}")
    print(f"\n{len(checks) - failed}/{len(checks)} checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
