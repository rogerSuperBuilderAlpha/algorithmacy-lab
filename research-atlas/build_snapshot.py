#!/usr/bin/env python3
"""Bind the atlas indexes to their exact Git blob hashes."""

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "research-atlas" / "snapshot.json"
INDEXES = ("catalog.json", "research-atlas/cards.json")


def git_blob(path):
    data = (ROOT / path).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def committed_blob(revision, path):
    return subprocess.check_output(
        ["git", "rev-parse", f"{revision}:{path}"], cwd=ROOT, text=True
    ).strip()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if snapshot.json is stale")
    args = parser.parse_args()
    revision = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    indexes = {path: git_blob(path) for path in INDEXES}
    content = json.dumps({"revision": revision, "indexes": indexes}, indent=1) + "\n"
    if args.check:
        try:
            saved = json.loads(OUTPUT.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            saved = {}
        saved_revision = saved.get("revision", "")
        try:
            committed = {path: committed_blob(saved_revision, path) for path in INDEXES}
        except subprocess.CalledProcessError:
            committed = {}
        if saved.get("indexes") != indexes or committed != indexes:
            print("research-atlas/snapshot.json is stale — run research-atlas/build_snapshot.py")
            return 1
        print("research-atlas/snapshot.json is up to date.")
    else:
        if any(committed_blob(revision, path) != blob for path, blob in indexes.items()):
            print("Commit both indexes before building the atlas snapshot.")
            return 1
        OUTPUT.write_text(content, encoding="utf-8")
        print("Wrote research-atlas/snapshot.json.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
